---
title: "Clase 03: Eficiencia de Pareto, Solución Planificada y Curva de Contrato en la Caja de Edgeworth"
course: "microeconomia-ii"
order: 3
classType: "clase"
description: "Definición del criterio de Pareto, planteamiento del problema del planificador social sin precios, deducción algebraica paso a paso de la curva de contrato para consumidores Cobb-Douglas y análisis de casos especiales."
math: true
conceptos: ["Eficiencia de Pareto", "Caja de Edgeworth", "Curva de contrato"]
---

## El Criterio de Eficiencia de Pareto y la Caja de Edgeworth

Consideremos una **economía de intercambio puro de `$2 \times 2$`** poblada por dos consumidores `$(i = 1, 2 \text{ o } A, B)$` y dos bienes físicos `$(j = 1, 2 \text{ o } X, Y)$`. En esta economía no hay producción; los consumidores nacen con **dotaciones iniciales** de ambos bienes:

* Dotación del Consumidor 1: `$W_1 = (W_{11}, W_{12})$`.
* Dotación del Consumidor 2: `$W_2 = (W_{21}, W_{22})$`.

Sumando las dotaciones individuales, obtenemos la **dotación total agregada de recursos de la economía** `$\underline{W} = (\underline{W}_1, \underline{W}_2)$`, la cual define las dimensiones de la **Caja de Edgeworth**:

$$
\begin{align*}\underline{W}_1 &= W_{11} + W_{21} \quad \text{(Total disponible del bien 1)} \\ \underline{W}_2 &= W_{12} + W_{22} \quad \text{(Total disponible del bien 2)}\end{align*}
$$

Una asignación `$((X_{11}, X_{12}), (X_{21}, X_{22}))$` es **factible** (sin desperdicio de recursos) si la suma de lo consumido por ambos agentes iguala exactamente las dotaciones totales:

$$
\begin{align*}X_{11} + X_{21} &= W_{11} + W_{21} = \underline{W}_1 \implies X_{21} = \underline{W}_1 - X_{11} \\ X_{12} + X_{22} &= W_{12} + W_{22} = \underline{W}_2 \implies X_{22} = \underline{W}_2 - X_{12}\end{align*}
$$

### ¿Qué es una Asignación Eficiente en el Sentido de Pareto?

Una asignación factible es **Pareto-eficiente (u óptima de Pareto)** si **no existe ninguna otra asignación factible que mejore estrictamente el bienestar de al menos un individuo sin empeorar el bienestar del otro**.

> **Nota conceptual fundamental:** Para encontrar las asignaciones de eficiencia **no se necesitan precios ni mercados**. Se trata de una **solución planificada** (el problema de un planificador omnisciente que conoce las preferencias y las dotaciones físicas y busca agotar todas las ganancias mutuas del intercambio).


## Planteamiento y Deducción Paso a Paso: Consumidores Cobb-Douglas

Siguiendo el desarrollo en pizarra del profesor David Tobón, supongamos que los dos consumidores tienen preferencias representadas por funciones de utilidad **Cobb-Douglas** con parámetros `$\alpha \in (0, 1)$` y `$\beta \in (0, 1)$`:

$$
\begin{align*}U_1(X_{11}, X_{12}) = X_{11}^\alpha X_{12}^{1 - \alpha}, \qquad \qquad U_2(X_{21}, X_{22}) = X_{21}^\beta X_{22}^{1 - \beta}\end{align*}
$$

### Formulación del Problema de Eficiencia

Para caracterizar todas las asignaciones eficientes en el sentido de Pareto, maximizamos la utilidad del Consumidor 1 sujeto a que el Consumidor 2 alcance al menos un nivel de utilidad fijo `$\underline{U}_2$` y sujeto a las restricciones físicas de recursos de la economía:

$$
\begin{align*}\max_{\{X_{11}, X_{12}, X_{21}, X_{22}\}} \quad & U_1 = X_{11}^\alpha X_{12}^{1 - \alpha} \\ \text{s.a.} \quad & U_2 = X_{21}^\beta X_{22}^{1 - \beta} \geq \underline{U}_2 \\ & W_{11} + W_{21} = X_{11} + X_{21} \\ & W_{12} + W_{22} = X_{12} + X_{22}\end{align*}
$$

*(Como señala el apunte de clase, en términos de bienestar social esto equivale a maximizar una suma ponderada `$W = U_1 + \lambda U_2$` sujeta a las restricciones de recursos `$W_{11} + W_{21} = X_{11} + X_{21}$` y `$W_{12} + W_{22} = X_{12} + X_{22}$`).*

### Paso 1: Sustitución de las Restricciones Físicas y Lagrangiano

Despejamos el consumo del agente 2 en función del consumo del agente 1 y de las dotaciones totales `$(X_{21} = \underline{W}_1 - X_{11}, \; X_{22} = \underline{W}_2 - X_{12})$`, reduciendo el problema a dos variables de decisión `$(X_{11}, X_{12})$`:

