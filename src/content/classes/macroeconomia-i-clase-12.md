---
title: "Clase 12: Tasa de Interés Real, Ecuación de Fisher y Costo de Uso del Capital"
course: "macroeconomia-i"
order: 12
classType: "clase"
description: "Deducción de la relación exacta y aproximada de Fisher entre tasa nominal y real, desglose del costo de arriendo del capital e integración en la función de inversión óptima."
math: true
---

---
---

¿Qué Determina la Tasa de Arrendamiento del Capital ($R_t$)?
------------------------------------------------------------

En la clase anterior dedujimos que la inversión óptima de la firma depende inversamente del precio de arriendo o renta del capital físico (`$R_t$`):

$$
\begin{align*}I_t = \epsilon \left( \left( \frac{P_t \alpha A_t}{R_t} \right)^{\frac{1}{1 - \alpha}} N_t - K_t \right)\end{align*}
$$

Para comprender qué fuerzas macroeconómicas determinan a `$R_t$`, debemos distinguir primero entre rendimientos monetarios (nominales) y rendimientos en bienes físicos (reales), siguiendo la Sección 4.2 y 4.3 de De Gregorio (*Macroeconomía: teoría y políticas*).


Tasa de Interés Nominal vs. Tasa de Interés Real
------------------------------------------------

Imaginemos el siguiente experimento financiero entre el período `$t$` y el período `$t + 1$`:

1. Suponga un activo financiero con valor nominal de `$\$1$`.
2. Dicho activo paga una **tasa de interés nominal `$i$`** por período.
3. Suponga que hoy (en `$t$`) una cesta de bienes de consumo cuesta exactamente `$P_t = \$1$`.
4. Entre `$t$` y `$t + 1$`, el nivel general de precios crece a la **tasa de inflación `$\pi$`**:

$$
\begin{align*}P_{t+1} = P_t (1 + \pi)\end{align*}
$$

### Evolución del Poder de Compra

* Si invertimos el valor de una cesta hoy (`$P_t$`), en el período `$t + 1$` recibiremos en unidades monetarias:

$$
\begin{align*}P_t (1 + i)\end{align*}
$$

* Sin embargo, en `$t + 1$` cada cesta de bienes cuesta ahora `$P_t (1 + \pi)$`. Por lo tanto, la cantidad de **cestas reales** que podemos comprar en `$t + 1$` es el cociente:

$$
\begin{align*}\frac{\text{Dinero recibido en } t+1}{\text{Precio de la cesta en } t+1} = \frac{\cancel{P_t}(1 + i)}{\cancel{P_t}(1 + \pi)} = \frac{1 + i}{1 + \pi} \gtreqless 1\end{align*}
$$

* **Si `$i > \pi \implies \frac{1 + i}{1 + \pi} > 1$`:** Ganamos poder adquisitivo en términos reales.
* **Si `$i < \pi \implies \frac{1 + i}{1 + \pi} < 1$`:** Perdemos poder adquisitivo (la inflación erosiona el retorno nominal).

### Fórmula Exacta y Aproximación de Fisher

Definimos la **tasa de interés real (`$r$`)** como el crecimiento efectivo del poder de compra:

$$
\begin{align*}1 + r = \frac{1 + i}{1 + \pi} \implies \boxed{r = \frac{1 + i}{1 + \pi} - 1} \quad \text{(Fórmula exacta)}\end{align*}
$$

Para obtener una aproximación lineal sencilla, pasamos `$(1 + \pi)$` a multiplicar al lado izquierdo:

$$
\begin{align*}(1 + \pi)(1 + r) &= 1 + i \\ \cancel{1} + r + \pi r + \pi &= \cancel{1} + i \\ r &= i - \pi - \pi r \quad \left( \text{o equivalentemente: } r = \frac{i - \pi}{1 + \pi} \right)\end{align*}
$$

En economías con inflaciones moderadas o bajas (`$\pi$` es muy pequeña) y tasas reales bajas (`$r$` es muy pequeña), el término cruzado de segundo orden es prácticamente nulo (`$r \pi \approx 0$`), lo que nos lleva a la célebre **Ecuación de Fisher**:

$$
\begin{align*}\boxed{r \approx i - \pi}\end{align*}
$$

