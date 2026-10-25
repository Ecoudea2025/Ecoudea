"""Continuidad: curva de indiferencia separa U(x) cerrado de L(x); sucesion converge dentro."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    # I(x): y = 36/x (pasa por x=(6,6)); U(x) = arriba (sombreado)
    xs = np.linspace(3.2, 10, 200)
    ax.plot(xs, 36.0 / xs, color="#0284c7", lw=2.4, zorder=4)
    end_label(ax, 10.05, 36.0 / 10, "I(x)", "#0284c7")
    ax.fill_between(xs, 36.0 / xs, 10.5, facecolor=TINTS[theme]["excl"],
                    edgecolor="none", zorder=1)
    label(ax, 8.2, 8.6, "U(x)", "#0284c7", theme)
    label(ax, 3.0, 2.2, "L(x)", t["muted"], theme)
    ax.plot(6, 6, "o", ms=10, color="#0284c7", zorder=5)
    label(ax, 5.6, 5.5, "x", "#0284c7", theme, ha="right")
    # sucesion y^n en U(x) -> y en U(x): puntos (8.5,4.6),(7.8,5.2),(7.2,5.7), limite (6.8,6.0)
    seq = [(8.5, 4.6), (7.8, 5.2), (7.2, 5.7), (6.8, 6.0)]
    for k, (px, py) in enumerate(seq[:-1]):
        ax.plot(px, py, "o", ms=8, color="#d97706", zorder=5)
        label(ax, px + 0.25, py + 0.2, f"y{k + 1}", "#d97706", theme, fontsize=10)
    ax.plot(seq[-1][0], seq[-1][1], "s", ms=9, color="#65a30d", zorder=5)
    label(ax, seq[-1][0] + 0.3, seq[-1][1] + 0.25, "y en U(x)", "#65a30d", theme)
    # flecha punteada de convergencia y^1 -> ... -> y
    ax.annotate("", xy=(6.95, 5.95), xytext=(8.3, 4.75),
                arrowprops=dict(arrowstyle="->", color="#d97706", lw=1.4,
                                linestyle=(0, (3, 2))))
    ax.set_xticks([6])
    ax.set_xticklabels(["x1"])
    ax.set_yticks([6])
    ax.set_yticklabels(["x2"])
    ax.set_xlabel("x1", fontsize=11.5, fontweight="bold")
    ax.set_ylabel("x2", fontsize=11.5, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/continuidad", theme=th, outdir=OUTDIR_MD)
