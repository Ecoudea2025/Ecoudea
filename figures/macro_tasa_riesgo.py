"""Tasa efectiva con riesgo de impago: r = r*/(1−p), convexa, asíntota en
p=1, cota r̄ y región sombreada de exclusión crediticia. Clase 06."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    rs, rb = 0.10, 0.40
    ps = 1 - rs / rb  # umbral donde r(p*) = r̄
    p = np.linspace(0, 0.985, 300)
    ax.plot(p, rs / (1 - p), color=ROLES["budget"], lw=2.8)
    ax.text(0.42, 0.60, "r = r*/(1−p)", fontsize=12, fontweight="bold",
            color=ROLES["budget"], ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # cota máxima y región de exclusión
    ax.axhline(rb, color=t["muted"], lw=1.6, linestyle=(0, (5, 4)))
    ax.text(1.0, rb + 0.015, "r̄", fontsize=12, fontweight="bold",
            color=t["muted"], ha="right", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # exclusión: tinta sólida premezclada (nada de alpha en rellenos: el
    # sombreado debe verse igual en web, PDF e impresión)
    excl = "#DCEAEC" if theme == "light" else "#091D2F"
    ax.axvspan(ps, 1.0, facecolor=excl, edgecolor="none", zorder=1)
    ax.text(0.875, 0.10, "exclusión", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="bottom")
    # asíntota en p=1
    ax.axvline(1.0, color=t["muted"], lw=1.2, linestyle=(0, (3, 3)), alpha=0.8)
    ax.plot(ps, rb, "o", ms=9, color=ROLES["endow"], zorder=5)
    ax.text(ps - 0.03, rb + 0.03, "p*", fontsize=12, fontweight="bold",
            color=ROLES["endow"], ha="right", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 0.68)
    pure_axes(ax, [ps, 1.0], ["p*", "1"], [rs, rb], ["r*", "r̄"],
              xlabel="p", ylabel="r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/tasa-riesgo", theme=th, outdir=OUTDIR_MD)
