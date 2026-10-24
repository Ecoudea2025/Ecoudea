"""Demanda de inversión I(r) con pendiente negativa y desplazamientos:
derecha si suben A, N o P/PK; izquierda si suben δ o K. Clase 13."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    I = np.linspace(0, 8, 200)
    ax.plot(I, 8.5 - 1.1 * I, color=t["muted"], lw=1.8,
            linestyle=(0, (5, 4)), alpha=0.8)
    ax.plot(I, 11 - 1.1 * I, color=ROLES["budget"], lw=2.8)
    ax.plot(I, 13.5 - 1.1 * I, color=t["muted"], lw=1.8,
            linestyle=(0, (5, 4)), alpha=0.8)
    ax.text(8.15, 2.0, "I(r)", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    # desplazamiento derecha (mejor tecnología): flecha a altura r=7
    ax.annotate("", xy=(5.9, 7), xytext=(3.64, 7),
                arrowprops=dict(arrowstyle="->", color=accent(theme), lw=2.0))
    ax.text(6.2, 7.45, "A↑", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # desplazamiento izquierda (más depreciación): flecha a altura r=4
    ax.annotate("", xy=(4.09, 4), xytext=(6.36, 4),
                arrowprops=dict(arrowstyle="->", color=ROLES["endow"], lw=2.0))
    ax.text(3.5, 4.45, "δ↑", fontsize=12, fontweight="bold",
            color=ROLES["endow"], ha="right", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 9.2)
    ax.set_ylim(0, 14.5)
    pure_axes(ax, [], [], [], [], xlabel="I", ylabel="r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/demanda-inversion", theme=th, outdir=OUTDIR_MD)
