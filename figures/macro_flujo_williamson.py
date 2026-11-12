"""Flujo circular del modelo intertemporal real (economia cerrada). Clase 18."""
import sys
sys.path.insert(0, "figures")
from matplotlib.patches import Rectangle, FancyBboxPatch
from style import setup_eco, save, ROLES, THEMES, OUTDIR_MD, label


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.6))
    t = THEMES[theme]
    ink = t["fg"]
    muted = t["muted"]
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 6.2)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "bottom", "left", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(False)
    # marco economia cerrada
    ax.add_patch(Rectangle((0.4, 0.3), 8.6, 5.2, fill=False,
                           edgecolor=muted, lw=1.4, linestyle=(0, (5, 4))))
    label(ax, 0.6, 5.7, "Economia cerrada", muted, theme, fontsize=10)
    label(ax, 9.3, 3.0, "Resto del\nmundo", muted, theme, fontsize=9)
    boxes = {
        "Familias": (1.0, 4.0, 2.2, 0.9),
        "Firmas": (6.2, 4.0, 2.2, 0.9),
        "Mercado": (3.6, 2.3, 2.2, 0.9),
        "Gobierno": (3.6, 0.7, 2.2, 0.9),
    }
    colors = {"Familias": ROLES["c2"], "Firmas": ROLES["c1"],
              "Mercado": ROLES["budget"], "Gobierno": ROLES["alt"]}
    for name, (x, y, w, h) in boxes.items():
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03",
                                    facecolor="none", edgecolor=colors[name], lw=2.2))
        label(ax, x + w / 2, y + h / 2, name, colors[name], theme,
              ha="center", fontsize=12)
    fam_c = (2.1, 4.0)
    fir_c = (7.3, 4.45)
    # Familias -> Firmas (arriba): N^s, S
    ax.annotate("", xy=(6.2, 4.75), xytext=(3.2, 4.75),
                arrowprops=dict(arrowstyle="->", color=ink, lw=1.8))
    label(ax, 4.7, 5.02, "N(s), S", ink, theme, fontsize=10)
    # Firmas -> Familias (abajo): w, C
    ax.annotate("", xy=(3.2, 4.15), xytext=(6.2, 4.15),
                arrowprops=dict(arrowstyle="->", color=ink, lw=1.8))
    label(ax, 4.7, 3.88, "w, C", ink, theme, fontsize=10)
    # Familias -> Mercado
    ax.annotate("", xy=(4.2, 2.75), xytext=(2.6, 4.0),
                arrowprops=dict(arrowstyle="->", color=muted, lw=1.6))
    label(ax, 2.75, 3.35, "C, N(s)", muted, theme, fontsize=9)
    # Firmas -> Mercado
    ax.annotate("", xy=(5.2, 2.75), xytext=(6.8, 4.0),
                arrowprops=dict(arrowstyle="->", color=muted, lw=1.6))
    label(ax, 6.35, 3.35, "Y, I, N(d)", muted, theme, fontsize=9)
    # Familias -> Gobierno (T)
    ax.annotate("", xy=(3.6, 1.15), xytext=(2.1, 4.0),
                arrowprops=dict(arrowstyle="->", color=muted, lw=1.4,
                                linestyle=(0, (4, 3))))
    label(ax, 2.35, 2.4, "T", muted, theme, fontsize=10)
    # Firmas -> Gobierno (T)
    ax.annotate("", xy=(5.8, 1.15), xytext=(7.3, 4.0),
                arrowprops=dict(arrowstyle="->", color=muted, lw=1.4,
                                linestyle=(0, (4, 3))))
    # Gobierno -> Mercado (G)
    ax.annotate("", xy=(4.7, 2.3), xytext=(4.7, 1.6),
                arrowprops=dict(arrowstyle="->", color=colors["Gobierno"], lw=2.0))
    label(ax, 4.95, 1.95, "G", colors["Gobierno"], theme, fontsize=10)
    _ = fam_c, fir_c
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "macroeconomia/flujo-williamson", theme=th, outdir=OUTDIR_MD)
