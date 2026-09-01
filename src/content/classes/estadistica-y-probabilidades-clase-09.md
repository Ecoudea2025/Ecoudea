---
title: "Clase 08"
course: "estadistica-y-probabilidades"
order: 12
classType: "clase"
description: "Variables aleatorias continuas - Funciones de probabilidad - Función de distribución acumulada - Esperanza matemática - Propiedades de esperanza matemática - Varianza"
math: true
bibliography: "../../referencias.bib"
---

Variables aleatorias continuas
------------------------------

### Función de probabilidad

Se dice que la función `$f(x)$` es una función de densidad de
probabilidad (*fdp*) de la variable aleatoria continua `$X$`, definida
en el conjunto de números reales si

1.  `$f(x)\geq0$` para todo `$x \in \mathbb{R}$`

2.  `$\int_{-\infty}^\infty f(x) dx=1$`

3.  `$\int_{a}^b f(x) dx = \mathbb{P}(a<X<b)$`

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
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$ siendo \(X\) una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo. A
partir de dicha función
</p>
<ol>
<li>
Verifique si la función de densidad de probabilidad está bien definida?
De no estarlo, multiplique la función por una constante \(k\) para que
quede bien definida.
</li>
<li>
Calcule la probabilidad de que el tiempo que tarda la serie en cumplir
un ciclo sea de \(30\) minutos a \(50\) minutos.
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

Para verificar si la función está bien definida, es necesario en primer
lugar observar si para todo \(X\) en el dominio definido, la función de
probabilidad de densidad de probabilidad es mayor o igual a \(0\). Para
ello supongamos \(3\) números diferentes, \(0.1\) \(0.4\) y \(0.7\), los
cuales vamos a evaluar en la función de densidad. $$\begin{align*}
f(0.1)=(0.1)^2(1-0.1)^2=0.0081 \\
f(0.4)=(0.4)^2(1-0.4)^2=0.0576 \\
f(0.7)=(0.7)^2(1-0.7)^2=0.0441
\end{align*}$$ La idea entonces, es apreciar que para todo \(0<x<1\),
\(f(x)\geq0\).<br>

En segundo lugar, para observar si la función de densidad de
probabilidad está bien definida, es necesario observar si al integrar
dicha función su resultado es igual a \(1\), es decir,

$$\begin{align*}
\int_{-\infty}^\infty f(x)dx & = \int_{-\infty}^0 0\; dx + \int_{0}^1 x^2(1-x)^2\; dx + \int_{1}^\infty 0\; dx \\
 & = \int_{0}^1 x^2(1-x)^2\; dx \\
 & = \int_{0}^1 x^2(1^2-2x+x^2)\; dx \\
 & = \int_{0}^1 x^2-2x^3+x^4\; dx \\
 & = \left(\frac{x^3}{3} - \frac{2x^4}{4} + \frac{x^5}{5} \right)\Bigg|^1_0 \\
 & = \left(\frac{1^3}{3} - \frac{1^4}{2} + \frac{1^5}{5} \right) - \left(\frac{0^3}{3} - \frac{0^4}{2} + \frac{0^5}{5} \right) \\
 & = \frac{1}{30}
\end{align*}$$ Entonces, como la integral no da exactamente \(1\), se
tendrá que multiplicar dicha función de densidad por una constante \(k\)
que haga que su resultado sea \(1\), es decir, si multiplicamos la
función por \(k=30\), se tendrá como resultado que la integral será
igual a \(1\), ya que, $$\begin{align*}
30\int_{-\infty}^\infty f(x)dx & = 30 \int_{0}^1 x^2(1-x)^2\; dx \\
 & = 30 \left(\frac{1^3}{3} - \frac{1^4}{2} + \frac{1^5}{5} \right) \\
 & = \frac{30}{30} \\
 & = 1
\end{align*}$$ Y en consecuencia, se tendrá que la nueva función de
densidad de probabilidad está bien definida. $$\begin{align*}
f(x) = 30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$

