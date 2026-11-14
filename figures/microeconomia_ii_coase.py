"""Caja de Edgeworth de Coase: dinero y humo, E, E', X, X'. Clase 15."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.4, 5.0))
    t = THEMES[theme]
    W, H = 10.0, 7.0
    ax.plot([0, W, W, 0, 0], [0, 0, H, H, 0], color=t["fg"], lw=1.8)
    label(ax, 0.2, H - 0.3, "B", t["muted"], theme, fontsize=12)
    label(ax, W - 0.2, 0.5, "A", t["muted"], theme, ha="right",
          fontsize=12)
    # dotaciones: E abajo (humo 0), E' arriba (humo max), linea vertical
    ax.plot(3.0, 0, "s", ms=9, color=ROLES["c2"], zorder=5)
    label(ax, 3.0, -0.62, "E", ROLES["c2"], theme, ha="center",
          fontsize=12)
    ax.plot(3.0, H, "s", ms=9, color=ROLES["c2"], zorder=5)
    label(ax, 3.0, H + 0.62, "E'", ROLES["c2"], theme, ha="center",
          fontsize=12)
    ax.plot([3.0, 3.0], [0, H], linestyle=(0, (5, 4)), color=t["muted"],
            lw=1.4)
    # curvas de A (crecientes en dinero y humo) y de B, tangencias X y X'
    x = np.linspace(0.5, 9.5, 200)
    ax.plot(x, 1.2 + 0.28 * (x - 3.0) ** 2 / 4, color=ROLES["c1"], lw=2.2)
    ax.plot(x, H - 1.0 - 0.30 * (x - 3.0) ** 2 / 4, color=ROLES["alt"],
            lw=2.2)
    X = (6.2, 2.9)
    Xp = (6.2, H - 2.4)
    for px, py in (X, Xp):
        ax.plot(px, py, "o", ms=10, color="#3f6212" if theme == "light"
                else "#84cc16", zorder=5)
    # rectas presupuestarias por E y E' tangentes en X y X'
    ax.plot([3.0, 9.4], [0, 4.35], color=t["muted"], lw=1.6)
    ax.plot([3.0, 9.4], [H, H - 3.6], color=t["muted"], lw=1.6)
    label(ax, X[0] + 0.25, X[1] + 0.3, "X", ROLES["c1"], theme,
          fontsize=13)
    label(ax, Xp[0] + 0.7, Xp[1] + 0.5, "X'", ROLES["alt"], theme,
          fontsize=13)
    # curva de contrato vertical (cuasilineal)
    ax.plot([6.2, 6.2], [2.2, H - 1.7], linestyle=(0, (3, 3)),
            color=t["muted"], lw=1.4)
    label(ax, 6.2, H - 1.3, "contrato", t["muted"], theme, ha="center",
          fontsize=9)
    label(ax, W / 2, -1.0, "Dinero", t["fg"], theme, ha="center",
          fontsize=12)
    label(ax, -0.7, H / 2, "Humo", t["fg"], theme, ha="center",
          fontsize=12)
    ax.set_xlim(-1.2, 11.0)
    ax.set_ylim(-1.4, H + 1.0)
    ax.set_xticks([])
    ax.set_yticks([])
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/coase-edgeworth", theme=th, outdir=OUTDIR_MD)
