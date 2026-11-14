"""Detector de solapamientos para figuras Ecoudea (reglas en pixeles, determinista).

Uso:
    from overlap import check_figure
    errors, warnings = check_figure(fig)

Reglas (medidas en pixeles del render final, ambos temas):
  ERROR (falla el gate):
    - texto <-> texto (cajas de glifo + pad; tick-tick exento: el 0/0 del
      origen es mobiliario de ejes, no contenido)
    - texto <-> punto visible (el marcador pinta ENCIMA del texto y el halo
      queda debajo: radio completo + pad)
    - texto <-> trazo VISIBLE (la linea pinta encima del texto/halo) o corte
      profundo en modo strict
    - texto fuera de la figura (recorte)
  AVISO (triage humano):
    - texto tocando un trazo que pinta DEBAJO (el halo lo tapa; se reporta
      con coordenadas; si lo atraviesa por el nucleo se marca "cruza")

  Fisica del render: el halo solo mitiga si el texto esta encima (zorder
  texto=3 por defecto vs linea=2). Con curvas z>=4 el halo queda debajo y
  todo roce es visible -> ERROR. Los parches decorativos (cajas, sombreados,
  ejes) NO participan: el texto vive encima de ellos por diseno (fondo del
  tema + halo). Las rejillas tampoco participan.
"""
import matplotlib
matplotlib.use("SVG")
import numpy as np
from matplotlib.text import Text
from matplotlib.lines import Line2D

TEXT_PAD = 2.0    # px extra alrededor de cada glifo (texto-texto)
LINE_TOUCH = 1.0  # px: la caja del glifo toca el trazo (con su grosor)
DEEP_PAD = 3.0    # px: si el trazo cruza la caja encogida -> ERROR (el halo
                  # ya no lo salva: la linea atraviesa el texto, no lo roza)


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


def _tick_texts(ax):
    """Rotulos de ticks (NO estan en ax.texts: el gate clasico no los veia
    y dos etiquetas podian compartir aire sin que nadie lo notara)."""
    out = []
    for tx in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
        try:
            if not tx.get_visible():
                continue
        except Exception:
            continue
        s = tx.get_text() or ''
        if not s.strip():
            continue
        out.append(tx)
    return out


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
    """Vertices de lineas solo-marcador -> (puntos display Nx2, radio px, z).
    Colecciones (scatter) igual, con su zorder."""
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
        try:
            pz = float(ln.get_zorder())
        except Exception:
            pz = 2.0
        out.append((pts.reshape(-1, 2), r, pz))
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
        try:
            pz = float(col.get_zorder())
        except Exception:
            pz = 1.0
        out.append((pts.reshape(-1, 2), r, pz))
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


