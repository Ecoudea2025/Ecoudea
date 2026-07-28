---
title: "Clase 10"
course: "probabilidad-inferencia"
order: 14
classType: "clase"
description: "Distribuciones de probabilidad discreta: - Ensayos Bernoulli. - Distribución binomial. - Distribución Poisson."
math: true
bibliography: "../../referencias.bib"
---

## Distribuciones de probabilidad discreta

### Proceso Bernoulli

Un proceso Bernoulli es aquel que cumple

1.  El experimento consta de ensayos repetidos bajo las mismas
    condiciones.
2.  Cada ensayo produce un resultado que se puede clasificar como éxito
    o fracaso.
3.  La probabilidad de éxito se denota por `$p$` y permanece constante
    de un ensayo a otro.
4.  Los ensayos repetidos son independientes entre si.

<button id="Show1" class="btn btn-secondary">
Mostrar Ejemplo
</button>
<button id="Hide1" class="btn btn-info">
Ocultar Ejemplo
</button>
<main id="botoncito1">
<h3 data-toc-skip>
Ejemplo
</h3>
<p>
Los siguientes, son algunos ejemplos de casos que pueden considerarse
como Procesos Bernoulli, debido a que cumplen las \(4\) condiciones
propuestas anteriormente.
</p>
<ul>
<li>
Tirar una moneda al aire y observar si sale cara o sello.
</li>
<li>
Mirar el próximo carro que pasa por debajo de un puente, y observar si
es o no de color azul.
</li>
<li>
Comprar una empanada y determinar si tiene buen sabor o mal sabor.
</li>
<li>
Seleccionar un estudiante de la Universidad, y determinar si éste nació
o no en Antioquia.
</li>
</ul>
</main>

### Ensayo de Bernoulli

Si la probabilidad de éxito de un experimento es `$p$`, entonces la
probabilidad de fallo debe ser `$1-p$` y la función de probabilidad de
la variable aleatoria `$X\sim Be(p)$` para un ensayo Bernoulli será

$$\begin{align*}p(x) = p^x(1-p)^{1-x} \quad \quad x=0,1\end{align*}$$


#### Teorema

Si `$X\sim Be(p)$`, entonces se puede probar que la media y la varianza
de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=p \quad \quad Var(X)=p(1-p)\end{align*}$$


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
Suponga que en un estudio se encontró que \(2\) de cada \(5\)
estudiantes no desea tomar clases virtuales. Si se selecciona
aleatoriamente un estudiante, cuál es la probabilidad de que éste desee
tomar clases virtuales, y determine su media y desviación estándar.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en la variable \(X\), que representa el
número de estudiantes que desean tomar clases virtuales, en donde
sabemos que si, \(2\) de cada \(5\) no quieren tomar clases virtuales,
entonces se tendrá que \(3\) de cada \(5\) si desean tomar clases
virtuales. Por tanto al aplicar la definición de frecuencia relativa se
tiene que

$$\begin{align*}
p &= \frac{\text{Número de éxitos}}{\text{Número de muestras}}\\
  &= \frac{3}{5} \\
  &= 0.6
\end{align*}$$ siendo \(p\) la probabilidad de que un estudiante desee
tomar clases virtuales.

Ahora, la probabilidad de que se seleccione un estudiante al azar, y
éste desee tomar clases virtuales será $$\begin{align*}
\mathbb{P}(X = 1) &= p(1-p)^{1-x} \\
                  &= 0.6(0.4)^{1-1} \\
                  &= 0.6(0.4)^0 \\
                  &= 0.6
\end{align*}$$

es decir, que la probabilidad de que el estudiante seleccionado desee
tomar clases virtuales será del \(60\%\).

Ahora, para calcular la desviación estándar se requiere calcular
inicialmente la varianza de la variable aleatoria, la cual está dada por
$$\begin{align*}
Var(X) &= p(1-p) \\
       &= 0.6(0.4) \\
       &= 0.24
\end{align*}$$

y a partir de éste valor, se tendrá que la desviación estándar es igual
a $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.24} \\
      &= 0.4898979
\end{align*}$$ Entonces, como el valor esperado de un proceso Bernoulli
es igual a \(p\), esto es $$\begin{align*}
\mathbb{E}(X) &= p \\
              &= 0.6
