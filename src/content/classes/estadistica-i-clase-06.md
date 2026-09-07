---
title: "Clase 17"
course: "estadistica-i"
order: 21
classType: "clase"
description: "Distribuciones de probabilidad discreta: - Distribución Uniforme discreta Teoremas de Aproximación: - Aproximación Hipergeométrica a Binomial - Aproximación Binomial a Poisson"
math: true
bibliography: "../../referencias.bib"
---

Distribuciones de probabilidad discretas
----------------------------------------

### Distribución Uniforme Discreta

Se dice que la variable aleatoria $X$ tiene una distribución uniforme
discreta en los enteros $a, a+1,\ldots, b$, si su distribución de
probabilidad es de la forma

$$\begin{align*}p(x) = \frac{1}{b-a+1} \quad \quad x = a,a+1, \ldots, b\end{align*}$$


#### Media y Varianza Uniforme Discreta

Si $X\sim Unif\{a, a+1,\ldots,b\}$ entonces se puede probar que la
media y varianza de la variable aleatoria $X$ están dadas por

$$\begin{align*}\mathbb{E}(X)=\frac{a+b}{2} \quad \quad Var(X)=\frac{(b-a+1)^2-1}{12}\end{align*}$$


#### Distribución Acumulada Uniforme Discreta

Si $X\sim Unif\{a, a+1,\ldots,b\}$ entonces se puede probar que la
función de distribución acumulada de la variable aleatoria $X$ es de
la forma

$$\begin{align*}F(x) = \frac{x-a+1}{b-a+1} \quad \quad & a\leq x\leq b\end{align*}$$


<!-- Demostración, suma de números triangulares pitágoras -->
<!-- 
$$\begin{align*}-->
<!-- \sum_{i=1}^N x_i = \frac{N(N+1)}{2} \quad \quad \sum_{i=1}^N x_i^2 = \frac{N(N+1)(2N+1)}{6} -->
<!--\end{align*}$$
 -->
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
Suponga que se decide realizar una rifa en la Facultad de Ciencias
Económicas con el fin de otorgar a uno de sus docentes una bonificación
salarial correspondiente a una semana de salario. Para realizar la rifa,
la Facultad enumera del $1$ al $297$ a la totalidad de docentes, de
tal forma que los primeros $87$ números corresponden a docentes del
Departamento de Administración de empresas, los siguientes $76$
corresponden a docentes del Departamento de Contaduría, los siguientes
$89$ corresponden a docentes del Departamento de Economía, y los
números finales a docentes del Departamento de Estadística y
Matemáticas. Si sacar cualquier número en la rifa posee la misma
probabilidad
<ol>
<li>
Calcule la probabilidad de que el número que se saque en la rifa sea el
$8$?
</li>
<li>
Calcule la probabilidad de que el número que se saque en la rifa
pertenezca al Departamento de Contaduría?
</li>
<li>
Calcule la esperanza matemática y desviación estándar de la variable
aleatoria?.
</li>
</ol>
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Para resolver este ejercicio, debemos tener en cuenta que todos los
números de la rida poseen la misma probabilidad, es decir, nos dicen que
la función de masa de probabilidad de la rifa está dada por
$$\begin{align*}
p(x) = \frac{1}{297-1+1}=\frac{1}{297} \quad \quad x = 1,2, \ldots, 297
\end{align*}$$
es decir, que cada uno de los números de la rifa tienen
una probabilidad de $1$ entre $297$ en salir.
</p>
<ol>
<li>
Basados en esta distribución, en el primer punto nos piden calcular la
probabilidad de que el número que sale en la rifa sea igual a $8$, es
decir que $$\begin{align*}
\mathbb{P}(X=8)
\end{align*}$$
Entonces, dado que la función de distribución de
probabilidad Uniforme discreta, no depende de la variable aleatoria
$X$, se tendrá que esta probabilidad es igual a $$\begin{align*}
\mathbb{P}(X=8) &= p(8) \\
                &= \frac{1}{297} \\
                &= 0.003367003
\end{align*}$$
Es decir, que se tendrá un $3.37\%$ de probabilidad, de
que el número elegido por la rifa sea el número $8$.
</li>
<li>

