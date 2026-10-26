---
title: "Clase 20: La frontera salario-beneficio"
course: "economia-clasica"
order: 20
classType: "clase"
description: "Relación inversa w-r, tasa máxima R y lectura del conflicto distributivo en la frontera."
math: true
conceptos: ["Frontera salario-beneficio", "Tasa máxima de beneficio", "Mercancía patrón"]
---

## Puente: el antagonismo hecho curva

La clase 19 separó técnica y reparto. Ahora dibujamos el reparto: para cada salario posible, ¿qué tasa queda? La respuesta es una frontera decreciente —la forma geométrica del conflicto entre obreros y capitalistas.

## Variables

* `$R$`: tasa máxima de beneficio (con `$w = 0$`, todo el excedente a beneficios).
* `$\hat{W}$`: salario máximo (con `$r = 0$`, todo a salarios).
* `$w(r)$`: frontera; en general decreciente y (salvo patrón) no lineal.

<Definicion>
**Frontera salario-beneficio**: lugar geométrico de los pares `$(w, r)$` compatibles con la técnica dada. Moverse por ella es repartir el mismo excedente de otra manera.
</Definicion>

## Deducción paso a paso

### Paso 1: Los dos extremos

Con `$w = 0$` el sistema da `$R$` (tasa física del sistema, prima de la homotecia). Con `$r = 0$` da `$\hat{W}$` (todo el neto a salarios). Ambos se calculan desde la técnica sin precios previos.

<Ejemplo>

En el sistema del curso (`$R = 44{,}9\%$`, clase 03): con `$w = 0$`, `$r = 44{,}9\%$`; con `$r = 0$`, `$w = \hat{W}$` (todo el neto a salarios). Un punto intermedio negociado, p. ej. `$w = \hat{W}/2$`, deja `$r \approx 22{,}45\%$` si la frontera fuera recta (en patrón lo es exactamente, clase 21; en trigo se curva por composición).

</Ejemplo>

### Paso 2: La inversa general

Entre extremos, subir `$w$` exige bajar `$r$`: la tesis de Ricardo demostrada en general. Pero ojo: ante cambios de `$w$`, los precios **también** se mueven (efecto composición, clase 16), así que la frontera puede curvarse; solo con la mercancía patrón (clase 21) es recta.

### Paso 3: Leer el conflicto

Cada punto es una correlación de fuerzas sociales. No hay punto "técnicamente correcto": la técnica da la frontera, la sociedad elige dónde estar. Los efectos complejos (un bien que se encarece y luego se abarata al subir `$w$`) se explican por el mecanismo precio-composición, ya esbozado por Ricardo.

<figure class="eco-figure">
  <img src="/assets/figures/clasica/frontera-w-r-light.svg" alt="Frontera decreciente entre salario w y tasa de beneficio r, desde R en el eje vertical hasta el salario máximo en el horizontal." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/frontera-w-r-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la frontera w-r es el conflicto distributivo dibujado; la técnica la traza, la sociedad elige el punto.</figcaption>
</figure>

<figure class="eco-figure">
  <img src="/assets/figures/clasica/frontera-alternativa-light.svg" alt="Frontera salario-beneficio recta en mercancía patrón frente a la curva arqueada en numerario trigo." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/frontera-alternativa-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: en patrón la frontera es recta; en trigo se comba por los efectos precio.</figcaption>
</figure>

## Interpretación económica

1. **Conflicto sin moralina**: no es que unos sean buenos y otros malos; es que el excedente es uno solo y dos clases lo reclaman.
2. **Política dentro del modelo**: fijar salario mínimo o tasa de interés es elegir punto; el modelo traduce la elección a precios.
3. **Límite del análisis**: la frontera supone técnica dada; el cambio técnico la desplaza (tema fuera del curso).

<IdeaClave>
`$R$` y `$\hat{W}$` se calculan; el punto interior se negocia. Quien te prometa el punto "óptimo técnico" te está vendiendo su punto social.
</IdeaClave>
