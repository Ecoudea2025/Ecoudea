---
title: "Clase 12"
course: "probabilidad-inferencia"
order: 16
classType: "clase"
description: "Distribuciones de probabilidad continua: - Distribución Exponencial: &nbsp * Relación con la distribución Poisson. &nbsp * Propiedad de Carencia de Memoria."
math: true
bibliography: "../../referencias.bib"
---

## Distribuciones de probabilidad continua

## Distribución Exponencial

Se dice que la variable aleatoria `$X$` tiene una distribución
Exponencial con parámetro `$\beta$`, si su función de densidad de
probabilidad es de la forma

$$\begin{align*}f(x) = \begin{cases} \frac{1}{\beta}e^{-\frac{x}{\beta}} & x\geq 0, \beta>0 \\ 0 & \text{en otro caso} \end{cases}\end{align*}$$


#### Teorema

Si `$X\sim Exp(\beta)$`, entonces se puede probar que la media y la
varianza de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=\beta \quad \quad Var(X)=\beta^2\end{align*}$$


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
Un ingeniero industrial afirma que encontró un catalizador solido que
permite aumentar la velocidad de reacción química promedio, requerida en
un proceso de producción de una bebida gaseosa. Dicho ingeniero asegura
que con este catalizador solido la velocidad de la reacción química se
reduce en promedio en \(3\) minutos, lo cual mejoraría la eficiencia de
la producción en un \(28\%\). Dado lo anterior
<ol>
<li>
Cuál es la probabilidad de en un lote cualquiera, el catalizador sólido
reduzca la velocidad de la reacción química en al menos \(5\) minutos?
</li>
<li>
Cuál es la probabilidad de en un lote cualquiera, el catalizador sólido
reduzca la velocidad de la reacción química en menos de \(4\) minutos,
pero en más de \(2.5\) minutos?
</li>
<li>
Cuál es el promedio y desviación estándar del tiempo que reduce el
catalizador solido para la reacción química empleada para la producción
de bebidas gaseosas?.
</li>
</ol>
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Como se aprecia en el enunciado del ejercicio, se pregunta por el tiempo
de reducción y se hace referencia en que el catalizador solido reduce
<strong>en promedio</strong> \(3\) minutos, sin dar más información al
respecto. Debido a ésto, podríamos asumir que la distribución de los
tiempos que reduce el catalizador sólido se distribuye exponencial con
parámetro \(\beta=3_{min}\).
<ol>
<li>
En este caso estamos interesados en calcular la probabilidad en que el
catalizador sólido reduzca la velocidad de la reacción química en al
menos \(5\) minutos. Esto es $$\begin{align*}
\mathbb{P}(X\geq5) = \int_5^\infty \frac{1}{3}e^{-\frac{x}{3}} dx
\end{align*}$$ Al hacer cambio de variable tenemos que $$\begin{align*}
u= \frac{x}{3} \quad \quad du = \frac{1}{3} dx
\end{align*}$$ Entonces, al evaluar los límites de la integral debido al
cambio de variable, se tiene que cuando \(x=5\), el valor de \(u=5/3\),
y cuando \(x=\infty\), el valor de \(u=\infty/3 = \infty\). Por tanto,
al hacer el cambio de variable y cambiar los límites de integración
tenemos que $$\begin{align*}
\mathbb{P}(X\geq5) &= \int_{\frac{5}{3}}^\infty e^{-u} du \\
                   &=  -e^{-u} \Bigg|_{\frac{5}{3}}^\infty \\
                   &=  -e^{-\infty} + e^{-\frac{5}{3}} \\
                   &=  0 + 0.1888756 \\
                   &=  0.1888756
