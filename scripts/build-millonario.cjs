#!/usr/bin/env node
/**
 * build-millonario.cjs — Construye UN banco INDEPENDIENTE por curso desde
 * data/millonario-src/<curso>/*.json. Sin mezclas entre cursos.
 *
 * Cada parcial NO trae id ni source: el script asigna ids únicos por banco
 * (<curso>-001, ...) y toma `source` del campo "class" del parcial,
 * verificado contra src/content/classes/.
 *
 * Config del juego derivada del tamaño del banco (niveles = tantas preguntas):
 *   safeHavens = [floor(n/3), floor(2n/3)]  — p.ej. 10 → [3,6]; 20 → [6,13]
 *   prizes     = generador geométrico: 100 → 1.000 (⅓) → 10.000 (⅔) → 1.000.000 (tope)
 *
 * Salida: public/assets/data/millonario-<curso>.json
 *         public/assets/data/millonario-index.json  (manifiesto para la intro)
 *
 * Uso: node scripts/build-millonario.cjs
 * Después: node scripts/check-millonario.cjs
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { validate, countPerLevel, levelSizes, niceRound } = require('./millonario-lib.cjs');

const ROOT = path.resolve(__dirname, '..');
const SRC_DIR = path.join(ROOT, 'data', 'millonario-src');
const CLASSES_DIR = path.join(ROOT, 'src', 'content', 'classes');
const DATA_OUT = path.join(ROOT, 'public', 'assets', 'data');

const COURSE_TITLES = {
  'estadistica-ii': 'Estadística II',
  'macroeconomia-i': 'Macroeconomía I'
};

function fail(msg) {
  console.error('BUILD FALLÓ: ' + msg);
  process.exit(1);
}

function courseTitle(id) {
  return COURSE_TITLES[id] || id
    .split('-')
    .map((w) => (w ? w.charAt(0).toUpperCase() + w.slice(1) : w))
    .join(' ');
}

/** Escalera de premios para n niveles (refugios en ⅓ y ⅔, tope 1.000.000). */
function gamePrizes(n) {
  const havens = [Math.max(2, Math.floor(n / 3)), Math.max(3, Math.floor(2 * n / 3))];
  const h1 = havens[0];
  const h2 = havens[1];
  const prizes = [];
  for (let lv = 1; lv <= n; lv++) {
    let v;
    if (lv === h1) v = 1000;                 // refugio 1
    else if (lv === h2) v = 10000;           // refugio 2
    else if (lv === n) v = 1000000;          // tope del juego
    else if (lv < h1) v = 100 * Math.pow(10, (lv - 1) / Math.max(1, h1 - 1));
    else if (lv < h2) v = 1000 * Math.pow(10, (lv - h1) / Math.max(1, h2 - h1));
    else v = 10000 * Math.pow(100, (lv - h2) / Math.max(1, n - h2));
    prizes.push(niceRound(v));
  }
  return prizes;
}

// --- Barrer directorios de curso ------------------------------------------
if (!fs.existsSync(SRC_DIR)) fail('No existe ' + SRC_DIR);

const knownSources = new Set(fs.readdirSync(CLASSES_DIR).filter((f) => f.endsWith('.md')));
const conflicts = fs.readdirSync(SRC_DIR).filter((f) => f.endsWith('.json'));
if (conflicts.length > 0) {
  fail(`Los parciales deben vivir en una carpeta de curso (data/millonario-src/<curso>/). Suelto(s): ${conflicts.join(', ')}`);
}

const courseDirs = fs.readdirSync(SRC_DIR).filter((f) =>
  fs.statSync(path.join(SRC_DIR, f)).isDirectory()
).sort();
if (courseDirs.length === 0) fail('No hay carpetas de curso en ' + SRC_DIR);

const index = [];

