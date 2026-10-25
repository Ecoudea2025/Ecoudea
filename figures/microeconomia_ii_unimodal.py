"""Votante mediano: valle no unimodal vs tres curvas de un solo pico."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label


def panel(ax, theme, left):
    ax.set_xlim(-0.4, 2.4)
    ax.set_ylim(0, 12.5)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Bajo", "Medio", "Alto"])
    ax.set_yticks([0, 5, 10])
    ax.set_yticklabels(["0", "5", "10"])
    xs = np.array([0.0, 1.0, 2.0])
    if left:
        ax.plot(xs, [6, 3, 11], color="#94a3a8", lw=2.4, zorder=4, marker="o", ms=7)
        label(ax, 1.7, 8.0, "k (valle)", "#94a3a8", theme, ha="center", fontsize=11)
        ax.set_title("No unimodal", fontsize=12, fontweight="bold")
    else:
        ax.plot(xs, [9, 5, 3], color="#0284c7", lw=2.2, zorder=4, marker="o", ms=7)
        label(ax, -0.15, 9.0, "i", "#0284c7", theme, ha="right", fontsize=12)
        ax.plot(xs, [2, 10, 5], color="#d97706", lw=2.2, zorder=4, marker="o", ms=7)
        label(ax, 1.0, 10.75, "j", "#d97706", theme, ha="center", fontsize=12)
        ax.plot(xs, [2, 5, 11], color="#65a30d", lw=2.2, zorder=4, marker="o", ms=7)
        label(ax, 2.05, 11.55, "k", "#65a30d", theme, fontsize=12)
        ax.set_title("Unimodales", fontsize=12, fontweight="bold")
    ax.set_ylabel("")
    ax.set_xlabel("")


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.8))
    fig.clear()
    fig.subplots_adjust(bottom=0.18, top=0.84, wspace=0.28)
    a1 = fig.add_subplot(1, 2, 1)
    a2 = fig.add_subplot(1, 2, 2)
    for ax in (a1, a2):
        ax.grid(True, linestyle="--", linewidth=0.7)
    panel(a1, theme, True)
    a1.set_ylabel("utilidad", fontsize=11.5, fontweight="bold")
    panel(a2, theme, False)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/unimodal-valle", theme=th, outdir=OUTDIR_MD)
