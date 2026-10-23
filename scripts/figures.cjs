// Genera (o regenera) las figuras SVG: npm run figures [-- <id>]
const { execFileSync } = require('child_process');
const manifest = require('../figures/manifest.json');

const only = process.argv[2];
const list = manifest.figures.filter((f) => !only || f.id === only);
if (!list.length) {
  console.error(`Figura "${only}" no está en figures/manifest.json`);
  process.exit(1);
}
for (const fig of list) {
  console.log(`Generando ${fig.id} (${fig.script})…`);
  execFileSync('python', [fig.script, '--theme', 'both'], { stdio: 'inherit' });
}
console.log('Listo. SVG en src/assets/figures/<id>-{light,dark}.svg');
