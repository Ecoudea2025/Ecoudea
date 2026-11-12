---
title: "Clase 18: Modelo Intertemporal Real con Inversión y Trabajo (Equilibrio General)"
course: "macroeconomia-i"
order: 18
classType: "clase"
description: "Arquitectura completa del modelo intertemporal real de equilibrio general (Williamson), flujo circular en economía cerrada, supuestos de primer mejor, restricción presupuestaria intertemporal, Lagrangiano y deducción paso a paso de todas las C.P.O."
math: true
---

Modelo Intertemporal Real con Inversión y Trabajo (Equilibrio General)
----------------------------------------------------------------------

Con esta sesión iniciamos el estudio del **Modelo Intertemporal Real con Inversión y Trabajo** en un marco de **Equilibrio General**, siguiendo la exposición de referencia de Stephen D. Williamson (*Macroeconomics*, Capítulo 10 en la 4.ª edición y Capítulo 11 en la 5.ª edición).

A diferencia de los modelos de equilibrio parcial vistos anteriormente —donde analizábamos por separado el consumo de las familias, la inversión de las firmas o la deuda del gobierno—, aquí integramos simultáneamente a **todos los agentes económicos** interactuando en el mercado de bienes, de trabajo y de fondos prestables dentro de una **economía cerrada** (aislada del resto del mundo).

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/flujo-williamson-light.svg" alt="Flujo circular en economia cerrada: familias y firmas intercambian trabajo y salarios, mercado en el centro y gobierno con impuestos y gasto." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/flujo-williamson-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: familias, firmas, mercado y gobierno en economía cerrada; el resto del mundo queda fuera sin flujos.</figcaption>
</figure>

### Supuestos Fundamentales para el Equilibrio General Óptimo de Pareto

Para que el equilibrio general competitivo de esta economía alcance el **Óptimo de Pareto o Primer Mejor (*First Best*)**, imponemos tres supuestos estructurales clave:

1. **No hay externalidades:** ninguna decisión de producción o consumo genera costos o beneficios externos no reflejados en los precios de mercado.
2. **No hay poder de mercado:** tanto las familias como las firmas actúan en competencia perfecta y son tomadoras de precios y salarios.
3. **No hay impuestos que generen distorsiones:** no existen impuestos *ad-valorem* (como impuestos proporcionales al consumo `$\tau_c$` o al ingreso `$\tau_y$`). El gobierno recauda exclusivamente mediante impuestos de suma fija `$(T_t)$`.


El Bloque de las Familias o Consumidores
----------------------------------------

Comenzamos el análisis desagregando las decisiones del primer gran agente del modelo: las **familias o consumidores**, quienes cumplen dos funciones simultáneas:

- Consumen (y ahorran/desahorran para suavizar consumo entre períodos).
- Deciden cuánto trabajar dada una tasa salarial real fijada de manera competitiva en el mercado de trabajo.

### Dotación de Tiempo, Trabajo y Ocio

Cada individuo cuenta con una **dotación fija de tiempo `$h$`** (en horas totales disponibles en el período; por ejemplo, `$360 \times 24$` horas anuales). Si denotamos por **`$N_t$`** la cantidad de horas trabajadas al año, al mes o al trimestre, entonces el tiempo restante se dedica al **ocio (`$\ell_t$`, del inglés *leisure*)**:

$$
\begin{align*}
\ell_t = h - N_t
\end{align*}
$$

En algunos modelos macroeconómicos es habitual normalizar la dotación total de tiempo dividiendo toda la ecuación por `$h$` para expresar ocio y trabajo como fracciones entre `$0$` y `$1$`:

$$
\begin{align*}
\frac{\ell_t}{h} = \frac{h}{h} - \frac{N_t}{h} \implies \ell_t = 1 - n_t \qquad \text{con} \qquad 0 < \ell_t < 1, \quad 0 < n_t < 1
\end{align*}
$$

### Función de Utilidad Instantánea y Sus Propiedades

¿Cómo eligen los consumidores su nivel de consumo `$C_t$` y su nivel de ocio `$\ell_t$`? A través de una **función de utilidad instantánea** que agrega ambos bienes:

$$
\begin{align*}
u = u(C_t, h - N_t) \qquad \text{o en forma normalizada:} \qquad u = u(C_t, 1 - n_t)
\end{align*}
$$

donde siempre `$h - N_t = \ell_t$`. Esta función satisface las propiedades estándar de monotonicidad positiva y concavidad estricta:

1. **Respecto al consumo `$(C_t)$`:**

$$
\begin{align*}
\frac{\partial u(\cdot)}{\partial C_t} > 0, \qquad \frac{\partial^2 u(\cdot)}{\partial C_t^2} < 0
\end{align*}
$$

2. **Respecto al ocio `$(\ell_t)$`:**

$$
\begin{align*}
\frac{\partial u(\cdot)}{\partial \ell_t} > 0, \qquad \frac{\partial^2 u(\cdot)}{\partial \ell_t^2} < 0
\end{align*}
$$

3. **Respecto a las horas trabajadas `$(N_t)$`:** dado que `$\ell_t = h - N_t$`, trabajar una hora más reduce el ocio en una hora `$(\frac{\partial \ell_t}{\partial N_t} = -1)$`, lo que invierte el signo de la primera derivada (el trabajo genera desutilidad marginal) pero mantiene negativa la segunda derivada:

$$
\begin{align*}
\frac{\partial u(\cdot)}{\partial N_t} < 0, \qquad \frac{\partial^2 u(\cdot)}{\partial N_t^2} < 0
\end{align*}
$$


Restricción de Presupuesto Intertemporal en Dos Períodos
--------------------------------------------------------

Definimos las variables reales del presupuesto familiar en cada período:

- **`$C_t$`**: consumo real.
- **`$S_t$`**: ahorro real.
- **`$W_t$`**: salario real por hora trabajada.
- **`$\Pi_t$`**: beneficios reales distribuidos por las firmas (propiedad de las familias).
- **`$T_t$`**: impuestos de suma fija.

### Paso 1: Restricciones Flujo Período a Período

- **En `$t = 1$`:** los ingresos laborales más los beneficios netos de impuestos financian el consumo y el ahorro del primer período:

$$
\begin{align*}
C_1 + S_1 = W_1 N_1 + \Pi_1 - T_1
\end{align*}
$$

- **En `$t = 2$`:** la familia recibe sus ingresos del segundo período más el capital e intereses del ahorro realizado en `$t = 1$` `$((1 + r) S_1)$`:

$$
\begin{align*}
C_2 + S_2 = W_2 N_2 + \Pi_2 - T_2 + (1 + r) S_1
\end{align*}
$$

Como el horizonte termina en `$t = 2$` y no hay herencias, en el óptimo la familia agota sus recursos y no deja ahorro final `$(S_2 = 0)$`:

$$
\begin{align*}
C_2 = W_2 N_2 + \Pi_2 - T_2 + (1 + r) S_1
\end{align*}
$$

### Paso 2: Consolidación en Valor Futuro y en Valor Presente

Despejando `$S_1 = W_1 N_1 + \Pi_1 - T_1 - C_1$` de la ecuación de `$t = 1$` y sustituyéndolo en la ecuación de `$t = 2$`, obtenemos la **Restricción Presupuestaria Intertemporal (R.P.I.) en valor futuro**:

$$
\begin{align*}
C_2 = W_2 N_2 + \Pi_2 - T_2 + (1 + r)(W_1 N_1 + \Pi_1 - T_1 - C_1)
\end{align*}
$$

Ahora realizamos el álgebra paso a paso para expresarla en **valor presente**: dividimos toda la ecuación por `$(1 + r)$`:

$$
\begin{align*}
\frac{C_2}{1 + r} = \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r} + W_1 N_1 + \Pi_1 - T_1 - C_1
\end{align*}
$$

Pasamos `$C_1$` al lado izquierdo sumando, obteniendo la **Restricción de Presupuesto Intertemporal en valor presente**:

$$
\begin{align*}
C_1 + \frac{C_2}{1 + r} = W_1 N_1 + \Pi_1 - T_1 + \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r}
\end{align*}
$$


Problema de Optimización Intertemporal de la Familia
----------------------------------------------------

En horizonte infinito, la función de utilidad intertemporal descontada a la tasa subjetiva `$\beta \in (0, 1)$` es:

$$
\begin{align*}
U = \sum_{t=1}^{\infty} \beta^{t-1} u(C_t, \ell_t) = \sum_{t=1}^{\infty} \beta^{t-1} u(C_t, h - N_t) < \infty
\end{align*}
$$

En nuestro modelo de **dos períodos**, la utilidad total es `$U = u(C_1, h - N_1) + \beta u(C_2, h - N_2)$`, y la familia resuelve:

$$
\begin{align*}
\max_{\{C_1, C_2, N_1, N_2\}} \quad & u(C_1, h - N_1) + \beta u(C_2, h - N_2) \\
\text{s.a.} \quad & C_1 + \frac{C_2}{1 + r} = W_1 N_1 + \Pi_1 - T_1 + \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r}
\end{align*}
$$

### Paso 1: Planteamiento del Lagrangiano

$$
\begin{align*}
\mathcal{L} = u(C_1, h - N_1) + \beta u(C_2, h - N_2) + \lambda \left[ W_1 N_1 + \Pi_1 - T_1 + \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r} - C_1 - \frac{C_2}{1 + r} \right]
\end{align*}
$$

### Paso 2: Condiciones de Primer Orden (C.P.O.)

Derivamos parcialmente respecto a `$C_1$`, `$C_2$`, `$N_1$`, `$N_2$` y `$\lambda$`, aplicando la regla de la cadena en `$\ell_t = h - N_t$` `$(\frac{\partial \ell_t}{\partial N_t} = -1)$`:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial C_1} &= \frac{\partial u(\cdot)}{\partial C_1} - \lambda = 0 \\
\frac{\partial \mathcal{L}}{\partial C_2} &= \beta \frac{\partial u(\cdot)}{\partial C_2} - \frac{\lambda}{1 + r} = 0 \\
\frac{\partial \mathcal{L}}{\partial N_1} &= -\frac{\partial u(\cdot)}{\partial \ell_1} + \lambda W_1 = 0 \\
\frac{\partial \mathcal{L}}{\partial N_2} &= -\beta \frac{\partial u(\cdot)}{\partial \ell_2} + \frac{\lambda W_2}{1 + r} = 0 \\
\frac{\partial \mathcal{L}}{\partial \lambda} &= -C_1 - \frac{C_2}{1 + r} + W_1 N_1 + \Pi_1 - T_1 + \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r} = 0
\end{align*}
$$

De la ecuación `(1)` despejamos directamente el multiplicador de Lagrange:

$$
\begin{align*}
\lambda = \frac{\partial u(\cdot)}{\partial C_1} = U_{mg C_1}
\end{align*}
$$

### Paso 3: Deducción de la Ecuación de Euler (Transición del Consumo)

Usamos las ecuaciones **`(1)` y `(2)`**. Despejamos de `(2)` y sustituimos `$\lambda = U_{mg C_1}$`:

$$
\begin{align*}
\beta U_{mg C_2} &= \frac{\lambda}{1 + r} = \frac{U_{mg C_1}}{1 + r} \\
U_{mg C_1} &= \beta U_{mg C_2} (1 + r)
\end{align*}
$$

Esta es la **Ecuación de Euler** o **ecuación de transición del consumo** entre el período `$1$` y el período `$2$`.

### Paso 4: Condiciones de Optimalidad Intratemporal en `$t = 1$` y `$t = 2$`

Usamos las ecuaciones **`(1)` y `(3)`** para el período `$t = 1$`. De `(3)` tenemos `$-U_{mg \ell_1} + \lambda W_1 = 0$`, es decir:

$$
\begin{align*}
\cancel{-} U_{mg \ell_1} = \cancel{-} \lambda W_1 = \cancel{-} U_{mg C_1} W_1
\end{align*}
$$

Cancelando el signo negativo en todos los términos, obtenemos la **condición de optimalidad intratemporal en `$t = 1$`**:

$$
\begin{align*}
U_{mg \ell_1} = U_{mg C_1} W_1
\end{align*}
$$

Repitiendo exactamente el mismo procedimiento con las ecuaciones **`(2)` y `(4)`** para el período `$t = 2$` (sustituyendo `$\frac{\lambda}{1+r} = \beta U_{mg C_2}$` y cancelando `$\beta$` en ambos lados), obtenemos la **condición de optimalidad intratemporal en `$t = 2$`**:

$$
\begin{align*}
U_{mg \ell_2} = U_{mg C_2} W_2
\end{align*}
$$

> **Intuición económica:** Tanto en `$t = 1$` como en `$t = 2$`, el consumidor óptimo iguala la utilidad marginal de una hora adicional de ocio `$(U_{mg \ell_t})$` con el valor en utilidad del consumo que podría comprar si trabajara esa hora al salario real `$W_t$` `$(U_{mg C_t} W_t)$`.
