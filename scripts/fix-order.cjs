const fs = require('fs');
const path = require('path');

const classesDir = path.resolve(__dirname, '../src/content/classes');

const files = fs.readdirSync(classesDir).filter(f => f.endsWith('.md'));

// Group by course
const byCourse = {};
for (const file of files) {
  const content = fs.readFileSync(path.join(classesDir, file), 'utf-8');
  const match = content.match(/course:\s*"([^"]+)"/);
  if (!match) continue;
  const course = match[1];
  if (!byCourse[course]) byCourse[course] = [];
  byCourse[course].push({ file, content });
}

// For each course, sort: presentacion first, then clases sorted by current order, then practicas
for (const [course, entries] of Object.entries(byCourse)) {
  entries.sort((a, b) => {
    const getType = (c) => {
      const m = c.content.match(/classType:\s*"([^"]+)"/);
      return m ? m[1] : 'clase';
    };
    const getOrder = (c) => {
      const m = c.content.match(/order:\s*(\d+)/);
      return m ? parseInt(m[1]) : 999;
    };

    const typeA = getType(a);
    const typeB = getType(b);

    // Type priority: presentacion=0, clase=1, practica=2, guia=3
    const priority = { presentacion: 0, clase: 1, practica: 2, guia: 3 };
    const pA = priority[typeA] ?? 1;
    const pB = priority[typeB] ?? 1;

    if (pA !== pB) return pA - pB;
    return getOrder(a) - getOrder(b);
  });

  // Re-assign order
  let order = 1;
  for (const entry of entries) {
    const newContent = entry.content.replace(/order:\s*\d+/, `order: ${order}`);
    fs.writeFileSync(path.join(classesDir, entry.file), newContent, 'utf-8');
    console.log(`[ORDER] ${entry.file} → order ${order}`);
    order++;
  }
}

console.log('\n✅ Órdenes corregidas');
