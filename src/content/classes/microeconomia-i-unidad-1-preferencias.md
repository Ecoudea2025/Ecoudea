---
title: "Preferencias y utilidad"
course: "microeconomia-i"
order: 1
classType: "clase"
description: "Axiomas de preferencia, función de utilidad y curvas de indiferencia"
math: true
conceptos: ["Utilidad", "Curvas de indiferencia", "Relación de preferencias"]
---

<!-- Guía de autoría: docs/AUTORIA.md. Bloques: :::tipo Título … ::: (ver clase
     de tortura en draft). Ecuaciones referenciables: \tag{id} + $\ref{id}$. -->

## Preferencias racionales

:::definicion Relación de preferencias
Una <Term id="relacion-de-preferencias">relación de preferencias</Term> $\succeq$ sobre el conjunto de canastas $X$ es **racional** si es
completa (siempre puedes comparar) y transitiva (coherente al encadenar).
:::

:::ejemplo Comparar canastas
Con $x = (2, 3)$ e $y = (3, 2)$, un consumidor racional elige $x \succeq y$ o
$y \succeq x$: no vale "no sé".
:::

## Función de utilidad

:::teorema Representación
Si $\succeq$ es racional y continua, existe $u: X \to \R$ tal que
$x \succeq y \iff u(x) \geq u(y)$.
:::

La condición que usaremos en todo el curso es la representación de la utilidad:

$$
x \succeq y \iff u(x) \geq u(y) \tag{utilidad}
$$

A partir de $\ref{utilidad}$, las <Term id="curvas-de-indiferencia">curvas de indiferencia</Term> son los conjuntos de
nivel $\{x \in X \mid u(x) = k\}$: moverse sobre ellas no cambia tu bienestar.

:::ideaclave
La <Term id="utilidad">utilidad</Term> no se mide en nada real: solo importa el orden que induce.
:::
