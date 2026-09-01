---
title: "Clase 20"
course: "estadistica-i"
order: 25
classType: "clase"
description: "Momentos. Función generadora de momentos."
bibliography: "../../referencias.bib"
---

Momentos
--------

Se define al `$r$`-ésimo **momento alrededor del origen** de una
variable aleatoria `$X$` de la forma

$$\begin{align*}\mu^´_r = \mathbb{E}(X^r) =\begin{cases} \sum_{x}x^rp(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty x^rf(x) \text{ d}x & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


mientras que, el `$r$`-ésimo **momento central** de la variable
aleatoria `$X$` es de la forma

$$\begin{align*}\mu_r = \mathbb{E}([X-\mu]^r) =\begin{cases} \sum_{x}(x-\mu)^rp(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty (x-\mu)^rf(x) \text{ d}x & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$

En este caso, se tendrá que en el caso particular cuando `$r = 1$`, se
dirá que **el primer momento central es igual al primero momento
alrededor del origen**.

Es decir, que

$$\begin{align*}\mu_1 &= \mu^´_1 \\ \mathbb{E}([X-\mu]) &= \mathbb{E}(X)\end{align*}$$


Función generadora de momentos
------------------------------

La función generadora de momentos de la variable aleatoria `$X$` es el
valor esperado de `$e^{xt}$`, se denota por `$M_x(t)$` y está dado por

$$\begin{align*}M_x(t) = \mathbb{E}(e^{xt}) =\begin{cases} \sum_{x}e^{xt}p(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty e^{xt}f(x) \text{ d}x & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


### Teorema: Cálculo de momentos a partir de la función generadora de momentos

Si `$X$` es una variable aleatoria con función generadora de momentos
`$M_x(t)$`, entonces

$$\begin{align*}\frac{\text{d}^rM_x(t)}{\text{d}t^r}\Bigg|_{t=0}=\mathbb{E}(X^r)\end{align*}$$


### Teorema de unicidad

Sean `$X$` y `$Y$` dos variables aleatorias con funciones generadoras de
momentos `$M_x(t)$` y `$M_y(t)$`, entonces si para todos los valores de
`$t$` se encuentra que `$M_x(t) = M_y(t)$` se tendrá por tanto que `$X$`
y `$Y$` tendrán la misma distribución de probabilidad.

### Teorema: Convolución de variables aleatorias

Si `$X_1. X_2, \ldots, X_n$` son variables aleatorias independientes con
función generadora de momentos
`$M_{x_1}(t), M_{x_2}(t), \ldots, M_{x_n}(t)$`, respectivamente, y sea
`$Y$` la convolución de las variables aleatorias
`$X_1. X_2, \ldots, X_n$`, tal que, `$Y = X_1 + X_2 + \ldots + X_n$`,
entonces se tendrá que la función generadora de momentos de `$Y$` estará
dada por

$$\begin{align*}M_{y}(t) = M_{x_1}(t) M_{x_2}(t) \ldots M_{x_n}(t)\end{align*}$$


### Propiedades de función la función generadora de momentos

Si `$X$` es una variable aleatoria y `$a$` una constante entonces se
tendrá

1.  `$M_{x+a}(t) = e^{at}M_x(t)$`

2.  `$M_{ax}(t) = M_x(at)$`