/**
 * Corrige listas numeradas que quedan pegadas a bloques de HTML crudo.
 *
 * El HTML crudo de R Markdown (`</ol>`) es un HTML block tipo 6 en CommonMark:
 * continúa hasta una línea en blanco. Si justo después viene un item `29.`
 * sin línea en blanco, ese item se renderiza como texto (no `<li>`), por lo
 * que la lista pierde el formato 1. / 2. o se "traga" el número.
 *
 * Uso: node scripts/fix-lists.cjs
 */
const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter((f) => f.endsWith('.md'));

const HTML_CLOSER = /^\s*<\/(ol|ul|li|div|table|p|blockquote)>\s*$/;
const NUMBERED_ITEM = /^\s*\d+\.\s/;
const DISPLAY_CLOSE = /^\s*\$\$\s*$/;

let changed = 0;
let inserted = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  const src = fs.readFileSync(filePath, 'utf-8');
  const match = src.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/);
  const frontmatter = match ? match[1] : '';
  const body = match ? match[2] : src;

  const lines = body.split('\n');
  const out = [];
  let added = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const prev = out.length ? out[out.length - 1] : '';
    if (
      NUMBERED_ITEM.test(line) &&
      prev !== '' &&
      (HTML_CLOSER.test(prev) || DISPLAY_CLOSE.test(prev))
    ) {
      out.push('');
      added++;
    }
    out.push(line);
  }

  const newBody = out.join('\n');
  if (newBody !== body) {
    fs.writeFileSync(filePath, frontmatter + newBody, 'utf-8');
    changed++;
    inserted += added;
    console.log(`[FIX] ${file} (+${added})`);
  }
}

console.log(`\n✅ Listas corregidas en ${changed} archivos (${inserted} líneas en blanco)`);
