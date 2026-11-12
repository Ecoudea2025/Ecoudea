---
title: "Clase 17: Sostenibilidad Fiscal y Equivalencia Ricardiana"
course: "macroeconomia-i"
order: 17
classType: "clase"
description: "Aplicación numérica completa de deuda/PIB sostenible, deducción paso a paso del teorema de Equivalencia Ricardiana y extensión analítica con hogares ricardianos y no ricardianos."
math: true
---

Aplicación Numérica: Cálculo del Superávit Primario Sostenible
--------------------------------------------------------------

Retomamos la ecuación de estado estacionario de la relación deuda pública / PIB deducida en la clase anterior, llamando `$d_t \equiv g_t - t_t$` al déficit primario como proporción del PIB:

$$
\begin{align*}
\bar{b} = \frac{g_t - t_t}{\gamma_y - r} = \frac{d_t}{\gamma_y - r}
\end{align*}
$$

Aquí `$\bar{b}$` representa la **relación deuda/PIB estable, constante o no explosiva** que la economía busca sostener a lo largo del tiempo.

### Ejemplo Numérico de Política Fiscal

Consideremos una economía con los siguientes datos observados:

- Meta estable de deuda pública sobre PIB: `$\bar{b} = 0.55$` (`$55\%$` del PIB).
- Tasa de crecimiento real del PIB: `$\gamma_y = 0.02$` (`$2\%$` anual).
- Tasa de interés real sobre la deuda pública: `$r = 0.12$` (`$12\%$` anual).

Sustituyendo estos valores en la ecuación de sostenibilidad:

$$
\begin{align*}
0.55 = \frac{d_t}{0.02 - 0.12} = \frac{d_t}{-0.10}
\end{align*}
$$

Despejando el déficit primario requerido `$d_t$`:

$$
\begin{align*}
d_t = -(0.55) \times (0.10) = -0.055 = g_t - t_t
\end{align*}
$$

Observemos el significado del signo negativo obtenido:

$$
\begin{align*}
-0.055 = g_t - t_t \iff t_t > g_t \implies \text{Superávit primario del } 5.5\% \text{ del PIB}
\end{align*}
$$

> **Intuición económica:** Como la tasa de interés real `$(12\%)$` excede ampliamente la tasa de crecimiento del PIB `$(2\%)$`, la deuda tiende a crecer por sí sola a un ritmo neto de `$r - \gamma_y = 10\%$` anual sobre el stock de `$55\%$` del PIB. Para impedir que la relación deuda/PIB explote y mantenerla estable en `$55\%$`, el Estado debe generar todos los años un **superávit primario del `$5.5\%$` del PIB** `$(t_t - g_t = 0.055)$`.


¿Es la Deuda Pública Riqueza Neta? Deducción de la Equivalencia Ricardiana
--------------------------------------------------------------------------

Abordamos ahora una pregunta fundamental de la macroeconomía moderna: si el gobierno decide recortar impuestos hoy financiándose con emisión de bonos de deuda pública `$(B_t)$`, ¿aumenta la riqueza percibida por las familias y, por tanto, su consumo agregado?

### Paso 1: Restricción Presupuestaria Intertemporal del Gobierno

En valor presente descontado a la tasa de interés real `$r$`, la deuda pública inicial más sus intereses acumulados debe ser exactamente igual al valor presente de todos los superávits primarios futuros del Estado (condición de solvencia intertemporal o de no-Ponzi):

$$
\begin{align*}
(1 + r) B_t = \sum_{i=0}^{\infty} \frac{T_{t+i} - G_{t+i}}{(1 + r)^i}
\end{align*}
$$

donde:

- **`$B_t$`**: stock real de deuda pública en circulación.
- **`$T_{t+i}$`**: recaudación tributaria real en el período `$t+i$`.
- **`$G_{t+i}$`**: gasto público real en el período `$t+i$`.

### Paso 2: Restricción Presupuestaria Intertemporal de las Familias

Por su parte, la familia representativa planea su senda de consumo `$C_{t+i}$` sujeta a su riqueza financiera inicial `$A_t$` más el valor presente de sus ingresos laborales netos de impuestos:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r) A_t + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i} - T_{t+i}}{(1 + r)^i}
\end{align*}
$$

Aquí **`$A_t$` son los activos financieros totales** en poder de las familias, los cuales están conformados por **deuda pública `$(B_t)$` y posiblemente otros activos financieros privados `$(A_t^P)$`**:

$$
\begin{align*}
A_t = B_t + A_t^P
\end{align*}
$$

### Paso 3: Sustitución y Cancelación de los Impuestos

Reemplazamos la descomposición `$A_t = A_t^P + B_t$` dentro de la restricción presupuestaria intertemporal de las familias:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r)(A_t^P + B_t) + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i} - T_{t+i}}{(1 + r)^i}
\end{align*}
$$