\end{align*}$$ Es decir, se tendrá que la probabilidad de que el
catalizador sólido encontrado por el Ingeniero Industrial, reduzca la
velocidad de reacción quiímica en al menos \(5\) minutos, es del
\(18.89\%\).
</li>
<li>
Para esta pregunta, se desea conocer la probabilidad de que el
catalizador sólido reduzca la velocidad de reacción química usado en la
producción de bebidas gaseosas, en más de \(2.5\) minutos pero en menos
de \(4\) minutos. Es decir, se desea calcular la siguiente probabilidad
$$\begin{align*}
\mathbb{P}(2.5<X<4) = \int_{2.5}^4 \frac{1}{3}e^{-\frac{x}{3}} dx
\end{align*}$$ Al aplicar el cambio de variable usado en el punto
anterio se tiene que $$\begin{align*}
u= \frac{x}{3} \quad \quad du = \frac{1}{3} dx
\end{align*}$$ en donde, al evaluar el límite inferior y superior de la
integrar en \(u\), se tendrá que cuando \(x=2.5\), \(u=2.5/3\), mientras
que, cuando \(x=4\), \(u=4/3\), obteniendo con ello, la siguiente
expresión $$\begin{align*}
\mathbb{P}(2.5<X<4) &= \int_{\frac{2.5}{3}}^{\frac{4}{3}} e^{-u} du \\
                    &=  -e^{-u} \Bigg|_{\frac{2.5}{3}}^{\frac{4}{3}} \\
                    &=  -e^{-\frac{4}{3}} + e^{-\frac{2.5}{3}} \\
                    &=  -0.2635971 + 0.4345982 \\
                    &=  0.1710011
\end{align*}$$ Es decir, se tendrá un \(17.10\%\) de probabilidad, de
que el catalizador sólido reduzca la velocidad de reacción química entre
\(2.5\) y \(4\) minutos.
</li>
<li>

Para calcular el tiempo promedio y desviación estándar de reducción que
genera emplear el catalizador sólido propuesto por el Ingeniero
Industrial, y sabiendo que la distribución de estos tiempos se
distribuye exponencialmente con parámetro \(\beta=3\). Se emplean las
ecuaciones de esperanza matemática y varianza de la distribución
exponencial, tal que la esperanza será igual a $$\begin{align*}
\mathbb{E}(X)&=\beta \\
             &=3
\end{align*}$$

y la varianza será igual a $$\begin{align*}
Var(X)& = \beta^2 \\
      & = 3^2 \\
      & = 9
\end{align*}$$ y ahora, empleando el resultado de la varianza se procede
a calcular la desviación estándar, tal que $$\begin{align*}
Sd(X)& = \sqrt{Var(X)} \\
      & = \sqrt{9} \\
      & = 3
\end{align*}$$ Es decir, se espera que la reducción promedio del tiempo
que reduce el catalizador sólido propuesto por el Ingeniero Industrial,
sea de \(3\) minutos con una desviación estándar de \(3\) minutos.
</li>
</ol>
</p>
</main>

#### Función de distribución acumulada Exponencial

Si `$X\sim Exp(\beta)$`, entonces se puede probar que la función de
distribución acumulada de `$X$` está dada por

$$\begin{align*}F(x) = \mathbb{P}(X\leq x) = \begin{cases} 0 & x<0 \\ 1- e^{-\frac{x}{\beta}} & x\geq 0, \beta>0  \end{cases}\end{align*}$$


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
Un ingeniero industrial afirma que encontró un catalizador solido que
permite aumentar la velocidad de reacción química promedio, requerida en
un proceso de producción de una bebida gaseosa. Dicho ingeniero asegura
que con este catalizador solido la velocidad de la reacción química se
reduce en promedio en \(3\) minutos, lo cual mejoraría la eficiencia de
la producción en un \(28\%\). Dado lo anterior, calcule la función de
distribución acumulada, y con ésta, calcule la probabilidad de que la
reducción promedio en la reacción química sea de entre \(5\) y \(8\)
minutos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Como el interés es calcular inicialmente la función de distribución
acumulada, entonces aplicamos la ecuación de la distribución acumulada,
reemplazando a \(\beta\) por \(3\), tal que $$\begin{align*} 
F(x) = 1- e^{-\frac{x}{3}}
\end{align*}$$

Ahora, al realizar el cálculo de la probabilidad de que la reducción del
tiempo que logra el catalizador sólido para la reacción química sea de
entre \(5\) y \(8\) minutos, y para ello, se realiza el siguiente
procedimiento, aplicando las propiedades de la función de distribución
acumulada para el caso continuo, ya presentadas en la
<a href="../../ProbabilidadeInferencia/PeIEClase08.html#función-de-distribución-acumulada-caso-continuo">Clase
08</a>. $$\begin{align*}
\mathbb{P}(5<X<8) &= F(8) - F(5) \\
                  &= \left(1- e^{-\frac{8}{3}}\right) - \left(1- e^{-\frac{5}{3}}\right)  \\
                  &=  e^{-\frac{5}{3}} - e^{-\frac{8}{3}} \\
                  &=  0.1888756 + 0.06948345 \\
                  &=  0.1193922
