---
title: "Clase 09: Externalidades, Pigou y Coase"
course: "microeconomia-ii"
order: 11
classType: "clase"
description: "Tipología de externalidades en producción y consumo, divergencia entre costos y beneficios privados y sociales, deducción paso a paso del impuesto de Pigou, Teorema de Coase y mercados de permisos transferibles."
math: true
conceptos: ["Externalidad", "Impuesto pigouviano", "Teorema de Coase"]
---

## ¿Por qué Falla la Mano Invisible? El Concepto de Externalidad

En la Clase 01 vimos que el **Primer Teorema Fundamental del Bienestar** requiere la **ausencia total de externalidades (principio de exclusión)**: que las acciones de consumo o producción de un agente afecten a los demás única y exclusivamente a través de los precios de mercado.

Decimos que existe una **externalidad** cuando la acción de un consumidor o de una empresa entra directamente en la función de utilidad de otro consumidor o en la función de producción/costos de otra empresa **sin que dicho efecto sea compensado ni tenga un precio en el mercado**.

### Tipología de las Externalidades

| Tipo de Externalidad | En la Producción `$(C_j(q_j, q_i))$` | En el Consumo `$(U_j(x_j, x_i))$` | Divergencia Marginal |
| :--- | :--- | :--- | :--- |
| **Negativa** (Genera costos externos) | Fábrica química que contamina el río de una pesquería aguas abajo. | Fumador en un espacio cerrado, ruido urbano o congestión vehicular. | `$CMgS > CMgP$` `(o `$BMgS < BMgP$`)` `$\implies$` **Sobreproducción** `$(q_M > q^*)$` |
| **Positiva** (Genera beneficios externos) | Apicultor cuyas abejas polinizan el huerto vecino; I+D tecnológico. | Vacunación contra epidemias, educación o restauración de fachadas. | `$BMgS > BMgP$` `(o `$CMgS < CMgP$`)` `$\implies$` **Subproducción** `$(q_M < q^*)$` |


## Modelación Matemática Paso a Paso: Externalidad Negativa en la Producción

Consideremos dos empresas competitivas:
1. **Firma 1 (Acero / Papelera):** Produce `$q_1$` unidades del bien 1, el cual vende al precio competitivo `$P_1$`. Su función de costos privados es estrictamente convexa: `$C_1(q_1)$` con `$C_1'(q_1) > 0$` y `$C_1''(q_1) > 0$`. Al producir `$q_1$`, genera simultáneamente contaminación `$e = e(q_1)$` `(por simplicidad, `$e = q_1$`)`.
2. **Firma 2 (Pesquería / Agricultura):** Produce `$q_2$` unidades del bien 2 al precio `$P_2$`, pero sus costos dependen tanto de su propia producción `$q_2$` como de la contaminación `$q_1$` emitida por la Firma 1:

$$
\begin{align*}C_2(q_2, q_1), \quad \text{con } \frac{\partial C_2}{\partial q_1} > 0 \quad \text{(Costo Marginal Externo } CMgExt > 0\text{)}\end{align*}
$$

### Paso 1: El Equilibrio Descentralizado de Mercado `$(q_1^M)$`

Si no hay regulación ni derechos de propiedad sobre el río, cada empresa maximiza su beneficio privado ignorando el daño causado a la otra:

* **Problema privado de la Firma 1:**

$$
\begin{align*}\max_{\{q_1\}} \quad \Pi_1 = P_1 q_1 - C_1(q_1)\end{align*}
$$

* **Condición de Primer Orden privada:**

$$
\begin{align*}\frac{\text{d}\Pi_1}{\text{d}q_1} = P_1 - C_1'(q_1) = 0 \implies \boxed{P_1 = C_1'(q_1^M) \equiv CMgP(q_1^M)}\end{align*}
$$

La Firma 1 produce hasta donde su **Costo Marginal Privado `$(CMgP)$`** iguala al precio `$P_1$`, ignorando por completo que cada unidad producida eleva los costos de la Firma 2 en `$\frac{\partial C_2}{\partial q_1} > 0$`.

### Paso 2: El Óptimo Social de Pareto `$(q_1^*)$`

Un planificador social (o ambas empresas fusionadas en una sola corporación) maximiza el **beneficio conjunto** de ambas actividades:

$$
\begin{align*}\max_{\{q_1, q_2\}} \quad \Pi_{\text{Social}} = \Big[ P_1 q_1 - C_1(q_1) \Big] + \Big[ P_2 q_2 - C_2(q_2, q_1) \Big]\end{align*}
$$

* **Condición de Primer Orden social respecto a `$q_1$`:**

$$
\begin{align*}\frac{\partial \Pi_{\text{Social}}}{\partial q_1} = P_1 - C_1'(q_1) - \frac{\partial C_2(q_2, q_1)}{\partial q_1} = 0\end{align*}
$$

Reordenando términos, obtenemos la **regla de eficiencia social**:

$$
\begin{align*}\boxed{P_1 = \underbrace{C_1'(q_1^*)}_{CMgP} + \underbrace{\frac{\partial C_2(q_2^*, q_1^*)}{\partial q_1}}_{CMgExt} \equiv CMgS(q_1^*)}\end{align*}
$$

### Paso 3: Demostración de la Sobreproducción `$(q_1^M > q_1^*)$`

Como el daño marginal externo es estrictamente positivo `$\left(\frac{\partial C_2}{\partial q_1} > 0\right)$`, en el óptimo social se cumple:

$$
\begin{align*}C_1'(q_1^*) = P_1 - \frac{\partial C_2}{\partial q_1} < P_1 = C_1'(q_1^M)\end{align*}
$$

Dado que el costo marginal privado es creciente `$(C_1'' > 0)$`, el hecho de que `$C_1'(q_1^*) < C_1'(q_1^M)$` implica inequívocamente que:

$$
\begin{align*}\boxed{q_1^M > q_1^*}\end{align*}
$$

El mercado sin regulación **produce demasiado del bien contaminante** y genera una **pérdida irrecuperable de eficiencia (peso muerto)** igual al área entre `$CMgS$` y `$P_1$` desde `$q_1^*$` hasta `$q_1^M$`.


## Soluciones Públicas y Privadas a las Externalidades

### 1. El Impuesto Pigouviano (Arthur Cecil Pigou, 1920)

Para lograr que la Firma 1 internalice el daño externo sin necesidad de prohibir su actividad, el Estado puede cobrar un **impuesto correctivo `$t^*$` por unidad producida (o emitida)** exactamente igual al **Costo Marginal Externo evaluado en el óptimo social `$q_1^*$`**:

$$
\begin{align*}\boxed{t^* = \frac{\partial C_2(q_2^*, q_1^*)}{\partial q_1} = CMgExt(q_1^*)}\end{align*}
$$

**Verificación:** Con el impuesto `$t^*$`, el nuevo beneficio privado de la Firma 1 es `$\Pi_1 = P_1 q_1 - C_1(q_1) - t^* q_1$`. Su nueva condición de primer orden privada es:

$$
\begin{align*}\frac{\text{d}\Pi_1}{\text{d}q_1} = P_1 - C_1'(q_1) - t^* = 0 \implies P_1 = C_1'(q_1) + \frac{\partial C_2(q_2^*, q_1^*)}{\partial q_1}\end{align*}
$$

¡La empresa elige voluntariamente producir `$q_1 = q_1^*$`! *(Si la externalidad es positiva, `$t^* < 0$` corresponde a un **subsidio pigouviano** igual al Beneficio Marginal Externo `$BMgExt(q^*)$`).*

### 2. El Teorema de Coase (Ronald Coase, 1960)

¿Es siempre indispensable que el Estado intervenga con un impuesto pigouviano? **Ronald Coase** revolucionó la microeconomía al demostrar que el origen profundo de la externalidad es la **ausencia de derechos de propiedad claramente definidos** sobre el recurso (el aire o el río).

> **Enunciado del Teorema de Coase:**
> *"Si los **derechos de propiedad están claramente definidos y protegidos**, y si los **costos de transacción son nulos `$(CT = 0)$`** (y no hay efectos riqueza sobre la valoración marginal, como ocurre con utilidades cuasilineales o beneficios empresariales), entonces la negociación voluntaria entre las partes llevará siempre a la **misma asignación eficiente en el sentido de Pareto `$(q_1^*)$`**, **independientemente de a quién se le asigne inicialmente el derecho de propiedad**."*

**Demostración de la invariancia de `$q_1^*$` (pero no de la distribución de riqueza):**
* **Caso A (El derecho al río limpio pertenece a la Pesquería 2):** La Firma 1 no puede contaminar sin permiso. Para producir la unidad `$q_1$`, la Firma 1 le ofrece un pago compensatorio a la Firma 2. Mientras el beneficio marginal neto de la Firma 1 `$(P_1 - C_1'(q_1))$` supere el daño marginal causado a la Firma 2 `$\left(\frac{\partial C_2}{\partial q_1}\right)$`, ambas ganan negociando hasta alcanzar exactamente **`$P_1 - C_1'(q_1^*) = \frac{\partial C_2}{\partial q_1} \iff q_1^*$`**.
* **Caso B (El derecho a usar el río pertenece a la Papelera 1):** La Firma 2 le ofrece pagar a la Firma 1 para que reduzca su producción desde `$q_1^M$`. Mientras el daño evitado por la Firma 2 `$\left(\frac{\partial C_2}{\partial q_1}\right)$` sea mayor que el beneficio sacrificado por la Firma 1 `$(P_1 - C_1'(q_1))$`, la Firma 2 le paga a la Firma 1 para recortar la producción exactamente hasta llegar a **`$q_1^*$`**.
* **Límite práctico (Conexión con Clase 01):** Cuando hay miles de afectados (por ejemplo, contaminación atmosférica de millones de automóviles), **los costos de transacción son altísimos `$(CT \gg 0)$`** y aparecen problemas de *free-rider* e información asimétrica, por lo que la negociación coaseana falla y se requiere regulación estatal (impuestos pigouvianos, normas de comando y control o mercados de permisos de emisión transferibles *cap-and-trade*).

<figure class="eco-figure">
  <img src="/assets/figures/micro2/pigou-externalidad-light.svg" alt="Precio horizontal, costo privado y social, cantidades privada y óptima, impuesto como llave y triángulo de pérdida." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/pigou-externalidad-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el impuesto pigouviano cierra la brecha; el triángulo es el bienestar quemado.</figcaption>
</figure>


<IdeaClave>

La externalidad es un precio faltante: Pigou lo pone con un impuesto, Coase con propiedad y negociación.

</IdeaClave>
