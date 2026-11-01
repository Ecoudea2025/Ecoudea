# Guía Maestra de Estilo Visual: Matplotlib y Manim para Ecoudea
*Estándar de visualización económica moderna para gráficos estáticos y animaciones vectoriales (Dark & Light Mode).*

---

## 1. Manifiesto y Filosofía Pedagógica Ecoudea

En **Ecoudea**, los gráficos y animaciones no son adornos técnicos ni pizarras atestadas de ecuaciones algebraicas áridas: **son herramientas para que el estudiante comprenda intuitivamente la economía viendo las dinámicas de otra forma**.

### Los 5 Mandamientos Visuales Ecoudea:
1. **Pedagogía Intuitiva vs. Saturación:** El estudiante debe entender en 3 segundos qué está pasando (quién gana, quién pierde, qué fuerza presiona el cambio). Menos texto adentro del gráfico, más claridad geométrica.
2. **Dark Mode First:** El estándar principal para la web ([Ecoudea en GitHub](https://ecoudea2025.github.io/Ecoudea/)), diapositivas interactivas y videos es el **Dark Canvas** (pizarra noche `#0F172A`). Las curvas brillan con alto contraste y eliminan el deslumbramiento ocular.
3. **Cero Solapamientos (Invariante Estricto):** Ningún texto, número o flecha puede montarse sobre una curva, sobre otro texto o sobre los títulos de los ejes.
4. **Ejes Teóricos Puros (Lección Editorial):** En diagramas teóricos (IS-LM, curvas de indiferencia, excedentes), **está prohibido mostrar números genéricos de cuadrícula (20, 40, 60...)**. Los únicos valores en los ejes son las variables económicas del modelo ($P^*, Q^*, Y_1, c_1^*$).
5. **Amplitud Geométrica ("El Abanico Abierto"):** La diferencia entre curvas comparativas debe ser amplia (al menos 30% del espacio visual). Curvas casi paralelas o ángulos agudos diminutos apelmazan los puntos y arruinan la explicación.

---

## 2. Paleta Cromática Semántica Ecoudea

| Elemento Económico | Token Color | Hex (Dark Mode) | Hex (Light Mode) | Rol Pedagógico |
| :--- | :--- | :--- | :--- | :--- |
| **Lienzo / Fondo** | `bg` | `#0F172A` | `#FFFFFF` | Pizarra profunda o papel editorial limpio |
| **Tarjetas / Cajas** | `card` | `#1E293B` | `#F8FAFC` | Fondo protector para textos anti-colisión |
| **Texto Principal** | `text` | `#F8FAFC` | `#0F172A` | Títulos y etiquetas de máxima jerarquía |
| **Texto Secundario / Ejes**| `muted` / `axis` | `#94A3B8` | `#4A5568` | Ejes, ticks y directrices punteadas |
| **Rejilla Tenue** | `grid` | `#1E293B` / `#334155`| `#E2E8F0` | Rejilla ultra suave al fondo (`alpha=0.5`) |
| **Demanda / Curva IS / Bienestar** | `demand` | `#38BDF8` (Cyan) | `#1E3A8A` (Zafiro) | Curvas descendentes y preferencias |
| **Oferta / Curva LM / Costos** | `supply` / `cost`| `#FB7185` (Coral)| `#B91C1C` (Carmesí) | Curvas ascendentes o costos marginales |
| **Ingreso Marginal / Restricciones** | `mr` / `budget`| `#A855F7` (Púrpura)| `#6D28D9` (Violeta) | Relaciones marginales y límites |
| **Equilibrios ($E^*$) / Eficiencia** | `equilibrium` | `#34D399` (Menta)| `#059669` (Esmeralda) | Puntos óptimos de tangencia o cruce |
| **Dotación Inicial ($A$)** | `dotacion` | `#F59E0B` (Ámbar) | `#D97706` (Ámbar oscuro) | Punto de partida de los agentes |
| **Pérdida Social (DWL)** | `dwl` | `#FBBF24` (Ámbar luz)| `#F59E0B` (Ámbar suave)| Triángulo de ineficiencia de mercado |
| **Beneficio Extraordinario** | `profit` | `#10B981` (Verde) | `#10B981` (Verde) | Rectángulo de rentas monopólicas |

---

## 3. Estándar Matplotlib: Plantilla y Reglas de Producción

### 3.1. Plantilla Base Reutilizable (`eco_matplotlib.py`)
```python
import matplotlib.pyplot as plt
import numpy as np

# Paleta Dark Mode Ecoudea
C = {
    "bg": "#0F172A",
    "card": "#1E293B",
    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "grid": "#1E293B",
    "demand": "#38BDF8",
    "supply": "#FB7185",
    "mr": "#A855F7",
    "eq": "#34D399",
    "dot": "#F59E0B",
    "proj": "#334155"
}

def setup_ecoudea_plot(figsize=(10.5, 6.8)):
    fig, ax = plt.subplots(figsize=figsize, dpi=300, facecolor=C["bg"])
    ax.set_facecolor(C["bg"])

    # 1. Eliminar spines obsoletos
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C["muted"])
    ax.spines['bottom'].set_color(C["muted"])
    ax.spines['left'].set_linewidth(1.3)
    ax.spines['bottom'].set_linewidth(1.3)
    
    # 2. Rejilla ultra suave en zorder inferior
    ax.grid(True, linestyle="--", linewidth=0.6, color=C["grid"], alpha=0.5, zorder=0)
    ax.set_axisbelow(True)
    return fig, ax

def set_pure_econ_axes(ax, x_ticks, x_labels, y_ticks, y_labels, xlabel="", ylabel=""):
    """Configura los ejes donde SOLO existen las variables teóricas del modelo."""
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=12, fontweight="bold")
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, fontsize=12, fontweight="bold")
    ax.tick_params(colors=C["muted"], length=5, width=1.2)

    # Rótulos en los extremos absolutos protegidos (cero colisión con títulos)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11.5, fontweight="bold", color=C["muted"], labelpad=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11.5, fontweight="bold", color=C["muted"], labelpad=14)

def add_projection(ax, x, y, color=C["muted"]):
    """Directrices ortogonales limpias hacia ambos ejes."""
    ax.plot([x, x], [0, y], linestyle=":", linewidth=1.2, color=color, alpha=0.8, zorder=2)
    ax.plot([0, x], [y, y], linestyle=":", linewidth=1.2, color=color, alpha=0.8, zorder=2)
```

### 3.2. Reglas Estrictas Anti-Solapamiento en Matplotlib
- **Prohibido `plt.legend()` flotante:** Toda curva lleva su nombre directo en el extremo o paralelo a ella usando rotación tangente (`angulo_de_recta`).
- **Aislamiento de la Banda Superior:** Siempre usar `fig.subplots_adjust(top=0.84)` para que títulos y subtítulos nunca rocen la parte superior del gráfico cartesiano.
- **Curvas de Eje a Eje:** Toda restricción presupuestaria debe nacer en $c_1 = 0$ y terminar tocando $c_2 = 0$.

---

## 4. Estándar ManimCE: Animaciones Vectoriales Fluidas

Cuando un proceso económico implique un choque dinámico ($t_0 \to t_1$, alza de tasa de interés, choque de oferta, etc.), **ManimCE es el estándar superior**: dibuja trazos continuos, interpola rotaciones en tiempo real y gestiona el posicionamiento de textos sin solapamientos.

### 4.1. Plantilla Maestra en ManimCE (`eco_manim.py`)
```python
from manim import *
import numpy as np

# Blindaje Windows File Locks
config.no_latex_cleanup = True

# Paleta Ecoudea
C_BG = "#0F172A"
C_AXIS = "#64748B"
C_TEXT = "#F8FAFC"
C_MUTED = "#94A3B8"
C_BLUE = "#38BDF8"
C_CORAL = "#FB7185"
C_MINT = "#34D399"
C_AMBER = "#F59E0B"

class EcoudeaBaseScene(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.camera.background_color = C_BG

        # Ejes limpios
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 120, 20],
            x_length=8.5,
            y_length=5.6,
            axis_config={"color": C_AXIS, "stroke_width": 2.2},
            tips=False
        ).to_corner(DL, buff=1.0)

        # Rótulos en los extremos libres con .next_to
        x_label = Text("Cantidad / Consumo presente (c₁)", font_size=15, color=C_MUTED, weight=BOLD)\
            .next_to(axes.x_axis.get_end(), DOWN, buff=0.3).shift(LEFT * 1.5)
        y_label = Text("Precio / Consumo futuro (c₂)", font_size=15, color=C_MUTED, weight=BOLD)\
            .next_to(axes.y_axis.get_end(), UP, buff=0.25).shift(RIGHT * 1.2)

        # Cabecera editorial separada
        title = Text("Modelo Económico Ecoudea", font_size=20, weight=BOLD, color=C_TEXT)\
            .to_corner(UL, buff=0.55)
        
        self.play(FadeIn(title), Create(axes), Write(x_label), Write(y_label), run_time=1.2)
        self.wait(1)
```

### 4.2. El Paradigma de Animación Pedagógica en 4 Actos
1. **Acto 1 (Punto de Partida):** Se dibuja únicamente la dotación inicial $A$ y el equilibrio base $E_0$. Cero elementos del futuro.
2. **Acto 2 (Dinámica Física del Choque):** La curva rota o se desplaza en vivo con `Transform(curva_inicial, curva_final, rate_func=smooth)`. El estudiante ve la física de la rotación sobre el punto de pivote.
3. **Acto 3 (El Nuevo Óptimo):** Se materializa suavemente la nueva curva de indiferencia (`Create(curva, rate_func=smooth)`) y el nuevo punto de tangencia $E_1$.
4. **Acto 4 (Conclusión):** Una flecha limpia (`GrowArrow`) señala la dirección del ajuste ($\Delta c_1 < 0$ o aumento del ahorro).

---

## 5. Tabla de Decisiones: ¿Cuándo usar Matplotlib y cuándo Manim?

| Caso de Uso | Herramienta Recomendada | Razón Técnica | Formato de Salida |
| :--- | :--- | :--- | :--- |
| **Imágenes estáticas para guías, apuntes o libros web** | **Matplotlib** | Renderizado vectorial rápido en PNG a 300 DPI o SVG ligero. | `.png` (300 DPI) o `.svg` |
| **Choques dinámicos, rotaciones y desplazamientos** | **ManimCE** | Muestra el proceso de cambio en tiempo real con curvas *smooth*. | `.mp4` (1080p60) y `.gif` |
| **Modelos comparativos de alta densidad** | **ManimCE** (o Matplotlib con panel lateral) | Evita amontonar todo en una sola imagen dividiendo el fenómeno por fases temporales. | `.gif` web optimizado |

---

## 6. Comandos de Renderizado y Optimización para Ecoudea

```bash
# Renderizar imagen estática en Matplotlib
python script_grafico.py

# Renderizar animación en ManimCE en máxima calidad (1080p, 60fps)
manim -qh --format=mp4 scene_archivo.py NombreDeLaEscena -o video_ecoudea.mp4

# Convertir el video de Manim a GIF web ultra optimizado con paleta Lanczos (sin pérdida de calidad)
ffmpeg -y -i "ruta/al/video.mp4" -vf "fps=18,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" "ruta/al/archivo.gif"
```
