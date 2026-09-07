---
title: "Clase 13"
course: "estadistica-i"
order: 17
classType: "clase"
description: "Esperanza condicional Varianza. - Caso univariado - Caso multivariado"
math: true
bibliography: "../../referencias.bib"
---

Esperanza matemática condicional
--------------------------------

Sean $X,Y$ variables aleatorias con función de masa de probabilidad
conjunta dada por $p(x,y)$ o función de densidad de probabilidad
conjunta dada por $f(x,y)$, entonces la esperanza condicional de $Y$
dado $X$ se define como

$$\begin{align*}\mathbb{E}(Y|X)=\begin{cases} \sum_{y}yp(y|x) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty yf(y|x) dy & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


Analogamente, la esperanza condicional de $X$ dado $Y$ se define
como

$$\begin{align*}\mathbb{E}(X|Y)=\begin{cases} \sum_{x}xp(x|y) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty xf(x|y) dx & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


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
calcule la esperanza matemática de $X$ dado que $Y=3$
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Para poder encontrar la esperanza matemática de $X$ dado que $Y=3$,
es necesario usar la distribución condicional de $X$ dado $Y=3$, la
cual está dada por
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto; font-size:120%!important">
<tbody>
<tr>
<td style="text-align:center;">
<script type="math/tex">X</script>
</td>
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
<td style="text-align:center;">
<script type="math/tex">f(x|y=3)</script>
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
<script type="math/tex">\frac{2}{6}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{6}</script>
</td>
<td style="text-align:center;">
<script type="math/tex">0</script>
</td>
<td style="text-align:center;">
<script type="math/tex">\frac{2}{6}</script>
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
</tr>
</tbody>
</table>
<p>

Para ver el procedimiento de cómo llegar a la distribución condicional,
remitase al ejemplo discreto para
<a href="../../EstadisticaI/EstIClase10.html#distribuciones-condicionales" target="\_blank">Distribuciones
Condicionales</a>.<br> <br> Entonces, basados en la distribución
condicional de $X$ dado $Y=3$ se realiza el cálculo de la esperanza
matemática de $X$ dado que $Y=3$, tal que

$$\begin{align*}
\mathbb{E}(X|Y=3)&=\sum_{x=2}^{12}x\,f(x|y=3) \\
             &=(2)\,f(x=2|y=3)+\ldots+(12)\,f(x=12|y=3) \\
             &=2\left(0\right)+3\left(0\right)+4\left(0\right)+5\left(\frac{2}{6}\right)+\ldots + 12\left(0\right) \\
             &=0 + 0+ 0 + \frac{10}{6}+\ldots + 0 \\
             &=\frac{42}{6} \\
             &=7
\end{align*}$$
Por tanto se tendrá que, el resultado esperado para la
suma de los dos dados es igual a $7$, cuando se sabe que el valor
absoluto de la diferencia de los dos dados fue igual a $3$.
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
Calcule el valor esperado de $Y$, dado que $X$ es a
lo más $1.3$
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para poder encontrar la esperanza matemática de $Y$ dado que
$X\leq 1.3$, es necesario usar la distribución condicional de $Y$
dado que $X\leq 1.3$, la cual está dada por $$\begin{align*}
f(y|x\leq1.3) =& 0.0476y^2 \quad \quad 1<y<4
\end{align*}$$
Para ver el procedimiento de cómo llegar a la
distribución condicional, remitase al ejemplo continuo para
<a href="../../EstadisticaI/EstIClase10.html#distribuciones-condicionales" target="\_blank">Distribuciones
Condicionales</a>. <br> <br> Entonces, basados en la distribución
condicional de $Y$ dado $X\leq 1.3$ se realiza el cálculo de la
esperanza matemática de interés, tal que $$\begin{align*}
\mathbb{E}(Y|X\leq 1.3) &= \int_{1}^4 y f(y|x\leq1.3) dy \\
                        &= \int_{1}^4 y \left(0.0476y^2\right) dy\\
                        &= 0.0476 \int_{1}^4 y^3 dy \\
                        &= 0.0476 \left(\frac{y^4}{4}\right) \Bigg|_{1}^4 \\
                        &= 0.0476 \left(\frac{4^4}{4} - \frac{1^4}{4}\right) \\
                        &= 0.0476 \left(\frac{256}{4} - \frac{1}{4}\right) \\ 
                        &= 0.0476 \left(\frac{255}{5}\right) \\
                        &= 2.4276