$$
\begin{align*}\max_{\{X_{11}, X_{12}\}} \quad & X_{11}^\alpha X_{12}^{1 - \alpha} \\ \text{s.a.} \quad & (\underline{W}_1 - X_{11})^\beta (\underline{W}_2 - X_{12})^{1 - \beta} = \underline{U}_2\end{align*}
$$

Planteamos la función Lagrangiana:

$$
\begin{align*}\mathcal{L}(X_{11}, X_{12}, \lambda) = X_{11}^\alpha X_{12}^{1 - \alpha} + \lambda \left[ (\underline{W}_1 - X_{11})^\beta (\underline{W}_2 - X_{12})^{1 - \beta} - \underline{U}_2 \right]\end{align*}
$$

### Paso 2: Condiciones de Primer Orden (C.P.O.)

Recordando la propiedad de las derivadas Cobb-Douglas `$\left(\frac{\partial U_1}{\partial X_{11}} = \frac{\alpha U_1}{X_{11}}\right)$` y aplicando la regla de la cadena sobre `$\underline{W}_1 - X_{11}$` (de donde sale un signo menos), derivamos respecto a `$X_{11}$` y `$X_{12}$`:

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial X_{11}} &= \frac{\alpha U_1}{X_{11}} - \frac{\lambda \beta U_2}{\underline{W}_1 - X_{11}} = 0 \implies \frac{\alpha U_1}{X_{11}} = \frac{\lambda \beta U_2}{\underline{W}_1 - X_{11}} \qquad \text{(1)} \\ \frac{\partial \mathcal{L}}{\partial X_{12}} &= \frac{(1 - \alpha) U_1}{X_{12}} - \frac{\lambda (1 - \beta) U_2}{\underline{W}_2 - X_{12}} = 0 \implies \frac{(1 - \alpha) U_1}{X_{12}} = \frac{\lambda (1 - \beta) U_2}{\underline{W}_2 - X_{12}} \qquad \text{(2)}\end{align*}
$$

### Paso 3: División de (1) entre (2) y Cancelación de Términos

Dividimos miembro a miembro la ecuación `(1)` entre la ecuación `(2)`. Observemos cómo se cancelan simultáneamente `$U_1$`, `$\lambda$` y `$U_2$`:

$$
\begin{align*}\frac{\dfrac{\alpha \cancel{U_1}}{X_{11}}}{\dfrac{(1 - \alpha) \cancel{U_1}}{X_{12}}} = \frac{\dfrac{\cancel{\lambda} \beta \cancel{U_2}}{\underline{W}_1 - X_{11}}}{\dfrac{\cancel{\lambda} (1 - \beta) \cancel{U_2}}{\underline{W}_2 - X_{12}}}\end{align*}
$$

Aplicando producto de extremos y medios en ambos lados, obtenemos la **condición de igualdad de las Relaciones Marginales de Sustitución `$(RMS_1 = RMS_2)$`**:

$$
\begin{align*}\frac{\alpha X_{12}}{(1 - \alpha) X_{11}} = \frac{\beta (\underline{W}_2 - X_{12})}{(1 - \beta) (\underline{W}_1 - X_{11})}\end{align*}
$$

### Paso 4: Despeje Algebraico de la Curva de Contrato

Multiplicamos en cruz para eliminar los denominadores:

$$
\begin{align*}\alpha (1 - \beta) X_{12} (\underline{W}_1 - X_{11}) = \beta (1 - \alpha) X_{11} (\underline{W}_2 - X_{12})\end{align*}
$$

Expandimos los productos en ambos lados:

$$
\begin{align*}\alpha (1 - \beta) \underline{W}_1 X_{12} - \alpha (1 - \beta) X_{11} X_{12} = \beta (1 - \alpha) \underline{W}_2 X_{11} - \beta (1 - \alpha) X_{11} X_{12}\end{align*}
$$

Agrupamos todos los términos que contienen a `$X_{12}$` en el lado izquierdo:

$$
\begin{align*}\alpha (1 - \beta) \underline{W}_1 X_{12} + \beta (1 - \alpha) X_{11} X_{12} - \alpha (1 - \beta) X_{11} X_{12} = \beta (1 - \alpha) \underline{W}_2 X_{11}\end{align*}
$$

Notemos que en los dos términos cruzados con `$X_{11} X_{12}$` podemos simplificar sus coeficientes:

$$
\begin{align*}\beta (1 - \alpha) - \alpha (1 - \beta) = \beta - \cancel{\alpha \beta} - \alpha + \cancel{\alpha \beta} = \beta - \alpha\end{align*}
$$

Factorizando `$X_{12}$` en el lado izquierdo:

$$
\begin{align*}X_{12} \Big[ \alpha (1 - \beta) \underline{W}_1 + (\beta - \alpha) X_{11} \Big] = \beta (1 - \alpha) \underline{W}_2 X_{11}\end{align*}
$$

Finalmente, despejamos **`$X_{12}^*$` en función de `$X_{11}$`**, obteniendo la **ecuación explícita de la Curva de Contrato (o Región de Contrato)**:

$$
\begin{align*}\boxed{X_{12}^* = \frac{\beta (1 - \alpha) \underline{W}_2 X_{11}}{\alpha (1 - \beta) \underline{W}_1 + (\beta - \alpha) X_{11}}}\end{align*}
$$

