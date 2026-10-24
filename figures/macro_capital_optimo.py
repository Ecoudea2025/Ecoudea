"""Capital óptimo: P·PMgK decreciente cruza el costo R en K*; ganancias a
la izquierda y pérdidas a la derecha sombreadas. Clase 11."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    gain = "#E2EACD" if theme == "light" else "#192718"
    loss = "#F6D5D6" if theme == "light" else "#2C1121"
    Ks, R = 16.0, 5.0
    K = np.linspace(1.5, 32, 300)
    pmg = 20 / np.sqrt(K)
    # ganancias (K < K*) y pérdidas (K > K*) en tintas sólidas
    Kg = np.linspace(4, Ks, 100)
    ax.fill_between(Kg, R, 20 / np.sqrt(Kg),
                    facecolor=gain, edgecolor="none", zorder=1)
    Kl = np.linspace(Ks, 30, 100)
    ax.fill_between(Kl, 20 / np.sqrt(Kl), R,
                    facecolor=loss, edgecolor="none", zorder=1)
    ax.plot(K, pmg, color=ROLES["c1"], lw=2.8)
    ax.text(32.4, 3.4, "P·PMgK", fontsize=12, fontweight="bold",
            color=ROLES["c1"], ha="left", va="center")
    ax.axhline(R, color=t["muted"], lw=2.0, linestyle=(0, (5, 4)))
    ax.text(32.4, R, "R", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="center")
    ax.plot(Ks, R, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(9.5, 5.72, "ganancias", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(22.5, 4.55, "pérdidas", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 35)
    ax.set_ylim(0, 11)
    pure_axes(ax, [Ks], ["K*"], [R], ["R"], xlabel="K", ylabel="")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/capital-optimo", theme=th, outdir=OUTDIR_MD)
