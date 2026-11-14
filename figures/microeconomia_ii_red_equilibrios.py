"""Externalidad de red: parabola p=n(1000-n) y equilibrios. Clase 16."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label, flow


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.6))
    t = THEMES[theme]
    c = 160000.0
    n = np.linspace(0, 1000, 500)
    p = n * (1000 - n)
    ax.plot(n, p, color=ROLES["c1"], lw=2.8)
    end_label(ax, 1000, p[-1] + 12000, "p(n)", ROLES["c1"])
    ax.axhline(c, color=t["fg"], lw=1.8)
    label(ax, 1010, c, "c", t["fg"], theme, fontsize=12)
    n1 = (1000 - np.sqrt(1000 ** 2 - 4 * c)) / 2
    n2 = (1000 + np.sqrt(1000 ** 2 - 4 * c)) / 2
    for nx, nm in [(0.0, "n0"), (n1, "n1"), (n2, "n2")]:
        ax.plot(nx, c, "o", ms=10, color=ROLES["budget"], zorder=5)
        label(ax, nx, c + 13000, nm, ROLES["budget"], theme, ha="center",
              fontsize=11)
    flow(ax, (150, c), (60, c), t["muted"])
    flow(ax, (400, c), (600, c), t["muted"])
    flow(ax, (920, c), (850, c), t["muted"])
    label(ax, 500, 60000, "masa critica n1", ROLES["c2"], theme,
          ha="center", fontsize=10)
    ax.set_xlim(0, 1120)
    ax.set_ylim(0, 300000)
    from style import pure_axes
    pure_axes(ax, [0, 500, 1000], ["0", "500", "1000"], [0], ["0"],
              xlabel="n", ylabel="p")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/red-equilibrios", theme=th, outdir=OUTDIR_MD)
