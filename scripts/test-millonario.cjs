#!/usr/bin/env node
/**
 * test-millonario.cjs — Pruebas del motor del millonario.
 * Carga public/assets/js/millonario.js en un sandbox con window/document
 * mínimos (sin DOM real). Verifica:
 *   1. partida completa (banco Estadística II, 10 niveles) sin repetidos
 *   2. una sola correcta tras shuffle + textos íntegros
 *   3. stats de vida por banco + récord por banco
 *   4. safe havens (refugios ⅓/⅔) y escalera parametrizada por N
 *   5. Saltar sin repetir, dificultad por bucket (N≠15)
 *   6. SUSPENSO: bloquea segundo clic, aborta en pausa, resuelve limpio
 *   7. cero transiciones ilegales + multi-banco (2º banco consecuente)
 *   8. ayuda del público, sonido seguro
 *
 * El sandbox tiene un setTimeout DIFERIDO (cola): select entra en suspenso
 * y flush() drena la cola (reveal → beat de revelación → feedback).
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
// setTimeout DIFERIDO: el suspenso entra y flush() drena la cola hasta vaciarla.
const pending = [];
win.setTimeout = function (fn, ms) { pending.push({ fn, ms }); return 0; };
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

function drainOnce() {
  while (pending.length) {
    const job = pending.shift();
    job.fn();
  }
}
function flush() {
  // cada fn puede agendar más (reveal → transición de feedback): drena a fondo
  let guard = 50;
  while (pending.length && guard-- > 0) drainOnce();
}
function answer(idx) {
  const ok = MQ.select(idx);
  flush();
  return ok;
}
function correctIdxOf(st) {
  return st.options.findIndex(function (o) { return o.isCorrect; });
}
function wrongIdxOf(st) {
  return st.options.findIndex(function (o) { return !o.isCorrect && st.hiddenIdx.indexOf(st.options.indexOf(o)) === -1; });
}

const bankA = JSON.parse(fs.readFileSync(
  path.join(ROOT, 'public', 'assets', 'data', 'millonario-estadistica-ii.json'), 'utf8'));
const bankB = JSON.parse(fs.readFileSync(
  path.join(ROOT, 'public', 'assets', 'data', 'millonario-macroeconomia-i.json'), 'utf8'));

let failures = 0;
function check(name, cond) {
  console.log((cond ? '  OK  ' : '  FAIL') + ' ' + name);
  if (!cond) failures++;
}

const TOTAL = bankA.config.questionsPerGame; // 10 niveles

/* 1. Partida completa sin repetidos ---------------------------------- */
console.log('1) Selección sin repetidos');
MQ.loadBank(bankA);
MQ.startGame();
check('banco cargado y partida iniciada', MQ.state().screen === 'playing');
check('1 pregunta montada en el nivel 1', MQ.state().level === 1 && MQ.state().question);

/* 2. Una sola correcta tras shuffle + cadena con suspenso ------------- */
console.log('2) Una sola correcta tras shuffle (con suspenso en cada respuesta)');
let allOne = true, textsMatch = true, chainOk = true;
const gameIds = [];
for (let lv = 1; lv <= TOTAL; lv++) {
  const st = MQ.state();
  const opts = st.options;
  gameIds.push(st.question.id);
  if (opts.filter(function (o) { return o.isCorrect; }).length !== 1) allOne = false;
  const src = st.question.options.slice().sort().join('|');
  const scr = opts.map(function (o) { return o.text; }).sort().join('|');
  if (src !== scr) textsMatch = false;
  if (!answer(correctIdxOf(st))) chainOk = false;
  if (lv < TOTAL && !MQ.advance()) chainOk = false;
}
MQ.advance(); // feedback del último nivel → gameover
check(TOTAL + ' preguntas jugadas', gameIds.length === TOTAL);
check('ids únicos en la partida (sin repetidos)', new Set(gameIds).size === TOTAL);
check('exactamente 1 correcta por nivel', allOne);
check('los 4 textos en pantalla = originales del JSON', textsMatch);
check('cadena select(suspenso)→advance estable en ' + TOTAL + ' niveles', chainOk);
check('victoria: outcome = win', MQ.state().outcome === 'win');
check('gameover alcanzado tras ganar', MQ.state().screen === 'gameover');
check('premio final = tope de la escalera (1.000.000)',
  MQ.core.prizeAmount(TOTAL, bankA.config.prizes) === 1000000);

