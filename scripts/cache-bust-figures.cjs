// Cache-busting de figuras (Fase anti-caché): npm run post:figcache (tras astro build).
// Los SVG de /assets/figures/ se sirven con cache-first (SW) + CDN: sin versión
// en la URL, un redeploy puede seguir mostrando la figura vieja tras F5.
// Aquí: `.../fig-light.svg` -> `.../fig-light.svg?v=<BUILD_ID>` en el HTML de dist.
// BUILD_ID = short hash del commit (estable por contenido) o timestamp.
// Solo dist/ (nunca src/); idempotente (no duplica ?v=); no toca _astro (ya trae hash).
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
const DIST = path.join(ROOT, 'dist');

function buildId() {
  try {
    return execSync('git rev-parse --short HEAD', { cwd: ROOT, encoding: 'utf8' }).trim();
  } catch (e) {
    return String(Date.now());
  }
}

const V = buildId();
const RE = /src="([^"]*\/assets\/figures\/[^"]+?\.(?:svg|webp|png))"/g;

let files = 0, hits = 0;
function processFile(f) {
  let html = fs.readFileSync(f, 'utf8');
  if (!html.includes('/assets/figures/')) return;
  let n = 0;
  const out = html.replace(RE, (m, u) => {
    if (u.includes('?')) return m;
    n++;
    return `src="${u}?v=${V}"`;
  });
  if (n > 0) {
    fs.writeFileSync(f, out);
    files++;
    hits += n;
  }
}

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith('.html')) processFile(p);
  }
}
walk(DIST);
console.log(`[figcache] ?v=${V} en ${hits} figuras (${files} HTML).`);
