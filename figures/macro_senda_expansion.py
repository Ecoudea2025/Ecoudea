"""Senda de expansión: mapa de indiferencia Cobb-Douglas y rayo desde el
origen con pendiente (1+r)(1-α)/α; tangencias E1 E2 E3. Clase 04."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, end_label


def draw(theme, r=0.25, alpha=0.5):
    fig, ax = setup_eco(theme)
    m = (1 - alpha) / alpha * (1 + r)  # 1.25
    x = np.linspace(0, 8, 200)
    ax.plot(x, m * x, color=ROLES["budget"], lw=2.6)
    end_label(ax, 8.15, m * 8 + 0.15, "senda", ROLES["budget"])
    pts = [(2.0, "E₁"), (4.0, "E₂"), (6.0, "E₃")]
    for i, (c1, tag) in enumerate(pts):
        c2 = m * c1
        u = (c1 ** alpha) * (c2 ** (1 - alpha))
        xx = np.linspace(max(0.7, c1 - 3.2), c1 + 3.2, 200)
        ax.plot(xx, (u / xx ** alpha) ** (1 / (1 - alpha)),
                color=ROLES["c1"], lw=2.2)
        ax.plot(c1, c2, "o", ms=9, color=accent(theme), zorder=5)
        ax.text(c1 + 0.22, c2 + 0.3, tag, fontsize=12, fontweight="bold",
                color=accent(theme))
    ax.set_xlim(0, 9.2)
    ax.set_ylim(0, 10)
    pure_axes(ax, [], [], [], [], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/senda-expansion", theme=th, outdir=OUTDIR_MD)
