"""Condorcet y Arrow: triangulo dirigido X->Y->Z->X + esquema de la deduccion imposible."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.patches as mp
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, TINTS


def draw(theme):
    fig, _ = setup_eco(theme, figsize=(10.8, 3.6))
    fig.clear()
    fig.subplots_adjust(bottom=0.18, top=0.84, wspace=0.28)
    t = THEMES[theme]
    a1 = fig.add_subplot(1, 2, 1)
    a2 = fig.add_subplot(1, 2, 2)
    for ax in (a1, a2):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
    # izquierda: triangulo X->Y->Z->X con puntas que aterrizan
    pos = {"X": (5.0, 8.0), "Y": (1.8, 2.2), "Z": (8.2, 2.2)}
    for n, (x, y) in pos.items():
        a1.add_patch(mp.Circle((x, y), 0.85, facecolor="#0284c7", edgecolor="none", zorder=3))
        a1.text(x, y, n, ha="center", va="center", fontsize=14, fontweight="bold",
                color="white", zorder=4)
        a1.text(x, y - 1.35, n, ha="center", va="center", fontsize=11,
                color=t["fg"], bbox=halo(theme), zorder=4)
    a1.set_title("Ciclo de Condorcet (2 a 1)", fontsize=12, fontweight="bold")
    for A, B in (("X", "Y"), ("Y", "Z"), ("Z", "X")):
        a1.annotate("", xy=pos[B], xytext=pos[A],
                    arrowprops=dict(arrowstyle="->", color="#d97706", lw=2.2,
                                    connectionstyle="arc3,rad=0.22",
                                    shrinkA=14, shrinkB=14))
    # derecha: esquema de Arrow
    a2.set_title("La deducción imposible", fontsize=12, fontweight="bold")
    boxes = [("Y ~S Z", "no dictadura", 1.2, 7.0), ("X >S Y", "unanimidad", 1.2, 4.2)]
    for txt, sub, x, y in boxes:
        a2.add_patch(mp.FancyBboxPatch((x, y - 0.7), 3.6, 1.5,
                     boxstyle="round,pad=0.1", facecolor=TINTS[theme]["excl"],
                     edgecolor="#0284c7", lw=1.6, zorder=3))
        a2.text(x + 1.8, y + 0.15, txt, ha="center", va="center", fontsize=12,
                fontweight="bold", color=t["fg"], zorder=4)
        a2.text(x + 1.8, y - 0.45, sub, ha="center", va="center", fontsize=9,
                color=t["muted"], zorder=4)
    a2.annotate("", xy=(6.3, 5.6), xytext=(5.0, 5.6),
                arrowprops=dict(arrowstyle="->", color="#d97706", lw=2.2))
    a2.add_patch(mp.FancyBboxPatch((6.5, 1.6), 3.3, 2.6,
                 boxstyle="round,pad=0.1", facecolor=TINTS[theme]["loss"],
                 edgecolor="#b91c1c", lw=1.8, zorder=3))
    a2.text(8.15, 3.5, "X >S Z", ha="center", va="center", fontsize=12,
            fontweight="bold", color="#b91c1c", zorder=4)
    a2.text(8.15, 2.7, "dictadura del agente i", ha="center", va="center", fontsize=8,
            color=t["fg"], zorder=4)
    label(a2, 5.65, 6.35, "transitividad", "#d97706", theme, ha="center", fontsize=9)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/condorcet-arrow", theme=th, outdir=OUTDIR_MD)
