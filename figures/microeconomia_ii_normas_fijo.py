"""Impuestos vs normas con P fijo: CMgc, CMgT, CMgS y areas. Clase 15."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from matplotlib.patches import Polygon
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, TINTS


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.8))
    t = THEMES[theme]
    P = 12.0
    q = np.linspace(0, 13, 400)
    cmgc = 1.0 * q
    cmgT = 2.0 * q
    cmgS = 3.0 * q
    ax.plot(q, cmgc, color=ROLES["alt"], lw=2.0)
    ax.text(10.0, 10.35, "CMgc", fontsize=11, fontweight="bold",
            color=ROLES["alt"], ha="left", va="center")
    ax.plot(q, cmgT, color=ROLES["c1"], lw=2.4)
    ax.text(6.6, 13.4, "CMgT", fontsize=11, fontweight="bold",
            color=ROLES["c1"], ha="left", va="center")
    ax.plot(q, cmgS, color=ROLES["budget"], lw=2.8)
    ax.text(4.6, 14.2, "CMgS", fontsize=11, fontweight="bold",
            color=ROLES["budget"], ha="left", va="center")
    ax.axhline(P, color=t["fg"], lw=1.8)
    label(ax, 13.1, P, "P", t["fg"], theme, fontsize=12)
    qS, qE = 4.0, 6.0
    f = 2.0 * qS
    # perdida empresa ECd: triangulo E(qE,P), C(qS,P), d(qS,f)
    ax.add_patch(Polygon([[qS, P], [qE, P], [qS, f]],
                         facecolor=TINTS[theme]["loss"], edgecolor="none",
                         zorder=1))
    # recaudacion acdf: rectangulo (0,f)-(qS,P)
    ax.fill_between([0, qS], [P, P], [f, f],
                    facecolor=TINTS[theme]["debt"], edgecolor="none",
                    zorder=1)
    # ganancia ambiental: trapecio bajo CMgc entre qS y qE
    xg = np.linspace(qS, qE, 50)
    ax.fill_between(xg, 0 * xg, 1.0 * xg, facecolor=TINTS[theme]["save"],
                    edgecolor="none", zorder=1)
    for qv in (qS, qE):
        ax.plot([qv, qv], [0, P], linestyle=":", color=t["muted"], lw=1.2)
    ax.plot(qS, P, "o", ms=9, color=t["fg"], zorder=5)
    ax.plot(qE, P, "o", ms=9, color=t["fg"], zorder=5)
    label(ax, qS, 0.7, "qS", t["fg"], theme, ha="center", fontsize=11)
    label(ax, qE, 0.7, "qE", t["fg"], theme, ha="center", fontsize=11)
    label(ax, qS + 0.2, P + 0.5, "C", t["fg"], theme, fontsize=12)
    label(ax, qE + 0.2, P + 0.5, "E", t["fg"], theme, fontsize=12)
    label(ax, 0.25, f, "f", t["fg"], theme, fontsize=11)
    label(ax, 2.0, 10.0, "t", ROLES["c2"], theme, fontsize=12)
    label(ax, 5.2, 9.0, "ECd", t["muted"], theme, fontsize=10)
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 15.5)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="q", ylabel="P, CMg")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/impuestos-normas-fijo", theme=th,
             outdir=OUTDIR_MD)
