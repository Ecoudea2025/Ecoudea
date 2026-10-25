"""EG con produccion: autarquia E, apertura E' (produce) y E'' (consume). FPP 4X^2+Y^2=100."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS, pure_axes, project


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 11.5)
    X = np.linspace(0.05, 5.0, 400)
    ax.plot(X, np.sqrt(100 - 4 * X ** 2), color="#0284c7", lw=2.6, zorder=4)
    end_label(ax, 5.02, 0.6, "FPP", "#0284c7")
    E = (3.53, 7.07)
    Ep = (1.21, 9.70)
    Epp = (10.30, 5.15)
    # autarquia: pendiente -2, tangente en E (verificada: disc=0)
    xa = np.linspace(1.2, 4.8, 60)
    ax.plot(xa, E[1] - 2 * (xa - E[0]), color="#65a30d", lw=2.0, zorder=3)
    end_label(ax, 4.85, E[1] - 2 * (4.85 - E[0]) - 0.15, "autarquía -2", "#65a30d", fontsize=10)
    # indiferencia U_E=5 (XY=25) tangente en E
    xu = np.linspace(2.2, 11.0, 200)
    ax.plot(xu, 25.0 / xu, color="#65a30d", lw=1.4, linestyle="--", zorder=3)
    # mundo: pendiente -1/2 por E', tangente a XY=53.05 en E''
    xw = np.linspace(0.3, 11.2, 80)
    ax.plot(xw, Ep[1] - 0.5 * (xw - Ep[0]), color="#d97706", lw=2.2, zorder=4)
    end_label(ax, 10.7, Ep[1] - 0.5 * (10.7 - Ep[0]) + 0.45, "mundo -1/2", "#d97706", fontsize=10, ha="right")
    xv = np.linspace(4.6, 11.2, 200)
    ax.plot(xv, 53.05 / xv, color="#d97706", lw=1.4, linestyle="--", zorder=3)
    ax.plot(E[0], E[1], "o", ms=10, color="#65a30d", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.4)
    label(ax, E[0] - 0.55, E[1] - 0.75, "E", "#65a30d", theme, ha="center", fontsize=13)
    ax.plot(Ep[0], Ep[1], "o", ms=10, color="#d97706", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.4)
    label(ax, Ep[0], Ep[1] + 0.75, "E'", "#d97706", theme, ha="center", fontsize=13)
    ax.plot(Epp[0], Epp[1], "o", ms=10, color="#d97706", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.4)
    label(ax, Epp[0], Epp[1] - 0.6, "E''", "#d97706", theme, ha="center", fontsize=13)
    label(ax, 6.3, 8.62, "U=7.28", "#d97706", theme, fontsize=10)
    label(ax, 4.6, 5.4, "U=5", "#65a30d", theme, fontsize=10)
    project(ax, E[0], E[1], theme)
    pure_axes(ax, [0, 5, 10], ["0", "5", "10"], [0, 5, 10], ["0", "5", "10"],
              xlabel="X", ylabel="Y")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/comercio-apertura", theme=th, outdir=OUTDIR_MD)
