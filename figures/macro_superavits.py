"""Superávits estabilizadores: déficit hoy (barra negativa) y senda de
superávits futuros cuya área descontada cubre la deuda. Clase 15."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    deficit = "#F6D5D6" if theme == "light" else "#2C1121"
    superav = "#E2EACD" if theme == "light" else "#192718"
    tt = np.arange(7)
    s = np.array([-3.0, 1.5, 1.2, 0.9, 0.6, 0.35, 0.1])
    colors = [deficit] + [superav] * 6
    edges = [ROLES["endow"]] + [ROLES["budget"]] * 6
    ax.bar(tt, s, color=colors, edgecolor=edges, linewidth=1.4, zorder=3)
    ax.axhline(0, color=t["muted"], lw=1.2)
    ax.text(0, -1.5, "déficit", fontsize=10, fontstyle="italic",
            color=t["fg"], ha="center", va="center")
    ax.text(2.5, 2.0, "superávits", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(-0.7, 6.7)
    ax.set_ylim(-4.0, 2.6)
    pure_axes(ax, [0, 3, 6], ["hoy", "t+3", "t+6"], [], [],
              xlabel="t", ylabel="T−G")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/superavits", theme=th, outdir=OUTDIR_MD)
