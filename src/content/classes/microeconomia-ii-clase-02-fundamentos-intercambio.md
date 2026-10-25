---
title: "Clase 02: Topología de Preferencias, Deseabilidad, Convexidad y Producción"
course: "microeconomia-ii"
order: 2
classType: "clase"
description: "Formalización matemática y geométrica de la monotonicidad, no saciabilidad local (LNS), conjuntos de contorno, convexidad estricta, continuidad de preferencias y conjuntos de producción convexos."
math: true
conceptos: ["Monotonicidad", "Preferencias convexas", "Continuidad"]
---

## El Espacio de Consumo y las Relaciones de Preferencia

Sea `$X = \mathbb{R}_+^n$` el conjunto de consumo, donde cada cesta `$x = (x_1, x_2, \ldots, x_n) \in X$` especifica cantidades no negativas de los `$n$` bienes disponibles en la economía. Para el análisis geométrico en el plano trabajaremos con dos bienes: `$x = (x_1, x_2) \in \mathbb{R}_+^2$`.

Sobre el conjunto `$X$` definimos una relación binaria de **preferencia débil `$\succcurlyeq$`** (*"es al menos tan bueno como"*), a partir de la cual se derivan:

1. **Preferencia estricta `$(y \succ x)$`:** `$y \succ x \iff (y \succcurlyeq x) \land \neg(x \succcurlyeq y)$`.
2. **Indiferencia `$(y \sim x)$`:** `$y \sim x \iff (y \succcurlyeq x) \land (x \succcurlyeq y)$`.

### Los Dos Axiomas de Racionalidad

Decimos que las preferencias `$\succcurlyeq$` del consumidor son **racionales** si satisfacen:
* **Completitud:** Para cualesquiera dos cestas `$x, y \in X$`, se cumple `$x \succcurlyeq y$`, o bien `$y \succcurlyeq x$`, o ambas `$(x \sim y)$`. *(Nota: al evaluar `$y = x$`, la completitud implica automáticamente la **reflexividad** `$x \succcurlyeq x$`).*
* **Transitividad:** Para cualesquiera tres cestas `$x, y, z \in X$`, si `$x \succcurlyeq y$` y `$y \succcurlyeq z$`, entonces `$x \succcurlyeq z$`.


## Axiomas de Deseabilidad: Monotonicidad y No Saciabilidad Local

Para que el consumidor desee adquirir bienes y agote su presupuesto al optimizar, imponemos axiomas sobre "cuánto más es mejor". Es crucial distinguir tres niveles de exigencia matemática (del más fuerte al más general):

### 1. Monotonicidad (o Monotonicidad Débil)

Para que una cesta `$y$` sea estrictamente preferida a `$x$`, basta con que contenga **estrictamente más de todos y cada uno de los bienes**. Usando la notación vectorial `$y \gg x \iff y_i > x_i, \; \forall i = 1, \ldots, n$`:

$$
\begin{align*}y \gg x \implies y \succ x \quad \text{(y si } y \geq x \implies y \succcurlyeq x\text{)}\end{align*}
$$

* **Implicación geométrica:** Debe aumentar estrictamente cada bien para garantizar un salto a una curva de indiferencia superior. Esta definición permite que las curvas de indiferencia tengan tramos horizontales/verticales (como en la función de proporciones fijas de Leontief `$U = \min\{x_1, x_2\}$`).

### 2. Monotonicidad Estricta (o Fuerte)

Basta con **aumentar la cantidad de al menos un bien sin reducir la de ningún otro** para que el consumidor esté estrictamente mejor. Usando la notación `$y \geq x \iff y_i \geq x_i, \; \forall i$` con `$y \neq x$`:

$$
\begin{align*}y \geq x, \; y \neq x \implies y \succ x\end{align*}
$$

* **Implicación geométrica:** Todas las utilidades marginales son estrictamente positivas `$(UMg_i > 0)$`, por lo que las curvas de indiferencia tienen pendiente estrictamente negativa y no pueden tener segmentos planos ni grosor.

### 3. No Saciabilidad Local (LNS — *Local Non-Satiation*)

Es el supuesto más débil y elegante requerido para demostrar el **Primer Teorema Fundamental del Bienestar** y el cumplimiento de la **Ley de Walras** con igualdad presupuestaria.

