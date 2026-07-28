---
title: "Clase 03"
course: "probabilidad-inferencia"
order: 4
classType: "clase"
description: "Probabilidad total. Teorema de Bayes."
math: true
bibliography: "../../referencias.bib"
---

## Probabilidad total

Sean `$A_1, A_2, \ldots, A_k$` eventos **mutuamente excluyentes**
`$(A_i\cap A_j = \oslash, \text{ para } i\neq j)$` y **exhaustivos**
`$\left(\underset{i=1}{\stackrel{k}{\cup}} A_i = S\right)$`, entonces
para cualquier otro evento `$B$`

$$\begin{align*}\mathbb{P}(B) &= \mathbb P(B\cap A_1)+\mathbb P(B\cap A_2)+\ldots+\mathbb P(B\cap A_k)\end{align*}$$

o alternativamente, al aplicar la formula de la
<a href="../../ProbabilidadeInferencia/PeIEClase02.html#regla-multiplicativa" target="\_blank">Regla
multiplicativa</a>, tenemos que

$$\begin{align*}\mathbb{P}(B) &= \mathbb P(A_1)\mathbb P(B|A_1)+\mathbb P(A_2)\mathbb P(B|A_2)+\ldots+\mathbb P(A_k)\mathbb P(B|A_k)\end{align*}$$


<button id="Show4" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>

Tres máquinas de cierta planta de ensamble \(A_1, A_2, A_3\) montan
\(30\%, 45\%, 25\%\) del total de los productos producidos por la
empresa, respectivamente. Se sabe por experiencia que \(4\%, 5\%, 2\%\)
de los productos ensamblados por cada maquina tienen defectos,
respectivamente. <br><br>

Si selecciona de forma aleatoria un producto terminado. Cuál es la
probabilidad de que éste se encuentra defectuoso? <br><br>

\(B\): El producto se encuentra defectuoso. <br> \(A_1\): el producto
fue producido por la máquina \(1\). <br> \(A_2\): el producto fue
producido por la máquina \(2\). <br> \(A_3\): el producto fue producido
por la máquina \(3\).
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Dado que el interés radica en encontrar la probabilidad de que se
seleccione un producto y resulte defectuoso, entonces nos están pidiendo
que se desea calcular la \(\mathbb{P}(B)\). <br><br>

Como entre la información dada en el enunciado no nos da la probabilidad
de que un artículo se encuentre defectuoso, entonces podemos tratar de
calcularla mediante el teorema de probabilidad total, aprovechando que
los eventos \(A_1, A_2, A_3\) son eventos <strong>mutuamente
excluyentes</strong> (Un artículo que es ensamblado por una máquina, no
puede ser ensamblado simultáneamente por otra),
<strong>exhaustivos</strong> (El total de los productos ensamblados por
la empresa, solo puede ser producido por alguna de estas tres máquinas)
y que nos están dando las probabilidades de los eventos \(B|A_1\),
\(B|A_2\) y \(B|A_3\). <br><br>

Partiendo de esto tenemos las siguientes probabilidades:<br>
$$\begin{align*}
\mathbb{P}(A_1) & = 0.30 \\
\mathbb{P}(A_2) & = 0.45 \\
\mathbb{P}(A_3) & = 0.25 \\
\mathbb{P}(B | A_1) & = 0.04 \\
\mathbb{P}(B | A_2) & = 0.05 \\
\mathbb{P}(B | A_3) & = 0.02 \\
\end{align*}$$

Entonces, al aplicar el teorema de probabilidad total, tendremos que<br>
$$\begin{align*}
\mathbb{P}(B) & = \mathbb{P}(A_1)\mathbb{P}(B | A_1) + \mathbb{P}(A_2)\mathbb{P}(B | A_2) + \mathbb{P}(A_3)\mathbb{P}(B | A_3) \\
 & = 0.30 \times 0.04 + 0.45 \times 0.05 + 0.25 \times 0.02\\
 & = 0.0395
\end{align*}$$

Obteniendo por tanto, que la probabilidad de que un artículo producido
en la empresa sea defectuoso es del \(3.95\%\)
</p>
</main>

## Teorema de Bayes

