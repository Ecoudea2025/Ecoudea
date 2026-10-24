"""Línea de tiempo intertemporal: nodos t..t+3 con flujos Y (entra), C (sale)
y transferencia del ahorro capitalizado (1+r)A. Clase 01."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 3.9))
    t = THEMES[theme]
    xs = [0, 1, 2, 3]
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-2.35, 1.9)
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    # eje temporal
    ax.annotate("", xy=(3.45, 0), xytext=(-0.45, 0),
                arrowprops=dict(arrowstyle="->", color=t["muted"], lw=1.4))
    for i, x in enumerate(xs):
        ax.plot(x, 0, "o", ms=11, color=accent(theme), zorder=5)
        ax.text(x, -0.32, f"t{'' if i == 0 else '+' + str(i)}", ha="center",
                va="top", fontsize=12, fontweight="bold", color=t["fg"])
        # ingreso laboral: entra desde arriba
        ax.annotate("", xy=(x, 0.12), xytext=(x, 1.05),
                    arrowprops=dict(arrowstyle="->", color=ROLES["budget"], lw=2.2))
        ax.text(x, 1.18, "Y", ha="center", va="bottom", fontsize=12,
                fontweight="bold", color=ROLES["budget"])
        # consumo: sale hacia abajo (solo nodos 0..2 para no saturar)
        if i < 3:
            ax.annotate("", xy=(x, -1.08), xytext=(x, -0.55),
                        arrowprops=dict(arrowstyle="->", color=ROLES["c2"], lw=2.2))
            ax.text(x, -1.20, "C", ha="center", va="top", fontsize=12,
                    fontweight="bold", color=ROLES["c2"])
    # transferencia del ahorro capitalizado (carril propio, lejos de las C)
    ax.annotate("", xy=(2.78, -1.72), xytext=(0.22, -1.72),
                arrowprops=dict(arrowstyle="->", color=t["muted"], lw=1.3,
                                linestyle=(0, (4, 3))))
    ax.text(1.5, -1.84, "(1+r)A", ha="center", va="top", fontsize=11,
            color=t["muted"])
    # ahorro del último nodo: flecha RECTA vertical (sin curva rara),
    # mismo lenguaje que las C pero en muted para distinguir
    ax.annotate("", xy=(3, -1.08), xytext=(3, -0.55),
                arrowprops=dict(arrowstyle="->", color=t["muted"], lw=2.2))
    ax.text(3.22, -0.82, "S", ha="left", va="center", fontsize=12,
            fontweight="bold", color=t["muted"])
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/linea-tiempo", theme=th, outdir=OUTDIR_MD)