En este caso, se nos pide calcular la probabilidad de que el número que
se saque en la rifa pertenezca al Departamento de Contaduría, entonces,
como nos dicen en el enunciado que los números del
$1\leftrightarrow87$ pertenecen al Departamento Administración de
empresas, del $88\leftrightarrow163$ pertenecen al Departamento de
Contaduría, del $164\leftrightarrow252$ pertenecen al Departamento de
Economía y del $253\leftrightarrow297$ pertenecen al Departamento de
Estadística y Matemáticas, así que nuestro interés será calcular
$$\begin{align*}
\mathbb{P}\left(88 \leq X \leq 163\right) 
\end{align*}$$
Entonces como a función de distribución acumulada de la
distribución Uniforme discreta está definida, podemos emplearla para
calcula la probabilidad de interés, tal que $$\begin{align*}
\mathbb{P}\left(88 \leq X \leq 163\right) &= \mathbb{P}\left(X \leq 163\right) - \mathbb{P}\left(X < 88\right) \\
                                          &= \mathbb{P}\left(X \leq 163\right) - \mathbb{P}\left(X \leq 87\right) \\
                                          &= F(163) - F(87) \\
                                          &= \frac{163-1+1}{297-1+1} + \frac{87-1+1}{297-1+1} \\
                                          &= \frac{163}{297} + \frac{87}{297} \\
                                          &= \frac{76}{297} \\
                                          &= 0.2558923
\end{align*}$$

Y por tanto, se tendrá una probabilidad del $25.59\%$ de que el número
seleccionado en la rifa pertenezca al Departamento de Contaduría.
</li>
<li>
Finalmente, en esta pregunta nos piden calcular la media y desviación
estándar de la variable aleatoria, y para ello podemos emplear la
definición de esperanza matemática y varianza para el caso de la
distribución Uniforme discreta, tal que el valor esperado sería igual a
$$\begin{align*}
\mathbb{E}(X) &= \frac{1+297}{2} \\
              &= \frac{298}{2} \\
              &= 149
\end{align*}$$
mientras que la varianza es igual a $$\begin{align*}
Var(X) &= \frac{(297-1+1)^2-1}{12} \\
       &= \frac{88209 - 1}{2} \\
       &= \frac{88208}{12} \\
       &= 7350.667
\end{align*}$$
Ahora, dada la relación que hay entre la varianza y la
desviación estándar, se tendrá que $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{7350.667} \\
      &= 85.73603
\end{align*}$$
Y por tanto, se tendrá que en promedio, se espera que el
número extraído en la rifa será de $149$, con una desviación estándar
de $85.73603$.
</li>
</ol>
</main>

Teoremas de Aproximación
------------------------

### Teorema de Aproximación Hipergeométrica a Binomial

Si $X\sim h(N,M,n)$ con $n$ pequeña en comparación con $N$
($n/N <0.05$) entonces se dice que $X\stackrel{a}{\sim}b(n,p)$ con
$p = M/N$.

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
Una gran distribuidora tiene $800$ equipos de computo, de los cuales
se sabe que $8$ de ellos están defectuosos. Una compañía compra $20$
de estos y le son despachados al azar. ¿Cuál es la probabilidad de que
en la muestra se observen $2$ o más defectuosos?. Emplee tanto la
distribución hipergeométrica como la aproximación a binomial y comente
sobre los resultados obtenidos
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en calcular una probabilidad
hipergeométrica de que en una muestra de $n=20$ equipos de computo,
extraídos de un total de $N=800$ equipos, se encuentren como mínimo
$2$ equipos defectuosos, cuando se sabe que dentro de los $N=800$
hay un total de $M=8$ equipos defectuosos, esto es $$\begin{align*}
\mathbb{P}(X\geq 2) 
\end{align*}$$

Ahora, antes de plantear la probabilidad, será necesario encontrar los
limites en donde está definida la función de probabilidad discreta, tal
que $$\begin{align*}
\max\{0, M-(N-n)\} &\leq x \leq \min\{M,n\} \\
\max\{0, 8-(800-20)\} &\leq x \leq \min\{8,20\} \\
\max\{0, 8-(780)\} &\leq x \leq \min\{8,20\} \\ 
\max\{0, -772\} &\leq x \leq \min\{8,20\} \\
0 &\leq x \leq 8 \\
\end{align*}$$
y por tanto, tendremos que el número de equipos de
cómputo defectuosos encontrados en la muestra puede ser de
$x=0, 1, 2, \ldots 8$. <br> <br> Ahora, podemos emplear la
distribución hipergeométrica para calcular la probabilidad de interés,
tal que $$\begin{align*}
\mathbb{P}(X\geq 2) &= \sum_{x=2}^{8} \frac{\left(\begin{array}{c}8\\ x\end{array}\right) \left(\begin{array}{c}792\\ 20-x\end{array}\right)}{\left(\begin{array}{c}800\\ 20\end{array}\right)} \\
                    &= 0.01520272
\end{align*}$$

