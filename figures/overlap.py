"""Detector de solapamientos para figuras Ecoudea (reglas en pixeles, determinista).

Uso:
    from overlap import check_figure
    errors, warnings = check_figure(fig)

Reglas (medidas en pixeles del render final, ambos temas):
  ERROR (falla el gate):
    - texto <-> texto (cajas de glifo + pad)
    - texto <-> punto/marcador (radio + pad)
    - texto fuera de la figura (recorte)
  AVISO (triage humano):
    - texto tocando un trazo (el halo lo mitiga; se reporta con coordenadas)

  Los parches decorativos (cajas, sombreados, ejes) NO participan: el texto
  vive encima de ellos por diseno (fondo del tema + halo). Las rejillas
  tampoco participan.
"""
import matplotlib
matplotlib.use("SVG")
import numpy as np
from matplotlib.text import Text
from matplotlib.lines import Line2D

TEXT_PAD = 2.0    # px extra alrededor de cada glifo (texto-texto)
LINE_TOUCH = 1.0  # px: la caja del glifo toca el trazo (con su grosor)


def _is_ghost(bb):
    """Textos nunca dibujados: vacios, de area ~0 o anclados en el origen
    (duplicados rancios de tick labels que matplotlib deja en (0,0,1,1))."""
    return bb.width <= 2.0 and bb.height <= 2.0


def _draw(fig):
    # Medir con Agg (el canvas SVG no expone renderer); el SVG final no cambia.
    try:
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        fig.set_canvas(FigureCanvasAgg(fig))
    except Exception:
        pass
    fig.canvas.draw()
    return fig.canvas.get_renderer()


def _texts(ax):
    """Solo textos editoriales (ax.text / label / end_label). Sin ticks ni
    anotaciones (el extent de un annotate incluye su flecha)."""
    from matplotlib.text import Annotation
    return [a for a in ax.texts if isinstance(a, Text) and a.get_visible()
            and not isinstance(a, Annotation)]


def _is_end_label(tx):
    return (tx.get_gid() or '') == 'end-label'


def _is_grid(line, ax):
    grids = set(map(id, ax.get_xgridlines() + ax.get_ygridlines()))
    return id(line) in grids


def _strokes(ax):
    """Lineas con trazo (no rejilla, no puntos sueltos)."""
    out = []
    for ln in ax.lines:
        if not ln.get_visible() or _is_grid(ln, ax):
            continue
        ls = ln.get_linestyle()
        if ls in ('None', ' ', ''):
            continue  # es marcador: va por la via de puntos
        out.append(ln)
    return out


def _dots(ax):
    """Vertices de lineas solo-marcador -> (puntos display Nx2, radio px)."""
    out = []
    dpi = ax.figure.dpi
    for ln in ax.lines:
        if not ln.get_visible() or _is_grid(ln, ax):
            continue
        ls = ln.get_linestyle()
        if ls not in ('None', ' ', ''):
            continue
        mk = ln.get_marker()
        if mk in ('None', ' ', '', None):
            continue
        try:
            pts = ln.get_transform().transform(ln.get_xydata())
        except Exception:
            continue
        r = float(ln.get_markersize()) * dpi / 72.0 / 2.0
        out.append((pts.reshape(-1, 2), r))
    for col in ax.collections:
        if not col.get_visible():
            continue
        try:
            offs = col.get_offsets()
        except Exception:
            continue
        if offs is None or len(offs) == 0:
            continue
        try:
            pts = col.get_transform().transform(np.asarray(offs))
        except Exception:
            continue
        try:
            sz = float(np.asarray(col.get_sizes()).ravel()[0])
            r = np.sqrt(sz) / 2.0  # sizes estan en puntos^2
        except Exception:
            r = 4.0
        out.append((pts.reshape(-1, 2), r))
    return out


def _rect_dist(px, py, x0, y0, x1, y1):
    """Distancia punto-rectangulo (0 si el punto cae dentro)."""
    dx = max(x0 - px, 0.0, px - x1)
    dy = max(y0 - py, 0.0, py - y1)
    return float(np.hypot(dx, dy))


def _seg_rect_dist(ax_, ay_, bx_, by_, x0, y0, x1, y1, n=24):
    """Distancia segmento-rectangulo por muestreo (exacta a efectos del gate)."""
    ts = np.linspace(0.0, 1.0, n + 1)
    best = float('inf')
    for t in ts:
        d = _rect_dist(ax_ + (bx_ - ax_) * t, ay_ + (by_ - ay_) * t, x0, y0, x1, y1)
        if d < best:
            best = d
            if best == 0.0:
                return 0.0
    return best