> **Espacio para gráfica 1:** *Poder de compra real vs. inflación y aproximación de Fisher.*
> Diagrama comparativo que muestra cómo el factor real `$\frac{1+i}{1+\pi}$` decrece de forma convexa a medida que aumenta la inflación `$\pi$` para una tasa nominal `$i$` dada, cruzando el umbral de ganancia nula (`$r = 0$`) exactamente cuando `$\pi = i$`.


El Costo de Uso o Precio de Arriendo del Capital ($R_t$)
--------------------------------------------------------

Supongamos que una empresa compra una unidad de capital físico en el período `$t$` a un precio nominal `$P_K$` para usarla en la producción. ¿Cuál es el costo económico total de utilizar esa máquina durante un período?

El costo se compone de tres elementos:

1. **Costo financiero (`$P_K i$`):** Es el interés que la firma paga por endeudarse en `$P_K$` pesos (o el costo de oportunidad de no depositar esos `$P_K$` pesos en un banco a la tasa nominal `$i$`).
2. **Costo por depreciación física (`$P_K \delta$`):** Durante el proceso productivo, el capital sufre desgaste físico y obsolescencia en una fracción `$\delta \in (0, 1)$` de su valor.
3. **Ganancia (o pérdida) de capital (`$-\Delta P_K$`):** Si el precio de mercado de la maquinaria sube entre `$t$` y `$t+1$` (`$\Delta P_K = P_{K, t+1} - P_{K, t} > 0$`), el activo de la empresa se valoriza, lo que **reduce** el costo efectivo de haberlo comprado.

Sumando los tres componentes en un mercado competitivo de arriendo de capital:

$$
\begin{align*}R_t = P_K i + P_K \delta - \Delta P_K\end{align*}
$$

Factorizando el precio del bien de capital `$P_K$`:

$$
\begin{align*}R_t = P_K \left( i + \delta - \frac{\Delta P_K}{P_K} \right)\end{align*}
$$

donde `$\frac{\Delta P_K}{P_K} \equiv \pi_K$` representa la **tasa de inflación específica de los bienes de capital**.

### Introducción de la Inflación General ($\pi$)

Para conectar `$R_t$` con la tasa de interés real de la economía (`$r = i - \pi$`), aplicamos el artificio algebraico de **sumar y restar la inflación general `$\pi$`** dentro del paréntesis:

$$
\begin{align*}R_t &= P_K \left( \underbrace{i - \pi}_{= r} + \delta + \pi - \frac{\Delta P_K}{P_K} \right) \\ R_t &= P_K \left( r + \delta + \frac{\Delta P}{P} - \frac{\Delta P_K}{P_K} \right)\end{align*}
$$

El término `$\left( \frac{\Delta P}{P} - \frac{\Delta P_K}{P_K} \right)$` mide el cambio en los **precios relativos** entre los bienes finales y los bienes de capital:
* Si la inflación general supera al encarecimiento de las máquinas (`$\pi > \pi_K$`), el capital se está abaratando en términos reales, lo que representa una pérdida de valor relativo y encarece el costo de uso.
* En el **equilibrio de largo plazo**, asumimos que no hay distorsiones de precios relativos: el precio del capital evoluciona al mismo ritmo que el nivel general de precios (`$\frac{\Delta P}{P} = \frac{\Delta P_K}{P_K}$`), cancelándose ambos términos:

$$
\begin{align*}\boxed{R_t = P_K (r + \delta)}\end{align*}
$$

Si además el precio nominal del capital es igual al precio del bien final (`$P_t = P_K$`), el costo real de uso del capital (`$\frac{R_t}{P_t}$`) es simplemente la suma de la tasa de interés real y la tasa de depreciación: **`$r + \delta$`**.


Integración en la Ecuación de Inversión Óptima
----------------------------------------------

Sustituyendo la expresión estructural del costo de uso `$R_t = P_K (r + \delta)$` dentro de nuestra ecuación de inversión con costos de ajuste:

$$
\begin{align*}I_t = \epsilon \left[ \left( \frac{P_t \alpha A}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} N - K_t \right]\end{align*}
$$

Esta ecuación resume todos los determinantes microfundamentados de la inversión agregada. En la siguiente clase calcularemos paso a paso las derivadas parciales de `$I_t$` respecto a cada uno de sus argumentos (`$r, \delta, A, N, \frac{P_t}{P_K}, \alpha, K_t$`) para verificar sus signos e interpretarlos económicamente.
