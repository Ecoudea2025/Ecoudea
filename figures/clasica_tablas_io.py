"""Matrices A y B del sistema trigo-hierro como mapas de calor anotados.
B = A + l s con los numeros del curso; la inversa de Leontief al lado."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, OUTDIR_MD, THEMES, label, TINTS

A = np.array([[0.35, 0.1463], [1.2983, 0.0]])
B = np.array([[0.4, 0.1463], [1.3666, 0.0]])
LI = np.array([[2.5, 0.3658], [3.4165, 1.0]])  # [I-B]^{-1} exacta (clase 07)


def panel(ax, theme, M, title, vmax, rows, cols):
    ax.set_xticks([0, 1])
    ax.set_xticklabels(cols, fontsize=11)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(rows, fontsize=11)
    im = ax.imshow(M, cmap="YlGn" if theme == "light" else "Greens",
                   vmin=0, vmax=vmax, aspect="equal", zorder=1)
    for i in range(2):
        for j in range(2):
            v = M[i, j]
            ax.text(j, i, f"{v:.4g}".replace(".", ","),
                    ha="center", va="center", fontsize=12, fontweight="bold",
                    color="#1d241a" if (theme == "light" or v > vmax * 0.55) else "#e8f0e8",
                    bbox=dict(facecolor="white" if theme == "light" else "black",
                                edgecolor="none", pad=1.6, alpha=0.85),
                    zorder=3)
    ax.set_title(title, fontsize=12, fontweight="bold")
    return im


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.6))
    fig.clear()
    axes = [fig.add_subplot(1, 3, k) for k in (1, 2, 3)]
    labs = (["trigo", "hierro"], ["trigo", "hierro"])
    panel(axes[0], theme, A, "A: tecnica", 1.4, *labs)
    panel(axes[1], theme, B, "B: tecnica + subsistencias", 1.4, *labs)
    panel(axes[2], theme, LI, "[I-B]^-1: directos + indirectos", 3.5, *labs)
    for a in axes:
        a.set_xlabel("insumo", fontsize=10)
    axes[0].set_ylabel("producto", fontsize=10)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/tablas-io", theme=th, outdir=OUTDIR_MD)
