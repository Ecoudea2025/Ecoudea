"""Frontera w-r: recta patron r=R(1-w) vs curva en trigo (cavada, calculo exacto).
Sistema del curso: A=[[0.35,0.1463],[1.2983,0]], l=[0.0098,0.0133].
Con numerario p_H=1: 1.2983*pT^2 + (0.0133*w-0.35)*pT - (0.1463+0.0098*w) = 0,
r = 1/(1.2983*pT + 0.0133*w) - 1. R = 44.9% (w=0)."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, pure_axes

R = 0.449


def trigo_curve(ws):
    rs, ps = [], []
    for w in ws:
        a, b, c = 1.2983, (0.0133 * w - 0.35), -(0.1463 + 0.0098 * w)
        disc = b * b - 4 * a * c
        p = (-b + np.sqrt(max(disc, 0))) / (2 * a)
        r = 1.0 / (1.2983 * p + 0.0133 * w) - 1.0
        rs.append(max(r, 0.0))
        ps.append(p)
    return np.array(rs)


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    ax.set_xlim(0, 1.12)
    ax.set_ylim(0, 0.50)
    what = 21.53  # salario maximo con p_H=1 (r=0): 1.2983*pT+0.0133*w=1
    w = np.linspace(0, 1, 200)
    w_abs = np.linspace(0, what, 250)
    rw = trigo_curve(w_abs)
    wn = w_abs / what
    ax.plot(w, R * (1 - w), color=THEMES[theme]["fg"], lw=2.2, zorder=4)
    end_label(ax, 1.0, 0.012, "patron: recta", THEMES[theme]["fg"], fontsize=10)
    ax.plot(wn, rw, color="#0284c7", lw=2.4, zorder=4)
    label(ax, 0.06, 0.46, "trigo: curva", "#0284c7", theme, fontsize=10)
    ax.plot(0.5, R * 0.5, "o", ms=8, color=THEMES[theme]["fg"], zorder=5)
    label(ax, 0.5, R * 0.5 + 0.035, "E (patron)", THEMES[theme]["fg"], theme,
          ha="center", fontsize=10)
    ax.plot(0.5, float(np.interp(0.5, wn, rw)), "s", ms=8, color="#0284c7",
            zorder=5)
    label(ax, 0.53, float(np.interp(0.5, wn, rw)) - 0.04, "E' (trigo)",
          "#0284c7", theme, fontsize=10)
    pure_axes(ax, [0, 0.5, 1.0], ["0", "1/2", "1"],
              [0, round(R / 2, 3), round(R, 3)], ["0", "R/2", "R=44,9%"],
              xlabel="salario relativo (w / w-max)", ylabel="tasa r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "clasica/frontera-alternativa", theme=th, outdir=OUTDIR_MD)
