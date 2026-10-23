"""Oferta y demanda con equilibrio y excedentes (Microeconomía).

Genera: src/assets/figures/microeconomia/oferta-demanda-{light,dark}.svg
Uso: python figures/oferta_demanda.py [--theme light|dark|both]
"""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup, save, PALETTE

Q = np.linspace(0, 10, 200)
DEMANDA = 10 - 0.9 * Q          # P = 10 - 0.9Q
OFERTA = 1 + 0.7 * Q            # P = 1 + 0.7Q
QE = (10 - 1) / (0.9 + 0.7)     # 5.625
PE = 10 - 0.9 * QE              # 4.9375


def draw(theme):
    fig, ax = setup(theme)
    ax.plot(Q, DEMANDA, color=PALETTE["macro"], lw=2.4, label="Demanda")
    ax.plot(Q, OFERTA, color=PALETTE["micro"], lw=2.4, label="Oferta")
    # Excedente del consumidor y del productor
    qf = np.linspace(0, QE, 100)
    ax.fill_between(qf, 10 - 0.9 * qf, PE, color=PALETTE["macro"], alpha=0.18, label="Excedente consumidor")
    ax.fill_between(qf, PE, 1 + 0.7 * qf, color=PALETTE["micro"], alpha=0.18, label="Excedente productor")
    # Equilibrio
    ax.plot([QE], [PE], "o", color=PALETTE["estadistica"], ms=8, zorder=5)
    ax.annotate(f"E = ({QE:.2f}, {PE:.2f})", (QE, PE), textcoords="offset points",
                xytext=(10, -18), fontsize=10)
    ax.plot([QE, QE], [0, PE], color=PALETTE["estadistica"], lw=1.2, ls=":")
    ax.plot([0, QE], [PE, PE], color=PALETTE["estadistica"], lw=1.2, ls=":")
    ax.set_xlabel("Cantidad (Q)")
    ax.set_ylabel("Precio (P)")
    ax.set_title("Equilibrio de mercado y excedentes")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    return fig


if __name__ == "__main__":
    arg = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    themes = ["light", "dark"] if arg == "both" else [arg]
    for th in themes:
        save(draw(th), "microeconomia/oferta-demanda", theme=th)
