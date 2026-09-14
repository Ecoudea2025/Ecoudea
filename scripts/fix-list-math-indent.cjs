/**
 * Re-indenta los bloques display `$$ … $$` que quedaron dentro de ítems de
 * lista tras separarlos en su propia línea.
 *
 * Cuando un `$$…$$` está dentro de un ítem (`1.  texto` seguido de contenido
 * indentado 4 espacios) y el bloque queda a columna 0, CommonMark cierra el
 * ítem: el contenido indentado que sigue (p. ej. `<ol type="a">`) pasa a ser un
 * bloque de código y se muestra el HTML literal. Re-indentar el bloque por la
 * indentación del ítem mantiene la lista y renderiza el HTML.
 *
 * Uso: node scripts/fix-list-math-indent.cjs
 */
const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter((f) => f.endsWith('.md'));

const LIST_ITEM = /^(\s*)(\d+\.|[-*+])\s/;
const indentOf = (line) => (line.match(/^\s*/) || [''])[0].length;

let changed = 0;
let reindented = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  const src = fs.readFileSync(filePath, 'utf-8');
  const match = src.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/);
  const frontmatter = match ? match[1] : '';
  const body = match ? match[2] : src;

  const lines = body.split('\n');
  const out = lines.slice();
  let count = 0;

  let i = 0;
  while (i < lines.length) {
    if (lines[i] !== '$$') {
      i++;
      continue;
    }

    // Cierre del bloque.
    let j = i + 1;
    while (j < lines.length && lines[j] !== '$$') j++;
    if (j >= lines.length) {
      i++;
      continue;
    }

    // ¿El bloque pertenece a un ítem de lista?
    let before = i - 1;
    while (before >= 0 && lines[before].trim() === '') before--;
    let after = j + 1;
    while (after < lines.length && lines[after].trim() === '') after++;

    const beforeIndent = before >= 0 ? indentOf(lines[before]) : 0;
    const afterIndent = after < lines.length ? indentOf(lines[after]) : 0;

    // Marcador de lista más cercano hacia arriba: la primera línea no vacía
    // con indentación 0 debe ser un ítem de lista; si no, el bloque es de
    // nivel superior y no se toca.
    let listMarked = false;
    for (let k = before; k >= 0; k--) {
      if (lines[k].trim() === '') continue;
      if (indentOf(lines[k]) === 0) {
        listMarked = LIST_ITEM.test(lines[k]);
        break;
      }
    }

    const pad = beforeIndent > 0 ? beforeIndent : afterIndent;
    const inListItem = listMarked && pad >= 2 && (beforeIndent >= 2 || afterIndent >= 4);

    if (inListItem) {
      const prefix = ' '.repeat(pad);
      for (let k = i; k <= j; k++) {
        if (out[k] === '') continue;
        if (indentOf(out[k]) === 0) out[k] = prefix + out[k];
      }
      count++;
    }

    i = j + 1;
  }

  if (count > 0 && out.join('\n') !== body) {
    fs.writeFileSync(filePath, frontmatter + out.join('\n'), 'utf-8');
    changed++;
    reindented += count;
    console.log(`[FIX] ${file} (${count} bloques)`);
  }
}

console.log(`\n✅ ${reindented} bloques re-indentados en ${changed} archivos`);
