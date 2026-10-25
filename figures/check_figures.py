#!/usr/bin/env python
"""Gate de figuras: npm run figures:check (exit 1 si hay ERROR de solapamiento).

Lee figures/manifest.json, ejecuta draw(theme) de cada script en ambos temas
y valida con figures/overlap.py. Ademas pasa el lint de captions en Markdown.
Uso: python figures/check_figures.py [id1 id2 ...]
"""
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
except Exception:
    pass
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'figures'))

import matplotlib
matplotlib.use('SVG')

from overlap import check_figure  # noqa: E402


def load_draw(script):
    path = os.path.join(ROOT, script)
    name = 'figmod_' + re.sub(r'\W', '_', script)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.draw


def main(only):
    manifest = json.load(open(os.path.join(ROOT, 'figures', 'manifest.json'),
                              encoding='utf-8'))
    figs = manifest['figures'] if isinstance(manifest, dict) else manifest
    if only:
        figs = [f for f in figs if f['id'] in only]
    bad = 0
    total_warn = 0
    for f in figs:
        fid = f['id']
        try:
            draw = load_draw(f['script'])
        except Exception as e:  # noqa: BLE001
            print(f'[figures] {fid}: ERROR importando script: {e}')
            bad += 1
            continue
        for theme in ('light', 'dark'):
            try:
                fig = draw(theme)
                errors, warnings = check_figure(fig)
            except Exception as e:  # noqa: BLE001
                print(f'[figures] {fid} [{theme}]: ERROR dibujando: {e}')
                bad += 1
                continue
            finally:
                try:
                    import matplotlib.pyplot as plt
                    plt.close('all')
                except Exception:
                    pass
            for v in errors:
                print(f"[figures] {fid} [{theme}]: ERROR {v['kind']}: "
                      f"'{v['text']}' — {v['detail']}")
                bad += 1
            for v in warnings:
                print(f"[figures] {fid} [{theme}]: aviso {v['kind']}: "
                      f"'{v['text']}' — {v['detail']}")
                total_warn += 1
    # lint de captions en Markdown
    cap_bad = 0
    for fp in glob.glob(os.path.join(ROOT, 'src', 'content', 'classes', '*.md')):
        raw = open(fp, encoding='utf-8').read()
        short = os.path.basename(fp)
        if 'Figura: Figura:' in raw:
            print(f'[figures] {short}: ERROR caption duplicado "Figura: Figura:"')
            cap_bad += 1
        for m in re.finditer(r'<img\s[^>]*class="fig-light"[^>]*>', raw):
            tag = m.group(0)
            am = re.search(r'alt="([^"]*)"', tag)
            if not am or not am.group(1).strip():
                print(f'[figures] {short}: ERROR <img fig-light> sin alt descriptivo')
                cap_bad += 1
    bad += cap_bad
    print(f'[figures] {len(figs)} figuras revisadas: '
          f'{bad} errores, {total_warn} avisos.')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