</li>
<li>

Dado que la función de densidad está en horas, será necesario pasar los
minutos a horas, en donde, al aplicar una regla de tres para cada límite
de la integral que nos piden se tendrá que $$\begin{align*}
60_\text{min}  &- 1_\text{hora} & \quad \quad & 60_\text{min} - 1_\text{hora}\\30_\text{min} &- a & \quad \quad & 50_\text{min} - b
\end{align*}$$ Entonces, al realizar la operación encontramos que los
límites de la integral serán
$$\begin{align*}a&=\frac{30_\text{min}\times1_{\text{hora}}}{60
_\text{min}}=0.5_\text{horas} \\
b&=\frac{50_\text{min}\times1_{\text{hora}}}{60
_\text{min}}=0.8333_\text{horas}
\end{align*}$$ Ahora, al realizar la integral tendremos que

$$\begin{align*}
\mathbb{P}(0.5 < X < 0.8333) & = \int_{0.5}^{0.8333} 30 x^2(1-x)^2\; dx \\
 & = 30\int_{0.5}^{0.8333} x^2-2x^3+x^4\; dx \\
 & = 30\left(\frac{x^3}{3} - \frac{2x^4}{4} + \frac{x^5}{5} \right)\Bigg|^{0.8333}_{0.5} \\
 & = 30 \left[\left(\frac{0.8333^3}{3} - \frac{0.8333^4}{2} + \frac{0.8333^5}{5} \right) - \left(\frac{0.5^3}{3} - \frac{0.5^4}{2} + \frac{0.5^5}{5} \right)\right] \\
 & = 0.4645
\end{align*}$$

En consecuencia, se tendrá una probabilidad del \(46.45\%\) de que el
tiempo que tarda la serie financiera en cumplir un ciclo estará entre
\(30\) minutos y \(50\) minutos.
</li>
</ol>
</main>

Función de distribución acumulada caso continuo
-----------------------------------------------

La función de distribución acumulada (*fda*) denotada por `$F(x)$`, para
una variable aleatoria continua `$X$` con distribución de probabilidad
`$f(x)$` es de la forma

$$\begin{align*}F(x)=\mathbb{P}(X\leq x)=\int_{-\infty}^x f(t) dt \quad \quad\end{align*}$$


para cualquier `$x$`, `$F(x)$` es el área izquierda bajo la curva de
densidad.

**Nota:** Si se quieren calcular probabilidades con la función de
distribución acumulada en el caso continuo, entonces, si `$a$` y `$b$`
son dos números constantes, deberán tenerse en cuenta las siguientes
reglas

-   `$\mathbb{P}(a \leq X \leq b) = \mathbb{P}(X\leq b) - \mathbb{P}(X\leq a) = F(b) - F(a)$`
-   `$\mathbb{P}(X \geq a) = 1 - \mathbb{P}(X\leq a) = 1 - F(a)$`
-   `$\mathbb{P}(X \leq b) = F(b)$`

**Nota:** Recordar que en el caso continuo, las probabilidad con o sin
la igualdad son equivalentes, y por tanto, solo se escriben las tres
reglas anteriores para generalizar todos los casos.

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
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$ siendo \(X\) una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo. A
partir de dicha función
</p>
<ol>
<li>
Calcule la función de distribución acumulada \(F(x)\).
</li>
<li>
Calcule la probabilidad de que el tiempo que tarda la serie financiera
en cumplir un ciclo, se encuentre entre \(30\) minutos y \(50\) minutos,
mediante el uso de \(F(x)\).
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Para encontrar la función de distribución acumulada a partir de una
función de densidad de probabilidad, es necesario realizar la integral
de la función de densidad, de la forma $$\begin{align*}
F(x)& = \int_{-\infty}^x f(t)dt \\
    & = \int_{-\infty}^0 0dt + \int_{0}^x 30t^2(1-t)^2 dt \\
    & = 30\int_{0}^{x} t^2-2t^3+t^4\; dt \\
    & = 30\left(\frac{t^3}{3} - \frac{2t^4}{4} + \frac{t^5}{5} \right)\Bigg|^{x}_{0} \\
    & = 30\left[\left(\frac{x^3}{3} - \frac{x^4}{2} + \frac{x^5}{5} \right) - \left(\frac{0^3}{3} - \frac{0^4}{2} + \frac{0^5}{5} \right)\right]  \\