Formalmente, las preferencias satisfacen **No Saciabilidad Local (LNS)** si para toda cesta `$x \in X$` y para cualquier radio `$\varepsilon > 0$` (por pequeño que sea), existe siempre al menos otra cesta `$y \in X$` dentro de la bola abierta de radio `$\varepsilon$` centrada en `$x$` que es estrictamente preferida a `$x$`:

$$
\begin{align*}\forall x \in X, \; \forall \varepsilon > 0, \; \exists y \in X \quad \text{tal que} \quad \|y - x\| < \varepsilon \quad \text{y} \quad y \succ x\end{align*}
$$

* **Interpretación clave:** La condición LNS exige que en la vecindad inmediata de cualquier cesta **exista al menos una dirección de mejora** (incluso si algún "mal" tuviera que reducirse), sin afirmar necesariamente que aumentar todos los bienes sea mejor.
* **Qué prohíbe LNS:** Prohíbe la existencia de **puntos de saciedad locales** (cimas o puntos de felicidad máxima absoluta alrededor de los cuales ninguna pequeña variación mejora al individuo) y prohíbe las **zonas de indiferencia gruesas** (*thick indifference curves*).
* **Jerarquía lógica de implicación:**

$$
\begin{align*}\text{Monotonicidad Estricta} \implies \text{Monotonicidad Débil} \implies \text{No Saciabilidad Local (LNS)}\end{align*}
$$

<figure class="eco-figure">
  <img src="/assets/figures/micro2/axiomas-monotonicidad-light.svg" alt="Tres paneles: cuadrante noreste, borde norte o este, y bola epsilon con un punto mejor." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/axiomas-monotonicidad-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: monotonicidad exige el cuadrante; la estricta admite el borde; LNS solo un punto mejor arbitrariamente cerca.</figcaption>
</figure>



## Los Tres Objetos Topológicos del Mapa de Preferencias

Dada una cesta de referencia `$x \in X$`, el espacio de consumo se particiona en **tres objetos matemáticos distintos** que nunca deben confundirse:

1. **Curva (o conjunto) de indiferencia de `$x$`:** Es el lugar geométrico de las cestas que brindan exactamente el **mismo bienestar** que `$x$`:

$$
\begin{align*}I(x) = \{y \in X : y \sim x\}\end{align*}
$$

2. **Conjunto de contorno superior de `$x$` (*Upper Contour Set*):** Es el conjunto de todas las cestas que son **al menos tan buenas** como `$x$` (la curva de indiferencia más toda la región situada por encima y a la derecha):

$$
\begin{align*}U(x) = \{y \in X : y \succcurlyeq x\}\end{align*}
$$

3. **Conjunto de contorno inferior de `$x$` (*Lower Contour Set*):** Es el conjunto de todas las cestas que son **a lo sumo tan buenas** como `$x$`:

$$
\begin{align*}L(x) = \{y \in X : x \succcurlyeq y\}\end{align*}
$$

> **Distinción fundamental:** La **convexidad** de las preferencias se define rigurosamente sobre el **conjunto de contorno superior `$U(x)$`** (que es una región sólida del plano), y **no** sobre la línea aislada de la curva de indiferencia `$I(x)$`.


## Convexidad y Convexidad Estricta de las Preferencias

La convexidad formaliza la **preferencia por la diversidad o por las mezclas balanceadas** frente a los extremos. Dadas dos cestas `$y, z \in X$`, una combinación lineal convexa (o mezcla promedio) para cualquier peso `$\lambda \in (0, 1)$` es:

$$
\begin{align*}m = \lambda y + (1 - \lambda) z\end{align*}
$$

Geométricamente, a medida que `$\lambda$` recorre el intervalo `$(0, 1)$`, el punto `$m$` traza el segmento de recta que une a `$y$` con `$z$`.

### 1. Preferencias Convexas (Débiles)

Las preferencias son **convexas** si, para toda cesta `$x \in X$`, el conjunto de contorno superior `$U(x) = \{y \in X : y \succcurlyeq x\}$` es un **conjunto convexo**. Equivalentemente:

$$
\begin{align*}\text{Si } y \succcurlyeq x \text{ y } z \succcurlyeq x \implies \lambda y + (1 - \lambda) z \succcurlyeq x, \quad \forall \lambda \in [0, 1]\end{align*}
$$

