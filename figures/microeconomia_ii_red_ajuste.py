"""Ajuste hacia el equilibrio: costes alto/bajo y trayectoria. Clase 16."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import save, ROLES, THEMES, OUTDIR_MD, label, flow


def draw(theme):
    t = THEMES[theme]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    fig.patch.set_alpha(0.0)
    for a in (a1, a2):
        a.set_facecolor("none")
        a.grid(True, linestyle="--", linewidth=0.7, color=t["grid"],
               alpha=0.6)
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    n = np.linspace(0, 1000, 400)
    a1.plot(n, n * (1000 - n), color=ROLES["c1"], lw=2.6)
    a1.axhline(300000, color=ROLES["alt"], lw=2.0)
    label(a1, 700, 308000, "coste alto", ROLES["alt"], theme, fontsize=10)
    a1.axhline(160000, color=t["fg"], lw=1.8)
    label(a1, 1010, 160000, "coste bajo", t["fg"], theme, fontsize=10)
    a1.plot(0, 300000, "o", ms=7, color=ROLES["alt"], zorder=5)
    for nx in (200.0, 800.0):
        a1.plot(nx, 160000, "o", ms=7, color=ROLES["budget"], zorder=5)
    a1.set_xlim(0, 1130)
    a1.set_ylim(0, 340000)
    a1.set_xlabel("n", fontweight="bold")
    a1.set_ylabel("p", fontweight="bold")
    a1.set_title("A. Costes alto y bajo", fontsize=11, color=t["fg"],
                 fontweight="bold")
    tt = np.linspace(0, 12, 300)
    n2 = 800.0
    traj = n2 / (1 + 39 * np.exp(-1.2 * (tt - 5)))
    a2.plot(tt, traj, color=ROLES["budget"], lw=2.8)
    a2.axhline(200, color=ROLES["c2"], lw=1.6, linestyle=(0, (5, 4)))
    label(a2, 11.0, 225, "n1", ROLES["c2"], theme, fontsize=11)
    a2.set_xlim(0, 12)
    a2.set_ylim(0, 900)
    a2.set_xlabel("tiempo", fontweight="bold")
    a2.set_ylabel("n", fontweight="bold")
    a2.set_title("B. Despegue tras la masa critica", fontsize=11,
                 color=t["fg"], fontweight="bold")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/red-ajuste", theme=th, outdir=OUTDIR_MD)
