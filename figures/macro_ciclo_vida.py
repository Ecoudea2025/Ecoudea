"""Ciclo de vida de Modigliani: ingreso acampanado, consumo constante C̄,
áreas A (deuda joven), B (ahorro maduro), C (desahorro vejez) y senda de
activos netos A_t. Clase 07."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.6))
    t = THEMES[theme]
    bg = "#faf8f1" if theme == "light" else "#0a0f1a"
    N = 78
    tt = np.linspace(0, N, 400)
    # ingreso laboral acampanado (cero antes de los 18 y al morir)
    s = np.clip((tt - 18) / (N - 18), 0, 1)
    Y = 100 * np.sin(np.pi * s) ** 0.8
    Cbar = np.full_like(tt, 55.0)
    # activos netos: deuda joven, ahorro maduro, agotamiento al final
    A = 0.0049 * (tt - 18) * (N - tt) * (tt - 45)
    A = np.where((tt >= 18) & (tt <= N), A, 0.0)
    # áreas: A y C (Y < C̄) en ámbar, B (Y > C̄) en verde
    # áreas: tintas sólidas premezcladas (nada de alpha en rellenos)
    debt = "#F5E3CB" if theme == "light" else "#2B2017"
    save_ = "#E2EACD" if theme == "light" else "#192718"
    ax.fill_between(tt, Y, Cbar, where=(Y < Cbar) & (tt >= 18),
                    facecolor=debt, edgecolor="none", zorder=1)
    ax.fill_between(tt, Y, Cbar, where=(Y >= Cbar),
                    facecolor=save_, edgecolor="none", zorder=1)
    ax.plot(tt, Y, color=ROLES["c1"], lw=2.8)
    ax.plot(tt, Cbar, color=t["muted"], lw=2.0, linestyle=(0, (5, 4)))
    ax.plot(tt, A, color=accent(theme), lw=2.2, linestyle=(0, (2, 2)))
    ax.axhline(0, color=t["muted"], lw=1.0, alpha=0.7)
    # etiquetas directas en extremos con fondo
    # C̄ ya va rotulado en el tick del eje Y: no duplicar al final de la línea
    ax.text(62, 88, "Yₗ−T", fontsize=12, fontweight="bold", color=ROLES["c1"],
            ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    ax.text(60, 62, "Aₜ", fontsize=12, fontweight="bold", color=accent(theme),
            ha="left", va="bottom",
            bbox=dict(facecolor=bg, edgecolor="none", pad=1.6, alpha=0.9))
    # letras de etapa centradas en su región
    ax.text(23, 42, "A", fontsize=13, fontweight="bold", color=t["muted"],
            ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=2.0, alpha=0.9))
    ax.text(46, 78, "B", fontsize=13, fontweight="bold", color=t["muted"],
            ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=2.0, alpha=0.9))
    ax.text(75.5, 47, "C", fontsize=13, fontweight="bold", color=t["muted"],
            ha="center", va="center",
            bbox=dict(facecolor=bg, edgecolor="none", pad=2.0, alpha=0.9))
    ax.set_xlim(0, 82)
    ax.set_ylim(-55, 112)
    pure_axes(ax, [18, 45, 60, 78], ["18", "45", "60", "78"], [55], ["C̄"],
              xlabel="edad t", ylabel="")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/ciclo-vida", theme=th, outdir=OUTDIR_MD)
