---
title: "Clase 02: Condición de Transversalidad y Preferencias Intertemporales"
course: "macroeconomia-i"
order: 2
classType: "clase"
description: "Condición de no-Ponzi, consolidación de la restricción intertemporal, modelación de preferencias aditivas y tasa subjetiva de descuento."
math: true
---

---
---

La Condición de Transversalidad y el Esquema de No-Ponzi
--------------------------------------------------------

En la clase anterior dedujimos la restricción presupuestaria intertemporal tras iterar `$N$` períodos hacia adelante:

$$
\begin{align*}\sum_{i=0}^N \frac{C_{t+i}}{(1 + r)^i} + \frac{A_{t+N+1}}{(1 + r)^N} = (1 + r)A_t + \sum_{i=0}^N \frac{Y_{\ell t+i} - T_{t+i}}{(1 + r)^i}\end{align*}
$$

donde hemos incorporado los impuestos netos de transferencias `$T_{t+i}$`. 

Para cerrar formalmente el modelo, debemos determinar el valor económico del término terminal:

$$
\begin{align*}\frac{A_{t+N+1}}{(1 + r)^N}\end{align*}
$$

### Caso 1: Horizonte de Vida Finito

Supongamos que el individuo vive exactamente hasta el período `$t+N$` y no experimenta motivaciones altruistas (no deja herencias voluntarias).

1. **No es óptimo dejar activos positivos (`$A_{t+N+1} > 0$`):** Por el axioma de no saciación de las preferencias, más consumo siempre genera mayor utilidad. Si el individuo muriera con `$A_{t+N+1} > 0$`, habría sacrificado consumo a lo largo de su vida de forma inútil.
2. **No es factible dejar deudas (`$A_{t+N+1} < 0$`):** Ningún prestamista racional extenderá crédito a un individuo en su último período de vida si sabe que fallecerá sin saldar su saldo deudor.

Por lo tanto, la condición de frontera natural exige que los activos al final de la vida sean exactamente cero:

$$
\begin{align*}A_{t+N+1} = 0 \implies \frac{A_{t+N+1}}{(1 + r)^N} = 0\end{align*}
$$

### Caso 2: Horizonte Infinito y la Condición de No-Ponzi

Cuando el horizonte temporal es infinito (`$N \to \infty$`), como ocurre en familias dinásticas que cuidan el bienestar de sus descendientes, surge la posibilidad técnica de que un agente intente financiar su consumo endeudándose indefinidamente, pagando la deuda anterior emitiendo nueva deuda.

Este comportamiento se conoce como un **juego a la Ponzi** (*Ponzi game*), en alusión a Charles Ponzi. Para evitar que los hogares caigan en este esquema insostenible, los mercados financieros imponen la **condición de no-Ponzi** o **condición de transversalidad**:

$$
\begin{align*}\lim_{N \to \infty} \frac{A_{t+N+1}}{(1 + r)^N} = 0\end{align*}
$$

Dado que la tasa de interés real es estrictamente positiva (`$r > 0$`), el factor de actualización satisface:

$$
\begin{align*}\frac{1}{1 + r} < 1 \implies \lim_{N \to \infty} \frac{1}{(1 + r)^N} = 0\end{align*}
$$

La condición de transversalidad garantiza que la deuda (o activos) no crezca en el largo plazo a una tasa mayor o igual que la tasa de interés real. En valor presente, la deuda terminal debe desvanecerse.


La Restricción Presupuestaria Intertemporal Consolidada
-------------------------------------------------------

Al aplicar la condición de transversalidad, obtenemos la forma canónica de la **Restricción Presupuestaria Intertemporal (RPI)**:

$$
\begin{align*}\sum_{i=0}^\infty \frac{C_{t+i}}{(1 + r)^i} = (1 + r)A_t + \sum_{i=0}^\infty \frac{Y_{\ell t+i} - T_{t+i}}{(1 + r)^i}\end{align*}
$$

De acuerdo con De Gregorio (Cap. 3), esta ecuación sintetiza una ley económica fundamental:

$$
\begin{align*}\text{Valor Presente del Consumo} = \text{Riqueza Financiera} + \text{Riqueza Humana}\end{align*}
$$

El agente no está restringido período a período por sus ingresos corrientes; su única cota es que la corriente descontada de todos sus consumos no sobrepase su riqueza integral.


Modelación de las Preferencias Intertemporales
----------------------------------------------

Una vez caracterizado el conjunto de posibilidades de consumo (los recursos), pasamos a formalizar los deseos del consumidor (sus preferencias).

En microeconomía estática, las preferencias sobre dos bienes `$X_1$` y `$X_2$` se representan mediante funciones de utilidad convexas y monótonas:

$$
\begin{align*}U(X_1, X_2) = X_1^\alpha X_2^\beta, \quad \alpha + \beta = 1\end{align*}
$$

cuyas curvas de nivel son las conocidas **curvas de indiferencia**.

### De Bienes Físicos a Bienes Fechados

En macroeconomía intertemporal, tratamos el consumo en diferentes momentos del tiempo (`$C_t, C_{t+1}, \ldots$`) como si fueran bienes diferenciados. El agente debe decidir no entre manzanas y peras, sino entre "consumir hoy" versus "consumir mañana".

Una primera forma de representar esta elección es mediante una función tipo Cobb-Douglas intertemporal:

$$
\begin{align*}U(C_t, C_{t+1}, \ldots, C_{t+N}) = \prod_{i=0}^N C_{t+i}^{\alpha_{t+i}}, \quad \sum_{i=0}^N \alpha_{t+i} = 1\end{align*}
$$

donde las ponderaciones reflejan la valoración de cada momento del tiempo, siendo típicamente decrecientes:

$$
\begin{align*}\alpha_0 > \alpha_1 > \alpha_2 > \ldots > \alpha_N\end{align*}
$$

### La Función de Utilidad Aditiva Separable

Para dotar al modelo de consistencia analítica e invariancia temporal, la literatura macroeconómica adopta la especificación **aditiva separable en el tiempo**:

$$
\begin{align*}U = u(C_1) + \beta u(C_2) + \beta^2 u(C_3) + \ldots = \sum_{i=0}^\infty \beta^i u(C_{t+i}) < \infty\end{align*}
$$

donde:
* `$u(C)$` es la **función de utilidad instantánea** (o periódica), estrictamente creciente y estrictamente cóncava:

$$
\begin{align*}\frac{\partial u}{\partial C} > 0, \quad \frac{\partial^2 u}{\partial C^2} < 0\end{align*}
$$

* `$\beta$` es el **factor subjetivo de descuento**.


Tasa Subjetiva de Descuento y Factor de Descuento
-------------------------------------------------

El parámetro `$\beta$` captura la impaciencia psicológica inherente a los seres humanos: la tendencia a valorar más una unidad de satisfacción hoy que esa misma unidad en el futuro.

Formalmente, el factor subjetivo de descuento se define a partir de la **tasa subjetiva de descuento** `$\rho$`:

$$
\begin{align*}\beta = \frac{1}{1 + \rho}, \quad \text{con } \rho > 0 \implies 0 < \beta < 1\end{align*}
$$

### Contraste entre Precios de Mercado y Preferencias Psicológicas

Es fundamental distinguir con total precisión dos variables que suelen confundirse en macroeconomía:

1. **El factor objetivo del mercado `$\frac{1}{1+r}$`:** Es un precio relativo determinado por el equilibrio del mercado financiero. Representa a cuántas unidades de consumo futuro equivale objetivamente una unidad de consumo presente.
2. **El factor subjetivo del consumidor `$\beta = \frac{1}{1+\rho}$`:** Es un parámetro de preferencias psicológicas del hogar. Refleja la tasa marginal a la que el agente está dispuesto a intercambiar bienestar presente por bienestar futuro en ausencia de compensación.

### Análisis del Perfil Temporal del Descuento

A medida que proyectamos períodos más lejanos en el tiempo (`$i$`), el peso relativo de la utilidad futura decae geométricamente según `$\beta^i = \left(\frac{1}{1+\rho}\right)^i$`.

* Si `$\rho$` es alto (individuo muy impaciente), `$\beta$` es pequeño y la ponderación del futuro se desploma rápidamente.
* Si `$\rho$` es bajo (individuo paciente), `$\beta$` es cercano a 1 y la curva de descuento decae de forma muy suave.

Para tres individuos con grados de impaciencia `$\rho_1 > \rho_2 > \rho_3$`:

$$
\begin{align*}\beta_1 < \beta_2 < \beta_3\end{align*}
$$

La trayectoria temporal de `$\beta^i$` muestra una caída mucho más pronunciada para el agente 1 que para el agente 3.

> **Espacio para gráfica 2:** *Curvas de indiferencia intertemporales y mapa de nivel.*
> Representación en el plano `$(C_1, C_2)$` de curvas de indiferencia estrictamente convexas al origen, mostrando que combinaciones intermedias de consumo son estrictamente preferidas a esquemas de consumo extremos (aversión a las fluctuaciones).

> **Espacio para gráfica 3:** *Trayectorias del factor subjetivo de descuento `$\beta^t$`.*
> Gráfica de `$\beta^t$` en función del tiempo `$t$`, partiendo de 1 en `$t=0$` y decayendo asintóticamente hacia 0, comparando tres curvas para `$\rho_1 > \rho_2 > \rho_3$`.
