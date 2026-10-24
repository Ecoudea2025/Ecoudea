#!/usr/bin/env node
/**
 * check-millonario.cjs — Gate de los bancos de preguntas del millonario.
 * Era multi-banco (Fase 12+): valida TODOS los bancos independientes
 * public/assets/data/millonario-<curso>.json contra el esquema, y el
 * manifiesto millonario-index.json (coherencia de conteos/niveles/refugios).
 *
 * Uso: node scripts/check-millonario.cjs   (exit 0 = OK, 1 = falla)
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { validate, countPerLevel, latexBalanced, levelSizes } = require('./millonario-lib.cjs');

const ROOT = path.resolve(__dirname, '..');
const DATA = path.join(ROOT, 'public', 'assets', 'data');
const INDEX = path.join(DATA, 'millonario-index.json');
const CLASSES_DIR = path.join(ROOT, 'src', 'content', 'classes');

if (!fs.existsSync(INDEX)) {
  console.error('CHECK FALLÓ: no existe millonario-index.json (corre primero scripts/build-millonario.cjs).');
  process.exit(1);
}

let manifest;
try {
  manifest = JSON.parse(fs.readFileSync(INDEX, 'utf8'));
} catch (e) {
  console.error('CHECK FALLÓ: índice JSON inválido — ' + e.message);
  process.exit(1);
}
if (!manifest || !Array.isArray(manifest.banks) || manifest.banks.length === 0) {
  console.error('CHECK FALLÓ: millonario-index.json no declara bancos.');
  process.exit(1);
}

const knownSources = fs.existsSync(CLASSES_DIR)
  ? new Set(fs.readdirSync(CLASSES_DIR).filter((f) => f.endsWith('.md')))
  : null;

const seenIds = new Set();
let failures = 0;
function check(name, cond) {
  console.log((cond ? '  OK  ' : '  FAIL') + ' ' + name);
  if (!cond) failures++;
}

for (const entry of manifest.banks) {
  console.log(`Banco ${entry.id} (${entry.title}):`);
  const bankPath = path.join(DATA, entry.file);
  if (!fs.existsSync(bankPath)) {
    check('archivo del banco presente', false);
    continue;
  }
  let bank;
  try {
    bank = JSON.parse(fs.readFileSync(bankPath, 'utf8'));
  } catch (e) {
    check('JSON del banco válido', false);
    continue;
  }

  const errors = validate(bank, { knownSources });
  if (errors.length > 0) {
    check(`esquema (${errors.length} errores)`, false);
    errors.forEach((e) => console.error('    - ' + e));
    continue;
  }
  check('esquema válido (estructura, 4 opciones, 1 correcta, LaTeX balanceado, sin duplicadas)', true);

  // Coherencia índice ↔ banco
  check('questionCount coincide', bank.meta.questionCount === entry.questionCount && bank.questions.length === entry.questionCount);
  check('niveles = tamaño del banco', bank.config.questionsPerGame === entry.levels && entry.levels === entry.questionCount);
  check('safeHavens = [floor(n/3), floor(2n/3)]',
    bank.config.safeHavens[0] === Math.floor(entry.levels / 3) &&
    bank.config.safeHavens[1] === Math.floor(2 * entry.levels / 3));
  check('escalera con tope 1.000.000', bank.config.prizes[bank.config.prizes.length - 1] === entry.topPrize);

  // ids únicos GLOBALMENTE (los bancos son independientes)
  const dup = bank.questions.some((q) => {
    if (seenIds.has(q.id)) return true;
    seenIds.add(q.id);
    return false;
  });
  check('ids únicos entre todos los bancos', !dup);

  // Cobertura: cada bucket debe tener al menos sus preguntas jugables
  const sizes = levelSizes(entry.levels);
  const per = countPerLevel(bank.questions);
  const covered = sizes.every((need, i) => (per[String(i + 1)] || 0) >= need);
  check(`cobertura por dificultad (${sizes.join('/')})`, covered);

  const latex = bank.questions.filter((q) =>
    latexBalanced(q.question) && q.options.every(latexBalanced) && latexBalanced(q.explanation)
  ).length;
  check(`LaTeX íntegro ${latex}/${bank.questions.length}`, latex === bank.questions.length);
}

// Escaleras entre bancos: deben diferir (bancos realmente independientes)
const files = manifest.banks.map((b) => b.file);
const unique = new Set(files).size === files.length;
check('archivos de banco únicos en el manifiesto', unique);

if (failures > 0) {
  console.error(`CHECK FALLÓ: ${failures} verificación(es) fallida(s).`);
  process.exit(1);
}
console.log(`CHECK OK: ${manifest.banks.length} bancos válidos (independientes), ${manifest.banks.reduce((s, b) => s + b.questionCount, 0)} preguntas en total.`);
