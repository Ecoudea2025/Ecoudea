"""Deposito reembolsable: CMg_ret vs Dano marginal. Practica 03."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label, TINTS


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    Q = 10.0
    qr = np.linspace(0, Q, 400)
    cmg = 0.8 * qr
    dmg = 0.6 * (Q - qr)
    ax.plot(qr, cmg, color=ROLES["c1"], lw=2.8)
    end_label(ax, Q, cmg[-1] + 0.15, "CMg_ret", ROLES["c1"])
    ax.plot(qr, dmg, color=ROLES["alt"], lw=2.8)
    end_label(ax, 0.0, dmg[0] + 0.2, "DMg", ROLES["alt"])
    qstar = 6.0 / 1.4
    d = 0.8 * qstar
    ax.plot([0, qstar], [d, d], color=t["fg"], lw=1.8,
            linestyle=(0, (5, 4)))
    label(ax, Q + 0.15, d, "d", t["fg"], theme, fontsize=12)
    ax.plot(qstar, d, "o", ms=10, color="#3f6212" if theme == "light"
            else "#84cc16", zorder=5)
    ax.plot([qstar, qstar], [0, d], linestyle=":", color=t["muted"],
            lw=1.2)
    label(ax, qstar, 0.25, "qr*", t["fg"], theme, ha="center",
          fontsize=11)
    xs = np.linspace(0, qstar, 60)
    ax.fill_between(xs, 0.8 * xs, 0.6 * (Q - xs),
                    facecolor=TINTS[theme]["save"], edgecolor="none",
                    zorder=1)
    ax.set_xlim(0, 11.6)
    ax.set_ylim(0, 7.2)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="qr",
              ylabel="$/unidad")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/deposito-reembolsable", theme=th,
             outdir=OUTDIR_MD)