F(x)& = 30\left(\frac{x^3}{3} - \frac{x^4}{2} + \frac{x^5}{5} \right)
\end{align*}$$
</li>
<li>

Dado que el interés es calcular la probabilidad de que el tiempo que
tarda la serie financiera en cumplir un ciclo, se encuentre entre \(30\)
minutos y \(50\) minutos, entonces se tendrá que la probabilidad de
interés, en horas, es la siguiente $$\begin{align*}
\mathbb{P}(0.5 < X < 0.8333)
\end{align*}$$

Entonces, siguiendo las reglas anteriormente expuestas, dicha
probabilidad puede calcularse mediante

$$\begin{align*}
\mathbb{P}(0.5 < X < 0.8333) & = F(0.8333) - F(0.5) \\
                         & = 30\left(\frac{0.8333^3}{3} - \frac{0.8333^4}{2} + \frac{0.8333^5}{5} \right) - 30\left(\frac{0.5^3}{3} - \frac{0.5^4}{2} + \frac{0.5^5}{5} \right) \\
                         & = 0.4645
\end{align*}$$

y por tanto, se tendrá que la probabilidad de que el tiempo que tarde la
serie financiera en cumplir un ciclo estará entre \(30\) minutos y
\(50\) minutos, es de \(46.45\%\).
</li>
</ol>
</main>

Esperanza matemática caso continuo
----------------------------------

Si `$x$` es una variable aleatoria con *fdp* `$f(x)$`, entonces la media
o valor esperado de la variable aleatoria se denota por
`$\mathbb{E}(X)$` o `$\mu$` está dada por

$$\begin{align*}\mathbb{E}(X)=\int_{-\infty}^\infty xf(x) dx\end{align*}$$


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
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$ siendo \(X\) una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo.
Calcule el valor esperado en que tarda la serie financiera en cumplir un
ciclo.
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
\end{align*}$$ Y por tanto, se tendrá que el tiempo esperado que tarda
una serie financiera en cumplir un ciclo será \(0.5\) horas, la cual al
pasarla a minutos mediante la regla de tres

$$\begin{align*}
1_\text{hora}  &- 60_\text{min}\\0.5_\text{horas} &- a
\end{align*}$$

se tendrá que $$\begin{align*}
a= \frac{0.5_\text{horas}\times 60_\text{min}}{1_\text{hora}} = 30_\text{min}
\end{align*}$$

el tiempo esperado que tarda una serie financiera en cumplir un ciclo
será de \(30\) minutos.
</p>
</main>

### Propiedades de la esperanza matemática

Sea `$a$` y `$b$` dos números constantes (reales) y `$X$` una variable
aleatoria, entonces se tiene que

-   `$\mathbb{E}(a) = a$`
-   `$\mathbb{E}(bX) = b\mathbb{E}(X)$`
-   `$\mathbb{E}(a+bX) = a+ b\mathbb{E}(X)$`
-   si `$m(X)$` es una función de `$X$`, entonces


$$\begin{align*}\mathbb{E}(m(X))=\int_{-\infty}^\infty m(x)f(x)\end{align*}$$


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
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$ siendo \(X\) una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo.
Calcule
</p>
<ol>
<li>
\(\mathbb{E}(60X)\)
</li>
<li>
\(\mathbb{E}(X+40)\)
</li>
<li>
\(\mathbb{E}(X^2)\)
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

se procede a calcular \(\mathbb{E}(60X)\), tal que $$\begin{align*}
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

