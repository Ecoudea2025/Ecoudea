---
title: "Clase 09"
course: "probabilidad-inferencia"
order: 13
classType: "clase"
description: "Introducción a variables aleatorias Variables aleatorias discretas - Funciones de probabilidad - Función de distribución acumulada - Esperanza matemática - Propiedades de esperanza matemática - Varianza - Propiedades de varianza"
math: true
bibliography: "../../referencias.bib"
---

## Variables aleatorias

Es una función que asocia un número real a cada elemento del espacio
muestral `$S$`. Comúnmente las variables aleatorias se denotan por
letras mayúsculas del final del alfabeto `$(X,Y,Z)$` y a los valores
observados por letras minúsculas `$(x,y,z)$`.

Las variables aleatorias se pueden clasificar en tres tipos

-   **Variables Bernoulli:** Cualquier variable aleatoria cuyos posibles
    valores sean 0 o 1.
-   **Variables discretas:** Son aquellas que tienen un número finito de
    posibilidades o una serie interminable de elementos como números
    enteros existentes (es enumerable).
-   **Variables continuas:** Son aquellas que contienen un número
    infinito de posibilidades, o igual número de puntos que un segmento
    de recta.

<button id="Show1" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide1" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito1">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Identifique el tipo de variables aleatorias y asigne un valor numérico a
los elementos del espacio muestral.
</p>
<ol>
<li>
El número de lanzamientos de un dado hasta que caiga un \(4\).
</li>
<li>
La proporción de estudiantes que se encuentran enfermas, en la Facultad
de Ciencias Económicas.
</li>
<li>
Toma un artículo de una banda de ensamble y verificar si éste se
encuentra o no defectuoso.
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Si llamamos a \(F\) al evento de obtener un número diferente a \(4\) y a
\(E\) al evento de obtener un \(4\), entonces observamos que al lanzar
el dado, el número \(4\) puede caer en el primer lanzamiento, o en el
segundo, o en el tercero, etc, etc, y por tanto el espacio muestral
estará dado por $$\begin{align*}
S:\{E, FE, FFE, FFFE, \ldots\}
\end{align*}$$ y en consecuencia, podemos definir la <strong>variable
aleatoria discreta \(X\) </strong> con los números \(1\), \(2\), \(3\),
\(\ldots\), para el número de lanzamientos necesarios hasta obtener un
\(4\). Es decir, la variable aleatoria tendrá dominio en
$$\begin{align*}
X=1, 2, 3, \ldots
\end{align*}$$
</li>
<li>
Dado que es una proporción, entonces el espacio muestral puede ser
cualquier valor que se encuentre entre \(0\) y \(1\), entonces tendremos
a <strong>\(Y\), una variable aleatoria continua </strong> con dominio
definido en $$\begin{align*}
0\leq Y\leq 1
\end{align*}$$
</li>
<li>
El ejercicio consta en elegir un artículo de una banda de ensamble y
comprobar si tiene o no defectos. En consecuencia, se tendrá un espacio
muestral con dos puntos situaciones, \(D\) si el artículo está
defectuoso, y \(N\) si el artículo no está defectuoso, tal que
$$\begin{align*}
S:\{D,N\}
\end{align*}$$ Entonces, como solo pueden haber dos posibilidades,
defectuoso y no defectuoso, podemos definir una variable aleatoria
Bernoulli \(Z\), la cual se definirá como $$\begin{align*}
Z = \begin{cases}
0 & \text{ Si el artículo está defectuoso } \\
1 & \text{ Si el artículo no está defectuoso }
\end{cases}
\end{align*}$$
</li>
</ol>
</main>

## Funciones de probabilidad discreta

Se dice que el conjunto de pares ordenados `$(x,p(x))$` es una función
de masa de probabilidad (*fmp*) de la variable aleatoria discreta `$X$`,
si para cualquier resultado posible de `$X$` se cumple que

1.  `$p(x)\geq0$` para todo `$x \in$` en el dominio de `$X$`
2.  `$\sum_x p(x)=1$`
3.  `$\sum_{x\in A}p(x) = \mathbb{P}(X\in A)$` con `$A$` un conjunto de
    valores `$\in$` al dominio de `$X$`.

