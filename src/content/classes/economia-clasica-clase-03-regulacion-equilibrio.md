---
title: "Clase 03: Regulación por los mercados y equilibrio"
course: "economia-clasica"
order: 3
classType: "clase"
description: "El problema de la coordinación, el sistema de precios como mecanismo y las nociones de equilibrio y estabilidad."
math: true
---

## Puente: del rasgo al problema

La clase anterior dejó cuatro rasgos. Ahora convertimos el segundo —descentralización— en **problema científico**: si nadie coordina, ¿por qué no hay caos permanente? La respuesta clásica y neoclásica coincide en el mecanismo (el sistema de precios) y difiere en casi todo lo demás.

## Variables del problema

* **Coordinación**: compatibilidad ex post de decisiones tomadas ex ante sin consultarse.
* **Equilibrio**: situación donde ninguna fuerza interna modifica precios ni cantidades; se autorreproduce.
* **Estabilidad**: propiedad por la cual el desequilibrio tiende al equilibrio por fuerzas internas.

<Definicion>
**Tesis de la autorregulación**: en una sociedad comercial de individuos egoístas funciona un sistema de precios, independiente de la voluntad de cada uno, que hace compatibles sus acciones.
</Definicion>

## La demostración en dos fases

### Paso 1: Existencia del equilibrio (teoría de la referencia)

Se construye un sistema de precios que, **si rigiera**, armonizaría todas las relaciones: reproduce insumos, distribuye el excedente, nadie quiere cambiar de plan. Es un mundo ideal posible. En clásico: tasa de beneficio uniforme `$r_1 = r_2 = \cdots = r_n = r$`; en neoclásico: oferta igual a demanda en todos los mercados con pleno empleo.

<Ejemplo>

Para el sistema trigo-hierro del curso (clases 06–07, con `$\mathbf{B} = \begin{pmatrix}0{,}4 & 0{,}1463 \\ 1{,}3666 & 0\end{pmatrix}$`), la tasa máxima de excedente sale del valor propio dominante `$\lambda_{\max}$` de `$\mathbf{B}$`:

$$
\begin{align*}\lambda_{\max} = \frac{0{,}4 + \sqrt{0{,}4^2 + 4 \times 0{,}1463 \times 1{,}3666}}{2} = \frac{0{,}4 + 0{,}98}{2} = 0{,}69\end{align*}
$$

$$
\begin{align*}R = \frac{1}{\lambda_{\max}} - 1 = \frac{1}{0{,}69} - 1 \approx 0{,}449\end{align*}
$$

Es decir: aun reinvirtiendo **todo** el excedente en las proporciones justas, el sistema no puede crecer más del **44,9%** por período. Ese número —puramente técnico— será el techo de toda la dinámica del curso (clases 08, 20–21).

</Ejemplo>

### Paso 2: Estabilidad (teoría del ajuste)

Se demuestra que ese mundo ideal es **probable**: desde cualquier desequilibrio, las fuerzas del mercado conducen a él. Sin esta fase, el equilibrio sería una curiosidad matemática. Smith la llamó **gravitación**; los modernos, estabilidad del equilibrio.

<Advertencia>
Explicar solo el equilibrio sin el ajuste —o el mercado sin la referencia— deja la teoría coja. El curso dedica las unidades 4–5 a la referencia y la unidad 6 al ajuste.
</Advertencia>

## Los cuatro interrogantes del equilibrio

1. **¿Existen los precios de equilibrio?** ¿Pueden calcularse? ¿Uno solo por mercancía?
2. **¿Cómo se transa a esos precios?** ¿Qué regla de reparto del excedente implican?
3. **¿Cómo se forma el sistema en el mercado?** ¿Qué proceso lleva de los precios corrientes a los de referencia?
4. **¿Es estable?** ¿Se alcanza siempre? ¿Se vuelve a él tras una perturbación?

| Interrogante | Dónde se responde |
| :--- | :--- |
| Existencia y cálculo | Clases 10–12 (sistema de precios), 15–17 (valor), 20–21 (Sraffa) |
| Transacción y reparto | Clases 11–12 (ganancia uniforme), 17 (salario) |
| Formación (mercado → referencia) | Clases 23–24 (gravitación, Torrens-BBK) |
| Estabilidad | Clases 23–25 (método y dinámica) |

## Interpretación económica

1. **Precio como sanción social**: el precio valida o castiga decisiones pasadas (beneficios altos/bajos), no solo informa.
2. **Anonimato del mecanismo**: nadie fija el resultado; por eso la economía se estudia separada de la política.
3. **Equilibrio ≠ pleno empleo (en clásico)**: la condición clásica es uniformidad de `$r$`, no ocupación total del trabajo.

<IdeaClave>
Toda teoría general ortodoxa = teoría del equilibrio + teoría de la estabilidad. Si una de las dos falla, la tesis de la autorregulación queda sin demostrar.
</IdeaClave>
