"""Trigo-trigo: la tasa como pendiente del rayo cosecha vs adelanto (K=800,Y=1000)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    ax.set_xlim(0, 1050)
    ax.set_ylim(0, 1150)
    xs = np.linspace(0, 1050, 100)
    ax.plot(xs, xs, color=t["muted"], lw=1.2, linestyle="--", zorder=2)
    end_label(ax, 1055, 1055, "r = 0", t["muted"], fontsize=10)
    # tecnica base: cosecha 1000 con adelanto 800 -> r = 25%
    ax.plot([0, 800], [0, 1000], color="#0284c7", lw=2.6, zorder=4)
    ax.plot(800, 1000, "o", ms=9, color="#0284c7", zorder=5)
    label(ax, 815, 960, "K=800, Y=1000", "#0284c7", theme)
    # tecnica mejorada: mismo Y con adelanto 700 -> r = 42,9%
    ax.plot([0, 700], [0, 1000], color="#d97706", lw=2.2, zorder=4)
    ax.plot(700, 1000, "o", ms=9, color="#d97706", zorder=5)
    label(ax, 530, 975, "K=700, Y=1000", "#d97706", theme, ha="center")
    label(ax, 880, 760, "pendiente = 1 + r", t["fg"], theme, ha="center",
          fontsize=11)
    label(ax, 880, 690, "r = 25% vs r = 42,9%", t["muted"], theme, ha="center",
          fontsize=10, bold=False)
    ax.set_xticks([700, 800])
    ax.set_xticklabels(["700", "800"])
    ax.set_yticks([1000])
    ax.set_yticklabels(["1000"])
    ax.set_xlabel("adelanto K (trigo)", fontsize=11.5, fontweight="bold")
    ax.set_ylabel("cosecha Y (trigo)", fontsize=11.5, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/trigo-trigo-numerico", theme=th, outdir=OUTDIR_MD)
