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
  const re = /\\tag\{([A-Za-z0-9:_-]+)\}/g;
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
const REF = /\$\\ref\{([A-Za-z0-9:_-]+)\}\$/g;
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
