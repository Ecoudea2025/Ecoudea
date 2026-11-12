"""Ricardiana: rebaja tributaria con deuda; R ahorran, NR consumen. Clase 17."""
import sys
sys.path.insert(0, "figures")
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label


def draw(theme):
    fig, ax = setup_eco(theme)
    t = THEMES[theme]
    cats = ["Ricardianos\n(1 - phi)", "No ricardianos\n(phi)"]
    vals = [0.0, 1.0]
    colors = [ROLES["budget"], ROLES["c2"]]
    x = [0, 1]
    ax.bar(x, vals, width=0.55, color=colors, edgecolor=t["fg"],
           linewidth=1.2, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=11, fontweight="bold")
    ax.set_xlim(-0.7, 1.7)
    ax.set_ylim(0, 1.45)
    ax.set_ylabel("Respuesta del consumo a -T con +B", fontsize=11,
                  fontweight="bold")
    label(ax, 0, 0.12, "ΔC(R) = 0\n(ahorran todo)", t["fg"], theme,
          ha="center", fontsize=10)
    label(ax, 1, 1.1, "ΔC(NR) > 0\n(gastan alivio)", colors[1], theme,
          ha="center", fontsize=10)
    label(ax, 1.55, 1.3, "a mayor phi,\nmayor efecto", t["muted"], theme,
          fontsize=9)
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/ricardiana", theme=th, outdir=OUTDIR_MD)