\end{align*}$$ Por tanto, al seleccionar un solo estudiante, se espera
que \(0.6\) estudiantes respondan que desean tomar clases virtuales, con
una desviación estándar de \(0.489\).
</p>
</main>

### Distribución Binomial

Si `$X$` es la variable aleatoria del número de éxitos de `$n$` ensayos
de Bernoulli, con probabilidad de éxito `$p$`, entonces se dice que
`$X\sim b(n,p)$` tal que

$$\begin{align*}p(x) = \left(\begin{array}{c}n\\ x\end{array}\right)p^x(1-p)^{n-x} \quad \quad x=0,1,\ldots,n\end{align*}$$


**Nota:** Esta distribución es usada cuando se realiza muestreo con
reemplazo o en poblaciones infinitas en donde es posible **suponer que
la probabilidad de éxito `$p$` es la misma** en cada ensayo Bernoulli.

#### Teorema

Si `$X\sim b(n,p)$`, entonces se puede probar que la media y varianza de
la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=np \quad \quad Var(X)=np(1-p)\end{align*}$$


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
Suponga que en un estudio se encontró que \(2\) de cada \(5\)
estudiantes no desea tomar clases virtuales. Si se selecciona
aleatoriamente \(20\) estudiantes, calcule
<ol>
<li>
Cuál es la probabilidad de que no más de \(3\) estudiantes deseen tomar
clases virtuales?
</li>
<li>
Cuál es la probabilidad de que no menos de \(6\) pero menos de \(12\)
deseen tomar clases virtuales?
</li>
<li>
Cuál es el número promedio y desviación estándar del número de
estudiantes que desean tomar clases virtuales?.
</li>
</ol>
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en la variable \(X\), que representa el
número de estudiantes que desean tomar clases virtuales, en donde
sabemos que si, \(2\) de cada \(5\) no quieren tomar clases virtuales,
entonces se tendrá que \(3\) de cada \(5\) si desean tomar clases
virtuales. Por tanto al aplicar la definición de frecuencia relativa se
tiene que

$$\begin{align*}
p &= \frac{\text{Número de éxitos}}{\text{Número de muestras}} \\
  &= \frac{3}{5} \\
  &= 0.6
\end{align*}$$ siendo \(p\) la probabilidad de que un estudiante desee
tomar clases virtuales.
</p>
<ol>
<li>
En este caso, estamos interesados en calcular la probabilidad de que no
más de \(3\) estudiantes deseen tomar clases virtuales, lo cual puede
representarse mediante la siguiente probabilidad $$\begin{align*}
P(X\leq 3) &= \sum_{x=0}^3 \left(\begin{array}{c}20\\ x\end{array}\right)0.6^x(1-0.6)^{20-x} \\
           &= \left(\begin{array}{c}20\\ 0\end{array}\right)0.6^0(0.4)^{20-0} + \ldots + \left(\begin{array}{c}20\\ 3\end{array}\right)0.6^3(0.4)^{20-3} \\
           &= 0.00000001099512 + 0.0000003298535 + 0.000004700412 + 0.00004230371 \\
           &= 0.00004734497
\end{align*}$$ Es decir, la probabilidad de que como máximo \(3\)
estudiantes de los \(20\) seleccionados, deseen tomar clases virtuales,
es del \(0.0047\%\).
</li>
<li>
Ahora, se tiene interés en conocer la probabilidad de que no menos de
\(6\) pero menos de \(12\) deseen tomar clases virtuales. En este caso,
la probabilidad asociada puede calcularse de la siguiente manera.
$$\begin{align*}
P(6 \leq x < 12) &= \sum_{x=6}^{11} \left(\begin{array}{c}20\\ x\end{array}\right)0.6^x(1-0.6)^{20-x} \\
           &= \left(\begin{array}{c}20\\ 6\end{array}\right)0.6^6(0.4)^{20-6} + \ldots + \left(\begin{array}{c}20\\ 11\end{array}\right)0.6^{11}(0.4)^{20-11} \\
           &= 0.4027898
\end{align*}$$ Es decir que, la probabilidad de que como mínimo \(6\)
pero menos de \(12\) estudiantes deseen tomar clases virtuales de los
\(20\) seleccionados, es del \(40.28\%\).
</li>
<li>

