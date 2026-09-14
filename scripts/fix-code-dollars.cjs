/**
 * Protege los `$` que aparecen dentro de bloques de código HTML (`<pre>`).
 *
 * El HTML crudo de R Markdown suele traer bloques de código resaltados con
 * `<pre class="highlight"><code>…</code></pre>` y a veces contienen líneas en
 * blanco. Esas líneas cortan el HTML block de CommonMark, así que el contenido
 * posterior se parsea como markdown y remark-math empareja los `$` de R
 * (p. ej. `datos$SatisTrabajo`) como si fueran matemáticas, rompiendo el código.
 *
 * Sustituir `$` por `&#36;` dentro de `<pre>…</pre>` evita el problema: el
 * navegador muestra exactamente el mismo carácter.
 *
 * Uso: node scripts/fix-code-dollars.cjs
 */
const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter((f) => f.endsWith('.md'));

let changed = 0;
let escaped = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  const src = fs.readFileSync(filePath, 'utf-8');
  let count = 0;
  const out = src.replace(/<pre\b[\s\S]*?<\/pre>/gi, (block) =>
    block.replace(/\$/g, () => {
      count++;
      return '&#36;';
    }),
  );
  if (out !== src) {
    fs.writeFileSync(filePath, out, 'utf-8');
    changed++;
    escaped += count;
    console.log(`[FIX] ${file} (${count} $)`);
  }
}

console.log(`\n✅ ${escaped} símbolos $ protegidos en ${changed} archivos`);
