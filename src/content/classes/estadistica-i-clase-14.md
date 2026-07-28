---
title: "Clase 10"
course: "estadistica-i"
order: 14
classType: "clase"
description: "Distribuciones de probabilidad conjuntas - Distribución de probabilidad conjunta discreta - Distribución de probabilidad conjunta continua"
math: true
bibliography: "../../referencias.bib"
---

Distribución de probabilidad conjunta
-------------------------------------

### Distribución de probabilidad conjunta discreta

Se dice que la función `$p(x,y)$`, es una función de masa de
probabilidad conjunta de las variables aleatorias discretas `$X, Y$`, si
se cumple que

1.  `$p(x,y)\geq0$` para todo `$x,y \in$` al rango de `$X,Y$`,
    respectivamente.
2.  `$\sum_x\sum_y p(x,y)=1$`
3.  `${\sum\sum}_{(x,y)\in A}p(x,y) = \mathbb{P}[(X,Y)\in A]$` con
    `$A\in$` al rango de `$X,Y$`.

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
Suponga un experimento que consta en lanzar dos dados al aire. Sea \(X\)
la variable aleatoria que indica la suma resultante de los dos dados, y
\(Y\) la variable aleatoria del valor absoluto de la diferencia de los
dos dados. Defina
</p>
<ol>
<li>
El espacio muestral \(S\) del experimento aleatorio.
</li>
<li>
Los valores que puede tomar la variable aleatoria \(X\).
</li>
<li>
Los valores que puede tomar la variable aleatoria \(Y\).
</li>
<li>
La función de probabilidad conjunta del experimento aleatorio.
</li>
<li>
La función de masa de probabilidad está bien definida?.
</li>
<li>
Calcule la probabilidad de que la suma de los dados sea menor a \(5\),
pero la resta absoluta sea a lo más de \(2\).
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Sean los números del \(1\) al \(6\) los números que representan el
resultado del primer y segundo dado, siendo la primera posición el
resultado del primer dado, y la segunda posición el resultado del
segundo dado, entonces, se tendrá que el espacio muestral se define como
$$\begin{align*}
S = \{&11,\;12,\;13,\;14,\;15,\;16, \\
      &21,\;22,\;23,\;24,\;25,\;26, \\
      &31,\;32,\;33,\;34,\;35,\;36, \\
      &41,\;42,\;43,\;44,\;45,\;46, \\
      &51,\;52,\;53,\;54,\;55,\;56, \\
      &61,\;62,\;63,\;64,\;65,\;66\}
\end{align*}$$
</li>
<li>

Como el interés de la variable aleatoria \(X\) radica en la suma del
resultado obtenido por los dos dados, se tendrá entonces que a partir
del espacio muestral \(S\) se puede encontrar que la suma en cada
situación es $$\begin{align*}
S = \{&\underset{2}{11},\;\underset{3}{12},\;\underset{4}{13},\;\underset{5}{14},\;\underset{6}{15},\;\underset{7}{16}, \\
      &\underset{3}{21},\;\underset{4}{22},\;\underset{5}{23},\;\underset{6}{24},\;\underset{7}{25},\;\underset{8}{26}, \\
      &\underset{4}{31},\;\underset{5}{32},\;\underset{6}{33},\;\underset{7}{34},\;\underset{8}{35},\;\underset{9}{36}, \\
      &\underset{5}{41},\;\underset{6}{42},\;\underset{7}{43},\;\underset{8}{44},\;\underset{9}{45},\;\underset{10}{46}, \\
      &\underset{6}{51},\;\underset{7}{52},\;\underset{8}{53},\;\underset{9}{54},\;\underset{10}{55},\;\underset{11}{56}, \\
      &\underset{7}{61},\;\underset{8}{62},\;\underset{9}{63},\;\underset{10}{64},\;\underset{11}{65},\;\underset{12}{66}\}
\end{align*}$$

Evidenciando, que podemos asignar los valores \(2,3,\ldots,12\) a la
variable aleatoria \(X\).
</li>
<li>

