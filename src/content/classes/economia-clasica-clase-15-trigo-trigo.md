---
title: "Clase 15: Ricardo y el modelo trigo-trigo"
course: "economia-clasica"
order: 15
classType: "clase"
description: "El modelo de un solo bien: la tasa de beneficio como cociente físico y su independencia de los precios."
math: true
conceptos: ["Modelo trigo-trigo", "Distribución del producto", "Tasa de beneficio"]
---

## Puente: el atajo de un bien

Ricardo quiere lo que Smith no logró: determinar `$r$` **sin** conocer precios. Su truco genial: un mundo donde el trigo se produce solo con trigo (más trabajo pagado en trigo). Entonces capital y producto hablan el mismo idioma y la tasa sale por división.

## Variables

* `$K$`: capital en trigo (semilla + subsistencias). `$Y$`: cosecha en trigo.
* `$r = (Y-K)/K$`: tasa física de excedente.

<Definicion>
**Modelo trigo-trigo**: sistema de un bien donde insumo y producto son la misma mercancía; la distribución se lee en cantidades físicas.
</Definicion>

## Deducción paso a paso

### Paso 1: Plantear el cociente

$$
\begin{align*}r = \frac{\text{trigo cosechado} - \text{trigo adelantado}}{\text{trigo adelantado}}\end{align*}
$$

Sin precios por ningún lado: `$r$` es una **tasa de rendimiento físico**, dictada por la técnica.

<Ejemplo>

Cosecha `$1{.}000$` t con adelanto `$800$` t (semilla `$500$` + subsistencias `$300$`): `$r = (1{.}000 - 800)/800 = 25\%$`. Si la técnica mejora y el adelanto cae a `$700$`, `$r = 300/700 \approx 42{,}9\%$`: la tasa se lee directa de las cantidades, sin mercado.

</Ejemplo>

<figure class="eco-figure">
  <img src="/assets/figures/clasica/trigo-trigo-numerico-light.svg" alt="Rayo cosecha-adelanto con pendiente 1 + r: 25 por ciento con adelanto 800 y 42,9 por ciento con 700 para cosecha 1000." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/trigo-trigo-numerico-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la pendiente del rayo es 1 + r: la tasa se lee sin precios.</figcaption>
</figure>

### Paso 2: Repartir sin valorar

Con `$r$` conocida, el excedente físico se reparte (beneficios aquí; salario ya adelantado como subsistencia). Los precios relativos ni aparecen: con un solo bien no hay proporciones que fijar.

### Paso 3: Marcar el límite

El truco muere con 2 bienes heterogéneos: ¿en qué unidades divides excedente entre capital si uno es trigo y otro hierro? Hace falta valorar, y valorar exige precios, y los precios exigen `$r$`. **Circularidad**: el capítulo entero de Ricardo es el intento de romperla (valor-trabajo, clase 16; dificultad de producción, clase 17).

## Interpretación económica

1. **`$r$` como variable de producción**: en este modelo el beneficio no reparte nada social; es rendimiento técnico.
2. **El salario como costo**: los obreros no participan del excedente; `$w$` es insumo como la semilla (oscurece el antagonismo salarios-beneficios, lo veremos en la clase 17).
3. **Programa ricardiano**: generalizar el trigo-trigo a `$n$` bienes sin perder la determinación física de `$r$`.

<IdeaClave>
Trigo-trigo = existencia demostrada de una `$r$` sin precios. Todo Ricardo posterior es la pregunta: ¿y con muchos bienes?
</IdeaClave>
