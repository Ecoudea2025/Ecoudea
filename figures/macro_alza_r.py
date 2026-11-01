"""Alza de r: la restricción rota sobre la dotación W (línea vieja tenue,
línea nueva sólida), E0 → E1. Clase 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, label, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    x = np.linspace(0, 8, 200)

    # vieja (r=10%) tenue y punteada, nueva (r=50%) sólida
    ax.plot(x, 8.8 - 1.1 * x, color=t["muted"], lw=2.0, linestyle=(0, (5, 4)),
            alpha=0.8)
    ax.plot(x, 10.4 - 1.5 * x, color=ROLES["budget"], lw=2.8)

    # Etiqueta de la nueva restricción al extremo inferior con end_label
    end_label(ax, 6.6, 10.4 - 1.5 * 6.6 + 0.35, "r′ > r", ROLES["budget"])

    # dotación (pivote) y óptimos
    ax.plot(4, 4.4, "o", ms=10, color=ROLES["endow"], zorder=5)
    label(ax, 4.35, 4.85, "W", ROLES["endow"], theme, pad=1.4)

    # Óptimo inicial E0
    ax.plot(5, 3.3, "o", ms=9, color=t["muted"], zorder=5)
    label(ax, 5.4, 3.65, "E₀", t["muted"], theme, pad=1.4)

    # Nuevo óptimo E1
    ax.plot(4.6, 3.5, "o", ms=10, color=accent(theme), zorder=5)
    label(ax, 3.9, 3.1, "E₁", accent(theme), theme, pad=1.4)

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