\end{align*}$$

Por tanto, si se sabe que el número promedio de horas de tiempo libre
que poseen los estudiantes es a lo más de $1.3$, se tendrá que el
valor esperado del número de horas promedio de tiempo libre que tiene el
profesor será de $2.4276$.
</p>
</main>

Varianza
--------

### Caso univariado

Sea $X$ una variable aleatoria con función de masa de probabilidad
$p(x)$ o función de densidad de probabilidad $f(x)$, entonces si
$m(X) = (X - \mathbb{E}(X))^2$, se tendrá que la varianza de $X$ que
se denota $Var(X)$ o $\sigma^2$ estará dada por

$$\begin{align*}Var(X) &= \sigma^2 = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)^2\right] \\ Var(X) &= \begin{cases}\sum_x(x-\mathbb{E}(X))^2p(x) & \text{ si } X \text{ es discreta}  \\ \int_{-\infty}^\infty(x-\mathbb{E}(X))^2f(x)dx & \text{ si } X \text{ es continua} \end{cases}\end{align*}$$


Puede demostrarse a partir de la ecuación anterior, que existe una
alternativa más simple para el cálculo de la $Var(X)$, la cual está
dada por

$$\begin{align*}Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2\end{align*}$$


además, la raíz cuadrada de la varianza de $X$ se llama desviación
estándar de $X$, se denota por $Sd(X)$ o $\sigma$ y se define como

$$\begin{align*}Sd(X) = \sigma = \sqrt{Var(X)}\end{align*}$$


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
Calcule la desviación estándar del número de niñas que hay en una
familia que posee $3$ hijos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para realizar el cálculo de la desviación estándar del número de niñas
que hay en una familia que posee $3$ hijos, es necesario calcular
inicialmente su varianza, la cual estaría dada por $$\begin{align*}
Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align*}$$
En donde se observa que ésta depende tanto de la
$\mathbb{E}(X)$ como de $\mathbb{E}(X^2)$.<br> <br> Entonces, de los
resultados obtenidos en el ejemplo discreto del caso univariado para la
<a href="../../EstadisticaI/EstIClase11.html#caso-univariado" target="\_blank">Esperanza
Matemática</a> y para sus
<a href="../../EstadisticaI/EstIClase11.html#propiedades-de-la-esperanza-matemática" target="\_blank">Propiedades</a>,
se encontró que $\mathbb{E}(X)=1.5$ y $\mathbb{E}(X^2)=3$, y en
consecuencia, se tendrá que la varianza del número de niñas que hay en
una familia de $3$ hijos es de

$$\begin{align*}
Var(X) &= 3 - (1.5)^2 \\
       &= 0.75
\end{align*}$$

mientras que, la desviación estándar será igual a

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.75} \\
      &= 0.866
\end{align*}$$

y por tanto, se tendrá que el número promedio de niñas que se espera
encontrar en una familia que posee $3$ hijos es de $1.5$ niñas, con
una desviación estándar de $0.866$ niñas.
</p>
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
Calcule la desviación estándar del tiempo que tarda la serie financiera
en cumplir un ciclo.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Basados en la función de densidad de probabilidad anterior, y en el
interés de calcular la desviación estándar del tiempo que tarda la serie
financiera en cumplir un ciclo, se procede a realizar el cálculo de la
varianza, en donde mediante la definición $$\begin{align*}
Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align*}$$
Se tiene que, debemos calcular inicialmente los valores
de la $\mathbb{E}(X)$ y la esperanza de $\mathbb{E}(X^2)$.<br> <br>
En donde se observa que ésta depende tanto de la $\mathbb{E}(X)$ como
de $\mathbb{E}(X^2)$. Entonces, de los resultados obtenidos en el
ejemplo continuo del caso univariado para la
<a href="../../EstadisticaI/EstIClase11.html#caso-univariado" target="\_blank">Esperanza
Matemática</a> y para sus
<a href="../../EstadisticaI/EstIClase11.html#propiedades-de-la-esperanza-matemática" target="\_blank">Propiedades</a>,
se encontró que $\mathbb{E}(X)=0.5$ y
$\mathbb{E}(X^2)=0.2857142857$, y en consecuencia, se tendrá que la
varianza el tiempo que tarda la serie financiera en cumplir un ciclo es
de

