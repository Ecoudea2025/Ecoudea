"""Gravitación: el precio de mercado p21 oscila entre 10 y 24.58 y converge
al precio natural 15, donde r1 = r2 = 25%. Clases 11 y 23."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, label, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    ax.set_xlim(0, 10)
    ax.set_ylim(8, 27)
    # precio natural: línea central
    ax.plot([0, 10], [15, 15], color=accent(theme), lw=2.2, zorder=3)
    # dos órbitas que convergen (amortiguadas, amplia diferencia inicial)
    tt = np.linspace(0, 10, 400)
    ax.plot(tt, 15 + 9.58 * np.exp(-0.45 * tt) * np.cos(1.1 * tt),
            color=ROLES["c2"], lw=2.0, zorder=4)
    ax.plot(tt, 15 - 5.0 * np.exp(-0.45 * tt) * np.cos(1.1 * tt + 0.6),
            color=ROLES["c1"], lw=2.0, zorder=4)
    pure_axes(ax, [0, 10], ["t0", "t"], [10, 15, 24.58],
              ["p=10", "p*=15", "p=24.58"])
    label(ax, 8.2, 16.4, "precio natural (r = 25%)", accent(theme), theme,
          ha="center", fontsize=11)
    label(ax, 0.3, 25.3, "r2 > r1: migran al hierro", ROLES["c2"], theme,
          fontsize=10, bold=False)
    label(ax, 0.3, 9.6, "r1 > r2: migran al trigo", ROLES["c1"], theme,
          fontsize=10, bold=False)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/gravitacion", theme=th, outdir=OUTDIR_MD)
