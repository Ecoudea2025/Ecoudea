"""Alza de r: la restricción rota sobre la dotación W (línea vieja tenue,
línea nueva sólida), E0 → E1. Clase 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    x = np.linspace(0, 8, 200)
    # vieja (r=10%) tenue y punteada, nueva (r=50%) sólida
    ax.plot(x, 8.8 - 1.1 * x, color=t["muted"], lw=2.0, linestyle=(0, (5, 4)),
            alpha=0.8)
    ax.plot(x, 10.4 - 1.5 * x, color=ROLES["budget"], lw=2.8)
    ax.text(0.6, 9.6, "r′ > r", fontsize=12, fontweight="bold",
            color=ROLES["budget"])
    # dotación (pivote) y óptimos
    ax.plot(4, 4.4, "o", ms=10, color=ROLES["endow"], zorder=5)
    ax.text(3.35, 5.0, "W", fontsize=12, fontweight="bold",
            color=ROLES["endow"])
    ax.plot(5, 3.3, "o", ms=9, color=t["muted"], zorder=5)
    ax.text(5.5, 2.85, "E₀", fontsize=12, fontweight="bold", color=t["muted"])
    ax.plot(4.6, 3.5, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(3.85, 3.0, "E₁", fontsize=12, fontweight="bold",
            color=accent(theme))
    # flecha de rotación
    ax.annotate("", xy=(2.2, 7.05), xytext=(1.35, 7.3),
                arrowprops=dict(arrowstyle="->", color=accent(theme), lw=2.0,
                                connectionstyle="arc3,rad=0.35"))
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    pure_axes(ax, [], [], [], [], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/alza-r", theme=th, outdir=OUTDIR_MD)
