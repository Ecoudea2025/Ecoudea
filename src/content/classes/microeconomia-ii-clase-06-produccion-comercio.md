---
title: "Clase 06: Equilibrio General con Producción y Apertura al Comercio Internacional"
course: "microeconomia-ii"
order: 6
classType: "clase"
description: "Deducción paso a paso de la FPP estrictamente cóncava con rendimientos decrecientes, condición de eficiencia global RMS = Px/Py = TMT, equilibrio autárquico y ganancias del comercio internacional."
math: true
conceptos: ["Autarquía", "Apertura comercial", "Ganancia de bienestar"]
---

## Planteamiento del Modelo de Equilibrio General con Producción

Siguiendo el modelo analítico desarrollado por el profesor David Tobón (*Equilibrio general con producción*), consideremos una economía competitiva compuesta por:

* **2 bienes de consumo final:** `$X$` e `$Y$`.
* **2 firmas competitivas** `(una productora de `$X$` y otra productora de `$Y$`)` y **1 consumidor representativo** (quien es dueño de la dotación de trabajo y de las firmas).
* **Tecnologías con rendimientos marginales decrecientes al trabajo:**

$$
\begin{align*}X = \frac{1}{2} \sqrt{L_X}, \qquad \qquad Y = \sqrt{L_Y}\end{align*}
$$

donde `$L_i$` denota la cantidad de trabajo (o capital humano) asignada al sector `$i \in \{X, Y\}$`.
* **Dotación total de trabajo de la economía:** Existen `$100$` unidades de trabajo disponibles en total:

$$
\begin{align*}L_X + L_Y = 100\end{align*}
$$

* **Preferencias del consumidor representativo:** Función de utilidad Cobb-Douglas simétrica:

$$
\begin{align*}U(X_C, Y_C) = X_C^{1/2} Y_C^{1/2}\end{align*}
$$


## Paso 1: Construcción de la Frontera de Posibilidades de Producción (FPP)

Para hallar la ecuación de la **FPP** que relaciona las cantidades máximas producibles de `$X$` e `$Y$`, despejamos los requerimientos de trabajo `$L_X$` y `$L_Y$` de cada función de producción:

1. **Del sector `$X$`:**

$$
\begin{align*}X = \frac{1}{2} \sqrt{L_X} \implies 2X = \sqrt{L_X} \implies \boxed{L_X = 4 X^2}\end{align*}
$$

2. **Del sector `$Y$`:**

$$
\begin{align*}Y = \sqrt{L_Y} \implies \boxed{L_Y = Y^2}\end{align*}
$$

3. **Sustituimos `$L_X$` y `$L_Y$` en la restricción de pleno empleo del trabajo `$(L_X + L_Y = 100)$`:**

$$
\begin{align*}\boxed{4 X^2 + Y^2 = 100} \quad \text{(Ecuación de la FPP)}\end{align*}
$$

Observemos los interceptos extremos de esta elipse en el primer cuadrante:
* Si `$X = 0 \implies Y^2 = 100 \implies Y_{\max} = 10$`.
* Si `$Y = 0 \implies 4X^2 = 100 \implies X^2 = 25 \implies X_{\max} = 5$`.


## Paso 2: La Tasa Marginal de Transformación `$(TMT)$` y la `$RMS$`

### 1. Deducción de la `$TMT$` mediante Diferencial Total de la FPP

Aplicamos la **derivada (o diferencial) total** a la ecuación implícita de la FPP `$4X^2 + Y^2 = 100$`:

$$
\begin{align*}8 X \, \text{d}X + 2 Y \, \text{d}Y = 0\end{align*}
$$

Despejando la pendiente `$\frac{\text{d}Y}{\text{d}X}$`, obtenemos la **Tasa Marginal de Transformación `$(TMT)$`**:

$$
\begin{align*}\frac{\text{d}Y}{\text{d}X} = TMT = -\frac{8 X}{2 Y} = -\frac{4 X}{Y} \quad \left( \text{en valor absoluto: } |TMT| = \frac{4 X}{Y} \right)\end{align*}
$$

### 2. Deducción de la `$RMS$` del Consumidor

A partir de `$U(X_C, Y_C) = X_C^{1/2} Y_C^{1/2}$`, calculamos la **Relación Marginal de Sustitución `$(RMS)$`** como el cociente de las utilidades marginales:

$$
\begin{align*}RMS = \frac{\dfrac{\partial U}{\partial X_C}}{\dfrac{\partial U}{\partial Y_C}} = \frac{\frac{1}{2} X_C^{-1/2} Y_C^{1/2}}{\frac{1}{2} X_C^{1/2} Y_C^{-1/2}} = \frac{Y_C}{X_C}\end{align*}
$$


## Paso 3: Equilibrio General en Economía Cerrada `(Autarquía — Punto `$E$`)`

En una economía cerrada sin comercio exterior, todo lo que se consume debe producirse internamente (**vaciado de mercados**: `$X_C = X$` e `$Y_C = Y$`), y la condición de optimalidad simultánea de productores y consumidores exige que la valoración subjetiva marginal iguale al precio relativo de mercado y al costo de oportunidad tecnológico:

$$
\begin{align*}RMS = \frac{P_X}{P_Y} = |TMT|\end{align*}
$$

### Resolución Algebraica Paso a Paso

1. **Igualamos `$\lvert TMT \rvert = RMS$` imponiendo vaciado de mercados `$(X_C = X, \; Y_C = Y)$`:**

$$
\begin{align*}\frac{4 X}{Y} = \frac{P_X}{P_Y} = \frac{Y}{X} \implies \boxed{4 X^2 = Y^2}\end{align*}
$$

2. **Reemplazamos la relación de optimalidad `$4X^2 = Y^2$` dentro de la FPP `$(4X^2 + Y^2 = 100)$`:**

$$
\begin{align*}Y^2 + Y^2 = 100 \implies 2 Y^2 = 100 \implies Y^2 = 50 \implies \boxed{Y^* = \sqrt{50} \approx 7.07}\end{align*}
$$

3. **Hallamos la producción y consumo de equilibrio de `$X$`:**

$$
\begin{align*}4 X^2 = 50 \implies X^2 = \frac{50}{4} = 12.5 \implies \boxed{X^* = \sqrt{\frac{50}{4}} \approx 3.53}\end{align*}
$$

4. **Hallamos el precio relativo de equilibrio en autarquía `$\left(\frac{P_X}{P_Y}\right)_E$`:**

Evaluando `$X^* = \frac{\sqrt{50}}{2}$` e `$Y^* = \sqrt{50}$` en la relación `$\frac{P_X}{P_Y} = \frac{Y^*}{X^*}$`:

$$
\begin{align*}\left( \frac{P_X}{P_Y} \right)_E = \frac{\sqrt{50}}{\frac{\sqrt{50}}{2}} = \boxed{2} \quad \text{(Punto } E\text{)}\end{align*}
$$

En autarquía `(Punto `$E$`)`, una unidad del bien `$X$` cuesta exactamente `$2$` unidades del bien `$Y$`, y el bienestar del consumidor representativo es `$U_E = \sqrt{3.53 \times 7.07} = \sqrt{25} = 5$`.


## Paso 4: Apertura de la Economía al Comercio Internacional `(Puntos `$E'$` y `$E''$`)`

Supongamos ahora que la economía se abre al libre comercio internacional, donde rigen los precios mundiales `$(P_X^I, P_Y^I)$`. En el mercado internacional se pagan **dos unidades de `$X$` por una de `$Y$`** `(por ejemplo, `$P_X^I = 1$` y `$P_Y^I = 2$`)`, es decir:

$$
\begin{align*}\frac{P_X^I}{P_Y^I} = \frac{1}{2}\end{align*}
$$

Observemos que con el libre comercio **se separan la decisión de producción `(Punto `$E'$`)` y la decisión de consumo `(Punto `$E''$`)`**:

### 1. El Nuevo Punto de Producción Óptima `$(E')$`

Las firmas nacionales ajustan su producción sobre la FPP hasta que la Tasa Marginal de Transformación iguale el nuevo precio relativo internacional `$\frac{P_X^I}{P_Y^I} = \frac{1}{2}$`:

$$
\begin{align*}|TMT| = \frac{4 X}{Y} = \frac{1}{2} \implies 8 X = Y \implies \boxed{64 X^2 = Y^2}\end{align*}
$$

Reemplazando `$Y^2 = 64 X^2$` dentro de la FPP `$(4X^2 + Y^2 = 100)$`:

$$
\begin{align*}4 X^2 + 64 X^2 = 100 \implies 68 X^2 = 100 \implies X^2 = \frac{100}{68} \implies \boxed{X_{E'}^* = \sqrt{\frac{100}{68}} \approx 1.21}\end{align*}
$$

Sustituyendo `$X_{E'}^* \approx 1.21$` en `$Y = 8 X$`:

$$
\begin{align*}\boxed{Y_{E'}^* = 8 \sqrt{\frac{100}{68}} \approx 9.70} \quad \text{(Punto } E'\text{ de producción)}\end{align*}
$$

Como el mundo valora mucho más el bien `$Y$` que antes `(en autarquía `$P_X/P_Y = 2$`, ahora `$P_X^I/P_Y^I = 1/2$`)`, el país se especializa parcialmente hacia su ventaja comparativa: **aumenta la producción de `$Y$` de `$7.07$` a `$9.70$`** y reduce la de `$X$` de `$3.53$` a `$1.21$`.

### 2. La Riqueza y el Nuevo Consumo `$(E'')$`

Fijando los precios internacionales `$P_X^I = 1$` y `$P_Y^I = 2$`, el valor monetario total de la producción nacional `(la renta o riqueza `$R$` de la economía)` es:

$$
\begin{align*}R = P_X^I X_{E'}^* + P_Y^I Y_{E'}^* = 1 \times (1.21) + 2 \times (9.70) = \boxed{20.61}\end{align*}
$$

Ahora el consumidor representativo maximiza su utilidad sujeto a la recta presupuestaria internacional de riqueza `$R = 20.6$`:

$$
\begin{align*}\max_{\{X_C, Y_C\}} \quad U(X_C, Y_C) = X_C^{1/2} Y_C^{1/2} \quad \text{s.a.} \quad 20.6 = 1 \cdot X_C + 2 \cdot Y_C\end{align*}
$$

Como la utilidad es Cobb-Douglas con exponentes `$\frac{1}{2}$` y `$\frac{1}{2}$`, el consumidor gasta la mitad de su ingreso en cada bien:

$$
\begin{align*}X_C^* &= \frac{1}{2} \left( \frac{R}{P_X^I} \right) = \frac{1}{2} \left( \frac{20.6}{1} \right) = \boxed{10.30} \\ Y_C^* &= \frac{1}{2} \left( \frac{R}{P_Y^I} \right) = \frac{1}{2} \left( \frac{20.6}{2} \right) = \boxed{5.15} \quad \text{(Punto } E''\text{ de consumo)}\end{align*}
$$

### Balance de Exportaciones, Importaciones y Ganancia de Bienestar

| Indicador Económico | Economía Cerrada `(Autarquía `$E$`)` | Economía Abierta: Producción `$(E')$` | Economía Abierta: Consumo `$(E'')$` | Comercio Exterior `$(E'' - E')$` |
| :--- | :---: | :---: | :---: | :--- |
| **Bien `$X$`** | `$3.53$` | `$1.21$` | `$10.30$` | **Importa** `$10.30 - 1.21 = 9.09$` unidades de `$X$` |
| **Bien `$Y$`** | `$7.07$` | `$9.70$` | `$5.15$` | **Exporta** `$9.70 - 5.15 = 4.55$` unidades de `$Y$` |
| **Precios relativos `$P_X/P_Y$`** | `$2.00$` | `$0.50$` | `$0.50$` | Balanza comercial equilibrada `$(1(9.09) \approx 2(4.55))$` |
| **Utilidad `$U = \sqrt{X_C Y_C}$`** | **`$5.00$`** | — | **`$7.28$`** | **Ganancia neta de bienestar `$( \Delta U = +2.28 > 0 )$`** |

> **Conclusión fundamental sobre los Tratados de Libre Comercio (TLC):** Aun cuando al abrirse al comercio la economía produzca excedentes en un sector que deben exportarse `$(Y)$` y faltantes en otro que deben importarse `$(X)$`, **el libre comercio expande el conjunto de posibilidades de consumo más allá de la FPP nacional**, permitiendo alcanzar una curva de indiferencia estrictamente superior `$(E'' \succ E)$`.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/comercio-apertura-light.svg" alt="FPP elíptica con tangencia autárquica E, tangencia productiva E' con precios mundiales y consumo E'' sobre indiferencia superior." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/comercio-apertura-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el comercio separa producir de consumir; se produce con precios mundiales y se consume más allá.</figcaption>
</figure>


<IdeaClave>

Abrirse al comercio separa dónde se produce de dónde se consume, y el consumo termina fuera de la propia frontera.

</IdeaClave>