<button id="Show2" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide2" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito2">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por \(3\) hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria \(X\), el número de niñas que hay en la familia. Defina
</p>
<ol>
<li>
El espacio muestral \(S\) del experimento aleatorio.
</li>
<li>
Los valores que puede tomar la variable aleatoria \(X\)
</li>
<li>
La función de probabilidad del experimento aleatorio.
</li>
<li>
La función de masa de probabilidad está bien definida?
</li>
<li>
Calcule la probabilidad de que en una familia que posee tres hijos,
hayan \(2\) o más niñas
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Sea \(H\) la letra que representa que el miembro de la familia es niño y
\(M\) para denotar que el miembro de la familia es niña, entonces, se
tendrá que el espacio muestral se define como $$\begin{align*}
S = \{HHH,\;HHM,\;HMH,\;MHH,\;HMM,\;MHM,\;MMH,\;MMM\}
\end{align*}$$
</li>
<li>
Como el interés de la variable aleatoria \(X\) radica en el número de
niñas que hay en la familia, se tendrá entonces que a partir del espacio
muestral \(S\) se puede contar el número de éxitos que hay en cada
situación $$\begin{align*}
S = \{\underset{0}{HHH},\;\underset{1}{HHM},\;\underset{1}{HMH},\;\underset{1}{MHH},\;\underset{2}{HMM},\;\underset{2}{MHM},\;\underset{2}{MMH},\;\underset{3}{MMM}\}
\end{align*}$$ Evidenciando, que podemos asignar los valores \(0,\)
\(1,\) \(2\) y \(3\) a la variable aleatoria \(X\).
</li>
<li>

Para encontrar la función de probabilidades del experimento aleatorio
asociadas a la variable aleatoria \(X\), podemos emplear la definición
de la
<a href="../../EstadisticaI/EstIClase04.html#probabilidad" target="\_blank">frecuencia
relativa</a>, aprovechando que todos los puntos del espacio muestral
poseen la misma probabilidad. En otro caso podríamos emplear un diagrama
de árbol para encontrar dichas probabilidades.<br>

Para el caso de \(X=0\), observamos que de las \(8\) posibles
situaciones que hay dentro del espacio muestral \(S\), solo tenemos una
situación en donde no hay ninguna mujer, y en consecuencia, al aplicar
la definición de
<a href="../../EstadisticaI/EstIClase04.html#probabilidad" target="\_blank">frecuencia
relativa</a>, se tendrá que la probabilidad de que \(X=0\), es
$$\begin{align*}
\mathbb{P}(X=0) = \frac{1}{8}
\end{align*}$$ Procedimiento similar se aplica para \(X=1\), \(X=2\) y
\(X=3\), obteniendo como resultado la siguiente tabla de probabilidades

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

</li>
<li>
Si, la variable aleatoria se encuentra bien definida, dado que cada una
de las probabilidades es mayor o igual a \(0\), además, al sumar cada
una de las probabilidades de la tabla

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

se encuentra que dicha suma es igual a \(1\).
</li>
<li>

Dado que solo nos interesa la situación en la cual hay \(2\) o más
niñas, se tendrá que nos están preguntando por la probabilidad de que

$$\begin{align*}
\mathbb{P}(X\geq2) = \sum_{x=2}^3p(x) = p(2) + p(3) = \frac{3}{8} + \frac{1}{8} = \frac{1}{2}
\end{align*}$$

y en consecuencia, se tendrá que la probabilidad de que en una familia
de \(3\) hijos, se tenga \(2\) o más niñas, es del \(50\%\).
</li>
</ol>
</main>

## Función de distribución acumulada caso discreto

La función de distribución acumulada (*fda*) denotada por `$F(x)$`, para
una variable aleatoria discreta `$X$` con distribución de probabilidad
`$p(x)$` es de la forma

$$\begin{align*}F(x)=\mathbb{P}(X\leq x)=\sum_{t\leq x}p(t) \quad \quad -\infty<x<\infty\end{align*}$$

para cualquier `$x$` dentro del rango de `$X$`, `$F(x)$` será la suma
acumulada de todos los valores de rango de `$X$` menores a `$x$`.

**Nota:** Si se quieren calcular probabilidades con la función de
distribución acumulada en el caso discreto, entonces, si `$a$` y `$b$`
son dos números **constantes enteras**, deberán tenerse en cuenta las
siguientes reglas

-   `$\mathbb{P}(a \leq X \leq b) = \mathbb{P}(X\leq b) - \mathbb{P}(X\leq a - 1) = F(b) - F(a - 1)$`
-   `$\mathbb{P}(a < X \leq b) = \mathbb{P}(X\leq b) - \mathbb{P}(X\leq a)  = F(b) - F(a)$`
-   `$\mathbb{P}(a \leq X < b) = \mathbb{P}(X\leq b-1) - \mathbb{P}(X\leq a-1) = F(b - 1) - F(a - 1)$`
-   `$\mathbb{P}(a < X < b) = \mathbb{P}(X\leq b-1) - \mathbb{P}(X\leq a) = F(b - 1) - F(a)$`
-   `$\mathbb{P}(X \geq a) = 1 - \mathbb{P}(X\leq a-1) = 1 - F(a-1)$`
-   `$\mathbb{P}(X > a) = 1 - \mathbb{P}(X\leq a) = 1 - F(a)$`
-   `$\mathbb{P}(X \leq b) = F(b)$`
-   `$\mathbb{P}(X < b) = \mathbb{P}(X\leq b-1) = F(b - 1)$`