\end{align*}$$ Es decir, que se tendrá un \(11.93\%\) de probabilidad,
de que el catalizador sólido, reduzca el tiempo de la reacción química
en un valor entre \(5\) y \(8\) minutos.
</p>
</main>

## Relación entre la distribución Exponencial y el proceso Poisson

Suponga que el número de eventos que ocurren en un intervalo de tiempo
`$t$`, tiene una distribución Poisson con parámetro `$\lambda$` y que el
número ocurrencias en intervalos de tiempo distintos son independientes
entre si. Entonces se tendrá que la distribución del tiempo transcurrido
entre dos eventos de Poisson sucesivos es Exponencial con parámetro
`$\beta = \frac{t}{\lambda}$`.

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
En cierta ciudad el número de automoviles que excede el límite de
velocidad de \(80_{km/h}\), es un intervalo de media hora, es una
variable aleatoria Poisson con media de \(8.4\) automóviles. ¿Cuál es la
probabilidad de que el tiempo de espera sea menor a \(5\) minutos para
que el próximo automóvil exceda el limite de velocidad de
\(80_{km/h}\)?.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
En este caso, nos dicen que el número de automoviles que excede el
límite de velocidad en <strong>media hora</strong> se distribuye Poisson
con parámetro \(\lambda=\mathbb{E}(X)=8.4\), pero nos preguntan por la
probabilidad de que el tiempo de espera sea menor de \(5\) minutos hasta
que transite el próximo automovil. Es decir nos preguntan, por una
variable aleatoria diferente a la inicialmente planteada, la cual puede
asumirse Exponencial, debido a que nos preguntan por un solo suceso, es
decir “el próximo automóvil”. <br> Para calcular el parámetro de la
distribución Exponencial, podemos emplear la relación que hay entre la
distribución Exponencial y el proceso Poisson, contruyendo una regla de
tres, para realizar el cálculo, tal que $$\begin{align*}
8.4_{Autos} &- 30_{min}\\
1_{Auto} &- a
\end{align*}$$ Lo anterior significa que si, \(8.4\) automóviles
transitan en promedio en \(30\) minutos, entonces \(1\) automovil,
transitará en promedio en cuanto tiempo?. Al resolver la regla de tres,
tenemos que $$\begin{align*}
a = \frac{1_{Auto} \times 30_{min}}{8.4_{Autos}} = 3.57_{min}
\end{align*}$$ El tiempo promedio que tardar en pasar un solo auto movil
es de \(3.57\), es decir, El parámetro \(\beta\) de la distribución
Exponencial es igual a \(3.57\). Y ahora, como ya conocemos el parámetro
de la distribución Exponencial, podemos realizar el cálculo de la
probabilidad de que el tiempo que tarda en hasta que el próximo
automóvil exceda el límite de velocidad sea menor a \(5\) minutos.
$$\begin{align*}
\mathbb{P}(Y<5) & = F(5) \\
                & = 1 - e^{-\frac{5}{3.57}}\\
                & = 1 - 0.2464589 \\
                & = 0.7535411
\end{align*}$$ Es decir, existe una probabilidad de \(75.35\%\), de que
el tiempo de espera sea menor a \(5\) minutos para que el próximo
automóvil exceda el limite de velocidad.
</p>
</main>
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
Suponga que el tiempo entre llegadas de taxis a un acopio del Metro,
tiene una distribución exponencial con media de \(3\) minutos. ¿Cuál es
la probabilidad de que en media hora lleguen más de \(15\) taxis?.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso, se inicia hablando del tiempo que hay entre la llegada de
dos taxis a un acopio, es decir, el tiempo que tarda en llegar el
próximo taxi a un acopio. Y nos dicen que este tiempo se distribuye
exponencial con parámetro \(\beta=\mathbb{E}(X)=3_{min}\). Pero nos
preguntan por el número de llegadas al acopio durante media hora, es
decir, nos preguntan, por una variable aleatoria diferente a la
inicialmente planteada, la cual puede asumirse Poisson, debido a que nos
preguntan por el número de sucesos en un periodo de tiempo.