En particular, si tomamos dos cestas sobre la misma curva de indiferencia `$(y \sim z)$`, el segmento que las une permanece íntegramente dentro del conjunto superior `$(m = \lambda y + (1 - \lambda) z \succcurlyeq y \sim z)$`. Esto **permite tramos rectos (lineales)** en las curvas de indiferencia (como en los bienes sustitutos perfectos `$U = ax_1 + bx_2$`, donde `$m \sim y \sim z$`).

### 2. Preferencias Estrictamente Convexas

Las preferencias son **estrictamente convexas** si la mezcla de dos cestas distintas igualmente buenas (o al menos tan buenas como `$x$`) es **estrictamente preferida**:

$$
\begin{align*}\text{Si } y \neq z, \; y \succcurlyeq x \text{ y } z \succcurlyeq x \implies \lambda y + (1 - \lambda) z \succ x, \quad \forall \lambda \in (0, 1)\end{align*}
$$

En términos de una curva de indiferencia: si `$y \neq z$` y `$y \sim z$`, su promedio `$m = \lambda y + (1 - \lambda) z$` cae en el **interior estricto** del conjunto superior `$(m \succ y \sim z)$`.

* **Consecuencia para el equilibrio general:**
  * Con **convexidad débil**, la demanda del consumidor a unos precios dados es una correspondencia convexa (puede haber un segmento de múltiples cestas óptimas).
  * Con **convexidad estricta**, la curva de indiferencia no tiene segmentos planos, la Relación Marginal de Sustitución `$(RMS)$` es estrictamente decreciente y **la cesta que maximiza la utilidad del consumidor para cualquier vector de precios `$p \gg 0$` es única**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/convexidad-light.svg" alt="Dos paneles: curva con tramo lineal y punto medio en el borde, frente a curva estricta con la cuerda por encima." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/convexidad-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: convexa admite tramos lineales; estrictamente convexa premia la mezcla.</figcaption>
</figure>



## Continuidad de las Preferencias

¿Qué significa que un consumidor no cambie bruscamente de opinión ante variaciones infinitesimales en las cantidades de una canasta?

Decimos que las preferencias `$\succcurlyeq$` son **continuas** si, para toda cesta `$x \in X$`, tanto el conjunto de contorno superior `$U(x) = \{y \in X : y \succcurlyeq x\}$` como el conjunto de contorno inferior `$L(x) = \{y \in X : x \succcurlyeq y\}$` son **conjuntos cerrados** (contienen a todos sus puntos frontera, que son precisamente la curva de indiferencia `$I(x)$`).

### Formulación mediante Sucesiones Convergentes

Equivalentemente, si tenemos una sucesión de canastas `$\{y^n\}_{n=1}^\infty$` tales que cada una de ellas es al menos tan buena como `$x$` `$(y^n \succcurlyeq x, \; \forall n)$`, y dicha sucesión converge a una canasta límite `$y$` `$(y^n \to y)$`, entonces la canasta límite también debe ser al menos tan buena como `$x$`:

$$
\begin{align*}\text{Si } y^n \succcurlyeq x \quad \forall n \quad \text{y} \quad y^n \to y \implies y \succcurlyeq x\end{align*}
$$

* **Mensaje clave:** La continuidad evita saltos discontinuos en el orden de preferencias (como ocurre en las **preferencias lexicográficas**, que violan este axioma). Gracias a la continuidad:
  1. Existe una **función de utilidad continua `$u(x)$`** que representa a las preferencias (`$y \succcurlyeq x \iff u(y) \geq u(x)$`, **Teorema de Debreu**).
  2. Las funciones de demanda `$x(p, w)$` y de exceso de demanda `$Z(p)$` varían de manera continua ante cambios en los precios, requisito indispensable para aplicar el **Teorema del Punto Fijo de Brouwer** y demostrar la existencia del equilibrio general.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/continuidad-light.svg" alt="Curva de indiferencia separando el conjunto superior sombreado del inferior, con una secuencia de puntos convergiendo dentro del superior." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/continuidad-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: continuidad cierra los conjuntos de contorno; el límite de lo mejor sigue siéndolo.</figcaption>
</figure>



## Geometría del Lado de la Producción: Conjuntos Convexos y Funciones Cóncavas

