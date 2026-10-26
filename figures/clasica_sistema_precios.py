"""Tasas sectoriales vs precio relativo: r1(p) y r2(p) se cruzan en p*=15, r=25%.
Sistema Sraffa 2x2 de la clase 11: curvas calculadas punto a punto, cruce analitico."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, label, end_label, pure_axes, project


def r1(p):
    m1 = 1 - 56.0 / 115.0 - (12.0 / 575.0) * p
    k1 = 56.0 / 115.0 + (12.0 / 575.0) * p
    return m1 / k1


def r2(p):
    m2 = p - 6.0 - 0.4 * p
    k2 = 6.0 + 0.4 * p
    return m2 / k2


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    ax.set_xlim(8, 26.5)
    ax.set_ylim(-0.06, 0.62)
    pp1 = np.linspace(9.5, 24.58, 250)  # dominio con m1 >= 0
    ax.plot(pp1, [r1(x) for x in pp1], color=ROLES["c1"], lw=2.4, zorder=4)
    end_label(ax, 9.3, 0.548, "r1 (trigo)", ROLES["c1"], ha="left")
    pp2 = np.linspace(10.0, 25.6, 250)  # dominio con m2 >= 0
    ax.plot(pp2, [r2(x) for x in pp2], color=ROLES["c2"], lw=2.4, zorder=4)
    end_label(ax, 25.4, r2(25.4) + 0.03, "r2 (hierro)", ROLES["c2"])
    ax.plot([15, 15], [-0.04, 0.60], color=accent(theme), lw=1.4,
            linestyle="--", zorder=3)
    ax.plot(15, 0.25, "o", ms=9, color=accent(theme), zorder=5,
            markeredgecolor=THEMES[theme]["fg"], markeredgewidth=1.2)
    label(ax, 15.4, 0.30, "p* = 15, r = 25%", accent(theme), theme, fontsize=11)
    for px, rr, nm, dx, dy in ((10.0, r1(10.0), "A", 0.0, -0.045),
                              (24.58, r2(24.58), "B", -0.42, -0.04)):
        ax.plot(px, rr, "s", ms=7, color=THEMES[theme]["muted"], zorder=5)
        label(ax, px + dx, rr + dy, nm, THEMES[theme]["muted"], theme,
              ha="center", fontsize=10)
    pure_axes(ax, [10, 15, 24.58], ["10", "15", "24,58"],
              [0, 0.25, 0.5], ["0", "25%", "50%"],
              xlabel="precio relativo $p_{21}$", ylabel="tasa de ganancia $r$")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/sistema-precios-2x2", theme=th, outdir=OUTDIR_MD)
