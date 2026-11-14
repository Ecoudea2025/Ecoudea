"""Security Market Line del CAPM. Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    rf, rm = 3.0, 9.0
    B = np.linspace(0, 2.0, 300)
    ax.plot(B, rf + (rm - rf) * B, color=ROLES["c1"], lw=2.8)
    end_label(ax, 2.0, rf + (rm - rf) * 2.0 + 0.35, "SML", ROLES["c1"])
    ax.plot(0, rf, "o", ms=9, color=ROLES["budget"], zorder=5)
    ax.plot(1, rm, "o", ms=10, color=ROLES["budget"], zorder=5)
    ax.plot([1, 1], [0, rm], linestyle=":", color=t["muted"], lw=1.2)
    ax.plot([0, 1], [rm, rm], linestyle=":", color=t["muted"], lw=1.2)
    label(ax, 0.3, rf + 0.3, "rf", t["fg"], theme, fontsize=11)
    label(ax, 0.3, rm + 0.35, "rm", ROLES["budget"], theme, fontsize=11)
    ax.set_xlim(0, 2.45)
    ax.set_ylim(0, 16.5)
    from style import pure_axes
    pure_axes(ax, [0, 1], ["0", "1"], [0], ["0"], xlabel="beta",
              ylabel="r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/sml-capm", theme=th, outdir=OUTDIR_MD)
