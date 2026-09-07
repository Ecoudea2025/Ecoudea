---
title: "Clase 14"
course: "estadistica-i"
order: 18
classType: "clase"
description: "Covarianza. Correlación. Independencia. Propiedades de la varianza y la covarianza. Teorema de Chebyshev"
math: true
bibliography: "../../referencias.bib"
---

## Covarianza

Sean $X,Y$ variables aleatorias con función de masa de probabilidad
conjunta dada por $p(x,y)$ o función de densidad de probabilidad
conjunta dada por $f(x,y)$, entonces la covarianza de $X$ y $Y$,
denotada por $Cov(X,Y)$ o $\sigma_{xy}$ está dada por

$$\begin{align*}Cov(X,Y) &= \sigma_{xy} = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)\left(Y-\mathbb{E}(Y)\right)\right] \\ Cov(X,Y) &=  \begin{cases}\sum_x\sum_y(x-\mathbb{E}(X))(y-\mathbb{E}(Y))p(x,y) & \text{ si } X,Y \text{ son discretas}  \\ \int_{-\infty}^\infty \int_{-\infty}^\infty (x-\mathbb{E}(X))(y-\mathbb{E}(Y))f(x,y)dxdy & \text{ si } X,Y \text{ son continuas} \end{cases}\end{align*}$$


Puede demostrarse a partir de la ecuación anterior, que existe una
alternativa más simple para el cálculo de la $Cov(X,Y)$, la cual está
dada por

$$\begin{align*}Cov(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)\end{align*}$$


### Nota

La covarianza entre dos variables aleatorias $X,Y$ es una medida de
asociación entre ambas, que describe la relación lineal entre las dos
variables aleatorias. El signo de la $Cov(X,Y)$ indicará el tipo de
dependencia lineal que hay entre las variables.

-   $Cov(X,Y) > 0$ indica que hay dependencia lineal positiva entre
    las variables, es decir, cuando aumenta una variable, la otra
    también aumenta.
-   $Cov(X,Y) < 0$ indica que hay dependencia lineal negativa entre
    las variables, es decir, cuando aumenta una variable, la otra
    disminuye.
-   $Cov(X,Y) \approx 0$ indica que no existencia dependencia lineal
    entre las dos variables.

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
calcule la covarianza entre la suma resultante de los dos dados y el
valor absoluto de la diferencia de los dos dados.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en calcular la covarianza entre las
variables $X$ y $Y$, la cual podemos calcular mediante la ecuación
$$\begin{align*}
Cov(X,Y) = \mathbb{E}(XY) -  \mathbb{E}(X)\mathbb{E}(Y)
\end{align*}$$

Al emplear los valores ya calculados en el ejemplo discreto de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, se tiene que
$\mathbb{E}(X)=7$, $\mathbb{E}(Y)=1.9444$ y
$\mathbb{E}(XY)=13.61111$, y por tanto se tendrá que $$\begin{align*}
Cov(X,Y) &= 13.61111 -  (7)(1.9444) \\
         &= 0.00031
\end{align*}$$

Por tanto se tendrá que la covarianza entre la suma resultante y el
valor absoluto de la diferencia de los dos dados es de $0.00031$, lo
cual, al observar el signo resultante, se tendrá que hay una dependencia
lineal positiva entre las variables. <br> <br> Es de anotar, que al
tener una covarianza con un valor tan cercano a $0$, no posible
afirmar si la dependencia lineal es o no es significativa, y por ello
será necesario realizar el cálculo de la correlación.
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
Calcule la covarianza entre el número promedio de horas
de tiempo libre del profesor, y de los estudiantes del curso de
Estadística I.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en realizar el cálculo de la covarianza
entre la variable $X$ la cual hace referencia al número de horas
promedio de tiempo libre del profesor, y la variable $Y$ la cual hace
referencia al número de horas promedio de tiempo libre de los
estudiantes. Esta covarianza puede ser calculada de forma simple por la
ecuación $$\begin{align*}
Cov(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)
\end{align*}$$
En donde, el valor para las esperanzas requeridas para el
cálculo de la covarianza, fueron calculados previamente en el ejemplo
continuo de la
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Esperanza
Matemática</a> para el caso multivariado, siendo los valores calculados
iguales a $\mathbb{E}(X)=4/3 =1.333333$,
$\mathbb{E}(Y)=85/28=3.035714$ y
$\mathbb{E}(XY)=255/63 = 4.047619$.<br> <br> Al reemplazar estos
valores en la función de covarianza tendremos que $$\begin{align*}
Cov(X,Y) &= \frac{255}{63} - \left(\frac{4}{3}\right)\left(\frac{85}{28}\right)\\
         &= 0
