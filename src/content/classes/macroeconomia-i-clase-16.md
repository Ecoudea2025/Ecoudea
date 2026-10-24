---
title: "Clase 16: Crecimiento Económico, Dinámica de la Relación Deuda/PIB y Sostenibilidad Fiscal"
course: "macroeconomia-i"
order: 16
classType: "clase"
description: "Efecto de la inflación e independencia del Banco Central, deducción paso a paso de la dinámica de la deuda como proporción del PIB, iteración en N períodos y condiciones de sostenibilidad fiscal."
math: true
---

---
---

Inflación, Deuda Real e Independencia del Banco Central
-------------------------------------------------------

En la clase anterior demostramos que, al incorporar el nivel general de precios `$P_t$` y la tasa de inflación `$\pi$`, la ley de movimiento de la deuda pública en términos reales (`$b_t \equiv \frac{B_t}{P_t}$`) viene dada por:

$$
\begin{align*}b_{t+1} = \frac{g_t - t_t}{1 + \pi} + (1 + r) b_t\end{align*}
$$

A partir de esta ecuación se observa que **la inflación reduce el valor real de la deuda pública**:

$$
\begin{align*}\Delta \pi \implies \nabla\left( \frac{g_t - t_t}{1 + \pi} \right), \quad \nabla b_t, \quad \nabla r \quad \implies \quad \nabla b_{t+1}\end{align*}
$$

### El Problema de Economía Política y el Rol del Banco Central

Debido a este mecanismo de licuación, **es de interés de algunos gobiernos generar o inducir altas inflaciones** para reducir el peso real de sus pasivos sin tener que recortar el gasto público (`$g_t$`) ni elevar los impuestos (`$t_t$`).

Sin embargo, en economías institucionalmente sólidas con un **Banco Central independiente**, la autoridad monetaria goza de autonomía técnica, legal y administrativa, y tiene el mandato de conducir la política monetaria con miras a reducir y controlar esa inflación creciente, impidiendo la monetización del déficit fiscal.


La Restricción Presupuestaria como Porcentaje del PIB
-----------------------------------------------------

Para evaluar si el endeudamiento de un país es manejable o excesivo, no basta con mirar el monto absoluto de la deuda real; debemos medir su tamaño en relación con la capacidad productiva de la economía, es decir, **como proporción del PIB real (`$Y_t$`)** (De Gregorio, Sección 5.3).

Definimos las variables reales del sistema:
* `$Y_t$`: PIB real de la economía en el período `$t$`.
* `$B_t$`: Deuda pública real vigente en `$t$`.
* `$r$`: Tasa de interés real constante.
* `$G_t$`: Gasto público primario real.
* `$T_t$`: Recaudo tributario real.
* `$\gamma_y$`: **Tasa de crecimiento del PIB real** entre `$t$` y `$t + 1$`:

$$
\begin{align*}Y_{t+1} = Y_t (1 + \gamma_y) \implies Y_t = \frac{Y_{t+1}}{1 + \gamma_y}\end{align*}
$$

### Deducción Paso a Paso de la Ecuación del Ratio Deuda/PIB

1. **Dividimos toda la ecuación de deuda real entre el PIB del período `$t$` (`$Y_t$`):**

$$
\begin{align*}\frac{B_{t+1}}{Y_t} = \frac{G_t - T_t}{Y_t} + (1 + r) \frac{B_t}{Y_t}\end{align*}
$$

2. **En el lado izquierdo, sustituimos `$Y_t = \frac{Y_{t+1}}{1 + \gamma_y}$`:**

$$
\begin{align*}\frac{B_{t+1}}{\frac{Y_{t+1}}{1 + \gamma_y}} = \frac{B_{t+1}(1 + \gamma_y)}{Y_{t+1}} = \frac{G_t - T_t}{Y_t} + (1 + r) \frac{B_t}{Y_t}\end{align*}
$$

3. **Definimos las variables en minúscula como proporciones del PIB:**
   * `$b_t \equiv \frac{B_t}{Y_t}$` y `$b_{t+1} \equiv \frac{B_{t+1}}{Y_{t+1}}$`: **Relación o ratio Deuda/PIB**.
   * `$g_t \equiv \frac{G_t}{Y_t}$`: **Tasa de gasto público** sobre el PIB.
   * `$t_t \equiv \frac{T_t}{Y_t}$`: **Tasa de recaudo tributario** (presión fiscal) sobre el PIB.

Reemplazando estas definiciones en nuestra ecuación:

$$
\begin{align*}b_{t+1}(1 + \gamma_y) = g_t - t_t + (1 + r) b_t\end{align*}
$$

4. **Dividimos ambos lados entre `$(1 + \gamma_y)$`:**

