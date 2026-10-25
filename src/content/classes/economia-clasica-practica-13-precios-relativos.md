---
title: "Práctica 03: precios relativos"
course: "economia-clasica"
order: 13
classType: "practica"
description: "Ejercicios con numerario, sistema Sraffa 2×2, tasas diferenciales y homogenización del trabajo."
math: true
---

## Lista de ejercicios

1.  Con `$p_h/p_g = 10$` y `$p_h = 120$`: halla `$p_g$`; luego propone otros dos pares absolutos compatibles y verifica el relativo. ¿Qué cambia y qué no cuando todos los absolutos se duplican?
2.  En el sistema del ejemplo 6 verifica las tasas del caso `$p_{21} = 10$` (`$r_1 = 43{,}75\%$`, `$r_2 = 0\%$`): calcula capitales (`$280+12(10)$`, `$120+8(10)$`), ingresos y ganancias. Repite para `$p_{21} = 24{,}58$`.
3.  Imponiendo `$r_1 = r_2 = r$` resuelve el sistema 2×2 y confirma `$p_{21} = 15$`, `$r = 25\%$`. Valora capitales, ingresos y ganancias a ese precio y comprueba la proporcionalidad al capital.
4.  Explica por qué `$(\mathbf{I}+\hat{\mathbf{r}})\mathbf{B}\mathbf{p} = \mathbf{p}$` está subdeterminado (cuenta ecuaciones vs incógnitas para `$n = 2$`) y qué ecuaciones lo cerrarían (adelanto de la unidad 6: oferta-demanda).
5.  Con `$n_1 = 50{.}000$`, `$n_2 = 10{.}000$`, `$w_2/w_1 = 2$`: reduce a trabajo metalúrgico y a trabajo general con `$L = 140{.}000$`. Interpreta `$L_1/L$` de las dos maneras (jornada y masa salarial).
6.  Discute en 5 líneas: si el salario lo fijan costumbres e instituciones, ¿por qué el modelo lo trata como dato y no como incógnita de mercado? Conecta con la forma `$(Ap+lw)(1+r) = p$`.

## Pistas (inténtalo primero sin mirar)

1. De `$p_h = 120$` y `$p_h/p_g = 10$` despeja `$p_g$`; para los otros pares elige absolutos que mantengan el cociente (p. ej. multiplica ambos por 2). Lo que cambia: la escala monetaria; lo que no: ninguna proporción ni decisión real.
2. Usa el <details> de la clase 11 para el caso `$p_{21} = 10$`; para `$24{,}58$` repite el mismo esquema (cuidado: ahora `$m_1 \approx 0$` y el hierro se lleva todo).
3. Imponer `$r_1 = r_2$` convierte dos ecuaciones sueltas en un sistema: despeja `$p_{21}$` de una e insértalo en la otra; verifica que a `$15$` cada `$m_i/K_i = 0{,}25$`.
4. Cuenta: con `$n = 2$`, ¿cuántas ecuaciones y cuántas incógnitas (`$p_{21}$`, `$r_1$`, `$r_2$`)? Si sobran incógnitas, el sistema no cierra solo: falta la regla de cierre (oferta-demanda en la unidad 6).
5. Ya lo hiciste en la clase 12: primero a metalúrgicos (pondera por `$w_i/w_2$`), luego a jornada social con `$L_i = W_i L / W$`. Interpreta: `$L_1/L$` es a la vez fracción del tiempo y fracción de la masa salarial.
6. Piensa en quién decide: si el salario fuera precio de mercado, la oferta y la demanda de trabajo lo fijarían; como lo fijan costumbres, entra como parámetro (como `$\mathbf{A}$`) y la forma `$(Ap+lw)(1+r) = p$` lo toma dado.

<IdeaClave>
El trío `$10/15/24{,}58$` y la fórmula `$L_i = W_iL/W$` deben salirte sin mirar. Son los dos músculos de esta unidad.
</IdeaClave>
