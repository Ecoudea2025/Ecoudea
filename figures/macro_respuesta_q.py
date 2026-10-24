"""Respuesta marginal esperada vs probabilidad de transitoriedad q: recta
descendente de α₁φ (permanente) a α₁ (transitorio). Clase 08."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    phi = 9.36  # Σ_{i=1}^{20} 1/1.1^{i−1}, múltiplo de α₁
    q = np.linspace(0, 1, 200)
    ax.plot(q, 1 + (phi - 1) * (1 - q), color=ROLES["budget"], lw=2.8)
    # guía del mínimo (choque transitorio)
    ax.plot([0, 1], [1, 1], color=t["muted"], lw=1.4,
            linestyle=(0, (5, 4)), alpha=0.8)
    ax.plot(0, phi, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(0.04, phi + 0.35, "α₁φ", fontsize=12, fontweight="bold",
            color=accent(theme), ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(1, 1, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(1.0, 0.55, "α₁", fontsize=12, fontweight="bold",
            color=accent(theme), ha="right", va="top",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(0.04, 8.55, "q=0: permanente", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="left", va="top",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(0.96, 1.75, "q=1: transitorio", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="right", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 1.06)
    ax.set_ylim(0, 10.6)
    pure_axes(ax, [0, 1], ["0", "1"], [1, phi], ["α₁", "α₁φ"],
              xlabel="q", ylabel="E[dC₁*/dY]")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/respuesta-q", theme=th, outdir=OUTDIR_MD)