$$
\begin{align*}\boxed{b_{t+1} = \frac{g_t - t_t}{1 + \gamma_y} + \left( \frac{1 + r}{1 + \gamma_y} \right) b_t}\end{align*}
$$


Iteración Dinámica hacia Adelante ($N$ Períodos)
------------------------------------------------

Para estudiar la trayectoria temporal de `$b_t$`, asumimos que el déficit primario ajustado por crecimiento es constante y definimos dos parámetros auxiliares (`$\varphi$` y `$\rho$`):

$$
\begin{align*}\varphi \equiv \frac{g_t - t_t}{1 + \gamma_y} = \text{constante}, \qquad \qquad \rho \equiv \frac{1 + r}{1 + \gamma_y}\end{align*}
$$

Observemos que el valor del coeficiente autorregresivo `$\rho$` depende exclusivamente de la comparación entre la tasa de interés real (`$r$`) y la tasa de crecimiento económico (`$\gamma_y$`):

$$
\begin{align*}\rho = \frac{1 + r}{1 + \gamma_y} \implies \begin{cases} r = \gamma_y \implies \rho = 1 \\ r > \gamma_y \implies \rho > 1 \\ r < \gamma_y \implies \rho < 1 \end{cases}\end{align*}
$$

Con esta notación, la ecuación dinámica de primer orden toma la forma lineal:

$$
\begin{align*}b_{t+1} = \varphi + \rho b_t\end{align*}
$$

### Iteración Paso a Paso

* **En el período `$t + 2$`:**

$$
\begin{align*}b_{t+2} &= \varphi + \rho b_{t+1} \\ &= \varphi + \rho (\varphi + \rho b_t) \\ &= \varphi + \rho \varphi + \rho^2 b_t\end{align*}
$$

* **En el período `$t + 3$`:**

$$
\begin{align*}b_{t+3} &= \varphi + \rho b_{t+2} \\ &= \varphi + \rho (\varphi + \rho \varphi + \rho^2 b_t) \\ &= \varphi + \rho \varphi + \rho^2 \varphi + \rho^3 b_t = \left[ \sum_{i=1}^3 \varphi \rho^{i-1} \right] + \rho^3 b_t\end{align*}
$$

* **Generalización para `$N$` períodos hacia adelante:**

$$
\begin{align*}\boxed{b_{t+N} = \left[ \sum_{i=1}^N \varphi \rho^{i-1} \right] + \rho^N b_t}\end{align*}
$$


Análisis de los Tres Casos de Sostenibilidad Fiscal
---------------------------------------------------

Evaluamos el comportamiento asintótico de la deuda como proporción del PIB cuando el horizonte temporal se extiende hacia el largo plazo (`$N \to \infty$`):

### Caso 1: $\rho = 1 \iff r = \gamma_y$

Si la tasa de interés real iguala exactamente a la tasa de crecimiento del PIB (`$\rho = 1$`):

$$
\begin{align*}b_{t+N} = \sum_{i=1}^N \varphi (1)^{i-1} + (1)^N b_t = N \varphi + b_t\end{align*}
$$

Si el gobierno mantiene un déficit primario positivo (`$\varphi > 0$`), a medida que `$N \to \infty$` la relación Deuda/PIB crece de forma lineal e ilimitada (`$b_{t+N} \to \infty$`).

### Caso 2: $\rho > 1 \iff r > \gamma_y$ (Trayectoria Explosiva)

Si la tasa de interés real supera al crecimiento de la economía (`$r > \gamma_y \implies \rho > 1$`):

$$
\begin{align*}b_{t+N} = \sum_{i=1}^N \varphi \rho^{i-1} + \rho^N b_t\end{align*}
$$

Cuando `$N \to \infty$`, el término exponencial `$\rho^N$` diverge hacia infinito (`$\rho^N \to \infty$`). Con un déficit primario positivo o nulo, **`$b_{t+N}$` sigue una trayectoria explosiva e insostenible**. Como señala De Gregorio (Sección 5.3), cuando `$r > \gamma_y$`, la única manera de estabilizar la deuda en un nivel constante es generando un **superávit primario** (`$t_t > g_t$`) suficiente para pagar el exceso de intereses sobre el crecimiento.

### Caso 3: $\rho < 1 \iff r < \gamma_y$ (Convergencia y Sostenibilidad)

Si la economía crece a un ritmo superior a la tasa de interés real (`$\gamma_y > r \implies 0 < \rho < 1$`):

1. **El término inicial amortizado desaparece en el límite:**

$$
\begin{align*}\lim_{N \to \infty} \rho^N = 0 \implies \lim_{N \to \infty} \rho^N b_t = 0\end{align*}
$$

2. **La serie geométrica converge a un valor finito:**