\end{align*}$$

Por tanto como el valor obtenido es igual a cero, se concluirá que no
existe una dependencia lineal entre el número promedio de horas de
tiempo libre del profesor, y el número promedio de horas de tiempo libre
de los estudiantes del curso de Estadística I.
</p>
</main>

## Correlación

Sean $X,Y$ variables aleatorias con covarianza $Cov(X,Y)$, y
desviaciones estándar $Sd(X)$ y $Sd(Y)$, entonces la correlación de
$X$ y $Y$, denotada por $Cor(X,Y)$ o $\rho_{xy}$ está dada por

$$\begin{align*}Cor(X,Y) = \rho_{xy} = \frac{Cov(X,Y)}{Sd(X)Sd(Y)}\end{align*}$$


### Nota

La correlación entre dos variables aleatorias $X,Y$ es una medida de
asociación entre ambas, que describe la fuerza de la relación lineal
entre las dos variables aleatorias. El valor de $\rho_{xy}$ indica el
tipo y fuerza de la dependencia lineal que hay entre las variables

-   $\rho_{xy} = 1$ indica que existe dependencia lineal positiva
    exacta entre las variables, es decir, cuando aumenta una variable,
    la otra aumenta proporcionalmente en la misma cantidad. Este aumento
    es de la forma $Y = a + bX$, siendo $a$ y $b$ dos constantes,
    con $b>0$.
-   $\rho_{xy} = -1$ indica que existe dependencia lineal negativa
    exacta entre las variables, es decir, cuando aumenta una variable,
    la otra disminuye proporcionalmente en la misma cantidad. Este
    aumento es de la forma $Y = a + bX$ con $a$ y $b$ dos
    constantes, y $b<0$.
-   $\rho_{xy} = 0$ No existe dependencia lineal entre las variables.

Además, se tendrá que si

-   $0.5 < \rho_{xy} \leq 1$ fuerte correlación positiva entre $X$ y
    $Y$.
-   $0.3 < \rho_{xy} \leq 0.5$ moderada correlación positiva entre
    $X$ y $Y$.
-   $0.1 < \rho_{xy} \leq 0.3$ débil correlación positiva entre $X$
    y $Y$.
-   $-0.1 \leq \rho_{xy} \leq 0.1$ débil o ninguna correlación entre
    $X$ y $Y$.
-   $-0.3 \leq \rho_{xy} < -0.1$ débil correlación negativa entre
    $X$ y $Y$.
-   $-0.5 \leq \rho_{xy} < -0.3$ moderada correlación negativa entre
    $X$ y $Y$.
-   $-1 \leq \rho_{xy} < -0.5$ fuerte correlación negativa entre $X$
    y $Y$.

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
calcule la correlación que hay entre la suma resultante de los dos dados
y el valor absoluto de la diferencia de los dos dados, y determine la
fuerza de la dependencia lineal de las variables.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este ejercicio debemos calcular la correlación entre las variables
$X$ y $Y$, y para ello podemos emplear la ecuación de correlación,
dada por $$\begin{align*}
Cor(X,Y) = \frac{Cov(X,Y)}{Sd(X)Sd(Y)}
\end{align*}$$

Entonces, para realizar el cálculo podemos emplear los valores de las
desviaciones estándar calculadas en los ejemplos discretos para el caso
multivariado de la
<a href="../../EstadisticaI/EstIClase12.html#caso-multivariado" target="\_blank">Varianza</a>
y el valor obtenido para la
<a href="../../EstadisticaI/EstIClase13.html#covarianza" target="\_blank">Covarianza</a>,
tal que, $Sd(X)=2.415229$, $Sd(Y)=1.432704$ y $Cov(X,Y)=−0.5552$,
y por tanto, al reemplazar en la formula de correlación, tendremos que
$$\begin{align*}
Cor(X,Y) &= \frac{0.00031}{(2.415229)(1.432704)} \\
         &= 0.00008958739
\end{align*}$$

