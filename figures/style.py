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


# ── Ecoudea: roles semánticos + ayudas editoriales ─────────────────────
# Paleta del sitio (tokens.css). Los consejos de la guía del usuario
# (ejes puros, etiquetas directas, proyecciones, banda superior) viven aquí.
OUTDIR_MD = "public/assets/figures"

ROLES = {
    "c1": "#0284c7",        # consumo presente / variable principal (macro)
    "c2": "#d97706",        # consumo futuro / segunda variable (ámbar)
    "budget": "#65a30d",    # restricción presupuestaria (oliva)
    "optimum": "#84cc16",   # óptimos y tangencias en dark
    "endow": "#d97706",     # dotación inicial (ámbar)
    "alt": "#7c3aed",       # curva alternativa / comparativa
}


def setup_eco(theme="light", figsize=(7.2, 4.4)):
    """Variante editorial: banda superior libre + salidas deterministas."""
    plt.rcParams["svg.hashsalt"] = "ecoudea"
    fig, ax = setup(theme=theme, figsize=figsize)
    fig.subplots_adjust(top=0.84)
    return fig, ax


def accent(theme):
    """Acento legible por tema (oliva-tinta en papel, brillo en tinta)."""
    return "#3f6212" if theme == "light" else "#84cc16"


def pure_axes(ax, xticks, xlabels, yticks, ylabels, xlabel="", ylabel=""):
    """Ejes teóricos puros: SOLO variables del modelo, sin cuadrícula numérica."""
    ax.set_xticks(list(xticks))
    ax.set_xticklabels(list(xlabels), fontsize=12, fontweight="bold")
    ax.set_yticks(list(yticks))
    ax.set_yticklabels(list(ylabels), fontsize=12, fontweight="bold")
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11.5, fontweight="bold", labelpad=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11.5, fontweight="bold", labelpad=14)


def end_label(ax, x, y, text, color, ha="left", fontsize=12):
    """Nombre directo de la curva en su extremo (nada de leyendas flotantes)."""
    ax.text(x, y, text, fontsize=fontsize, fontweight="bold", color=color,
            ha=ha, va="center")


def project(ax, x, y, theme="light", color=None):
    """Directrices punteadas ortogonales del punto (x, y) a ambos ejes."""
    c = color or THEMES[theme]["muted"]
    ax.plot([x, x], [0, y], linestyle=":", linewidth=1.2, color=c, alpha=0.8, zorder=2)
    ax.plot([0, x], [y, y], linestyle=":", linewidth=1.2, color=c, alpha=0.8, zorder=2)