En la teoría de la firma de equilibrio general, representamos la tecnología mediante el **conjunto de producción `$Y$`**, cuyos elementos son planes tecnológicos de insumo-producto `$(x, q)$`, donde `$x \geq 0$` es el insumo utilizado y `$q \geq 0$` es el producto obtenido. La frontera superior de `$Y$` está descrita por la **función de producción `$q = f(x)$`**.

### 1. Conjunto de Producción Convexo

El conjunto de producción `$Y$` es **convexo** si dados dos planes tecnológicos factibles cualesquiera `$y, y' \in Y$`, cualquier combinación lineal convexa (o promedio ponderado) de ambos también es tecnológicamente factible:

$$
\begin{align*}y, y' \in Y \implies \lambda y + (1 - \lambda) y' \in Y, \quad \forall \lambda \in (0, 1)\end{align*}
$$

* **Interpretación económica:** Es posible operar simultáneamente a escala fraccionaria una combinación de dos procesos productivos factibles. La convexidad de `$Y$` equivale a asumir **rendimientos a escala no crecientes** (constantes o decrecientes), descartando las economías de escala crecientes que destruirían la competencia perfecta.

### 2. Conjunto de Producción Estrictamente Convexo

El conjunto `$Y$` es **estrictamente convexo** si para dos planes eficientes distintos (`$y \neq y'$` sobre la frontera), su mezcla promedio queda en el **interior estricto** del conjunto de producción `$(int(Y))$`, generando una **holgura productiva**:

$$
\begin{align*}\text{Si } y \neq y' \implies \lambda y + (1 - \lambda) y' \in \text{int}(Y), \quad \forall \lambda \in (0, 1)\end{align*}
$$

* **Consecuencia fundamental:** Con la misma combinación promedio de insumos se puede alcanzar estrictamente más producto que el promedio de los productos individuales. Esto garantiza que, **dados los precios de mercado, el plan de producción que maximiza los beneficios de la empresa sea único** (rendimientos estrictamente decrecientes a escala).

### 3. Equivalencia con la Función de Producción Cóncava

Cuando existe un solo producto y hay libre disposición de insumos `$(Y = \{(x, q) : 0 \leq q \leq f(x)\})$`, la convexidad del conjunto `$Y$` equivale exactamente a la **concavidad de la función de producción `$f(x)$`**:

$$
\begin{align*}f\big(\lambda x + (1 - \lambda) x'\big) \geq \lambda f(x) + (1 - \lambda) f(x')\end{align*}
$$

Si `$f(x)$` es dos veces diferenciable, la producción aumenta con el insumo pero su **Productividad Marginal `$(PMg)$` es decreciente** (más alta cuando el insumo es escaso en `$A$` y más baja cuando el insumo es abundante en `$B$`):

$$
\begin{align*}f'(x) > 0 \quad \text{y} \quad f''(x) < 0 \qquad \iff \qquad f \text{ cóncava} \iff Y \text{ convexo}\end{align*}
$$

| Propiedad Topológica | Lado del Consumidor (Preferencias) | Lado de la Firma (Tecnología) |
| :--- | :--- | :--- |
| **Objeto convexo** | Conjunto de contorno superior `$U(x) = \{y : y \succcurlyeq x\}$` | Conjunto de posibilidades de producción `$Y$` |
| **Función asociada** | Función de utilidad **cuasicóncava** `$u(x)$` | Función de producción **cóncava** `$f(x)$` `$(f''(x) < 0)$` |
| **Tasa marginal** | `$RMS$` decreciente a lo largo de `$I(x)$` | Productividad marginal `$PMg = f'(x)$` decreciente |
| **Consecuencia de estrictez** | Unicidad de la cesta demandada `$x^*(p, w)$` | Unicidad del plan óptimo que maximiza beneficios `$y^*(p)$` |

<figure class="eco-figure">
  <img src="/assets/figures/micro2/produccion-concava-light.svg" alt="Función de producción cóncava con dos planes eficientes, tangentes de distinta pendiente y brecha de holgura en el insumo promedio." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/produccion-concava-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: rendimientos decrecientes hacen convexo al conjunto; promediar insumos rinde más que promediar productos.</figcaption>
</figure>


<IdeaClave>

Monotonicidad, convexidad y continuidad no son caprichos: son lo mínimo para que la demanda exista y se comporte bien.

</IdeaClave>
