"""Frontera salario-beneficio en mercancía patrón: r = R(1-ω), recta de
(R, 0) a (0, Ŵ). La técnica traza la frontera, la sociedad elige el punto.
Clases 20-21."""
import sys
sys.path.insert(0, "figures")
import numpy as np
import matplotlib.pyplot as plt
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, accent, label, project, pure_axes


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    R = 0.25
    ax.set_xlim(0, 1.18)
    ax.set_ylim(0, 0.30)
    w = np.linspace(0, 1, 200)
    ax.plot(w, R * (1 - w), color=accent(theme), lw=2.4, zorder=4)
    # puntos de reparto: todo a beneficios, mitad, todo a salarios
    for wi, ms, txt in [(0.0, 9, "todo a beneficios"), (0.5, 9, "reparto"),
                        (1.0, 9, "todo a salarios")]:
        ri = R * (1 - wi)
        ax.plot(wi, ri, "o", ms=ms, color=ROLES["endow"], zorder=5)
        project(ax, wi, ri, theme)
    pure_axes(ax, [0, 0.5, 1.0], ["0", "1/2", "ω=1 (Ŵ)"],
              [0, R], ["0", "R=25%"], xlabel="salario (ω)",
              ylabel="tasa de beneficio (r)")
    label(ax, 0.52, 0.20, "r = R(1-ω)", accent(theme), theme, fontsize=12)
    ax.text(1.02, 0.02, "patrón: recta", fontsize=10, color=t["muted"],
            ha="left", va="bottom")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/frontera-w-r", theme=th, outdir=OUTDIR_MD)
