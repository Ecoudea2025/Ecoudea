"""Caja de Edgeworth con curva de contrato y lente de mejoras desde la dotacion.
alpha=0.6, beta=0.3, W1=10, W2=8: la curva X12*=f(X11) es analitica (RMS1=RMS2)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS, pure_axes


A, B = 0.6, 0.3
W1, W2 = 10.0, 8.0
OM = np.array([7.0, 2.5])  # dotacion inicial (mucho X1 para A... en coords A)


def u1(x11, x12):
    return (x11 ** A) * (x12 ** (1 - A))


def u2(x11, x12):
    x21, x22 = W1 - x11, W2 - x12
    return (x21 ** B) * (x22 ** (1 - B))


def contract(x11):
    # despeje analitico de RMS1=RMS2 (ver clase 03, Paso 4)
    return B * (1 - A) * W2 * x11 / (A * (1 - B) * W1 + (B - A) * x11)


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(-1.0, 11.0)
    ax.set_ylim(0, 9.2)
    ax.plot([0, W1, W1, 0, 0], [0, 0, W2, W2, 0], color=t["muted"], lw=1.6, zorder=3)
    label(ax, 0.35, 8.55, "O2", t["fg"], theme, fontsize=12)
    label(ax, 9.65, 0.45, "O1", t["fg"], theme, fontsize=12)
    # curva de contrato analitica
    xs = np.linspace(0.05, 9.95, 300)
    ax.plot(xs, contract(xs), color="#65a30d", lw=2.6, zorder=4)
    end_label(ax, 9.85, contract(9.9) + 0.2, "contrato", "#65a30d", ha="right")
    # tres tangencias: curvas de indiferencia por los puntos de la curva
    for x11 in (3.0, 5.5, 8.0):
        x12 = contract(x11)
        u1v = u1(x11, x12)
        u2v = u2(x11, x12)
        g1 = np.linspace(0.4, 9.8, 300)
        ax.plot(g1, (u1v / g1 ** A) ** (1 / (1 - A)), color="#0284c7", lw=1.6, zorder=3)
        g2 = np.linspace(0.2, 9.8, 300)
        y2 = W2 - (u2v / (W1 - g2) ** B) ** (1 / (1 - B))
        ok = (y2 > 0) & (y2 < W2) & ((W1 - g2) > 0.05)
        ax.plot(g2[ok], y2[ok], color="#d97706", lw=1.6, zorder=3)
        ax.plot(x11, x12, "o", ms=8, color=t["fg"], zorder=5,
                markeredgecolor="#65a30d", markeredgewidth=1.6)
    label(ax, 6.5, 3.2, "RMS1 = RMS2", "#65a30d", theme, ha="center")
    # dotacion y lente de mejoras: {U1>=U1(w)} cap {U2>=U2(w)}
    ax.plot(OM[0], OM[1], "D", ms=9, color="#d97706", zorder=6)
    label(ax, OM[0] + 0.3, OM[1] - 0.45, "ω", "#d97706", theme, fontsize=13)
    g = np.linspace(0.05, 9.95, 240)
    G1, G2 = np.meshgrid(g, np.linspace(0.05, 7.95, 200))
    mask = (u1(G1, G2) >= u1(*OM)) & (u2(G1, G2) >= u2(*OM))
    ax.contourf(G1, G2, mask.astype(float), levels=[0.5, 1.5],
                colors=[TINTS[theme]["save"]], zorder=1)
    label(ax, 8.3, 2.2, "lente", t["muted"], theme, fontsize=10)
    pure_axes(ax, [0, W1], ["0", "W1"], [0, W2], ["0", "W2"],
              xlabel="bien 1 (X11)", ylabel="bien 2 (X12)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/edgeworth-contrato", theme=th, outdir=OUTDIR_MD)
