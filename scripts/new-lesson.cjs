// Scaffold de clase nueva: npm run new:lesson -- <curso> <slug> [--title ..] [--type clase] [--order N] [--description ..]
// Crea src/content/classes/<curso>-<slug>.md con plantilla comentada. No toca nada más.
const fs = require('fs');
const path = require('path');

function arg(name, def = '') {
  const i = process.argv.indexOf('--' + name);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

const [course, slug] = [process.argv[2], process.argv[3]];
if (!course || !slug || course.startsWith('--') || slug.startsWith('--')) {
  console.error('Uso: npm run new:lesson -- <curso> <slug> [--title "…"] [--type clase|practica|guia|resumen] [--order N] [--description "…"]');
  process.exit(1);
}
const coursesDir = path.join(__dirname, '..', 'src', 'content', 'courses');
if (!fs.existsSync(path.join(coursesDir, course + '.md'))) {
  console.error(`No existe el curso "${course}". Créalo con: npm run new:course -- ${course}`);
  process.exit(1);
}
const classesDir = path.join(__dirname, '..', 'src', 'content', 'classes');
const file = path.join(classesDir, `${course}-${slug}.md`);
if (fs.existsSync(file)) {
  console.error(`Ya existe ${file}`);
  process.exit(1);
}
const sameCourse = fs.readdirSync(classesDir).filter((f) => f.startsWith(course + '-') && f.endsWith('.md'));
const maxOrder = sameCourse.reduce((m, f) => {
  const t = fs.readFileSync(path.join(classesDir, f), 'utf8').match(/^order:\s*(\d+)/m);
  return Math.max(m, t ? parseInt(t[1], 10) : 0);
}, 0);
const title = arg('title', 'Clase ' + String(maxOrder + 1).padStart(2, '0'));
const type = arg('type', 'clase');
if (!['clase', 'practica', 'guia', 'resumen'].includes(type)) {
  console.error('type debe ser: clase|practica|guia|resumen');
  process.exit(1);
}
const order = parseInt(arg('order', String(maxOrder + 1)), 10);
const description = arg('description', 'Resumen de la clase (editar).');

const body = `---
title: "${title.replace(/"/g, '\\"')}"
course: "${course}"
order: ${order}
classType: "${type}"
description: "${description.replace(/"/g, '\\"')}"
math: true
---

<!-- Guía rápida (borra estos comentarios al publicar):
  - Títulos: ## Sección, ### Subsección (generan el TOC automáticamente).
  - Fórmulas: $x^2$ inline, $$...$$ display. Macros globales en src/lib/katex-macros.tex.
  - Bloques: <Definicion>…</Definicion>, <Teorema>, <Ejemplo>, <Ejercicio>,
    <IdeaClave>, <Nota>, <Advertencia>. Demostraciones y soluciones con <details>.
  - Figuras: <Figure id="oferta-demanda" caption="…" alt="Descripción…" /> (alt obligatorio).
  - Términos: <Term id="elasticidad">elasticidad</Term> (alimenta el glosario).
  - Al publicar: npm run content:fix && npm run build
-->

## Introducción

Escribe aquí el contenido de la clase.

<!-- Ejemplo de fórmula display:
$$
E = mc^2
$$
-->
`;
fs.writeFileSync(file, body);
console.log(`Clase creada: src/content/classes/${course}-${slug}.md (order ${order})`);
