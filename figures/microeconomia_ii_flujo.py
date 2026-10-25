"""Flujo circular incrustado en la biosfera: hogares, empresas, gobierno + recursos/contaminacion."""
import sys
sys.path.insert(0, "figures")
import matplotlib.patches as mp
from style import setup_eco, save, OUTDIR_MD, THEMES, halo, label, flow, TINTS


def draw(theme):
    fig, ax = setup_eco(theme, figsize=(7.6, 4.6))
    t = THEMES[theme]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.8)
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    # marco biosfera
    ax.add_patch(mp.FancyBboxPatch((0.2, 0.3), 9.6, 9.2, boxstyle="round,pad=0.25",
                 facecolor="none", edgecolor="#65a30d", lw=2.2, zorder=2))
    label(ax, 5.0, 10.3, "Biosfera y entorno físico", "#65a30d", theme, ha="center", fontsize=12)
    label(ax, 5.0, 9.75, "Energía · Minerales · Aire · Agua · Plantas · Animales · Tierra · Suelo",
          t["muted"], theme, ha="center", fontsize=8.5)
    # cajas
    boxes = {"Hogares": (1.0, 4.2), "Empresas": (6.4, 4.2), "Gobierno": (3.7, 1.0)}
    for name, (x, y) in boxes.items():
        ax.add_patch(mp.FancyBboxPatch((x, y), 2.6, 1.7, boxstyle="round,pad=0.08",
                     facecolor=TINTS[theme]["excl"], edgecolor="#0284c7", lw=1.8, zorder=3))
        ax.text(x + 1.3, y + 0.85, name, ha="center", va="center", fontsize=12,
                fontweight="bold", color=t["fg"], zorder=4)
    # flujos internos: trabajo Hogares->Empresas, bienes Empresas->Hogares,
    # impuestos Hogares/Empresas->Gobierno, servicios Gobierno->Hogares
    flow(ax, (6.4, 5.6), (3.6, 5.6), "#0284c7")          # trabajo H->E (ida)
    label(ax, 5.0, 6.0, "trabajo", "#0284c7", theme, ha="center", fontsize=9)
    flow(ax, (6.4, 4.7), (3.6, 4.7), "#d97706")          # bienes E->H (vuelta)
    label(ax, 5.0, 4.35, "bienes", "#d97706", theme, ha="center", fontsize=9)
    flow(ax, (2.3, 4.2), (3.9, 2.7), t["muted"])        # impuestos H->G
    label(ax, 2.75, 3.75, "impuestos", t["muted"], theme, ha="right", fontsize=9)
    flow(ax, (7.7, 4.2), (5.6, 2.7), t["muted"])        # impuestos E->G
    flow(ax, (3.7, 2.2), (2.4, 4.2), "#65a30d")         # servicios G->H
    label(ax, 3.85, 2.95, "leyes y servicios", "#65a30d", theme, fontsize=9)
    # entradas verdes (recursos) aterrizan en las cajas desde arriba
    flow(ax, (1.6, 5.95), (1.6, 8.6), "#65a30d")
    label(ax, 1.75, 7.3, "recursos", "#65a30d", theme, fontsize=9)
    flow(ax, (8.4, 5.95), (8.4, 8.6), "#65a30d")
    # salidas rojas (contaminacion) abandonan las cajas hacia abajo
    flow(ax, (8.9, 1.2), (8.9, 4.2), "#b91c1c")
    label(ax, 9.05, 2.9, "contaminación", "#b91c1c", theme, fontsize=9)
    flow(ax, (1.0, 1.2), (1.0, 4.2), "#b91c1c")
    return fig


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "both"
    for th in (["light", "dark"] if which == "both" else [which]):
        save(draw(th), "micro2/flujo-biosfera", theme=th, outdir=OUTDIR_MD)
