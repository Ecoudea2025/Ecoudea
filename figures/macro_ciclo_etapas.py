"""Ciclo de vida por etapas: ingreso nulo hasta los 15, hump productivo
15–60 sobre C̄ y retiro desde los 60; deuda juvenil y ahorro sombreados.
Clase 10."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.6))
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    debt = "#E2EACD" if theme == "light" else "#192718"
    save_ = "#F6D5D6" if theme == "light" else "#2C1121"
    N = 78
    tt = np.linspace(0, N, 500)
    s = np.clip((tt - 15) / 45, 0, 1)
    Y = np.where((tt >= 15) & (tt <= 60), 100 * np.sin(np.pi * s) ** 0.9, 0.0)
    Cbar = np.full_like(tt, 55.0)
    # juventud (0–15): consumo sobre ingreso nulo; vida activa: ahorro
    ax.fill_between(tt, Cbar, Y, where=(tt < 15),
                    facecolor=debt, edgecolor="none", zorder=1)
    ax.fill_between(tt, Y, Cbar, where=(Y > Cbar),
                    facecolor=save_, edgecolor="none", zorder=1)
    ax.plot(tt, Y, color=ROLES["c1"], lw=2.8)
    ax.plot(tt, Cbar, color=t["muted"], lw=2.0, linestyle=(0, (5, 4)))
    ax.text(38, 104, "Yₗₜ", fontsize=12, fontweight="bold", color=ROLES["c1"],
            ha="center", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(7.5, 27, "deuda", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(44, 72, "ahorro", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(69, 30, "retiro", fontsize=10, fontstyle="italic",
            color=t["muted"], ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.set_xlim(0, 82)
    ax.set_ylim(-8, 112)
    pure_axes(ax, [0, 15, 60, 78], ["0", "15", "60", "78"], [55], ["C̄"],
              xlabel="edad t", ylabel="")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/ciclo-etapas", theme=th, outdir=OUTDIR_MD)
