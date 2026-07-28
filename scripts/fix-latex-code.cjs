const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter(f => f.endsWith('.md'));

let fixed = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  let original = content;

  // Find backtick-wrapped \begin{align}...\end{align} and convert to $$...$$
  content = content.replace(
    /`\\begin\{(align\*?|equation\*?)\}([\s\S]*?)\\end\{(align\*?|equation\*?)\}`/g,
    (match, env1, inner, env2) => {
      // Clean up the inner content - remove leading/trailing whitespace per line
      const cleaned = inner.replace(/\n\s+/g, '\n').trim();
      return `\n$$\\begin{${env1}}${cleaned}\\end{${env2}}$$\n`;
    }
  );

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf-8');
    fixed++;
    console.log(`[FIX] ${file}`);
  }
}

console.log(`\n✅ ${fixed} archivos con LaTeX en backticks corregidos`);
