"""Mapa de curvas de indiferencia intertemporales (convexas) en (C1, C2).
Muestra que una combinación intermedia (suavización) domina a consumos extremos. Clase 02."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes, end_label, label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    x = np.linspace(1.5, 9.6, 250)

    # Tres niveles de utilidad Cobb-Douglas simétrica U = C1 * C2
    # u1 = 18 (extremos), u2 = 27 (promedio equilibrado), u3 = 55
    curves = [(18.0, "u¹", ROLES["c1"]), (27.0, "u²", accent(theme)), (55.0, "u³", ROLES["c1"])]
    for k, tag, col in curves:
        ax.plot(x, k / x, color=col, lw=2.4 if k != 27.0 else 2.6)
        end_label(ax, 9.7, k / 9.7 + 0.35, tag, col)

    # Dos consumos extremos sobre u1: A = (2.2, 8.18) y B = (8.0, 2.25)
    ax.plot(2.2, 18.0 / 2.2, "o", ms=8, color=ROLES["c2"], zorder=5)
    label(ax, 1.35, 8.7, "A", ROLES["c2"], theme, pad=1.4)

    ax.plot(8.0, 2.25, "o", ms=8, color=ROLES["c2"], zorder=5)
    label(ax, 7.8, 1.35, "B", ROLES["c2"], theme, pad=1.4)

    # Cuerda (segmento) entre A y B mostrando las combinaciones convexas
    ax.plot([2.2, 8.0], [18.0 / 2.2, 2.25], color=t["muted"], ls="--", lw=1.5, alpha=0.8, zorder=2)

    # Punto intermedio equilibrado M = (5.1, 5.215) sobre u2 > u1
    ax.plot(5.1, 5.215, "o", ms=10, color=accent(theme), zorder=6)
    label(ax, 5.45, 5.95, "M (0.5A + 0.5B)", accent(theme), theme, fontsize=11, pad=1.4)

    ax.set_xlim(0, 10.4)
    ax.set_ylim(0, 10.4)
    pure_axes(ax, [2.2, 5.1, 8.0], ["2.2", "5.1", "8.0"],
              [2.25, 5.2, 8.2], ["2.2", "5.2", "8.2"],
              xlabel="Consumo presente (C₁)", ylabel="Consumo futuro (C₂)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/curvas-indiferencia", theme=th, outdir=OUTDIR_MD)
