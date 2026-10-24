"""q de Tobin: curva creciente que cruza (0, 1); arriba se invierte,
abajo se desinvierte. Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    inv = "#E2EACD" if theme == "light" else "#192718"
    des = "#F6D5D6" if theme == "light" else "#2C1121"
    I = np.linspace(-3, 4.5, 300)
    q = 1 + 0.3 * I + 0.05 * I ** 2
    # zonas que siguen la curva: inversión (I>0, q>1) y desinversión (I<0)
    m_inv = I >= 0
    ax.fill_between(I[m_inv], 1, q[m_inv],
                    facecolor=inv, edgecolor="none", zorder=1)
    m_des = I <= 0
    ax.fill_between(I[m_des], q[m_des], 1,
                    facecolor=des, edgecolor="none", zorder=1)
    ax.plot(I, q, color=ROLES["budget"], lw=2.8)
    ax.text(4.62, 3.36, "q=1+C′(I)", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    ax.axhline(1.0, color=t["muted"], lw=1.6, linestyle=(0, (5, 4)))
    ax.text(5.9, 1.06, "q=1", fontsize=12, fontweight="bold",
            color=t["muted"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.plot(0, 1, "o", ms=10, color=accent(theme), zorder=5)
    ax.text(4.2, 1.9, "invierte", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(-1.8, 0.72, "desinvierte", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(-3.5, 6.4)
    ax.set_ylim(0.2, 3.8)
    pure_axes(ax, [0], ["0"], [1], ["1"], xlabel="I", ylabel="q")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/q-tobin", theme=th, outdir=OUTDIR_MD)
