---
title: "Clase 05: Función de Utilidad CRRA, Desigualdad de Jensen y Consumo Óptimo"
course: "macroeconomia-i"
order: 5
classType: "clase"
description: "Análisis geométrico y analítico de la función CRRA, aversión al riesgo mediante la Desigualdad de Jensen, límite de L'Hôpital y deducción de la función de consumo óptimo."
math: true
---


Geometría de la Concavidad y Desigualdad de Jensen
--------------------------------------------------

En la teoría macroeconómica del consumo, la forma de la función de utilidad instantánea `$u(C_t)$` encierra toda la información sobre cómo reaccionan las familias frente a la incertidumbre y frente a las fluctuaciones de su ingreso a lo largo del tiempo.

Sabemos que toda función de utilidad estándar cumple dos axiomas:

$$
\begin{align*}\frac{\partial u}{\partial C} > 0 \quad (\text{No saciación}), \qquad \frac{\partial^2 u}{\partial C^2} < 0 \quad (\text{Utilidad marginal decreciente})\end{align*}
$$

### Combinación Convexa y Desigualdad de Jensen

Supongamos dos niveles distintos de consumo, un estado bajo `$C_1$` y un estado alto `$C_2$`, y definamos una **combinación lineal convexa** (un promedio ponderado) entre ambos:

$$
\begin{align*}\bar{C} = \lambda C_1 + (1 - \lambda) C_2, \quad \text{con } \lambda \in (0, 1)\end{align*}
$$

Por su parte, la utilidad promedio esperada (ubicada sobre la cuerda recta que une los puntos `$(C_1, u(C_1))$` y `$(C_2, u(C_2))$`) viene dada por:

$$
\begin{align*}\bar{u}(C_t) = \lambda u(C_1) + (1 - \lambda) u(C_2)\end{align*}
$$

Debido a que la función `$u(C_t)$` es estrictamente cóncava (`$\frac{\partial^2 u}{\partial C^2} < 0$`), la curva de la función siempre pasa por encima de la cuerda secante. Formalmente, esto se conoce como la **Desigualdad de Jensen**:

$$
\begin{align*}u(\bar{C}) > \lambda u(C_1) + (1 - \lambda) u(C_2) \equiv \bar{u}(C_t)\end{align*}
$$

> **Espacio para gráfica 1:** *Desigualdad de Jensen y concavidad de la función de utilidad `$u(C_t)$`.*
> En el eje horizontal se ubican `$C_1$`, `$\bar{C} = \lambda C_1 + (1-\lambda)C_2$` y `$C_2$`. Se traza la curva roja cóncava `$u(C_t)$` y la cuerda verde lineal que une `$(C_1, u(C_1))$` con `$(C_2, u(C_2))$`. En la vertical sobre `$\bar{C}$`, se señala cómo la altura hasta la curva roja `$u(\bar{C})$` supera estrictamente a la altura hasta la cuerda verde `$\lambda u(C_1) + (1-\lambda)u(C_2)$`.

### ¿Riesgo de qué? Actitudes frente al Riesgo y Suavizamiento

En macroeconomía intertemporal, decir que el consumidor es **averso al riesgo** significa que rechaza enfrentar **oscilaciones fuertes o saltos bruscos en su senda de consumo** (y, por consiguiente, en su utilidad). Prefiere consumir una cantidad estable `$\bar{C}$` en todos los períodos antes que alternar entre períodos de abundancia (`$C_2$`) y períodos de escasez (`$C_1$`).

Podemos clasificar a los agentes económicos según la curvatura de `$u(C_t)$`:

| Tipo de Agente | Relación de Jensen | Derivada Segunda | Implicación Intertemporal |
| :--- | :--- | :--- | :--- |
| **Averso al riesgo** | `$u(\bar{C}) > \bar{u}(C_t)$` | `$u''(C) < 0$` (Cóncava) | Desea suavizar el consumo en el tiempo |
| **Neutral al riesgo** | `$u(\bar{C}) = \bar{u}(C_t)$` | `$u''(C) = 0$` (Lineal) | Indiferente ante saltos bruscos del consumo |
| **Amante del riesgo** | `$u(\bar{C}) < \bar{u}(C_t)$` | `$u''(C) > 0$` (Convexa) | Prefiere concentrar el consumo en extremos |


La Función CRRA (Constant Relative Risk Aversion)
-------------------------------------------------

Para parametrizar de forma exacta el grado de concavidad subjetiva, utilizamos la **función de utilidad instantánea CRRA**:

$$
\begin{align*}u(C_t) = \frac{C_t^{1 - \sigma} - 1}{1 - \sigma}\end{align*}
$$