Es decir, que la probabilidad de que como mínimo se encuentren $2$
equipos de computo defectuosos dentro de la muestra de $10$ equipos de
computo, extraídos de un grupo de $800$ de los cuales se sabe queh hay
$8$ artículos defectuosos, es de $1.52\%.$.<br> <br> Ahora, si
realizamos la aproximación de la distribución hipergeométrica a la
distribución binomial que resultado tendríamos?. <br> <br> Para ello
será necesario calcular el valor del parámetro $p$ de la distribución
binomial, el cual está dado por $$\begin{align*}
p &= \frac{M}{N} \\
  &= \frac{8}{800} \\
  &= 0.01
\end{align*}$$
Es decir que la distribución $h(N=800, M=8, n=20)$
puede aproximarse a una distribución $b(n=20, p=0.01)$, donde
observamos que $n/N = 20/800 = 0.025$, y por tanto, se tendrá que la
aproximación debería ser buena, debido a que cumple la condición de la
aproximación.<br> <br> Entonces, al emplear la distribución binomial
para calcula la probabilidad tendremos que $$\begin{align*}
\mathbb{P}(X\geq 2) &= \sum_{x=2}^{20} \left(\begin{array}{c}20\\ x\end{array}\right)0.01^x(1-0.01)^{20-x}\\
                    &= 0.01685934
\end{align*}$$
Lo cual indica que, al realizar la aproximación, se tiene
un $1.69\%$ de probabilidad de encontrar al menos $2$ equipos de
computo defectuosos de una muestra de $20$ artículos seleccionados,
cuando la probabilidad de que un artículo sea defectuoso es del $1\$$.
<br> <br> Al observar las dos probabilidades anteriores, la calculada
con la distribución hipergeométrica $1.52\%$, y la calculada con la
aproximación binomial $1.69\%$, donde se aprecia que las dos son
relativamente similares, y en consecuencia, se dice que la aproximación
binomial dadas las características del ejercicio ofrece una buena
aproximación al que se obtendría con la distribución hipergeométrica.
</p>
</main>

### Teorema de Aproximación Binomial a Poisson

Si $X\sim b(n,p)$ con $n$ grande $(n\geq 100)$ y $p$ pequeña
$(p\leq 0.01)$ entonces se dice que $X\stackrel{a}{\sim}P(\lambda)$
donde $\lambda = np$

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
Suponga que al realizar un estudio sobre un proceso de producción, se
encontró que el $3\%$ de los artículos producidos resultaba tener
algún tipo de defecto. Si se producen $900$ artículos en un día, cuál
es la probabilidad de que $30$ artículos o menos resulten tener algún
tipo de defecto. Emplee tanto la distribución binomial como la
aproximación a Poisson y comente sobre los resultados obtenidos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en calcular una probabilidad binomial
de un grupo $n$ de $900$ artículos, de los cuales se busca a que el
número de artículos defectuosos $X$, sea de al menos $30$
defectuosos, sabiendo que la probabilidad de producir un artículo
defectuoso es del $3\%$. Esto es $$\begin{align*}
\mathbb{P}(X \leq 30) &= \sum_{x=0}^{30} \left(\begin{array}{c}900\\ x\end{array}\right) (0.03)^x(0.97)^{900-x} \\
                      &= 0.7581561
\end{align*}$$
Es decir, que la probabilidad de que como máximo $30$
artículos de los $900$ sean defectuosos es del $75.81\%$. <br> <br>

Ahora, si realizamos la aproximación de la distribución binomial a la
distribución Poisson que resultado tendríamos?. <br> <br>

Para ello será necesario calcular el parámetro $\lambda$ de la
distribución Poisson, el cual está dado por $$\begin{align*}
\lambda &= np \\
        &= 900(0.03) \\
        &= 27
\end{align*}$$
Es decir que la distribución $b(n=900, p=0.03)$ puede
aproximarse a una distribución $Pois(\lambda=27)$, que $n$ es grande
y $p$ es pequeño (aunque éste no cumpla la condición de que
$p\leq 0.01$, pero dichas condiciones son valores para tener como
puntos de referencia). Por tanto, al calcular la probabilidad con la
distribución Poisson tenemos que $$\begin{align*}
\mathbb{P}(X \leq 30) &= \sum_{x=0}^{30} \frac{e^{-27}27^x}{x!} \\
                      &= 0.7553101
\end{align*}$$
Lo cual indica que, al realizar la aproximación, se tiene
un $75.53\%$ de probabilidad de que al menos $30$ artículos de los
$900$ seleccionados, resulten tener algún tipo de defecto. <br> <br>

Al observar las dos probabilidades anteriores, la calculada con la
distribución binomial $75.81\%$, y la calculada con la distribución
Poisson $75.53\%$, se aprecia que las dos son muy similares, y en
consecuencia, se dice que la distribución Poisson dadas las
características del ejercicio ofrece una buena aproximación al que se
obtendría con la distribución binomial.
</p>
</main>