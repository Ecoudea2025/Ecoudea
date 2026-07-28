const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');

const files = fs.readdirSync(classesDir).filter(f => f.endsWith('.md'));

const byCourse = {};
for (const file of files) {
  const content = fs.readFileSync(path.join(classesDir, file), 'utf-8');
  const courseMatch = content.match(/course:\s*"([^"]+)"/);
  if (!courseMatch) continue;
  const course = courseMatch[1];
  if (!byCourse[course]) byCourse[course] = [];
  byCourse[course].push({ file, content });
}

for (const [course, entries] of Object.entries(byCourse)) {
  entries.sort((a, b) => {
    const getType = (c) => {
      const m = c.content.match(/classType:\s*"([^"]+)"/);
      return m ? m[1] : 'clase';
    };
    const getTitle = (c) => {
      const m = c.content.match(/title:\s*"([^"]+)"/);
      return m ? m[1] : '';
    };

    const typeA = getType(a);
    const typeB = getType(b);
    const priority = { presentacion: 0, clase: 1, practica: 2, guia: 3 };
    const pA = priority[typeA] ?? 1;
    const pB = priority[typeB] ?? 1;

    if (pA !== pB) return pA - pB;

    // Within same type, sort by title number (Clase 01 < Clase 02 < ... < Clase 20)
    const titleA = getTitle(a);
    const titleB = getTitle(b);

    // Extract the numeric part from title like "Clase 01" or "Práctica 05" or "Presentación Curso"
    const numA = parseInt(titleA.match(/\d+/)?.[0] || '0', 10);
    const numB = parseInt(titleB.match(/\d+/)?.[0] || '0', 10);

    // For presentacion, put it first (it has no number or number 0)
    if (typeA === 'presentacion') return -1;
    if (typeB === 'presentacion') return 1;

    return numA - numB;
  });

  let order = 1;
  for (const entry of entries) {
    const newContent = entry.content.replace(/order:\s*\d+/, `order: ${order}`);
    fs.writeFileSync(path.join(classesDir, entry.file), newContent, 'utf-8');
    console.log(`[ORDER] ${entry.file} → order ${order}`);
    order++;
  }
}

console.log('\n✅ Órdenes corregidas (versión 2)');
