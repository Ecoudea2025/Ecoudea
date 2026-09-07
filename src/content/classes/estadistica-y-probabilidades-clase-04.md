---
title: "Clase 12"
course: "estadistica-y-probabilidades"
order: 17
classType: "clase"
description: "Distribuciones de probabilidad conjuntas - Distribuciones marginales - Distribuciones condicionales - Independencia estadística"
math: true
bibliography: "../../referencias.bib"
---

Distribución de probabilidad conjunta
-------------------------------------

### Distribuciones marginales

Sean `$X, Y$` dos variables aleatorias con función de masa de
probabilidad conjunta `$p(x,y)$`o función de densidad de probabilidad
conjunta `$f(x,y)$`, entonces las distribuciones marginales solo de
`$X$`, están dada por

$$\begin{align*}g(x)=\begin{cases} \sum_{y}p(x,y) & \text{ si } x,y \text{ son discretas} \\ \int_{-\infty}^\infty f(x,y) dy & \text{ si } x,y \text{ son continuas} \end{cases}\end{align*}$$


Similarmente, las distribuciones marginales solo de `$Y$`, están dadas
por

$$\begin{align*}h(y)=\begin{cases} \sum_{x}p(x,y) & \text{ si } x,y \text{ son discretas} \\ \int_{-\infty}^\infty f(x,y) dx & \text{ si } x,y \text{ son continuas} \end{cases}\end{align*}$$


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
dos dados. Encuentre la distribución marginal de $X$ y de $Y$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
En el caso de una distribución discreta, encontrar las distribuciones
marginales es cuestion de sumar las probabilidades que hay en la tabla
por filas o por columnas. Para ilustrar esto, retomemos la tabla de
distribución que encontramos anteriormente para este punto
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td rowspan="2" colspan="2" style="text-align:center; vertical-align: middle;">
<script type="math/tex">p(x,y)</script>
</td>
<td style="text-align:center;" colspan="11">
<script type="math/tex">X</script>
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
</tr>
</tbody>
</table>
<p>
Como se aprecia, se tiene en la parte izquierda la variable aleatoria
$Y$, mientras que en la parte superior la variable aleatoria $X$.
Entonces, si realizamos la suma de las probabilidades por columna,
encontraremos la distribución marginal de $X$, $g(x)$, mientras que
si sumamos las probabilidades por fila, encontraremos la distribución
marginal de $Y$, $h(y)$. tal que
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
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
</main>
<button id="Show6" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
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
\end{align*}$$ siendo $X$ la variable aleatoria que representa el
número promedio de horas de tiempo libre del profesor y $Y$ el número
promedio de horas de tiempo libre de los estudiantes. A partir de dicha
función encuentre la distribución marginal de $X$ y de $Y$
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para encontrar las distribuciones marginales en el caso de una
distribución continua, será necesario realizar una integración en el
dominio de la variable contraria a la cual se desea encontrar la
distribución marginal. Por ejemplo, si se desea encontrar la
distribución marginal de $X$, será necesario eliminar la variable
$Y$ de la ecuación, y por tanto será necesario realizar la integral
respecto a $Y$ en todo su dominio. Es decir <br>

$$\begin{align*}
g(x) =& \int_1^{4}\frac{1}{42}xy^2\text{ d}y \\ 
     =& \frac{1}{42}\int_{1}^{4}xy^2\text{ d}y \\
     =& \frac{1}{42}x\frac{y^3}{3}\Bigg|_{1}^{4} \\
     =& \frac{1}{126}x(4^3 - 1^3) \\
     =& \frac{1}{126}x(64 - 1) \\
g(x) =& \frac{1}{2}x \quad \quad 0<x<2
\end{align*}$$ Donde se observa que la distribución marginal $g(x)$
solo depende de la variable aleatoria $X$. Similarmente para la
distribución marginal de $Y$, en donde, será necesario eliminar la
variable aleatoria $X$ y por tanto, se realiza la integral en todo el
dominio de $X$, tal que

$$\begin{align*}
h(y) =& \int_0^{2}\frac{1}{42}xy^2\text{ d}x \\ 
     =& \frac{1}{42}\int_{0}^{2}xy^2\text{ d}x \\
     =& \frac{1}{42}\frac{x^2}{2}y^2\Bigg|_{0}^{2} \\
     =& \frac{1}{84}(2^2 - 0^2)y^2 \\
     =& \frac{1}{84}(4)y^2 \\
h(y) =& \frac{1}{21}y^2 \quad \quad 1<y<4
\end{align*}$$ Donde se evidencia que la distribución marginal $h(y)$
solo depende de la variable aleatoria $Y$.
</p>
</main>

