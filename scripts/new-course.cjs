// Scaffold de curso nuevo: npm run new:course -- <slug> [--title ..] [--description ..] [--category ..] [--order N]
// Crea src/content/courses/<slug>.md con frontmatter completo. No toca nada más.
const fs = require('fs');
const path = require('path');

function arg(name, def = '') {
  const i = process.argv.indexOf('--' + name);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

const slug = process.argv[2];
if (!slug || slug.startsWith('--') || !/^[a-z0-9-]+$/.test(slug)) {
  console.error('Uso: npm run new:course -- <slug> [--title "…"] [--description "…"] [--category "Cursos"] [--order N]');
  process.exit(1);
}
const dir = path.join(__dirname, '..', 'src', 'content', 'courses');
const file = path.join(dir, slug + '.md');
if (fs.existsSync(file)) {
  console.error(`Ya existe ${file}`);
  process.exit(1);
}
const existing = fs.readdirSync(dir).filter((f) => f.endsWith('.md'));
const maxOrder = existing.reduce((m, f) => {
  const t = fs.readFileSync(path.join(dir, f), 'utf8').match(/^order:\s*(\d+)/m);
  return Math.max(m, t ? parseInt(t[1], 10) : 0);
}, 0);

const title = arg('title', slug.split('-').map((w) => w[0].toUpperCase() + w.slice(1)).join(' '));
const description = arg('description', 'Descripción del curso (editar).');
const category = arg('category', 'Cursos');
const order = parseInt(arg('order', String(maxOrder + 1)), 10);

const front = `---
title: "${title.replace(/"/g, '\\"')}"
description: "${description.replace(/"/g, '\\"')}"
category: "${category}"
order: ${order}
---

<!-- Portada opcional: image: "/assets/images/<archivo>.jpg" -->
<!-- Área (Fase 2): area: "estadistica" (micro|macro|econometria|estadistica|matematicas|historia) -->
`;
fs.writeFileSync(file, front);
console.log(`Curso creado: src/content/courses/${slug}.md (order ${order})`);
console.log(`Siguiente: npm run new:lesson -- ${slug} <slug-clase> --title "Clase 01"`);
