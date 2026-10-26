---
title: "Clase 07: Matrices A, B y Leontief"
course: "economia-clasica"
order: 7
classType: "clase"
description: "Coeficientes aij, bij, matriz sociotécnica B = A + ls, excedente E = y[I − B] e inversa de Leontief."
math: true
---

## Puente: del ejemplo a la forma general

La clase 06 calculó el excedente a mano. Ahora comprimimos cualquier sistema de `$n$` bienes en tres objetos (`$\mathbf{A}$`, `$\mathbf{l}$`, `$\mathbf{B}$`) y una fórmula (`$\mathbf{E} = \mathbf{y}[\mathbf{I} - \mathbf{B}]$`). Es el lenguaje en que se escribirán todos los sistemas de precios.

## Variables

* `$a_{ij} = y_{ij}/y_i$`: insumo `$j$` por unidad de `$i$`. `$\mathbf{A}$`: matriz técnica.
* `$l_i = L_i/y_i$`: trabajo por unidad de `$i$`. `$\mathbf{l}$`: vector columna.
* `$b_{ij} = y^+_{ij}/y_i$`: insumo **más** subsistencia por unidad. `$\mathbf{B}$`: matriz sociotécnica.

<Definicion>
`$\mathbf{B} - \mathbf{A} = \mathbf{l}\mathbf{s}$`: la diferencia entre lo sociotécnico y lo técnico es exactamente la subsistencia por unidad (`$l_i s_j$`).
</Definicion>

## Deducción paso a paso

### Paso 1: Normalizar por unidad

Dividir cada fila del sistema entre su producto `$y_i$` convierte cantidades absolutas en coeficientes. Para el trigo-hierro: `$a_{11} = 0{,}35$`, `$a_{12} = 0{,}1463$`, `$a_{21} = 1{,}2983$`, `$a_{22} = 0$`; `$l_1 = 0{,}0097$`, `$l_2 = 0{,}013$`.

### Paso 2: Forma matricial del excedente

$$
\begin{align*}\mathbf{E} = \mathbf{y}[\mathbf{I} - \mathbf{B}]\end{align*}
$$

con `$\mathbf{y} = [y_1\ y_2\ \cdots\ y_n]$`. Si `$\mathbf{E} = 0$`, el sistema homogéneo solo tiene solución económica si `$\det[\mathbf{I}-\mathbf{B}] = 0$` (estructura única por homotecia). Si `$\mathbf{E} > 0$` en algún bien:

$$
\begin{align*}\mathbf{y} = \mathbf{E}[\mathbf{I} - \mathbf{B}]^{-1}\end{align*}
$$

cada excedente define una estructura productiva distinta.

### Paso 3: Leer la inversa de Leontief

La fila `$i$` de `$[\mathbf{I}-\mathbf{B}]^{-1}$` dice los requerimientos **directos e indirectos** para disponer de una unidad de `$i$` en el excedente. Sentido económico exige inversa no negativa (Perron-Frobenius: valor propio dominante de `$\mathbf{B}$` menor que `$1$`).

<Ejemplo>

Para el trigo-hierro, `$\mathbf{I}-\mathbf{B} = \begin{pmatrix}0{,}6 & -0{,}1463 \\ -1{,}3666 & 1\end{pmatrix}$` con determinante `$0{,}6 \times 1 - 0{,}1463 \times 1{,}3666 = 0{,}6 - 0{,}2 = 0{,}4$`. La inversa es:

$$
\begin{align*}[\mathbf{I}-\mathbf{B}]^{-1} = \frac{1}{0{,}4}\begin{pmatrix}1 & 0{,}1463 \\ 1{,}3666 & 0{,}6\end{pmatrix} = \begin{pmatrix}2{,}5 & 0{,}3658 \\ 3{,}4165 & 1{,}5\end{pmatrix}\end{align*}
$$

Lee la primera fila: para dejar **1 tonelada de trigo en el excedente** hay que producir en bruto `$2{,}5$` t de trigo y `$0{,}3658$` t de hierro (directos + indirectos). La segunda fila: 1 t de hierro neta exige `$3{,}4165$` t de trigo y `$1{,}5$` t de hierro brutos. Toda entrada es `$\geq 0$`: el sistema tiene sentido económico.

</Ejemplo>

<figure class="eco-figure">
  <img src="/assets/figures/clasica/tablas-io-light.svg" alt="Matrices A y B del sistema trigo-hierro y la inversa de Leontief con los requerimientos directos e indirectos." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/tablas-io-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: A registra la técnica, B suma las subsistencias y la inversa dice cuánto producir en bruto por cada unidad neta.</figcaption>
</figure>

## Básicos vs no básicos

<Definicion>
**Bien básico**: interviene directa o indirectamente en la producción de **todos** los bienes. Sin él, el sistema se paraliza. Los bienes de lujo son no básicos por excelencia.
</Definicion>

Solo un excedente compuesto de básicos (en cantidades suficientes) puede acumularse íntegramente; con no básicos, parte solo puede consumirse.

## Interpretación económica

1. **La técnica determina el espacio de lo posible**: dados `$\mathbf{B}$`, no toda estructura `$y$` es viable.
2. **Distribución como dato de la composición**: quién se apropia `$\mathbf{E}$` decide su composición física (inversión en básicos vs consumo en lujos).
3. **Puente a precios**: `$\mathbf{B}$` será el determinante fundamental de los precios naturales (clase 11).

<Ejercicio>
Con los `$b_{ij}$` del trigo-hierro (`$b_{11}=0{,}4$, `$b_{12}=0{,}1463$, `$b_{21}=1{,}3666$, `$b_{22}=0$`), verifica `$\mathbf{B}-\mathbf{A} = \mathbf{l}\mathbf{s}$` celda por celda antes de la práctica 09.
</Ejercicio>
