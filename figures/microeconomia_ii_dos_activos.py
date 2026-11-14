"""Dominancia entre portafolios: dos rectas desde rf. Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    rf = 2.0
    sx, rx = 8.0, 6.0
    sy, ry = 6.0, 7.0
    px, py = (rx - rf) / sx, (ry - rf) / sy
    S = np.linspace(0, 12, 300)
    ax.plot(S, rf + px * S, color=ROLES["c2"], lw=2.4)
    end_label(ax, 12.0, rf + px * 12 + 0.2, "x", ROLES["c2"])
    ax.plot(S, rf + py * S, color=ROLES["c1"], lw=2.8)
    end_label(ax, 12.0, rf + py * 12 + 0.3, "y", ROLES["c1"])
    ax.plot(S, 4 + 0.03125 * S ** 2, color=ROLES["budget"], lw=2.0)
    ax.plot(S, 5.47 + 0.05 * S ** 2, color=ROLES["budget"], lw=1.4,
            linestyle=(0, (4, 3)))
    ax.plot(sx, rx, "o", ms=9, color=ROLES["budget"], zorder=5)
    ax.plot([sx, sx], [0, rx], linestyle=":", color=t["muted"], lw=1.2)
    label(ax, sx + 0.25, 0.35, "sigx", t["muted"], theme, fontsize=10)
    label(ax, 0.55, rf - 0.05, "rf", t["fg"], theme, fontsize=12)
    ax.set_xlim(0, 14.0)
    ax.set_ylim(0, 13.5)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="sigma", ylabel="r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/dos-activos", theme=th, outdir=OUTDIR_MD)
