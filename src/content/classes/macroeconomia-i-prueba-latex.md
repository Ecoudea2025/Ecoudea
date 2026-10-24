---
title: "Prueba de tortura LaTeX"
course: "macroeconomia-i"
order: 999
classType: "clase"
description: "Página interna de pruebas extremas (borrador, no se publica)."
math: true
draft: true
---

## Bloques teóricos

:::definicion Preferencias racionales
Una relación de preferencias $\succeq$ sobre $X$ es **racional** si es completa y transitiva. Con $\E[X] = \sum_x x \Prob(X = x)$ medimos la esperanza.
:::

:::teorema Representación de la utilidad
Si $\succeq$ es racional y continua, existe $u: X \to \R$ tal que $x \succeq y \iff u(x) \geq u(y)$.
:::

:::lema Continuidad
Todo subconjunto cerrado y acotado de $\R^n$ es compacto.
:::

:::demostracion
Por Heine-Borel, directa.
:::

:::ejemplo Cálculo de elasticidad
Con $Q = 10 - 2P$, la elasticidad precio es $\varepsilon = \frac{\dd Q}{\dd P}\frac{P}{Q}$.
:::

:::ejercicio Maximización
Resuelve $\argmax_{x \geq 0} u(x)$ sujeto a $px \leq m$.
:::

:::ideaclave
La restricción manda: sin precios no hay elección.
:::

:::nota
Los axiomas fallan con el paradox de Allais.
:::

:::advertencia
No confundas $\Var(X)$ con $\E[X^2]$: recuerda que $\Var(X) = \E[X^2] - \E[X]^2$.
:::

:::intuicion
Piensa en la utilidad marginal como el último bocado: cada vez satisface menos.
:::

## Fórmulas extremas

Ecuación larga (debe scrollear sin romper la página):

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \xb)(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \xb)^2} + \frac{\sum_{i=1}^{n}(x_i - \xb)(\varepsilon_i - \bar{\varepsilon})}{\sum_{i=1}^{n}(x_i - \xb)^2} + \text{término de corrección por heteroscedasticidad robusta}
$$

Sistema con `aligned` y `cases`:

$$
\begin{aligned}
\max_{x,y} \quad & u(x, y) = x^{\alpha}y^{1-\alpha} \\
\text{s.a.} \quad & p_x x + p_y y = m
\end{aligned}
\qquad
D(p) =
\begin{cases}
10 - 2p & \text{si } p < 5 \\
0 & \text{si } p \geq 5
\end{cases}
$$

Matriz grande:

$$
\Sigma =
\begin{pmatrix}
\sigma_1^2 & \rho_{12}\sigma_1\sigma_2 & \rho_{13}\sigma_1\sigma_3 \\
\rho_{12}\sigma_1\sigma_2 & \sigma_2^2 & \rho_{23}\sigma_2\sigma_3 \\
\rho_{13}\sigma_1\sigma_3 & \rho_{23}\sigma_2\sigma_3 & \sigma_3^2
\end{pmatrix}
$$

Ecuación numerada con `tag`:

$$
\E[\bar{X}] = \mu \tag{1}
$$

Inline con macros: $\Var(\bar{X}) = \sigma^2/n$, variables $\iid$, reales $\R$, naturales $\N$.

## Tabla ancha y código

| Parámetro | Símbolo | Estimador | Varianza | IC 95% | Notas |
|---|---|---|---|---|---|
| Media | $\mu$ | $\bar{x}$ | $s^2/n$ | $\bar{x} \pm 1.96 s/\sqrt{n}$ | robusto |
| Varianza | $\sigma^2$ | $s^2$ | $2\sigma^4/(n-1)$ | ajustado | sesgo leve |

```python
import numpy as np
x = np.linspace(0, 10, 200)
```

## Colapsable nativo y nota al pie

<details>
<summary>Demostración completa (clic para expandir)</summary>

Contenido colapsable sin JavaScript: funciona con teclado y lector de pantalla.

</details>

Una afirmación con nota al pie.[^1]

[^1]: Esta es la nota al pie de prueba.
