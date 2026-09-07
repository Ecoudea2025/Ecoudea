---
title: "Sesión 04"
course: "semillero-r"
order: 6
classType: "clase"
description: "La familia apply - Función apply() - Función sapply() - Función lapply() - Función vapply() - Función mapply() - Función tapply()"
math: true
bibliography: "../../referencias.bib"
---

Funciones que se introducen en esta sesión
------------------------------------------

En ésta sesión se introducen las siguientes funciones

-   <tt>apply</tt>: se usa cuando se desea aplicar una función a las
    filas o columnas de una matriz (y análogos de dimensiones
    superiores).
-   <tt>lapply</tt>: se usa cuando se desea aplicar una función a cada
    elemento de una lista y retornar una lista.
-   <tt>sapply</tt>: se usa cuando se desea aplicar una función a cada
    elemento de una lista y retorna un vector, un arreglo, una lista,
    una matriz.
-   <tt>vapply</tt>: se usa cuando se desea usar una función
    <tt>sapply</tt>, pero mejorando un poco la velocidad y permitiendo
    establecer verificación para los valores retornados.
-   <tt>mapply</tt>: se usa cuando se tienen varias estructuras de datos
    (por ejemplo, vectores, listas) y se desea aplicar una función a los
    primeros elementos de cada uno, y luego a los segundos elementos de
    cada uno, y así sucesivamente.
-   <tt>tapply</tt>: se usa cuando se desea aplicar una función a
    subconjuntos de un vector y los subconjuntos están definidos por
    algún otro vector, generalmente un factor.

Qué es la familia apply?
------------------------

La familia <tt>apply</tt> es un conjunto de funciones de <tt>R</tt> que
**permiten manipular de forma repetitiva cada elemento de un vectores,
matrices, data frame, arrays y listas**. Estas funciones trabajan
similar a como lo hacen ciclo, pero con la ventaja de que suelen ser más
rápidas, requieren usualmente de menos código, y por ello, es preferible
usar las funciones pertenecientes a esta familia, en lugar de construir
ciclos.

**El objetivo de estas funciones es automatizar tareas completas,
mediante el empleo de poca líneas de código**, y pueden tomarse como una
de las características distintivas de <tt>R</tt> como lenguaje de
programación.

En si, la familia de funciones <tt>apply</tt> se compone por las
funciones <tt>apply()</tt>, <tt>lapply()</tt>, <tt>sapply()</tt>,
<tt>vapply()</tt>, <tt>mapply()</tt>, y <tt>tapply()</tt>, y todas
tienen la misma característica en común, y es que **cada una recibe como
argumentos a un objeto y al menos una función**

Función <tt>apply()</tt>
------------------------

La función <tt>apply()</tt> **aplica una función a todos los elementos
de una matriz o cualquier objeto que pueda coercionarse a una matriz**,
tal como un vector, una arreglo o un marco de datos, y retorna como
resultado de la aplicación de la función una matriz.

La estructura de esta función es la siguiente.

``` r
apply(X, MARGIN, FUN, ...)
```

-   <tt>X</tt>: Conjunto de observaciones que puede coercionarse a una
    matriz.
-   <tt>MARGIN</tt>: Forma en como se aplicará la función a los
    elementos de <tt>X</tt>. Donde el identificador 1 indica filas y el
    identificador 2 indica.
-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.

<button id="Show1" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide1" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito1">
<h3 data-toc-skip>
Función <tt>apply</tt>
</h3>
<p>
Construya una matríz de la forma $$\begin{align*}
M = \begin{bmatrix}5 & 12 & 14 \\13 & 6 & 3 \\8 & 9 & 12 \\15 & 12 & 11 \end{bmatrix}
\end{align*}$$
Y con ésta, encuentre el número máximo y número mínimo
por cada fila y por cada columna.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se crean la matríz</span><span class="w">
</span><span class="n">M</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="kc">matrix</span><span class="p">(</span><span class="n">data</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="m">5</span><span class="p">,</span><span class="w"> </span><span class="m">12</span><span class="p">,</span><span class="w"> </span><span class="m">14</span><span class="p">,</span><span class="w"> </span><span class="m">13</span><span class="p">,</span><span class="w"> </span><span class="m">6</span><span class="p">,</span><span class="w"> </span><span class="m">3</span><span class="p">,</span><span class="w"> </span><span class="m">8</span><span class="p">,</span><span class="w"> </span><span class="m">9</span><span class="p">,</span><span class="w"> </span><span class="m">12</span><span class="p">,</span><span class="w"> </span><span class="m">15</span><span class="p">,</span><span class="w"> </span><span class="m">12</span><span class="p">,</span><span class="w"> </span><span class="m">11</span><span class="p">),</span><span class="w"> </span><span class="n">nrow</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">4</span><span class="p">,</span><span class="w"> </span><span class="n">ncol</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">3</span><span class="p">,</span><span class="w"> 
    </span><span class="n">byrow</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">T</span><span class="p">)</span><span class="w">
