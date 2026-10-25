"""FPU concava con igualitario A, utilitarista B y tangencia E con isobienestar W2."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, pure_axes, TINTS


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.6))
    t = THEMES[theme]
    ax.set_xlim(0, 11.0)
    ax.set_ylim(0, 11.0)
    f = lambda s: 10.0 - s ** 2 / 10.0
    xs = np.linspace(0, 10, 300)
    ax.plot(xs, f(xs), color="#0284c7", lw=2.6, zorder=4)
    end_label(ax, 10.02, f(9.9) + 0.3, "FPU", "#0284c7")
    # A igualitario: US=UJ sobre la frontera: US^2+10US-100=0
    UA = (-10 + np.sqrt(500)) / 2  # 6.18
    ax.plot([0, UA], [0, UA], color=t["muted"], lw=1.2, linestyle="--", zorder=2)
    label(ax, UA + 0.4, UA + 0.9, "45°", t["muted"], theme, fontsize=10)
    ax.plot(UA, UA, "o", ms=10, color="#d97706", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    label(ax, UA - 0.35, UA + 0.15, "A", "#d97706", theme, ha="right", fontsize=13)
    # B utilitarista: max US+UJ -> US=5
    ax.plot(5, 7.5, "o", ms=10, color="#d97706", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    label(ax, 5.0, 8.15, "B", "#d97706", theme, ha="center", fontsize=13)
    # E tangencia con W2: E=(7, 5.1); circulo centro en la normal, r=3
    E = np.array([7.0, f(7.0)])
    n = np.array([1.4, 1.0]) / np.sqrt(1.4 ** 2 + 1)
    C = E + 3.0 * n
    ang0 = np.degrees(np.arctan2(E[1] - C[1], E[0] - C[0]))
    angs = np.radians(np.linspace(ang0 - 28, ang0 + 28, 80))
    ax.plot(C[0] + 3.0 * np.cos(angs), C[1] + 3.0 * np.sin(angs),
            color="#65a30d", lw=2.0, zorder=3)
    end_label(ax, C[0] + 3.0 * np.cos(np.radians(ang0 + 28)) + 0.15,
              C[1] + 3.0 * np.sin(np.radians(ang0 + 28)), "W2", "#65a30d")
    ax.plot(E[0], E[1], "o", ms=10, color="#65a30d", zorder=6,
            markeredgecolor=t["fg"], markeredgewidth=1.2)
    label(ax, E[0] + 0.3, E[1] - 0.35, "E", "#65a30d", theme, fontsize=13)
    # D interior peor que E; F interior peor que E pero mejor que D
    ax.plot(4.0, 3.0, "s", ms=8, color=t["muted"], zorder=5)
    label(ax, 4.0, 2.45, "D", t["muted"], theme, ha="center", fontsize=11)
    ax.plot(7.5, 2.5, "s", ms=8, color=t["muted"], zorder=5)
    label(ax, 7.5, 1.95, "F", t["muted"], theme, ha="center", fontsize=11)
    pure_axes(ax, [0, 10], ["0", "10"], [0, 10], ["0", "10"],
              xlabel="Utilidad de Santiago US", ylabel="Utilidad de Juan UJ")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/fpu-optimo", theme=th, outdir=OUTDIR_MD)
