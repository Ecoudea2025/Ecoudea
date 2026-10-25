"""Externalidad negativa: CMgP vs CMgS, impuesto pigouviano t* y triangulo de perdida."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(-0.5, 9.0)
    ax.set_ylim(0, 10.5)
    q = np.linspace(0, 8, 200)
    ax.plot(q, 1 + q, color="#0284c7", lw=2.4, zorder=4)
    end_label(ax, 8.02, 9.3, "CMgP", "#0284c7")
    ax.plot(q, 3 + q, color="#d97706", lw=2.4, zorder=4)
    end_label(ax, 8.02, 11.1 - 0.4, "CMgS", "#d97706")
    ax.plot([0, 8.2], [6, 6], color="#65a30d", lw=2.0, zorder=3)
    end_label(ax, 8.25, 6.0, "P1", "#65a30d")
    qM, qS = 5.0, 3.0  # 1+q=6 ; 3+q=6 (analitico)
    for qq, nm in ((qM, "qM"), (qS, "q*")):
        ax.plot([qq, qq], [0, 6], color=t["muted"], lw=1.1, linestyle=":", zorder=2)
    ax.plot(qM, 6, "o", ms=9, color="#0284c7", zorder=5)
    label(ax, qM + 0.2, 6.45, "qM", "#0284c7", theme)
    ax.plot(qS, 6, "o", ms=9, color="#d97706", zorder=5)
    label(ax, qS - 0.25, 6.45, "q*", "#d97706", theme, ha="right")
    # llave del impuesto en q*: de CMgP(3)=4 a CMgS(3)=6
    ax.annotate("", xy=(qS - 0.12, 6.0), xytext=(qS - 0.12, 4.0),
                arrowprops=dict(arrowstyle="<->", color="#d97706", lw=1.8))
    label(ax, qS - 0.35, 5.0, "t*", "#d97706", theme, ha="right", fontsize=13)
    # DWL: triangulo (3,6)-(5,6)-(5,8)
    ax.fill([3, 5, 5], [6, 6, 8], facecolor=TINTS[theme]["loss"],
            edgecolor="none", zorder=1)
    label(ax, 4.45, 6.5, "perdida", "#b91c1c", theme, ha="center", fontsize=9)
    pure_axes(ax, [0, qS, qM], ["0", "q*", "qM"], [0, 6], ["0", "P1"],
              xlabel="q1", ylabel="costos y precio")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/pigou-externalidad", theme=th, outdir=OUTDIR_MD)
