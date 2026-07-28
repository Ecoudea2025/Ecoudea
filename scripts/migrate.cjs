const fs = require('fs');
const path = require('path');

const OLD_ROOT = path.resolve(__dirname, '../../jiperezga.github.io-master');
const NEW_CLASSES = path.resolve(__dirname, '../src/content/classes');
const NEW_COURSES = path.resolve(__dirname, '../src/content/courses');

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

const TYPE_MAP = {
  'clase': 'clase',
  'practica': 'practica',
  'presentacion': 'presentacion',
  'guia': 'guia',
};

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[áäàâ]/g, 'a').replace(/[éëèê]/g, 'e')
    .replace(/[íïìî]/g, 'i').replace(/[óöòô]/g, 'o')
    .replace(/[úüùû]/g, 'u').replace(/[ñ]/g, 'n')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { frontmatter: {}, body: content };
  const raw = match[1];
  const body = match[2];
  const fm = {};
  let currentKey = null;
  let currentValue = '';
  const lines = raw.split('\n');
  for (const line of lines) {
    const keyMatch = line.match(/^(\w[\w-]*):\s*(.*)$/);
    if (keyMatch) {
      if (currentKey) fm[currentKey] = currentValue.trim();
      currentKey = keyMatch[1];
      currentValue = keyMatch[2];
    } else if (currentKey && (line.startsWith(' ') || line.startsWith('\t') || line === '')) {
      currentValue += '\n' + line;
    } else {
      if (currentKey) fm[currentKey] = currentValue.trim();
      currentKey = null;
      currentValue = '';
    }
  }
  if (currentKey) fm[currentKey] = currentValue.trim();

  for (const key of Object.keys(fm)) {
    const val = fm[key];
    if (val === '') { fm[key] = null; continue; }
    if (val === 'true') { fm[key] = true; continue; }
    if (val === 'false') { fm[key] = false; continue; }
    if (/^\d+$/.test(val)) { fm[key] = parseInt(val, 10); continue; }
    if (val.startsWith('[') && val.endsWith(']')) {
      try {
        fm[key] = JSON.parse(val.replace(/'/g, '"'));
      } catch { fm[key] = val; }
      continue;
    }
    if (val.startsWith('|')) {
      fm[key] = val.replace(/^\|\s*/, '').split('\n').map(l => l.replace(/^\s*\|\s*/, '').trim()).filter(Boolean).join(' ');
      continue;
    }
    if (val.startsWith('"') && val.endsWith('"')) {
      fm[key] = val.slice(1, -1);
      continue;
    }
    if (val.startsWith("'") && val.endsWith("'")) {
      fm[key] = val.slice(1, -1);
      continue;
    }
  }

  return { frontmatter: fm, body };
}

function detectMath(body) {
  return body.includes('$$') || body.includes('\\(') || body.includes('\\[');
}

function getClassType(mainClass) {
  const t = (mainClass || '').toLowerCase().trim();
  return TYPE_MAP[t] || 'clase';
}

function extractTags(fm) {
  const raw = fm.tags;
  if (!raw) return [];
  if (Array.isArray(raw)) return raw.filter(Boolean);
  if (typeof raw === 'string') {
    return raw.split(',').map(t => t.trim()).filter(Boolean);
  }
  return [];
}

function extractDescription(fm) {
  const intro = fm.introduction;
  if (!intro) return '';
  return String(intro)
    .replace(/<br\s*\/?>/gi, ' ')
    .replace(/<[^>]+>/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function getCourseSlug(dirname) {
  return DIR_MAP[dirname] || slugify(dirname);
}

function countExisting(dir, courseSlug) {
  const files = fs.readdirSync(dir).filter(f => f.startsWith(courseSlug));
  return files.length;
}

// Main migration
const postsDirs = Object.keys(DIR_MAP);
let totalMigrated = 0;

for (const dirName of postsDirs) {
  const courseSlug = DIR_MAP[dirName];
  const postsDir = path.join(OLD_ROOT, dirName, '_posts');

  if (!fs.existsSync(postsDir)) {
    console.log(`[SKIP] ${dirName} - no _posts directory`);
    continue;
  }

  const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md')).sort();

  let order = 0;
  for (const file of files) {
    order++;
    const filePath = path.join(postsDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const { frontmatter: fm, body } = parseFrontmatter(content);

    const title = fm.title || file.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '').replace(/[-_]/g, ' ');
    const classType = getClassType(fm['main-class']);
    const tags = extractTags(fm);
    const description = extractDescription(fm);
    const math = detectMath(body);
    const bibliography = fm.bibliography || null;

    // Clean the body - remove old layout indicators, rmarkdown-specific content if any
    let cleanBody = body.trim();

    // Generate new filename
    const typePrefix = classType === 'presentacion' ? 'presentacion' : classType === 'practica' ? 'practica' : classType === 'guia' ? 'guia' : 'clase';
    const titleSlug = slugify(title.replace(/^(Clase|Práctica|Practica|Presentación|Presentacion|Guía|Guia)\s*\d*/i, '').trim());
    const newFilename = `${courseSlug}-${typePrefix}-${String(order).padStart(2, '0')}${titleSlug ? '-' + titleSlug : ''}.md`;

    const newFrontmatter = {
      title,
      course: courseSlug,
      order,
      classType,
    };
    if (description) newFrontmatter.description = description;
    if (tags.length > 0) newFrontmatter.tags = tags;
    if (math) newFrontmatter.math = true;
    if (bibliography) newFrontmatter.bibliography = bibliography;

    // Format frontmatter as YAML
    let yaml = '---\n';
    for (const [k, v] of Object.entries(newFrontmatter)) {
      if (v === null || v === undefined) continue;
      if (Array.isArray(v)) {
        if (v.length === 0) continue;
        yaml += `${k}:\n`;
        for (const item of v) {
          yaml += `  - "${item}"\n`;
        }
      } else if (typeof v === 'boolean') {
        if (v) yaml += `${k}: true\n`;
      } else if (typeof v === 'number') {
        yaml += `${k}: ${v}\n`;
      } else {
        yaml += `${k}: "${String(v).replace(/"/g, '\\"')}"\n`;
      }
    }
    yaml += '---\n\n';

    const newContent = yaml + cleanBody;
    const newPath = path.join(NEW_CLASSES, newFilename);
    fs.writeFileSync(newPath, newContent, 'utf-8');
    totalMigrated++;
    console.log(`[OK] ${dirName}/${file} → ${newFilename}`);
  }
}

console.log(`\n✅ Migración completa: ${totalMigrated} archivos migrados a ${NEW_CLASSES}`);