def check_figure(fig, strict=False):
    """Devuelve (errors, warnings): listas de dicts {kind, text, detail}.

    strict=True: todo roce texto-trazo tambien es ERROR (gate cero-avisos
    para figuras nuevas; las historicas siguen en modo aviso).
    """
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
            raw.append((s, bb.x0, bb.y0, bb.x1, bb.y1, _is_end_label(tx),
                        False, float(tx.get_zorder())))
            # recorte contra la figura (no contra los ejes: titulos viven fuera)
            if bb.x0 < fbox.x0 - 1 or bb.y0 < fbox.y0 - 1 or \
               bb.x1 > fbox.x1 + 1 or bb.y1 > fbox.y1 + 1:
                errors.append({
                    'kind': 'recorte',
                    'text': s[:40],
                    'detail': 'etiqueta fuera de la figura (xlim/ylim sin aire)',
                })
        # ticks: participan en texto-texto (antes invisibles al gate),
        # marcados como tick para eximir tick-tick (el 0/0 del origen).
        for tx in _tick_texts(ax):
            try:
                bb = tx.get_window_extent(renderer=renderer)
            except Exception:
                continue
            s = tx.get_text() or ''
            if not s.strip() or _is_ghost(bb):
                continue
            raw.append((s, bb.x0, bb.y0, bb.x1, bb.y1, False, True,
                        float(tx.get_zorder())))
        boxes = [(s, x0 - TEXT_PAD, y0 - TEXT_PAD, x1 + TEXT_PAD, y1 + TEXT_PAD, tick)
                 for (s, x0, y0, x1, y1, _, tick, _) in raw]
        glyphs = [(s, x0, y0, x1, y1, z)
                  for (s, x0, y0, x1, y1, _, _, z) in raw]
        no_end_all = [(s, x0, y0, x1, y1, z)
                      for (s, x0, y0, x1, y1, _, _, z) in raw]  # end labels incluidos
        # texto <-> texto (tick-tick exento: mobiliario de ejes)
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if a[5] and b[5]:
                    continue
                if a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]:
                    errors.append({
                        'kind': 'texto-texto',
                        'text': (a[0][:30] + ' / ' + b[0][:30]),
                        'detail': 'dos etiquetas se pisan',
                    })
        # texto <-> punto: el punto pinta encima (z>=4 tipico) y el halo queda
        # debajo -> ERROR con radio completo + pad. Si el punto pintara
        # debajo del texto, el halo lo tapa -> aviso.
        for pts, r, pz in _dots(ax):
            rr = r + TEXT_PAD
            for (s, x0, y0, x1, y1, tz) in glyphs:
                dx = np.maximum(x0 - rr - pts[:, 0], pts[:, 0] - x1 - rr)
                dy = np.maximum(y0 - rr - pts[:, 1], pts[:, 1] - y1 - rr)
                dist = float(np.min(np.hypot(np.maximum(dx, 0.0),
                                             np.maximum(dy, 0.0))))
                if dist == 0.0:
                    if pz > tz:
                        errors.append({
                            'kind': 'texto-punto',
                            'text': s[:40],
                            'detail': 'etiqueta pisa un marcador (moverla)',
                        })
                    else:
                        warnings.append({
                            'kind': 'texto-punto',
                            'text': s[:40],
                            'detail': 'marcador bajo el texto (revisar a ojo)',
                        })
        # texto tocando trazo: end labels incluidos (antes exentos: vivian
        # pegados a su curva y el gate nunca los media). Fisica del render:
        # si la linea pinta ENCIMA del texto (lz > tz: curvas z>=4), el halo
        # queda debajo y todo roce es visible -> ERROR. Si pinta debajo, el
        # halo lo tapa: solo el corte profundo (trazo por el nucleo del
        # glifo) es ERROR; el roce de borde queda como aviso, salvo
        # strict=True (cero-avisos para figuras nuevas).
        for ln in _strokes(ax):
            try:
                verts = ln.get_transform().transform(ln.get_path().vertices)
            except Exception:
                continue
            if len(verts) == 0:
                continue
            step = max(1, len(verts) // 800)
            vv = verts[::step]
            lw = float(ln.get_linewidth()) * fig.dpi / 72.0 / 2.0 + LINE_TOUCH
            try:
                lz = float(ln.get_zorder())
            except Exception:
                lz = 2.0
            for (s, x0, y0, x1, y1, tz) in no_end_all:
                ex0, ey0, ex1, ey1 = x0 - lw, y0 - lw, x1 + lw, y1 + lw
                hit = False
                for k in range(len(vv) - 1):
                    d = _seg_rect_dist(vv[k][0], vv[k][1], vv[k + 1][0], vv[k + 1][1],
                                       ex0, ey0, ex1, ey1, n=64)
                    if d == 0.0:
                        hit = True
                        break
                if not hit:
                    continue
                # ¿corte profundo? (trazo dentro de la caja encogida)
                ix0, iy0, ix1, iy1 = (x0 + DEEP_PAD, y0 + DEEP_PAD,
                                      x1 - DEEP_PAD, y1 - DEEP_PAD)
                deep = False
                if ix0 < ix1 and iy0 < iy1:
                    for k in range(len(vv) - 1):
                        d = _seg_rect_dist(vv[k][0], vv[k][1],
                                           vv[k + 1][0], vv[k + 1][1],
                                           ix0, iy0, ix1, iy1, n=64)
                        if d == 0.0:
                            deep = True
                            break
                if (lz > tz) or strict:
                    errors.append({
                        'kind': 'texto-trazo',
                        'text': s[:40],
                        'detail': ('el trazo cruza la etiqueta (moverla)' if deep
                                   else ('la linea pinta encima del texto (bajar z o moverla)'
                                         if lz > tz and not strict
                                         else 'roce con trazo en modo strict (moverla)')),
                    })
                else:
                    warnings.append({
                        'kind': 'texto-trazo',
                        'text': s[:40],
                        'detail': ('el trazo cruza bajo el halo (revisar a ojo)'
                                   if deep else
                                   'la etiqueta pisa un trazo (revisar a ojo)'),
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