<button id="Show3" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide3" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito3">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por \(3\) hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria \(X\), el número de niñas que hay en la familia.
</p>
<ol>
<li>
Calcule la función de distribución acumulada \(F(x)\).
</li>
<li>
Calcule la probabilidad de que en una familia que posee tres hijos,
hayan \(2\) o más niñas, mediante el uso de \(F(x)\).
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Como la función de distribución acumulada parte de la función de masa de
probabilidad, calculamos la función de masa de probabilidad para el
número de niñas que hay en una familia que posee \(3\) hijos.

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

A partir de ésta tabla se procede a realizar el cálculo de la función de
distribución acumulada \(F(x)\). Para ello, debemos calcular las
siguientes probabilidades \(F(0) = \mathbb{P}(X\leq 0)\),
\(F(1) = \mathbb{P}(X\leq1)\), \(F(2) = \mathbb{P}(X\leq2)\) y
\(F(3) = \mathbb{P}(X\leq3)\)

$$\begin{align*}
F(0) & = \mathbb{P}(X\leq0) = p(0) = \frac{1}{8} \\
F(1) & = \mathbb{P}(X\leq1) = p(0) + p(1) = \frac{1}{8} + \frac{3}{8} =  \frac{4}{8}\\
F(2) & = \mathbb{P}(X\leq2) = \sum_{x=0}^{2} p(x) = \frac{1}{8} + \frac{3}{8} + \frac{3}{8} =  \frac{7}{8} \\
F(3) & = \mathbb{P}(X\leq3) = \sum_{x=0}^{3} p(x) = \frac{1}{8} + \frac{3}{8} + \frac{3}{8} + \frac{1}{8} = \frac{8}{8}
\end{align*}$$

Entonces, mediante el empleo de estas probabilidades, podemos construir
la función de distribución acumulada para la variable aleatoria \(X\),
tal que

$$\begin{align*}
F(x) = \begin{cases} 0 & x<0 \\
                     \frac{1}{8}  & 0\leq x<1 \\
                     \frac{4}{8}  & 1\leq x<2 \\
                     \frac{7}{8}  & 2\leq x<3 \\
                     \frac{8}{8}  & x\geq 3
       \end{cases}
\end{align*}$$ En donde se aprecia, que para valores menores a \(0\), no
hay ninguna probabilidad definida, para valores mayores o iguales a
\(0\) pero menores que \(1\) solo está definido \(F(0)=p(0)\), para
valores mayores o iguales a \(1\) pero menores que \(2\) está definido
\(F(1)=p(0)+p(1)\), para valores mayores o iguales a \(2\) pero menores
que \(3\) está definido \(F(2)=p(0)+p(1)+p(2)\), y para valores mayores
o iguales a \(3\) está definido \(F(3)=p(0)+p(1)+p(2)+p(3)\).
</li>
<li>

Dado que el interés es calcular la probabilidad de que en una familia de
\(3\) hijos hayan \(2\) o más niñas, entonces se tendrá que la
probabilidad de interés es la siguiente $$\begin{align*}
\mathbb{P}(X \geq 2)
\end{align*}$$

Entonces, siguiendo las reglas anteriormente expuestas para la
probabilidad acumulada, dicha probabilidad puede calcularse mediante

$$\begin{align*}
\mathbb{P}(X \geq 2) & = 1 - \mathbb{P}(X < 2) \\
                     & = 1 - F(2-1) \\
                     & = 1 - F(1) \\
                     & = 1 - \frac{4}{8} \\
                     & = \frac{1}{2}
\end{align*}$$

y por tanto, se tendrá que la probabilidad de que en una familia de
\(3\) hijos, tengan \(2\) o más niñas es de \(50\%\).
</li>
</ol>
</main>

## Esperanza matemática caso discreto

Si `$X$` es una variable aleatoria con función de masa de probabilidad
`$p(x)$`, entonces la media o valor esperado de la variable aleatoria se
denota por `$\mathbb{E}(X)$` o `$\mu$` está dada por

