"""Oferta de trabajo N(s) y desplazamientos con r. Clase 19."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label


def curve(N, h, k, c=1.6):
    return k * N / (h - N + c)


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(8.0, 4.6))
    t = THEMES[theme]
    h = 10.0
    W1 = 3.0
    N = np.linspace(0, 9.4, 300)
    ax.plot(N, curve(N, h, 2.05), color=ROLES["alt"], lw=2.2)
    end_label(ax, 7.9, curve(7.9, h, 2.05) + 0.55, "N(s, r2)",
              ROLES["alt"])
    ax.plot(N, curve(N, h, 1.55), color=ROLES["budget"], lw=2.8)
    end_label(ax, 9.15, curve(9.15, h, 1.55) + 0.5, "N(s, r0)",
              ROLES["budget"], ha="left")
    ax.plot(N, curve(N, h, 1.15), color=ROLES["c1"], lw=2.4)
    end_label(ax, 9.4, curve(9.4, h, 1.15) - 0.55, "N(s, r1)",
              ROLES["c1"])
    # resolver N sobre cada curva a un salario dado (biseccion sobre la malla)
    def solve(k, W):
        idx = int(np.argmin(np.abs(curve(N, h, k) - W)))
        return N[idx]
    N1, N2 = solve(1.55, W1), solve(1.15, W1)
    ax.axhline(W1, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    label(ax, 0.15, W1 + 0.22, "W1", t["fg"], theme, fontsize=12)
    for Nx in (N1, N2):
        ax.plot([Nx, Nx], [0, W1], color=t["muted"], lw=1.2,
                linestyle=(0, (3, 3)))
    ax.plot(N1, W1, "o", ms=8, color=ROLES["budget"], zorder=5)
    ax.plot(N2, W1, "o", ms=8, color=ROLES["c1"], zorder=5)
    label(ax, N1, -0.35, "N1", ROLES["budget"], theme, fontsize=11)
    label(ax, N2, -0.35, "N2", ROLES["c1"], theme, fontsize=11)
    # flecha "r sube": entre r0 y r1 a y=2.5, etiqueta a la derecha de r1
    a0, a1 = solve(1.55, 2.5), solve(1.15, 2.5)
    ax.annotate("", xy=(a1 - 0.1, 2.5), xytext=(a0 + 0.1, 2.5),
                arrowprops=dict(arrowstyle="->", color=ROLES["c1"], lw=2.0))
    label(ax, a1 + 0.25, 2.5, "r sube", ROLES["c1"], theme,
          fontsize=10, ha="left")
    # flecha "r baja": entre r0 y r2 a y=1.7, etiqueta a la izquierda de r2
    b0, b2 = solve(1.55, 1.7), solve(2.05, 1.7)
    ax.annotate("", xy=(b2 + 0.1, 1.7), xytext=(b0 - 0.1, 1.7),
                arrowprops=dict(arrowstyle="->", color=ROLES["alt"], lw=2.0))
    label(ax, b2 - 0.5, 1.7, "r baja", ROLES["alt"], theme,
          fontsize=10, ha="right")
    # asintota N = h
    ax.axvline(h, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    label(ax, h + 0.25, 5.6, "N = h", t["muted"], theme, fontsize=11,
          ha="left")
    ax.set_xlim(0, 11.8)
    ax.set_ylim(-0.8, 6.6)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="N", ylabel="W")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/oferta-trabajo", theme=th, outdir=OUTDIR_MD)