Como el interés de la variable aleatoria \(Y\) radica en el valor
absoluto de la resta absoluta de los resultado obtenido por los dos
dados, se tendrá entonces que a partir del espacio muestral \(S\) se
puede encontrar que la resta absoluta en cada situación es
$$\begin{align*}
S = \{&\underset{0}{11},\;\underset{1}{12},\;\underset{2}{13},\;\underset{3}{14},\;\underset{4}{15},\;\underset{5}{16}, \\
      &\underset{1}{21},\;\underset{0}{22},\;\underset{1}{23},\;\underset{2}{24},\;\underset{3}{25},\;\underset{4}{26}, \\
      &\underset{2}{31},\;\underset{1}{32},\;\underset{0}{33},\;\underset{1}{34},\;\underset{2}{35},\;\underset{3}{36}, \\
      &\underset{3}{41},\;\underset{2}{42},\;\underset{1}{43},\;\underset{0}{44},\;\underset{1}{45},\;\underset{2}{46}, \\
      &\underset{4}{51},\;\underset{3}{52},\;\underset{2}{53},\;\underset{1}{54},\;\underset{0}{55},\;\underset{1}{56}, \\
      &\underset{5}{61},\;\underset{4}{62},\;\underset{3}{63},\;\underset{2}{64},\;\underset{1}{65},\;\underset{0}{66}\}
\end{align*}$$

Evidenciando, que podemos asignar los valores \(0,1,\ldots,5\) a la
variable aleatoria \(Y\).
</li>
<li>

Para encontrar la función de probabilidades del experimento aleatorio
asociadas a la función de probabilidad conjunta, podemos emplear la
definición de la
<a href="../../EstadisticaI/EstIClase05.html#probabilidad" target="\_blank">frecuencia
relativa</a>, aprovechando que todos los puntos del espacio muestral
poseen la misma probabilidad y que tenemos el espacio muestral de las
dos variables aleatorias.<br>

Por ejemplo, se tiene que cuando \(X=2\), \(Y\) solo puede ser igual a
\(0\) en el punto muestral \(11\), y en consecuencia,
\(\mathbb{P}(X=2, Y=0) = 1/36\). Similarmente, se tiene que cuando
\(X=3\), \(Y\) solo puede ser igual a \(1\) en los dos puntos puestrales
\(12\) y \(21\), y en consecuencia, \(\mathbb{P}(X=3, Y=1) = 2/36\).
Procedimiento similar se aplica para el calculo de todas las
probabilidades posibles, obteniendo la siguiente tabla resultante

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto; font-size:100%!important">
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
</li>
<li>

Dado que solo nos interesa la situación en que la suma sea menor a \(5\)
y la resta absoluta sea a lo más de \(2\), se tendrá que nos están
preguntando por la probabilidad de que

$$\begin{align*}
\mathbb{P}(X<5, Y\leq2)
\end{align*}$$

entonces al observar la tabla de probabilidades tenemos que las
probabilidades que cumplen tal condición son

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto; font-size:100%!important">
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
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">\frac{1}{36}</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">0</script>
</span>
</td>
<td style="text-align:center;">
<span style="border-radius: 4px;padding-right: 0px;padding-left: 0px;padding-top: 3px;padding-bottom: 7px;background-color: #974c55 !important;">
<script type="math/tex">\frac{1}{36}</script>
</span>
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

Por tanto, la probabilidad calculada será

$$\begin{align*}
\mathbb{P}(X<5, Y\leq2) = & \sum_{x=2}^{4}\sum_{y=0}^2p(x,y) \\
                        = & p(2,0) + p(2,1) + p(2,2) + p(3,0) + \ldots p(4,2)  \\
                        = &\frac{1}{36} + 0 + 0 + 0 + \frac{2}{36} + 0 + \frac{1}{36} + 0 + \frac{2}{36} \\
                        = &\frac{6}{36}
\end{align*}$$

y en consecuencia, se tendrá que la probabilidad de que la suma de los
dados sea menor a \(5\), pero la resta absoluta sea a lo más de \(2\) es
del \(16.67\%\).
</li>
</ol>
</main>

### Distribución de probabilidad conjunta continua

Se dice que la función `$f(x,y)$`, es una función de densidad de
probabilidad conjunta de las variables aleatorias discretas `$X, Y$`, si
se cumple que

