"""Circuito circular de la producción: insumos + trabajo entran, sale el
producto total, se reponen medios y subsistencias, y queda el excedente E
que se divide en acumulación G y consumo final F. Clases 06-08."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, label, halo


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.2))
    t = THEMES[theme]
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    def box(x, y, w, h, text, color):
        ax.add_patch(plt.Rectangle((x, y), w, h, facecolor="none",
                                   edgecolor=color, lw=1.8))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=12, fontweight="bold", color=t["fg"])

    # nodos: Producción -> Producto total -> reposición + excedente
    box(0.4, 2.4, 2.4, 1.2, "Producción", ROLES["c1"])
    box(3.9, 2.4, 2.4, 1.2, "Producto\ntotal", t["fg"])
    box(3.9, 0.3, 2.4, 1.1, "Reposición\n(insumos + subs.)", ROLES["budget"])
    box(7.3, 2.4, 2.3, 1.2, "Excedente E", accent(theme))
    box(7.3, 0.3, 1.05, 1.1, "G", ROLES["c1"])
    box(8.55, 0.3, 1.05, 1.1, "F", ROLES["c2"])

    def arrow(x1, y1, x2, y2, color):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.8))

    arrow(2.8, 3.0, 3.9, 3.0, t["muted"])          # prod -> producto
    arrow(6.3, 3.0, 7.3, 3.0, accent(theme))       # producto -> excedente
    arrow(5.1, 2.4, 5.1, 1.4, ROLES["budget"])     # producto -> reposición
    # reposición vuelve a producción (circularidad)
    ax.annotate("", xy=(1.0, 2.4), xytext=(3.9, 0.85),
                arrowprops=dict(arrowstyle="->", color=ROLES["budget"],
                                lw=1.4, linestyle=(0, (4, 3)),
                                connectionstyle="arc3,rad=0.25"))
    arrow(8.45, 2.4, 8.45, 1.4, t["muted"])        # E -> G/F
    label(ax, 1.55, 3.35, "medios + trabajo", t["muted"], theme,
          fontsize=10, bold=False)
    label(ax, 7.0, 4.15, "E = PT - CPT", accent(theme), theme, fontsize=11)
    label(ax, 2.0, 1.45, "circula de vuelta", ROLES["budget"], theme,
          fontsize=10, bold=False)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/circuito-produccion", theme=th, outdir=OUTDIR_MD)
