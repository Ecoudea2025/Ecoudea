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


def end_label(ax, x, y, text, color, ha=None, fontsize=12):
    """Nombre directo de la curva en su extremo (nada de leyendas flotantes).
    Sin ha: elige solo el lado con mas aire dentro del xlim."""
    if ha is None:
        lo, hi = ax.get_xlim()
        ha = "right" if (hi - x) < (x - lo) else "left"
    t = ax.text(x, y, text, fontsize=fontsize, fontweight="bold", color=color,
            ha=ha, va="center")
    t.set_gid('end-label')  # el gate de solapamientos no le exige aire al trazo
    return t


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


def _text_hits(ax, tx, renderer, dots, strokes, skip_self=True):
    """True si el texto toca otro texto, un marcador o un trazo."""
    import numpy as np
    PAD = 2.0  # igual que el gate: cajas de glifo +2px
    bb = tx.get_window_extent(renderer=renderer)
    x0, y0, x1, y1 = bb.x0 - PAD, bb.y0 - PAD, bb.x1 + PAD, bb.y1 + PAD
    for o in ax.texts:
        if o is tx and skip_self:
            continue
        if not o.get_visible() or not (o.get_text() or '').strip():
            continue
        try:
            b2 = o.get_window_extent(renderer=renderer)
        except Exception:
            continue
        if b2.width <= 2 and b2.height <= 2:
            continue
        if x0 < b2.x1 + PAD and b2.x0 < x1 + PAD and y0 < b2.y1 + PAD and b2.y0 < y1 + PAD:
            return True
    for pts, r in dots:
        dx = np.maximum(x0 - pts[:, 0], pts[:, 0] - x1)
        dy = np.maximum(y0 - pts[:, 1], pts[:, 1] - y1)
        if bool(np.any((dx <= r * 0.5) & (dy <= r * 0.5))):
            return True
    for verts, lw in strokes:
        ex0, ey0, ex1, ey1 = x0 - lw, y0 - lw, x1 + lw, y1 + lw
        for k in range(len(verts) - 1):
            ax0, ay0 = verts[k]
            bx0, by0 = verts[k + 1]
            ok = False
            for tt in np.linspace(0.0, 1.0, 9):
                px, py = ax0 + (bx0 - ax0) * tt, ay0 + (by0 - ay0) * tt
                if ex0 <= px <= ex1 and ey0 <= py <= ey1:
                    ok = True
                    break
            if ok:
                return True
    return False


def _collect_geometry(ax, fig):
    """Puntos (coords display, radio) y trazos (vertices, semigrosor) del axes."""
    import numpy as np
    from matplotlib.lines import Line2D
    grids = set(map(id, ax.get_xgridlines() + ax.get_ygridlines()))
    dots, strokes = [], []
    for ln in ax.lines:
        if not ln.get_visible() or id(ln) in grids:
            continue
        try:
            pts = np.asarray(ln.get_transform().transform(ln.get_xydata()))
        except Exception:
            continue
        if len(pts) == 0:
            continue
        ls = ln.get_linestyle()
        if ls in ('None', ' ', ''):
            r = float(ln.get_markersize()) * fig.dpi / 120.0
            dots.append((pts.reshape(-1, 2), r))
        else:
            lw = float(ln.get_linewidth()) * fig.dpi / 72.0 / 2.0 + 1.0
            step = max(1, len(pts) // 300)
            dots_v = pts[::step]
            strokes.append((dots_v, lw))
    return dots, strokes


def smart_label(ax, x, y, text, color, theme, r=0.35, order=None,
                fontsize=12, bold=True, va="center", pad=1.6):
    """Etiqueta que se auto-ubica: prueba posiciones compass alrededor del
    ancla (radio r en unidades de datos) y usa la primera sin choques
    (texto/texto, texto/punto, texto/trazo). Si ninguna sirve, usa la
    primera y avisa en consola (el gate lo reportara como aviso/error)."""
    import numpy as np
    if order is None:
        order = [("right", 1, 0, "left"), ("top", 0, 1, "center"),
                 ("topleft", -0.7, 0.7, "right"),
                 ("topright", 0.7, 0.7, "left"),
                 ("left", -1, 0, "right"),
                 ("bottomright", 0.7, -0.7, "left"),
                 ("bottom", 0, -1, "center"),
                 ("bottomleft", -0.7, -0.7, "right")]
    fig = ax.figure
    try:
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        fig.set_canvas(FigureCanvasAgg(fig))
    except Exception:
        pass
    dots, strokes = _collect_geometry(ax, fig)
    best, best_name = None, None
    for name, dxn, dyn, ha in order:
        tx = ax.text(x + dxn * r, y + dyn * r, text, fontsize=fontsize,
                     fontweight="bold" if bold else "normal",
                     color=color, ha=ha, va=va, bbox=halo(theme, pad=pad))
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        try:
            hit = _text_hits(ax, tx, renderer, dots, strokes)
        except Exception:
            hit = True
        if not hit:
            return tx
        tx.remove()
        if best is None:
            best, best_name = (x + dxn * r, y + dyn * r, ha), name
    # sin posicion limpia: primera opcion + aviso (el gate decide)
    import sys
    print(f"[style] smart_label sin hueco limpio para '{text}' "
          f"(uso {best_name})", file=sys.stderr)
    tx = ax.text(best[0], best[1], text, fontsize=fontsize,
                 fontweight="bold" if bold else "normal",
                 color=color, ha=best[2], va=va, bbox=halo(theme, pad=pad))
    return tx


def fit_margins(ax, pad=0.06):
    """Expande xlim/ylim para que ninguna etiqueta toque el borde (con pad
    fraccional del rango). Llamar ANTES de smart_label (mueve los limites y
    puede invalidar colocaciones ya verificadas); el gate verifica al final.
    Si los limites ya estan ajustados a mano, no hace falta llamarla."""
    import numpy as np
    fig = ax.figure
    try:
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        fig.set_canvas(FigureCanvasAgg(fig))
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
    except Exception:
        return
    inv = ax.transData.inverted()
    x0d, x1d = ax.get_xlim()
    y0d, y1d = ax.get_ylim()
    xs = [x0d, x1d]
    ys = [y0d, y1d]
    for tx in ax.texts:
        try:
            bb = tx.get_window_extent(renderer=renderer)
        except Exception:
            continue
        if (bb.width <= 2 and bb.height <= 2) or not (tx.get_text() or '').strip():
            continue
        for cx, cy in [(bb.x0, bb.y0), (bb.x1, bb.y1)]:
            try:
                dx, dy = inv.transform((cx, cy))
            except Exception:
                continue
            xs.append(dx)
            ys.append(dy)
    xr = max(xs) - min(xs) or 1.0
    yr = max(ys) - min(ys) or 1.0
    ax.set_xlim(min(xs) - pad * xr, max(xs) + pad * xr)
    ax.set_ylim(min(ys) - pad * yr, max(ys) + pad * yr)


def gap_caps(ax, x, y1, y2, color, theme=None, cap=0.25, lw=2.2, zorder=5):
    """Segmento vertical de medicion con remates (holguras, impuestos,
    primas): se lee como medida, no como linea suelta."""
    ax.plot([x, x], [y1, y2], color=color, lw=lw, zorder=zorder)
    ax.plot([x - cap, x + cap], [y1, y1], color=color, lw=lw, zorder=zorder)
    ax.plot([x - cap, x + cap], [y2, y2], color=color, lw=lw, zorder=zorder)


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
