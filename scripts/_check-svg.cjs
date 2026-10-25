#!/usr/bin/env node
/* Verifica si el SVG local == committed == raw GitHub == página desplegada. */
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const FILES = [
  'produccion-concava-light.svg',
  'walras-equilibrio-light.svg',
  'flujo-biosfera-light.svg',
  'unimodal-valle-light.svg',
  'condorcet-arrow-light.svg',
  'continuidad-light.svg',
  'edgeworth-contrato-light.svg'
];
const RAW_BASE = 'https://raw.githubusercontent.com/Ecoudea2025/Ecoudea/master/public/assets/figures/micro2/';
const PAGES_BASE = 'https://ecoudea2025.github.io/Ecoudea/assets/figures/micro2/';

function norm(buf) {
  return Buffer.from(buf.toString('utf8').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n'));
}
function hash(buf) { return require('crypto').createHash('sha256').update(buf).digest('hex').slice(0, 12); }

(async () => {
  for (const f of FILES) {
    const localPath = path.join('public/assets/figures/micro2', f);
    const local = norm(fs.readFileSync(localPath));
    const committed = norm(execFileSync('git', ['show', `HEAD:public/assets/figures/micro2/${f}`], { maxBuffer: 20 * 1024 * 1024 }));
    let raw, pages, rawErr = '', pagesErr = '';
    try { raw = norm(Buffer.from(await (await fetch(RAW_BASE + f)).arrayBuffer())); } catch (e) { rawErr = e.message; }
    try { pages = norm(Buffer.from(await (await fetch(PAGES_BASE + f)).arrayBuffer())); } catch (e) { pagesErr = e.message; }
    const eq = (a, b) => (a && b && a.equals(b)) ? 'IGUAL' : 'DIFIERE';
    const line = [
      `local==committed: ${eq(local, committed)}`,
      `committed==rawGit: ${eq(committed, raw)}${rawErr ? ' (' + rawErr + ')' : ''}`,
      `pages==committed: ${eq(pages, committed)}${pagesErr ? ' (' + pagesErr + ')' : ''}`,
      f
    ].join('  |  ');
    console.log(line);
  }
})();
