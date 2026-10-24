// Valida enlaces internos del sitio construido: npm run check:links
// Falla si un href interno no resuelve a un archivo en dist/ o si quedó
// alguna referencia a localhost. Se ejecuta en CI tras el build.
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, '..', 'dist');
const BASE = process.env.BASE_PATH || '/Ecoudea';

function files(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) files(p, out);
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

function existsDist(rel) {
  const cands = [path.join(DIST, rel), path.join(DIST, rel + '.html')];
  for (const c of cands) {
    try { if (fs.statSync(c).isFile()) return true; } catch {}
  }
  try { return fs.statSync(path.join(DIST, rel, 'index.html')).isFile(); } catch { return false; }
}

function resolveTarget(href) {
  const clean = href.split('#')[0].split('?')[0];
  if (!clean || !clean.startsWith('/')) return null; // externo, ancla o especial
  let rel = clean;
  if (BASE !== '/' && rel.startsWith(BASE)) rel = rel.slice(BASE.length);
  else if (BASE !== '/' && !rel.startsWith(BASE)) return null; // fuera del sitio (CDN, fuentes)
  rel = rel.replace(/^\/+/, '');
  return existsDist(rel) ? null : clean;
}

let bad = 0;
for (const f of files(DIST)) {
  const html = fs.readFileSync(f, 'utf8');
  if (/(?:https?:)?\/\/localhost(?::\d+)?\//.test(html)) {
    console.error(`[links] ${path.relative(DIST, f)}: referencia a localhost`);
    bad++;
  }
  const seen = new Set();
  const re = /(?:href|src)="([^"]+)"/g;
  let m;
  while ((m = re.exec(html))) {
    const target = resolveTarget(m[1]);
    if (target && !seen.has(target)) {
      seen.add(target);
      console.error(`[links] ${path.relative(DIST, f)} -> roto: ${target}`);
      bad++;
    }
  }
}
if (bad > 0) {
  console.error(`[links] ${bad} problemas.`);
  process.exit(1);
}
console.log('[links] OK: sin enlaces rotos ni referencias a localhost.');
