// Valida SEO técnico del build: npm run check:seo
// - sitemap sin /admin, sin archivadas, sin styleguide, con las activas
// - robots.txt existe y apunta al sitemap
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, '..', 'dist');
const manifest = require('../archive/manifest.json');

let bad = 0;
const fail = (m) => { console.error('[seo] ' + m); bad++; };

const sm = path.join(DIST, 'sitemap-0.xml');
if (!fs.existsSync(sm)) { fail('falta sitemap-0.xml'); }
const xml = fs.existsSync(sm) ? fs.readFileSync(sm, 'utf8') : '';
for (const badUrl of ['/admin', '/styleguide']) {
  if (xml.includes(badUrl)) fail(`sitemap contiene ${badUrl}`);
}
for (const c of manifest.courses) {
  if (xml.includes(`/cursos/${c.id}/`) || xml.includes(`/cursos/${c.id}<`)) fail(`sitemap contiene curso archivado ${c.id}`);
}
for (const must of ['/cursos/estadistica-ii/', '/cursos/microeconomia-i/', '/glosario/', '/tablero-latex/']) {
  if (!xml.includes(must)) fail(`sitemap no contiene ${must}`);
}
const robots = path.join(DIST, 'robots.txt');
if (!fs.existsSync(robots)) fail('falta robots.txt');
else if (!fs.readFileSync(robots, 'utf8').includes('sitemap-index.xml')) fail('robots.txt sin Sitemap');

if (bad > 0) process.exit(1);
console.log('[seo] OK: sitemap y robots.txt válidos.');
