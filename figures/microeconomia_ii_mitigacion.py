"""Mitigacion Tobon-Vasco: salto CMgTD -> CMgT e impuesto. Clase 15."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, TINTS, gap_caps


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.8))
    t = THEMES[theme]
    Q = np.linspace(0, 0.8, 400)
    for slope, name, col, xl, yl in [(1.2, "CMgc", ROLES["alt"], 0.72, 0.94),
                                   (1.4, "CMgT", ROLES["c1"], 0.75, 1.13),
                                   (1.6, "CMgD", "#e11d48", 0.78, 1.33),
                                   (2.6, "CMgS", ROLES["budget"], 0.80, 2.16),
                                   (3.0, "CMgTD", "#7c3aed", 0.83, 2.57)]:
        ax.plot(Q, slope * Q, lw=2.2 if name != "CMgS" else 2.8, color=col)
        ax.text(xl, yl, name, fontsize=10, fontweight="bold",
                color=col, ha="left", va="center")
    ax.axhline(1.0, color=t["fg"], lw=1.8)
    label(ax, 0.9, 0.72, "PT=1", t["fg"], theme, fontsize=12)
    qD, qTD, qS, qT = 0.29, 0.33, 0.3846, 0.7143
    for qv, nm, ha, yy in [(qD, "qD", "right", -0.07),
                           (qS, "qS", "center", -0.07),
                           (qT, "qT", "center", -0.07)]:
        ax.plot([qv, qv], [0, 1.0], linestyle=":", color=t["muted"], lw=1.1)
        label(ax, qv, yy, nm, t["muted"], theme, ha=ha, fontsize=9)
    ax.plot([qTD, qTD], [0, 1.0], linestyle=":", color=t["muted"], lw=1.1)
    label(ax, 0.36, 0.10, "qTD", t["muted"], theme, ha="left",
          fontsize=9)
    # recorrido: por CMgTD hasta qD, salto a CMgT, tramo hasta qS
    ax.annotate("", xy=(0.27, 0.81), xytext=(0.05, 0.15),
                arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=2.0))
    ax.plot([qD, qD], [3.0 * qD, 1.4 * qD], linestyle=(0, (4, 3)),
            color=t["muted"], lw=1.8)
    ax.annotate("", xy=(qS - 0.01, 1.4 * (qS - 0.01)),
                xytext=(qD + 0.01, 1.4 * (qD + 0.01)),
                arrowprops=dict(arrowstyle="->", color=ROLES["c1"],
                                lw=2.0))
    # pago de impuestos: cuadrilatero entre CMgT y PT=1 en [qD, qS]
    xs = np.linspace(qD, qS, 40)
    ax.fill_between(xs, 1.4 * xs, np.ones_like(xs),
                    facecolor=TINTS[theme]["debt"], edgecolor="none",
                    zorder=1)
    gap_caps(ax, 0.44, 1.4 * qS, 1.0, ROLES["c2"], theme=theme, cap=0.04)
    label(ax, 0.42, 0.77, "t", ROLES["c2"], theme, fontsize=12,
          ha="right")
    ax.set_xlim(0, 0.95)
    ax.set_ylim(-0.12, 2.6)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="Q", ylabel="PT")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/mitigacion-tobon", theme=th, outdir=OUTDIR_MD)