Por tanto se tendrá que la correlación entre la suma resultante y el
valor absoluto de la diferencia de los dos dados es de
$0.008958739\%$, lo cual quiere decir, que existe una dependencia
lineal positiva débil o nula entre las variables de interés, debido a
que el valor está muy cercano a $0$.
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
Calcule la correlación entre el número promedio de horas
de tiempo libre del profesor, y de los estudiantes del curso de
Estadística I.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en realizar el cálculo de la
correlación entre el número de horas promedio de tiempo libre del
profesor, y el número de horas promedio de tiempo libre de los
estudiantes, es decir $$\begin{align*}
Cor(X,Y) = \frac{Cov(X,Y)}{Sd(X)Sd(Y)}
\end{align*}$$

Entonces, para realizar el cálculo empleamos los valores calculados
previamente para las desviaciones estándar, las cuales fueron calculadas
en los ejemplos continuos para el caso multivariado de la
<a href="../../EstadisticaI/EstIClase12.html#caso-multivariado" target="\_blank">Varianza</a>
y el valor obtenido para la
<a href="../../EstadisticaI/EstIClase13.html#covarianza" target="\_blank">Covarianza</a>,
tal que, $Sd(X)=0.4714053$, $Sd(Y)=0.7261525$ y $Cov(X,Y)=0$, y
por tanto, al reemplazar en la formula de correlación, tendremos que
$$\begin{align*}
Cor(X,Y) &= \frac{0}{(0.4714053)(0.7261525)} \\
         &= 0
\end{align*}$$

Por tanto como la correlación es igual a cero, se concluye que no existe
una dependencia lineal entre el número promedio de horas de tiempo libre
del profesor, y el número promedio de horas de tiempo libre de los
estudiantes del curso de Estadística I.
</p>
</main>

## Independencia

Si las variables aleatorias $X, Y$ son independientes, entonces se
debe cumplir que

$$\begin{align*}\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)\end{align*}$$


y por tanto se tendrá que 
$$\begin{align*}Cov(X,Y) = 0\end{align*}$$


**Nota:** La situación opuesta, sin embargo, no se cumple por lo
general, es decir, existen situaciones en las cuales las variables
aleatorias tienen covarianza cero pese a que no son independientes.

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
Entonces, basados en la función de masa de probabilidad conjunta,
compruebe si la suma resultante de los dos dados y el valor absoluto de
la diferencia de los dos dados, son o no independientes.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para probar si las variables $X$ y $Y$ son independientes, debemos
verificar si la multiplicación entre el valor esperado de la suma
resultante de los dos dados y el valor esperado del valor absoluto de la
diferencia de los dos dados, es igual a la esperanza conjunta de las dos
variables, tal que se pueda probar si $$\begin{align*}
\mathbb{E}(XY) = \mathbb{E}(X) \mathbb{E}(Y)
\end{align*}$$

Entonces, al emplear los
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Valores
Esperados</a> $\mathbb{E}(X)=7$, $\mathbb{E}(Y)=1.9444$ y
$\mathbb{E}(XY)=13.61111$, que fueron calculados en el ejemplo
discreto para el caso multivariado, se tendrá que $$\begin{align*}
\mathbb{E}(XY) &= \mathbb{E}(X) \mathbb{E}(Y) \\
13.61111 &= (7)(1.9444) \\
13.61111 &\neq 13.6108
\end{align*}$$
En consecuencia, dado que la igualdad no se cumple, se
concluye que la variable de la suma resultante de los dos dados es
dependiente de la variable del valor absoluto de la diferencia de los
dos dados.
</p>
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
Pruebe si el número promedio de horas de tiempo libre que
tiene el profesor son independientes del número promedio de horas de
tiempo libre que tienen los estudiantes del curso de Estadística I.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Para probar si el número promedio de horas de tiempo libre que tiene el
profesor son independientes del número promedio de horas de tiempo libre
que tienen los estudiantes del curso de Estadística I, debemos verificar
si la multiplicación entre el valor esperado de la suma resultante de
los dos dados y el valor esperado del valor absoluto de la diferencia de
los dos dados, es igual a la esperanza conjunta de las dos variables,
tal que se pueda probar si $$\begin{align*}
\mathbb{E}(XY) = \mathbb{E}(X) \mathbb{E}(Y)
\end{align*}$$
Basados en los
<a href="../../EstadisticaI/EstIClase11.html#caso-multivariado" target="\_blank">Valores
Esperados</a> calculados en el ejemplo continuo para el caso
multivariado, tenemos que $\mathbb{E}(X)=4/3$, $\mathbb{E}(Y)=85/28$
y $\mathbb{E}(XY)=255/63$. Entonces, al reemplazar en la ecuación
anterior, tenemos que $$\begin{align*}
\mathbb{E}(XY) &= \mathbb{E}(X) \mathbb{E}(Y) \\
\frac{255}{63} &= \left(\frac{4}{3}\right)\left(\frac{85}{28}\right) \\
\frac{85}{21} &= \frac{85}{21}
\end{align*}$$
En consecuencia, dado que la igualdad se cumple, se
concluye que el número promedio de horas de tiempo libre que tiene el
profesor es independientes del número promedio de horas de tiempo libre
que tienen los estudiantes del curso de Estadística I.
</p>
</main>

