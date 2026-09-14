/**
 * Normaliza los delimitadores display `$$...$$` del contenido.
 *
 * remark-math (micromark) solo reconoce `$$` como bloque cuando el delimitador
 * está solo en su línea:
 *
 *     $$
 *     \begin{align*} ... \end{align*}
 *     $$
 *
 * El contenido migrado de R Markdown suele traer `$$\begin{align*}` y
 * `\end{align*}$$` en la misma línea que el contenido, lo que hace que se
 * parsee como math inline y falle (o se trague prosa/HTML).
 *
 * Uso: node scripts/fix-math-delims.cjs
 */
const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter((f) => f.endsWith('.md'));

let changed = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  const src = fs.readFileSync(filePath, 'utf-8');
  const match = src.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/);
  const frontmatter = match ? match[1] : '';
  const body = match ? match[2] : src;

  const out = [];
  let fence = false;
  for (const line of body.split('\n')) {
    if (/^\s*(```|~~~)/.test(line)) {
      fence = !fence;
      out.push(line);
      continue;
    }
    if (fence || line.indexOf('$$') === -1) {
      out.push(line);
      continue;
    }

    if (line.trim() === '$$') {
      out.push(line);
      continue;
    }

    // Cada `$$` queda solo en su propia línea.
    const parts = line.split('$$');
    let rebuilt = '';
    for (let i = 0; i < parts.length; i++) {
      if (i > 0) rebuilt += '\n$$\n';
      rebuilt += parts[i];
    }
    out.push(rebuilt.replace(/^\n+/, '').replace(/\n+$/, ''));
  }

  const newBody = out.join('\n');
  if (newBody !== body) {
    fs.writeFileSync(filePath, frontmatter + newBody, 'utf-8');
    changed++;
    console.log(`[FIX] ${file}`);
  }
}

console.log(`\n✅ Delimitadores $$ normalizados en ${changed} archivos`);
