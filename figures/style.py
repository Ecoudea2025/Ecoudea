"""Estilo común de figuras Ecoudea (editorial, coherente con los tokens).

Uso:
    from style import setup, PALETTE, save
    fig, ax = setup(theme="light")
    ... dibujar ...
    save(fig, "microeconomia/oferta-demanda", theme="light")
"""
import matplotlib
matplotlib.use("SVG")
import matplotlib.pyplot as plt

PALETTE = {
    "micro": "#d97706",
    "macro": "#0284c7",
    "econometria": "#7c3aed",
    "estadistica": "#65a30d",
    "matematicas": "#e11d48",
    "historia": "#0e7774",
    "ink_light": "#1d241a",
    "muted_light": "#5c6656",
    "ink_dark": "#e8f0e8",
    "muted_dark": "#94a3a8",
}

THEMES = {
    "light": {"fg": PALETTE["ink_light"], "muted": PALETTE["muted_light"], "grid": "#e2dccb"},
    "dark": {"fg": PALETTE["ink_dark"], "muted": PALETTE["muted_dark"], "grid": "#2a3a2a"},
}


def setup(theme="light", figsize=(6.4, 4.2)):
    t = THEMES[theme]
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Inter", "DejaVu Sans"],
        "font.size": 11,
        "axes.edgecolor": t["muted"],
        "axes.labelcolor": t["fg"],
        "text.color": t["fg"],
        "xtick.color": t["muted"],
        "ytick.color": t["muted"],
        "grid.color": t["grid"],
        "grid.alpha": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 1.1,
    })
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_alpha(0.0)
    ax.set_facecolor("none")
    ax.grid(True, linestyle="--", linewidth=0.7)
    return fig, ax


def save(fig, name, theme="light", outdir="src/assets/figures"):
    import os
    path = os.path.join(outdir, f"{name}-{theme}.svg")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    print("figura:", path)