## Propiedades de la varianza, covarianza y correlación

Sea $a$ y $b$ números reales (constantes) y $X$ y $Y$ dos
variables aleatorias discretas o continuas, entonces

1.  $Var(a)=0$

2.  $Var(aX)=a^2Var(X)$

3.  $Var(a+bX) = b^2Var(X)$

4.  $Var(X+Y) = Var(X) + Var(Y) + 2 Cov(X,Y)$

5.  $Var(X-Y) = Var(X) + Var(Y) - 2 Cov(X,Y)$

6.  Si $X, Y$ son independientes entonces
    $Var(X+Y) = Var(X) + Var(Y)$

7.  Si $X, Y$ son independientes entonces
    $Var(X-Y) = Var(X) + Var(Y)$

8.  $Cov(aX,bY) = abCov(X,Y)$

9.  Si $X, Y$ son linealmente independientes entonces
    $Cov(aX,bY) = 0$

10. $Cor(aX,bY) = Cor(X,Y)$

11. Si $X, Y$ son linealmente independientes entonces
    $Cor(aX,bY) = 0$

## Desigualdad de Chebyshev

### Desigualdad de Markov

Sea $q(x)$ una función no negativa de la variable aleatoria $X$.
Entonces, si $\mathbb{E}(q(x))$ existe, se tendrá que para todo
$\tau>0$

$$\begin{align*}\mathbb{P}(q(x)\geq \tau)\leq \frac{\mathbb{E}(q(X))}{\tau}\end{align*}$$


### Desigualdad de Chebyshev

Sea $X$ una variable aleatoria que tiene una distribución de
probabilidad para la cual solo se supone que existe la varianza
$\sigma^2$. Entonces, si $\tau = k^2$ y $q(x)=(x-\mu)^2/\sigma^2$,
donde $\mu=\mathbb{E}(X)$ y $\sigma^2=Var(X)$, se tendrá que

$$\begin{align*}\mathbb{P}\left(\frac{(x-\mu)^2}{\sigma^2}\geq k^2\right) \leq \frac{1}{k^2}\mathbb{E}\left(\frac{(x-\mu)^2}{\sigma^2}\right)\end{align*}$$


en donde, puede demostrarse que la expresión anterior es igual a

$$\begin{align*}\mathbb{P}\left(\mu - k\sigma \leq x \leq \mu + k\sigma \right) \geq 1 - \frac{1}{k^2}\end{align*}$$


siendo $k$ cualquier número positivo, tal que $k>1$.

<button id="Show7" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide7" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
</button>
<main id="botoncito7">
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

<p>
Entonces, basados en la función de masa de probabilidad, calcule la
probabilidad de que el número de niñas que hay en una familia de $3$
hijos difiera de su media en más de $1.1258$, mediante
</p>
<ol>
<li>
El empleo de la función de probabilidad.
</li>
<li>
El empleo del teorema de Chevyshev.
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En este caso, nos piden calcular la siguiente probabilidad
$$\begin{align*}
\mathbb{P}(|X-\mu|>1.1258)
\end{align*}$$
La cual, al desarrollarla nos lleva a la estructura
$$\begin{align*}
\mathbb{P}(|X-\mu|>1.1258) &= 1 - \mathbb{P}(|X-\mu|<1.1258)\\
                           &= 1 - \mathbb{P}(-1.1258 < X - \mu < 1.1258)\\
                           &= 1 - \mathbb{P}(\mu - 1.1258 < X < \mu + 1.1258)\\
\end{align*}$$