### Caso Particular Simétrico `$( \alpha = \beta )$`

Si ambos consumidores valoran con la misma intensidad relativa los dos bienes `$( \alpha = \beta )$`, el término `$(\beta - \alpha) X_{11}$` en el denominador se anula y los factores `$\alpha(1-\alpha)$` se cancelan:

$$
\begin{align*}X_{12}^* = \frac{\cancel{\alpha (1 - \alpha)} \underline{W}_2 X_{11}}{\cancel{\alpha (1 - \alpha)} \underline{W}_1 + 0} = \left( \frac{\underline{W}_2}{\underline{W}_1} \right) X_{11}\end{align*}
$$

Cuando `$\alpha = \beta$`, **la curva de contrato es exactamente la diagonal principal recta** que une el origen `$O_1$` con el origen `$O_2$` de la Caja de Edgeworth. Si `$\beta > \alpha$`, la curva de contrato se arquea por debajo de la diagonal; si `$\beta < \alpha$`, se arquea por encima.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/edgeworth-contrato-light.svg" alt="Caja de Edgeworth con curva de contrato, tres tangencias entre indiferencias y lente de mejoras desde la dotación." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/edgeworth-contrato-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: Figura: la curva de contrato une las tangencias; el lente muestra cuánto queda por ganar.</figcaption>
</figure>



## Casos Especiales de Eficiencia en la Guía de Estudio

En los talleres y exámenes de Microeconomía II aparecen frecuentemente preferencias no estándar donde la curva de contrato cambia radicalmente de forma:

1. **Consumidor 1 carnívoro puro `$(U_1 = X_1)$` y Consumidor 2 vegetariano puro `$(U_2 = X_2)$`:**
   * Al agente 1 solo le interesa la carne `$(X_1)$` y al agente 2 solo los vegetales `$(X_2)$`.
   * **Única asignación eficiente de Pareto:** El agente 1 recibe **toda la carne** de la economía `$(X_{11}^* = \underline{W}_1, \; X_{12}^* = 0)$` y el agente 2 recibe **todos los vegetales** `$(X_{21}^* = 0, \; X_{22}^* = \underline{W}_2)$`. Geométricamente, la curva de contrato se colapsa en una única esquina de la Caja de Edgeworth.
2. **Complementos perfectos (Leontief) con distintas proporciones `$(U_1 = \min\{X_{11}, 6X_{12}\}, \; U_2 = \min\{2X_{21}, X_{22}\})$`:**
   * El rayo de expansión eficiente del agente 1 es `$X_{12} = \frac{1}{6}X_{11}$` (3 unidades de `$F$` por media de `$C$`) y el del agente 2 es `$X_{22} = 2X_{21}$` (1 unidad de `$F$` por 2 de `$C$`).
   * Como las curvas de indiferencia tienen forma de "L", los conjuntos de asignaciones Pareto-eficientes abarcan la región comprendida entre los dos rayos de vértices de ambos consumidores dentro de la caja.
3. **El problema de dividir un pastel entre dos personas ("Uno corta y el otro elige"):**
   * Si un pastel homogéneo (un solo bien divisible) se reparte entre dos personas monótonas, **cualquier partición que no desperdicie pastel `$(x_1 + x_2 = 1)$` es eficiente en el sentido de Pareto** (para mejorar a uno habría que quitarle pastel al otro).
   * La regla *"uno corta y el otro elige primero"* garantiza una asignación **equitativa (libre de envidias)** y eficiente, pero no es la única asignación eficiente; si el pastel es heterogéneo (mitad chocolate y mitad vainilla con gustos distintos), el corte 50/50 puede ni siquiera agotar las mejoras paretianas de intercambio.


## Los Dos Teoremas Fundamentales de la Economía del Bienestar

| Teorema | Enunciado Formal | Supuestos Requeridos | Implicación Institucional y de Política |
| :--- | :--- | :--- | :--- |
| **Primer Teorema del Bienestar** | Todo equilibrio competitivo walrasiano es **eficiente en el sentido de Pareto**. | **No saciabilidad local (LNS)**, mercados completos, agentes precio-aceptantes y ausencia de externalidades. *(No requiere convexidad)*. | Formaliza la **Mano Invisible** de Adam Smith: el mercado competitivo agota todas las ganancias del intercambio sin necesidad de un planificador. |
| **Segundo Teorema del Bienestar** | Cualquier asignación eficiente en el sentido de Pareto puede alcanzarse como un equilibrio competitivo mediante una **redistribución adecuada de las dotaciones iniciales** (transferencias de suma fija). | **Convexidad** de las preferencias y de los conjuntos de producción, continuidad y LNS. | Permite **separar eficiencia y equidad**: el Estado puede redistribuir dotaciones iniciales (p. ej., capital humano o riqueza base) y dejar que el sistema de precios opere libremente. |

<IdeaClave>

Pareto no necesita precios: la curva de contrato es pura geometría de tangencias que agotan las ganancias del intercambio.

</IdeaClave>
