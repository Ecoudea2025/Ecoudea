"""Mapa de curvas de indiferencia intertemporales (convexas) en (C1, C2).
Un punto intermedio sobre una curva más alta domina un extremo. Clase 02."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    x = np.linspace(1.6, 9.6, 200)
    for k, tag in [(18, "u¹"), (40, "u²"), (70, "u³")]:
        ax.plot(x, k / x, color=ROLES["c1"], lw=2.4)
        end_label(ax, 9.7, k / 9.7 + 0.35, tag, ROLES["c1"])
    # extremo sobre u¹ y punto intermedio sobre u²
    ax.plot(8.5, 18 / 8.5, "o", ms=9, color=ROLES["c2"], zorder=5)
    ax.text(8.5, 1.45, "A", ha="center", fontsize=12, fontweight="bold",
            color=ROLES["c2"])
    ax.plot(6.3, 40 / 6.3, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(6.3, 7.35, "E*", ha="center", fontsize=12, fontweight="bold",
            color=accent(theme))
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 10.2)
    pure_axes(ax, [], [], [], [], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/curvas-indiferencia", theme=th, outdir=OUTDIR_MD)
