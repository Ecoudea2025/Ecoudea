---
title: "Clase 11: El sistema de precios y su equilibrio"
course: "economia-clasica"
order: 11
classType: "clase"
description: "Capital, tasa de ganancia y el ejemplo Sraffa 2×2: de precios de desequilibrio al precio de equilibrio con r uniforme."
math: true
conceptos: ["Sistema de precios", "Numerario", "Tasa de ganancia"]
---

## Puente: de la vara al sistema

La clase 10 midió un intercambio. Ahora medimos **todos a la vez**: a cada sistema de producción le corresponde un sistema de precios, con una hipótesis fuerte —**precio único** por mercancía (información completa, Mill). Veremos cuándo ese sistema reproduce y cuándo incentiva a moverse.

## Variables

* **Capital `$K_i$`**: valor de insumos + subsistencias adelantados en `$i$`.
* **Tasa de ganancia `$r_i = m_i/K_i$`**: beneficio por unidad de capital.
* **Precio de equilibrio**: reproduce todo y deja `$r$` uniforme. **De mercado**: no lo logra.

<Definicion>
**Capital**: valor mercantil de los bienes usados en producir (medios estrictos + subsistencias). **Tasa de ganancia**: `$r_i = m_i / K_i$`.
</Definicion>

## El ejemplo Sraffa 2×2 (trigo-hierro, trigo numerario)

### Paso 1: Sistema con ganancias distintas

$$
\begin{align*}\tfrac{56}{115} + \tfrac{12}{575}p_{21} + m_1 &= 1 \\ 6 + \tfrac{2}{5}p_{21} + m_2 &= p_{21}\end{align*}
$$

Con `$p_{21} = 10$`: el trigo gana `$r_1 = 43{,}75\%$`, el hierro `$r_2 = 0\%$`. Todo el excedente lo apropia el trigo. Los recursos **migrarán** al trigo, su oferta subirá y `$p_{21}$` subirá.

<details>
<summary>Verificación de `$r_1 = 43{,}75\%$` paso a paso</summary>

Capital adelantado en trigo: `$K_1 = \frac{56}{115} + \frac{12}{575} \times 10 = 0{,}487 + 0{,}209 = 0{,}696$`. Beneficio: `$m_1 = 1 - 0{,}696 = 0{,}304$`. Tasa: `$r_1 = 0{,}304 / 0{,}696 = 0{,}4375$`. En hierro: `$K_2 = 6 + \frac{2}{5} \times 10 = 10$` que iguala al producto `$p_{21} = 10$`: `$m_2 = 0$`. Todo el excedente va al trigo porque solo él rinde.

</details>

### Paso 2: El caso espejo

Con `$p_{21} = 24{,}58$`: `$r_1 = 0\%$`, `$r_2 = 55{,}26\%$`. Ahora todo lo apropia el hierro y los recursos migran al revés; `$p_{21}$` bajará. Conclusión: `$p_{21}$` **fluctúa** entre `$10$` y `$24{,}58$` mientras las rentabilidades difieran: es precio **de desequilibrio**.

### Paso 3: Imponer igual rentabilidad

Con `$r_1 = r_2 = r$` el sistema se cierra (`$n$` ecuaciones, `$n-1$` relativos + `$r$`) y da solución única desde la técnica:

$$
\begin{align*}p_{21} = 15, \quad r = 25\%\end{align*}
$$

A `$p_{21} = 15$` ambos reponen capitales y ganan `$25\%$`: nadie migra, la composición no cambia, ninguna fuerza mueve el precio. Es precio **de equilibrio** (de producción o natural).

<figure class="eco-figure">
  <img src="/assets/figures/clasica/gravitacion-light.svg" alt="El precio de mercado oscila entre 10 y 24.58 y converge al precio natural 15, donde ambas tasas igualan 25%." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/gravitacion-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: los precios de mercado gravitan en torno al natural; la igualación de tasas es el imán.</figcaption>
</figure>

<figure class="eco-figure">
  <img src="/assets/figures/clasica/sistema-precios-2x2-light.svg" alt="Curvas de tasa de ganancia de trigo y hierro que se cruzan en p*=15 con r=25%, con los desequilibrios A y B." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/sistema-precios-2x2-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: los precios corrientes dan rentabilidades distintas; solo en p* = 15 ambas coinciden.</figcaption>
</figure>

## Formas del sistema (referencia rápida)

* Desequilibrio: `$(\mathbf{I}+\hat{\mathbf{r}})\mathbf{B}\mathbf{p} = \mathbf{p}$` (subdeterminado: `$n$` ecuaciones, `$2n-1$` incógnitas; lo cierra oferta-demanda, unidad 6).
* Equilibrio ricardiano: `$\mathbf{B}\mathbf{p}(1+r) = \mathbf{p}$` (`$n$` ecuaciones, `$n$` incógnitas; solución simultánea de precios y `$r$`).
* Formas equivalentes: `$(\mathbf{A}\mathbf{p}+\mathbf{l}\mathbf{s}\mathbf{p})(1+r) = \mathbf{p}$`, `$(\mathbf{A}\mathbf{p}+\mathbf{l}w)(1+r) = \mathbf{p}$` con `$w = \mathbf{s}\mathbf{p}$`.

## Interpretación económica

1. **Simultaneidad**: el excedente se reparte en proporción al capital **y** esa proporción exige conocer precios: precios y distribución se determinan **a la vez** (Sraffa).
2. **El precio como distribuidor**: cada `$p_{21}$` es un reparto del excedente; solo `$15$` reparte proporcional al capital.
3. **Equilibrio observable en sus efectos**: no se "ve" el `$15$`; se ve que a `$15$` nadie se mueve.

<IdeaClave>
Memoriza el trío `$10 \to 15 \to 24{,}58$`: dos desequilibrios espejo y un centro que los anula. Es el ADN de la gravitación (unidad 6).
</IdeaClave>
