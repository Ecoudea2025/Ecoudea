---
title: "Clase 10: Bienes Públicos y Condición de Samuelson"
course: "microeconomia-ii"
order: 12
classType: "clase"
description: "Clasificación de los bienes según rivalidad y exclusión, deducción paso a paso de la Condición de Samuelson vs. bienes privados, subprovisión voluntaria por el problema del polizón (free-rider) y equilibrio de Lindahl."
math: true
conceptos: ["Bien público", "Condición de Samuelson", "Equilibrio de Lindahl"]
---

## Taxonomía Microeconómica de los Bienes: Rivalidad y Exclusión

Los bienes públicos constituyen una de las fallas más severas del mecanismo de precios. Para clasificar rigurosamente cualquier bien o servicio en la economía, evaluamos dos propiedades técnicas e institucionales:

1. **Rivalidad en el consumo:** Un bien es **rival** si el consumo de una unidad por parte de una persona impide o reduce física y simultáneamente su disfrute por parte de otra persona `$( \Delta x_i \implies \nabla x_j )$`. Es **no rival** si el costo marginal de que un individuo adicional disfrute del bien ya producido es exactamente cero `$(CMg_{\text{usuario adicional}} = 0)$`.
2. **Exclusión:** Un bien es **excluible** si es técnica, legal y económicamente factible (a bajo costo de transacción) impedir que quien no pague por él lo consuma.

| Clasificación de los Bienes | **Excluible** (Derechos de propiedad aplicables) | **No Excluible** (Imposible o muy costoso excluir) |
| :--- | :--- | :--- |
| **Rival en el consumo** `$(CMg_{\text{uso}} > 0)$` | **1. Bienes Privados Puros:** Pan, ropa, vivienda, automóviles `$(X = \sum_{i=1}^n x_i)$`. | **2. Recursos de Uso Común (Comunales):** Bancos de pesca en altamar, acuíferos, bosques abiertos *(Tragedia de los Comunes — Ostrom)*. |
| **No Rival en el consumo** `$(CMg_{\text{uso}} = 0)$` | **3. Bienes de Club (o Artificialmente Escasos):** Televisión por suscripción, autopistas con peaje sin congestión, parques privados. | **4. Bienes Públicos Puros:** Defensa nacional, alumbrado público, aire limpio, teoremas matemáticos `$(G = g_1 = g_2 = \ldots = g_n)$`. |


## Deducción Paso a Paso de la Condición de Samuelson (1954)

Consideremos una economía con `$n$` consumidores `$(i = 1, \ldots, n)$`, un **bien privado `$X$`** `(que se reparte entre los individuos: `$X = \sum_{i=1}^n x_i$`)` y un **bien público puro `$G$`** `(que todos consumen simultáneamente en la misma cantidad total: `$G$`)`.

* La utilidad de cada individuo `$i$` es `$U_i(x_i, G)$`.
* La tecnología de la economía está resumida por la **Frontera de Posibilidades de Producción (FPP)** implícita `$F(X, G) = 0$`, o explícitamente como el costo en unidades de bien privado `$C(G)$` necesario para producir `$G$` unidades de bien público, dada una dotación total de recursos `$W$`:

$$
\begin{align*}\sum_{i=1}^n x_i + C(G) = W\end{align*}
$$

donde `$C'(G) = \frac{\text{d}X}{\text{d}G} \equiv |TMT_{G, X}| = CMg_G$` es la **Tasa Marginal de Transformación** (el costo marginal social de producir una unidad más de bien público en términos de bien privado sacrificado).

### Paso 1: Planteamiento del Lagrangiano de Eficiencia de Pareto

Maximizamos la utilidad del individuo 1 sujeto a mantener constantes las utilidades de los demás individuos `$(U_i(x_i, G) = \underline{U}_i \text{ para } i = 2, \ldots, n)$` y sujeto a la restricción agregada de recursos:

$$
\begin{align*}\mathcal{L} = U_1(x_1, G) + \sum_{i=2}^n \mu_i \Big[ U_i(x_i, G) - \underline{U}_i \Big] + \lambda \left[ W - \sum_{i=1}^n x_i - C(G) \right]\end{align*}
$$

*(Definiendo `$\mu_1 \equiv 1$`, podemos escribir los primeros términos de manera compacta como `$\sum_{i=1}^n \mu_i U_i(x_i, G)$`).*

### Paso 2: Condiciones de Primer Orden respecto a `$x_i$` y respecto a `$G$`

1. **Derivamos respecto al consumo privado `$x_i$` de cada individuo `$(i = 1, \ldots, n)$`:**

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial x_i} = \mu_i \frac{\partial U_i}{\partial x_i} - \lambda = 0 \implies \mu_i = \frac{\lambda}{\dfrac{\partial U_i}{\partial x_i}}, \quad \forall i = 1, \ldots, n \qquad \text{(1)}\end{align*}
$$

2. **Derivamos respecto a la cantidad total del bien público `$G$`** `(observando que `$G$` entra simultáneamente en las `$n$` funciones de utilidad)`:

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial G} = \sum_{i=1}^n \mu_i \frac{\partial U_i}{\partial G} - \lambda C'(G) = 0 \qquad \text{(2)}\end{align*}
$$

### Paso 3: Sustitución y Obtención de la Condición de Samuelson

Sustituimos la expresión de `$\mu_i$` de `(1)` dentro de la ecuación `(2)`:

$$
\begin{align*}\sum_{i=1}^n \left( \frac{\lambda}{\dfrac{\partial U_i}{\partial x_i}} \right) \frac{\partial U_i}{\partial G} = \lambda C'(G)\end{align*}
$$

Cancelamos el multiplicador `$\lambda > 0$` en ambos lados y reconocemos que el cociente `$\frac{\partial U_i / \partial G}{\partial U_i / \partial x_i} \equiv RMS_{G, x_i}^i$` es la **Relación Marginal de Sustitución (o disposición marginal a pagar)** del individuo `$i$` por el bien público:

$$
\begin{align*}\boxed{\sum_{i=1}^n RMS_{G, x_i}^i = \sum_{i=1}^n \frac{\dfrac{\partial U_i}{\partial G}}{\dfrac{\partial U_i}{\partial x_i}} = C'(G) \equiv |TMT_{G, X}|}\end{align*}
$$

> **Contraste Fundamental entre Bienes Privados y Bienes Públicos:**
> * **En Bienes Privados (Suma Horizontal de Demandas):** Cada persona consume una cantidad distinta `$(x_i)$`, pero todas pagan el mismo precio marginal:
>
> 
$$
> \begin{align*}RMS^1 = RMS^2 = \ldots = RMS^n = |TMT|\end{align*}
> 
$$
>
> * **En Bienes Públicos (Suma Vertical de Disposiciones a Pagar — Condición de Samuelson):** Todos consumen exactamente la misma cantidad total `$(G)$`, por lo que el beneficio marginal social es la **suma vertical** de las valoraciones marginales de todos los ciudadanos:
>
> 
$$
> \begin{align*}RMS^1 + RMS^2 + \ldots + RMS^n = |TMT|\end{align*}
> 
$$


## El Problema del Polizón (*Free-Rider*) y la Subprovisión Voluntaria

¿Por qué fracasa el mercado privado cuando intenta proveer un bien público mediante contribuciones voluntarias?

Supongamos `$n$` individuos con utilidad cuasilineal `$U_i(x_i, G) = x_i + v_i(G)$` `(con `$v_i' > 0, \; v_i'' < 0$`)`, donde cada individuo `$i$` decide cuánto aportar voluntariamente `$(g_i \geq 0)$` de su riqueza `$w_i$` para financiar el bien público total `$G = g_i + G_{-i}$` `(siendo `$G_{-i} = \sum_{j \neq i} g_j$` lo que aportan los demás)`. Si el precio unitario de producir `$G$` es `$c$`, el individuo `$i$` resuelve:

$$
\begin{align*}\max_{\{g_i \geq 0\}} \quad w_i - c g_i + v_i(g_i + G_{-i})\end{align*}
$$

* **Condición de Equilibrio de Nash (provisión voluntaria):**
  Cada individuo iguala únicamente su **propio** beneficio marginal privado con el costo `$c$`:

  $$
  \begin{align*}v_i'(G^{\text{Nash}}) = c \quad \text{(para el individuo con mayor valoración)}\end{align*}
  $$

* **Condición de Samuelson (óptimo de Pareto):**
  La eficiencia social exige sumar los beneficios marginales de **todos** los `$n$` individuos:

  $$
  \begin{align*}\sum_{i=1}^n v_i'(G^*) = c\end{align*}
  $$

Como `$v_i' > 0$` y `$v_i'' < 0$`, se cumple estrictamente que **`$G^{\text{Nash}} < G^*$`**: cada agente actúa como **polizón (*free-rider*)** esperando beneficiarse gratis del aporte de los demás, lo que conduce a una severa **subprovisión (o provisión nula)** del bien público en el mercado privado.


## Mecanismos de Solución: Precios de Lindahl y Diseño de Mecanismos

1. **El Equilibrio de Precios Personalizados de Lindahl (Erik Lindahl, 1919):**
   Si un subastador pudiera cobrarle a cada ciudadano `$i$` una **participación impositiva personalizada `$s_i$`** por cada unidad de bien público `(tal que `$\sum_{i=1}^n s_i = c = CMg_G$`)` igual a su propia valoración marginal en el óptimo `$(s_i^* = RMS_{G, x_i}^i(G^*))$`, entonces todos los ciudadanos demandarían unánimemente la misma cantidad eficiente `$G^*$`:

   $$
   \begin{align*}\sum_{i=1}^n s_i^* = \sum_{i=1}^n RMS_{G, x_i}^i(G^*) = c\end{align*}
   $$

   * **Debilidad del mecanismo de Lindahl:** Si el gobierno le pregunta a cada ciudadano cuál es su valoración `$RMS^i$` para cobrarle `$s_i = RMS^i$`, cada ciudadano tiene incentivos estratégicos a **mentir y declarar `$RMS^i = 0$`** para no pagar impuestos (reaparece el *free-rider*).
2. **Mecanismo de Revelación Directa de Clarke-Groves (Vickrey-Clarke-Groves):**
   Diseña un impuesto de transferencia donde cada individuo sólo paga el costo social neto que su declaración le impone a los demás cuando su voto resulta **pivotal** (cambia la decisión colectiva), logrando que **decir la verdad sea una estrategia dominante**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/samuelson-vertical-light.svg" alt="Dos disposiciones marginales, su suma vertical, costo marginal, Nash frente a Samuelson y precios de Lindahl." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/samuelson-vertical-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: Figura: el bien público se suma en vertical; el free-rider aporta de menos.</figcaption>
</figure>


<IdeaClave>

El bien público se financia sumando disposiciones marginales en vertical, no igualando una sola al costo.

</IdeaClave>