En donde, como $\mu=\mathbb{E}(X)=1.5$, siendo dicho valor calculado
previamente en el ejemplo discreto para la
<a href="../../EstadisticaI/EstIClase11.html#caso-univariado" target="\_blank">Esperanza
Matemática</a> del caso univariado, entonces tendremos que
$$\begin{align*}
\mathbb{P}(|X-\mu|>1.1258) &= 1 - \mathbb{P}(1.5 - 1.1258 < X < 1.5 + 1.1258)\\
                           &= 1 - \mathbb{P}(0.3742 < X < 2.6258)\\
                           &= 1 - \sum_{x=1}^2 p(x)\\
                           &= 1 - \left(p(1) + p(2) \right) \\
                           &= 1 - \left(\frac{3}{8} + \frac{3}{8}\right) \\
                           &= 1 - \frac{6}{8} \\
                           &= \frac{1}{4} \\
                           &= 0.25 \\
\end{align*}$$

Es decir, se tendrá una probabilidad del $25\%$, de que el número de
niñas que hay en una familia de $3$ hijos, difiera de su media en más
de $1.1258$.
</li>
<li>

Ahora, estamos interesados en realizar el cálculo mediante el teorema de
Chebyshev, y para ello, debemos llevar la probabilidad de interés a la
estructura $$\begin{align*}
\mathbb{P}\left(\mu - k\sigma \leq x \leq \mu + k\sigma \right)
\end{align*}$$
tal que $$\begin{align*}
\mathbb{P}(|X-\mu|>1.1258) &= 1 - \mathbb{P}(|X-\mu|<1.1258)\\
                           &= 1 - \mathbb{P}(-1.1258 < X - \mu < 1.1258)\\
                           &= 1 - \mathbb{P}(\mu - 1.1258 < X < \mu + 1.1258)
\end{align*}$$

De lo anterior se observa que el valor $1.1258=k\sigma$, y como la
desviación estándar de la distribución es igual a
$\sigma=Sd(X)=0.866$, siendo dicho valor calculado previamente en el
ejemplo discreto para la
<a href="../../EstadisticaI/EstIClase12.html#caso-univariado" target="\_blank">Varianza</a>
del caso univariado, tendremos que $$\begin{align*}
1.1258 &= k\sigma \\
1.1258 &= k(0.866) \\
\frac{1.1258}{0.866} &= k \\
k &= 1.3
\end{align*}$$
haciendo que la probabilidad anterior se transforme en
$$\begin{align*}
\mathbb{P}(|X-\mu|>1.1258) &= 1 - \mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) \\
\end{align*}$$
Lo cual nos daría la estructura del teorema de Chevyshev.
Ahora, al aplicar el teorema, reemplazando $k$ por $1.3$ tendremos
que $$\begin{align*}
\mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) &\geq 1 - \frac{1}{(1.3)^2} \\
\mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) &\geq 0.408284 \\
\end{align*}$$
Ahora, como estamos interesados es en calcular
$$\begin{align*}
1 - \mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma)
\end{align*}$$

se tendrá que $$\begin{align*}
\mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) &\geq 1 - \frac{1}{(1.3)^2} \\
1 - \mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) &\leq 1 - 0.408284 \\
1 - \mathbb{P}(\mu - 1.3\sigma < X < \mu + 1.3\sigma) &\leq 0.591716 \\
\mathbb{P}(|X-\mu|>1.1258) &\leq 0.591716
\end{align*}$$