Finalmente, se tiene interés en conocer cual será el número promedio y
desviación estándar, de estudiantes que desean tomar clases virtuales,
cuando se realiza la selección aleatoria de \(20\). Al aplicar la
formular de esperanza matemática para la distribución binomial, se tiene
que el valor esperado de estudiantes que desean tomar clases virtuales
es de $$\begin{align*}
\mathbb{E}(X) & = np \\
              & = 20(0.6)\\
\mathbb{E}(X) & = 12
\end{align*}$$

Se procede a realizar el cálculo de la varianza para poder calcular la
desviación estándar, del número de estudiantes que desean tomar clases
virtuales, tal que $$\begin{align*}
Var(X) &= np(1-p) \\
       &= 20(0.6)(1-0.6)\\
Var(X) & = 4.8
\end{align*}$$ y con este valor, se procede a calcular la desviación
estándar $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{Var(4.8)} \\
Sd(X) & = 2.19089
\end{align*}$$ De lo anterior se tiene que, al realizar la selección
aleatoria de \(20\) estudiantes, es espera que \(12\) estudiantes desean
tomar clases virtuales, con una desviación estándar de \(2.19\)
estudiantes.
</li>
</ol>
</main>

### Proceso Poisson

Un proceso Poisson es aquel que cumple

1.  El número de resultados que ocurren en un intervalo o región
    específica es independiente del número que ocurre en cualquier otro
    intervalo de tiempo o región del espacio disjunto.
2.  La probabilidad de que ocurra un solo resultado durante un intervalo
    de tiempo corto o región pequeña es proporcional a la longitud del
    intervalo o al tamaño de la región, y no depende del número de
    resultados que ocurren por fuera de este intervalo de tiempo o
    región.
3.  La probabilidad de que ocurra más de un resultado en tal intervalo o
    región pequeña es insignificante.

<button id="Show4" class="btn btn-secondary">
Mostrar Ejemplo
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejemplo
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejemplo
</h3>
<ul>
<li>
El número de carros que transitan por una glorieta en dos horas.
</li>
<li>
El número de estudiantes que entrar a la universidad en un día.
</li>
<li>
Mirar el número de carros que pasa por debajo de un puente, en \(5\)
minutos.
</li>
<li>
El número de empanada que se venden en media hora.
</li>
<li>
El número de resaltos para reducción de velocidad que se encuentran en
la carretera en un kilómetro.
</li>
</ul>
</main>

### Distribución Poisson

El número de sucesos que ocurren en un intervalo de tiempo o región
específica, es una variable aleatoria `$X$` con distribución de
probabilidad Poisson, tal que

$$\begin{align*}p(x) = \frac{e^{-\lambda}\lambda^x}{x!} \quad \quad x=0,1,\ldots\end{align*}$$

donde `$\lambda$` es el parámetro de la distribución y representa el
número promedio de sucesos por unidad de tiempo o región específica.

#### Teorema

Si `$X\sim P(\lambda)$` entonces se puede probar que la media y varianza
de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=\lambda \quad \quad Var(X)=\lambda\end{align*}$$


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
Los huecos en las carreteras pueden ser un problema grave y requieren de
reparación constante con un tipo específico de mezcla de concreto. La
experiencia sugiere que hay en promedio \(1.5\) huecos por cada dos
kilómetros recorridos, después de cierta cantidad de uso. Si se supone
que \(X\) representa el número de huecos que hay en la carretera
<ol>
<li>
Cuál es la probabilidad de que no aparezca más de un hueco en la
carretera en un tramo de dos kilómetros?
</li>
<li>
Cuál es la probabilidad de que aparezca más de hueco en un tramo de un
kilómetro?
</li>
<li>
Cuál es el número promedio y desviación estándar del número de huecos
que se encuentran en \(5\) kilómetros?.
</li>
</ol>
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
En este caso nos dicen que nuestra variable aleatorias es \(X\) el
número de huecos que se encuentran en la carretera, y que en promedio se
encuentran \(1.5\) huecos cada dos kilómetros.
</p>
<ol>
<li>
Basados en lo anterior, nos preguntan por la probabilidad de que no
aparezca más de un hueco en la carretera en un tramo de dos kilómetros.
Es decir, nos preguntan por la probabilidad de que aparezca como máximo
\(1\) hueco en la carretera en un tramo de dos kilómetros. En este caso
se tendrá la siguiente probabilidad $$\begin{align*}
P(X\leq 1) &= \sum_{x=0}^1 \frac{e^{-1.5}1.5^x}{x!} \\
           &= \frac{e^{-1.5}1.5^0}{0!} + \frac{e^{-1.5}1.5^1}{1!} \\\\
           &= 0.2231302 + 0.3346952 \\
           &= 0.5578254
