"""Dos distribuciones de rendimiento: A (media +, ancha) y B (media -, angosta). Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, THEMES, OUTDIR_MD, label


def draw(theme):
    t = THEMES[theme]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
    fig.patch.set_alpha(0.0)
    for a in (a1, a2):
        a.set_facecolor("none")
        a.grid(True, linestyle="--", linewidth=0.7, color=t["grid"],
               alpha=0.6)
        a.set_xlabel("rendimiento", fontsize=11, fontweight="bold")
    a1.set_ylabel("probabilidad", fontsize=11, fontweight="bold")
    for a in (a1, a2):
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    x = np.linspace(-6, 6, 400)
    a1.plot(x, np.exp(-((x - 1.2) ** 2) / (2 * 2.2 ** 2)), color="#0284c7",
            lw=2.8)
    a1.axvline(0, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    a1.axvline(1.2, color="#0284c7", lw=1.2, linestyle=(0, (3, 3)))
    a1.set_title("A: media positiva, mayor varianza", fontsize=11,
                 color=t["fg"], fontweight="bold")
    a1.set_xlim(-6, 6)
    a2.plot(x, np.exp(-((x + 1.0) ** 2) / (2 * 1.0 ** 2)), color="#d97706",
            lw=2.8)
    a2.axvline(0, color=t["muted"], lw=1.4, linestyle=(0, (5, 4)))
    a2.axvline(-1.0, color="#d97706", lw=1.2, linestyle=(0, (3, 3)))
    a2.set_title("B: media negativa, menor varianza", fontsize=11,
                 color=t["fg"], fontweight="bold")
    a2.set_xlim(-6, 6)
    label(a1, 1.2, 0.12, "muA > 0", "#0284c7", theme, ha="center",
          fontsize=10)
    label(a2, -1.0, 0.12, "muB < 0", "#d97706", theme, ha="center",
          fontsize=10)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/distribuciones-AB", theme=th, outdir=OUTDIR_MD)
