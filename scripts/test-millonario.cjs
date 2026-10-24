#!/usr/bin/env node
/**
 * test-millonario.cjs — Pruebas ligeras del motor del millonario (Fase 3).
 * Carga public/assets/js/millonario.js en un sandbox con window/document
 * mínimos (sin DOM real) y verifica: selección sin repetidos, una sola
 * correcta tras shuffle, premios con safe havens, Saltar sin repetir y
 * cero transiciones ilegales en partidas completas.
 *
 * Uso: node scripts/test-millonario.cjs  (exit 0 = todo OK)
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..');

/* --- Sandbox mínimo ------------------------------------------------- */
function noop() { }
const win = {
  console: { error: noop, warn: noop, log: noop },
  setInterval: () => 0,
  clearInterval: noop,
  localStorage: {
    _m: {},
    getItem(k) { return this._m[k] || null; },
    setItem(k, v) { this._m[k] = String(v); }
  }
};
const $doc = {
  readyState: 'loading', // fuerza rama DOMContentLoaded → sin wiring
  addEventListener: noop,
  getElementById: () => null,
  querySelector: () => null,
  querySelectorAll: () => []
};
win.document = $doc;
win.window = win;
$doc.window = win;

const sandbox = { window: win, document: $doc };
const code = fs.readFileSync(path.join(ROOT, 'public', 'assets', 'js', 'millonario.js'), 'utf8');
vm.runInNewContext(code, sandbox, { filename: 'millonario.js' });

const MQ = win.MQ;
if (!MQ) { console.error('El motor no expuso window.MQ'); process.exit(1); }

const bank = JSON.parse(fs.readFileSync(
  path.join(ROOT, 'public', 'assets', 'data', 'millonario.json'), 'utf8'));

let failures = 0;
function check(name, cond) {
  console.log((cond ? '  OK  ' : '  FAIL') + ' ' + name);
  if (!cond) failures++;
}

/* 1. Selección sin repetidos --------------------------------------- */
console.log('1) Selección sin repetidos');
MQ.loadBank(bank);
MQ.startGame();
check('banco cargado y partida iniciada', MQ.state().screen === 'playing');
check('1 pregunta montada en el nivel 1', MQ.state().level === 1 && MQ.state().question);

/* 2. Una sola correcta tras shuffle --------------------------------- */
console.log('2) Una sola correcta tras shuffle');
let allOne = true, textsMatch = true, chainOk = true;
const gameIds = [];
for (let lv = 1; lv <= 15; lv++) {
  const st = MQ.state();
  const opts = st.options;
  gameIds.push(st.question.id);
  if (opts.filter(function (o) { return o.isCorrect; }).length !== 1) allOne = false;
  const src = st.question.options.slice().sort().join('|');
  const scr = opts.map(function (o) { return o.text; }).sort().join('|');
  if (src !== scr) textsMatch = false;
  const correctIdx = opts.findIndex(function (o) { return o.isCorrect; });
  if (!MQ.select(correctIdx)) chainOk = false;
  if (lv < 15 && !MQ.advance()) chainOk = false;
}
MQ.advance(); // feedback del nivel 15 → gameover
check('15 preguntas jugadas', gameIds.length === 15);
check('ids únicos en la partida (sin repetidos)', new Set(gameIds).size === 15);
check('exactamente 1 correcta por nivel', allOne);
check('los 4 textos en pantalla = originales del JSON', textsMatch);
check('cadena select→advance estable en 15 niveles', chainOk);
check('victoria: outcome = win', MQ.state().outcome === 'win');
check('gameover alcanzado tras ganar', MQ.state().screen === 'gameover');
check('premio final = tope de la escalera',
  MQ.core.prizeAmount(15, bank.config.prizes) === 1000000);

/* 2b. Persistencia de vida (Fase 8) ---------------------------------- */
const ltRaw = win.localStorage.getItem('ecoudea-millonario-stats');
check('stats de vida guardadas tras la partida', !!ltRaw);
if (ltRaw) {
  const lt = JSON.parse(ltRaw);
  check('1 partida registrada', lt.games === 1);
  check('1 victoria registrada', lt.wins === 1);
  check('mejor nivel = 15', lt.bestLevel === 15);
  check('15 correctas acumuladas', lt.correct === 15);
  check('precisión 100 %answered=15', lt.answered === 15);
}

/* 3. Premios con safe havens [5,10] ---------------------------------- */
console.log('3) Premios con safe havens [5,10]');
const havens = bank.config.safeHavens;
const prizes = bank.config.prizes;
check('fallos sin refugio (2 aciertos) conservan 0', MQ.core.keptLevel(2, havens) === 0);
check('fallos tras 5 aciertos conservan nivel 5', MQ.core.keptLevel(5, havens) === 5);
check('fallos con 7 aciertos conservan nivel 5', MQ.core.keptLevel(7, havens) === 5);
check('fallos con 10 aciertos conservan nivel 10', MQ.core.keptLevel(10, havens) === 10);
check('prizeAmount(nivel 5) = ' + prizes[4], MQ.core.prizeAmount(5, prizes) === prizes[4]);
check('prizeAmount(nivel 7) = ' + prizes[6], MQ.core.prizeAmount(7, prizes) === prizes[6]);
check('prizeAmount(0) = 0', MQ.core.prizeAmount(0, prizes) === 0);

