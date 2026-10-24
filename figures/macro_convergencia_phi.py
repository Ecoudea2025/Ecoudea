"""Convergencia de la serie geométrica: φ^i decae de 1 a 0 y el área
acumulada bajo la envolvente vale (1+r)/r. Clase 10."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    r = 0.10
    phi = 1 / (1 + r)
    area = "#DCEAEC" if theme == "light" else "#091D2F"
    i = np.linspace(0, 30, 300)
    y = phi ** i
    # área acumulada finita bajo la envolvente (tinta sólida, sin alpha)
    ax.fill_between(i, y, 0, facecolor=area, edgecolor="none", zorder=1)
    ax.plot(i, y, color=ROLES["budget"], lw=2.8)
    ax.text(30.4, 0.10, "φⁱ", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    ax.text(19, 0.42, "(1+r)/r", fontsize=12, fontweight="bold",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(0, 1, "o", ms=9, color=ROLES["budget"], zorder=5)
    ax.set_xlim(0, 33)
    ax.set_ylim(0, 1.18)
    pure_axes(ax, [0], ["0"], [1], ["1"], xlabel="i", ylabel="φⁱ")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/convergencia-phi", theme=th, outdir=OUTDIR_MD)
