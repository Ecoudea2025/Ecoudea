#!/usr/bin/env node
/**
 * check-millonario.cjs — Gate del banco de preguntas del millonario.
 * Valida public/assets/data/millonario.json contra el esquema del plan:
 * estructura, 4 opciones, 1 correcta, ids únicos, dificultad 1..5,
 * ≥ 3 preguntas por nivel, source verificable, LaTeX balanceado,
 * sin opciones duplicadas, sin "todas/ninguna de las anteriores".
 *
 * Uso: node scripts/check-millonario.cjs   (exit 0 = OK, 1 = falla)
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { validate, countPerLevel, latexBalanced } = require('./millonario-lib.cjs');

const ROOT = path.resolve(__dirname, '..');
const BANK = path.join(ROOT, 'public', 'assets', 'data', 'millonario.json');
const CLASSES_DIR = path.join(ROOT, 'src', 'content', 'classes');

if (!fs.existsSync(BANK)) {
  console.error('CHECK FALLÓ: no existe public/assets/data/millonario.json (corre primero scripts/build-millonario.cjs).');
  process.exit(1);
}

let bank;
try {
  bank = JSON.parse(fs.readFileSync(BANK, 'utf8'));
} catch (e) {
  console.error('CHECK FALLÓ: JSON inválido — ' + e.message);
  process.exit(1);
}

const knownSources = fs.existsSync(CLASSES_DIR)
  ? new Set(fs.readdirSync(CLASSES_DIR).filter((f) => f.endsWith('.md')))
  : null;

const errors = validate(bank, { knownSources });

if (errors.length > 0) {
  console.error('CHECK FALLÓ: ' + errors.length + ' error(es):');
  errors.forEach((e) => console.error('  - ' + e));
  process.exit(1);
}

// Área de cross-check live disponible en el html output (metadatos extra)
const per = countPerLevel(bank.questions);
const latex = bank.questions.filter((q) =>
  latexBalanced(q.question) && q.options.every(latexBalanced) && latexBalanced(q.explanation)
).length;

console.log(`CHECK OK: ${bank.questions.length} preguntas, version ${bank.meta.version} (${bank.meta.updated}).`);
console.log('  Por nivel: ' + Object.entries(per).map(([k, v]) => `N${k}=${v}`).join('  '));
console.log(`  ${latex}/${bank.questions.length} con LaTeX íntegro.`);
