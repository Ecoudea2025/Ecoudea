"""Preferencias convexas vs estrictamente convexas: la cuerda y el punto medio."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, TINTS


def indif(x, k, bend):
    # curva decreciente convexa que pasa por y,z; bend controla curvatura
    return k / (x ** bend)


def panel(ax, theme, strict):
    t = THEMES[theme]
    ax.set_xlim(1, 9)
    ax.set_ylim(1, 9)
    ax.grid(True, linestyle="--", linewidth=0.7)
    y = np.array([2.0, 7.0])
    z = np.array([7.0, 2.0])
    m = 0.5 * y + 0.5 * z  # (4.5, 4.5)
    if strict:
        k = 2.0 * (7.0 ** 1.4)  # pasa aprox por y,z
        xs = np.linspace(1.6, 7.6, 200)
        ax.plot(xs, indif(xs, 2.0 * 7.0 ** 1.4, 1.4), color="#0284c7", lw=2.4, zorder=4)
    else:
        # tramo lineal entre y,z con quiebres (convexa no estricta)
        xa = np.linspace(1.0, 2.0, 30)
        ax.plot(xa, 11.0 - 2 * xa, color="#0284c7", lw=2.4, zorder=4)  # por (2,7)
        xb = np.linspace(2.0, 7.0, 50)
        ax.plot(xb, 9.0 - xb, color="#0284c7", lw=2.4, zorder=4)       # y-z lineal
        xc = np.linspace(7.0, 9.0, 30)
        ax.plot(xc, 2.0 - 0.5 * (xc - 7.0), color="#0284c7", lw=2.4, zorder=4)  # por (7,2)
    ax.plot([y[0], z[0]], [y[1], z[1]], color="#d97706", lw=1.6, linestyle="--", zorder=3)
    for p, nm in [(y, "y"), (z, "z")]:
        ax.plot(p[0], p[1], "o", ms=9, color="#d97706", zorder=5)
        label(ax, p[0] + 0.25, p[1] + 0.25, nm, "#d97706", theme)
    ax.plot(m[0], m[1], "o", ms=10, color="#65a30d", zorder=5)
    if strict:
        label(ax, m[0] + 0.3, m[1] + 0.35, "m mejor que y ~ z", "#65a30d", theme, fontsize=11)
    else:
        label(ax, m[0] + 0.3, m[1] + 0.35, "m ~ y ~ z", "#65a30d", theme)
    ax.set_xticks([2, 7])
    ax.set_xticklabels(["y1", "z1"])
    ax.set_yticks([2, 7])
    ax.set_yticklabels(["z2", "y2"])


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.8))
    fig.clear()
    fig.subplots_adjust(bottom=0.18, top=0.84, wspace=0.28)
    a1 = fig.add_subplot(1, 2, 1)
    a2 = fig.add_subplot(1, 2, 2)
    for ax in (a1, a2):
        ax.grid(True, linestyle="--", linewidth=0.7)
    panel(a1, theme, False)
    a1.set_title("Convexas (tramo lineal)", fontsize=12, fontweight="bold")
    a1.set_xlabel("x1", fontsize=11.5, fontweight="bold")
    a1.set_ylabel("x2", fontsize=11.5, fontweight="bold")
    panel(a2, theme, True)
    a2.set_title("Estrictamente convexas", fontsize=12, fontweight="bold")
    a2.set_xlabel("x1", fontsize=11.5, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/convexidad", theme=th, outdir=OUTDIR_MD)