</span><span class="n">M</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>     [,1] [,2] [,3]
[1,]    5   12   14
[2,]   13    6    3
[3,]    8    9   12
[4,]   15   12   11
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula mínimo por filas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">1</span><span class="p">,</span><span class="w"> </span><span class="n">min</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1]  5  3  8 11
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula máximo por filas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">1</span><span class="p">,</span><span class="w"> </span><span class="n">max</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 14 13 12 15
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula mínimo por columnas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">2</span><span class="p">,</span><span class="w"> </span><span class="n">min</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 5 6 3
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula máximo por columnas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">2</span><span class="p">,</span><span class="w"> </span><span class="n">max</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 15 12 14
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula mínimo y máximo por filas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">1</span><span class="p">,</span><span class="w"> </span><span class="k">function</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="nf">min</span><span class="p">(</span><span class="n">x</span><span class="p">),</span><span class="w"> </span><span class="nf">max</span><span class="p">(</span><span class="n">x</span><span class="p">)))</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>     [,1] [,2] [,3] [,4]
[1,]    5    3    8   11
[2,]   14   13   12   15
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula mínimo y máximo por columas</span><span class="w">
</span><span class="kc">apply</span><span class="p">(</span><span class="n">M</span><span class="p">,</span><span class="w"> </span><span class="m">2</span><span class="p">,</span><span class="w"> </span><span class="k">function</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="nf">min</span><span class="p">(</span><span class="n">x</span><span class="p">),</span><span class="w"> </span><span class="nf">max</span><span class="p">(</span><span class="n">x</span><span class="p">)))</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>     [,1] [,2] [,3]
[1,]    5    6    3
[2,]   15   12   14
</code></pre>
</section>
</section>
</main>

Función <tt>lapply()</tt>
-------------------------

La función <tt>lapply()</tt> **aplica una función a todos los elementos
de una lista o cualquier objeto que pueda coercionarse a una lista**, y
retornara como resultado de la aplicación de la función una lista.

La estructura de esta función es la siguiente.

``` r
lapply(X, FUN, ...)
```

-   <tt>X</tt>: Conjunto de observaciones que puede coercionarse a una
    lista.
-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.

