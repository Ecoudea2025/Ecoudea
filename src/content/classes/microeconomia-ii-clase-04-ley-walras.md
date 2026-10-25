---
title: "Clase 04: Equilibrio General Walrasiano, Ley de Walras y Teorema de Brouwer"
course: "microeconomia-ii"
order: 4
classType: "clase"
description: "Deducción paso a paso del equilibrio de mercado para consumidores Cobb-Douglas, demostración algebraica de la Ley de Walras, normalización de precios y condiciones del Teorema de Punto Fijo de Brouwer."
math: true
conceptos: ["Ley de Walras", "Demanda neta", "Exceso de demanda"]
---

## De la Planificación Central al Equilibrio Descentralizado de Mercado

En la clase anterior caracterizamos todas las asignaciones eficientes en el sentido de Pareto (la Curva de Contrato), pero el criterio de Pareto por sí solo deja indeterminado en cuál de los infinitos puntos de la curva terminará la economía.

En una **economía de mercado**, cada consumidor parte de su dotación privada `$W_i = (W_{i1}, W_{i2})$` y observa un vector de precios de mercado `$P = (P_1, P_2)$`. El valor monetario de la dotación (la riqueza o renta nominal `$R_i$` del consumidor `$i$`) es:

$$
\begin{align*}R_1 &= P_1 W_{11} + P_2 W_{12} \\ R_2 &= P_1 W_{21} + P_2 W_{22}\end{align*}
$$

Un **Equilibrio General Walrasiano (o Competitivo)** es un par compuesto por un vector de precios `$P^* = (P_1^*, P_2^*)$` y una asignación de consumo `$((X_{11}^*, X_{12}^*), (X_{21}^*, X_{22}^*))$` tales que:
1. Cada consumidor `$i$` maximiza su utilidad `$U_i(X_{i1}, X_{i2})$` sujeto a su restricción presupuestaria `$P_1^* X_{i1} + P_2^* X_{i2} = R_i$`.
2. **Todos los mercados se vacían simultáneamente** (la demanda agregada iguala a la oferta/dotación agregada en cada mercado).


## Deducción Paso a Paso: Equilibrio General con Consumidores Cobb-Douglas

Siguiendo las notas manuscritas del profesor David Tobón, resolvamos el equilibrio general para dos consumidores Cobb-Douglas:

$$
\begin{align*}U_1 = X_{11}^\alpha X_{12}^{1 - \alpha}, \quad W_1 = (W_{11}, W_{12}), \qquad \qquad U_2 = X_{21}^\beta X_{22}^{1 - \beta}, \quad W_2 = (W_{21}, W_{22})\end{align*}
$$

### Paso 1: Demandas Individuales (Brutas) de Cada Consumidor

1. **Problema del Consumidor 1:**

$$
\begin{align*}\max_{\{X_{11}, X_{12}\}} \quad X_{11}^\alpha X_{12}^{1 - \alpha} \quad \text{s.a.} \quad R_1 = P_1 W_{11} + P_2 W_{12} = P_1 X_{11} + P_2 X_{12}\end{align*}
$$

Como sabemos de la optimización Cobb-Douglas `(donde `$\alpha + (1 - \alpha) = 1$`)`, el consumidor gasta una fracción `$\alpha$` de su riqueza `$R_1$` en el bien 1 y una fracción `$(1 - \alpha)$` en el bien 2:

$$
\begin{align*}X_{11}(P_1, P_2) = \frac{\alpha R_1}{P_1} = \frac{\alpha (P_1 W_{11} + P_2 W_{12})}{P_1}, \qquad X_{12}(P_1, P_2) = \frac{(1 - \alpha) R_1}{P_2} = \frac{(1 - \alpha) (P_1 W_{11} + P_2 W_{12})}{P_2}\end{align*}
$$

2. **Problema del Consumidor 2:**

$$
\begin{align*}\max_{\{X_{21}, X_{22}\}} \quad X_{21}^\beta X_{22}^{1 - \beta} \quad \text{s.a.} \quad R_2 = P_1 W_{21} + P_2 W_{22} = P_1 X_{21} + P_2 X_{22}\end{align*}
$$

De manera análoga, sus funciones de demanda bruta son:

$$
\begin{align*}X_{21}(P_1, P_2) = \frac{\beta R_2}{P_1} = \frac{\beta (P_1 W_{21} + P_2 W_{22})}{P_1}, \qquad X_{22}(P_1, P_2) = \frac{(1 - \beta) R_2}{P_2} = \frac{(1 - \beta) (P_1 W_{21} + P_2 W_{22})}{P_2}\end{align*}
$$

> **Propiedad de Homogeneidad de Grado Cero:** Si multiplicamos todos los precios por una constante positiva `$\lambda > 0$` `$((\lambda P_1, \lambda P_2))$`, las rentas `$R_i$` quedan multiplicadas por `$\lambda$`, el cual se cancela con el `$\lambda P_j$` del denominador. Por tanto, **las demandas dependen únicamente de los precios relativos `$(P_1/P_2)$` y son homogéneas de grado 0 en los precios** (no hay ilusión monetaria).