Al integrarla en un horizonte temporal de `$T$` períodos (o infinito), obtenemos la **función de utilidad intertemporal separable**:

$$
\begin{align*}V = \frac{C_1^{1 - \sigma} - 1}{1 - \sigma} + \beta \frac{C_2^{1 - \sigma} - 1}{1 - \sigma} + \beta^2 \frac{C_3^{1 - \sigma} - 1}{1 - \sigma} + \ldots = \sum_{i=0}^\infty \beta^i u(C_{t+i})\end{align*}
$$

### Propiedades Analíticas de la Función CRRA

1. **Primera derivada (Utilidad Marginal Positiva):**

$$
\begin{align*}\frac{\partial u(C_t)}{\partial C_t} = (1 - \sigma) \frac{C_t^{(1 - \sigma) - 1}}{1 - \sigma} = C_t^{-\sigma} > 0, \quad \forall C_t > 0\end{align*}
$$

2. **Segunda derivada (Concavidad Estricta):**

$$
\begin{align*}\frac{\partial^2 u(C_t)}{\partial C_t^2} = -\sigma C_t^{-\sigma - 1} < 0, \quad \forall C_t > 0 \iff \sigma > 0\end{align*}
$$

Cuanto mayor sea el parámetro `$\sigma$`, más negativa es la segunda derivada, más curvada es la función de utilidad y **mayor es el deseo del individuo por suavizar su consumo**.

### El Papel de la Constante $-1$ y el Caso $\sigma = 1$ (Regla de L'Hôpital)

Observemos que algebraicamente podemos separar la fracción como:

$$
\begin{align*}\frac{C_t^{1 - \sigma} - 1}{1 - \sigma} = \left[ \frac{C_t^{1 - \sigma}}{1 - \sigma} \right] - \left( \frac{1}{1 - \sigma} \right)\end{align*}
$$

En problemas donde `$\sigma \neq 1$`, el término constante `$-\frac{1}{1-\sigma}$` desaparece al derivar respecto a `$C_t$`. Sin embargo, restar `$1$` en el numerador es indispensable para evaluar qué ocurre en el límite cuando `$\sigma \to 1$`.

Si sustituimos directamente `$\sigma = 1$`, obtenemos una indeterminación:

$$
\begin{align*}\lim_{\sigma \to 1} \frac{C_t^{1 - \sigma} - 1}{1 - \sigma} = \frac{C_t^0 - 1}{1 - 1} = \frac{0}{0}\end{align*}
$$

**Demostración paso a paso mediante la Regla de L'Hôpital:**

1. Reescribimos `$C_t^{1-\sigma}$` utilizando la identidad exponencial-logarítmica `$x = e^{\ln(x)}$`:

$$
\begin{align*}\frac{C_t^{1 - \sigma} - 1}{1 - \sigma} = \frac{e^{\ln(C_t^{1 - \sigma})} - 1}{1 - \sigma} = \frac{e^{(1 - \sigma) \ln C_t} - 1}{1 - \sigma}\end{align*}
$$

2. Derivamos el numerador y el denominador **respecto al parámetro `$\sigma$`** (recordando que `$C_t$` actúa aquí como constante):

$$
\begin{align*}\frac{\partial \left( e^{(1 - \sigma) \ln C_t} - 1 \right)}{\partial \sigma} &= -\ln C_t \cdot e^{(1 - \sigma) \ln C_t} \\ \frac{\partial (1 - \sigma)}{\partial \sigma} &= -1\end{align*}
$$

3. Evaluamos el límite del cociente de las derivadas cuando `$\sigma \to 1$`:

$$
\begin{align*}\lim_{\sigma \to 1} \frac{-\ln C_t \cdot e^{(1 - \sigma) \ln C_t}}{-1} = \frac{-\ln C_t \cdot e^{0 \cdot \ln C_t}}{-1} = \ln C_t\end{align*}
$$

De esta forma, la familia completa de utilidad instantánea CRRA queda definida como:

$$
\begin{align*}u(C_t) = \begin{cases} \dfrac{C_t^{1 - \sigma} - 1}{1 - \sigma}, & \forall \sigma > 0, \; \sigma \neq 1 \\[8pt] \ln C_t, & \text{si } \sigma = 1 \end{cases}\end{align*}
$$


Deducción Paso a Paso del Consumo Óptimo con Utilidad CRRA
----------------------------------------------------------

Consideremos una economía de dos períodos (`$t = 1, 2$`) donde el individuo resuelve:

$$
\begin{align*}\max_{\{C_1, C_2\}} \quad & U = \frac{C_1^{1 - \sigma}}{1 - \sigma} + \beta \frac{C_2^{1 - \sigma}}{1 - \sigma} \\ \text{s.a.} \quad & C_1 + \frac{C_2}{1 + r} = Y_1 + \frac{Y_2}{1 + r}\end{align*}
$$

### Paso 1: Planteamiento del Lagrangiano y C.P.O.

$$
\begin{align*}\mathcal{L} = \frac{C_1^{1 - \sigma}}{1 - \sigma} + \beta \frac{C_2^{1 - \sigma}}{1 - \sigma} + \lambda \left[ Y_1 + \frac{Y_2}{1 + r} - C_1 - \frac{C_2}{1 + r} \right]\end{align*}
$$

Derivando respecto a `$C_1$` y `$C_2$`:

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_1} &= C_1^{-\sigma} - \lambda = 0 \implies \lambda = C_1^{-\sigma} \\ \frac{\partial \mathcal{L}}{\partial C_2} &= \beta C_2^{-\sigma} - \frac{\lambda}{1 + r} = 0 \implies \beta C_2^{-\sigma} = \frac{\lambda}{1 + r}\end{align*}
$$

### Paso 2: Ecuación de Euler y Despeje de $C_2$

Sustituyendo `$\lambda = C_1^{-\sigma}$` en la segunda condición:

$$
\begin{align*}\beta C_2^{-\sigma} = \frac{C_1^{-\sigma}}{1 + r} \implies C_2^{-\sigma} = \frac{C_1^{-\sigma}}{\beta (1 + r)}\end{align*}
$$

Elevamos ambos lados de la ecuación a la potencia `$-\frac{1}{\sigma}$` para despejar `$C_2$`:

$$
\begin{align*}\left( C_2^{-\sigma} \right)^{-\frac{1}{\sigma}} &= \left( \frac{C_1^{-\sigma}}{\beta (1 + r)} \right)^{-\frac{1}{\sigma}} \\ C_2 &= C_1 (1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}}\end{align*}
$$

### Paso 3: Sustitución en la R.P.I. para Encontrar $C_1^*$

Reemplazamos la relación óptima de `$C_2$` en la restricción presupuestaria intertemporal:

$$
\begin{align*}C_1 + \frac{C_1 (1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}}}{1 + r} = Y_1 + \frac{Y_2}{1 + r}\end{align*}
$$

Factorizamos `$C_1$` en el lado izquierdo:

$$
\begin{align*}C_1 \left( 1 + \frac{(1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}}}{1 + r} \right) = Y_1 + \frac{Y_2}{1 + r}\end{align*}
$$

Despejando `$C_1$`, obtenemos la **función explícita de consumo óptimo en el período 1**:

$$
\begin{align*}C_1^* = \left[ Y_1 + \frac{Y_2}{1 + r} \right] \left( 1 + \frac{(1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}}}{1 + r} \right)^{-1}\end{align*}
$$


Introducción a la Sensibilidad frente a la Tasa de Interés
----------------------------------------------------------

Una vez hallada la forma cerrada de `$C_1^*$`, surge la pregunta central de política macroeconómica: **¿Qué efecto tiene un aumento en la tasa de interés `$r$` sobre el consumo presente `$C_1^*$`?**

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} \gtreqless 0 \quad \implies \quad \text{Depende críticamente del valor de } \sigma\end{align*}
$$

Veamos inicialmente el caso particular cuando **`$\sigma = 1$`** (utilidad logarítmica). Al evaluar `$\sigma = 1$` en la expresión de `$C_1^*$`, el término `$\frac{(1+r)^1 \beta^1}{1+r}$` se simplifica a `$\beta$`:

$$
\begin{align*}C_1^* = \left[ Y_1 + \frac{Y_2}{1 + r} \right] (1 + \beta)^{-1} = \left( Y_1 + \frac{Y_2}{1 + r} \right) \frac{1}{1 + \beta}\end{align*}
$$

Si derivamos respecto a `$r$` (asumiendo `$Y_2 > 0$`):

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -\frac{Y_2}{(1 + r)^2 (1 + \beta)} < 0\end{align*}
$$

Cuando `$\sigma = 1$` y existen ingresos futuros (`$Y_2 > 0$`), un alza en `$r$` reduce el consumo presente (`$\Delta r \implies \nabla C_1^*$`) y eleva el ahorro (`$\Delta S_1^*$`), debido a la caída en el valor presente de `$Y_2$`. En la siguiente clase resolveremos analíticamente la derivada general para todos los valores posibles de `$\sigma$`.