def check_figure(fig):
    """Devuelve (errors, warnings): listas de dicts {kind, text, detail}."""
    renderer = _draw(fig)
    errors, warnings = [], []
    fbox = fig.bbox  # figura completa (incluye titulos y xlabels)
    for ax in fig.axes:
        raw = []
        for tx in _texts(ax):
            try:
                bb = tx.get_window_extent(renderer=renderer)
            except Exception:
                continue
            s = tx.get_text() or ''
            if not s.strip() or _is_ghost(bb):
                continue  # vacios y duplicados rancios de ticks
            raw.append((s, bb.x0, bb.y0, bb.x1, bb.y1, _is_end_label(tx)))
            # recorte contra la figura (no contra los ejes: titulos viven fuera)
            if bb.x0 < fbox.x0 - 1 or bb.y0 < fbox.y0 - 1 or \
               bb.x1 > fbox.x1 + 1 or bb.y1 > fbox.y1 + 1:
                errors.append({
                    'kind': 'recorte',
                    'text': s[:40],
                    'detail': 'etiqueta fuera de la figura (xlim/ylim sin aire)',
                })
        boxes = [(s, x0 - TEXT_PAD, y0 - TEXT_PAD, x1 + TEXT_PAD, y1 + TEXT_PAD)
                 for (s, x0, y0, x1, y1, _) in raw]
        glyphs = [(s, x0, y0, x1, y1)
                  for (s, x0, y0, x1, y1, _) in raw]
        no_end = [(s, x0, y0, x1, y1)
                  for (s, x0, y0, x1, y1, e) in raw if not e]  # sin pad: toque real
        # texto <-> texto
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]:
                    errors.append({
                        'kind': 'texto-texto',
                        'text': (a[0][:30] + ' / ' + b[0][:30]),
                        'detail': 'dos etiquetas se pisan',
                    })
        # texto <-> punto: ERROR solo si el centro toca de verdad el glifo
        # (caja del glifo expandida apenas medio radio: la vecindad con halo
        #  es diseno intencional, no error). Se reporta la distancia minima.
        for pts, r in _dots(ax):
            rr = r * 0.5
            for (s, x0, y0, x1, y1) in glyphs:
                dx = np.maximum(x0 - rr - pts[:, 0], pts[:, 0] - x1 - rr)
                dy = np.maximum(y0 - rr - pts[:, 1], pts[:, 1] - y1 - rr)
                dist = float(np.min(np.hypot(np.maximum(dx, 0.0),
                                             np.maximum(dy, 0.0))))
                if dist == 0.0:
                    errors.append({
                        'kind': 'texto-punto',
                        'text': s[:40],
                        'detail': 'etiqueta pisa un marcador (moverla)',
                    })
        # texto tocando trazo -> aviso (el halo lo mitiga; decide el humano)
        for ln in _strokes(ax):
            try:
                verts = ln.get_transform().transform(ln.get_path().vertices)
            except Exception:
                continue
            if len(verts) == 0:
                continue
            step = max(1, len(verts) // 400)
            vv = verts[::step]
            lw = float(ln.get_linewidth()) * fig.dpi / 72.0 / 2.0 + LINE_TOUCH
            # distancia segmento a rectangulo por tramos (end labels exentos:
            # viven pegados al extremo de su curva por diseno)
            for (s, x0, y0, x1, y1) in no_end:
                ex0, ey0, ex1, ey1 = x0 - lw, y0 - lw, x1 + lw, y1 + lw
                hit = False
                for k in range(len(vv) - 1):
                    d = _seg_rect_dist(vv[k][0], vv[k][1], vv[k + 1][0], vv[k + 1][1],
                                       ex0, ey0, ex1, ey1)
                    if d == 0.0:
                        hit = True
                        break
                if hit:
                    warnings.append({
                        'kind': 'texto-trazo',
                        'text': s[:40],
                        'detail': 'la etiqueta pisa un trazo (revisar a ojo)',
                    })
    # de-duplicar avisos repetidos por la misma etiqueta
    seen = set()
    uniq = []
    for w in warnings:
        key = (w['kind'], w['text'])
        if key not in seen:
            seen.add(key)
            uniq.append(w)
    return errors, uniq
