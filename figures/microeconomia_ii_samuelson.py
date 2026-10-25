"""Bien publico: suma vertical, Nash free-rider vs Samuelson, precios de Lindahl."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, pure_axes, project


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(-0.6, 11.5)
    ax.set_ylim(0, 20)
    G = np.linspace(0, 11, 200)
    ax.plot(G, 8 - G, color="#0284c7", lw=2.2, zorder=3)
    end_label(ax, 8.6, 8 - 8.6 + 0.5, "RMS1", "#0284c7", fontsize=11)
    ax.plot(G, 10 - 0.8 * G, color="#d97706", lw=2.2, zorder=3)
    end_label(ax, 11.1, 10 - 0.8 * 11.1 + 0.3, "RMS2", "#d97706", fontsize=11)
    ax.plot(G, 18 - 1.8 * G, color="#65a30d", lw=2.8, zorder=4)
    end_label(ax, 2.5, 18 - 1.8 * 2.5 + 0.45, "suma vertical", "#65a30d", fontsize=11)
    ax.plot([0, 11.2], [9, 9], color=t["muted"], lw=1.8, zorder=3)
    end_label(ax, 11.3, 9.0, "c", t["muted"], fontsize=11)
    # Nash: RMS2=c -> 10-0.8G=9 -> G=1.25 ; Samuelson: 18-1.8G=9 -> G*=5
    GN, GS = 1.25, 5.0
    ax.plot(GN, 9, "o", ms=9, color="#d97706", zorder=5)
    label(ax, GN - 0.3, 10.1, "G Nash", "#d97706", theme, ha="center")
    ax.plot(GS, 9, "o", ms=10, color="#65a30d", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    label(ax, GS + 0.25, 10.1, "G*", "#65a30d", theme, fontsize=13)
    project(ax, GS, 9, theme)
    # Lindahl: s1*=RMS1(5)=3, s2*=RMS2(5)=6
    ax.plot([GS, GS], [0, 3], color="#0284c7", lw=2.6, zorder=4)
    label(ax, GS + 0.25, 1.5, "s1*=3", "#0284c7", theme, fontsize=10)
    ax.plot([GS, GS], [3, 9], color="#d97706", lw=2.6, zorder=4)
    label(ax, GS + 0.25, 6.0, "s2*=6", "#d97706", theme, fontsize=10)
    pure_axes(ax, [0, GN, GS, 10], ["0", "GN", "G*", "10"], [0, 9], ["0", "c"],
              xlabel="G", ylabel="valoración / costo")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/samuelson-vertical", theme=th, outdir=OUTDIR_MD)
