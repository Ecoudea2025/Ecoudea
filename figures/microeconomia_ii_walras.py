"""Ley de Walras en la caja: recta fuera de equilibrio con excesos vs recta tangente.
CD: A: alpha=0.6, B: beta=0.4; dotaciones W1=(2,2), W2=(1,3); p* analitico."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS, pure_axes


A, B = 0.6, 0.4
W1i = np.array([2.0, 2.0])
W2i = np.array([1.0, 3.0])
W1, W2 = 3.0, 5.0
# p1* = (a1*W12+a2*W22)/(W1-a1*W11-a2*W21): vacia ambos mercados
PSTAR = (A * W1i[1] + B * W2i[1]) / (W1 - A * W1i[0] - B * W2i[0])
P0 = 0.55 * PSTAR  # precio de desequilibrio


def demands(p1):
    # p2 = 1 numerario; devuelve (X1, X2) de cada agente
    out = []
    for a, w in ((A, W1i), (B, W2i)):
        E = p1 * w[0] + w[1]
        out.append(np.array([a * E / p1, (1 - a) * E]))
    return out


def u1v(x11, x12):
    return x11 ** A * x12 ** (1 - A)


def u2v(x11, x12):
    return (W1 - x11) ** B * (W2 - x12) ** (1 - B)


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(-0.45, 3.6)
    ax.set_ylim(0, 5.9)
    ax.plot([0, W1, W1, 0, 0], [0, 0, W2, W2, 0], color=t["muted"], lw=1.6, zorder=3)
    label(ax, 0.18, 5.55, "O2", t["fg"], theme, fontsize=12)
    label(ax, 2.82, 0.35, "O1", t["fg"], theme, fontsize=12)
    W = W1i  # dotacion agregada vista desde O1
    ax.plot(W[0], W[1], "D", ms=9, color="#d97706", zorder=6)
    label(ax, W[0] + 0.12, W[1] - 0.3, "W", "#d97706", theme)
    # recta de desequilibrio P0 por W + elecciones
    (a1, a2) = demands(P0)
    xs = np.linspace(0.2, 3.2, 60)
    ax.plot(xs, W[1] + P0 * (W[0] - xs), color=t["muted"], lw=1.6, linestyle="--", zorder=3)
    end_label(ax, 3.05, W[1] + P0 * (W[0] - 3.05) + 0.15, "P0", t["muted"], ha="right")
    for pt, nm, col, lx, ly in ((a1, "X1", "#0284c7", 0.12, 0.18),
                             (a2, "X2", "#d97706", -0.42, -0.4)):
        ax.plot(pt[0], pt[1], "o", ms=8, color=col, zorder=5)
        label(ax, pt[0] + lx, pt[1] + ly, nm, col, theme)
    # corchetes de exceso: z11+z21 en X, z12+z22 en Y
    z1 = (a1[0] - W1i[0]) + (a2[0] - W2i[0])
    z2 = (a1[1] - W1i[1]) + (a2[1] - W2i[1])
    ax.annotate("", xy=(a1[0], 4.6), xytext=(a2[0], 4.6),
                arrowprops=dict(arrowstyle="<->", color="#b91c1c", lw=1.6))
    label(ax, (a1[0] + a2[0]) / 2, 4.85, "z11+z21 != 0", "#b91c1c", theme, ha="center", fontsize=9)
    ax.annotate("", xy=(0.35, a1[1]), xytext=(0.35, a2[1]),
                arrowprops=dict(arrowstyle="<->", color="#b91c1c", lw=1.6))
    label(ax, 0.35, (a1[1] + a2[1]) / 2 + 0.25, "z12+z22 != 0", "#b91c1c", theme,
          ha="center", fontsize=9, va="bottom")
    # recta de equilibrio P* por W + tangencia unica sobre el contrato
    (b1, b2) = demands(PSTAR)
    ax.plot(xs, W[1] + PSTAR * (W[0] - xs), color="#65a30d", lw=2.2, zorder=4)
    end_label(ax, 2.75, W[1] + PSTAR * (W[0] - 2.75) + 0.12, "P*", "#65a30d")
    ax.plot(b1[0], b1[1], "o", ms=10, color="#65a30d", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    # indiferencias tangentes por el equilibrio
    g = np.linspace(0.3, 2.9, 200)
    ax.plot(g, (u1v(b1[0], b1[1]) / g ** A) ** (1 / (1 - A)), color="#0284c7", lw=1.6, zorder=3)
    gg = np.linspace(0.1, 2.9, 200)
    y2 = W2 - (u2v(b1[0], b1[1]) / (W1 - gg) ** B) ** (1 / (1 - B))
    ok = (y2 > 0) & (y2 < W2) & ((W1 - gg) > 0.05)
    ax.plot(gg[ok], y2[ok], color="#d97706", lw=1.6, zorder=3)
    label(ax, 1.9, 1.35, "Z(P*) = 0", "#65a30d", theme, ha="center")
    pure_axes(ax, [0, W1], ["0", "W1"], [0, W2], ["0", "W2"],
              xlabel="bien 1", ylabel="bien 2")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/walras-equilibrio", theme=th, outdir=OUTDIR_MD)
