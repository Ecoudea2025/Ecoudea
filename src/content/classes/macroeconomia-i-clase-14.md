---
title: "Clase 14: Teoría q de Tobin y Optimización Intertemporal de la Firma"
course: "macroeconomia-i"
order: 14
classType: "clase"
description: "Maximización intertemporal del valor presente de la firma con costos de ajuste convexos, deducción paso a paso de la q de Tobin, condición de arbitraje e iteración hacia adelante."
math: true
---


El Problema Intertemporal de la Firma
-------------------------------------

En las clases anteriores resolvimos la decisión de la firma en dos etapas separadas: primero hallamos el capital estático deseado `$K^*$` y luego minimizamos un costo cuadrático de ajuste. 

La **Teoría `$q$` de Tobin** (desarrollada por el Premio Nobel James Tobin y formalizada con costos de ajuste en la Sección 4.5 y 4.8 de De Gregorio) unifica ambas decisiones en un único **problema de optimización intertemporal**: la firma maximiza el valor presente descontado de sus beneficios futuros netos de los costos de comprar e instalar capital:

$$
\begin{align*}V_t = \sum_{i=0}^\infty \frac{\Pi_{t+i}}{(1 + r)^i}\end{align*}
$$

### Definición de Variables y Costos de Instalación

* `$r$`: Tasa de interés real constante a la que se descuentan los flujos futuros.
* `$\Pi_t$`: Beneficio neto de la firma en el período `$t$`.
* `$P_t Y_t$`: Ingreso por ventas de la firma representativa y competitiva.
* `$P_{Kt}$`: Precio de adquisición de cada unidad nueva de capital físico.
* `$I_t$`: Inversión bruta en el período `$t$`.
* `$C(I_t)$`: **Costos de invertir (o de ajuste/instalación)**. Es una función estrictamente convexa (usualmente cuadrática y simétrica) que satisface `$C(0) = 0$`, `$C'(0) = 0$` y `$C''(I_t) > 0$`.

Por lo tanto, el desembolso total asociado a invertir `$I_t$` unidades es `$P_{Kt} \big( I_t + C(I_t) \big)$`, y el beneficio corriente de la firma se escribe como:

$$
\begin{align*}\Pi_t = P_t Y_t - P_{Kt} \big( I_t + C(I_t) \big) - W_t L_t\end{align*}
$$


Las Dos Restricciones del Problema
----------------------------------

La firma maximiza `$V_t$` sujeta a dos restricciones estructurales en cada período:

1. **Restricción tecnológica (Función de producción):**

$$
\begin{align*}Y_t = A_t F(K_t, L_t)\end{align*}
$$

2. **Ley de movimiento del capital físico:**

El capital disponible en el período siguiente (`$K_{t+1}$`) es igual al capital sobreviviente tras la depreciación `$(1 - \delta)K_t$` más la inversión bruta `$I_t$`:

$$
\begin{align*}K_{t+1} = (1 - \delta)K_t + I_t \implies I_t = K_{t+1} - (1 - \delta)K_t\end{align*}
$$

*(Nota: En términos de variación, `$\frac{\partial I_t}{\partial K_{t+1}} = 1$` y `$\frac{\partial I_{t+1}}{\partial K_{t+1}} = -(1 - \delta)$`: aumentar `$K_{t+1}$` exige invertir una unidad más hoy, pero ahorra tener que reponer `$(1 - \delta)$` unidades mañana).*


Expansión Intertemporal y Condiciones de Primer Orden
-----------------------------------------------------

Sustituyendo ambas restricciones en los beneficios de `$t, t+1, t+2, \ldots$`, el valor presente de la firma `$V_t$` queda expresado puramente en función de la secuencia de capital y trabajo `$\{K_{t+1}, L_t\}_{t=0}^\infty$`:

$$
\begin{align*}V_t = \sum_{i=0}^\infty \frac{P_{t+i} A_{t+i} F(K_{t+i}, L_{t+i}) - P_{K, t+i} \Big[ I_{t+i} + C(I_{t+i}) \Big] - W_{t+i} L_{t+i}}{(1 + r)^i}\end{align*}
$$

### 1. Condición de Optimalidad para la Contratación de Trabajo ($L_t$)

Como el trabajo no tiene costos de ajuste intertemporales, derivamos `$V_t$` respecto a `$L_t$` en el período `$i = 0$`:

$$
\begin{align*}\frac{\partial V_t}{\partial L_t} = P_t PMgL_t - W_t = 0 \implies \boxed{P_t PMgL_t = W_t}\end{align*}
$$

### 2. Condición de Optimalidad para el Capital ($K_{t+1}$)

Observemos que la variable `$K_{t+1}$` aparece únicamente en **dos sumandos consecutivos** de la serie infinita:
* En `$i = 0$` (período `$t$`): incrementar `$K_{t+1}$` aumenta la inversión hoy `$I_t$`, generando un costo marginal `$-P_{Kt}\big(1 + C'(I_t)\big)$`.
* En `$i = 1$` (período `$t + 1$`, descontado por `$1 + r$`): ese mayor `$K_{t+1}$` produce más bienes (`$P_{t+1} PMgK_{t+1}$`) y deja capital remanente más ahorro en costos de ajuste futuros (`$P_{K, t+1}\big[(1 - \delta) + C'(I_{t+1})\big]$`).

Derivando `$V_t$` respecto a `$K_{t+1}$` e igualando a cero:

$$
\begin{align*}\frac{\partial V_t}{\partial K_{t+1}} = \frac{-P_{Kt} \big( 1 + C'(I_t) \big)}{(1 + r)^0} + \frac{P_{t+1} PMgK_{t+1} + P_{K, t+1} \big( (1 - \delta) + C'(I_{t+1}) \big)}{(1 + r)^1} = 0\end{align*}
$$

Pasando el primer término al otro lado de la igualdad:

$$
\begin{align*}P_{Kt} \big( 1 + C'(I_t) \big) = \frac{P_{t+1} PMgK_{t+1} + P_{K, t+1} \big( (1 - \delta) + C'(I_{t+1}) \big)}{1 + r}\end{align*}
$$


Definición de la $q$ de Tobin y Condición de Arbitraje
------------------------------------------------------

Para interpretar con total claridad esta condición de optimalidad, normalizamos todos los precios a la unidad (`$P_t = P_{t+1} = P_{Kt} = P_{K, t+1} = 1$`):

* **`$1 + C'(I_t) \equiv q_t$`:** Es el costo marginal total (compra más instalación) de añadir una unidad de capital en el período `$t$`. En el óptimo, coincide con el valor económico sombra de una unidad de capital instalada.
* **`$1 + C'(I_{t+1}) \equiv q_{t+1}$`:** Es el costo marginal (y valor sombra) de una unidad de capital en el período `$t + 1$`.

Sustituyendo `$q_t$` y `$q_{t+1}$` en nuestra condición de primer orden (notando que `$(1 - \delta) + C'(I_{t+1}) = -\delta + \big(1 + C'(I_{t+1})\big) = -\delta + q_{t+1}$`):

$$
\begin{align*}1 + C'(I_t) = \frac{PMgK_{t+1} - \delta + \big( 1 + C'(I_{t+1}) \big)}{1 + r}\end{align*}
$$

Con lo que llegamos a la **ecuación fundamental de movimiento de la `$q$` de Tobin**:

$$
\begin{align*}\boxed{q_t = \frac{PMgK_{t+1} - \delta + q_{t+1}}{1 + r}}\end{align*}
$$

### Deducción de la Ecuación de Arbitraje de Activos

Multiplicamos ambos lados por `$(1 + r)$`:

$$
\begin{align*}(1 + r) q_t &= PMgK_{t+1} - \delta + q_{t+1} \\ q_t + r q_t &= PMgK_{t+1} - \delta + q_{t+1}\end{align*}
$$

Pasamos `$q_t$` a restar al lado derecho y definimos la ganancia de capital como `$\Delta q_{t+1} \equiv q_{t+1} - q_t$`:

$$
\begin{align*}r q_t = PMgK_{t+1} - \delta + \underbrace{q_{t+1} - q_t}_{\equiv \Delta q_{t+1}}\end{align*}
$$

Dividiendo toda la expresión entre `$q_t$`:

$$
\begin{align*}r = \frac{PMgK_{t+1} - \delta + \Delta q_{t+1}}{q_t} \iff \boxed{r = \frac{PMgK_{t+1} - \delta}{q_t} + \frac{\Delta q_{t+1}}{q_t}}\end{align*}
$$

