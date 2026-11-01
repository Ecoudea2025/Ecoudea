"""Optimización CES en tres períodos: perfil temporal del consumo (C1, C2, C3)
según la elasticidad de sustitución intertemporal σ = 1/(1-ρ) con r > 0. Clase 09."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, pure_axes, end_label, label, accent


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    r = 0.25
    W = 10.0 + 10.0 / (1 + r) + 10.0 / (1 + r) ** 2  # riqueza total en dotaciones iguales Yt=10

    periods = np.array([1.0, 2.0, 3.0])

    scenarios = [
        {"sigma": 0.2, "tag": "σ = 0.2 (suavización)", "color": ROLES["c2"], "ls": "-."},
        {"sigma": 1.0, "tag": "σ = 1.0 (Cobb-Douglas)", "color": ROLES["alt"], "ls": "--"},
        {"sigma": 2.2, "tag": "σ = 2.2 (alta sustitución)", "color": ROLES["c1"], "ls": "-"},
    ]

    for sc in scenarios:
        sig = sc["sigma"]
        denom = sum((1 + r) ** ((sig - 1) * (k - 1)) for k in [1, 2, 3])
        c1 = W / denom
        c2 = c1 * ((1 + r) ** sig)
        c3 = c1 * ((1 + r) ** (2 * sig))
        c_path = np.array([c1, c2, c3])

        # Curva de interpolación suave
        t_dense = np.linspace(1.0, 3.0, 100)
        c_dense = c1 * ((1 + r) ** (sig * (t_dense - 1)))
        ax.plot(t_dense, c_dense, color=sc["color"], lw=2.5, ls=sc["ls"])

        # Puntos discretos en cada período
        ax.plot(periods, c_path, "o", ms=7, color=sc["color"], zorder=5)

        # Etiqueta al extremo a la derecha del marcador
        end_label(ax, 3.12, float(c3), sc["tag"], sc["color"], ha="left", fontsize=10.5)

    # Nivel de dotación plana Y = 10 de referencia
    ax.axhline(10.0, color=t["muted"], ls=":", lw=1.2, alpha=0.6, zorder=1)
    label(ax, 1.05, 10.65, "Dotación Yₜ = 10", t["muted"], theme, fontsize=10, pad=1.2)

    ax.set_xlim(0.8, 4.35)
    ax.set_ylim(4.5, 18.0)
    pure_axes(ax, [1, 2, 3], ["t = 1", "t = 2", "t = 3"],
              [6, 10, 14], ["6", "10", "14"],
              xlabel="Períodos de vida", ylabel="Consumo óptimo (Cₜ*)")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/ces-tres-periodos", theme=th, outdir=OUTDIR_MD)
