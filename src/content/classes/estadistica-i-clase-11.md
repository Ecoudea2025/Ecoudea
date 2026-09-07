---
title: "Clase 12"
course: "estadistica-i"
order: 16
classType: "clase"
description: "Esperanza matemática - Caso discreto - Caso continuo - Caso multivariado Propiedades de la esperanza matemática"
math: true
bibliography: "../../referencias.bib"
---

Esperanza matemática
--------------------

### Caso univariado

Sea $X$ una variable aleatoria con función de masa de probabilidad
dada por $p(x)$ o función de densidad de probabilidad dada por
$f(x)$, entonces la media o valor esperado de $X$, denotado por
$\mathbb{E}(X)$ o $\mu$ está dado por

$$\begin{align*}\mathbb{E}(X) = \mu =\begin{cases} \sum_{x}xp(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty xf(x) dx & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


<button id="Show1" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide1" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
</button>
<main id="botoncito1">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por $3$ hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria $X$, el número de niñas que hay en la familia, y se define
la función de masa de probabilidad como
</p>
<div style="font-size:120%!important">
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
$X$
</td>
<td style="text-align:left;">
$0$
</td>
<td style="text-align:left;">
$1$
</td>
<td style="text-align:left;">
$2$
</td>
<td style="text-align:left;">
$3$
</td>
</tr>
<tr>
<td style="text-align:left;">
$p(x)$
</td>
<td style="text-align:left;">
$\frac{1}{8}$
</td>
<td style="text-align:left;">
$\frac{3}{8}$
</td>
<td style="text-align:left;">
$\frac{3}{8}$
</td>
<td style="text-align:left;">
$\frac{1}{8}$
</td>
</tr>
</tbody>
</table>
</div>
<p>
Calcule el valor esperado del número de niñas que hay en una familia que
posee $3$ hijos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Basados en la tabla asociada a la distribución de masa de probabilidad
para el número de niñas que hay en una familia que tiene $3$ hijos, se
realiza el cálculo de la esperanza matemática de la variable aleatoria
mediante la ecuación

$$\begin{align*}
\mathbb{E}(X)&=\sum_{x=0}^3x\,p(x) \\
             &=0\,p(0)+1\,p(1)+2\,p(2)+3\,p(3) \\
             &=0\left(\frac{1}{8}\right)+1\left(\frac{3}{8}\right)+2\left(\frac{3}{8}\right)+3\left(\frac{1}{8}\right) \\
             &=0+\frac{3}{8}+\frac{6}{8}+\frac{3}{8} \\
             &=\frac{12}{8} \\
             &=1.5
\end{align*}$$

se tendrá que el número promedio de niñas que se espera encontrar en una
familia que posee $3$ hijos es de $1.5$ niñas.
</p>
</main>
<button id="Show2" class="btn btn-secondary">
Mostrar Ejercicio Caso Continuo
</button>
<button id="Hide2" class="btn btn-info">
Ocultar Ejercicio Caso Continuo
</button>
<main id="botoncito2">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$
siendo $X$ una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo.
Calcule el valor esperado del tiempo que tarda la serie financiera en
cumplir un ciclo.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Conocida la función de densida de probabilidad, se procede a calcular el
valor esperado del tiempo que tarda la serie financiera en cumplir un
ciclo, tal que $$\begin{align*}
\mathbb{E}(X)&= \int_{0}^1x\,f(x) dx\\
             &= \int_{0}^1x\,30x^2(1-x)^2 dx\\
             &= 30\int_{0}^1x^3\,(1-x)^2 dx\\
             &= 30 \int_{0}^1x^3\,(1-2x+x^2) dx\\
             &= 30 \int_{0}^1x^3-2x^4+x^5 dx\\
             &= 30 \left(\frac{x^4}{4} - 2\frac{x^5}{5} + \frac{x^6}{6}\right)\Bigg|_0^1 \\
             &= 30 \left[\left(\frac{1^4}{4} - 2\frac{1^5}{5} + \frac{1^6}{6}\right) - \left(\frac{0^4}{4} - 2\frac{0^5}{5} + \frac{0^6}{6}\right)\right] \\
             &= 30 \left(\frac{1}{4} - \frac{2}{5} + \frac{1}{6}\right) \\
             &= 0.5
\end{align*}$$
Y por tanto, se tendrá que el tiempo esperado que tarda
una serie financiera en cumplir un ciclo será $0.5$ horas, la cual al
pasarla a minutos mediante la regla de tres

$$\begin{align*}
1_\text{hora}  &- 60_\text{min}\\0.5_\text{horas} &- a
\end{align*}$$

se tendrá que $$\begin{align*}
a= \frac{0.5_\text{horas}\times 60_\text{min}}{1_\text{hora}} = 30_\text{min}
\end{align*}$$

el tiempo esperado que tarda una serie financiera en cumplir un ciclo
será de $30$ minutos.
</p>
</main>

### Propiedades de la esperanza matemática

Sea $a$ y $b$ números reales (constantes) y $X$ una variable
aleatoria con función de masa de probabilidad dada por $p(x)$ o
función de densidad de probabilidad dada por $f(x)$, entonces

-   $\mathbb{E}(a) = a$
-   $\mathbb{E}(bX) = b\mathbb{E}(X)$
-   $\mathbb{E}(a+bX) = a+ b\mathbb{E}(X)$
-   Si $m(X)$ es una función de $X$, entonces


$$\begin{align*}\mathbb{E}(m(X))=\begin{cases} \sum_{x}m(x)p(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty m(x)f(x) dx & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


<button id="Show3" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide3" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
</button>
<main id="botoncito3">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por $3$ hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria $X$, como el número de niñas que hay en la familia, y se
tiene que la función de probabilidad está dada por
</p>
<div style="font-size:120%!important">
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
$X$
</td>
<td style="text-align:left;">
$0$
</td>
<td style="text-align:left;">
$1$
</td>
<td style="text-align:left;">
$2$
</td>
<td style="text-align:left;">
$3$
</td>
</tr>
<tr>
<td style="text-align:left;">
$p(x)$
</td>
<td style="text-align:left;">
$\frac{1}{8}$
</td>
<td style="text-align:left;">
$\frac{3}{8}$
</td>
<td style="text-align:left;">
$\frac{3}{8}$
</td>
<td style="text-align:left;">
$\frac{1}{8}$
</td>
</tr>
</tbody>
</table>
</div>
<p>
Calcule
</p>
<ol>
<li>
$\mathbb{E}(X+2)$
</li>
<li>
$\mathbb{E}(3X)$
</li>
<li>
$\mathbb{E}(X^2)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

A partir de la tabla de distribución de probabilidad, se procede a
realizar el cálculo de $\mathbb{E}(X+2)$, tal que

$$\begin{align*}
\mathbb{E}(X+2)&=\sum_{x=0}^3(x+2)\,p(x) \\
             &=(0+2)\,p(0)+(1+2)\,p(1)+(2+2)\,p(2)+(3+2)\,p(3) \\
             &=2\left(\frac{1}{8}\right)+3\left(\frac{3}{8}\right)+4\left(\frac{3}{8}\right)+5\left(\frac{1}{8}\right) \\
             &=\frac{2}{8}+\frac{9}{8}+\frac{12}{8}+\frac{5}{8} \\
             &=\frac{28}{8} \\
             &=3.5
\end{align*}$$

Resultado similar, puede obtenerse mediante la propiedad
$\mathbb{E}(X+b)=\mathbb{E}(X)+b$, en donde ya sabemos que
$\mathbb{E}(X)=1.5$, y en consecuencia se tendrá que

$$\begin{align*}
\mathbb{E}(X+2)&=\mathbb{E}(X) + 2 \\
             &=1.5 + 2 \\
             &=3.5
\end{align*}$$
</li>
<li>

Similar al caso anterio, se tiene que para realizar el cálculo de
$\mathbb{E}(3X)$, es posible emplear la definición de esperanza
matemática, tal que

$$\begin{align*}
\mathbb{E}(3X)&=\sum_{x=0}^33x\,p(x) \\
             &=(3)(0)\,p(0)+(3)(1)\,p(1)+(3)(2)\,p(2)+(3)(3)\,p(3) \\
             &=0\left(\frac{1}{8}\right)+3\left(\frac{3}{8}\right)+6\left(\frac{3}{8}\right)+9\left(\frac{1}{8}\right) \\
             &=\frac{9}{8}+\frac{18}{8}+\frac{9}{8} \\
             &=\frac{36}{8} \\
             &=4.5
\end{align*}$$
Resultado similar, puede obtenerse mediante la propiedad
$\mathbb{E}(aX)=a\mathbb{E}(X)$, en donde ya sabemos que
$\mathbb{E}(X)=1.5$, y en consecuencia se tendrá que

$$\begin{align*}
\mathbb{E}(aX)&=3\mathbb{E}(X) \\
             &=(3)(1.5) \\
             &=4.5
\end{align*}$$
</li>
<li>

Finalmente, para encontrar la $\mathbb{E}(X^2)$ se tendrá que en este
caso $m(X) = X^2$, y por tanto, al aplicar la propiedad
$\mathbb{E}(m(X))= \sum_{x}m(x)p(x)$ tendremos que

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
<button id="Show4" class="btn btn-secondary">
Mostrar Ejercicio Caso Continuo
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejercicio Caso Continuo
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$
siendo $X$ una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo.
Calcule
</p>
<ol>
<li>
$\mathbb{E}(60X)$
</li>
<li>
$\mathbb{E}(X+40)$
</li>
<li>
$\mathbb{E}(X^2)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<p>
Dado que la función de densidad de probabilidad estádada por
$$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$
</p>
<ol>
<li>

se procede a calcular $\mathbb{E}(60X)$, tal que $$\begin{align*}
\mathbb{E}(60X)&= \int_{0}^160x\,f(x) dx\\
             &= \int_{0}^1(60x)\,30x^2(1-x)^2 dx\\
             &= 1800\int_{0}^1x^3\,(1-x)^2 dx\\
             &= 1800 \int_{0}^1x^3\,(1-2x+x^2) dx\\
             &= 1800 \int_{0}^1x^3-2x^4+x^5 dx\\
             &= 1800 \left(\frac{x^4}{4} - 2\frac{x^5}{5} + \frac{x^6}{6}\right)\Bigg|_0^1 \\
             &= 1800 \left[\left(\frac{1^4}{4} - 2\frac{1^5}{5} + \frac{1^6}{6}\right) - \left(\frac{0^4}{4} - 2\frac{0^5}{5} + \frac{0^6}{6}\right)\right] \\
             &= 1800 \left(\frac{1}{4} - \frac{2}{5} + \frac{1}{6}\right) \\
             &= 30
\end{align*}$$

Similarmente, al usar la propiedad $\mathbb{E}(aX)=a\mathbb{E}(X)$,
sabiendo que $\mathbb{E}(X)=0.5$ se tendrá que $$\begin{align*}
\mathbb{E}(60X)&= 60\mathbb{E}(X) \\
               &= 60(0.5) \\
               &= 30 \\
\end{align*}$$
</li>
<li>

Para el cálculo de $\mathbb{E}(X+40)$, se procede a la aplicación de
la ecuación de esperanza matemática, tal que $$\begin{align*}
\mathbb{E}(X+40)&= \int_{0}^1(x+40)\,f(x) dx\\
             &= \int_{0}^1(x+40)\,30x^2(1-x)^2 dx\\
             &= 30\left[\int_{0}^1x^3\,(1-x)^2 dx + 40\int_{0}^1x^2\,(1-x)^2 dx\right]\\
             &= 30 \left[\int_{0}^1x^3\,(1-2x+x^2) dx + 40\int_{0}^1x^2\,(1-2x+x^2) dx\right]\\
             &= 30 \left[\int_{0}^1x^3-2x^4+x^5 dx + 40\int_{0}^1x^2-2x^3+x^4 dx\right]\\
             &= 30 \left[\left(\frac{x^4}{4} - 2\frac{x^5}{5} + \frac{x^6}{6}\right)\Bigg|_0^1 + 40\left(\frac{x^3}{3} - 2\frac{x^4}{4} + \frac{x^5}{5}\right)\Bigg|_0^1\right] \\
             &= 30 \left[\left(\frac{1^4}{4} - 2\frac{1^5}{5} + \frac{1^6}{6}\right) - \left(\frac{0^4}{4} - 2\frac{0^5}{5} + \frac{0^6}{6}\right) + 40\left(\frac{1^3}{3} - 2\frac{1^4}{4} + \frac{1^5}{5}\right) - 40\left(\frac{0^3}{3} - 2\frac{0^4}{4} + \frac{0^5}{5}\right)\right] \\
             &= 30 \left[\left(\frac{1}{4} - \frac{2}{5} + \frac{1}{6}\right) + 40\left(\frac{1}{3} - \frac{2}{4} + \frac{1}{5}\right)\right] \\
             &= 40.5
\end{align*}$$

Ahora, aplicando la propiedad $\mathbb{E}(X+b)=\mathbb{E}(X)+b$, se
tendrá que dicha esperanza puede calcularse en dos lineas, tal que
$$\begin{align*}
\mathbb{E}(X+40)&= \mathbb{E}(X) + 40\\
               &= 0.5 + 40 \\
               &= 40.5 \\
\end{align*}$$
</li>
<li>
Para el cálculo de la $\mathbb{E}(X^2)$, se tendrá que en este caso
$m(X) = X^2$, y por tanto, al aplicar la propiedad
$\mathbb{E}(m(X))=\int_{-\infty}^\infty m(x)f(x) dx$ tendremos que
$$\begin{align*}
\mathbb{E}(X^2)&= \int_{0}^1x^2\,f(x) dx\\
               &= \int_{0}^1x^2\,30x^2(1-x)^2 dx\\
               &= 30\int_{0}^1x^4\,(1-x)^2 dx\\
               &= 30 \int_{0}^1x^4\,(1-2x+x^2) dx\\
               &= 30 \int_{0}^1x^4-2x^5+x^6 dx\\
               &= 30 \left(\frac{x^5}{5} - 2\frac{x^6}{6} + \frac{x^7}{7}\right)\Bigg|_0^1 \\
               &= 30 \left[\left(\frac{1^5}{5} - 2\frac{1^6}{6} + \frac{1^7}{7}\right) - \left(\frac{0^5}{5} - 2\frac{0^6}{6} + \frac{0^7}{7}\right)\right] \\
               &= 30 \left(\frac{1}{5} - \frac{2}{6} + \frac{1}{7}\right) \\
               &= 0.2857142857
\end{align*}$$
</li>
</ol>
</main>

### Caso multivariado

Sea $X, Y$ variables aleatorias con función de masa de probabilidad
conjunta dada por $p(x,y)$ o función de densidad de probabilidad
conjunta dada por $f(x,y)$, entonces si la función $m(X,Y)$ que
depende tanto de $X$ como de $Y$, se tendrá que el valor esperado de
$m(X,Y)$ es de la forma

$$\begin{align*}\mathbb{E}(m(X,Y))=\begin{cases} \sum_{y}\sum_{x}m(x,y)p(x,y) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty \int_{-\infty}^\infty m(x,y)f(x,y) dxdy & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


Ahora, si la función $m(X,Y) = m(X)$ solo depende de $X$, y $g(x)$
es la función de distribución marginal de $X$, se tendrá que el valor
esperado de $m(X)$ es de la forma

$$\begin{align*}\mathbb{E}(m(X))=\begin{cases} \sum_{x}m(x)g(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty m(x)g(x) dx & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


mientras que, si la función $m(X,Y) = m(Y)$ solo depende de $Y$, y
$h(y)$ es la función de distribución marginal de $Y$, se tendrá que
el valor esperado de $m(Y)$ es de la forma

$$\begin{align*}\mathbb{E}(m(Y))=\begin{cases} \sum_{y}m(y)h(y) & \text{ si } Y \text{ es discreta}  \\ \int_{-\infty}^\infty m(y)h(y) dy & \text{ si } Y \text{ es continua} \end{cases}\end{align*}$$


<button id="Show5" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide5" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
</button>
<main id="botoncito5">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento que consta en lanzar dos dados al aire. Sea $X$
la variable aleatoria que indica la suma resultante de los dos dados, y
$Y$ la variable aleatoria del valor absoluto de la diferencia de los
dos dados, en donde, la función de masa de probabilidad conjunta está
dada por
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto; font-size:120%!important">
<tbody>
<tr>
<td rowspan="2" colspan="2" style="text-align:center; vertical-align: middle;">
<script type="math/tex">p(x,y)</script>
</td>
<td style="text-align:center;" colspan="11">
<script type="math/tex">X</script>
</td>
<td style="text-align:center;vertical-align: middle !important;" rowspan="2">
<script type="math/tex">h(y)</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{2}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{3}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{4}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{5}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{6}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{7}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{8}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{9}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{10}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{11}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{12}</script>
</td>
</tr>
<tr>
<td style="text-align:center;vertical-align: middle !important;" rowspan="6">
<script type="math/tex">Y</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\mathbf{0}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{6}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{1}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{10}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{2}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{8}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{3}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{6}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{4}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{4}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;">
<script type="math/tex">\mathbf{5}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
</tr>
<tr>
<td style="text-align:center;" colspan="2">
<script type="math/tex">g(x)</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{3}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{4}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{5}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{6}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{5}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{4}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{3}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{1}{36}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{36}{36}</script>
</td>
</tr>
</tbody>
</table>
<p>
Entonces, basados en dicha función de masa de probabilidad conjunta,
calcule
</p>
<ol>
<li>
$\mathbb{E}(X)$
</li>
<li>
$\mathbb{E}(Y)$
</li>
<li>
$\mathbb{E}(XY)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Dado que estamos interesados en calcular $\mathbb{E}(X)$, la cual solo
depende de la variable aleatoria $X$, entonces podemos emplear la
distribución marginal $g(x)$ para realizar el cálculo, tal que
$$\begin{align*}
\mathbb{E}(X)&=\sum_{x=2}^{12}x\,g(x) \\
             &=(2)\,g(2)+(3)\,g(3)+(4)\,g(4)+\ldots+(12)\,g(12) \\
             &=2\left(\frac{1}{36}\right)+3\left(\frac{2}{36}\right)+4\left(\frac{3}{36}\right)+\ldots + 12\left(\frac{1}{36}\right) \\
             &=\frac{2}{36}+\frac{6}{36}+\frac{12}{36}+\ldots + \frac{12}{36} \\
             &=\frac{252}{36} \\
             &=7
\end{align*}$$
Por tanto se tendrá que el valor esperado para la suma
resultante de los dos dados es de $7$.
</li>
<li>
Similar al procedimiento anterior, se realiza el cálculo de la
$\mathbb{E}(Y)$, la cual, al depender solo de la variable aleatoria
$Y$, permite que se realice el cálculo mediante el empleo de la
distribución marginal $h(y)$, tal que $$\begin{align*}
\mathbb{E}(Y)&=\sum_{y=0}^{5}y\,h(y) \\
             &=(0)\,h(0)+(1)\,h(1)+(2)\,h(2)+\ldots+(5)\,h(5) \\
             &=0\left(\frac{6}{36}\right)+1\left(\frac{10}{36}\right)+2\left(\frac{8}{36}\right)+\ldots + 5\left(\frac{2}{36}\right) \\
             &=0+\frac{10}{36}+\frac{16}{36}+\ldots + \frac{10}{36} \\
             &=\frac{70}{36} \\
             &=1.9444
\end{align*}$$
Por tanto se tendrá que el valor esperado para el valor
absoluto de la diferencia de los dos dados es de $1.9444$.
</li>
<li>
En este caso, estamos interesados en calcular la $\mathbb{E}(XY)$, en
donde, al depender la esperanza matemática de las dos variables
aleatorias, entonces empleamos la función de distribución conjunta
$p(x,y)$ tal que $$\begin{align*}
\mathbb{E}(XY)&=\sum_{x=2}^{12}\sum_{y=0}^{5}xy\,p(x,y) \\
             &=(2)(0)\,p(2,0)+(2)(1)\,p(2,1)+\ldots + (3)(0)\,p(3,0)+(3)(1)\,p(3,1)+\ldots+(12)(5)\,p(12,5) \\
             &=(2)(0)\left(\frac{1}{36}\right)+(2)(1)\left(0\right)+\ldots+(3)(0)\left(0\right)+(3)(1)\left(\frac{2}{36}\right)+\ldots + (12)(5)\left(0\right) \\
             &=0+\frac{6}{36}+\ldots+0+ \frac{6}{36}+\ldots + 0 \\
             &=\frac{490}{36} \\
             &=13.61111
\end{align*}$$
Por tanto se tendrá que el valor esperado de $XY$ es de
$13.61111$ (Es anotar que solo las esperanzas simples de $X$ y $Y$
tienen interpretación en el contexto de los datos).
</li>
</ol>
</main>
<button id="Show6" class="btn btn-secondary">
Mostrar Ejercicio Caso Continuo
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejercicio Caso Continuo
</button>
<main id="botoncito6">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga que se tiene interés en observar el número promedio de horas de
tiempo libre que posee un profesor en un día y el número promedio de
horas de tiempo libre que poseen los estudiantes a los cuales se les
dicta un curso de Estadística I. Para ello, se encuentra que la función
de densidad de probabilidad conjunta está dada por $$\begin{align*}
f(x,y)=\frac{1}{42}xy^2 \quad \quad 0<x<2; 1<y<4
\end{align*}$$
siendo $X$ la variable aleatoria que representa el
número promedio de horas de tiempo libre del profesor y $Y$ el número
promedio de horas de tiempo libre de los estudiantes. Entonces, si las
distribuciones marginales de $X$ está dada por $$\begin{align*}
g(x) =& \frac{1}{2}x \quad \quad 0<x<2
\end{align*}$$
y la distribución marginal de $Y$ está dada por
$$\begin{align*}
h(y) =& \frac{1}{21}y^2 \quad \quad 1<y<4
\end{align*}$$
Calcule
</p>
<ol>
<li>
$\mathbb{E}(X)$
</li>
<li>
$\mathbb{E}(Y)$
</li>
<li>
$\mathbb{E}(XY)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Dado que estamos interesados en calcular $\mathbb{E}(X)$, la cual solo
depende de la variable aleatoria $X$, entonces podemos emplear la
distribución marginal $g(x)$ para realizar el cálculo, tal que
$$\begin{align*}
\mathbb{E}(X)&=\int_{-\infty}^{\infty}x\,g(x) dx\\
             &=\int_{0}^{2}x\left(\frac{1}{2}x\right) dx \\
             &=\frac{1}{2}\int_{0}^{2}x^2 dx \\
             &=\frac{1}{2}\left(\frac{x^3}{3}\right)\Bigg|_0^2 \\
             &=\frac{1}{2}\left(\frac{2^3}{3} - \frac{0^3}{3}\right) \\
             &=\frac{1}{2}\left(\frac{8}{3} - \frac{0}{3}\right) \\
             &=\frac{1}{2}\left(\frac{8}{3}\right) \\
             &=\frac{4}{3} \\
             &=1.333333 
\end{align*}$$
Por tanto se tendrá que el valor esperado para el número
de horas promedio de tiempo libre que tiene el profesor de Estadística I
en un día es de $1.3333$ horas.
</li>
<li>
Similar al cálculo de la esperanza de $X$, se realiza el cálculo de la
$\mathbb{E}(Y)$, la cual, al depender solo de la variable aleatoria
$Y$, permite que el cálculo se realice mediante el empleo de la
distribución marginal $h(y)$, tal que $$\begin{align*}
\mathbb{E}(Y)&=\int_{-\infty}^{\infty}y\,h(y) dy\\
             &=\int_{1}^{4}y\left(\frac{1}{21}y^2\right) dy \\
             &=\frac{1}{21}\int_{1}^{4}y^3 dy \\
             &=\frac{1}{21}\left(\frac{y^4}{4}\right)\Bigg|_{1}^{4}\\
             &=\frac{1}{21}\left(\frac{4^4}{4} - \frac{1^4}{4}\right) \\
             &=\frac{1}{21}\left(\frac{256}{4} - \frac{1}{4}\right) \\
             &=\frac{85}{28} \\
             &=3.035714 
\end{align*}$$
Por tanto se tendrá que el valor esperado para el número
promedio de horas de tiempo libre que tienen los estudiantes que cursan
Estadística I es de $3.035714$ horas
</li>
<li>
En este punto, estamos interesados en calcular la esperanza conjunta de
$XY$, esto es, $\mathbb{E}(XY)$, en donde, se observa que la
esperanza matemática depende de dos variables aleatorias, y por tanto
para resolver el ejercicio empleamos la función de distribución conjunta
$f(x,y)$ tal que $$\begin{align*}
\mathbb{E}(XY)&=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy\,f(x,y) dy\\
             &=\int_{1}^{4}\int_{0}^{2}xy\left(\frac{1}{42}xy^2\right) dxdy \\
             &=\frac{1}{42}\int_{1}^{4}\int_{0}^{2} x^2y^3 dxdy \\
             &=\frac{1}{42}\int_{1}^{4} \left(\frac{x^3}{3}\right)y^3 dy\Bigg|_{0}^{2} \\
             &=\frac{1}{42}\int_{1}^{4} \left(\frac{2^3}{3} - \frac{0^3}{3}\right)y^3 dy \\
             &=\frac{1}{42}\int_{1}^{4} \left(\frac{8}{3}\right)y^3 dy \\
             &=\frac{4}{63}\int_{1}^{4} y^3 dy \\
             &=\frac{4}{63}\left(\frac{y^4}{4}\right)\Bigg|_{1}^{4} \\
             &=\frac{4}{63}\left(\frac{4^4}{4} - \frac{1^4}{4}\right) \\
             &=\frac{4}{63}\left(\frac{256}{4} - \frac{1}{4}\right) \\
             &=\frac{4}{63}\left(\frac{255}{4}\right) \\
             &=\frac{255}{63} \\
             &=4.047619
\end{align*}$$
Por tanto se tendrá que el valor esperado de $XY$ es de
$4.047619$ (Es anotar que solo las esperanzas simples de $X$ y $Y$
tienen interpretación en el contexto de los datos).
</li>
</ol>
</main>