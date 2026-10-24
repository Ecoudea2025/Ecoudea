"""Restricción vía precios: quiebre en la dotación, pendiente −(1+r*) al
ahorrar y −(1+r) más empinada al endeudarse; First Best vs Second Best.
Clase 06."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    Y1, Y2 = 3.0, 5.5
    # First Best completo (tenue): lo que habría sin prima de riesgo
    x = np.linspace(0, 8, 200)
    ax.plot(x, 8.8 - 1.1 * x, color=t["muted"], lw=1.8,
            linestyle=(0, (5, 4)), alpha=0.8)
    # recta efectiva quebrada en W: suave a la izquierda, empinada a la derecha
    ax.plot([0, Y1], [8.8, Y2], color=ROLES["budget"], lw=2.8)
    ax.plot([Y1, 6.63], [Y2, 0.05], color=ROLES["budget"], lw=2.8)
    ax.text(0.5, 8.0, "−(1+r*)", fontsize=11, fontweight="bold",
            color=ROLES["budget"],
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(5.0, 2.08, "−(1+r)", fontsize=11, fontweight="bold",
            color=ROLES["budget"],
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # I₁ por el First Best E* (inalcanzable con prima)
    xi = np.linspace(2.2, 7.6, 200)
    ax.plot(xi, -0.9 + 16.8 / (xi - 1), color=ROLES["c1"], lw=2.2)
    ax.text(7.7, 1.45, "I₁", fontsize=12, fontweight="bold", color=ROLES["c1"])
    ax.plot(4.91, 3.4, "o", ms=9, mfc="none", mec=t["muted"], mew=2.0,
            zorder=5)
    ax.text(5.3, 3.62, "E*", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # I₂ por el Second Best E** (tangencia sobre el tramo empinado)
    xj = np.linspace(2.0, 6.6, 200)
    ax.plot(xj, -0.9 + 14.7 / (xj - 1), color=ROLES["alt"], lw=2.2)
    ax.text(6.7, 1.72, "I₂", fontsize=12, fontweight="bold",
            color=ROLES["alt"], ha="left", va="center")
    ax.plot(4.13, 3.8, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(3.35, 3.45, "E**", fontsize=12, fontweight="bold",
            color=accent(theme), ha="right", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(Y1, Y2, "o", ms=10, color=ROLES["endow"], zorder=5)
    ax.text(Y1 + 0.28, Y2 + 0.45, "W", fontsize=12, fontweight="bold",
            color=ROLES["endow"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 8.8)
    ax.set_ylim(0, 9.5)
    pure_axes(ax, [Y1], ["Y₁"], [Y2], ["Y₂"], xlabel="C₁", ylabel="C₂")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/restriccion-precios", theme=th, outdir=OUTDIR_MD)
