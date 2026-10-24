// Valida matemáticas renderizadas: npm run check:math
// Falla si alguna página construida contiene spans .katex-error (fórmula rota).
// Es la red de seguridad para el contenido que aporta el autor: el build no
// falla por LaTeX inválido (KaTeX lo renderiza en rojo), así que se verifica aquí.
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, '..', 'dist');

function files(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) files(p, out);
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

let bad = 0;
for (const f of files(DIST)) {
  let html = fs.readFileSync(f, 'utf8');
  const re = /katex-error" title="([^"]{0,140})/g;
  let m;
  while ((m = re.exec(html))) {
    bad++;
    console.error(`[math] ${path.relative(DIST, f)}: ${m[1].slice(0, 120)}`);
  }
  // Delimitadores display sin convertir (fuera de <script> y comentarios;
  // ojo: <!-- --> del autor puede contener $$ de borradores). KaTeX nunca
  // emite `$$` literales.
  const noScript = html.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<!--[\s\S]*?-->/g, '');
  const dm = noScript.match(/\$\$/g);
  if (dm) {
    bad++;
    console.error(`[math] ${path.relative(DIST, f)}: ${dm.length / 2} bloque(s) $$ sin convertir.`);
  }
}
if (bad > 0) {
  console.error(`[math] ${bad} fórmula(s) rota(s). Revisa el TeX indicado arriba.`);
  process.exit(1);
}
console.log('[math] OK: cero fórmulas rotas en el sitio construido.');
