const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');
const files = fs.readdirSync(classesDir).filter(f => f.endsWith('.md'));

let fixedCount = 0;

for (const file of files) {
  const filePath = path.join(classesDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  const original = content;

  // Replace ALL relative image references like ../../Dir/images/ or ../Dir/images/
  content = content.replace(/\.\.\/\.\.\/[^/]+\/images\//g, '/assets/images/');
  content = content.replace(/\.\.\/[^/]+\/images\//g, '/assets/images/');

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf-8');
    fixedCount++;
    console.log(`[FIX] ${file}`);
  }
}

console.log(`\n✅ ${fixedCount} archivos actualizados`);
