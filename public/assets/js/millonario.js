/**
 * millonario.js — Motor del juego "¿Quién quiere ser millonario?" (Ecoudea)
 *
 * 100% estático client-side. Sin globals sueltos: la ÚNICA API pública es
 * `window.MQ`. La lógica pura vive en `MQ.core` (testeable en Node sin DOM);
 * el DOM se toca solo desde los handlers `on*` y los `render*`, nunca desde
 * las transiciones.
 *
 * Máquina de estados (rejilla en MQ.core.MACHINE):
 *   intro → playing ; playing → feedback | paused ;
 *   feedback → playing | gameover ; paused → playing | gameover ;
 *   gameover → intro.
 */
(function () {
  'use strict';

  if (window.MQ) return; // anti doble carga (view transitions / SW)

  /* ═══════════════════════════════════════════════════════════════════
     NÚCLEO (puro, sin DOM) — window.MQ.core
     ═══════════════════════════════════════════════════════════════════ */
  var core = {};

  /**
   * Distribución de N niveles en 5 dificultades: buckets casi iguales, los
   * sobrantes (total % 5) van a las primeras dificultades. N=15→[3,3,3,3,3]
   * (identico al esquema 1-3/4-6/…/13-15 original). N=12→[3,3,2,2,2].
   */
  core.levelSizes = function (total) {
    var base = Math.floor(total / 5);
    var rem = total - base * 5;
    var sizes = [];
    for (var i = 0; i < 5; i++) sizes.push(i < rem ? base + 1 : base);
    return sizes;
  };

  /** Dificultad (1..5) de la pregunta del nivel (1-based) en una partida de `total` niveles. */
  core.difficultyForLevel = function (level, total) {
    var sizes = core.levelSizes(total || 15);
    var acc = 0;
    for (var d = 0; d < sizes.length; d++) {
      acc += sizes[d];
      if (level <= acc) return d + 1;
    }
    return 5;
  };

  /** Último refugio seguro ya superado con `solved` niveles confirmados; 0 si ninguno. */
  core.keptLevel = function (solved, safeHavens) {
    var havens = (safeHavens || []).filter(function (h) { return h <= solved; });
    return havens.length ? Math.max.apply(null, havens) : 0;
  };

  /** Premio (Ecopuntos) del nivel `level` (1-based) con la escalera `prizes`. */
  core.prizeAmount = function (level, prizes) {
    if (level < 1) return 0;
    return prizes[Math.min(level, prizes.length) - 1] || 0;
  };

  /** Fisher–Yates no destructivo. */
  core.shuffle = function (arr) {
    var out = Array.from(arr);
    for (var i = out.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = out[i]; out[i] = out[j]; out[j] = t;
    }
    return out;
  };

  /**
   * Selección de la partida: 1 pregunta por nivel 1..questionsPerGame con la
   * dificultad que toque, sin repetir ids. Devuelve null si el banco no alcanza.
   */
  core.pickQuestions = function (bank) {
    var total = (bank.config && bank.config.questionsPerGame) || 15;
    var byDifficulty = { 1: [], 2: [], 3: [], 4: [], 5: [] };
    bank.questions.forEach(function (q) {
      if (byDifficulty[q.difficulty]) byDifficulty[q.difficulty].push(q);
    });
    Object.keys(byDifficulty).forEach(function (k) {
      byDifficulty[k] = core.shuffle(byDifficulty[k]);
    });
    var picked = [];
    for (var level = 1; level <= total; level++) {
      var d = core.difficultyForLevel(level, total);
      if (!byDifficulty[d] || byDifficulty[d].length === 0) return null;
      picked.push(byDifficulty[d].pop());
    }
    return picked;
  };

  /** Baraja de opciones preservando la correcta (exactamente 1 isCorrect). */
  core.shuffledOptions = function (q) {
    return core.shuffle([0, 1, 2, 3]).map(function (origIdx) {
      return { text: q.options[origIdx], isCorrect: origIdx === q.correct, originalIdx: origIdx };
    });
  };

  /**
   * Ayuda del público: { correct, others:[3] } suma 100. Peso de la correcta
   * baja con la dificultad: nivel 1 ≈ 70–85% → nivel 5 ≈ 35–50%, ruido ±8%.
   */
  core.audiencePoll = function (difficulty, rand) {
    var rnd = rand || Math.random;
    var t = (difficulty - 1) / 4;
    var lo = 0.70, hi = 0.85;
    var exact = hi - t * (hi - lo);
    var weight = exact * (0.92 + rnd() * 0.16);
    var correctPct = Math.round(Math.max(0.30, Math.min(0.97, weight)) * 100);
    var rest = 100 - correctPct;
    var r1 = rnd(), r2 = rnd(), r3 = rnd();
    var s = (r1 + r2 + r3) || 1;
    var a = Math.floor((r1 / s) * rest);
    var b = Math.floor((r2 / s) * rest);
    return { correct: correctPct, others: [a, b, rest - a - b] };
  };

  /** Rejilla de transiciones legales. */
  core.MACHINE = {
    intro: ['playing'],
    playing: ['feedback', 'paused', 'gameover'], // gameover directo = retiro prematuro
    feedback: ['playing', 'gameover'],
    paused: ['playing', 'gameover'],
    gameover: ['intro']
  };
  core.canTransition = function (from, to) {
    return (core.MACHINE[from] || []).indexOf(to) !== -1;
  };

  /* ═══════════════════════════════════════════════════════════════════
     ESTADO DE LA PARTIDA (sin UI)
     ═══════════════════════════════════════════════════════════════════ */
  function initialState() {
    return {
      bank: null,
      screen: 'intro',
      pools: null,             // {1:[q],...,5:[q]} barajados; pop() = sin repetir
      level: 0,                // nivel actual 1..15 (0 = sin empezar)
      solved: 0,               // niveles confirmados
      question: null,          // pregunta del nivel corriente
      options: null,           // opciones barajadas {text,isCorrect,originalIdx}
      usedLifelines: { fifty50: false, skip: false, audience: false },
      hiddenIdx: [],           // opciones descartadas por 50:50
      usedIds: [],             // ids ya jugados o quemados por Saltar
      stats: { correct: 0, wrong: 0, skipped: 0 },
      outcome: null,           // null en juego | 'win' | 'lose' | 'retire'
      seedRand: null           // rand inyectado para tests
    };
  }

  var state = initialState();
  var TIME_MAX = (state.bank && state.bank.config.timePerQuestion) || 30;
  /** Máximo de segundos: sale del banco (config.timePerQuestion). */
  function timeMax() { return (state.bank && state.bank.config.timePerQuestion) || 30; }
  var LETTERS = ['A', 'B', 'C', 'D'];

  function rnd() { return state.seedRand || Math.random; }

  /* ═══════════════════════════════════════════════════════════════════
     SONIDO (Fase 7): Web Audio 100% procedural (sin archivos).
     Apagado por defecto; el AudioContext se crea sólo al activarlo
     (gesto del usuario). Persistido con try/catch.
     ═══════════════════════════════════════════════════════════════════ */
  var soundState = { ctx: null, master: null, enabled: false };
  var SND_KEY = 'ecoudea-millonario-sonido';

  function soundLoad() {
    try { soundState.enabled = window.localStorage.getItem(SND_KEY) === '1'; } catch (e) { }
    return soundState.enabled;
  }
  function soundSave() {
    try { window.localStorage.setItem(SND_KEY, soundState.enabled ? '1' : '0'); } catch (e) { }
  }
  function audioCtx() {
    if (!soundState.enabled) return null;
    if (!soundState.ctx) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      try {
        soundState.ctx = new AC();
        soundState.master = soundState.ctx.createGain();
        soundState.master.gain.value = 0.22;
        soundState.master.connect(soundState.ctx.destination);
      } catch (e) { soundState.ctx = null; return null; }
    }
    if (soundState.ctx.state === 'suspended' && soundState.ctx.resume) {
      try { soundState.ctx.resume(); } catch (e) { }
    }
    return soundState.ctx;
  }

  /** Nota simple: oscilador + envolvente de take. `vol` 0..1 relativo al maestro. */
  function beep(freq, start, dur, type, vol) {
    var ctx = audioCtx();
    if (!ctx || !soundState.master) return;
    var t0 = ctx.currentTime + (start || 0);
    var d = dur || 0.25;
    var osc = ctx.createOscillator();
    var g = ctx.createGain();
    osc.type = type || 'triangle';
    osc.frequency.setValueAtTime(freq, t0);
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.linearRampToValueAtTime(Math.max(0.01, vol || 0.8), t0 + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + d);
    osc.connect(g);
    g.connect(soundState.master);
    osc.start(t0);
    osc.stop(t0 + d + 0.06);
  }

  var MQSound = {
    isOn: function () { return soundState.enabled; },
    setEnabled: function (v) {
      soundState.enabled = !!v;
      soundSave();
      if (soundState.enabled) beep(660, 0, 0.12, 'sine', 0.45); // blip de confirmación
      return soundState.enabled;
    },
    correct: function () {
      beep(523.25, 0, 0.16);
      beep(659.25, 0.09, 0.16);
      beep(783.99, 0.18, 0.34, 'triangle', 0.9);
    },
    wrong: function () {
      beep(220, 0, 0.25, 'sawtooth', 0.65);
      beep(146.83, 0.18, 0.45, 'sawtooth', 0.75);
    },
    lifeline: function () {
      beep(440, 0, 0.08, 'sine', 0.4);
      beep(587.33, 0.06, 0.14, 'sine', 0.5);
    },
    tick: function (urgent) {
      beep(urgent ? 880 : 640, 0, 0.05, 'sine', urgent ? 0.5 : 0.3);
    },
    /** Redoble de suspenso: golpes graves acelerando + shimmer ascendente final. */
    drum: function () {
      var t = 0;
      var iv = 0.24;
      for (var i = 0; i < 5; i++) {
        beep(82 + i * 6, t, 0.11, 'sine', 1.0);
        beep(165, t, 0.07, 'triangle', 0.35);
        t += iv;
        iv *= 0.76;
      }
      beep(261.63, t, 0.28, 'triangle', 0.4);   // C4 sube
      beep(392, t + 0.1, 0.34, 'triangle', 0.45); // G4
    },
    win: function () {
      [523.25, 659.25, 783.99, 1046.5, 1318.5].forEach(function (f, i) {
        beep(f, i * 0.12, 0.4, 'triangle', 0.85);
      });
    },
    retire: function () {
      beep(493.88, 0, 0.15);
      beep(392, 0.12, 0.35);
    }
  };

  /* ═══════════════════════════════════════════════════════════════════
     TRANSICIONES + PANTALLAS
     ═══════════════════════════════════════════════════════════════════ */
  function $(id) { return document.getElementById(id); }

  function transition(to) {
    if (!core.canTransition(state.screen, to)) {
      throw new Error('MQ transición ilegal: ' + state.screen + ' → ' + to);
    }
    state.screen = to;
    showScreen(to);
    return true;
  }

  function showScreen(name) {
    var app = $('mq-app');
    if (app) {
      app.dataset.screen = name;
      app.classList.remove('mq-ladder-open'); // la escalera móvil se cierra al cambiar pantalla
    }
    if (name !== 'playing') {
      suspense.active = false; // seguridad: ningún subestado sobrevive al cambio
      suspense.idx = -1;
      if (app) app.classList.remove('mq-suspending');
    }
    ['intro', 'playing', 'feedback', 'gameover', 'paused'].forEach(function (s) {
      var el = $('mq-screen-' + s);
      if (el) el.hidden = s !== name;
    });
    if (name === 'playing') startTimer();
    else stopTimer();
  }

  /* ═══════════════════════════════════════════════════════════════════
     TIMER (30 s verde → ámbar → rojo; congela en pausa/feedback/gameover)
     ═══════════════════════════════════════════════════════════════════ */
  var timerId = null;
  var timeLeft = TIME_MAX;

  function startTimer() {
    stopTimer();
    if (state.screen !== 'playing' || !state.question) return;
    timerId = window.setInterval(function () {
      timeLeft -= 1;
      paintTimer();
      if (timeLeft > 0 && timeLeft <= 10) MQSound.tick(timeLeft <= 5);
      if (timeLeft <= 0) { stopTimer(); resolveAnswer(-1); }
    }, 1000);
  }
  function stopTimer() {
    if (timerId !== null) { window.clearInterval(timerId); timerId = null; }
  }
  function resetTimer() { timeLeft = timeMax(); paintTimer(); }
  function paintTimer() {
    var fill = $('mq-timer-fill');
    var label = $('mq-timer-label');
    var bar = $('mq-timer');
    if (!fill || !label) return;
    var mx = timeMax();
    fill.style.width = Math.max(0, (timeLeft / mx) * 100) + '%';
    label.textContent = timeLeft + ' s';
    if (bar) {
      bar.classList.toggle('mq-warn', timeLeft <= 10 && timeLeft > 5);
      bar.classList.toggle('mq-danger', timeLeft <= 5);
      bar.setAttribute('aria-valuenow', String(Math.max(0, timeLeft)));
    }
  }

  /* ═══════════════════════════════════════════════════════════════════
     RENDER
     ═══════════════════════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════════════════════
   MATH (Fase 5): KaTeX client-side con fallback a texto crudo.
   Renderiza segmentos $...$ (inline) y $$...$$ (display) con
   renderToString(throwOnError:false). Si KaTeX no está (o falla todo),
   el elemento queda con el texto crudo — nunca se rompe la pantalla.
   ═══════════════════════════════════════════════════════════════════ */
function escHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function renderMath(el, text) {
  if (!el) return;
  var s = String(text === undefined || text === null ? '' : text);
  var k = (typeof window !== 'undefined' && window.katex && typeof window.katex.renderToString === 'function')
    ? window.katex : null;
  if (!k || s.indexOf('$') === -1) {
    el.textContent = s; // fallback crudo
    return;
  }
  var parts = s.split(/(\$\$[\s\S]+?\$\$|\$[^$]+?\$)/g);
  var out = '';
  for (var i = 0; i < parts.length; i++) {
    var p = parts[i];
    if (!p) continue;
    if (p.charAt(0) === '$') {
      var display = p.slice(0, 2) === '$$';
      var cut = display ? 2 : 1;
      var tex = p.slice(cut, -cut);
      try {
        out += k.renderToString(tex, {
          throwOnError: false,
          displayMode: display,
          strict: false,
          macros: window.katexMacros || {}
        });
      } catch (e) {
        out += escHtml(p);
      }
    } else {
      out += escHtml(p);
    }
  }
  // Un solo hijo: el padre flex (.mq-question) no debe ver N items
  // (cada segmento inline se volvería un flex-item y se separaría).
  el.innerHTML = '<span class="mq-math-flow">' + out + '</span>';
}

/**
 * Re-renderiza el math de la pantalla visible (KaTeX cargó tarde).
 * No reinicia el timer ni el estado; en feedback solo la explicación.
 */
function refreshMath() {
  if (state.screen === 'playing' && state.question) {
    renderQuestion();
  } else if (state.screen === 'feedback' && state.question) {
    var expl = $('mq-feedback-explanation');
    if (expl) renderMath(expl, state.question.explanation);
  }
}

  function buildLadder() {
    var ladder = $('mq-ladder');
    if (!ladder || !state.bank) return;
    var prizes = state.bank.config.prizes;
    var havens = state.bank.config.safeHavens;
    ladder.innerHTML = '';
    for (var lv = prizes.length; lv >= 1; lv--) {
      var li = document.createElement('li');
      li.dataset.level = String(lv);
      if (havens.indexOf(lv) !== -1) li.classList.add('mq-safe');
      var amount = document.createElement('span');
      amount.className = 'mq-ladder-amount';
      amount.textContent = 'Ecopuntos ' + prizes[lv - 1].toLocaleString('es-CO');
      li.appendChild(amount);
      ladder.appendChild(li);
    }
    markLadder();
  }
  function markLadder() {
    var ladder = $('mq-ladder');
    if (!ladder) return;
    Array.prototype.forEach.call(ladder.children, function (li) {
      var lv = Number(li.dataset.level);
      li.classList.toggle('mq-done', state.level > 0 && lv <= state.solved);
      li.classList.toggle('mq-current', lv === state.level);
    });
  }

  function updateLifelineButtons() {
    Array.prototype.forEach.call(document.querySelectorAll('.mq-lifeline'), function (b) {
      var key = b.dataset.lifeline;
      var used = state.usedLifelines[key];
      b.disabled = used || (key === 'skip' && !skipAvailable());
      b.classList.toggle('mq-used', used);
    });
  }

  /** ¿Quedan preguntas de la dificultad actual sin jugar ni quemar? */
  function skipAvailable() {
    if (!state.bank || !state.question) return false;
    var d = core.difficultyForLevel(state.level, state.bank.config.questionsPerGame);
    var pool = (state.pools && state.pools[d]) || [];
    return pool.length > 0;
  }

  function renderQuestion() {
    var lv = $('mq-level');
    if (lv) lv.textContent = String(state.level);
    renderMath($('mq-question'), state.question ? state.question.question : '');
    var buttons = document.querySelectorAll('#mq-options .mq-opt');
    Array.prototype.forEach.call(buttons, function (btn, i) {
      if (!state.options || !state.options[i]) { return; }
      btn.disabled = false;
      btn.setAttribute('aria-checked', 'false');
      btn.classList.remove('mq-correct', 'mq-wrong', 'mq-selected', 'mq-dimmed');
      renderMath(btn.querySelector('.mq-opt-text'), state.options[i].text);
    });
    var audience = $('mq-audience');
    if (audience) audience.hidden = true;
    updateLifelineButtons();
    var ret = $('mq-btn-retire');
    if (ret) ret.disabled = false;
    markLadder();
    resetTimer();
  }

  function renderAudience(poll) {
    var wrap = $('mq-audience');
    var bars = $('mq-audience-bars');
    if (!wrap || !bars || !state.options) return;
    bars.innerHTML = '';
    // orden en pantalla de las opciones incorrectas visibles (no ocultas por 50:50)
    var order = [];
    for (var i = 0; i < 4; i++) {
      if (!state.options[i].isCorrect && state.hiddenIdx.indexOf(i) === -1) order.push(i);
    }
    for (var j = 0; j < 4; j++) {
      var pct;
      if (state.options[j].isCorrect) pct = poll.correct;
      else if (state.hiddenIdx.indexOf(j) !== -1) pct = 0;
      else pct = poll.others[order.indexOf(j)] || 0;

      var row = document.createElement('div');
      row.className = 'mq-audience-row';
      var letter = document.createElement('span');
      letter.className = 'mq-audience-letter';
      letter.textContent = LETTERS[j];
      var track = document.createElement('span');
      track.className = 'mq-audience-track';
      var fillBar = document.createElement('span');
      fillBar.className = 'mq-audience-fill';
      fillBar.style.width = pct + '%';
      var value = document.createElement('span');
      value.className = 'mq-audience-pct';
      value.textContent = pct + '%';
      track.appendChild(fillBar);
      row.appendChild(letter); row.appendChild(track); row.appendChild(value);
      bars.appendChild(row);
    }
    wrap.hidden = false;
  }

  /* ═══════════════════════════════════════════════════════════════════
     FLUJO DEL JUEGO
     ═══════════════════════════════════════════════════════════════════ */
  function safeRecord() {
    var rec = 0;
    try { rec = Number(window.localStorage.getItem(recordKey()) || 0) || 0; } catch (e) { }
    return rec;
  }

  /** Estadísticas de vida (Fase 8), ahora POR BANCO (Fase 12+); nunca lanza. */
  function bankId() { return (state.bank && state.bank.meta && state.bank.meta.id) || ''; }
  function recordKey() { return 'ecoudea-millonario-record' + (bankId() ? '-' + bankId() : ''); }
  function statsKey() { return 'ecoudea-millonario-stats' + (bankId() ? '-' + bankId() : ''); }

  function safeStats() {
    try {
      return JSON.parse(window.localStorage.getItem(statsKey()) || '{}') || {};
    } catch (e) {
      return {};
    }
  }

  function saveStats(s) {
    try { window.localStorage.setItem(statsKey(), JSON.stringify(s)); } catch (e) { }
  }

  function refreshRecord() {
    var rec = safeRecord();
    var a = $('mq-record');
    if (a) a.textContent = 'Ecopuntos ' + rec.toLocaleString('es-CO');
    var b = $('mq-stat-record');
    if (b) b.textContent = rec.toLocaleString('es-CO');
    return rec;
  }

  function loadBank(bank, seedRand) {
    state = initialState();
    state.bank = bank;
    state.seedRand = seedRand || null;
    buildLadder();
    refreshRecord();
    return true;
  }

  /** Rellena `state.pools` barajados (la partida y Saltar consumen por pop). */
  function buildPools() {
    state.pools = { 1: [], 2: [], 3: [], 4: [], 5: [] };
    state.bank.questions.forEach(function (q) {
      if (state.pools[q.difficulty]) state.pools[q.difficulty].push(q);
    });
    Object.keys(state.pools).forEach(function (k) {
      state.pools[k] = core.shuffle(state.pools[k]);
    });
  }

  function startGame() {
    if (!state.bank) throw new Error('MQ: banco no cargado');
    var bank = state.bank;
    var rand = state.seedRand;
    state = initialState();
    state.bank = bank;
    state.seedRand = rand;
    buildPools();

    var total = state.bank.config.questionsPerGame;
    for (var lv = 1; lv <= total; lv++) {
      if (state.pools[core.difficultyForLevel(lv, total)].length === 0) {
        throw new Error('MQ: el banco no alcanza para el nivel ' + lv);
      }
    }
    state.level = 1;
    state.solved = 0;
    state.outcome = null;
    state.stats = { correct: 0, wrong: 0, skipped: 0 };
    state.usedIds = [];
    var lvTotal = $('mq-level-total');
    if (lvTotal) lvTotal.textContent = String(total);
    mountQuestion(state.pools[core.difficultyForLevel(1, total)].pop());
    transition('playing');
    return true;
  }

  function mountQuestion(q) {
    state.question = q;
    state.usedIds.push(q.id);
    state.options = core.shuffledOptions(q);
    state.hiddenIdx = [];
    renderQuestion();
    animateIn();
  }

  /** Re-dispara la entrada animada (respeta prefers-reduced-motion). */
  function animateIn() {
    if (!window.matchMedia) return;
    try { if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return; } catch (e) { return; }
    var q = $('mq-question');
    if (q) { q.classList.remove('mq-anim'); void q.offsetWidth; q.classList.add('mq-anim'); }
    Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (b, i) {
      b.classList.remove('mq-anim');
      void b.offsetWidth;
      b.classList.add('mq-anim');
      b.style.animationDelay = (i * 60) + 'ms';
    });
  }

  /* ═══════════════════════════════════════════════════════════════════
      SUSPENSO (Fase 12+): al elegir, la opción pulsa en ámbar ~1.9 s
      (timer congelado) antes de revelar; pausa/retiro abortan limpio.
      Subestado de 'playing': no rompe el MACHINE.
      ═══════════════════════════════════════════════════════════════════ */
  var SUSPENSE_MS = 1900;
  var REVEAL_MS = 750;   // beat visible en la pantalla de juego antes del panel
  var suspense = { active: false, idx: -1, token: 0 };

  /** Planificador wire/sandbox: si no hay setTimeout, resuelve en línea. */
  function schedule(fn, ms) {
    if (typeof window.setTimeout === 'function') return window.setTimeout(fn, ms);
    fn();
    return null;
  }
  function reduceMotion() {
    try {
      return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    } catch (e) { return false; }
  }

  function beginSuspense(idx) {
    stopTimer();
    suspense.active = true;
    suspense.idx = idx;
    suspense.token += 1;
    var app = $('mq-app');
    if (app) app.classList.add('mq-suspending');
    Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (btn, i) {
      btn.disabled = true;
      btn.setAttribute('aria-checked', i === idx ? 'true' : 'false');
      if (i === idx) btn.classList.add('mq-suspense');
    });
    MQSound.drum();
    // reveal: sólo si sigue siendo el suspenso vigente (pausa/retiro lo invalidan)
    var token = suspense.token;
    schedule(function () {
      if (suspense.active && suspense.token === token) resolveAnswer(suspense.idx);
    }, reduceMotion() ? 20 : SUSPENSE_MS);
  }

  /** Aborta el suspenso y devuelve la pregunta a estado jugable (sin resolver). */
  function cancelSuspense() {
    if (!suspense.active) return false;
    suspense.active = false;
    suspense.idx = -1;
    suspense.token += 1;
    var app = $('mq-app');
    if (app) app.classList.remove('mq-suspending');
    Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (btn) {
      btn.disabled = false;
      btn.classList.remove('mq-suspense');
      btn.setAttribute('aria-checked', 'false');
    });
    return true;
  }

  function select(idx) {
    if (state.screen !== 'playing' || suspense.active) return false;
    if (state.hiddenIdx.indexOf(idx) !== -1) return false;
    beginSuspense(idx);
    return true;
  }

  function resolveAnswer(idx) {
    if (state.screen !== 'playing') return false;
    var wasSuspense = suspense.active;
    suspense.active = false; // cierra el subestado (reveal o timeout del timer)
    suspense.idx = -1;
    stopTimer();
    var app = $('mq-app');
    if (app) app.classList.remove('mq-suspending');
    var correctIdx = -1;
    state.options.forEach(function (o, i) { if (o.isCorrect) correctIdx = i; });
    var ok = idx === correctIdx;

    Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (btn, i) {
      btn.disabled = true;
      btn.setAttribute('aria-checked', i === idx ? 'true' : 'false');
      if (i === correctIdx) btn.classList.add('mq-correct');
      if (i === idx && !ok) btn.classList.add('mq-wrong');
      if (i === idx && ok) btn.classList.add('mq-selected');
      // beat de revelación: brillo verde / sacudida roja sobre la opción
      if (i === correctIdx && wasSuspense && !reduceMotion()) btn.classList.add('mq-reveal-good');
      if (i === idx && !ok && wasSuspense && !reduceMotion()) btn.classList.add('mq-reveal-bad');
    });

    if (ok) {
      state.stats.correct += 1;
      state.solved = state.level;
      MQSound.correct();
      if (state.level === state.bank.config.questionsPerGame) state.outcome = 'win';
    } else {
      state.stats.wrong += 1;
      state.outcome = 'lose';
      MQSound.wrong();
    }
    showFeedback(ok, idx === -1, correctIdx);
    if (idx === -1 || !wasSuspense || reduceMotion()) {
      transition('feedback'); // timeout: directo; sin suspenso: como antes
    } else {
      // beat: el glow/sacudida respira en pantalla antes del panel
      schedule(function () {
        if (state.screen === 'playing') transition('feedback');
      }, REVEAL_MS);
    }
    return true;
  }

  function showFeedback(ok, timedOut, correctIdx) {
    var title = $('mq-feedback-heading');
    var answer = $('mq-feedback-answer');
    var expl = $('mq-feedback-explanation');
    var prize = $('mq-feedback-prize');
    var next = $('mq-btn-next');
    var total = state.bank.config.questionsPerGame;

    if (ok) {
      var claimed = core.prizeAmount(state.level, state.bank.config.prizes);
      if (title) title.textContent = state.outcome === 'win' ? '¡La pregunta final es correcta!' : '¡Respuesta correcta!';
      if (answer) answer.textContent = 'Ecopuntos ' + claimed.toLocaleString('es-CO') + ' asegurados en el nivel ' + state.level + '.';
      if (prize) {
        prize.hidden = false;
        prize.textContent = 'Premio actual: Ecopuntos ' + core.prizeAmount(state.solved, state.bank.config.prizes).toLocaleString('es-CO');
      }
      if (next) next.textContent = state.outcome === 'win' ? 'Ver resultado final' : 'Siguiente pregunta';
    } else {
      var keep = core.keptLevel(state.solved, state.bank.config.safeHavens);
      if (title) title.textContent = timedOut ? 'Se agotó el tiempo' : 'Respuesta incorrecta';
      if (answer) answer.textContent = correctIdx >= 0 ? 'La respuesta correcta era la ' + LETTERS[correctIdx] + '.' : '';
      if (prize) {
        prize.hidden = false;
        prize.textContent = keep > 0
          ? 'Refugio seguro: conservas Ecopuntos ' + core.prizeAmount(keep, state.bank.config.prizes).toLocaleString('es-CO')
          : 'Sin refugio: conservas Ecopuntos 0';
      }
      if (next) next.textContent = 'Ver resultado';
    }
    if (expl) renderMath(expl, state.question.explanation);
  }

  function advance() {
    if (state.screen !== 'feedback') return false;
    if (state.outcome !== null) {
      finishGame(state.outcome);
      return true;
    }
    var total = state.bank.config.questionsPerGame;
    state.level += 1;
    var q = state.pools[core.difficultyForLevel(state.level, total)].pop();
    transition('playing');
    mountQuestion(q);
    return true;
  }

  function finishGame(outcome) {
    state.outcome = outcome;
    var total = state.bank.config.questionsPerGame;
    var kept = outcome === 'win' ? total : core.keptLevel(state.solved, state.bank.config.safeHavens);
    var amount = core.prizeAmount(kept, state.bank.config.prizes);

    var rec = safeRecord();
    if (amount > rec) {
      try { window.localStorage.setItem(recordKey(), String(amount)); } catch (e) { }
    }
    if (outcome === 'win') MQSound.win();
    else if (outcome === 'retire') MQSound.retire();

    /* Fase 8: estadísticas de vida */
    var lt = safeStats();
    lt.games = (lt.games || 0) + 1;
    if (outcome === 'win') lt.wins = (lt.wins || 0) + 1;
    lt.bestLevel = Math.max(lt.bestLevel || 0, kept);
    if (amount > (lt.bestPrize || 0)) lt.bestPrize = amount;
    lt.correct = (lt.correct || 0) + state.stats.correct;
    lt.answered = (lt.answered || 0) + (state.stats.correct + state.stats.wrong);
    saveStats(lt);
    state.lifetime = lt;

    var panel = $('mq-screen-gameover');
    if (panel) panel.dataset.outcome = outcome;
    var h = $('mq-gameover-heading');
    if (h) h.textContent = outcome === 'win' ? '¡Millonario!' : (outcome === 'retire' ? 'Te retiraste a tiempo' : 'Fin del camino');
    var sub = $('mq-gameover-sub');
    if (sub) {
      sub.textContent = outcome === 'win'
        ? 'Respondiste las ' + total + ' preguntas correctamente.'
        : outcome === 'retire'
          ? 'Cerraste la partida en el nivel ' + state.level + '.'
          : 'Caíste en el nivel ' + state.level + '.';
    }
    var amountEl = $('mq-gameover-amount');
    if (amountEl) amountEl.textContent = 'Ecopuntos ' + amount.toLocaleString('es-CO');
    var sc = $('mq-stat-correct');
    if (sc) sc.textContent = String(state.stats.correct);
    var sl = $('mq-stat-level');
    if (sl) sl.textContent = String(kept || state.level);
    var life = $('mq-gameover-lifetime');
    if (life) {
      var acc = lt.answered ? Math.round((100 * lt.correct) / lt.answered) + ' %' : '—';
      life.textContent = lt.games + ' partida' + (lt.games === 1 ? '' : 's') +
        ' · ' + (lt.wins || 0) + ' millonario' + ((lt.wins || 0) === 1 ? '' : 's') +
        ' · precisión acumulada ' + acc;
    }
    refreshRecord();
    transition('gameover');
    var retry = $('mq-btn-retry');
    if (retry) retry.focus(); // a11y: foco en la acción principal
    return true;
  }

  function retire() {
    if (state.screen !== 'playing') return false;
    cancelSuspense(); // retiro durante el suspenso: aborta sin resolver
    stopTimer();
    finishGame('retire');
    return true;
  }

  function pauseGame() {
    if (state.screen !== 'playing') return false;
    cancelSuspense(); // pausa durante el suspenso: aborta sin resolver
    stopTimer();
    transition('paused');
    var res = $('mq-btn-resume');
    if (res) res.focus(); // a11y: el foco entra al diálogo
    return true;
  }
  function resumeGame() {
    if (state.screen !== 'paused') return false;
    transition('playing'); // el interval del timer se restaura en showScreen
    if (state.outcome) transition('feedback'); // se pausó durante el beat: sana el estado
    var p = $('mq-btn-pause');
    if (p) p.focus(); // a11y: el foco vuelve al controlador de pausa
    return true;
  }
  function quitFromPaused() {
    if (state.screen !== 'paused') return false;
    finishGame('retire');
    return true;
  }

  function useLifeline(name) {
    if (state.screen !== 'playing' || state.usedLifelines[name]) return false;

    if (name === 'fifty50') {
      var wrongs = [];
      for (var i = 0; i < 4; i++) if (!state.options[i].isCorrect) wrongs.push(i);
      if (wrongs.length < 2) return false;
      var kill = core.shuffle(wrongs).slice(0, 2);
      kill.forEach(function (k) { state.hiddenIdx.push(k); });
      Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (btn, i) {
        if (state.hiddenIdx.indexOf(i) !== -1) {
          btn.classList.add('mq-dimmed');
          btn.disabled = true;
        }
      });
      state.usedLifelines.fifty50 = true;
    } else if (name === 'skip') {
      if (!skipAvailable()) return false;
      var total = state.bank.config.questionsPerGame;
      var d = core.difficultyForLevel(state.level, total);
      mountQuestion(state.pools[d].pop());
      state.stats.skipped += 1;
      state.usedLifelines.skip = true;
    } else if (name === 'audience') {
      var totalAud = state.bank.config.questionsPerGame;
      renderAudience(core.audiencePoll(core.difficultyForLevel(state.level, totalAud), rnd()));
      state.usedLifelines.audience = true;
    } else {
      return false;
    }
    MQSound.lifeline();
    updateLifelineButtons();
    return true;
  }

  /* ═══════════════════════════════════════════════════════════════════
     CABLEADO DE EVENTOS + INIT
     ═══════════════════════════════════════════════════════════════════ */
  function wrap(fn) {
    return function (e) {
      e.preventDefault();
      try { fn(); } catch (err) { if (window.console) window.console.error('[MQ]', err); }
    };
  }

  function bind() {
    var on = function (id, fn) { var el = $(id); if (el) el.addEventListener('click', wrap(fn)); };
    on('mq-btn-start', startGame);
    on('mq-btn-next', advance);
    on('mq-btn-retry', function () {
      if (state.screen !== 'gameover') return; // robustez: idempotente, solo válido desde gameover
      transition('intro');
      startGame();
    });
    on('mq-btn-pause', pauseGame);
    on('mq-btn-resume', resumeGame);
    on('mq-btn-quit', quitFromPaused);
    on('mq-btn-retire', retire);

    var snd = $('mq-sound');
    if (snd) {
      snd.checked = soundState.enabled;
      snd.addEventListener('change', wrap(function () { MQSound.setEnabled(snd.checked); }));
    }

    Array.prototype.forEach.call(document.querySelectorAll('.mq-lifeline'), function (b) {
      b.addEventListener('click', wrap(function () { useLifeline(b.dataset.lifeline); }));
    });
    Array.prototype.forEach.call(document.querySelectorAll('#mq-options .mq-opt'), function (b) {
      b.addEventListener('click', wrap(function () { select(Number(b.dataset.idx)); }));
    });

    // Fase 9 (a11y): navegación por flechas dentro del radiogroup de opciones
    var optsWrap = $('mq-options');
    if (optsWrap) {
      optsWrap.addEventListener('keydown', function (e) {
        var btn = e.target;
        if (!btn || !btn.classList || !btn.classList.contains('mq-opt')) return;
        var move = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
        if (!move) return;
        var enabled = Array.prototype.filter.call(optsWrap.querySelectorAll('.mq-opt'), function (o) { return !o.disabled; });
        if (enabled.length < 2) return;
        var i = enabled.indexOf(btn);
        e.preventDefault();
        enabled[((i || 0) + move + enabled.length) % enabled.length].focus();
      });
    }

    // Fase 9: escalera como modal en móvil
    var ladderBtn = $('mq-btn-ladder');
    if (ladderBtn) {
      ladderBtn.addEventListener('click', wrap(function () {
        var app = $('mq-app');
        if (!app) return;
        var open = app.classList.toggle('mq-ladder-open');
        ladderBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      }));
      // clic en el backdrop cierra
      var col = document.querySelector('.mq-ladder-col');
      if (col) col.addEventListener('click', function (e) {
        if (e.target === col) { $('mq-app').classList.remove('mq-ladder-open'); ladderBtn.setAttribute('aria-expanded', 'false'); }
      });
      // Esc cierra
      document.addEventListener('keydown', function (e) {
        var app = $('mq-app');
        if (e.key === 'Escape' && app && app.classList.contains('mq-ladder-open')) {
          app.classList.remove('mq-ladder-open');
          ladderBtn.setAttribute('aria-expanded', 'false');
          ladderBtn.focus();
        }
      });
    }
  }

  /* ═══════════════════════════════════════════════════════════════════
      BANCOS POR CURSO (Fase 12+): índice + selector en la intro.
      Cada banco es independiente (sin mezclas); niveles = tamaño del banco;
      refugios en ⅓ y ⅔; stats/récord por banco (sufijo con meta.id).
      ═══════════════════════════════════════════════════════════════════ */
  var BANK_KEY = 'ecoudea-millonario-banco';
  var banksIndex = [];
  var currentBankId = '';
  var bankCache = {};

  function baseHref() {
    var meta = document.querySelector('meta[name="astro-base"]');
    return (meta && meta.content) || '';
  }

  function cacheBust() {
    var v = '';
    try {
      var self = document.querySelector('script[src*="millonario.js"]');
      var m = self && /(?:\?|&)v=([^&]+)/.exec(self.src);
      if (m) v = '?v=' + m[1];
    } catch (e) { }
    return v;
  }

  /** Tarjeta de banco en la intro. */
  function renderBankCards() {
    var box = $('mq-banks');
    if (!box) return;
    box.innerHTML = '';
    banksIndex.forEach(function (b) {
      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'mq-bank-card';
      card.dataset.bank = b.id;
      card.setAttribute('role', 'radio');
      card.setAttribute('aria-checked', b.id === currentBankId ? 'true' : 'false');
      if (b.id === currentBankId) card.classList.add('mq-bank-active');
      var title = document.createElement('span');
      title.className = 'mq-bank-title';
      title.textContent = b.title;
      var sub = document.createElement('span');
      sub.className = 'mq-bank-sub';
      sub.textContent = b.questionCount + ' preguntas · ' + b.questionCount +
        ' niveles · refugios ' + b.safeHavens.join(' y ');
      var rec = document.createElement('span');
      rec.className = 'mq-bank-record';
      try {
        var r = Number(window.localStorage.getItem('ecoudea-millonario-record-' + b.id) || 0) || 0;
        rec.textContent = r > 0 ? 'Récord: Ecopuntos ' + r.toLocaleString('es-CO') : 'Sin récord aún';
      } catch (e) { rec.textContent = ''; }
      if (b.id === currentBankId) rec.classList.add('mq-bank-record-active');
      card.appendChild(title); card.appendChild(sub); card.appendChild(rec);
      box.appendChild(card);
    });
  }

  /** Rellena las reglas de la intro con los números del banco corriente. */
  function paintIntroRules() {
    var bank = state.bank;
    if (!bank) return;
    var total = bank.config.questionsPerGame;
    var havens = bank.config.safeHavens || [];
    var totalEl = $('mq-rule-total');
    var count = (bank.meta && bank.meta.questionCount) || total;
    if (totalEl) totalEl.textContent = count + ' preguntas';
    var havEl = $('mq-rule-havens');
    if (havEl) havEl.textContent = havens.join(' y ');
    var totalEl2 = $('mq-level-total');
    if (totalEl2) totalEl2.textContent = String(total);
    var havEl = $('mq-rule-havens');
    if (havEl) havEl.textContent = havens.join(' y ');
  }

  function selectBank(id, cb) {
    var entry = null;
    for (var i = 0; i < banksIndex.length; i++) if (banksIndex[i].id === id) entry = banksIndex[i];
    if (!entry) return;
    currentBankId = id;
    try { window.localStorage.setItem(BANK_KEY, id); } catch (e) { }
    if (bankCache[id]) {
      applyBank(bankCache[id]);
      if (cb) cb();
      return;
    }
    fetch(baseHref() + '/assets/data/millonario-' + id + '.json' + cacheBust())
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (bank) {
        bankCache[id] = bank;
        applyBank(bank);
        if (cb) cb();
      })
      .catch(function (err) { if (window.console) window.console.error('[MQ] banco "' + id + '" no disponible:', err); });
  }

  function applyBank(bank) {
    loadBank(bank);
    paintIntroRules();
    renderBankCards();
  }

  /** Cards clicables (delegación, las cards se re-renderizan). */
  function bindBankSelector() {
    var box = $('mq-banks');
    if (!box) return;
    box.addEventListener('click', function (e) {
      var card = e.target && e.target.closest ? e.target.closest('.mq-bank-card') : null;
      if (card && card.dataset.bank && card.dataset.bank !== currentBankId) {
        selectBank(card.dataset.bank, null);
      }
    });
  }

  function loadBankIndex(json) {
    banksIndex = Array.isArray(json) ? json : (json && json.banks) || [];
    var saved = '';
    try { saved = window.localStorage.getItem(BANK_KEY) || ''; } catch (e) { }
    if (saved && banksIndex.some(function (b) { return b.id === saved; })) currentBankId = saved;
    else if (banksIndex.length) currentBankId = banksIndex[0].id;
    bindBankSelector();
    if (currentBankId) selectBank(currentBankId, null);
    else renderBankCards();
  }

  function init() {
    if (!$('mq-app')) return; // sin DOM de juego (tests / otras páginas)
    soundLoad();
    bind();
    refreshRecord();
    if (typeof fetch !== 'function') return;
    // Fase 9: cache-busting — hereda ?v= del tag <script> propio
    fetch(baseHref() + '/assets/data/millonario-index.json' + cacheBust())
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(loadBankIndex)
      .catch(function (err) { if (window.console) window.console.error('[MQ] índice de bancos no disponible:', err); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* ═══════════════════════════════════════════════════════════════════
     API PÚBLICA (integración + tests)
     ═══════════════════════════════════════════════════════════════════ */
  window.MQ = {
    core: core,
    state: function () { return state; },
    loadBank: loadBank,
    selectBank: selectBank,
    banks: function () { return banksIndex; },
    currentBank: function () { return currentBankId; },
    startGame: startGame,
    select: select,
    advance: advance,
    retire: retire,
    pauseGame: pauseGame,
    resumeGame: resumeGame,
    quitFromPaused: quitFromPaused,
    useLifeline: useLifeline,
    skipAvailable: skipAvailable,
    finishGame: finishGame,
    transition: transition,
    refreshMath: refreshMath,
    renderMath: renderMath,
    suspense: function () { return { active: suspense.active, idx: suspense.idx }; },
    cancelSuspense: cancelSuspense,
    sound: MQSound
  };
})();