for (const course of courseDirs) {
  const dir = path.join(SRC_DIR, course);
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.json')).sort();
  if (files.length === 0) fail(`${course}: no hay parciales`);

  let pool = [];
  for (const file of files) {
    const raw = fs.readFileSync(path.join(dir, file), 'utf8');
    let doc;
    try {
      doc = JSON.parse(raw);
    } catch (e) {
      fail(`${course}/${file}: JSON inválido (${e.message}).`);
    }
    if (!Array.isArray(doc.questions) || doc.questions.length === 0) {
      fail(`${course}/${file}: falta el array "questions" (no vacío).`);
    }
    if (typeof doc.class !== 'string' || !/^[a-z0-9-]+$/.test(doc.class)) {
      fail(`${course}/${file}: "class" ausente o inválido.`);
    }
    if (!doc.class.startsWith(course + '-')) {
      fail(`${course}/${file}: la clase ${doc.class} no pertenece al curso ${course}.`);
    }
    if (typeof doc.category !== 'string' || doc.category.trim().length === 0) {
      fail(`${course}/${file}: falta "category".`);
    }
    const source = doc.class + '.md';
    if (!knownSources.has(source)) {
      fail(`${course}/${file}: la clase ${source} no existe en src/content/classes/.`);
    }
    doc.questions.forEach((q, i) => {
      if (q && q.id !== undefined) fail(`${course}/${file}: pregunta ${i} trae "id" (los ids los asigna el build).`);
      if (q && q.difficulty !== undefined && !Number.isInteger(q.difficulty)) {
        fail(`${course}/${file}: pregunta ${i} con dificultad no entera.`);
      }
      pool.push({ ...q, category: doc.category, source });
    });
  }

  pool.sort((a, b) =>
    (a.difficulty - b.difficulty) || (a.source.localeCompare(b.source))
  );
  pool.forEach((q, i) => {
    q.id = `${course}-${String(i + 1).padStart(3, '0')}`;
  });

  const n = pool.length;
  const sizes = levelSizes(n);
  const havens = [Math.floor(n / 3), Math.floor(2 * n / 3)];
  const config = {
    questionsPerGame: n,
    timePerQuestion: 30,
    safeHavens: havens,
    lifelines: { fifty50: true, skip: true, audience: true },
    prizes: gamePrizes(n)
  };
  const perLevel = countPerLevel(pool);

  // Cobertura: cada bucket de dificultad necesita todas sus preguntas jugables.
  const shortages = [];
  for (let d = 1; d <= 5; d++) {
    const need = sizes[d - 1];
    const have = perLevel[String(d)] || perLevel[d] || 0;
    if (have < need) shortages.push(`dificultad ${d}: necesita ${need}, hay ${have}`);
  }
  if (shortages.length > 0) {
    fail(`${course}: el banco no alcanza para ${n} niveles → ${shortages.join('; ')}`);
  }

  const bank = {
    meta: {
      id: course,
      courseTitle: courseTitle(course),
      title: `¿Quién quiere ser millonario? — ${courseTitle(course)}`,
      language: 'es',
      version: '2.0.0',
      updated: new Date().toISOString().slice(0, 10),
      generator: 'scripts/build-millonario.cjs',
      questionCount: pool.length,
      levels: n,
      perLevel,
      sources: [...new Set(pool.map((q) => q.source))]
    },
    config,
    questions: pool
  };

  const errors = validate(bank, { knownSources });
  if (errors.length > 0) {
    console.error(`BUILD FALLÓ: el banco ${course} tiene ${errors.length} error(es):`);
    errors.forEach((e) => console.error('  - ' + e));
    process.exit(1);
  }

  const out = path.join(DATA_OUT, `millonario-${course}.json`);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, JSON.stringify(bank, null, 2) + '\n', 'utf8');
  console.log(`OK: ${course} → ${pool.length} preguntas, ${n} niveles, refugios ${havens.join('/')} → ${path.relative(ROOT, out)}`);
  console.log(`   Por dificultad: ${Object.entries(perLevel).map(([k, v]) => `N${k}=${v}`).join('  ')}`);
  console.log(`   Escalera: ${config.prizes.join(', ')}`);
  console.log(`   Fuentes: ${bank.meta.sources.join(', ')}`);

  index.push({
    id: course,
    title: courseTitle(course),
    file: `millonario-${course}.json`,
    questionCount: pool.length,
    levels: n,
    safeHavens: havens,
    topPrize: config.prizes[n - 1]
  });
}

// --- Manifiesto para la intro (bancos independientes) ----------------------
const indexPath = path.join(DATA_OUT, 'millonario-index.json');
fs.writeFileSync(indexPath, JSON.stringify({ banks: index }, null, 2) + '\n', 'utf8');
console.log(`OK: ${index.length} bancos → ${path.relative(ROOT, indexPath)}`);