/* 2b. Stats y récord POR BANCO (Fase 12+) ------------------------------ */
console.log('2b) Stats de vida por banco');
const statsKey = 'ecoudea-millonario-stats-' + bankA.meta.id;
const recordKey = 'ecoudea-millonario-record-' + bankA.meta.id;
const ltRaw = win.localStorage.getItem(statsKey);
check('stats de vida guardadas con sufijo del banco (' + statsKey + ')', !!ltRaw);
if (ltRaw) {
  const lt = JSON.parse(ltRaw);
  check('1 partida registrada', lt.games === 1);
  check('1 victoria registrada', lt.wins === 1);
  check('mejor nivel = ' + TOTAL, lt.bestLevel === TOTAL);
  check(TOTAL + ' correctas acumuladas', lt.correct === TOTAL);
  check('precisión 100 % (answered=' + TOTAL + ')', lt.answered === TOTAL);
}
check('récord por banco guardado (' + recordKey + ')', win.localStorage.getItem(recordKey) === '1000000');
check('las llaves globales viejas NO se usan', win.localStorage.getItem('ecoudea-millonario-stats') === null);

/* 3. Premios con safe havens ⅓/⅔ (est II: [3,6]) ----------------------- */
console.log('3) Premios con safe havens ' + JSON.stringify(bankA.config.safeHavens));
const havens = bankA.config.safeHavens;
const prizes = bankA.config.prizes;
check('refugios en ⅓ y ⅔ de ' + TOTAL, havens[0] === Math.floor(TOTAL / 3) && havens[1] === Math.floor(2 * TOTAL / 3));
check('fallos sin refugio (2 aciertos) conservan 0', MQ.core.keptLevel(2, havens) === 0);
check('fallos tras 3 aciertos conservan nivel 3', MQ.core.keptLevel(3, havens) === 3);
check('fallos con 5 aciertos conservan nivel 3', MQ.core.keptLevel(5, havens) === 3);
check('fallos con 6 aciertos conservan nivel 6', MQ.core.keptLevel(6, havens) === 6);
check('prizeAmount(nivel 3) = ' + prizes[2], MQ.core.prizeAmount(3, prizes) === 1000);
check('prizeAmount(nivel 6) = ' + prizes[5], MQ.core.prizeAmount(6, prizes) === 10000);
check('prizeAmount(0) = 0', MQ.core.prizeAmount(0, prizes) === 0);
check('escalera monótona ascendente', prizes.every((p, i) => i === 0 || p > prizes[i - 1]));

/* 4. Saltar sin repetir la pregunta (dificultad por bucket) ------------ */
console.log('4) Saltar sin repetir la pregunta');
MQ.loadBank(bankA);
MQ.startGame();
const firstId = MQ.state().question.id;
check('comodín Saltar aplicable', MQ.useLifeline('skip') === true);
const st = MQ.state();
check('la pregunta cambió por OTRA (distinta) del mismo nivel',
  st.question.id !== firstId && MQ.core.difficultyForLevel(st.level, TOTAL) === 1);
check('la correcta sigue única tras el salto',
  st.options.filter(function (o) { return o.isCorrect; }).length === 1);
check('Saltar de uso único (2ª vez rechazada)', MQ.useLifeline('skip') === false);
check('ids usados/quemados únicos', new Set(st.usedIds).size === st.usedIds.length);
check('bucket map parametrizado: nivel 7 → dificultad 4, nivel 6 → 3 (tamaños 2/2/2/2/2)',
  MQ.core.difficultyForLevel(7, TOTAL) === 4 && MQ.core.difficultyForLevel(6, TOTAL) === 3);

/* 4b. 2º banco: Macro I (20 niveles, tamaños 4×5) ----------------------- */
console.log('4b) Banco independiente macroeconomia-i (20 niveles)');
check('config del banco B: 20 niveles, refugios [6,13]',
  bankB.config.questionsPerGame === 20 && JSON.stringify(bankB.config.safeHavens) === '[6,13]');
check('ids del banco B prefijados por curso',
  bankB.questions.every((q) => q.id.startsWith('macroeconomia-i-')));