$$\begin{align*}\mathbb{E}(X)=\sum_{x}xp(x)\end{align*}$$

<button id="Show4" class="btn btn-secondary">Mostrar Ejercicio </button>
<button id="Hide4" class="btn btn-info">Ocultar Ejercicio </button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por \(3\) hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria \(X\), el número de niñas que hay en la familia. Calcule el
valor esperado del número de niñas que hay en una familia que posee
\(3\) hijos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Como para calcular la esperanza matemática debemos calcular primero la
función de masa de probabilidad, entonces calculamos la tabla asociada a
la función de distribución para el número de niñas que hay en una
familia que posee \(3\) hijos.
</p>

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

<p>

A partir de ésta tabla se realiza el cálculo de la esperanza matemática
de la variable aleatoria mediante la ecuación

$$\begin{align*}
\mathbb{E}(X)&=\sum_{x=0}^3x\,p(x) \\
             &=0\,p(0)+1\,p(1)+2\,p(2)+3\,p(3) \\
             &=0\left(\frac{1}{8}\right)+1\left(\frac{3}{8}\right)+2\left(\frac{3}{8}\right)+3\left(\frac{1}{8}\right) \\
             &=0+\frac{3}{8}+\frac{6}{8}+\frac{3}{8} \\
             &=\frac{12}{8} \\
             &=1.5
\end{align*}$$

se tendrá que el número promedio de niñas que se espera encontrar en una
familia que posee \(3\) hijos es de \(1.5\) niñas.
</p>
</main>

### Propiedades de la esperanza matemática

Sea `$a$` y `$b$` dos números constantes `$\in \mathbb{R}$` y `$X$` una
variable aleatoria, entonces se tiene que

-   `$\mathbb{E}(a) = a$`
-   `$\mathbb{E}(bX) = b\mathbb{E}(X)$`
-   `$\mathbb{E}(a+bX) = a+ b\mathbb{E}(X)$`
-   si `$m(X)$` es una función de `$X$`, entonces


$$\begin{align*}\mathbb{E}(m(X))=\sum_xm(x)p(x)\end{align*}$$


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
Suponga un experimento aleatorio que consta en consultar una familia
conformada por \(3\) hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria \(X\) como el número de niñas que hay en la familia, calcule
</p>
<ol>
<li>
\(\mathbb{E}(X+2)\)
</li>
<li>
\(\mathbb{E}(3X)\)
</li>
<li>
\(\mathbb{E}(X^2)\)
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<p>
Similar al caso anterior, calculamos la función de masa de probabilidad
para el número de niñas que hay en una familia que posee \(3\) hijos.
</p>
<ol>

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

<li>

A partir de la tabla anterior, se procede a realizar el cálculo de
\(\mathbb{E}(X+2)\), tal que

$$\begin{align*}
\mathbb{E}(X+2)&=\sum_{x=0}^3(x+2)\,p(x) \\
             &=(0+2)\,p(0)+(1+2)\,p(1)+(2+2)\,p(2)+(3+2)\,p(3) \\
             &=2\left(\frac{1}{8}\right)+3\left(\frac{3}{8}\right)+4\left(\frac{3}{8}\right)+5\left(\frac{1}{8}\right) \\
             &=\frac{2}{8}+\frac{9}{8}+\frac{12}{8}+\frac{5}{8} \\
             &=\frac{28}{8} \\
             &=3.5
\end{align*}$$

Resultado similar, puede obtenerse mediante la propiedad
\(\mathbb{E}(X+b)=\mathbb{E}(X)+b\), en donde ya sabemos que
\(\mathbb{E}(X)=1.5\), y en consecuencia se tendrá que

$$\begin{align*}
\mathbb{E}(X+2)&=\mathbb{E}(X) + 2 \\
             &=1.5 + 2 \\
             &=3.5
\end{align*}$$
</li>
<li>

Similar al caso anterio, se tiene que para realizar el cálculo de
\(\mathbb{E}(3X)\), es posible emplear la definición de esperanza
matemática, tal que

$$\begin{align*}
\mathbb{E}(3X)&=\sum_{x=0}^33x\,p(x) \\
             &=(3)(0)\,p(0)+(3)(1)\,p(1)+(3)(2)\,p(2)+(3)(3)\,p(3) \\
             &=0\left(\frac{1}{8}\right)+3\left(\frac{3}{8}\right)+6\left(\frac{3}{8}\right)+9\left(\frac{1}{8}\right) \\
             &=\frac{9}{8}+\frac{18}{8}+\frac{9}{8} \\
             &=\frac{36}{8} \\
             &=4.5