### Distribuciones condicionales

Sea `$X, Y$` dos variables aleatorias con función de masa de
probabilidad conjunta o función de densidad de probabilidad conjunta
entonces la distribución condicional de `$X$` dado `$Y$` es

$$\begin{align*}f(x|y)=\frac{f(x,y)}{h(y)} \text{ con } h(y)>0\end{align*}$$


Análogamente, la distribución condicional de `$Y$` dado `$X$` es

$$\begin{align*}f(y|x)=\frac{f(x,y)}{g(x)} \text{ con } g(x)>0\end{align*}$$


<button id="Show4" class="btn btn-secondary">
Mostrar Ejercicio Caso Discreto
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejercicio Caso Discreto
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento que consta en lanzar dos dados al aire. Sea $X$
la variable aleatoria que indica la suma resultante de los dos dados, y
$Y$ la variable aleatoria del valor absoluto de la diferencia de los
dos dados. Encuentre la distribución condicional de $X$ dado que
$Y=3$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

El interés en este punto radica en calcular la distribución de la suma
de los dados, dado que se sabe que la resta absoluta es igual a $3$,
es decir, $$\begin{align*}
f(x|y=3)=\frac{f(x,y=3)}{h(y=3)} \text{ con } h(y)>0
\end{align*}$$

Para calcular dicha distribución, necesitamos tanto la función de masa
de probabilidad como las distribución marginal de $Y=3$, y para ello,
empleamos la tabla anteriormente calculada con sus correspondientes
distribuciones marginales, tal que
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
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
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">\frac{2}{36}</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">\frac{2}{36}</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">\frac{2}{36}</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #a97c22 !important;">
<script type="math/tex">\frac{6}{36}</script>
</span>
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
En donde se aprecia que $f(x,y=3)$ aparece resaltado de color rojo,
mientras que $h(y=3)$ aparece resaltado de color amarillo. Entonces al
aplicar la formula de probabilidad condicional, se tendrá que la
distribución condicional de $X$ dado que $Y=3$ es
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
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
<script type="math/tex">f(x,y=3)</script>
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
</main>
<button id="Show7" class="btn btn-secondary">
Mostrar Ejercicio Caso Continuo
</button>
<button id="Hide7" class="btn btn-info">
Ocultar Ejercicio Caso Continuo
</button>
<main id="botoncito7">
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
\end{align*}$$ siendo $X$ la variable aleatoria que representa el
número promedio de horas de tiempo libre del profesor y $Y$ el número
promedio de horas de tiempo libre de los estudiantes. A partir de dicha
función encuentre la distribución condicional de $Y$, dado que $X$
es a lo más $1.3$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este punto, el interés es encontrar la distribución condicional del
número promedio de horas de tiempo libre de los estudiantes, dado que el
número promedio de horas de tiempo libre que tiene el profesor es como
máximo $1.3$ horas. Por definición, esta distribución condicional
puede definirse como $$\begin{align*}
f(y|x\leq1.3) = \frac{f(x\leq1.3, y)}{g(x\leq1.3)} \text{ con } g(x)>0
\end{align*}$$

En donde, para encontrar esta distribución será necesario calcular
inicialmente $f(x\leq1.3, y)$ la cual es equivalente a la siguiente
integral

$$\begin{align*}
f(x\leq1.3, y) =& \int_{0}^{1.3} \frac{1}{42}xy^2 \text{ d}x \\
               =& \frac{1}{42}\int_{0}^{1.3}xy^2\text{ d}x \\
               =& \frac{1}{42}\frac{x^2}{2}y^2\Bigg|_{0}^{1.3} \\
               =& \frac{1}{84}(1.3^2 - 0^2)y^2 \\
               =& \frac{1}{84}(1.69)y^2 \\
               =& 0.0201y^2
\end{align*}$$