\end{align*}$$ Es decir, la probabilidad de que no aparezca más de un
hueco en la carretera en el tramo de dos kilómetros es del \(55.78\%\).
</li>
<li>

Ahora, se tiene interés en conocer la probabilidad de que aparezca más
de un hueco en un tramo de un kilómetro. En este caso debe notarse que
se cambió la unidad de medida, en donde en lugar de dos kilómetros se
habla de un kilómetro.<br> <br> Debido a ésto, será necesario actualizar
nuestro parámetro \(\lambda\) mediante el empleo de una regla de \(3\),
de la siguiente manera. $$\begin{align*}
 2_{\text{km}} &- 1.5_{\text{huecos}} \\
 1_{\text{km}} &- \lambda
\end{align*}$$ esto es, $$\begin{align*}
 \lambda &= \frac{1.5_{\text{huecos}} \times 1_{\text{km}}}{2_{\text{km}}} \\
 \lambda &= 0.75_{\text{huecos}}
\end{align*}$$ Es decir, que en un tramo de un kilómetro ocurren
\(0.75\) huecos en promedio. Conocido el valor del parámetro \(\lambda\)
para el tramo de un kilómetro, se procede a calcular la probabilidad de
que aparezca más de un hueco en el tramo de un kilómetro, tal que
$$\begin{align*}
 \mathbb{P}(X>1) = \sum_{x=2}^\infty \frac{e^{-0.75}0.75^x}{x!} \\
\end{align*}$$ En donde se aprecia que es una suma infinita, y en
consecuencia se procede a trabajar tal probabilidad por su complemento.
$$\begin{align*}
 \mathbb{P}(X>1) &= 1 - \mathbb{P}(X\leq1)  \\
                 &= 1 - \sum_{x=0}^1 \frac{e^{-0.75}0.75^x}{x!} \\
                 &= 1 - \frac{e^{-0.75}0.75^0}{0!} - \frac{e^{-0.75}0.75^1}{1!} \\
                 &= 1 - 0.4723666 - 0.3542749 \\
                 &= 0.1733585
\end{align*}$$

Es decir que, la probabilidad de que se encuentre más de \(1\) hueco en
un tramo de \(1\) kilómetro cuando se viaja por carretera, es del
\(17.33\%\).
</li>
<li>

Finalmente, se tiene interés en conocer cual será el promedio y
desviación estándar, del número de huecos que se encontrarán en la
carretera en el tramo de \(5\) kilómetro. En este caso, como se cambia
la unidad de medida de \(2\) kilómetros a \(5\) kilómetros, será
necesario recalcular el valor de \(\lambda\), ta que

$$\begin{align*}
 2_{\text{km}} &- 1.5_{\text{huecos}} \\
 5_{\text{km}} &- \lambda
\end{align*}$$ esto es, $$\begin{align*}
 \lambda &= \frac{1.5_{\text{huecos}} \times 5_{\text{km}}}{2_{\text{km}}} \\
 \lambda &= 3.75_{\text{huecos}}
\end{align*}$$

Ahora, al aplicar la formular de esperanza matemática para la
distribución Poisson, se tiene que el número esperado de huecos en \(5\)
kilómetros es de $$\begin{align*}
\mathbb{E}(X) & = \lambda \\
              & = 3.75\\
\end{align*}$$

Similarmente, se procede a realizar el cálculo de la varianza para poder
calcular la desviación estándar, del número de huecos que hay en un
tramo de \(5\) kilómetros $$\begin{align*}
Var(X) &= \lambda \\
       &= 3.75\\
\end{align*}$$ y con este valor, se procede a calcular la desviación
estándar $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{Var(3.75)} \\
Sd(X) & = 1.936492
\end{align*}$$ De lo anterior se tiene que, en el tramo de \(5\)
kilómetros de carretera, se espera encontrar \(3.75\) huecos, con una
desviación estándar de \(1.93\) huecos.
</li>
</ol>
</main>