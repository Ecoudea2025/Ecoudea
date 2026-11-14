"""Utilidad esperada vs certeza: u(W)=sqrt(W), cuerda y brecha. Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label, project


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    W = np.linspace(3, 17, 300)
    u = np.sqrt(W)
    ax.plot(W, u, color=ROLES["c1"], lw=2.8)
    end_label(ax, 17.0, np.sqrt(17) + 0.08, "u(W)", ROLES["c1"])
    u5, u15 = np.sqrt(5), np.sqrt(15)
    umid = 0.5 * u5 + 0.5 * u15
    ax.plot([5, 15], [u5, u15], color=ROLES["c2"], lw=2.2)
    end_label(ax, 15.1, umid + 0.12, "cuerda", ROLES["c2"])
    for x, y in [(5, u5), (15, u15)]:
        ax.plot(x, y, "o", ms=8, color=ROLES["c2"], zorder=5)
    ax.plot(10, np.sqrt(10), "o", ms=9, color=ROLES["budget"], zorder=5)
    ax.plot(10, umid, "o", ms=9, color=ROLES["c2"], zorder=5,
            markerfacecolor="none", markeredgewidth=2)
    project(ax, 10, np.sqrt(10), theme)
    ax.plot([5, 5], [0, u5], linestyle=":", color=t["muted"], lw=1.2)
    ax.plot([15, 15], [0, u15], linestyle=":", color=t["muted"], lw=1.2)
    ax.plot([10, 10], [umid, np.sqrt(10)], color=ROLES["budget"], lw=2.4,
            zorder=5)
    label(ax, 10.35, (umid + np.sqrt(10)) / 2, "brecha", ROLES["budget"],
          theme, fontsize=10)
    ax.set_xlim(2.5, 18.2)
    ax.set_ylim(1.4, 4.6)
    from style import pure_axes
    pure_axes(ax, [5, 10, 15], ["5", "10", "15"], [], [], xlabel="W",
              ylabel="u")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/utilidad-esperada", theme=th, outdir=OUTDIR_MD)