## Funciones de Exceso de Demanda y Demostración de la Ley de Walras

Definimos el **exceso de demanda individual** del agente `$i$` por el bien `$j$` como `$z_{ij}(P) = X_{ij}(P) - W_{ij}$`:
* Si `$z_{ij}(P) > 0$`, el agente `$i$` es un **comprador neto (demandante neto)** del bien `$j$`.
* Si `$z_{ij}(P) < 0$`, el agente `$i$` es un **vendedor neto (oferente neto)** del bien `$j$`.

Sumando entre todos los consumidores, obtenemos la **función de exceso de demanda agregada** en cada mercado:

$$
\begin{align*}Z_1(P_1, P_2) &= \big( X_{11}(P) - W_{11} \big) + \big( X_{21}(P) - W_{21} \big) \\ Z_2(P_1, P_2) &= \big( X_{12}(P) - W_{12} \big) + \big( X_{22}(P) - W_{22} \big)\end{align*}
$$

### Enunciado y Verificación Algebraica de la Ley de Walras

La **Ley de Walras** establece que, **para cualquier vector de precios `$P = (P_1, P_2)$` (esté o no en equilibrio)**, el valor monetario agregado de los excesos de demanda es idénticamente igual a cero:

$$
\begin{align*}P \cdot Z(P) \equiv P_1 Z_1(P_1, P_2) + P_2 Z_2(P_1, P_2) = 0, \quad \forall (P_1, P_2) \gg 0\end{align*}
$$

**Demostración algebraica paso a paso (según el apunte de clase):**

Sustituimos las demandas Cobb-Douglas dentro de `$P_1 Z_1(P) + P_2 Z_2(P)$`:

$$
\begin{align*}P_1 \left[ \left( \frac{\alpha R_1}{P_1} - W_{11} \right) + \left( \frac{\beta R_2}{P_1} - W_{21} \right) \right] + P_2 \left[ \left( \frac{(1 - \alpha) R_1}{P_2} - W_{12} \right) + \left( \frac{(1 - \beta) R_2}{P_2} - W_{22} \right) \right]\end{align*}
$$

Reemplazando `$R_1 = P_1 W_{11} + P_2 W_{12}$` y `$R_2 = P_1 W_{21} + P_2 W_{22}$`, y cancelando los precios `$P_1$` y `$P_2$` que multiplican a cada corchete:

$$
\begin{align*}&\Big[ \alpha (P_1 W_{11} + P_2 W_{12}) - P_1 W_{11} + \beta (P_1 W_{21} + P_2 W_{22}) - P_1 W_{21} \Big] \\ &\quad + \Big[ (1 - \alpha)(P_1 W_{11} + P_2 W_{12}) - P_2 W_{12} + (1 - \beta)(P_1 W_{21} + P_2 W_{22}) - P_2 W_{22} \Big]\end{align*}
$$

Agrupando factor por factor cada término de dotación `$(P_1 W_{11}, P_2 W_{12}, P_1 W_{21}, P_2 W_{22})$`:

$$
\begin{align*}&= P_1 W_{11} \big( \alpha - 1 + (1 - \alpha) \big) + P_2 W_{12} \big( \alpha + (1 - \alpha) - 1 \big) \\ &\quad + P_1 W_{21} \big( \beta - 1 + (1 - \beta) \big) + P_2 W_{22} \big( \beta + (1 - \beta) - 1 \big) \\ &= P_1 W_{11} (0) + P_2 W_{12} (0) + P_1 W_{21} (0) + P_2 W_{22} (0) \implies \boxed{0 = 0}\end{align*}
$$

### Tres Corolarios Fundamentales de la Ley de Walras

1. **Redundancia de una ecuación de mercado:** En una economía con `$k$` mercados, si `$k - 1$` mercados están en equilibrio `$(Z_1(P^*) = Z_2(P^*) = \ldots = Z_{k-1}(P^*) = 0)$` y `$P_k^* > 0$`, entonces **el `$k$`-ésimo mercado está automáticamente en equilibrio `$(Z_k(P^*) = 0)$`**.
   * *Ejemplo en 2 bienes:* Por la Ley de Walras, basta buscar el equilibrio en **un solo mercado** (por ejemplo, el mercado 1); el mercado 2 quedará automáticamente vaciado.
2. **Desequilibrios compensados fuera de equilibrio:** Si para unos precios iniciales `$P^0$` existe exceso de demanda positivo en el mercado 1 `$(Z_1(P^0) > 0)$`, necesariamente debe existir un exceso de oferta en el mercado 2 `$(Z_2(P^0) = -\frac{P_1^0}{P_2^0} Z_1(P^0) < 0)$`. El subastador walrasiano corregirá este desequilibrio **subiendo el precio del bien 1 `$(P_1)$` y/o bajando el precio del bien 2 `$(P_2)$`**.
3. **¿Qué ocurre si los consumidores ahorran sin mercado de crédito?** La Ley de Walras proviene de que cada consumidor gasta exactamente el 100% de su presupuesto (gracias a la No Saciabilidad Local). Si en un modelo estático los consumidores atesoraran o generaran ahorros positivos no canalizados como demanda de otro activo/bien futuro, la suma del gasto en bienes sería menor que el valor de las dotaciones y la Ley de Walras en los mercados de bienes no se cumpliría con igualdad a cero.