Es decir, se tendrá que la probabilidad de que el número de niñas que
hay en una familia de $3$ hijos, difiera de su media en más de
$1.1258$, será como máximo del $59.17\%$, lo cual es consistente con
la probabilidad calculada de forma exacta, la cual es igual a $25\%$.
</li>
</ol>
</main>
<button id="Show8" class="btn btn-secondary">
Mostrar Ejercicio Caso Continuo
</button>
<button id="Hide8" class="btn btn-info">
Ocultar Ejercicio Caso Continuo
</button>
<main id="botoncito8">
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
Entonces, basados en la función de densidad de probabilidad, calcule la
probabilidad de que el tiempo en horas que tarda la serie financiera en
cumplir un ciclo se encuentre entre $0.0464$ y $0.9536$ horas,
mediante
</p>
<ol>
<li>
El empleo de la función de probabilidad.
</li>
<li>
El empleo del teorema de Chevyshev
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
En este caso nos piden la probabilidad de que, el tiempo en horas que
tarda una serie financiera en dar un ciclo se encuentre entre $0.0464$
y $0.9536$ horas, esto es $$\begin{align*}
\mathbb{P}(0.0464<X<0.9536)
\end{align*}$$
Entonces al emplear la función de densidad de
probabilidad tendremos que $$\begin{align*}
\mathbb{P}(0.0464<X<0.9536) &= \int_{0.0464}^{0.9536} f(x) dx\\
                            &= \int_{0.0464}^{0.9536} 30x^2(1-x)^2 dx\\
                            &= 30 \int_{0.0464}^{0.9536} x^2(1 - 2x + x^2) dx \\
                            &= 30 \int_{0.0464}^{0.9536} x^2 - 2x^3 + x^4 dx \\
                            &= 30 \left(\frac{x^3}{3} - \frac{2x^4}{4} + \frac{x^5}{5}\right) \Bigg|_{0.0464}^{0.9536} \\
                            &= 30 \Bigg[\left(\frac{0.9536^3}{3} - \frac{2(0.9536)^4}{4} + \frac{0.9536^5}{5}\right) \\
                            & \quad \; - \left(\frac{0.0464^3}{3} - \frac{2(0.0464)^4}{4} + \frac{(0.0464)^5}{5}\right)\Bigg] \\
                            &= 30 (0.03327128) \\
                            &= 0.9981385
\end{align*}$$
Es decir que, la probabilidad de que la serie financiera
tarde entre $0.0464$ y $0.9536$ horas, en dar un ciclo es del
$99.81\%$.
</li>
<li>

Ahora, estamos interesados en realizar el cálculo mediante el teorema de
Chebyshev, y para ello, debemos llevar la probabilidad de interés a la
estructura $$\begin{align*}
\mathbb{P}\left(\mu - k\sigma \leq x \leq \mu + k\sigma \right)
\end{align*}$$

en donde, en el ejemplo continuo para la
<a href="../../EstadisticaI/EstIClase11.html#caso-univariado" target="\_blank">Esperanza
Matemática</a> del caso univariado, se encontró que
$\mathbb{E}(X)=\mu=0.5$, mientras que, del ejemplo continuo para la
<a href="../../EstadisticaI/EstIClase12.html#caso-univariado" target="\_blank">Varianza</a>
del caso discreto, se encontró que $Sd(X)=\sigma= 0.1889822$. <br>
<br> Entonces al retomar la probabilidad de interés, tenemos que
$$\begin{align*}
\mathbb{P}(0.0464<X<0.9536)
\end{align*}$$

Siendo el límite inferior $0.0464=\mu - k\sigma$, mientras que, el
límite superior $0.9536=\mu + k\sigma$, los cuales, al reemplazar los
valores de $\mu$ y $\sigma$ por la media y la desviación estándar de
la distribución, tendremos que a través de las dos ecuaciones se llega a
que $$\begin{align*}
0.0464 &= \mu - k\sigma  & 0.9536 &= \mu + k\sigma\\
0.0464 &= 0.5 - k(0.1889822) & 0.9536 &= 0.5 + k(0.1889822) \\
0.0464 - 0.5 &= - k & 0.9536 - 0.5 &= k(0.1889822) \\
\frac{-0.4536}{0.1889822} &= - k & \frac{0.4536}{0.1889822} &= k\\
k &= 2.400226 & 2.400226 &= k
\end{align*}$$

lo cual, al reemplazarlo en probabilidad de interés, tendremos que
$$\begin{align*}
\mathbb{P}(0.0464<X<0.9536) = \mathbb{P}(0.5 - (2.400226)(0.1889822) < X < 0.5 + (2.400226)(0.1889822))
\end{align*}$$

Ahora, al aplicar el teorema de Chebyshev, se tiene que $$\begin{align*}
\mathbb{P}(\mu - 2.400226\sigma < X < \mu + 2.400226\sigma) &\geq 1 - \frac{1}{(2.400226)^2} \\
\mathbb{P}(0.0464<X<0.9536) &\geq 0.8264216
\end{align*}$$

Es decir que, la probabilidad de que la serie financiera tarde entre
$0.0464$ y $0.9536$ horas, en dar un ciclo es como mínimo del
$82.64\%$, lo cual es consistente con la probabilidad calculada de
forma exacta, la cual es igual a $99.81\%$.
</li>
</ol>
</main>