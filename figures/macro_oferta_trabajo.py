"""Oferta de trabajo N(s) y desplazamientos con r. Clase 19."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label


def curve(N, h, k, c=1.6):
    return k * N / (h - N + c)


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    h = 10.0
    W1 = 3.0
    N = np.linspace(0, 9.4, 300)
    ax.plot(N, curve(N, h, 1.55), color=ROLES["budget"], lw=2.8)
    end_label(ax, 8.55, curve(8.55, h, 1.55) + 0.35, "N(s, r0)",
              ROLES["budget"])
    ax.plot(N, curve(N, h, 1.15), color=ROLES["c1"], lw=2.4)
    end_label(ax, 8.85, curve(8.85, h, 1.15) + 0.3, "N(s, r1)",
              ROLES["c1"])
    ax.plot(N, curve(N, h, 2.05), color=ROLES["alt"], lw=2.2)
    end_label(ax, 8.3, curve(8.3, h, 2.05) + 0.4, "N(s, r2)",
              ROLES["alt"])
    # resolver N1, N2 al salario W1 (biseccion simple sobre la malla)
    def solve(k):
        idx = int(np.argmin(np.abs(curve(N, h, k) - W1)))
        return N[idx]
    N1, N2 = solve(1.55), solve(1.15)
    ax.axhline(W1, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    label(ax, 0.15, W1 + 0.22, "W1", t["fg"], theme, fontsize=12)
    for Nx in (N1, N2):
        ax.plot([Nx, Nx], [0, W1], color=t["muted"], lw=1.2,
                linestyle=(0, (3, 3)))
    ax.plot(N1, W1, "o", ms=8, color=ROLES["budget"], zorder=5)
    ax.plot(N2, W1, "o", ms=8, color=ROLES["c1"], zorder=5)
    label(ax, N1, 0.28, "N1", ROLES["budget"], theme, fontsize=11)
    label(ax, N2, 0.28, "N2", ROLES["c1"], theme, fontsize=11)
    # flechas de desplazamiento
    ax.annotate("", xy=(N2 - 0.15, 1.5), xytext=(N1 + 0.15, 1.5),
                arrowprops=dict(arrowstyle="->", color=ROLES["c1"], lw=2.0))
    label(ax, (N1 + N2) / 2, 1.85, "r sube", ROLES["c1"], theme,
          fontsize=10)
    ax.annotate("", xy=(N1 - 1.3, W1 + 1.8), xytext=(N1 - 0.3, W1 + 1.8),
                arrowprops=dict(arrowstyle="->", color=ROLES["alt"], lw=2.0))
    label(ax, N1 - 1.7, W1 + 2.1, "r baja", ROLES["alt"], theme,
          fontsize=10)
    # asintota N = h
    ax.axvline(h, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    label(ax, h + 0.25, 5.6, "N = h", t["muted"], theme, fontsize=11,
          ha="left")
    ax.set_xlim(0, 11.6)
    ax.set_ylim(0, 6.4)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="N", ylabel="W")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/oferta-trabajo", theme=th, outdir=OUTDIR_MD)