Para calcular el parámetro de la distribución Poisson, podemos emplear
la relación que hay entre la distribución Exponencial y el proceso
Poisson, contruyendo una regla de tres, para realizar el cálculo, tal
que $$\begin{align*}
3_{min} &- 1_{taxi}\\
30_{min} &- b
\end{align*}$$ Lo anterior significa que si, en promedio tarda \(3\)
minutos en llegar \(1\) taxi al acopio, entonces, cuantos taxis llegarán
al acopio en un intervalo de \(30\) minutos?. Al resolver la regla de
tres, tenemos que $$\begin{align*}
b = \frac{1_{taxi} \times 30_{min}}{3_{min}} = 10_{taxis}
\end{align*}$$ El número promedio de taxis que llegan al acopio en un
intervalo de \(30\) minutos será de \(10\) taxis, es decir, el parámetro
\(\lambda\) de la distribución Poisson es igual a \(10\). Y ahora, como
ya conocemos el parámetro de la distribución Poisson, podemos realizar
el cálculo de la probabilidad de que lleguen más de \(15\) taxis en
media hora. $$\begin{align*}
\mathbb{P}(X>15) & = 1 - \mathbb{P}(X\leq15)  \\
                 & = 1 - \sum_{0}^{15} \frac{e^{-10} 10^{x}}{x!}\\
                 & = 1 - 0.9512596 \\
                 & = 0.0487404
\end{align*}$$ Es decir, existe una probabilidad del \(4.87\%\), de que
en un intervalo de media hora lleguen más de \(15\) taxis al acopio del
Metro.
</p>
</main>

## Propiedad de carencia de memoria

Suponga que `$X$` es una variable aleatoria tal que
`$X\sim Exp(\beta)$`, entonces sean dos reales positivos `$a$` y `$b$`,
entonces se puede probar que

1.  `$\mathbb{P}(X\geq a+b | x \geq b) = \mathbb{P}(X\geq a)$`
2.  `$\mathbb{P}(X\leq a+b | x \geq b) = \mathbb{P}(X\leq a)$`

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
Suponga que se realiza un estudio en un Call Center, y se encuentra que
el tiempo promedio entre llamadas es de \(2\) minutos. Entonces, si han
pasado ya \(2\) minutos y no ha entrado ninguna llamada al Call Center,
cuál es la probabilidad de que tarde al menos \(1.5\) minutos más en
entrar la próxima llamada?.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
En este ejercicio, nos preguntan por una probabilidad condicional,
debido a que nos dicen que ya han pasado \(2\) minutos y no ha entrado
ninguna llamada, y nos preguntan por la probabilidad de que la próxima
llamada tarde menos de \(1.5\) minutos más. Al aplicar el procedimiento
para resolver la probabilidad condicional se tendrá que $$\begin{align*}
\mathbb{P}(X\geq3.5|X>1.5) & = \frac{\mathbb{P}(X\geq3.5 \cap X>1.5)}{\mathbb{P}(X>1.5)}  \\
                        & = \frac{\mathbb{P}(X\geq3.5)}{\mathbb{P}(X>1.5)} \\
                        & = \frac{\mathbb{P}(X\geq3.5)}{\mathbb{P}(X>1.5)} \\
                        & = \frac{1 - \mathbb{P}(X<3.5)}{1 - \mathbb{P}(X\leq1.5)} \\
                        & = \frac{1 - F(3.5)}{1 - F(1.5)} \\
                        & = \frac{1 - \left(1 - e^{-\frac{3.5}{2}}\right)}{1 - \left(1 - e^{-\frac{1.5}{2}}\right)} \\
                        & = \frac{e^{-\frac{3.5}{2}}}{e^{-\frac{1.5}{2}}} \\
                        & = 0.3678794
\end{align*}$$ Ahora, si empleamos la propiedad de carencia de memoria
de la distribución Exponencial, se tendrá que, dicha probabilidad peude
resolverse de forma más rápida, de la forma $$\begin{align*}
\mathbb{P}(X\geq3.5|X>1.5) & = \mathbb{P}(X\geq2 + 1.5 |X>1.5) \\
                        & = \mathbb{P}(X\geq2) \\
                        & = 1 - \mathbb{P}(X<2) \\
                        & = 1 - F(2) \\
                        & = 1 - \left(1 - e^{-\frac{2}{2}}\right) \\
                        & = e^{-1} \\
                        & = 0.3678794
\end{align*}$$ Obteniendo el mismo resultado. Ahora la interpretación
del resultado es que, si ya han pasado \(2\) minutos y no ha entrado
ninguna llamada al Call Center, la probabilidad de que tarde almenos
\(1.5\) minutos más en entrar la próxima llamada será de \(36.78\%\).
</p>
</main>