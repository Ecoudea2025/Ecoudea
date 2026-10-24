"""Equilibrio intertemporal: recta con pendiente -(1+r), dotación W y
óptimo E* en tangencia, con proyecciones C1*, C2*. Clase 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, project


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    r = 0.1
    x = np.linspace(0, 8, 200)
    ax.plot(x, 9 - (1 + r) * x, color=ROLES["budget"], lw=2.8)
    ax.text(0.7, 8.15, "−(1+r)", fontsize=12, fontweight="bold",
            color=ROLES["budget"])
    # indiferencia tangente en E=(5, 3.5): (C1-1)(C2+0.9)=17.6
    xi = np.linspace(2.0, 8.2, 200)
    ax.plot(xi, -0.9 + 17.6 / (xi - 1), color=ROLES["c1"], lw=2.4)
    ax.text(8.3, 1.35, "u*", fontsize=12, fontweight="bold", color=ROLES["c1"])
    # dotación y óptimo
    ax.plot(3, 5.7, "o", ms=10, color=ROLES["endow"], zorder=5)
    ax.text(2.55, 6.25, "W", fontsize=12, fontweight="bold",
            color=ROLES["endow"])
    ax.plot(5, 3.5, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(5.45, 3.05, "E*", fontsize=12, fontweight="bold",
            color=accent(theme))
    project(ax, 5, 3.5, theme)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 10)
    pure_axes(ax, [5], ["C₁*"], [3.5], ["C₂*"], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/equilibrio", theme=th, outdir=OUTDIR_MD)
