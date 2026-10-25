"""Produccion concava: q=f(x), conjunto Y, tangentes PMg y holgura del promedio."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, end_label, TINTS
from style import gap_caps, smart_label


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.2, 4.4))
    t = THEMES[theme]
    # f(x) = 6*sqrt(x): concava, PMg decreciente
    f = lambda x: 6.0 * np.sqrt(x)
    fp = lambda x: 3.0 / np.sqrt(x)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 20)
    xs = np.linspace(0.05, 10, 300)
    ax.plot(xs, f(xs), color="#0284c7", lw=2.6, zorder=4)
    end_label(ax, 10.1, f(10) + 0.4, "q = f(x)", "#0284c7")
    ax.fill_between(xs, 0, f(xs), facecolor=TINTS[theme]["excl"],
                    edgecolor="none", zorder=1)
    label(ax, 7.6, 4.5, "Y", "#0284c7", theme, fontsize=13)
    # planes eficientes A=(1,6), B=(9,18); PMg(A)=3 > PMg(B)=1
    A = (1.0, f(1.0))
    B = (9.0, f(9.0))
    for (px, py), nm, pmg in [(A, "A", fp(1.0)), (B, "B", fp(9.0))]:
        ax.plot(px, py, "o", ms=9, color="#d97706", zorder=5)
        # tangente corta centrada en el punto (PMg calculada)
        dx = 1.1
        ax.plot([px - dx, px + dx], [py - pmg * dx, py + pmg * dx],
                color="#d97706", lw=1.4, linestyle="--", zorder=3)
    label(ax, 0.35, 5.35, "A PMg=3", "#d97706", theme, ha="right")
    smart_label(ax, 9.0, 18.0, "B PMg=1", "#d97706", theme, r=0.9)
    # cuerda secante A-B y holgura en el insumo promedio
    lam = 0.5
    xm = lam * A[0] + (1 - lam) * B[0]  # 5.0
    y_cuerda = lam * A[1] + (1 - lam) * B[1]  # 12.0
    y_fun = f(xm)  # ~13.42
    ax.plot([A[0], B[0]], [A[1], B[1]], color="#65a30d", lw=1.8, zorder=3)
    gap_caps(ax, xm, y_cuerda, y_fun, "#65a30d", cap=0.25)
    ax.plot(xm, y_fun, "o", ms=8, color="#65a30d", zorder=5)
    label(ax, 5.7, 12.35, "holgura", "#65a30d", theme)
    ax.set_xlim(0, 11.5)
    ax.set_xticks([1, 5, 9])
    ax.set_xticklabels(["x", "xm", "x'"])
    ax.set_yticks([])
    ax.set_xlabel("insumo x", fontsize=11.5, fontweight="bold")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/produccion-concava", theme=th, outdir=OUTDIR_MD)
