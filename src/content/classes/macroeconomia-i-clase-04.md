---
title: "Clase 04: Optimización con Preferencias Cobb-Douglas e Impuestos Distorsionantes"
course: "macroeconomia-i"
order: 4
classType: "clase"
description: "Resolución paso a paso del problema intertemporal con función Cobb-Douglas no separable, impuestos al consumo y a la renta, estática comparativa y diferencial total."
math: true
---

---
---

Estructura General del Equilibrio del Consumidor
------------------------------------------------

Al resolver el problema intertemporal del consumidor para un horizonte de `$N$` períodos:

$$
\begin{align*}\max_{\{C_t\}_{t=0}^N} \quad U(C_0, C_1, \ldots, C_N) \quad \text{s.a.} \quad \text{R.P.I.}\end{align*}
$$

las Condiciones de Primer Orden (C.P.O.) siempre se dividen en dos bloques económicos fundamentales:

1. **Condiciones de marginalidad (optimalidad intratemporal/intertemporal):** Igualan la tasa marginal de sustitución entre períodos con el precio relativo de mercado.
2. **Cumplimiento de la Restricción Presupuestaria Intertemporal (factibilidad):** Garantiza que el plan óptimo agote exactamente los recursos disponibles (bajo no saciación).

En conjunto, estas condiciones conforman un **sistema determinado de `$N$` ecuaciones con `$N$` incógnitas**, del cual emergen las funciones de demanda óptima de consumo para cada período. En esta clase resolveremos de principio a fin un caso explícito fundamental: preferencias **Cobb-Douglas** en presencia de **impuestos distorsionantes** sobre el consumo y sobre el ingreso laboral.


Planteamiento del Modelo Cobb-Douglas con Impuestos
---------------------------------------------------

Consideremos una economía de dos períodos (`$t = 1, 2$`) donde las preferencias del individuo están representadas por una función de utilidad Cobb-Douglas:

$$
\begin{align*}U(C_1, C_2) = C_1^\alpha C_2^{1-\alpha}, \quad \text{con } 0 < \alpha < 1\end{align*}
$$

> **Nota pedagógica:** A diferencia de la utilidad logarítmica o CRRA estándar, esta formulación multiplicativa es una **función no separable aditivamente** en niveles (aunque sí mediante una transformación monótona logarítmica), donde la utilidad marginal del consumo presente depende directamente del nivel de consumo futuro (`$C_2$`).

### Condición de Preferencia por el Presente

El parámetro `$\alpha$` mide el peso subjetivo del consumo presente, mientras que `$1 - \alpha$` mide el peso del consumo futuro. Para que el consumidor exhiba impaciencia o **preferencia por el consumo presente** sobre el futuro, debe cumplirse que:

$$
\begin{align*}\alpha > 1 - \alpha \iff 2\alpha > 1 \iff \alpha > \frac{1}{2}\end{align*}
$$

Si generalizamos esta función a `$N$` períodos de la forma `$U = C_1^{\alpha_1} C_2^{\alpha_2} \cdots C_N^{\alpha_N}$` con `$\sum_{i=1}^N \alpha_i = 1$`, la preferencia por el presente exige una secuencia estrictamente decreciente de exponentes:

$$
\begin{align*}\alpha_1 > \alpha_2 > \alpha_3 > \ldots > \alpha_N\end{align*}
$$

### La Restricción Presupuestaria con Política Fiscal

Introducimos al gobierno a través de dos instrumentos tributarios proporcionales:
* `$\tau_c \in (0, 1)$`: Tasa de impuesto al consumo (como el IVA), que encarece cada unidad consumida a un precio efectivo de `$(1 + \tau_c)$`.
* `$\tau_y \in (0, 1)$`: Tasa de impuesto sobre la renta laboral, que reduce el ingreso disponible en cada período a una fracción `$(1 - \tau_y)Y_t$`.

Por tanto, la Restricción Presupuestaria Intertemporal (R.P.I.) toma la forma:

$$
\begin{align*}(1 + \tau_c)C_1 + \frac{(1 + \tau_c)C_2}{1 + r} = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r}\end{align*}
$$


Resolución Paso a Paso mediante Multiplicadores de Lagrange
-----------------------------------------------------------

### Paso 1: Construcción del Lagrangiano

Planteamos la función Lagrangiana asociando el multiplicador `$\lambda$` a la restricción presupuestaria intertemporal:

$$
\begin{align*}\mathcal{L}(C_1, C_2, \lambda) = C_1^\alpha C_2^{1-\alpha} + \lambda \left[ (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} - (1 + \tau_c)C_1 - \frac{(1 + \tau_c)C_2}{1 + r} \right]\end{align*}
$$

### Paso 2: Obtención de las Condiciones de Primer Orden (C.P.O.)

