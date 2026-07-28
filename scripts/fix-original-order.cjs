const fs = require('fs');
const path = require('path');

const OLD_ROOT = path.resolve(__dirname, '../../jiperezga.github.io-master');
const NEW_CLASSES = path.resolve(__dirname, '../src/content/classes');

// Map old dirnames to course slugs
const DIR_MAP = {
  'EstadisticaI': 'estadistica-i',
  'EstadisticaII': 'estadistica-ii',
  'ProbabilidadeInferencia': 'probabilidad-inferencia',
  'MuestreoySeriesdeTiempo': 'muestreo-series',
  'Guias': 'guias',
  'SemilleroR': 'semillero-r',
  'SemilleroPython': 'semillero-python',
  'MaestriaPoliticasPublicas': 'maestria-politicas',
  'EspecializacionSocioeconomica': 'especializacion-socioeconomica',
  'EstadisticayProbabilidades': 'estadistica-y-probabilidades',
  'PresentacionesyPoster': 'presentaciones-poster',
};

function extractDate(filename) {
  const match = filename.match(/^(\d{4}-\d{2}-\d{2})-/);
  return match ? match[1] : '9999-99-99';
}

function extractTitleFromFrontmatter(content) {
  const match = content.match(/title:\s*"([^"]+)"/);
  return match ? match[1] : '';
}

// Read migrated classes and get their titles
const migratedFiles = fs.readdirSync(NEW_CLASSES).filter(f => f.endsWith('.md'));
const migratedByCourse = {};
for (const file of migratedFiles) {
  const content = fs.readFileSync(path.join(NEW_CLASSES, file), 'utf-8');
  const courseMatch = content.match(/course:\s*"([^"]+)"/);
  if (!courseMatch) continue;
  const course = courseMatch[1];
  const title = extractTitleFromFrontmatter(content);
  if (!migratedByCourse[course]) migratedByCourse[course] = [];
  migratedByCourse[course].push({ file, content, title });
}

// For each old course directory, get files sorted by date DESCENDING (Jekyll default)
for (const [dirName, courseSlug] of Object.entries(DIR_MAP)) {
  const postsDir = path.join(OLD_ROOT, dirName, '_posts');
  if (!fs.existsSync(postsDir)) continue;

  const oldFiles = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));
  oldFiles.sort((a, b) => {
    const dateA = extractDate(a);
    const dateB = extractDate(b);
    return dateB.localeCompare(dateA); // descending = newest first
  });

  const migratedEntries = migratedByCourse[courseSlug];
  if (!migratedEntries || migratedEntries.length === 0) continue;

  // For each old file (in correct order), find matching migrated entry by title
  let orderCount = 0;
  for (const oldFile of oldFiles) {
    const oldContent = fs.readFileSync(path.join(postsDir, oldFile), 'utf-8');
    const oldTitle = extractTitleFromFrontmatter(oldContent);
    if (!oldTitle) continue;

    // Find the migrated entry with matching title
    const entry = migratedEntries.find(e => e.title === oldTitle);
    if (!entry) {
      console.log(`[WARN] No matching migrated entry for "${oldTitle}" in ${courseSlug}`);
      continue;
    }

    orderCount++;
    const newContent = entry.content.replace(/order:\s*\d+/, `order: ${orderCount}`);
    fs.writeFileSync(path.join(NEW_CLASSES, entry.file), newContent, 'utf-8');
    console.log(`[OK] ${courseSlug} → order ${orderCount}: ${entry.title}`);
  }
}

console.log('\n✅ Orden original restaurado con prácticas intercaladas');
