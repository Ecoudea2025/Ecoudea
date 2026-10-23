// Archiva cursos heredados fuera de src/content (Fase 2.a).
// Uso: node scripts/archive-courses.cjs
// Mueve con `git mv` (conserva historial) y genera archive/manifest.json
// para los avisos de "curso archivado" en URLs viejas.
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const KEEP = ['estadistica-ii'];

const coursesDir = path.join(ROOT, 'src', 'content', 'courses');
const classesDir = path.join(ROOT, 'src', 'content', 'classes');
const archiveDir = path.join(ROOT, 'archive');
const archiveCourses = path.join(archiveDir, 'courses');
const archiveClasses = path.join(archiveDir, 'classes');
fs.mkdirSync(archiveCourses, { recursive: true });
fs.mkdirSync(archiveClasses, { recursive: true });

function frontmatter(file) {
  const t = fs.readFileSync(file, 'utf8');
  const m = t.match(/^---\n([\s\S]*?)\n---/);
  const get = (k) => (m && m[1].match(new RegExp(`^${k}:\\s*\"?([^\"\\n]+)\"?`, 'm')) || [])[1] || '';
  return { title: get('title'), category: get('category'), order: get('order') };
}

const manifest = { archivedAt: new Date().toISOString().slice(0, 10), keep: KEEP, courses: [], classes: [] };

for (const f of fs.readdirSync(coursesDir).filter((f) => f.endsWith('.md'))) {
  const id = f.replace(/\.md$/, '');
  if (KEEP.includes(id)) continue;
  const fm = frontmatter(path.join(coursesDir, f));
  manifest.courses.push({ id, title: fm.title, category: fm.category });
  execFileSync('git', ['mv', path.join('src/content/courses', f), path.join('archive/courses', f)], { cwd: ROOT });
}

for (const f of fs.readdirSync(classesDir).filter((f) => f.endsWith('.md'))) {
  const t = fs.readFileSync(path.join(classesDir, f), 'utf8');
  const m = t.match(/^course:\s*"?([^"\n]+)"?/m);
  const course = m ? m[1].trim() : '';
  if (KEEP.includes(course)) continue;
  manifest.classes.push({ id: f.replace(/\.md$/, ''), course });
  execFileSync('git', ['mv', path.join('src/content/classes', f), path.join('archive/classes', f)], { cwd: ROOT });
}

manifest.courses.sort((a, b) => a.id.localeCompare(b.id));
manifest.classes.sort((a, b) => a.id.localeCompare(b.id));
fs.writeFileSync(path.join(archiveDir, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
console.log(`Cursos archivados: ${manifest.courses.length}`);
console.log(`Clases archivadas: ${manifest.classes.length}`);
console.log(`Cursos activos: ${KEEP.join(', ')}`);