Sea `$A_1, A_2, \ldots, A_k$` eventos **mutuamente excluyentes** y
**exhaustivos**, con probabilidades previas `$\mathbb P(A_i)$`, para
`$i=1,2,\ldots,k$`, entonces para cualquier evento `$B$` para el cual
`$\mathbb P(B)>0$`, la probabilidad posterior `$A_j$` dado que `$B$` ha
ocurrido, está dada por

$$\begin{align*}\mathbb P(A_j|B) &= \frac{\mathbb P(A_j\cap B)}{\mathbb P(B)}\end{align*}$$

En donde, al aplicar la formula de la
<a href="../../ProbabilidadeInferencia/PeIEClase02.html#regla-multiplicativa" target="\_blank">Regla
multiplicativa</a> en el numerador, y la formula de la
<a href="../../ProbabilidadeInferencia/PeIEClase02.html#probabilidad-total" target="\_blank">Probabilidad
total</a> en el denominador, tenemos que


$$\begin{align*}\mathbb P(A_j|B) &= \frac{\mathbb P(A_j)\mathbb P(B|A_j)}{\sum_{i=1}^k \mathbb P(A_i)\mathbb P(B|A_i)}\end{align*}$$


<button id="Show5" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide5" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito5">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>

Tres máquinas de cierta planta de ensamble \(A_1, A_2, A_3\) montan
\(30\%, 45\%, 25\%\) del total de los productos producidos por la
empresa, respectivamente. Se sabe por experiencia que \(4\%, 5\%, 2\%\)
de los productos ensamblados por cada maquina tienen defectos,
respectivamente. <br><br>

Si selecciona de forma aleatoria un producto terminado y se encuentra
que es defectuoso, Cuál es la probabilidad de que éste artículo haya
sido ensamblado por la máquina \(3\)? <br><br>

\(B\): El producto se encuentra defectuoso. <br> \(A_1\): el producto
fue producido por la máquina \(1\). <br> \(A_2\): el producto fue
producido por la máquina \(2\). <br> \(A_3\): el producto fue producido
por la máquina \(3\).
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso, se tiene interés en saber la probabilidad de que un
artículo haya sido ensamblado por la máquina \(3\), \(A_3\),
<strong>dado que</strong> se sabe que el artículo seleccionado esta
defectuoso, \(B\), se tendrá que se desea calcular la
\(\mathbb{P}{(A_3|B)}\). <br><br>

De lo anterior apreciamos que nos están preguntando una probabilidad
condicional la cual se puede expresar de la forma $$\begin{align*}
\mathbb{P}{(A_3|B)} & = \frac{\mathbb{P}(A_3 \cap B)}{\mathbb{P}(B)}
\end{align*}$$

El problema, es que al observar las probabilidades necesarias para
realizar el cálculo de la formula anterior vemos que no poseemos ninguna
de las dos probabilidades que necesitamos para llevar a cabo el cálculo
de interés. <br> <br>

Al detallar la ecuación más detenidamente, observamos que los eventos
\(A_1, A_2, A_3\) son <strong>mutuamente excluyentes</strong> y
<strong>exhaustivos</strong>, lo cual nos permite poder calcular la
\(\mathbb{P}(B)\) mediante el teorema de
<a href="../../ProbabilidadeInferencia/PeIEClase02.html#probabilidad-total" target="\_blank">Probabilidad
total</a>, y la probabilidad \(\mathbb{P}(A_3 \cap B)\) mediante el
teorema de la
<a href="../../ProbabilidadeInferencia/PeIEClase02.html#regla-multiplicativa" target="\_blank">Regla
multiplicativa</a>. Lo cual nos lleva a la siguiente expresión.
$$\begin{align*}
\mathbb{P}{(A_3|B)} & = \frac{\mathbb{P}(A_3)\mathbb{P}(B|A_3)}{\mathbb{P}(A_1)\mathbb{P}(B|A_1)+\mathbb{P}(A_2)\mathbb{P}(B|A_2)+\mathbb{P}(A_3)\mathbb{P}(B|A_3)} \\
& = \frac{0.25\times 0.02}{0.30\times 0.04 + 0.45\times 0.05 + 0.25\times 0.02} \\
& = \frac{0.005}{0.0395} \\
& = 0.1265823
\end{align*}$$

Es decir, se tiene que la probabilidad de que un artículo que se sabe
está defectuoso, haya sido ensamblado por la máquina \(3\), es del
\(12.69\%.\)
</p>
</main>