seguidamente, será necesario calcular $g(x\leq1.3$ mediante la
integral

$$\begin{align*}
g(x\leq1.3) =& \int_0^{1.3}\frac{1}{2}x \text{ d}x \\
            =& \frac{1}{2}\int_0^{1.3}x \text{ d}x \\
            =& \frac{1}{2}\frac{x^2}{2}\Bigg|_0^{1.3} \\
            =& \frac{1}{4}(1.3^2 - 0^2) \\
            =& \frac{1}{4}(1.69) \\
            =& 0.4225
\end{align*}$$

finalmente, al realizar la división entre las dos ecuaciones se tendrá
que la distribución condicional de $Y$ dado que $x\leq1.3$ estará
dada por

$$\begin{align*}
f(y|x\leq1.3) =& \frac{0.0201y^2}{0.4225} \\ 
              =& 0.0476y^2 \quad \quad 1<y<4
\end{align*}$$
</p>
</main>

### Independencia estadística

Sea `$X, Y$` dos variables aleatorias discretas con función de masa de
probabilidad conjunta `$p(x,y)$` o continuas con función de densidad de
probabilidad conjunta `$f(x,y)$`, y con distribuciones marginales
`$g(x)$` y `$h(y)$`. entonces, se dice que las variables aleatorias
`$X,Y$` son estadísticamente independientes si y solo si

$$\begin{align*}f(x,y)=g(x)h(y)\end{align*}$$


para todo `$(x,y)$` dentro de sus rangos o planos.

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
dos dados. Verifique si las variables aleatorias $X$ y $Y$ son
estadísticamente independientes.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Para observar si la suma de los dos dados y la resta absoluta del
resultado de los dos dados es o no independiente, es necesario calcular
inicialmente, las distribuciones marginales de las variables aleatorias
tal como se hizo en puntos anteriores
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
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

Una vez conocida la distribución de probabilidad conjunta y las
distribuciones marginales, es posible verificar si las variables
aleatorias son independientes mediante la formula

$$\begin{align*}
f(x,y)=g(x)h(y)
\end{align*}$$

Entonces si son independientes, al evaluar la función de distribución
conjunta y las marginales en cualquier punto debería surgir como
resultado el mismo valor a ambos lados de la desigualdad. Por ejemplo,
vamos a evaluar a $X=4$ y $Y=2$. En este caso se tendrá que

$$\begin{align*}
f(x=4,y=2)=\frac{2}{36}
\end{align*}$$

mientras que

$$\begin{align*}
g(x=4)=\frac{3}{36} \quad \text{ y } \quad h(y=2)=\frac{8}{36}
\end{align*}$$

Por tanto, al evaluar los dos lados de la desigualdad, se tendrá que

$$\begin{align*}
f(x=4,y=2) &= g(x=4)h(y=2) \\
\frac{2}{36} &= \frac{3}{36} \frac{8}{36} \\
\frac{1}{18} &\neq \frac{1}{54}
\end{align*}$$ Y en consecuencia, como los dos lados de la desigualdad
son diferentes, se concluirá que la suma y la resta absoluta obtenida
por el lanzamiento de los dos dados no son variables aleatorias
independientes.
</p>
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
Suponga que se tiene interés en observar el número promedio de horas de
tiempo libre que posee un profesor en un día y el número promedio de
horas de tiempo libre que poseen los estudiantes a los cuales se les
dicta un curso de Estadística I. Para ello, se encuentra que la función
de densidad de probabilidad conjunta está dada por $$\begin{align*}
f(x,y)=\frac{1}{42}xy^2 \quad \quad 0<x<2; 1<y<4
\end{align*}$$ siendo $X$ la variable aleatoria que representa el
número promedio de horas de tiempo libre del profesor y $Y$ el número
promedio de horas de tiempo libre de los estudiantes. Verifique si las
variables aleatorias $X$ y $Y$ son estadísticamente independientes.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Similar al caso discreto, el objetivo será observar si el tiempo libre
promedio del profesor es independiente del tiempo libre promedio de los
estudiantes, y para ello será cuestión de observar al multiplicar las
distribuciones marginales se obtiene como resultado la misma
distribución conjunta. <br>

Así tenemos entonces que, la distribución conjunta está dada por
$$\begin{align*}
f(x,y)=\frac{1}{42}xy^2 \quad \quad 0<x<2; 1<y<4
\end{align*}$$ mientras que las distribuciones marginales están dadas
por $$\begin{align*}
g(x) =& \frac{1}{2}x &\quad \quad 0<x<2 \\
h(y) =& \frac{1}{21}y^2 &\quad \quad 1<y<4
\end{align*}$$ por tanto, al aplicar la formula de independencia
tendremos que $$\begin{align*}
f(x,y)&=g(x)h(y) \\
\frac{1}{42}xy^2&= \left(\frac{1}{2}x\right) \left(\frac{1}{21}y^2\right) \\
\frac{1}{42}xy^2&= \frac{1}{42}xy^2
\end{align*}$$ y en consecuencia, como ambos lados de la desigualdad son
iguales se tendrá que el número promedio de horas de tiempo libre que
tiene el profesor es independiente del número promedio de horas de
tiempo libre que tienen los estudiantes del curso de Estadística I.
</p>
</main>