Derivamos parcialmente respecto a las tres incógnitas (`$C_1, C_2, \lambda$`) e igualamos a cero:

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_1} &= \alpha C_1^{\alpha - 1} C_2^{1 - \alpha} - \lambda(1 + \tau_c) = 0 \tag{4.1} \\ \frac{\partial \mathcal{L}}{\partial C_2} &= (1 - \alpha) C_1^\alpha C_2^{-\alpha} - \lambda \left( \frac{1 + \tau_c}{1 + r} \right) = 0 \tag{4.2} \\ \frac{\partial \mathcal{L}}{\partial \lambda} &= (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} - (1 + \tau_c)C_1 - \frac{(1 + \tau_c)C_2}{1 + r} = 0 \tag{4.3}\end{align*}
$$

Observamos que tenemos un sistema cerrado de **3 ecuaciones y 3 variables** (`$C_1, C_2, \lambda$`).

### Paso 3: Eliminación de $\lambda$ y Condición de Tangencia

De la ecuación $\ref{4.1}$, despejamos explícitamente el multiplicador `$\lambda$` (que representa la utilidad marginal del ingreso disponible ajustada por impuestos al consumo):

$$
\begin{align*}\alpha C_1^{\alpha - 1} C_2^{1 - \alpha} = \lambda(1 + \tau_c) \implies \lambda = \frac{\alpha C_1^{\alpha - 1} C_2^{1 - \alpha}}{1 + \tau_c} \tag{4.1b}\end{align*}
$$

Sustituimos la expresión $\ref{4.1b}$ dentro de la ecuación $\ref{4.2}$:

$$
\begin{align*}(1 - \alpha) C_1^\alpha C_2^{-\alpha} - \left( \frac{\alpha C_1^{\alpha - 1} C_2^{1 - \alpha}}{1 + \tau_c} \right) \left( \frac{1 + \tau_c}{1 + r} \right) = 0\end{align*}
$$

> **Resultado clave sobre el IVA intertemporal:** Si la tasa de impuesto al consumo `$\tau_c$` es **constante** entre el período 1 y el período 2, el factor `$(1 + \tau_c)$` en el numerador y en el denominador se cancela exactamente. Esto significa que un impuesto al consumo uniforme en el tiempo **no distorsiona el precio relativo entre consumir hoy y consumir mañana**.

Tras cancelar `$(1 + \tau_c)$`, reordenamos términos reconociendo las utilidades marginales (`$UmgC_1 = \alpha C_1^{\alpha-1}C_2^{1-\alpha}$` y `$UmgC_2 = (1-\alpha)C_1^\alpha C_2^{-\alpha}$`):

$$
\begin{align*}UmgC_2 = \frac{UmgC_1}{1 + r} \iff \frac{UmgC_1}{UmgC_2} = 1 + r \tag{4.4}\end{align*}
$$

### Paso 4: Simplificación de Exponentes y Senda de Expansión

Sustituimos las derivadas explícitas en la condición de optimalidad `(4)`:

$$
\begin{align*}\frac{\alpha C_1^{\alpha - 1} C_2^{1 - \alpha}}{(1 - \alpha) C_1^\alpha C_2^{-\alpha}} = 1 + r\end{align*}
$$

Aplicando leyes de los exponentes:
* Para `$C_1$`: `$C_1^{(\alpha - 1) - \alpha} = C_1^{-1} = \frac{1}{C_1}$`.
* Para `$C_2$`: `$C_2^{(1 - \alpha) - (-\alpha)} = C_2^{1 - \alpha + \alpha} = C_2^1 = C_2$`.

Por lo tanto, la relación se reduce limpiamente a:

$$
\begin{align*}\frac{\alpha C_2}{(1 - \alpha) C_1} = 1 + r\end{align*}
$$

Despejando `$C_2$` en función de `$C_1$`, obtenemos la **ecuación de transición (o senda de expansión intertemporal)**:

$$
\begin{align*}C_2 = \frac{(1 + r)(1 - \alpha)}{\alpha} C_1 \tag{4.5}\end{align*}
$$

> **Espacio para gráfica 1:** *Mapa de curvas de indiferencia y senda de expansión del consumo.*
> En el plano `$(C_1, C_2)$`, representación de una familia de curvas de indiferencia convexas junto con la línea recta que parte del origen con pendiente `$\frac{(1+r)(1-\alpha)}{\alpha}$` (ecuación 5), uniendo todos los puntos de tangencia óptima para distintos niveles de riqueza.

### Paso 5: Sustitución en la R.P.I. para Hallar $C_1^*$ y $C_2^*$

Ahora reemplazamos la ecuación `(5)` dentro de la restricción presupuestaria `(3)`:

$$
\begin{align*}(1 + \tau_c)C_1 + \left[ \frac{(1 + r)(1 - \alpha)}{\alpha} C_1 \right] \frac{1 + \tau_c}{1 + r} = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r}\end{align*}
$$

Observamos que el factor `$(1 + r)$` en el segundo término del lado izquierdo se cancela con el denominador:

$$
\begin{align*}(1 + \tau_c)C_1 + \frac{1 - \alpha}{\alpha} (1 + \tau_c)C_1 = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r}\end{align*}
$$

Extraemos `$(1 + \tau_c)C_1$` como factor común:

$$
\begin{align*}(1 + \tau_c)C_1 \left[ 1 + \frac{1 - \alpha}{\alpha} \right] = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r}\end{align*}
$$

Resolvemos la suma de fracciones dentro del corchete:

$$
\begin{align*}1 + \frac{1 - \alpha}{\alpha} = \frac{\alpha + 1 - \alpha}{\alpha} = \frac{1}{\alpha}\end{align*}
$$

Sustituyendo este resultado:

$$
\begin{align*}\frac{(1 + \tau_c)C_1}{\alpha} = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r}\end{align*}
$$

Finalmente, despejamos la **demanda óptima de consumo en el período 1 (`$C_1^*$`)**:

$$
\begin{align*}C_1^* = \frac{\alpha}{1 + \tau_c} \left[ (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} \right]\end{align*}
$$

Para encontrar la **demanda óptima de consumo en el período 2 (`$C_2^*$`)**, sustituimos `$C_1^*$` en la ecuación `(5)`:

$$
\begin{align*}C_2^* &= \frac{(1 + r)(1 - \alpha)}{\alpha} \cdot \frac{\alpha}{1 + \tau_c} \left[ (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} \right] \\ C_2^* &= \frac{(1 + r)(1 - \alpha)}{1 + \tau_c} \left[ (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} \right]\end{align*}
$$

> **Interpretación de las soluciones óptimas:** En una economía Cobb-Douglas, el individuo destina una fracción fija `$\alpha$` de su riqueza humana neta de impuestos al gasto total en consumo del período 1 (`$(1+\tau_c)C_1^*$`), y la fracción complementaria `$(1 - \alpha)$` al valor presente del gasto en consumo del período 2.


Estática Comparativa y Diferencial Total
----------------------------------------

Definamos la riqueza humana neta de impuestos a la renta como `$W$`:

$$
\begin{align*}W \equiv (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} > 0\end{align*}
$$

Analizamos formalmente cómo reacciona el consumo presente `$C_1^*$` ante cambios en cada uno de los parámetros del entorno económico:

### 1. Impacto del Impuesto al Consumo ($\tau_c$)

Derivando `$C_1^* = \alpha (1 + \tau_c)^{-1} W$` respecto a `$\tau_c$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial \tau_c} = -\frac{\alpha}{(1 + \tau_c)^2} W < 0\end{align*}
$$

Un aumento en el IVA encarece directamente cada unidad de consumo y reduce el poder de compra real de la riqueza, contrayendo el consumo presente.

### 2. Impacto del Impuesto a la Renta ($\tau_y$)

Derivando respecto a `$\tau_y$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial \tau_y} = -\frac{\alpha}{1 + \tau_c} \left[ Y_1 + \frac{Y_2}{1 + r} \right] < 0\end{align*}
$$

Un incremento en la tributación directa disminuye el ingreso disponible en ambos períodos (efecto riqueza negativo), reduciendo `$C_1^*$`.

### 3. Impacto de los Ingresos Laborales ($Y_1$ y $Y_2$)

$$
\begin{align*}\frac{\partial C_1^*}{\partial Y_1} &= \frac{\alpha(1 - \tau_y)}{1 + \tau_c} > 0 \\ \frac{\partial C_1^*}{\partial Y_2} &= \frac{\alpha(1 - \tau_y)}{(1 + \tau_c)(1 + r)} > 0\end{align*}
$$

Tanto el ingreso presente como el futuro tienen un impacto positivo sobre `$C_1^*$`, pero el ingreso futuro está atenuado por el factor de descuento `$\frac{1}{1+r}$`.

### 4. Impacto de la Tasa de Interés Real ($r$)

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -\frac{\alpha(1 - \tau_y)Y_2}{(1 + \tau_c)(1 + r)^2} < 0\end{align*}
$$

### El Diferencial Total de la Función de Consumo

Dado que el consumo óptimo es una función multivariable `$C_1^* = f(Y_1, Y_2, r, \tau_c, \tau_y)$`, recordamos que para cualquier función diferenciable `$Y = f(X_1, X_2, \ldots, X_N)$`, su **diferencial total** permite aproximar el cambio simultáneo ante variaciones en todos sus determinantes:

$$
\begin{align*}\text{d}Y = \sum_{i=1}^N \frac{\partial f(\cdot)}{\partial X_i} \text{d}X_i\end{align*}
$$

Aplicado a nuestra función de consumo:

$$
\begin{align*}\text{d}C_1^* = \underbrace{\frac{\partial C_1^*}{\partial Y_1}}_{(+)} \text{d}Y_1 + \underbrace{\frac{\partial C_1^*}{\partial Y_2}}_{(+)} \text{d}Y_2 + \underbrace{\frac{\partial C_1^*}{\partial r}}_{(-)} \text{d}r + \underbrace{\frac{\partial C_1^*}{\partial \tau_c}}_{(-)} \text{d}\tau_c + \underbrace{\frac{\partial C_1^*}{\partial \tau_y}}_{(-)} \text{d}\tau_y\end{align*}
$$
