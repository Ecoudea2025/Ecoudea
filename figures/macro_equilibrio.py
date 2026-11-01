"""Equilibrio intertemporal: recta con pendiente -(1+r), dotación W y
óptimo E* en tangencia, con proyecciones C1*, C2*. Clase 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, project, label, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    r = 0.1
    x = np.linspace(0, 8, 200)
    ax.plot(x, 9 - (1 + r) * x, color=ROLES["budget"], lw=2.8)
    # Pendiente en extremo libre de la recta con end_label
    end_label(ax, 7.8, 9 - (1 + r) * 7.8 + 0.45, "−(1+r)", ROLES["budget"])

    # indiferencia tangente en E=(5, 3.5): (C1-1)(C2+0.9)=17.6
    xi = np.linspace(2.0, 8.2, 200)
    ax.plot(xi, -0.9 + 17.6 / (xi - 1), color=ROLES["c1"], lw=2.4)
    end_label(ax, 8.3, 1.45, "u*", ROLES["c1"])

    # dotación y óptimo
    ax.plot(3, 5.7, "o", ms=10, color=ROLES["endow"], zorder=5)
    label(ax, 2.4, 5.1, "W", ROLES["endow"], theme, pad=1.4)

    ax.plot(5, 3.5, "o", ms=10, color=accent(theme), zorder=5)
    label(ax, 5.35, 4.15, "E*", accent(theme), theme, pad=1.4)

    project(ax, 5, 3.5, theme)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 10)
    pure_axes(ax, [5], ["C₁*"], [3.5], ["C₂*"], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/equilibrio", theme=th, outdir=OUTDIR_MD)