1.  `$f(x,y)\geq0$` para todo `$x,y \in \mathbb{R}$`.
2.  `$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y) dxdy=1$`
3.  `$\iint_{(x,y)\in A}f(x,y) = \mathbb{P}[(X,Y)\in A]$` con `$A$` un
    intervalo de valores `$\in \mathbb{R}$`

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
Suponga que se tiene interés en observar el número promedio de horas de
tiempo libre que posee un profesor en un día y el número promedio de
horas de tiempo libre que poseen los estudiantes a los cuales se les
dicta un curso de Estadística I. Para ello, se encuentra que la función
de densidad de probabilidad conjunta está dada por $$\begin{align*}
f(x,y)=\frac{k}{8}xy^2 \quad \quad 0<x<2; 1<y<4
\end{align*}$$ siendo \(X\) la variable aleatoria que representa el
número promedio de horas de tiempo libre del profesor y \(Y\) el número
promedio de horas de tiempo libre de los estudiantes. A partir de dicha
función
</p>
<ol>
<li>
Encuentre el valor de la constante \(k\) para que hace que \(f(x,y)\) se
encuentre bien definida.
</li>
<li>
Calcule la probabilidad de que el tiempo promedio libre que tiene el
profesor sea a lo más de \(0.7\) horas, y el tiempo promedio libre de
los estudiantes se encuentre entre \(1.2\) y \(2.3\) horas.
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

Para verificar si la función de distribución conjunta está bien
definida, es necesario observar si para todo \(X\) y \(Y\) en los
dominio definido, la función de probabilidad de densidad de probabilidad
es mayor o igual a \(0\). en donde se aprecia que al ser una
multiplicación, y que los dominios se encuentran definidos para números
positivos, se tendrá que \(f(x,y)\geq0\) siempre y cuando \(k>0\). <br>

Ahora, para encontrar el valor de \(k\) que hace que la función de
densidad de probabilidad conjunta se encuentre bién definida, se tendrá
que integrar \(f(x,y)\) en todo el dominio definido para la variable
aleatoria \(X\) y la variable aleatoria \(Y\).

$$\begin{align*}
\int_0^2\int_1^4\frac{k}{8}xy^2\text{ d}y\text{ d}x =& \frac{k}{8}\int_0^2\int_1^4xy^2\text{ d}y\text{ d}x \\
=& \frac{k}{8}\int_0^2x\frac{y^3}{3}\Bigg|^4_1\text{ d}x \\
=& \frac{k}{24}\int_0^2x(4^3 - 1^3)\text{ d}x \\
=& \frac{k}{24}\int_0^2x(64 - 1)\text{ d}x \\
=& k\frac{63}{24}\int_0^2x\text{ d}x \\
=& k\frac{63}{24}\frac{x^2}{2}\Bigg|_0^2 \\
=& k\frac{63}{48}(2^2 - 0^2) \\
=& k\frac{63}{48}(4) \\
=& k\frac{21}{4} \\
\end{align*}$$

Y por tanto, para que \(f(x,y)\) sea una función bién definida se tendrá
que \(k\) deberá ser igual a \(\frac{4}{21}\), debido a que la integral
en todo el dominio definido siempre debe dar igual a \(1\).
</li>
<li>

Dado que el interés es encontrar la probabilidad de que el tiempo
promedio que tiene libre el profesor y los estudiantes es a lo más de
\(0.7\) y entre \(1.2\) y \(2.3\) horas, respectivamente, entonces se
tendrá que la probabilidad a calcular será

$$\begin{align*}
\mathbb{P}(X \leq 0.7;\; 1.2 < Y < 2.3) 
\end{align*}$$

Así, que al realizar la integral se obtendrá que

$$\begin{align*}
\mathbb{P}(X \leq 0.7, 1.2 < Y < 2.3) 
  =& \int_0^{0.7}\int_{1.2}^{2.3}\frac{4}{21}\frac{1}{8}xy^2\text{ d}y\text{ d}x \\ 
  =& \frac{1}{42}\int_0^{0.7}\int_{1.2}^{2.3}xy^2\text{ d}y\text{ d}x \\
  =& \frac{1}{42}\int_0^{0.7}x\frac{y^3}{3}\Bigg|_{1.2}^{2.3}\text{ d}x \\
  =& \frac{1}{126}\int_0^{0.7}x(2.3^3 - 1.2^3)\text{ d}x \\
  =& \frac{1}{126}\int_0^{0.7}x(12.167 - 1.728)\text{ d}x \\
  =& \frac{10.439}{126}\int_0^{0.7}x\text{ d}x \\
  =& \frac{10.439}{126}\frac{x^2}{2}\Bigg|_0^{0.7} \\
  =& \frac{10.439}{252}(0.7^2 - 0^2) \\
  =& \frac{10.439}{252}(0.49) \\
  =& 0.0203 \\
\end{align*}$$ En consecuencia se tendrá que la probabilidad de que el
tiempo promedio libre que tiene el profesor sea a lo más de \(0.7\)
horas, y el tiempo promedio libre que tienen los estudiantes se
encuentre entre \(1.2\) y \(2.3\) horas, es del \(2.03\%\).
</li>
</ol>
</main>