<button id="Show2" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide2" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito2">
<h3 data-toc-skip>
Función <tt>lapply</tt>
</h3>
<p>
Emplee la base de datos <tt>trees</tt> de la base de <tt>R</tt>, y para
ésta, calcule el valor para los cuartiles de cada variable, y retorne
los valores calculados en forma de una lista.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se muestra la estructura de cada variale</span><span class="w">
</span><span class="kc">str</span><span class="p">(</span><span class="n">trees</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>'data.frame':   31 obs. of  3 variables:
 $ Girth : num  8.3 8.6 8.8 10.5 10.7 10.8 11 11 11.1 11.2 ...
 $ Height: num  70 65 63 72 81 83 66 75 80 75 ...
 $ Volume: num  10.3 10.3 10.2 16.4 18.8 19.7 15.6 18.2 22.6 19.9 ...
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calculan los cuartiles para cada variable</span><span class="w">
</span><span class="kc">lapply</span><span class="p">(</span><span class="n">trees</span><span class="p">,</span><span class="w"> </span><span class="n">quantile</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>$Girth
   0%   25%   50%   75%  100% 
 8.30 11.05 12.90 15.25 20.60 

$Height
  0%  25%  50%  75% 100% 
  63   72   76   80   87 

$Volume
  0%  25%  50%  75% 100% 
10.2 19.4 24.2 37.3 77.0
</code></pre>
</section>
</section>
</main>

Función <tt>sapply()</tt>
-------------------------

La función <tt>sapply()</tt> **aplica una función a todos los elementos
de una lista o cualquier objeto que pueda coercionarse a una lista**, y
retornara como resultado de la aplicación de la función un vector, un
arreglo, una lista o una matriz.

La estructura de esta función es la siguiente.

``` r
sapply(X, FUN, ..., simplify = TRUE)
```

-   <tt>X</tt>: Conjunto de observaciones que puede coercionarse a una
    lista.
-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.
-   <tt>simplify</tt>: valor lógico, que permite simplificar el
    resultado obtenido a un vector, matriz o arreglos, si <tt>simplify =
    FALSE</tt>, el valor retornado será en forma de lista, similar al
    obtenido mediante la función <tt>lapply</tt>.

<button id="Show3" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide3" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito3">
<h3 data-toc-skip>
Función <tt>sapply</tt>
</h3>
<p>
Emplee la base de datos <tt>trees</tt> de la base de <tt>R</tt>, y para
ésta, calcule el valor para los cuartiles de cada variable, y retorne
los valores calculados de forma simplificada.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se muestra la estructura de cada variale</span><span class="w">
</span><span class="kc">str</span><span class="p">(</span><span class="n">trees</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>'data.frame':   31 obs. of  3 variables:
 $ Girth : num  8.3 8.6 8.8 10.5 10.7 10.8 11 11 11.1 11.2 ...
 $ Height: num  70 65 63 72 81 83 66 75 80 75 ...
 $ Volume: num  10.3 10.3 10.2 16.4 18.8 19.7 15.6 18.2 22.6 19.9 ...
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calculan los cuartiles para cada variable</span><span class="w">
</span><span class="kc">sapply</span><span class="p">(</span><span class="n">trees</span><span class="p">,</span><span class="w"> </span><span class="n">quantile</span><span class="p">,</span><span class="w"> </span><span class="n">simplify</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">T</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>     Girth Height Volume
0%    8.30     63   10.2
25%  11.05     72   19.4
50%  12.90     76   24.2
75%  15.25     80   37.3
100% 20.60     87   77.0
</code></pre>
</section>
</section>
</main>

Función <tt>vapply()</tt>
-------------------------

La función <tt>vapply()</tt> funciona similar a la función
<tt>sapply</tt> simplificada, puesto que **aplica una función a todos
los elementos de una lista o cualquier objeto que pueda coercionarse a
una lista**, y retornara como resultado de la aplicación de la función
un arreglo. La principal diferencia entre <tt>vapply()</tt> y
<tt>sapply</tt> radica en que, <tt>vapply()</tt> es ligeramente más
velóz (más eficiente) y mejorar la consistencia al proporcionar
comprobaciones de tipo, limitando los valores retornados.

La estructura de esta función es la siguiente.

``` r
vapply(X, FUN, FUN.VALUE, ...)
```

-   <tt>X</tt>: Conjunto de observaciones que puede coercionarse a una
    lista.
-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>FUN.VALUE</tt>: Un vector (generalizado), asociado a los valores
    que se retornarán en <tt>FUN</tt> para observar si éstos cumplen o
    no la condición.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.

<button id="Show4" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Función <tt>vapply</tt>
</h3>
<p>
Emplee la base de datos <tt>trees</tt> de la base de <tt>R</tt>, y para
ésta, calcule el valor para los cuartiles de cada variable, y use como
verificador de resultados que cada valor sea de tipo numérico.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se muestra la estructura de cada variale</span><span class="w">
</span><span class="kc">str</span><span class="p">(</span><span class="n">trees</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>'data.frame':   31 obs. of  3 variables:
 $ Girth : num  8.3 8.6 8.8 10.5 10.7 10.8 11 11 11.1 11.2 ...
 $ Height: num  70 65 63 72 81 83 66 75 80 75 ...
 $ Volume: num  10.3 10.3 10.2 16.4 18.8 19.7 15.6 18.2 22.6 19.9 ...
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calculan los cuartiles para cada variable</span><span class="w">
</span><span class="kc">vapply</span><span class="p">(</span><span class="n">trees</span><span class="p">,</span><span class="w"> </span><span class="n">quantile</span><span class="p">,</span><span class="w"> </span><span class="n">numeric</span><span class="p">(</span><span class="m">5</span><span class="p">))</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>     Girth Height Volume
0%    8.30     63   10.2
25%  11.05     72   19.4
50%  12.90     76   24.2
75%  15.25     80   37.3
100% 20.60     87   77.0
</code></pre>
</section>
</section>
</main>

Función <tt>mapply()</tt>
-------------------------

La función <tt>mapply()</tt> es una versión multivariada de
<tt>sapply()</tt>, puesto que **aplica una función al primer elementos
de cada argumento, luego al segundo elemento de cada argumento y así
sucesivamente**, y retornara como resultado de la aplicación de la
función un vector, un arreglo, una lista o una matriz.

La estructura de esta función es la siguiente.

``` r
mapply(FUN, ..., MoreArgs = NULL, SIMPLIFY = TRUE)
```

-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.
-   <tt>MoreArgs</tt>: Una lista de otros argumentos asociados a
    <tt>FUN</tt>.
-   <tt>simplify</tt>: valor lógico, que permite simplificar el
    resultado obtenido a un vector, matriz o arreglos, si <tt>simplify =
    FALSE</tt>, el valor retornado será en forma de lista, similar al
    obtenido mediante la función <tt>lapply</tt>.

<button id="Show5" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide5" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito5">
<h3 data-toc-skip>
Función <tt>mapply</tt>
</h3>
<p>
Emplee la base de datos <tt>cars</tt> de la base de <tt>R</tt>, y para
ésta, calcule el valor de la velocidad al cuadrado, multiplicada por la
distancia, y dividido todo por la suma entre velocidad y distancia.
Retorne los valores calculados de forma simplificada.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se muestra la estructura de cada variale</span><span class="w">
</span><span class="kc">str</span><span class="p">(</span><span class="n">cars</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>'data.frame':   50 obs. of  2 variables:
 $ speed: num  4 4 7 7 8 9 10 10 10 11 ...
 $ dist : num  2 10 4 22 16 10 18 26 34 17 ...
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se calcula la función
(speed^2 * dist) / (speed + dist) </span><span class="w">
</span><span class="kc">mapply</span><span class="p">(</span><span class="k">function</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="p">)</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="o">^</span><span class="m">2</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">y</span><span class="p">)</span><span class="o">/</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">y</span><span class="p">),</span><span class="w"> </span><span class="n">cars</span><span class="o">$</span><span class="n">speed</span><span class="p">,</span><span class="w"> </span><span class="n">cars</span><span class="o">$</span><span class="n">dist</span><span class="p">,</span><span class="w"> </span><span class="n">SIMPLIFY</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">T</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code> [1]   5.333333  11.428571  17.818182  37.172414  42.666667  42.631579
 [7]  64.285714  72.222222  77.272727  73.464286  86.871795  77.538462
[13]  90.000000  96.000000 100.800000 112.666667 122.255319 122.255319
[19] 131.762712 127.400000 141.120000 158.918919 166.808511 128.571429
[25] 142.682927 176.086957 170.666667 182.857143 188.734694 202.807018
[31] 215.671642 226.800000 245.189189 261.957447 266.823529 236.290909
[37] 255.476923 282.160920 246.153846 282.352941 288.888889 294.736842
[43] 304.761905 363.000000 370.987013 428.936170 456.827586 457.846154
[49] 480.000000 482.954545
</code></pre>
</section>
</section>
</main>

Función <tt>tapply()</tt>
-------------------------

La función <tt>tapply()</tt> **aplica una función a un vector, en base a
una variable factor**, y retornara como resultado de la aplicación de la
función un vector.

La estructura de esta función es la siguiente.

``` r
tapply(X, INDEX, FUN, ..., simplify = TRUE)
```

-   <tt>X</tt>: Conjunto de observaciones que puede coercionarse a un
    vector.
-   <tt>INDEX</tt>: Una lista de uno o más elementos que puedan
    coercionarse a unn factores. Debe ser del mismo tamaño de
    <tt>X</tt>.
-   <tt>FUN</tt>: La función que se aplicará a las filas o las columnas.
-   <tt>`$\ldots$`</tt>: Argumentos adicionales asociados a
    <tt>FUN</tt>.
-   <tt>simplify</tt>: valor lógico, que permite simplificar el
    resultado.

<button id="Show6" class="btn btn-secondary">
Mostrar Ejemplo en <tt>R</tt>
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejemplo en <tt>R</tt>
</button>
<main id="botoncito6">
<h3 data-toc-skip>
Función <tt>tapply</tt>
</h3>
<p>
Emplee la base de datos <tt>cars</tt> de la base de <tt>R</tt>, y para
ésta, calcule el valor promedio de distancia, basados en los diferentes
niveles de velocidad. Retorne los valores calculados de forma
simplificada.
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se muestra la estructura de cada variale</span><span class="w">
</span><span class="kc">str</span><span class="p">(</span><span class="n">cars</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>'data.frame':   50 obs. of  2 variables:
 $ speed: num  4 4 7 7 8 9 10 10 10 11 ...
 $ dist : num  2 10 4 22 16 10 18 26 34 17 ...
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># La media de la distancia, basada
en los niveles de velocidad</span><span class="w">
</span><span class="kc">tapply</span><span class="p">(</span><span class="n">cars</span><span class="o">$</span><span class="n">dist</span><span class="p">,</span><span class="w"> </span><span class="n">cars</span><span class="o">$</span><span class="n">speed</span><span class="p">,</span><span class="w"> </span><span class="n">mean</span><span class="p">,</span><span class="w"> </span><span class="n">simplify</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">T</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>       4        7        8        9       10       11       12       13 
 6.00000 13.00000 16.00000 10.00000 26.00000 22.50000 21.50000 35.00000 
      14       15       16       17       18       19       20       22 
50.50000 33.33333 36.00000 40.66667 64.50000 50.00000 50.40000 66.00000 
      23       24       25 
54.00000 93.75000 85.00000
</code></pre>
</section>
</section>
</main>