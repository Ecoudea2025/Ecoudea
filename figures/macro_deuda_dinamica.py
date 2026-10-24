"""Dinámica de la deuda/PIB: converge si ρ<1, lineal si ρ=1 y explosiva
si ρ>1, desde el mismo punto inicial. Clase 16."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    bbar, b0 = 2.0, 3.0
    tt = np.linspace(0, 20, 300)
    ax.axhline(bbar, color=t["muted"], lw=1.6, linestyle=(0, (5, 4)))
    ax.text(0.3, bbar + 0.18, "b̄", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(tt, bbar + (b0 - bbar) * 0.9 ** tt, color=ROLES["budget"], lw=2.8)
    ax.text(12, 2.62, "ρ<1", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="center", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(tt, b0 + 0.08 * tt, color=t["muted"], lw=2.2)
    ax.text(20.3, 4.6, "ρ=1", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="center")
    ax.plot(tt, bbar + (b0 - bbar) * 1.1 ** tt, color=ROLES["c1"], lw=2.8)
    ax.text(20.3, 8.73, "ρ>1", fontsize=12, fontweight="bold",
            color=ROLES["c1"], ha="left", va="center")
    ax.plot(0, b0, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(0.4, 3.45, "b₀", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 23)
    ax.set_ylim(0, 10)
    pure_axes(ax, [], [], [], [], xlabel="t", ylabel="b")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/deuda-dinamica", theme=th, outdir=OUTDIR_MD)
