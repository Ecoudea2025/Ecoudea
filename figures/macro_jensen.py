"""Desigualdad de Jensen: u cóncava, cuerda por debajo, u(C̄) sobre la
cuerda. Clase 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    x = np.linspace(0.2, 10, 300)
    ax.plot(x, np.sqrt(x), color=ROLES["c1"], lw=2.8)
    ax.text(10.15, 3.0, "u(C)", fontsize=12, fontweight="bold",
            color=ROLES["c1"])
    c1, c2, cb = 2.0, 8.0, 5.0
    u = np.sqrt
    # cuerda
    ax.plot([c1, c2], [u(c1), u(c2)], color=t["muted"], lw=2.0,
            linestyle=(0, (5, 4)))
    # vertical en C̄: del valor de la cuerda a la curva
    chord = u(c1) + (u(c2) - u(c1)) * (cb - c1) / (c2 - c1)
    ax.plot([cb, cb], [chord, u(cb)], color=accent(theme), lw=2.2,
            linestyle=(0, (2, 2)))
    for px, py in [(c1, u(c1)), (c2, u(c2))]:
        ax.plot(px, py, "o", ms=8, color=t["muted"], zorder=5)
    ax.plot(cb, u(cb), "o", ms=10, color=accent(theme), zorder=5)
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    ax.text(cb + 0.45, u(cb) + 0.30, "u(C̄)", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 10.8)
    ax.set_ylim(0, 3.9)
    # Sin duplicar u(C): va rotulado en el extremo de la curva (arriba),
    # el eje Y queda sin etiqueta para no repetir
    pure_axes(ax, [c1, cb, c2], ["C₁", "C̄", "C₂"], [], [],
              xlabel="C", ylabel="")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/jensen", theme=th, outdir=OUTDIR_MD)