check('dificultad nivel 7 (de 20) → 2', MQ.core.difficultyForLevel(7, 20) === 2);
check('dificultad nivel 16 (de 20) → 4 y nivel 17 → 5', MQ.core.difficultyForLevel(16, 20) === 4 && MQ.core.difficultyForLevel(17, 20) === 5);
MQ.loadBank(bankB);
MQ.startGame();
for (let lv = 1; lv <= 20; lv++) {
  answer(correctIdxOf(MQ.state()));
  if (lv < 20) MQ.advance();
}
MQ.advance();
check('victoria en el banco B (20 niveles)', MQ.state().outcome === 'win');
check('stats por banco B separadas',
  JSON.parse(win.localStorage.getItem('ecoudea-millonario-stats-macroeconomia-i')).wins === 1);

/* 5. Cero estados inválidos ------------------------------------------ */
console.log('5) Cero estados inválidos');
MQ.loadBank(bankA);
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

// derrota bajo refugio: 3 aciertos (cruza el refugio 3) y fallo en el nivel 4
MQ.loadBank(bankA);
MQ.startGame();
for (let i = 1; i <= 3; i++) {
  answer(correctIdxOf(MQ.state()));
  MQ.advance();
}
check('partida cruzada refugio: nivel 4 tras 3 correctas', MQ.state().level === 4 && MQ.state().solved === 3);
answer(wrongIdxOf(MQ.state()));
MQ.advance();
check('fallo tras cruzar refugio 3 → conserva Ecopuntos 1.000 (premio final)',
  MQ.core.prizeAmount(MQ.core.keptLevel(3, havens), prizes) === 1000);

/* 6. SUSPENSO (Fase 12+): bloqueo, aborto en pausa, resolución ---------- */
console.log('6) Suspenso de revelación');
MQ.loadBank(bankA);
MQ.startGame();
const stSusp = MQ.state();
const ci = correctIdxOf(stSusp);
check('select entra en suspenso (sigue en playing)', MQ.select(ci) === true && MQ.suspense().active === true);
check('segundo clic bloqueado durante el suspenso', MQ.select(wrongIdxOf(stSusp)) === false);
check('pausa aborta el suspenso', MQ.pauseGame() === true && MQ.suspense().active === false);
check('el reveal diferido NO resuelve tras el aborto (screen sigue paused)', MQ.state().screen === 'paused');
MQ.resumeGame();
check('tras abortar: se puede elegir de nuevo', MQ.select(correctIdxOf(MQ.state())) === true);
flush();
check('reveal correcto → feedback con acierto', MQ.state().screen === 'feedback' && MQ.state().outcome === null);
MQ.advance();

// cancel manual + tolerancia a re-selección (índice correcto FRESCO por nivel)
check('cancel sin suspenso es no-op (devuelve false)', MQ.cancelSuspense() === false);
check('suspenso en el nivel 2', MQ.select(correctIdxOf(MQ.state())) === true && MQ.suspense().active === true);
check('cancelSuspense manual aborta', MQ.cancelSuspense() === true && MQ.suspense().active === false);
check('re-selección tras cancel manual permitida', MQ.select(correctIdxOf(MQ.state())) === true);
flush();
check('respuesta resuelta limpiamente tras cancel+reselect', MQ.state().screen === 'feedback' && MQ.state().outcome === null);

MQ.advance(); // feedback → playing nivel 2
const stW = MQ.state();
check('fallo en suspenso → outcome lose tras flush', (function () {
  MQ.select(wrongIdxOf(stW));
  flush();
  return MQ.state().screen === 'feedback' && MQ.state().outcome === 'lose';
})());
MQ.advance();
check('gameover tras derrota con suspenso', MQ.state().screen === 'gameover');

/* 7. Ayuda del público: suma 100 y sesgo por nivel --------------------- */
console.log('7) Ayuda del público');
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

/* 8. Sonido seguro sin AudioContext ------------------------------------ */
console.log('8) Sonido seguro sin AudioContext');
check('sonido apagado por defecto', MQ.sound.isOn() === false);
check('setEnabled(true) sin AudioContext no lanza (devuelve true y no crashea)',
  MQ.sound.setEnabled(true) === true);
check('los sonidos procedurales no lanzan sin audio (incl. drum de suspenso)', (function () {
  try {
    MQ.sound.correct(); MQ.sound.wrong(); MQ.sound.lifeline();
    MQ.sound.tick(true); MQ.sound.win(); MQ.sound.retire(); MQ.sound.drum();
    return true;
  } catch (e) { return false; }
})());
MQ.sound.setEnabled(false);

console.log('');
if (failures > 0) {
  console.error('TESTS FALLIDOS: ' + failures);
  process.exit(1);
}
console.log('TESTS OK: motor del millonario verificado (suspenso + multi-banco).');