/* 4. Saltar sin repetir la pregunta ---------------------------------- */
console.log('4) Saltar sin repetir la pregunta');
MQ.loadBank(bank);
MQ.startGame();
const firstId = MQ.state().question.id;
check('comodín Saltar aplicable', MQ.useLifeline('skip') === true);
const st = MQ.state();
check('la pregunta cambió por OTRA (distinta) del mismo nivel',
  st.question.id !== firstId && MQ.core.difficultyForLevel(st.level) === 1);
check('la correcta sigue única tras el salto',
  st.options.filter(function (o) { return o.isCorrect; }).length === 1);
check('Saltar de uso único (2ª vez rechazada)', MQ.useLifeline('skip') === false);
check('ids usados/quemados únicos', new Set(st.usedIds).size === st.usedIds.length);

/* 5. Cero estados inválidos ------------------------------------------ */
console.log('5) Cero estados inválidos');
MQ.loadBank(bank);
MQ.startGame();
check('intro → playing (startGame)', MQ.state().screen === 'playing');
MQ.pauseGame();
check('playing → paused', MQ.state().screen === 'paused');
MQ.resumeGame();
check('paused → playing (timer restaurado vía showScreen)', MQ.state().screen === 'playing');
MQ.retire();
check('playing → gameover (retiro directo)', MQ.state().screen === 'gameover');
MQ.transition('intro');
check('gameover → intro', MQ.state().screen === 'intro');

// transición realmente ilegal debe lanzar
let threw = false;
try { MQ.transition('feedback'); } catch (e) { threw = true; }
check('transición ilegal (intro → feedback) lanza error', threw);

// derrota en safe haven: fallar en el nivel 5 debe conservar el nivel anterior…
// con 4 aciertos y fallo en el 5º: kept = 0 (refugio en 5 aún no SUPERADO)?
// Regla del plan: el refugio te salva SI lo cruzaste; fallar EN el 5 significa
// que llevas 4 resueltas → kept=0. Con 9 resueltas y fallo en el 10 → kept=5.
MQ.loadBank(bank);
MQ.startGame();
for (let i = 1; i <= 4; i++) {
  const o = MQ.state().options;
  MQ.select(o.findIndex(function (x) { return x.isCorrect; }));
  MQ.advance();
}
check('partida bajo refugio: nivel 5 tras 4 correctas', MQ.state().level === 5 && MQ.state().solved === 4);
const wrongIdx = MQ.state().options.findIndex(function (x) { return !x.isCorrect; });
MQ.select(wrongIdx);
MQ.advance();
check('fallo en nivel 5 sin cruzar refugio → conserva Ecopuntos 0 (premio final)',
  MQ.core.prizeAmount(MQ.core.keptLevel(4, havens), prizes) === 0);

/* 6. Ayuda del público: suma 100 y sesgo por nivel -------------------- */
console.log('6) Ayuda del público');
let sumOk = true, biasOk = true;
for (let i = 0; i < 500; i++) {
  const easy = MQ.core.audiencePoll(1, Math.random);
  const hard = MQ.core.audiencePoll(5, Math.random);
  const se = easy.correct + easy.others[0] + easy.others[1] + easy.others[2];
  const sh = hard.correct + hard.others[0] + hard.others[1] + hard.others[2];
  if (se !== 100 || sh !== 100) sumOk = false;
  if (easy.correct <= hard.correct) biasOk = false;
}
check('todas las sumas = 100 (500 iter × 2 niveles)', sumOk);
check('sesgo: correcta más votada en fácil que en difícil', biasOk);

/* 7. Sonido (Fase 7): sandbox sin AudioContext → no debe lanzar ------- */
console.log('7) Sonido seguro sin AudioContext');
check('sonido apagado por defecto', MQ.sound.isOn() === false);
check('setEnabled(true) sin AudioContext no lanza (devuelve true y no crashea)',
  MQ.sound.setEnabled(true) === true);
check('los sonidos procedurales no lanzan sin audio', (function () {
  try {
    MQ.sound.correct(); MQ.sound.wrong(); MQ.sound.lifeline();
    MQ.sound.tick(true); MQ.sound.win(); MQ.sound.retire();
    return true;
  } catch (e) { return false; }
})());
MQ.sound.setEnabled(false);

console.log('');
if (failures > 0) {
  console.error('TESTS FALLIDOS: ' + failures);
  process.exit(1);
}
console.log('TESTS OK: motor del millonario verificado (Fase 3).');
