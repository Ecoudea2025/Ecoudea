"""Factor subjetivo de descuento β^t para tres impaciencias ρ1 > ρ2 > ρ3.
Parte de 1 en t=0 y decae; a mayor impaciencia, caída más rápida. Clase 02."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes, end_label, label, accent


def draw(theme):
    fig, ax = setup_eco(theme)
    t_vals = np.linspace(0, 20, 300)

    # Parámetros analíticos exactos de Clase 02
    cases = [
        {"rho": 0.20, "tag": "β₁=0.833 (ρ=0.20, impaciente)", "color": ROLES["c2"]},
        {"rho": 0.10, "tag": "β₂=0.909 (ρ=0.10, moderado)", "color": ROLES["alt"]},
        {"rho": 0.02, "tag": "β₃=0.980 (ρ=0.02, paciente)", "color": ROLES["c1"]},
    ]

    for c in cases:
        beta = 1.0 / (1.0 + c["rho"])
        traj = beta ** t_vals
        ax.plot(t_vals, traj, color=c["color"], lw=2.6)
        # Etiquetado al extremo derecho con suficiente aire
        end_label(ax, 20.35, float(traj[-1]), c["tag"], c["color"], fontsize=11)

    # Punto común de origen en t=0, D_0 = 1.0
    ax.axhline(1.0, color=THEMES[theme]["muted"], ls=":", lw=1.1, alpha=0.5, zorder=1)
    ax.plot(0, 1.0, "o", ms=9, color=accent(theme), zorder=6)
    label(ax, 0.65, 1.04, "D₀ = 1.0", accent(theme), theme, fontsize=11, pad=1.4)

    ax.set_xlim(-0.3, 27.2)
    ax.set_ylim(-0.05, 1.15)
    pure_axes(ax, [0, 5, 10, 15, 20], ["0", "5", "10", "15", "20"],
              [0, 0.5, 1.0], ["0", "0.5", "1.0"],
              xlabel="Períodos (t)", ylabel="Ponderación (βᵗ)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/factor-descuento", theme=th, outdir=OUTDIR_MD)
