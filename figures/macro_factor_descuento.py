"""Factor subjetivo de descuento β^t para tres impaciencias ρ1 > ρ2 > ρ3.
Parte de 1 en t=0 y decae; a mayor impaciencia, caída más rápida. Clase 02."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = np.linspace(0, 20, 300)
    for beta, tag, color in [(0.85, "β₁", ROLES["c2"]),
                             (0.92, "β₂", ROLES["alt"]),
                             (0.97, "β₃", ROLES["c1"])]:
        ax.plot(t, beta ** t, color=color, lw=2.6)
        end_label(ax, 20.4, beta ** 20 + 0.06, tag, color)
    ax.set_xlim(0, 22.5)
    ax.set_ylim(-0.05, 1.12)
    pure_axes(ax, [0, 10, 20], ["0", "10", "20"], [0, 0.5, 1.0],
              ["0", "0.5", "1"], xlabel="t", ylabel="βᵗ")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/factor-descuento", theme=th, outdir=OUTDIR_MD)
