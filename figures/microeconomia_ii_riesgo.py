"""Riesgo: log concava con EC y prima; Spence: umbral que separa costos."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS


def left(ax, theme):
    t = THEMES[theme]
    ax.set_xlim(0, 11.5)
    ax.set_ylim(-0.4, 2.8)
    w = np.linspace(1.0, 11.0, 300)
    ax.plot(w, np.log(w), color="#0284c7", lw=2.6, zorder=4)
    end_label(ax, 11.1, np.log(11) + 0.08, "u=ln W", "#0284c7")
    W1, W2, p = 2.0, 10.0, 0.5
    EW = p * W1 + (1 - p) * W2  # 6
    Eu = p * np.log(W1) + (1 - p) * np.log(W2)
    import math
    EC = math.exp(Eu)  # 4.47
    ax.plot([W1, W2], [np.log(W1), np.log(W2)], color=t["muted"], lw=1.4,
            linestyle="--", zorder=3)
    for wx, nm in ((W1, "W1"), (W2, "W2")):
        ax.plot([wx, wx], [0, np.log(wx)], color=t["muted"], lw=1.0, linestyle=":",
                zorder=2)
    ax.plot(EW, np.log(EW), "o", ms=8, color="#d97706", zorder=5)
    label(ax, EW + 0.15, np.log(EW) + 0.18, "E[W]", "#d97706", theme)
    ax.plot([EC, EC], [0, Eu], color="#65a30d", lw=1.4, linestyle=":", zorder=2)
    ax.plot(EC, Eu, "s", ms=8, color="#65a30d", zorder=5)
    label(ax, EC - 0.35, Eu + 0.15, "EC", "#65a30d", theme, ha="right")
    ax.plot([EC, EW], [Eu, Eu], color="#65a30d", lw=2.6, zorder=5)
    label(ax, (EC + EW) / 2 + 0.15, Eu - 0.32, "prima", "#65a30d", theme, ha="center", fontsize=10)
    ax.set_xticks([W1, EC, EW, W2])
    ax.set_xticklabels(["W1", "EC", "E[W]", "W2"])
    ax.set_yticks([])
    ax.set_title("Equivalente cierto y prima", fontsize=12, fontweight="bold")
    ax.set_xlabel("riqueza W", fontsize=11.5, fontweight="bold")


def right(ax, theme):
    t = THEMES[theme]
    ax.set_xlim(0, 4.4)
    ax.set_ylim(0, 7.5)
    e = np.linspace(0, 4, 200)
    ax.plot(e, 0.5 * e, color="#0284c7", lw=2.4, zorder=4)
    end_label(ax, 4.05, 2.15, "cH suave", "#0284c7", fontsize=11)
    ax.plot(e, 1.5 * e, color="#d97706", lw=2.4, zorder=4)
    end_label(ax, 4.05, 6.15, "cL empinado", "#d97706", fontsize=11)
    # salario escalon: 1 si e<2, 4 si e>=2
    ax.plot([0, 2, 2, 4.2], [1, 1, 4, 4], color="#65a30d", lw=2.2, zorder=4)
    end_label(ax, 4.25, 4.0, "w(e)", "#65a30d", fontsize=11)
    ax.plot([2, 2], [0, 4], color=t["muted"], lw=1.2, linestyle=":", zorder=2)
    # el tick ya rotula e*; sin etiqueta extra para no tapar el escalón
    ax.set_xticks([2])
    ax.set_xticklabels(["e*"])
    ax.set_yticks([1, 4])
    ax.set_yticklabels(["1", "4"])
    ax.set_title("Separación de Spence", fontsize=12, fontweight="bold")
    ax.set_xlabel("educación e", fontsize=11.5, fontweight="bold")


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.8))
    fig.clear()
    fig.subplots_adjust(bottom=0.18, top=0.84, wspace=0.28)
    a1 = fig.add_subplot(1, 2, 1)
    a2 = fig.add_subplot(1, 2, 2)
    for ax in (a1, a2):
        ax.grid(True, linestyle="--", linewidth=0.7)
    left(a1, theme)
    right(a2, theme)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/riesgo-ce-prima", theme=th, outdir=OUTDIR_MD)