\end{align*}$$ Resultado similar, puede obtenerse mediante la propiedad
\(\mathbb{E}(aX)=a\mathbb{E}(X)\), en donde ya sabemos que
\(\mathbb{E}(X)=1.5\), y en consecuencia se tendrá que

$$\begin{align*}
\mathbb{E}(aX)&=3\mathbb{E}(X) \\
             &=(3)(1.5) \\
             &=4.5
\end{align*}$$
</li>
<li>

Finalmente, para encontrar la \(\mathbb{E}(X^2)\) se tendrá que en este
caso \(m(X) = X^2\), y por tanto, al aplicar la propiedad
\(\mathbb{E}(m(X))= \sum_{x}m(x)p(x)\) tendremos que

$$\begin{align*}
\mathbb{E}(X^2)&=\sum_{x=0}^3x^2\,p(x) \\
             &=0^2\,p(0)+1^2\,p(1)+2^2\,p(2)+3^2\,p(3) \\
             &=0\left(\frac{1}{8}\right)+1\left(\frac{3}{8}\right)+4\left(\frac{3}{8}\right)+9\left(\frac{1}{8}\right) \\
             &=0+\frac{3}{8}+\frac{12}{8}+\frac{9}{8} \\
             &=\frac{24}{8} \\
             &=3
\end{align*}$$
</li>
</ol>
</main>

## Varianza caso discreto

Sea `$X$` una variable aleatoria con *fmp* `$p(x)$`, entonces si
`$m(X) = (X - \mathbb{E}(X))^2$`, se tendrá que la varianza de `$X$` que
se denota `$Var(X)$` o `$\sigma^2$` estará dada por

$$\begin{align*}Var(X) = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)^2\right]=\sum_x(x-\mathbb{E}(X))^2p(x)\end{align*}$$


Puede demostrarse a partir de la ecuación anterior, que una alternativa
para el cálculo de la `$Var(X)$` es de la forma


$$\begin{align*}Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2\end{align*}$$


además, la raíz cuadrada de la varianza de `$X$` se llama desviación
estándar de `$X$`, se denota por `$Sd(X)$` o `$\sigma$` y se define como

$$\begin{align*}Sd(X) = \sqrt{Var(X)}\end{align*}$$


<button id="Show6" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito6">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por \(3\) hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria \(X\), el número de niñas que hay en la familia.
</p>
<ol>
<li>
Calcule la \(Var(X)\).
</li>
<li>
Calcule la \(Sd(X)\).
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<p>
Como la función de varianza es en sí, es una esperanza matemática,
entonces iniciamos con el cálculo de la función de masa de probabilidad
para el número de niñas que hay en una familia que posee \(3\) hijos.
</p>

<table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
\(X\)
</td>
<td style="text-align:left;">
\(0\)
</td>
<td style="text-align:left;">
\(1\)
</td>
<td style="text-align:left;">
\(2\)
</td>
<td style="text-align:left;">
\(3\)
</td>
</tr>
<tr>
<td style="text-align:left;">
\(p(x)\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{3}{8}\)
</td>
<td style="text-align:left;">
\(\frac{1}{8}\)
</td>
</tr>
</tbody>
</table>

<ol>
<li>

A partir de la tabla anterior, se procede a realizar el cálculo de
\(Var(X)\), a partir de los valores ya calculado de
\(\mathbb{E}(X^2)=3\) y \(\mathbb{E}(X)=1.5\), tal que

$$\begin{align*}
Var(X)&=\mathbb{E}(X^2) - \mathbb{E}(X)^2 \\
        &=3 - (1.5)^2 \\
        &=3 - 2.25 \\
        &=0.75
\end{align*}$$

Y en consecuencia, se tendrá que la varianza del número de niña que hay
en una familia que posee \(3\) hijos es de \(0.75\) hijos\(^2\).
</li>
<li>

Basado en el valor de la varianza \(Var(X)=0.75\), se procede a realizar
el cálculo de la desviación estándar de la variable aleatoria \(X\),
\(Sd(X)\), tal que

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.75} \\
      &= 0.8660
\end{align*}$$

Es decir, se tendrá que el número promedio de niñas que tiene una
familia que posee \(3\) hijos es de \(1.5\) niñas, con una desviación
estándar de \(0.8660\) niñas.
</li>
</ol>
</main>

### Propiedades de la varianza

Sea `$a$` y `$b$` números reales (constantes) y `$X$` una variable
aleatorias, entonces se tiene que

1.  `$Var(a)=0$`
2.  `$Var(aX)=a^2Var(X)$`
3.  `$Var(a+bX) = b^2Var(X)$`