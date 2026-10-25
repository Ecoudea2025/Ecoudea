---
title: "Clase 12: Trabajo homogéneo y salario"
course: "economia-clasica"
order: 12
classType: "clase"
description: "Definición económica del trabajo, homogenización por salarios y el salario natural de Smith y Ricardo."
math: true
---

## Puente: el insumo que no es mercancía

Los sistemas `$(\mathbf{A}\mathbf{p}+\mathbf{l}w)(1+r) = \mathbf{p}$` usan `$\mathbf{l}$` homogéneo y `$w$` dado. Pero los trabajos reales son heterogéneos (agrícola vs metalúrgico) y el salario parece un precio más. Esta clase justifica ambos supuestos: cómo se homogeniza y por qué el salario **no** es un precio.

## Variables

* **Trabajo (clásico)**: actividad productora de bienes **remunerada con salario**. Lo no asalariado (doméstico, cuenta propia) queda fuera del campo.
* `$n_i$`: trabajadores concretos del tipo `$i$`. `$w_i$`: su salario. `$L_i$`: trabajo homogéneo del sector `$i$`.
* `$w$`: salario natural = valor de la canasta de subsistencia `$\mathbf{s}$`.

<Definicion>
**Trabajo**: esfuerzo contratado por salario; trabajar y recibir salario son equivalentes. **Salario natural**: ingreso que asegura subsistencia normal y reproducción del obrero y su familia.
</Definicion>

## Homogenización por salarios

### Paso 1: Condiciones

a) todo trabajo reconocido es asalariado; b) calidades distintas cobran distinto; c) la estructura salarial se conoce **antes** de los precios; d) es estable entre generaciones. Entonces la escala salarial vive **fuera** del núcleo precio-distribución.

### Paso 2: Reducción a un trabajo particular

Con `$W_i = n_i w_i$` y proporciones `$w_i/w_j$` conocidas, todo se convierte a unidades del sector `$j$`. Ejemplo: `$n_1 = 50{.}000$`, `$n_2 = 10{.}000$`, `$w_2/w_1 = 2$` → `$25{.}000 + 10{.}000 = 35{.}000$` metalúrgicos equivalentes.

<details>
<summary>¿Por qué la homogenización esconde un problema?</summary>

Reducir por salarios supone que las diferencias salariales reflejan diferencias de calificación estables y conocidas **antes** de los precios. Pero si los salarios relativos cambian con la distribución, la "unidad de trabajo" cambia con lo que se quiere medir: circularidad parecida a la del capital (clase 16). El clásico la acepta como aproximación práctica, no como solución teórica cerrada.
</details>

### Paso 3: Reducción a trabajo general

Más limpio: definir `$L$` (jornada social) con `$W = Lw$` y repartir por masa salarial:

$$
\begin{align*}L_i = \frac{W_i}{W}L\end{align*}
$$

`$L_i$` = fracción de la jornada (o de la masa salarial) empleada en `$i$`. Con `$L = 140{.}000$`: `$L_1 = 100{.}000$`, `$L_2 = 40{.}000$` —el caso del ejemplo 2 del capítulo 2. Los `$l_i$` del sistema son estos `$L_i$` por unidad.

<Ejemplo>

Verifica la consistencia: con `$n_1 = 50{.}000$`, `$n_2 = 10{.}000$`, `$w_2 = 2w_1$, la masa salarial es `$W = 50{.}000\,w_1 + 10{.}000 \times 2w_1 = 70{.}000\,w_1$`. Participaciones: `$W_1/W = 50/70$`, `$W_2/W = 20/70$`. Luego `$L_1 = \frac{5}{7} \times 140{.}000 = 100{.}000$` y `$L_2 = \frac{2}{7} \times 140{.}000 = 40{.}000$`. Exacto: las dos vías (equivalentes metalúrgicos y jornada social) coinciden porque ambas ponderan por salarios.

</Ejemplo>

## El salario natural (Smith-Ricardo)

Smith: mínimo de subsistencia; sube sobre él en estado **progresivo** (capital crece más que población) y vuelve en el estacionario. Ricardo: `$w_n$` lo fija la canasta `$\mathbf{s}$` (alimentos + necesarios + comodidades, con hábitos de cada país y época); el ingreso **sigue** a la canasta, no al revés; el "precio del trabajo" es en verdad el precio de la canasta `$\mathbf{s}\mathbf{p}$`; el trabajo no es mercancía con valor propio sino **derecho** a la subsistencia.

## Interpretación económica

1. **El salario es distributivo, no técnico**: lo fijan fisiología + costumbres + instituciones, fuera del mercado de "oferta y demanda de trabajo".
2. **Anticipado**: se adelanta al inicio del período; por eso entra en el capital (forma ricardiana).
3. **Puente a valor-trabajo**: con `$\mathbf{l}$` homogéneo ya tiene sentido preguntar si los precios los regulan las cantidades de trabajo (unidad 4).

<IdeaClave>
Trabajo homogéneo = peso salarial relativo (`$L_i = W_i L / W$`). Salario = derecho a `$\mathbf{s}$`, no precio del esfuerzo. Con esto, `$\mathbf{l}$` y `$w$` quedan legitimados como datos.
</IdeaClave>
