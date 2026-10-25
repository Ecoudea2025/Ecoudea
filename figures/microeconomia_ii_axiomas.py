"""Axiomas de racionalidad: monotonicidad, estricta y LNS. Tres paneles en (x1,x2)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS


def panel(ax, theme, mode):
    t = THEMES[theme]
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    ax.grid(True, linestyle="--", linewidth=0.7)
    x = np.array([4.0, 4.0])
    ax.plot(x[0], x[1], "o", ms=9, color="#0284c7", zorder=5)
    label(ax, 3.4, 3.3, "x", "#0284c7", theme, ha="right")
    if mode == "mono":
        # interior del cuadrante NE sombreado
        ax.fill([4, 10, 10, 4], [4, 4, 10, 10], facecolor=TINTS[theme]["excl"],
                edgecolor="none", zorder=1)
        ax.plot([4, 10], [4, 4], color=t["muted"], lw=1.2)
        ax.plot([4, 4], [4, 10], color=t["muted"], lw=1.2)
        ax.plot(7, 7.5, "o", ms=9, color="#d97706", zorder=5)
        label(ax, 7.3, 7.5, "y ≫ x", "#d97706", theme)
        ax.set_title("Monotonicidad", fontsize=12, fontweight="bold")
    elif mode == "estricta":
        ax.fill([4, 10, 10, 4], [4, 4, 10, 10], facecolor=TINTS[theme]["excl"],
                edgecolor="none", zorder=1)
        ax.plot([4, 10], [4, 4], color="#d97706", lw=2.0)  # borde este
        ax.plot([4, 4], [4, 10], color="#d97706", lw=2.0)  # borde norte
        ax.plot(4, 7.5, "o", ms=9, color="#d97706", zorder=5)
        label(ax, 4.5, 7.5, "y ≥ x, y ≠ x", "#d97706", theme, fontsize=11)
        ax.set_title("Monotonicidad estricta", fontsize=12, fontweight="bold")
    else:
        circ = plt.Circle((5, 5), 2.0, facecolor=TINTS[theme]["save"],
                          edgecolor=t["muted"], linestyle="--", lw=1.4, zorder=2)
        ax.add_patch(circ)
        ax.plot(5, 5, "o", ms=9, color="#0284c7", zorder=5)
        label(ax, 4.4, 4.4, "x", "#0284c7", theme, ha="right")
        # punto y a distancia < eps: (5.9, 5.7) -> dist ~1.14 < 2
        ax.plot(5.9, 5.7, "o", ms=9, color="#d97706", zorder=5)
        label(ax, 6.2, 6.1, "y mejor que x", "#d97706", theme, fontsize=10)
        label(ax, 6.9, 4.6, "radio ε", t["muted"], theme, fontsize=10)
        ax.set_title("No saciabilidad local", fontsize=12, fontweight="bold")
    ax.set_xticks([4])
    ax.set_xticklabels(["x1"])
    ax.set_yticks([4] if mode != "lns" else [5])
    ax.set_yticklabels(["x2"] if mode != "lns" else ["x2"])


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.4))
    fig.clear()
    fig.subplots_adjust(bottom=0.18, top=0.84, wspace=0.28)
    axes = [fig.add_subplot(1, 3, k) for k in (1, 2, 3)]
    for ax in axes:
        ax.grid(True, linestyle="--", linewidth=0.7)
    panel(axes[0], theme, "mono")
    panel(axes[1], theme, "estricta")
    panel(axes[2], theme, "lns")
    axes[0].set_ylabel("x2", fontsize=11.5, fontweight="bold")
    axes[1].set_xlabel("x1", fontsize=11.5, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/axiomas-monotonicidad", theme=th, outdir=OUTDIR_MD)