$$\begin{align*}
Var(X) &= 0.2857142857 - (0.5)^2 \\
       &= 0.03571429
\end{align*}$$

mientras que, la desviación estándar será igual a

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.03571429} \\
      &=0.1889822
\end{align*}$$

Y por tanto, se tendrá que el tiempo esperado que tarda una serie
financiera en cumplir un ciclo será $0.5$ horas con desviación
estándar de $0.1889822$ horas, la cual al pasarla a minutos mediante
la regla de tres

$$\begin{align*}
1_\text{hora}  &- 60_\text{min}\\0.1889822_\text{horas} &- a
\end{align*}$$

se tendrá que $$\begin{align*}
a= \frac{0.1889822_\text{horas}\times 60_\text{min}}{1_\text{hora}} = 11.33893_\text{min}
\end{align*}$$

es decir, que el tiempo esperado que tarda una serie financiera en
cumplir un ciclo será de $30$ minutos con una desviación estándar de
$11.33893$ minutos.
</p>
</main>

### Caso multivariado

Sean $X,Y$ variables aleatorias con función de masa de probabilidad
conjunta o función de densidad de probabilidad conjunta, con
distribuciones marginales $g(x)$ y $h(y)$, entonces si
$m(X) = (X - \mathbb{E}(X))^2$ se tendrá que la varianza de $X$ que
se denota $Var(X)$ o $\sigma_x^2$ estará dada por

$$\begin{align*}Var(X) &= \sigma_x^2 = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)^2\right] \\ Var(X) &= \begin{cases}\sum_x(x-\mathbb{E}(X))^2g(x) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty(x-\mathbb{E}(X))^2g(x)dx & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


mientras que si $m(Y) = (Y - \mathbb{E}(Y))^2$ se tendrá que la
varianza de $Y$ que se denota $Var(Y)$ o $\sigma_y^2$ estará dada
por

$$\begin{align*}Var(Y) &= \sigma_y^2= \mathbb{E}\left[\left(Y-\mathbb{E}(Y)\right)^2\right] \\ Var(Y) &= \begin{cases}\sum_y(y-\mathbb{E}(Y))^2h(y) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty(y-\mathbb{E}(Y))^2h(y)dy & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


Es de anotar que, la varianza de $X$ también puede ser calculada
mediante la ecuación

$$\begin{align*}Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2\end{align*}$$


mientras que, la varianza de $Y$ pueden calcularse mediante la
ecuación

$$\begin{align*}Var(Y) = \mathbb{E}(Y^2) - \mathbb{E}(Y)^2\end{align*}$$


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
$Sd(X)$
</li>
<li>
$Sd(Y)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

Dado que estamos interesados en calcular la desviación estándar de la
suma resultante de los dos dados, necesitamos primero calcular el valor
de la varianza, la cual se calcularía por facilidad mediante la ecuación
$$\begin{align*}
Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align*}$$

En donde, el valor de la $\mathbb{E}(X)$ se calculó en el ejemplo
discreto de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, y se encontró que
$\mathbb{E}(X) = 7$. Por tanto nos faltaría realizar el cálculo de
$\mathbb{E}(X^2)$, la cual al depender solamente de la variable
aleatoria $X$, entonces se procede al cálculo mediante la distribución
marginal $g(x)$, tal que

