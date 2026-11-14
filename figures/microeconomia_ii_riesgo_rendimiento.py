"""Riesgo y rendimiento: recta presupuestaria y tangencia. Clase 14."""
import sys
sys.path.insert(0, "figures")
import numpy as np
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label, end_label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    rf, sm, rm = 2.0, 10.0, 8.0
    p = (rm - rf) / sm
    S = np.linspace(0, 13, 300)
    ax.plot(S, rf + p * S, color=ROLES["c1"], lw=2.8)
    end_label(ax, 13.0, rf + p * 13 + 0.25, "recta", ROLES["c1"])
    sig, mu = 7.5, rf + p * 7.5
    ax.plot([sm], [rm], "s", ms=8, color=ROLES["c2"], zorder=5)
    label(ax, sm + 0.6, rm + 0.5, "m", ROLES["c2"], theme, fontsize=12)
    U0 = mu - 0.5 * 0.08 * sig ** 2
    ax.plot(S, U0 + 0.04 * S ** 2, color=ROLES["budget"], lw=2.2)
    ax.plot(S, (U0 + 1.75) + 0.04 * S ** 2, color=ROLES["budget"], lw=1.4,
            linestyle=(0, (4, 3)))
    ax.plot(sig, mu, "o", ms=10, color=ROLES["budget"], zorder=5)
    ax.plot([sig, sig], [0, mu], linestyle=":", color=t["muted"], lw=1.2)
    ax.plot([0, sig], [mu, mu], linestyle=":", color=t["muted"], lw=1.2)
    label(ax, sig + 0.25, 0.35, "sig*", ROLES["budget"], theme, fontsize=11)
    label(ax, 0.15, mu + 0.45, "r*", ROLES["budget"], theme, fontsize=11)
    label(ax, 0.55, rf - 0.05, "rf", t["fg"], theme, fontsize=12)
    ax.set_xlim(0, 15.2)
    ax.set_ylim(0, 11.5)
    from style import pure_axes
    pure_axes(ax, [0], ["0"], [0], ["0"], xlabel="sigma", ylabel="r")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/riesgo-rendimiento", theme=th, outdir=OUTDIR_MD)
