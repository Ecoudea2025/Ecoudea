"""Aproximación de Fisher: el factor real (1+i)/(1+π) decrece convexo con
la inflación y cruza la ganancia nula justo en π=i. Clase 12."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    inom = 0.10
    pi = np.linspace(0, 0.30, 300)
    ax.plot(pi, (1 + inom) / (1 + pi), color=ROLES["budget"], lw=2.8)
    ax.text(0.305, 0.838, "(1+i)/(1+π)", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    # umbral de ganancia nula r=0
    ax.axhline(1.0, color=t["muted"], lw=1.6, linestyle=(0, (5, 4)))
    ax.text(0.305, 1.0, "r=0", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # cruce exacto en π=i
    ax.plot([inom, inom], [0, 1.0], color=t["muted"], lw=1.2,
            linestyle=(0, (3, 3)), alpha=0.8)
    ax.plot(inom, 1.0, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(inom + 0.012, 1.035, "π=i", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 0.375)
    ax.set_ylim(0.80, 1.16)
    pure_axes(ax, [inom], ["i"], [1.0], ["1"], xlabel="π", ylabel="(1+i)/(1+π)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/fisher", theme=th, outdir=OUTDIR_MD)