> **Interpretación de arbitraje financiero:** Para que la firma sea indiferente en el margen entre invertir en un bono financiero o invertir en una máquina, el rendimiento del bono (`$r$`) debe ser igual al rendimiento total del capital físico, el cual suma:
> 1. **El dividendo operacional neto por peso invertido:** `$\frac{PMgK_{t+1} - \delta}{q_t}$`.
> 2. **La tasa de ganancia de capital (valorización de `$q$`):** `$\frac{\Delta q_{t+1}}{q_t} = \frac{q_{t+1} - q_t}{q_t}$`.


Iteración Hacia Adelante y Valor Presente de la $q$ de Tobin
------------------------------------------------------------

A partir de la relación recursiva:

$$
\begin{align*}q_t = \frac{PMgK_{t+1} - \delta + q_{t+1}}{1 + r}\end{align*}
$$

sabemos que un período adelante se cumple:

$$
\begin{align*}q_{t+1} = \frac{PMgK_{t+2} - \delta + q_{t+2}}{1 + r}\end{align*}
$$

### Sustitución Sucesiva

Reemplazando `$q_{t+1}$` dentro de la ecuación de `$q_t$`:

$$
\begin{align*}q_t &= \frac{PMgK_{t+1} - \delta}{1 + r} + \frac{1}{1 + r} \left( \frac{PMgK_{t+2} - \delta + q_{t+2}}{1 + r} \right) \\ &= \frac{PMgK_{t+1} - \delta}{1 + r} + \frac{PMgK_{t+2} - \delta}{(1 + r)^2} + \frac{q_{t+2}}{(1 + r)^2}\end{align*}
$$

Sustituyendo un período más (`$q_{t+2}$`):

$$
\begin{align*}q_t = \frac{PMgK_{t+1} - \delta}{1 + r} + \frac{PMgK_{t+2} - \delta}{(1 + r)^2} + \frac{1}{(1 + r)^3} \Big( PMgK_{t+3} - \delta + q_{t+3} \Big)\end{align*}
$$

Al iterar `$N$` períodos hacia adelante, obtenemos la serie general:

$$
\begin{align*}q_t = \sum_{i=1}^N \frac{PMgK_{t+i} - \delta}{(1 + r)^i} + \frac{1}{(1 + r)^N} q_{t+N}\end{align*}
$$

### Condición de Transversalidad (No Burbujas Especulativas)

Cuando `$N \to \infty$`, como `$\lim_{N \to \infty} \frac{1}{(1 + r)^N} = 0$`, imponemos la condición de transversalidad para descartar burbujas especulativas en el valor del capital:

$$
\begin{align*}\lim_{N \to \infty} \frac{1}{(1 + r)^N} q_{t+N} = 0\end{align*}
$$

Con esto llegamos a la **expresión fundamental de la `$q$` de Tobin** (en certidumbre y bajo incertidumbre usando el operador de expectativas condicionales `$\mathbb{E}_t$`):

$$
\begin{align*}q_t = \sum_{i=1}^\infty \frac{PMgK_{t+i} - \delta}{(1 + r)^i} \qquad \implies \qquad \boxed{q_t = \mathbb{E}_t \left\{ \sum_{i=1}^\infty \frac{PMgK_{t+i} - \delta}{(1 + r)^i} \right\}}\end{align*}
$$

### Regla de Decisión de Inversión según $q_t$

Como `$q_t = 1 + C'(I_t)$` y `$C'(0) = 0$` con `$C'' > 0$`:
* **Si `$q_t > 1 \implies C'(I_t) > 0 \implies I_t > 0$`:** El valor presente de los beneficios marginales netos de una unidad de capital supera su costo de reposición. Conviene expandir el capital.
* **Si `$q_t = 1 \implies C'(I_t) = 0 \implies I_t = 0$`:** El stock de capital ha alcanzado su estado estacionario (`$PMgK = r + \delta$`).
* **Si `$q_t < 1 \implies C'(I_t) < 0 \implies I_t < 0$`:** El valor económico del capital es menor que su costo de reposición; la firma desinvierte.

> **Espacio para gráfica 1:** *Relación entre la `$q$` de Tobin y la inversión `$I_t$`.*
> En el plano `$(I_t, q_t)$`, se traza la curva creciente `$q_t = 1 + C'(I_t)$` que cruza el eje vertical en `$q_t = 1$` cuando `$I_t = 0$`, mostrando la zona de inversión positiva (`$q_t > 1$`) y la zona de desinversión (`$q_t < 1$`).