Distribuimos el factor `$(1 + r)$`:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r) A_t^P + (1 + r) B_t + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i} - T_{t+i}}{(1 + r)^i}
\end{align*}
$$

Ahora sustituimos el término `$(1 + r) B_t$` por la restricción intertemporal del gobierno obtenida en el Paso 1:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r) A_t^P + \sum_{i=0}^{\infty} \frac{T_{t+i} - G_{t+i}}{(1 + r)^i} + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i} - T_{t+i}}{(1 + r)^i}
\end{align*}
$$

Separando las sumatorias de ingresos y tributos, notamos que el valor presente de los impuestos aparece con signo positivo en el bloque del gobierno y con signo negativo en el bloque de las familias:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r) A_t^P + \sum_{i=0}^{\infty} \frac{\cancel{T_{t+i}} - G_{t+i} + Y_{\ell, t+i} - \cancel{T_{t+i}}}{(1 + r)^i}
\end{align*}
$$

Al cancelarse los impuestos período a período, obtenemos la **restricción presupuestaria consolidada de la economía** (el resultado de la **Equivalencia Ricardiana**):

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}}{(1 + r)^i} = (1 + r) A_t^P + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i} - G_{t+i}}{(1 + r)^i}
\end{align*}
$$

> **Conclusión de la Equivalencia Ricardiana:** Si todos los agentes pueden mantener deuda pública y todos pagan impuestos bajo horizontes intertemporales consistentes, **la deuda pública no es riqueza neta**. Para las familias, el bono público que poseen como activo se compensa peso a peso con el valor presente de los impuestos futuros necesarios para pagarlo. En consecuencia, sustituir impuestos hoy por deuda pública deja intacto el consumo intertemporal, siempre que no cambie la trayectoria del gasto público `$G_{t+i}$`.


Extensión: Economías con Agentes Ricardianos y No Ricardianos
------------------------------------------------------------

En la realidad, no todos los hogares tienen acceso al crédito ni pueden comprar o acumular activos financieros. Para analizar las desviaciones respecto a la Equivalencia Ricardiana, dividimos la población en dos grupos:

### 1. Hogares No Ricardianos `$(NR)$` — Proporción `$\phi$`

Suponga que una fracción **`$\phi \in (0, 1)$`** de la población **no puede acumular activos financieros** ni acceder al mercado de crédito `$(A_t^{NR} = 0)$`. Su restricción intertemporal colapsa a:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}^{NR}}{(1 + r)^i} = \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i}^{NR} - T_{t+i}^{NR}}{(1 + r)^i}
\end{align*}
$$

Al carecer de activos y acceso financiero, estos hogares consumen su ingreso disponible período a período `$(C_{t+i}^{NR} = Y_{\ell, t+i}^{NR} - T_{t+i}^{NR})$`.

### 2. Hogares Ricardianos `$(R)$` — Proporción `$1 - \phi$`

Suponga que la fracción restante **`$(1 - \phi)$`** de la población **sí puede acumular activos financieros** `$(A_t^R)$` y suavizar su consumo óptimamente a lo largo del tiempo:

$$
\begin{align*}
\sum_{i=0}^{\infty} \frac{C_{t+i}^R}{(1 + r)^i} = (1 + r) A_t^R + \sum_{i=0}^{\infty} \frac{Y_{\ell, t+i}^R - T_{t+i}^R}{(1 + r)^i}
\end{align*}
$$

### Pregunta de Análisis: ¿Se Cumple la Equivalencia Ricardiana y en Qué Grado?

Cuando `$\phi > 0$`, **la Equivalencia Ricardiana deja de cumplirse de forma absoluta y se cumple únicamente de manera parcial**:

| Tipo de hogar | Peso poblacional | Respuesta ante rebaja tributaria financiada con deuda `$(-\Delta T_t = \Delta B_t > 0)$` |
| :--- | :--- | :--- |
| **Ricardianos `$(R)$`** | `$1 - \phi$` | Ahorran íntegramente el recorte tributario para pagar los mayores impuestos futuros; `$\Delta C_t^R = 0$`. |
| **No Ricardianos `$(NR)$`** | `$\phi$` | No pueden suavizar ni endeudarse; gastan el alivio tributario en consumo inmediato: `$\Delta C_t^{NR} > 0$`. |

En conclusión, cuanto mayor sea la proporción `$\phi$` de hogares con restricciones de liquidez, menor es el grado en que se cumple la Equivalencia Ricardiana y mayor es el impacto expansivo de corto plazo de un déficit fiscal sobre el consumo agregado.

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/ricardiana-light.svg" alt="Barras de respuesta del consumo: ricardianos cero y no ricardianos positivo ante rebaja tributaria con deuda." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/ricardiana-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: los ricardianos ahorran el alivio tributario y los no ricardianos lo consumen; a mayor phi, mayor efecto expansivo.</figcaption>
</figure>
