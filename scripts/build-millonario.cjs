#!/usr/bin/env node
/**
 * build-millonario.cjs — Fusiona los parciales de data/millonario-src/
 * en public/assets/data/millonario.json (banco consolidado).
 *
 * Los parciales NO traen id ni source: el script asigna ids únicos
 * (mq-001, mq-002, ...) ordenadas por dificultad y toma `source` del
 * campo "class" de cada parcial, verificado contra src/content/classes/.
 *
 * Uso: node scripts/build-millonario.cjs
 * Después: node scripts/check-millonario.cjs
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { validate, countPerLevel } = require('./millonario-lib.cjs');

const ROOT = path.resolve(__dirname, '..');
const SRC_DIR = path.join(ROOT, 'data', 'millonario-src');
const CLASSES_DIR = path.join(ROOT, 'src', 'content', 'classes');
const OUT = path.join(ROOT, 'public', 'assets', 'data', 'millonario.json');

/** Configuración del juego (única fuente de verdad, se copia a cada build). */
const CONFIG = {
  questionsPerGame: 15,
  timePerQuestion: 30,
  safeHavens: [5, 10],
  lifelines: { fifty50: true, skip: true, audience: true },
  prizes: [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
};

function fail(msg) {
  console.error('BUILD FALLÓ: ' + msg);
  process.exit(1);
}

// --- Cargar parciales ------------------------------------------------------
if (!fs.existsSync(SRC_DIR)) fail('No existe ' + SRC_DIR);

const files = fs.readdirSync(SRC_DIR).filter((f) => f.endsWith('.json')).sort();
if (files.length === 0) fail('No hay parciales en ' + SRC_DIR);

let pool = [];

for (const file of files) {
  const raw = fs.readFileSync(path.join(SRC_DIR, file), 'utf8');
  let doc;
  try {
    doc = JSON.parse(raw);
  } catch (e) {
    fail(`${file}: JSON inválido (${e.message}).`);
  }

  if (!Array.isArray(doc.questions) || doc.questions.length === 0) {
    fail(`${file}: falta el array "questions" (no vacío).`);
  }
  if (typeof doc.class !== 'string' || !/^[a-z0-9-]+$/.test(doc.class)) {
    fail(`${file}: "class" ausente o inválido.`);
  }
  if (typeof doc.category !== 'string' || doc.category.trim().length === 0) {
    fail(`${file}: falta "category".`);
  }

  const source = doc.class + '.md';
  if (!fs.existsSync(path.join(CLASSES_DIR, source))) {
    fail(`${file}: la clase ${source} no existe en src/content/classes/.`);
  }

  doc.questions.forEach((q, i) => {
    if (q && q.id !== undefined) fail(`${file}: pregunta ${i} trae "id" (los parciales no deben incluirlo; el build lo asigna).`);
    if (q && q.difficulty !== undefined && !Number.isInteger(q.difficulty)) {
      fail(`${file}: pregunta ${i} con dificultad no entera.`);
    }
    pool.push({ ...q, category: doc.category, source });
  });
}

// --- Ordenar (dificultad asc, luego clase y posición estable) ---------------
pool.sort((a, b) =>
  (a.difficulty - b.difficulty) || (a.source.localeCompare(b.source))
);

// --- Asignar ids únicos ------------------------------------------------------
pool.forEach((q, i) => {
  q.id = 'mq-' + String(i + 1).padStart(3, '0');
});

// --- Banco consolidado -------------------------------------------------------
const perLevel = countPerLevel(pool);
const bank = {
  meta: {
    title: '¿Quién quiere ser millonario? — Ecoudea',
    language: 'es',
    version: '1.0.0',
    updated: new Date().toISOString().slice(0, 10),
    generator: 'scripts/build-millonario.cjs',
    questionCount: pool.length,
    perLevel,
    sources: [...new Set(pool.map((q) => q.source))]
  },
  config: CONFIG,
  questions: pool
};

// --- Validar antes de escribir ------------------------------------------------
const knownSources = new Set(
  fs.readdirSync(CLASSES_DIR).filter((f) => f.endsWith('.md'))
);
const errors = validate(bank, { knownSources });
if (errors.length > 0) {
  console.error('BUILD FALLÓ: el banco consolidado tiene ' + errors.length + ' error(es):');
  errors.forEach((e) => console.error('  - ' + e));
  process.exit(1);
}

// --- Escribir ------------------------------------------------------------------
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(bank, null, 2) + '\n', 'utf8');

console.log(`OK: ${pool.length} preguntas → ${path.relative(ROOT, OUT)}`);
console.log('   Por nivel: ' + Object.entries(perLevel).map(([k, v]) => `N${k}=${v}`).join('  '));
console.log('   Fuentes: ' + bank.meta.sources.join(', '));
