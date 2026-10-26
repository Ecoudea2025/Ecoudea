"""Torrens vs BBK: crecimiento balanceado a R=44,9% frente a senda con e_j desigual.
Escala logaritmica: la pendiente es la tasa; la senda no balanceada crece al min(e_j)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    ax.set_xlim(0, 7.0)
    ax.set_ylim(4.4, 6.4)
    tt = np.linspace(0, 6.0, 120)
    g_bal, g_des = 0.449, 0.25
    # en escala logaritmica la senda es recta y la pendiente es log10(1+g)
    ax.plot(tt, 5.0 + np.log10(1 + g_bal) * tt, color="#0284c7", lw=2.6, zorder=4)
    ax.plot(tt, 5.0 + np.log10(1 + g_des) * tt, color="#d97706", lw=2.2,
            linestyle="--", zorder=4)
    end_label(ax, 6.08, 5.0 + np.log10(1 + g_bal) * 6.0, "g* = R (Torrens)",
              "#0284c7", ha="left", fontsize=11)
    end_label(ax, 6.08, 5.0 + np.log10(1 + g_des) * 6.0, "g = min ej",
              "#d97706", fontsize=10, ha="left")
    label(ax, 2.5, 6.05, "log Y", t["fg"], theme, ha="center", fontsize=11)
    label(ax, 2.5, 4.95, "la pendiente es la tasa", t["muted"], theme,
          ha="center", fontsize=10, bold=False)
    pure_axes(ax, [0, 5], ["t0", "t"], [], [],
              xlabel="tiempo", ylabel="producto (log)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/torrens-vs-bbk", theme=th, outdir=OUTDIR_MD)
