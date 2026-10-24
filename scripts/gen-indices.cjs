// Índice de ecuaciones etiquetadas: npm run equations (o prebuild automático).
// Recorre las clases ACTIVAS (no drafts) buscando `\tag{etiqueta}` en math
// display y escribe src/lib/ecuaciones.json { etiqueta: {course, class} }.
// Falla con error legible si una etiqueta se repite (referencias ambiguas).
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const CLASSES = path.join(ROOT, 'src', 'content', 'classes');
const OUT = path.join(ROOT, 'src', 'lib', 'ecuaciones.json');

function frontmatter(text) {
  const m = text.match(/^---\n([\s\S]*?)\n---\n?/);
  const body = m ? text.slice(m[0].length) : text;
  const fm = (m ? m[1] : '');
  const get = (k) => (fm.match(new RegExp(`^${k}:\\s*\"?([^\"\\n]+)\"?`, 'm')) || [])[1] || '';
  return { body, course: get('course').trim(), draft: /^\s*draft:\s*true/m.test(fm) };
}

const index = {};
const seen = {};
let files = 0;
for (const f of fs.readdirSync(CLASSES).filter((f) => f.endsWith('.md'))) {
  const { body: raw, course, draft } = frontmatter(fs.readFileSync(path.join(CLASSES, f), 'utf8'));
  if (draft) continue;
  files++;
  // Ignorar comentarios HTML (suelen documentar la sintaxis con ejemplos).
  const body = raw.replace(/<!--[\s\S]*?-->/g, '');
  const re = /\\tag\{([A-Za-z0-9:._-]+)\}/g;
  let m;
  while ((m = re.exec(body))) {
    const label = m[1];
    if (seen[label]) {
      console.error(`[ecuaciones] etiqueta duplicada "${label}": ${seen[label]} y ${f}. Renombra un \\tag{...}.`);
      process.exit(1);
    }
    seen[label] = f;
    index[label] = { course, class: f.replace(/\.md$/, '') };
  }
}
fs.writeFileSync(OUT, JSON.stringify(index, null, 2) + '\n');
console.log(`[ecuaciones] ${Object.keys(index).length} etiquetas en ${files} clases -> src/lib/ecuaciones.json`);

// ── Validar referencias: `$\ref{id}$` standalone debe existir ─────────
// (Astro 7 tolera errores de render y genera el artículo vacío, así que la
//  garantía de fallo va aquí, en Node puro, no en el plugin remark.)
const REF = /\$\\ref\{([A-Za-z0-9:._-]+)\}\$/g;
let bad = 0;
for (const f of fs.readdirSync(CLASSES).filter((f) => f.endsWith('.md'))) {
  const { body: raw, draft } = frontmatter(fs.readFileSync(path.join(CLASSES, f), 'utf8'));
  if (draft) continue;
  const body = raw.replace(/<!--[\s\S]*?-->/g, '');
  let m;
  while ((m = REF.exec(body))) {
    if (!index[m[1]]) {
      console.error(`[eqref] referencia a ecuación inexistente "${m[1]}" en ${f}. Etiqueta con \\tag{${m[1]}} en alguna clase publicada o corrige el \\ref.`);
      bad++;
    }
  }
}
if (bad > 0) process.exit(1);

// ── Glosario: `<Term id="x">etiqueta</Term>` + `conceptos:` del frontmatter ─
// Escribe src/lib/glosario.json { id: { label, refs: [{course, class, classTitle}] } }.
// Sin definiciones redactadas: es un índice (dónde se explica cada término).
function slug(s) {
  return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

const terms = {};
function addTerm(id, label, course, classId, classTitle) {
  if (!id) return;
  if (!terms[id]) terms[id] = { label, refs: [] };
  if (!terms[id].refs.some((r) => r.class === classId)) {
    terms[id].refs.push({ course, class: classId, classTitle });
  }
}

for (const f of fs.readdirSync(CLASSES).filter((f) => f.endsWith('.md'))) {
  const raw = fs.readFileSync(path.join(CLASSES, f), 'utf8');
  const { body, course, draft } = frontmatter(raw);
  if (draft) continue;
  const classId = f.replace(/\.md$/, '');
  const titleM = raw.match(/^title:\s*"([^"\n]+)"/m);
  const classTitle = titleM ? titleM[1] : classId;
  const clean = body.replace(/<!--[\s\S]*?-->/g, '');
  // 1) <Term id="x">Etiqueta</Term> en el cuerpo
  const tre = /<Term\s+id="([A-Za-z0-9:._-]+)"\s*>([\s\S]*?)<\/Term\s*>/g;
  let tm;
  while ((tm = tre.exec(clean))) {
    const label = tm[2].replace(/<[^>]+>/g, '').trim() || tm[1];
    addTerm(tm[1], label, course, classId, classTitle);
  }
  // 2) conceptos: ["A", "B"] del frontmatter
  const cm = raw.match(/^conceptos:\s*\[([^\]\n]*)\]/m);
  if (cm) {
    for (const c of cm[1].split(',')) {
      const label = c.replace(/["']/g, '').trim();
      if (label) addTerm(slug(label), label, course, classId, classTitle);
    }
  }
}
const ordered = Object.fromEntries(Object.entries(terms).sort((a, b) => a[1].label.localeCompare(b[1].label, 'es')));
fs.writeFileSync(path.join(ROOT, 'src', 'lib', 'glosario.json'), JSON.stringify(ordered, null, 2) + '\n');
console.log(`[glosario] ${Object.keys(ordered).length} términos -> src/lib/glosario.json`);
