// Post-procesado de ecuaciones (Fase 3.b): npm run post:eqrefs (tras astro build).
// KaTeX emite <annotation encoding="application/x-tex"> con el fuente exacto.
// Aquí: `$\ref{id}$` standalone -> enlace, y display con `\tag{X}` -> ancla.
// (No va como plugin rehype: en este stack los rehypePlugins del config no se
//  ejecutan para el contenido; verificado por prueba. El prebuild ya valida.)
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DIST = path.join(ROOT, 'dist');
const BASE = process.env.BASE_PATH || '/Ecoudea';
const index = require('../src/lib/ecuaciones.json');

const REF = /^\\ref\{([A-Za-z0-9:._-]+)\}$/;
const TAG = /\\tag\{([A-Za-z0-9:._-]+)\}/g;

// Extrae el tex de la anotación dentro de un span.katex ya localizado.
function annotationTex(html, from) {
  const m = /<annotation encoding="application\/x-tex">([\s\S]*?)<\/annotation>/.exec(html.slice(from, from + 4000));
  return m ? m[1] : null;
}

// Localiza el span.katex de nivel superior que empieza en `start`.
function outerKatexEnd(html, start) {
  const re = /<\/?span\b[^>]*>/g;
  re.lastIndex = start;
  let depth = 0;
  let m;
  while ((m = re.exec(html))) {
    if (m[0].startsWith('</')) depth--;
    else depth++;
    if (depth === 0) return m.index + m[0].length;
  }
  return -1;
}

let links = 0, anchors = 0, bad = 0;
function processFile(f) {
  let html = fs.readFileSync(f, 'utf8');
  if (!html.includes('application/x-tex')) return;
  let out = '';
  let pos = 0;
  while (true) {
    const start = html.indexOf('<span class="katex">', pos);
    if (start === -1) { out += html.slice(pos); break; }
    const end = outerKatexEnd(html, start);
    if (end === -1) { out += html.slice(pos); break; }
    const tex = (annotationTex(html, start) || '').trim();
    const rm = tex.match(REF);
    if (rm) {
      const label = rm[1];
      const hit = index[label];
      if (!hit || !hit.course) {
        console.error(`[eqref] ref sin destino "${label}" en ${path.relative(DIST, f)}`);
        bad++;
        out += html.slice(pos, end);
      } else {
        out += html.slice(pos, start);
        out += `<a class="eq-ref" href="${BASE}/cursos/${hit.course}/${hit.class}#eq-${label}">(${label})</a>`;
        links++;
      }
      pos = end;
      continue;
    }
    const tms = [...new Set([...tex.matchAll(TAG)].map((m) => m[1]))];
    if (tms.length) {
      // Un align puede numerar varias líneas: un ancla por etiqueta
      // (todas apuntan al bloque; los ids existen y los enlaces funcionan).
      out += html.slice(pos, start);
      for (const label of tms) {
        out += `<span class="eq-anchor" id="eq-${label}" aria-hidden="true"></span>`;
        anchors++;
      }
    } else {
      out += html.slice(pos, start);
    }
    // copiar el propio span.katex intacto
    out += html.slice(start, end);
    pos = end;
  }
  if (out !== html) fs.writeFileSync(f, out);
}

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith('.html')) processFile(p);
  }
}
walk(path.join(DIST, 'cursos'));
if (bad > 0) process.exit(1);
console.log(`[eqref] ${links} refs enlazadas, ${anchors} anclas en dist/cursos.`);
