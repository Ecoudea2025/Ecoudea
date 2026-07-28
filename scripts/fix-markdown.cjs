const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter(f => f.endsWith('.md'));

let linkCount = 0;
let mathCount = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  let original = content;

  // Fix 1: Convert {:target="..."} Jekyll syntax to real HTML links
  // Pattern: [text](url){:target="_blank"} or similar
  content = content.replace(
    /\[([^\]]+)\]\(([^\)]+)\)\{:target="[^"]+"\}/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
  );

  // Fix 2: Replace \[ \] display math delimiters with $$ $$
  // Pattern: \[\begin{align*}...\end{align*}\] -> $$\begin{align*}...\end{align*}$$
  content = content.replace(
    /\\\[(\\begin\{(align|equation)\*?\}[\s\S]*?\\end\{(align|equation)\*?\})\\\]/g,
    '$$$$$1$$$$'
  );
  // Also handle simple \[ ... \] cases (without align environment)
  content = content.replace(
    /\\\[([\s\S]*?)\\\]/g,
    (match, inner) => {
      // Only convert if it contains LaTeX math (has \ or $$ already)
      if (/\\[a-zA-Z]/.test(inner) || /\$\$/.test(inner)) {
        return '$$' + inner + '$$';
      }
      return match;
    }
  );

  if (content !== original) {
    if (original !== content.replace(/\[([^\]]+)\]\(([^\)]+)\)\{:target="[^"]+"\}/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')) {
      linkCount++;
    }
    if (original !== content.replace(/\\\[/g, '$$').replace(/\\\]/g, '$$')) {
      mathCount++;
    }
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`[FIX] ${file}`);
  }
}

console.log(`\n✅ Enlaces Jekyll convertidos en ${linkCount} archivos`);
console.log(`✅ Delimitadores \[ \] → \$ \$ en ${mathCount} archivos`);
