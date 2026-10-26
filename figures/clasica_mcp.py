"""Mercancia patron: insumos vs producto de la canasta homotetica q=(1, 1.98).
Cociente uniforme 1.4498 -> R = 44.98% en ambos bienes (sistema del curso)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, pure_axes, accent

B = np.array([[0.4, 0.1463], [1.3666, 0.0]])
Q = np.array([1.0, 1.98])          # vector propio (canasta patron, escala 1)
INP = B @ Q                        # [0.6897, 1.3666]
R = float(Q[0] / INP[0] - 1)       # ~0.4498


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0, 2.6)
    xs = ["trigo", "hierro"]
    x = np.arange(2)
    w = 0.32
    ax.bar(x - w / 2, INP, width=w, color="#d97706", zorder=3)
    ax.bar(x + w / 2, Q, width=w, color=accent(theme), zorder=3)
    for i, (a, b) in enumerate(zip(INP, Q)):
        label(ax, i - w / 2, a + 0.09, f"{a:.2f}".replace(".", ","),
              "#d97706", theme, ha="center", fontsize=10)
        label(ax, i + w / 2, b + 0.09, f"{b:.2f}".replace(".", ","),
              accent(theme), theme, ha="center", fontsize=10)
    label(ax, 1.02, 2.25, f"R = {R * 100:.1f}% en ambos".replace(".", ","),
          t["fg"], theme, ha="center", fontsize=11)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(xs, fontsize=12)
    ax.set_ylabel("cantidades físicas", fontsize=11.5, fontweight="bold")
    ax.set_title("Insumos vs producto de la MCP", fontsize=12, fontweight="bold")
    return fig


def accent(theme):
    return "#3f6212" if theme == "light" else "#84cc16"


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/composicion-mcp", theme=th, outdir=OUTDIR_MD)