Aplicando la fórmula de la suma geométrica que demostramos en la Clase 10:

$$
\begin{align*}\sum_{i=1}^N \varphi \rho^{i-1} = \varphi \sum_{i=1}^N \rho^{i-1} = \frac{\varphi (1 - \rho^N)}{1 - \rho} \xrightarrow{N \to \infty} \frac{\varphi}{1 - \rho}\end{align*}
$$

Por lo tanto, cuando `$N \to \infty$`, la relación Deuda/PIB converge a un **estado estacionario finito**:

$$
\begin{align*}\lim_{N \to \infty} b_{t+N} = \frac{\varphi}{1 - \rho} + 0 = \boxed{\frac{\varphi}{1 - \rho}} \quad \text{(Finita)}\end{align*}
$$


Deducción del Nivel de Deuda/PIB Sostenible ($\bar{b}$)
-------------------------------------------------------

Cuando se cumple la condición de estabilidad (`$b_{t+1} = b_t = b_{t-1} = \ldots = \bar{b}$`), sustituimos las definiciones estructurales de `$\varphi = \frac{g_t - t_t}{1 + \gamma_y}$` y `$\rho = \frac{1 + r}{1 + \gamma_y}$` en la expresión de estado estacionario:

$$
\begin{align*}\bar{b} = \frac{\varphi}{1 - \rho} = \frac{\dfrac{g_t - t_t}{1 + \gamma_y}}{1 - \dfrac{1 + r}{1 + \gamma_y}}\end{align*}
$$

Resolvemos la resta de fracciones en el denominador:

$$
\begin{align*}1 - \frac{1 + r}{1 + \gamma_y} = \frac{1 + \gamma_y - 1 - r}{1 + \gamma_y} = \frac{\gamma_y - r}{1 + \gamma_y}\end{align*}
$$

Reemplazando en la ecuación de `$\bar{b}$` y cancelando los denominadores `$(1 + \gamma_y)$`:

$$
\begin{align*}\bar{b} = \frac{(g_t - t_t) / \cancel{(1 + \gamma_y)}}{(\gamma_y - r) / \cancel{(1 + \gamma_y)}} \implies \boxed{\bar{b} = \frac{g_t - t_t}{\gamma_y - r} = -\frac{g_t - t_t}{r - \gamma_y}}\end{align*}
$$

### Interpretación Económica de $\bar{b}$

1. **Cuando `$\gamma_y > r$`:** El crecimiento económico "paga" por sí mismo parte del servicio de la deuda, permitiendo sostener un nivel positivo de deuda estacionaria `$\bar{b} > 0$` incluso con un déficit primario moderado (`$g_t > t_t$`).
2. **Cuando `$r > \gamma_y$` (el caso habitual de largo plazo en De Gregorio):** Como el denominador `$r - \gamma_y > 0$`, para sostener una deuda positiva `$\bar{b} > 0$` sin que explote se requiere obligatoriamente que `$g_t - t_t < 0$`, es decir, generar un **superávit primario permanente** igual a:

$$
\begin{align*}t_t - g_t = (r - \gamma_y) \bar{b}\end{align*}
$$

| Régimen Dinámico | Relación de Tasas | Factor $\rho = \frac{1+r}{1+\gamma_y}$ | Trayectoria de $b_{t+N}$ (con $g_t > t_t$) | Condición para Estabilizar $\bar{b} > 0$ |
| :--- | :---: | :---: | :--- | :--- |
| **Crecimiento alto** | `$\gamma_y > r$` | `$\rho < 1$` | Converge a `$\bar{b} = \frac{g_t - t_t}{\gamma_y - r}$` | Compatible con déficit primario acotado |
| **Caso frontera** | `$\gamma_y = r$` | `$\rho = 1$` | Crecimiento lineal `$N\varphi + b_t$` | Exige equilibrio primario (`$g_t = t_t$`) |
| **Interés alto** | `$r > \gamma_y$` | `$\rho > 1$` | **Explosiva** (`$\rho^N \to \infty$`) | Exige **superávit primario** `$t_t - g_t = (r - \gamma_y)\bar{b}$` |

> **Espacio para gráfica 1:** *Trayectorias dinámicas de la relación Deuda/PIB (`$b_t$`) según `$\rho \gtreqless 1$`.*
> En el plano `$(t, b_t)$`, se traza la línea horizontal de estado estacionario `$\bar{b}_0$`, mostrando la curva convergente cuando `$\frac{1+r}{1+\gamma_y} < 1$` (`$\gamma_y > r$`) y la curva divergente/explosiva hacia arriba cuando `$\frac{1+r}{1+\gamma_y} > 1$` (`$r > \gamma_y$`).
