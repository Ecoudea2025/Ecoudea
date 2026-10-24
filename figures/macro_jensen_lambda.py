"""Jensen con ponderación lambda: curva cóncava, cuerda, C̄ descentrado y
brecha u(C̄) − ū señalada con puntos y etiquetas con fondo. Clase 05."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    # Curvatura logarítmica (más marcada que raíz: fines didácticos, la
    # brecha de Jensen se ve ~2.5× más grande)
    u = np.log
    x = np.linspace(1, 10, 300)
    ax.plot(x, u(x), color=ROLES["c1"], lw=2.8)
    ax.text(10.15, 2.25, "u(C)", fontsize=12, fontweight="bold",
            color=ROLES["c1"])
    lam = 0.4
    c1, c2 = 2.0, 8.0
    cb = lam * c1 + (1 - lam) * c2
    # cuerda
    ax.plot([c1, c2], [u(c1), u(c2)], color=t["muted"], lw=2.0,
            linestyle=(0, (5, 4)))
    # vertical en C̄: de la cuerda a la curva (la brecha de Jensen)
    chord = u(c1) + (u(c2) - u(c1)) * (cb - c1) / (c2 - c1)
    ax.plot([cb, cb], [chord, u(cb)], color=accent(theme), lw=2.2,
            linestyle=(0, (2, 2)))
    for px, py in [(c1, u(c1)), (c2, u(c2))]:
        ax.plot(px, py, "o", ms=8, color=t["muted"], zorder=5)
    # punto sobre la cuerda (utilidad promedio): etiqueta abajo-izquierda,
    # bien separada de la cuerda para que se lea
    ax.plot(cb, chord, "o", ms=8, color=t["muted"], zorder=5)
    ax.text(4.95, 1.30, "ū", fontsize=12, fontweight="bold",
            color=t["muted"], ha="right", va="top",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # punto sobre la curva (utilidad del promedio) con etiqueta arriba-derecha
    ax.plot(cb, u(cb), "o", ms=10, color=accent(theme), zorder=5)
    ax.text(6.1, 1.95, "u(C̄)", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 10.8)
    ax.set_ylim(0, 2.9)
    pure_axes(ax, [c1, cb, c2], ["C₁", "C̄", "C₂"], [], [],
              xlabel="C", ylabel="")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/jensen-lambda", theme=th, outdir=OUTDIR_MD)