## Cálculo Explícito del Precio Relativo de Equilibrio `$(P_1^*, P_2^* = 1)$`

Como solo importan los precios relativos, fijamos al bien 2 como **numerario**: **`$P_2^* = 1$`**, y despejamos `$P_1^*$` igualando la oferta total con la demanda total en el mercado del bien 1:

$$
\begin{align*}W_{11} + W_{21} &= X_{11}(P_1^*, 1) + X_{21}(P_1^*, 1) \\ W_{11} + W_{21} &= \frac{\alpha (P_1^* W_{11} + 1 \cdot W_{12})}{P_1^*} + \frac{\beta (P_1^* W_{21} + 1 \cdot W_{22})}{P_1^*}\end{align*}
$$

Multiplicamos ambos lados de la ecuación por `$P_1^*$`:

$$
\begin{align*}P_1^* (W_{11} + W_{21}) = P_1^* (\alpha W_{11} + \beta W_{21}) + \alpha W_{12} + \beta W_{22}\end{align*}
$$

Pasamos los términos con `$P_1^*$` al lado izquierdo y factorizamos:

$$
\begin{align*}P_1^* \Big[ (1 - \alpha) W_{11} + (1 - \beta) W_{21} \Big] = \alpha W_{12} + \beta W_{22}\end{align*}
$$

Despejando **`$P_1^*$`** `(con `$P_2^* = 1$`)`, obtenemos la **fórmula cerrada del precio relativo de equilibrio general**:

$$
\begin{align*}\boxed{P_1^* = \frac{\alpha W_{12} + \beta W_{22}}{(1 - \alpha) W_{11} + (1 - \beta) W_{21}}, \qquad P_2^* = 1}\end{align*}
$$

En este precio de equilibrio `$P^*$`, los excesos de demanda individuales se compensan exactamente en ambos mercados:

$$
\begin{align*}z_{11}(P^*) + z_{21}(P^*) &= 0 \implies Z_1(P^*) = 0 \\ z_{12}(P^*) + z_{22}(P^*) &= 0 \implies Z_2(P^*) = 0\end{align*}
$$


## Existencia del Equilibrio General: El Teorema de Punto Fijo de Brouwer

En economías generales con `$n$` bienes, ¿bajo qué condiciones matemáticas podemos garantizar que existe al menos un vector de precios `$P^*$` tal que `$Z(P^*) \leq 0$` `(y `$Z(P^*) = 0$` cuando no hay bienes libres)`?

La demostración moderna de **Arrow y Debreu (1954)** utiliza el **Teorema del Punto Fijo de Brouwer**, el cual establece que toda función continua `$g: S \to S$` que mapea un conjunto compacto (cerrado y acotado) y convexo `$S$` en sí mismo posee al menos un punto fijo `$P^* \in S$` tal que `$g(P^*) = P^*$`.

Para aplicar el Teorema de Brouwer a una economía guiada por las señales de los precios, se requiere que:

1. **El conjunto de precios esté normalizado en el Símplex unitario `$S^{n-1}$`:** Aprovechando la homogeneidad de grado cero de `$Z(P)$`, restringimos los precios para que sumen 1:

$$
\begin{align*}S^{n-1} = \left\{ P \in \mathbb{R}_+^n : \sum_{i=1}^n P_i = 1, \; P_i \geq 0 \right\}\end{align*}
$$

El símplex `$S^{n-1}$` es un conjunto no vacío, **compacto y convexo**.
2. **La función de exceso de demanda `$Z(P)$` sea continua:** Esto se garantiza cuando las preferencias de los consumidores son **continuas y estrictamente convexas** y las dotaciones iniciales son estrictamente positivas.
3. **La función `$Z(P)$` cumpla la Ley de Walras `$(P \cdot Z(P) = 0)$`:** Esto se garantiza cuando las preferencias satisfacen **No Saciabilidad Local (LNS)**.

Con estos ingredientes, se define la función de ajuste de precios del subastador `$g_i(P) = \frac{P_i + \max\{0, Z_i(P)\}}{1 + \sum_{j=1}^n \max\{0, Z_j(P)\}}$` (que sube el precio de los bienes con exceso de demanda positivo y mantiene los precios en el símplex). Por Brouwer, existe `$P^*$` tal que `$g(P^*) = P^*$`, y usando la Ley de Walras se demuestra que en dicho punto fijo `$Z_i(P^*) = 0$` para todos los bienes con `$P_i^* > 0$`.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/walras-equilibrio-light.svg" alt="Caja con dotación inicial, recta fuera de equilibrio con excesos señalados y recta de equilibrio tangente sobre el contrato." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/walras-equilibrio-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: fuera del equilibrio sobra de un bien y falta del otro; el precio walrasiano vacía ambos.</figcaption>
</figure>


<IdeaClave>

Walras dice que basta vaciar todos los mercados menos uno; el subastador es el mecanismo que lo hace posible.

</IdeaClave>
