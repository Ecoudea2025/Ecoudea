"""FPP individuales de Robinson y Venus + conjunta quebrada exterior con puntos."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(0, 260)
    ax.set_ylim(0, 260)
    P = np.linspace(0, 240, 300)
    # individuales: CR=160-2PR (P:0..80), CV=80-0.5PV (P:0..160)
    ax.plot([0, 80], [160, 0], color="#0284c7", lw=2.0, zorder=3)
    end_label(ax, 81, 4, "CR", "#0284c7", fontsize=11)
    ax.plot([0, 160], [80, 0], color="#d97706", lw=2.0, zorder=3)
    end_label(ax, 161, 4, "CV", "#d97706", fontsize=11)
    # conjunta quebrada exterior: (0,240)->(160,160)->(240,0)
    jx = [0, 160, 240]
    jy = [240, 160, 0]
    ax.plot(jx, jy, color="#65a30d", lw=2.8, zorder=4)
    label(ax, 100, 205, "conjunta", "#65a30d", theme, ha="center")
    # ganancia de especializacion: triangulo (120,120)-(160,120)-(160,160)
    ax.fill([120, 160, 160], [120, 120, 160], facecolor=TINTS[theme]["save"],
            edgecolor="none", zorder=1)
    label(ax, 145, 130, "ganancia", "#65a30d", theme, ha="center", fontsize=9)
    # puntos: (120,120) alfa=beta=0.5 ; (80,80) invertida
    ax.plot(120, 120, "o", ms=9, color=t["fg"], zorder=5,
            markeredgecolor="#65a30d", markeredgewidth=1.6)
    label(ax, 120, 108, "(120,120)", t["fg"], theme, ha="center", fontsize=9)
    ax.plot(80, 80, "s", ms=8, color="#b91c1c", zorder=5)
    label(ax, 80, 68, "(80,80)", "#b91c1c", theme, ha="center", fontsize=9)
    ax.plot(160, 160, "o", ms=9, color="#65a30d", zorder=5,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    label(ax, 163, 168, "(160,160)", "#65a30d", theme, fontsize=9)
    ax.plot(0, 240, "o", ms=7, color=t["muted"], zorder=5)
    ax.plot(240, 0, "o", ms=7, color=t["muted"], zorder=5)
    pure_axes(ax, [0, 80, 160, 240], ["0", "80", "160", "240"],
              [0, 80, 160, 240], ["0", "80", "160", "240"],
              xlabel="P", ylabel="C")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/fpp-conjunta", theme=th, outdir=OUTDIR_MD)
