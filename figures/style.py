"""Estilo común de figuras Ecoudea (editorial, coherente con los tokens).

Uso:
    from style import setup_eco, save, label, shade, span, flow
    fig, ax = setup_eco(theme="light")
    ... dibujar ...
    label(ax, 4.3, 4.8, "W", ROLES["endow"], theme)  # siempre con halo
    save(fig, "macroeconomia/alza-r", theme="light")

REGLAS ANTI-SOLAPAMIENTO (obligatorias en figuras nuevas):
  1. Toda etiqueta que quede a <0.4 unidades de una línea/curva usa halo()
     (fondo del tema): ver label(). Sin excepciones.
  2. Desplazar etiquetas en PERPENDICULAR a la curva y verificar con la
     geometría calculada (evaluar la función en el punto), nunca a ojo.
  3. Prohibido duplicar: si la curva ya lleva su nombre en el extremo
     (end_label), el eje queda sin esa etiqueta (ylabel="").
  4. Rellenos SIEMPRE con tintas sólidas premezcladas (TINTS + shade()/span()):
     el alpha en fills se ve opaco en algunos visores e imprime mal.
     El alpha solo está permitido en strokes (líneas tenues/punteadas).
  5. Curvas de la misma familia si no deben cruzarse (cruzar indiferencias
     es un error teórico, no estético). Para separar dos curvas cercanas,
     mover el punto de anclaje (p. ej. la dotación a la izquierda del
     óptimo), no forzar la forma.
  6. Puntos de tangencia CALCULADOS (intersección + igualdad de pendientes),
     nunca a ojo. Dejar la cuenta en un comentario.
  7. xlim/ylim con aire a la derecha/arriba para end labels (nada cortado).
  8. Cada SVG se inspecciona en AMBOS temas antes de reemplazar el
     placeholder (ver figuras con viewSVGFile o en página construida).

REGLAS DE FLECHAS:
  A. Rectas por defecto (flow()): mismo lenguaje en toda la figura; las
     curvas (connectionstyle arc) solo con propósito narrativo explícito.
  B. Toda flecha LLEGA a un elemento (punto, curva, eje): prohibido morir
     en el aire o flotar sin anclaje.
  C. Si un flujo viaja y DOBLA (carril + conector), el carril va SIN punta
     y la dirección la da el conector final. Una sola cabeza por historia.
  D. La etiqueta de una flecha va FUERA del trazo, del lado con más aire,
     con halo si hay otra línea a <0.4.
  E. Anotaciones de régimen ("q=0", "ρ>1") junto a SU zona, nunca cruzando
     la curva que describen.
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


# ── Ecoudea: anti-solapamiento + flechas (aditivo, nada existente cambia) ──
# Fondos opacos por tema: el halo hace legible la etiqueta sobre cualquier
# línea sin importar el tema activo.
BG = {"light": "#faf8f1", "dark": "#0a0f1a"}


def halo(theme, pad=1.6, alpha=0.9):
    """Fondo para etiquetas cercanas a líneas (regla 1)."""
    return dict(facecolor=BG[theme], edgecolor="none", pad=pad, alpha=alpha)


def label(ax, x, y, text, color, theme, ha="left", va="center", fontsize=12,
          bold=True, italic=False, pad=1.6):
    """Texto SIEMPRE con halo (regla 1). Para end labels sin nada detrás,
    pasar pad=0... mejor: usar end_label() en extremos libres."""
    ax.text(x, y, text, fontsize=fontsize,
            fontweight="bold" if bold else "normal",
            fontstyle="italic" if italic else "normal",
            color=color, ha=ha, va=va,
            bbox=halo(theme, pad=pad))


# Tintas sólidas premezcladas con el fondo del tema (regla 4): el alpha en
# fills se renderiza opaco en algunos visores. Roles: save (ahorro/verde),
# debt (deuda/ámbar), loss (pérdida/rojo), excl (exclusión/azul).
TINTS = {
    "light": {
        "save": "#E2EACD",
        "debt": "#F5E3CB",
        "loss": "#F6D5D6",
        "excl": "#DCEAEC",
    },
    "dark": {
        "save": "#192718",
        "debt": "#2B2017",
        "loss": "#2C1121",
        "excl": "#091D2F",
    },
}


def shade(ax, x, y1, y2, theme, role, where=None):
    """Relleno sólido entre curvas (regla 4). `role` en TINTS."""
    kw = dict(facecolor=TINTS[theme][role], edgecolor="none", zorder=1)
    if where is None:
        ax.fill_between(x, y1, y2, **kw)
    else:
        ax.fill_between(x, y1, y2, where=where, **kw)


def span(ax, xmin, xmax, theme, role):
    """Franja vertical sólida (regla 4). `role` en TINTS."""
    ax.axvspan(xmin, xmax, facecolor=TINTS[theme][role], edgecolor="none",
               zorder=1)


def flow(ax, xy, xytext, color, lw=2.0, dashed=False, head=True):
    """Flecha RECTA (regla A). `head=False` para carriles que doblan: la
    dirección la da el conector final (regla C)."""
    style = dict(arrowstyle="->" if head else "-", color=color, lw=lw)
    if dashed:
        style["linestyle"] = (0, (4, 3))
    ax.annotate("", xy=xy, xytext=xytext, arrowprops=style)
