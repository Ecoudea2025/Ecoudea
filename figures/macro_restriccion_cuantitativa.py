"""Restricción cuantitativa: recta quebrada vertical en Y₁, óptimo E*
inalcanzable sobre I₁ y solución de esquina en la dotación sobre I₂.
Clase 06."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    Y1, Y2, r = 3.0, 5.5, 0.10
    # extensión sin restricción (tenue, punteada): lo que el agente querría
    x = np.linspace(0, 8, 200)
    ax.plot(x, 8.8 - 1.1 * x, color=t["muted"], lw=1.8,
            linestyle=(0, (5, 4)), alpha=0.8)
    # recta efectiva: tramo sólido hasta Y₁ + quiebre vertical
    ax.plot([0, Y1], [8.8, Y2], color=ROLES["budget"], lw=2.8)
    ax.plot([Y1, Y1], [0, Y2], color=ROLES["budget"], lw=2.8)
    ax.text(0.5, 8.0, "−(1+r*)", fontsize=11, fontweight="bold",
            color=ROLES["budget"],
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # I₁ tangente a la extensión en E* (inalcanzable): (C1−1)(C2+0.9)=16.8
    xi = np.linspace(2.2, 7.6, 200)
    ax.plot(xi, -0.9 + 16.8 / (xi - 1), color=ROLES["c1"], lw=2.2)
    ax.text(7.7, 1.45, "I₁", fontsize=12, fontweight="bold", color=ROLES["c1"])
    ax.plot(4.91, 3.4, "o", ms=9, mfc="none", mec=t["muted"], mew=2.0,
            zorder=5)
    ax.text(5.3, 3.62, "E*", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # I₂ por la dotación (solución de esquina): dotación a la izquierda del
    # óptimo para separar ambas indiferencias en todo el rango (misma
    # familia hiperbólica: nunca se cruzan)
    xj = np.linspace(1.8, 8.2, 200)
    ax.plot(xj, -0.9 + 12.8 / (xj - 1), color=ROLES["alt"], lw=2.2)
    ax.text(8.3, 0.85, "I₂", fontsize=12, fontweight="bold", color=ROLES["alt"])
    ax.plot(Y1, Y2, "o", ms=11, color=ROLES["endow"], zorder=5)
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
        save(draw(th), "macroeconomia/restriccion-cuantitativa", theme=th, outdir=OUTDIR_MD)
