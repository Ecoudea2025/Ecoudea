"""Impuestos vs normas con demanda DD de pendiente negativa. Clase 15."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from matplotlib.patches import Polygon
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, TINTS


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.8))
    t = THEMES[theme]
    q = np.linspace(0, 9, 400)
    ax.plot(q, 1.0 * q, color=ROLES["alt"], lw=2.0)
    ax.text(7.6, 7.8, "CMgc", fontsize=11, fontweight="bold",
            color=ROLES["alt"], ha="left", va="center")
    ax.plot(q, 2.0 * q, color=ROLES["c1"], lw=2.4)
    ax.text(6.3, 13.0, "CMgT", fontsize=11, fontweight="bold",
            color=ROLES["c1"], ha="left", va="center")
    ax.plot(q, 3.0 * q, color=ROLES["budget"], lw=2.8)
    ax.text(4.9, 15.1, "CMgS", fontsize=11, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    dd = 18 - 1.5 * q
    ax.plot(q, dd, color="#e11d48", lw=2.4)
    ax.text(8.6, 5.1, "DD", fontsize=12, fontweight="bold",
            color="#e11d48", ha="left", va="center")
    qS, h, f = 4.0, 12.0, 8.0
    qE, PE = 5.14, 10.29
    ax.plot([0, qS], [h, h], color=t["muted"], lw=1.4,
            linestyle=(0, (5, 4)))
    ax.plot([0, qE], [PE, PE], color=t["muted"], lw=1.4,
            linestyle=(0, (5, 4)))
    ax.plot([qS, qS], [0, h], color=t["muted"], lw=1.2, linestyle=(0, (3, 3)))
    ax.plot([qE, qE], [0, PE], color=t["muted"], lw=1.2,
            linestyle=(0, (3, 3)))
    # rectangulo fiscal hgdf
    ax.fill_between([0, qS], [h, h], [f, f],
                    facecolor=TINTS[theme]["debt"], edgecolor="none",
                    zorder=1)
    # triangulo gEc: g(qS,h), E(qE,PE), c(qS,PE)
    ax.add_patch(Polygon([[qS, h], [qE, PE], [qS, PE]],
                         facecolor=TINTS[theme]["loss"], edgecolor="none",
                         zorder=1))
    # triangulo ECd: E, C=(qS,h), d=(qS,f)
    ax.add_patch(Polygon([[qS, h], [qE, PE], [qS, f]],
                         facecolor=TINTS[theme]["loss"], edgecolor="none",
                         zorder=1, alpha=0.6))
    # ganancia ambiental bajo CMgc
    xg = np.linspace(qS, qE, 50)
    ax.fill_between(xg, 0 * xg, 1.0 * xg, facecolor=TINTS[theme]["save"],
                    edgecolor="none", zorder=1)
    ax.plot(qS, h, "o", ms=9, color=t["fg"], zorder=5)
    ax.plot(qE, PE, "o", ms=9, color=t["fg"], zorder=5)
    label(ax, qS, 0.7, "qS", t["fg"], theme, ha="center", fontsize=11)
    label(ax, qE, 0.7, "qE", t["fg"], theme, ha="center", fontsize=11)
    label(ax, 0.25, h, "h", t["fg"], theme, fontsize=11)
    label(ax, 0.25, PE, "PE", t["fg"], theme, fontsize=11)
    label(ax, 0.25, f, "f", t["fg"], theme, fontsize=11)
    label(ax, qS + 0.2, h + 0.4, "g", t["fg"], theme, fontsize=12)
    label(ax, qE + 0.2, PE + 0.4, "E", t["fg"], theme, fontsize=12)
    ax.set_xlim(0, 9.6)
    ax.set_ylim(0, 16.5)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="q", ylabel="P")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/impuestos-normas-dd", theme=th,
             outdir=OUTDIR_MD)
