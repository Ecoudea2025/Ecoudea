---
title: "Clase 08: Choques Transitorios, Permanentes y bajo Incertidumbre con Descuento Financiero"
course: "macroeconomia-i"
order: 8
classType: "clase"
description: "Comparación analítica de choques futuros de ingreso, diferencial total ante choques permanentes, efecto sobre el ahorro y modelación del cambio esperado en el consumo bajo incertidumbre."
math: true
---

---
---

Sensibilidad del Consumo ante Ingresos Futuros ($r > 0$)
--------------------------------------------------------

Partimos de la solución óptima para el consumo en el período 1 cuando el individuo planifica en un horizonte de `$N$` períodos con una tasa de interés real positiva (`$r > 0$`):

$$
\begin{align*}C_1^* = \alpha_1 \left\{ Y_1 + \frac{Y_2}{1 + r} + \frac{Y_3}{(1 + r)^2} + \ldots + \frac{Y_N}{(1 + r)^{N - 1}} \right\}\end{align*}
$$

A partir de esta expresión general, nos planteamos dos preguntas fundamentales:
1. ¿Cómo reacciona el consumo presente ante aumentos transitorios del ingreso en diferentes momentos futuros (por ejemplo, en `$t = 3$` frente a `$t = 6$`)?
2. ¿Cómo cambia la respuesta cuando el aumento del ingreso ocurre simultáneamente en todos los períodos (`$\Delta Y_i = \Delta \bar{Y}$`)?


1. Comparación de Choques Transitorios en Distintos Períodos
------------------------------------------------------------

Calculemos las derivadas parciales de `$C_1^*$` respecto al ingreso del período 3 (`$Y_3$`) y respecto al ingreso del período 6 (`$Y_6$`):

$$
\begin{align*}\frac{\partial C_1^*}{\partial Y_3} = \alpha_1 \frac{1}{(1 + r)^2} > 0, \qquad \frac{\partial C_1^*}{\partial Y_6} = \alpha_1 \frac{1}{(1 + r)^5} > 0\end{align*}
$$

Estas derivadas representan las **propensiones marginales a consumir hoy** ante un incremento futuro en el período 3 (`$PMgC_{1, 3}$`) y en el período 6 (`$PMgC_{1, 6}$`).

Dado que `$r > 0$`, el denominador crece exponencialmente con el tiempo (`$(1 + r)^2 < (1 + r)^5$`), lo que implica:

$$
\begin{align*}\frac{\alpha_1}{(1 + r)^2} > \frac{\alpha_1}{(1 + r)^5} \implies PMgC_{1, 3} > PMgC_{1, 6}\end{align*}
$$

> **Intuición económica:** Ambos choques futuros aumentan el consumo hoy porque elevan la riqueza humana del agente. Sin embargo, un ingreso adicional en el período 6 sufre un castigo por descuento financiero mucho mayor (`$5$` períodos de descuento) que un ingreso en el período 3 (`$2$` períodos de descuento). En general, se cumple la jerarquía estricta:
> $$\alpha_1 > \frac{\alpha_1}{1 + r} > \frac{\alpha_1}{(1 + r)^2} > \ldots > \frac{\alpha_1}{(1 + r)^{N - 1}}$$

### Impacto sobre el Ahorro Corriente ($S_1$)

Recordemos que el ahorro en el primer período se define como:

$$
\begin{align*}S_1 = Y_1 - C_1^*\end{align*}
$$

Analicemos qué ocurre con el ahorro hoy cuando aumenta el ingreso futuro (`$Y_3$` o `$Y_6$`), manteniendo constante el ingreso corriente `$Y_1$`:

$$
\begin{align*}\frac{\partial S_1}{\partial Y_3} &= \frac{\partial Y_1}{\partial Y_3} - \frac{\partial C_1^*}{\partial Y_3} = 0 - \frac{\alpha_1}{(1 + r)^2} = -\frac{\alpha_1}{(1 + r)^2} < 0 \\ \frac{\partial S_1}{\partial Y_6} &= -\frac{\partial C_1^*}{\partial Y_6} = -\frac{\alpha_1}{(1 + r)^5} < 0\end{align*}
$$

En contraste, si el aumento ocurre en el **ingreso presente (`$Y_1$`)**:

$$
\begin{align*}\frac{\partial S_1}{\partial Y_1} = 1 - \frac{\partial C_1^*}{\partial Y_1} = 1 - \alpha_1 > 0 \quad (\text{dado que } 0 < \alpha_1 < 1)\end{align*}
$$

* **Si sube el ingreso hoy (`$\Delta Y_1 > 0$`):** El ahorro corriente **aumenta**, porque el individuo guarda una fracción `$1 - \alpha_1$` para financiar el futuro.
* **Si se anuncia que subirá el ingreso mañana (`$\Delta Y_3 > 0$`):** El ahorro corriente **disminuye** (o el endeudamiento aumenta), porque el individuo anticipa su mayor riqueza futura y empieza a disfrutarla desde hoy reduciendo su esfuerzo de ahorro presente.


2. Choque Permanente en Todos los Períodos ($\Delta Y_i = \Delta \bar{Y}$)
--------------------------------------------------------------------------

Supongamos ahora que el ingreso aumenta en la misma cuantía en todos los períodos (`$\text{d}Y_1 = \text{d}Y_2 = \ldots = \text{d}Y_N = \text{d}\bar{Y}$`). Aplicamos la fórmula del **diferencial total** para una función de varias variables `$Y = F(X_1, X_2, \ldots, X_N)$`:

$$
\begin{align*}\text{d}Y = \sum_{i=1}^N \frac{\partial F(\cdot)}{\partial X_i} \text{d}X_i\end{align*}
$$

Aplicando el diferencial total a `$C_1^*$` cuando todos los ingresos varían en `$\text{d}\bar{Y}$`:

$$
\begin{align*}\text{d}C_1^* = \alpha_1 \left( 1 + \frac{1}{1 + r} + \frac{1}{(1 + r)^2} + \ldots + \frac{1}{(1 + r)^{N - 1}} \right) \text{d}\bar{Y}\end{align*}
$$

Dividiendo por `$\text{d}\bar{Y}$` y expresando la suma en notación compacta:

$$
\begin{align*}\frac{\text{d}C_1^*}{\text{d}\bar{Y}} = \alpha_1 \sum_{i=1}^N \frac{1}{(1 + r)^{i - 1}}\end{align*}
$$

Definamos el factor acumulado de actualización como `$\phi$`:

$$
\begin{align*}\phi \equiv \sum_{i=1}^N \frac{1}{(1 + r)^{i - 1}} = 1 + \frac{1}{1 + r} + \ldots + \frac{1}{(1 + r)^{N - 1}} > 1\end{align*}
$$

Dado que el primer término de la suma es `$1$` y todos los términos siguientes son estrictamente positivos, se garantiza que `$\phi > 1$`. Así, podemos comparar directamente ambas propensiones marginales:

* **Propensión marginal a consumir del ingreso transitorio (en el período `$i$`):**

$$
\begin{align*}\left. \frac{\text{d}C_1^*}{\text{d}Y_i} \right|_{i = 1, \ldots, N} = \frac{\alpha_1}{(1 + r)^{i - 1}}\end{align*}
$$

* **Propensión marginal a consumir del ingreso permanente:**

$$
\begin{align*}\frac{\text{d}C_1^*}{\text{d}\bar{Y}} = \alpha_1 \phi\end{align*}
$$

Como `$\phi > 1 \geq \frac{1}{(1 + r)^{i - 1}}$`, concluimos rigurosamente que:

$$
\begin{align*}\frac{\text{d}C_1^*}{\text{d}\bar{Y}} > \frac{\text{d}C_1^*}{\text{d}Y_1} > \frac{\text{d}C_1^*}{\text{d}Y_3} > \frac{\text{d}C_1^*}{\text{d}Y_6}\end{align*}
$$

El ingreso permanente induce grandes cambios en el consumo presente, mientras que el ingreso transitorio induce cambios de mucha menor magnitud.


3. Choques de Ingreso bajo Incertidumbre ($q$ y $1 - q$)
--------------------------------------------------------

En la vida real, cuando un hogar recibe un aumento en su ingreso hoy, rara vez tiene certeza absoluta de si ese aumento será efímero o duradero.

Supongamos que ante un choque de ingreso existen dos estados de la naturaleza posibles:
* Con probabilidad **`$q \in [0, 1]$`**, el choque es **transitorio** (afecta únicamente al ingreso del primer período, `$Y_1$`).
* Con probabilidad **`$(1 - q)$`**, el choque es **permanente** (afecta a todos los períodos `$Y_1, Y_2, \ldots, Y_N$`).

### Valor Esperado del Cambio en el Consumo

Por definición estadística, el valor esperado de una variable aleatoria discreta con dos estados es:

$$
\begin{align*}\mathbb{E}(X) = P(x_1) X_1 + \big( 1 - P(x_1) \big) X_2\end{align*}
$$

Sabemos que la respuesta del consumo en cada estado es:
1. Si el choque es transitorio (solo en `$Y_1$`): `$\frac{\partial C_1^*}{\partial Y_1} = \alpha_1$`.
2. Si el choque es permanente (en todos los `$Y_t$`): `$\frac{\text{d}C_1^*}{\text{d}\bar{Y}} = \alpha_1 \sum_{i=1}^N \frac{1}{(1 + r)^{i - 1}} = \alpha_1 \phi$`.

Por lo tanto, el **valor esperado de la respuesta marginal del consumo** es la combinación lineal ponderada por las probabilidades `$q$` y `$(1 - q)$`:

$$
\begin{align*}\mathbb{E}\left[ \frac{\text{d}C_1^*}{\text{d}Y} \right] = q \alpha_1 + (1 - q) \alpha_1 \sum_{i=1}^N \frac{1}{(1 + r)^{i - 1}}\end{align*}
$$

Factorizando `$\alpha_1$` y sustituyendo `$\phi$`:

$$
\begin{align*}\mathbb{E}\left[ \frac{\text{d}C_1^*}{\text{d}Y} \right] = \alpha_1 \Big( q + (1 - q)\phi \Big)\end{align*}
$$

| Valor de la probabilidad `$q$` | Percepción del Agente | Respuesta Esperada $\mathbb{E}[\text{d}C_1^*/\text{d}Y]$ | Magnitud del Efecto |
| :--- | :--- | :--- | :--- |
| **`$q \to 1$`** (Muy grande) | Choque puramente transitorio | `$\alpha_1$` | Mínima (se ahorra casi todo) |
| **`$q \in (0, 1)$`** (Intermedio) | Incertidumbre mixta | `$\alpha_1(q + (1 - q)\phi)$` | Ponderada por credibilidad |
| **`$q \to 0$`** (Muy pequeño) | Choque puramente permanente | `$\alpha_1 \phi$` | Máxima (fuerte expansión de `$C_1^*$`) |

> **Espacio para gráfica 1:** *Respuesta marginal esperada del consumo en función de la probabilidad de transitoriedad `$q$`.*
> En el plano `$(q, \mathbb{E}[\text{d}C_1^*/\text{d}Y])$` con `$q \in [0, 1]$`, se traza una línea recta con pendiente negativa que parte del valor máximo `$\alpha_1 \phi$` cuando `$q = 0$` (choque permanente) y desciende hasta el valor mínimo `$\alpha_1$` cuando `$q = 1$` (choque transitorio).
