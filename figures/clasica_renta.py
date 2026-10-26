"""Renta diferencial: tres tierras de fertilidad distinta, mismo costo, renta = sobrante.
Marginal (C) fija el precio; A y B generan renta diferencial."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, pure_axes, accent


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    lands = ["A (fértil)", "B (media)", "C (marginal)"]
    out = np.array([100.0, 80.0, 60.0])
    cost = np.array([60.0, 60.0, 60.0])
    x = np.arange(3)
    w = 0.34
    ax.bar(x - w / 2, out, width=w, color="#0284c7", zorder=3)
    ax.bar(x + w / 2, cost, width=w, color="#d97706", zorder=3)
    for i in (0, 1):
        ax.annotate("", xy=(x[i], out[i] - 1), xytext=(x[i], cost[i] + 1),
                    arrowprops=dict(arrowstyle="<->", color=accent(theme), lw=1.8))
        label(ax, x[i] + 0.28, (out[i] + cost[i]) / 2,
              f"renta {out[i] - cost[i]:.0f}", accent(theme), theme, fontsize=10)
    label(ax, 2, 64, "renta 0", t["muted"], theme, ha="center", fontsize=10)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["A", "B", "C"], fontsize=12)
    ax.set_ylabel("producto / costo", fontsize=11.5, fontweight="bold")
    ax.set_title("Renta diferencial por fertilidad", fontsize=12, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/renta-diferencial", theme=th, outdir=OUTDIR_MD)
