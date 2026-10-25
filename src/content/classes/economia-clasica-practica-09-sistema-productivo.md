---
title: "Práctica 02: sistema productivo"
course: "economia-clasica"
order: 9
classType: "practica"
description: "Ejercicios numéricos con el sistema trigo-hierro: coeficientes, excedente, Leontief y crecimiento."
math: true
---

## Lista de ejercicios

1.  Con los métodos del ejemplo 2 (clase 06) y `$\mathbf{s} = [5{,}125\ \ 0]$`, calcula `$S_1$`, `$S_2$` y verifica `$\mathbf{E} = [\text{2.050.000 trigo},\ \text{1.500.000 hierro}]$`. Muestra cada resta.
2.  Calcula `$a_{11}, a_{12}, a_{21}, a_{22}$` y `$l_1, l_2$` dividiendo entre `$y_1 = \text{10.250.000}$`, `$y_2 = \text{3.000.000}$`. Compara con los valores de la clase 07 (`$0{,}35$; `$0{,}1463$`; `$1{,}2983$`; `$0$`; `$0{,}0097$`; `$0{,}013$`).
3.  Obtén `$b_{11}, b_{12}, b_{21}, b_{22}$` y verifica `$\mathbf{B} - \mathbf{A} = \mathbf{l}\mathbf{s}$` celda por celda.
4.  Con `$\mathbf{E} = [175\ \ 0]$` del ejemplo 6 (cantidades 280/12 → 575 y 120/8 → 20), plantea `$\mathbf{y} = \mathbf{E}[\mathbf{I}-\mathbf{B}]^{-1}$` y discute: ¿qué estructura `$y$` sostiene ese excedente? ¿Es única? (apunta a la nota 20 del libro: homotecia + ecuación de trabajo).
5.  Calcula las tasas físicas `$e_{\text{trigo}}$`, `$e_{\text{hierro}}$` del sistema del ejemplo 2 y determina a qué tasa puede crecer sin reestructurarse. Explica qué habría que cambiar para igualarlas y crecer al máximo.
6.  Clasifica: ¿el hierro del ejemplo 2 es básico? ¿y un bien de lujo que no entra en ningún método? Justifica con la definición 9 (qué se paraliza si falta).

## Pistas (inténtalo primero sin mirar)

1. Subsistencia por sector: `$S_1 = 5{,}125 \times 100{.}000$`, `$S_2 = 5{,}125 \times 40{.}000$`. Resta cada insumo total de su producto y compara con `$\mathbf{E}$`.
2. Es el cálculo inverso del Ejemplo de la clase 06: fila ÷ producto. Si un decimal no cuadra, revisa ceros (son miles y millones).
3. Ya hiciste `$b_{11}$` en la clase 07; repite el patrón `$b_{ij} = a_{ij} + l_i s_j$` en las otras tres (ojo: `$s_2 = 0$` anula dos términos).
4. Usa la inversa de la clase 07: `$\mathbf{y} = [175\ \ 0][\mathbf{I}-\mathbf{B}]^{-1}$` da una **única** `$\mathbf{y}$` (calcula las dos componentes). Unicidad ≠ arbitrariedad: la homotecia fija proporciones.
5. Es el Ejemplo de la clase 08 con otros números: calcula `$e$` por bien y el mínimo manda. Para igualarlas habría que reasignar trabajo entre sectores.
6. Mira `$a_{12} = 0{,}1463$` (¿el trigo necesita hierro?) y `$a_{22} = 0$` (¿el hierro se necesita a sí mismo?). El lujo no entra en ningún `$a_{ij}$`.

<IdeaClave>
Si estos 6 ejercicios salen fluidos, las unidades 3–5 serán lectura, no lucha: ya hablas el idioma `$\mathbf{A}/\mathbf{B}/\mathbf{E}$`.
</IdeaClave>