$$\begin{align*}
\mathbb{E}(X^2)&=\sum_{x=2}^{12}x^2\,g(x) \\
             &=(2)^2\,g(2)+(3)^2\,g(3)+(4)^2\,g(4)+\ldots+(12)^2\,g(12) \\
             &=4\left(\frac{1}{36}\right)+9\left(\frac{2}{36}\right)+16\left(\frac{3}{36}\right)+\ldots + 144\left(\frac{1}{36}\right) \\
             &=\frac{4}{36}+\frac{18}{36}+\frac{48}{36}+\ldots + \frac{1}{36} \\
             &=\frac{1974}{36} \\
             &=54.833333
\end{align*}$$

Ahora, empleando este valor, procedemos al cálculo de la varianza de la
suma resultante de los dos dados, tal que $$\begin{align*}
Var(X) &= 54.833333 - 7^2\\
       &= 54.833333 - 49\\
       &= 5.833333
\end{align*}$$

y en consecuencia se tendrá que la desviación estándar estará dada por
$$\begin{align*}
Sd(X) &= \sqrt{Var(X)}\\
      &= \sqrt{5.833333}\\
      &= 2.415229
\end{align*}$$
es decir que, el valor promedio que se espera para la
suma resultante de los dos dados es de $7$, con una desviación
estándar de $2.415229$.
</li>
<li>

Similar al procedimiento anterior, se realiza el cálculo de la varianza
para el valor absoluto de la diferencia de los dos dados, mediante la
ecuación $$\begin{align*}
Var(Y) = \mathbb{E}(Y^2) - \mathbb{E}(Y)^2
\end{align*}$$

En donde, el valor de la $\mathbb{E}(Y)$ se calculó en el ejemplo
discreto de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, y se encontró que
$\mathbb{E}(Y) = 1.9444$. Ahora, dado que no poseemos el valor para
$\mathbb{E}(Y^2)$, procedemos a realizar su cálculo, en donde, al
depender el valor esperado de interés solo de la variable aleatoria
$Y$, entonces realizamos el cálculo mediante la distribución marginal
$h(y)$, tal que $$\begin{align*}
\mathbb{E}(Y^2)&=\sum_{y=0}^{5}y^2\,h(y) \\
             &=(0)^2\,h(0)+(1)^2\,h(1)+(2)^2\,h(2)+\ldots+(5)^2\,h(5) \\
             &=0\left(\frac{6}{36}\right)+1\left(\frac{10}{36}\right)+4\left(\frac{8}{36}\right)+\ldots + 25\left(\frac{2}{36}\right) \\
             &=0+\frac{10}{36}+\frac{32}{36}+\ldots + \frac{50}{36} \\
             &=\frac{210}{36} \\
             &=5.833333
\end{align*}$$
Ahora, empleando este valor, procedemos al cálculo de la
varianza del valor absoluto de la diferencia de los dos dado, tal que
$$\begin{align*}
Var(Y) &= 5.833333 - (1.9444)^2\\
       &= 5.833333 - 3.780691\\
       &= 2.052642
\end{align*}$$

y en consecuencia se tendrá que la desviación estándar estará dada por
$$\begin{align*}
Sd(Y) &= \sqrt{Var(Y)}\\
      &= \sqrt{2.052642}\\
      &= 1.432704
\end{align*}$$

