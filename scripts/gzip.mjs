// Precomprime todos los assets estáticos para GitHub Pages.
// GitHub Pages sirve el archivo .gz con Content-Encoding: gzip si existe.
// Uso: node scripts/gzip.mjs  (se ejecuta tras `astro build`)
import { gzipSync } from 'node:zlib';
import { readdirSync, statSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const dist = fileURLToPath(new URL('../dist/', import.meta.url));
const compressible = /\.(html|css|js|mjs|svg|json|xml|txt)$/i;

function walk(dir) {
  return readdirSync(dir).flatMap((name) => {
    const full = join(dir, name);
    return statSync(full).isDirectory() ? walk(full) : [full];
  });
}

let count = 0;
let saved = 0;

for (const file of walk(dist)) {
  if (!compressible.test(file)) continue;
  const gz = `${file}.gz`;
  const buf = readFileSync(file);
  const compressed = gzipSync(buf, { level: 9 });
  if (compressed.length >= buf.length) continue; // no beneficio: no generes .gz
  rmSync(gz, { force: true });
  writeFileSync(gz, compressed);
  count++;
  saved += buf.length - compressed.length;
  console.log(`  gzip ${relative(dist, file)} (${(buf.length / 1024).toFixed(1)}KB -> ${(compressed.length / 1024).toFixed(1)}KB)`);
}

console.log(`Gzip: ${count} archivos precomprimidos, ~${(saved / 1024 / 1024).toFixed(2)}MB ahorrados en transferencia.`);
