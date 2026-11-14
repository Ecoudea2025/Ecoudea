"""Mercado bilateral: respuestas cruzadas y equilibrios. Clase 16."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label, flow


def R(n):
    return 95.0 / (1.0 + np.exp(-(n - 40.0) / 8.0))


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 5.0))
    t = THEMES[theme]
    g = np.linspace(0, 110, 500)
    ax.plot(g, R(g), color=ROLES["c1"], lw=2.8)
    end_label(ax, 112, R(110) + 6, "n1=R1(n2)", ROLES["c1"], ha="left")
    ax.plot(R(g), g, color=ROLES["c2"], lw=2.8)
    end_label(ax, 88, 68, "n2=R2(n1)", ROLES["c2"], ha="right")
    # intersecciones numericas (biseccion sobre la diferencia)
    diff = R(g) - g
    roots = []
    for i in range(len(g) - 1):
        if diff[i] == 0:
            roots.append(g[i])
        elif diff[i] * diff[i + 1] < 0:
            a, b = g[i], g[i + 1]
            for _ in range(40):
                m = 0.5 * (a + b)
                if (R(a) - a) * (R(m) - m) <= 0:
                    b = m
                else:
                    a = m
            roots.append(0.5 * (a + b))
    for r in roots:
        ax.plot(r, R(r), "o", ms=10, color="#3f6212" if theme == "light"
                else "#84cc16", zorder=5)
    # campo de ajuste: hacia (0,0) abajo del umbral, hacia alto arriba
    flow(ax, (15, 8), (6, 3), t["muted"])
    flow(ax, (8, 15), (3, 6), t["muted"])
    flow(ax, (70, 60), (85, 80), ROLES["budget"])
    flow(ax, (60, 70), (80, 85), ROLES["budget"])
    label(ax, 30, 12, "colapso", t["muted"], theme, ha="center",
          fontsize=10)
    label(ax, 100, 50, "adopcion", ROLES["budget"], theme, ha="center",
          fontsize=10)
    ax.set_xlim(0, 142)
    ax.set_ylim(0, 118)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="n1", ylabel="n2")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/bilateral", theme=th, outdir=OUTDIR_MD)