Por tanto se tendrá que el valor esperado para el valor absoluto de la
diferencia de los dos dados es de $1.9444$, con una desviación
estándar de $1.432704$.
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
$Sd(X)$
</li>
<li>
$Sd(Y)$
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En este caso estamos interesados en realizar el cálculo de la desviación
estándar del número promedio de horas de tiempo libre del profesor, y
para ello necesitamos calcular el valor de la varianza, la cual estará
dada por $$\begin{align*}
Var(X) =& \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align*}$$
En donde, el valor de la $\mathbb{E}(X)$ se calculó en
el ejemplo continuo de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, y se encontró que
$\mathbb{E}(X) = 1.333333$, pero no se realizó el cálculo del valor de
$\mathbb{E}(X^2)$. <br> <br> Así que se procede al cálculo de
$\mathbb{E}(X^2)$, en donde, al depender solo de la variable aleatoria
$X$, se emplea para su cálculo la distribución marginal $g(x)$, tal
que $$\begin{align*}
\mathbb{E}(X^2)&=\int_{-\infty}^{\infty}x^2\,g(x) dx\\
               &=\int_{0}^{2}x^2\left(\frac{1}{2}x\right) dx \\
               &=\frac{1}{2}\int_{0}^{2}x^3 dx \\
               &=\frac{1}{2}\left(\frac{x^4}{4}\right)\Bigg|_0^2 \\
               &=\frac{1}{2}\left(\frac{2^4}{4} - \frac{0^4}{4}\right) \\
               &=\frac{1}{2}\left(\frac{16}{4} - \frac{0}{4}\right) \\
               &=\frac{1}{2}\left(4\right) \\
               &=\frac{4}{2} \\
               &=2 
\end{align*}$$

Ahora, al emplear este valor, procedemos al cálculo de la varianza del
número promedio de horas de tiempo libre del profesor, tal que
$$\begin{align*}
Var(Y) &= 2 - (1.333333)^2\\
       &= 2 - 1.777777\\
       &= 0.222223
\end{align*}$$

y en consecuencia se tendrá que la desviación estándar estará dada por
$$\begin{align*}
Sd(X) &= \sqrt{Var(X)}\\
      &= \sqrt{0.222223}\\
      &= 0.4714053
\end{align*}$$

Por tanto se tendrá que el valor esperado para el número de horas
promedio de tiempo libre que tiene el profesor de Estadística I en un
día es de $1.3333$ horas, con una desviación estándar de $0.4714053$
horas.
</li>
<li>

Similar al procedimiento anterior, se realiza el cálculo de la varianza
para el número promedio de horas de tiempo libre de los estudiantes,
mediante la ecuación $$\begin{align*}
Var(Y) = \mathbb{E}(Y^2) - \mathbb{E}(Y)^2
\end{align*}$$

En donde, el valor de la $\mathbb{E}(Y)$ se calculó en el ejemplo
continuo de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, y se encontró que
$\mathbb{E}(Y) = 3.035714$. Ahora, dado que no poseemos el valor para
$\mathbb{E}(Y^2)$, procedemos a realizar su cálculo, en donde, al
depender el valor esperado de interés solo de la variable aleatoria
$Y$, empleamos para su cálculo la distribución marginal $h(y)$, tal
que $$\begin{align*}
\mathbb{E}(Y^2)&=\int_{-\infty}^{\infty}y^2\,h(y) dy\\
               &=\int_{1}^{4}y^2\left(\frac{1}{21}y^2\right) dy \\
               &=\frac{1}{21}\int_{1}^{4}y^4 dy \\
               &=\frac{1}{21}\left(\frac{y^5}{5}\right)\Bigg|_{1}^{4}\\
               &=\frac{1}{21}\left(\frac{4^5}{5} - \frac{1^5}{5}\right) \\
               &=\frac{1}{21}\left(\frac{1024}{5} - \frac{1}{5}\right) \\
               &=\frac{341}{35} \\
               &=9.742857 
\end{align*}$$
Ahora, empleando este valor, procedemos al cálculo de la
varianza del número promedio de horas de tiempo libre de los
estudiantes, tal que $$\begin{align*}
Var(Y) &= 9.742857 - (3.035714)^2\\
       &= 9.742857 - 9.215559\\
       &= 0.5272975
\end{align*}$$

y en consecuencia se tendrá que la desviación estándar estará dada por
$$\begin{align*}
Sd(Y) &= \sqrt{Var(Y)}\\
      &= \sqrt{0.5272975}\\
      &= 0.7261525
\end{align*}$$

Por tanto se tendrá que el valor esperado para el número promedio de
horas de tiempo libre que tienen los estudiantes que cursan Estadística
I es de $3.035714$ horas, con una desviación estándar de $0.7261525$
horas.
</li>
</ol>
</main>