Similarmente, al usar la propiedad \(\mathbb{E}(aX)=a\mathbb{E}(X)\),
sabiendo que \(\mathbb{E}(X)=0.5\) se tendrá que $$\begin{align*}
\mathbb{E}(60X)&= 60\mathbb{E}(X) \\
               &= 60(0.5) \\
               &= 30 \\
\end{align*}$$
</li>
<li>

Para el cálculo de \(\mathbb{E}(X+40)\), se procede a la aplicación de
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

Ahora, aplicando la propiedad \(\mathbb{E}(X+b)=\mathbb{E}(X)+b\), se
tendrá que dicha esperanza puede calcularse en dos lineas, tal que
$$\begin{align*}
\mathbb{E}(X+40)&= \mathbb{E}(X) + 40\\
               &= 0.5 + 40 \\
               &= 40.5 \\
\end{align*}$$
</li>
<li>
Para el cálculo de la \(\mathbb{E}(X^2)\), se tendrá que en este caso
\(m(X) = X^2\), y por tanto, al aplicar la propiedad
\(\mathbb{E}(m(X))=\int_{-\infty}^\infty m(x)f(x) dx\) tendremos que
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

Varianza caso continuo
----------------------

Sea `$X$` una variable aleatoria con *fdp* `$f(x)$`, entonces si
`$m(X) = (X - \mathbb{E}(X))^2$`, se tendrá que la varianza de `$X$` que
se denota `$Var(X)$` o `$\sigma^2$` estará dada por

$$\begin{align*}Var(X) = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)^2\right]=\int_{-\infty}^\infty(x-\mathbb{E}(X))^2f(x) dx\end{align*}$$


Similar al caso discreto, se puede demostrar a partir de la ecuación
anterior, que una alternativa para el cálculo de la `$Var(X)$` es de la
forma


$$\begin{align*}Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2\end{align*}$$


además, la raíz cuadrada de la varianza de `$X$` se llama desviación
estándar de `$X$`, se denota por `$Sd(X)$` o `$\sigma$` y se define como

$$\begin{align*}Sd(X) = \sqrt{Var(X)}\end{align*}$$


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
Suponga que el tiempo que tarda una serie financiera en cumplir un
ciclo, es una variable aleatoria continua con función de densidad de
probabilidad dada por $$\begin{align*}
f(x)=30x^2(1-x)^2 \quad \quad 0<x<1
\end{align*}$$ siendo \(X\) una variable aleatoria que representa el
tiempo en horas que tarda la serie financiera en cumplir un ciclo.
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
<ol>
<li>

A partir de las ecuaciones anteriormente presentadas, se tiene que la
\(Var(X)\), puede calcularse a partir de la
\(\mathbb{E}(X^2)=0.2857142857\) y la \(\mathbb{E}(X)=0.5\). Entonces
basados en estos valores se tendrá que la varianza del tiempo en horas
que tarda la serie financiera en cumplir un ciclo está dada por

$$\begin{align*}
Var(X)&=\mathbb{E}(X^2) - \mathbb{E}(X)^2 \\
        &=0.2857142857 - (0.5)^2 \\
        &=0.2857142857 - 0.25 \\
        &=0.0357142857
\end{align*}$$

es decir, se tendrá que la varianza del tiempo que tarda una serie
financiera en cumplir un ciclo es de \(0.0357142857\) horas\(^2\).
</li>
<li>

Ahora bien, dado que la varianza no tiene una interpretación aplicable
al conjunto de datos, entonces, se procede a calcular la desviación
estándar, la cual es posible calcular a partir del valor de la
\(Var(X)=0.0357142857\), tal que

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.0357142857} \\
      &= 0.1889822
\end{align*}$$

y en consecuencia, se tendrá que el tiempo esperado que tarda una serie
financiera en cumplir un ciclo será \(0.5\) horas, con una desviación
estándar de \(0.1889822\) horas. Esto es, un promedio de \(30\) minutos
con una desviación de \(11.33893\).
</li>
</ol>
</main>