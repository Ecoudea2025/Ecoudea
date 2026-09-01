---
title: "Clase 16"
course: "estadistica-i"
order: 20
classType: "clase"
description: "Distribuciones de probabilidad discreta: - Distribución Geométrica - Distribución Binomial Negativa - Distribución Poisson"
math: true
bibliography: "../../referencias.bib"
---

Distribuciones de probabilidad discretas
----------------------------------------

### Experimento Binomial Negativo

Consideremos un experimento con las mismas propiedades de un experimento
binomial, solo que en este caso, las pruebas se repetirán hasta que
ocurra un número fijo de éxitos. Por lo tanto en vez de encontrar la
probabilidad de `$X$` éxitos en `$n$` pruebas, donde `$n$` es fija,
ahora nos interesa la probabilidad de que ocurra el `$k$`-ésimo éxito en
la `$X$`-ésima prueba.

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
Experimentos Binomial Negativo, debido a que cumplen las propiedades de
un experimento binomial, es decir, las \(4\) condiciones propuestas en
el
<a href="../../EstadisticaI/EstIClase12.html#proceso-bernoulli">Proceso
Bernoulli</a>.
</p>
<ul>
<li>
Tirar una moneda al aire, hasta obtener la primera cara.
</li>
<li>
Contar el número de carros que pasan por debajo de un puente, hasta que
pasen \(5\) carros azules.
</li>
<li>
Comprar empanada hasta encontrar la segunda refritas.
</li>
<li>
Seleccionar estudiantes de la Universidad, hasta encontrar el primero
que nació por fuera de Antioquia.
</li>
</ul>
</main>

### Distribución Geométrica

Sea `$X$` el número de ensayos necesarios para generar un éxito
(`$k=1$`), entonces se dice que `$X\sim g(p)$` si su función de
probabilidad es de la forma

$$\begin{align*}p(x) = p(1-p)^{x-1} \quad \quad x = 1,2,\ldots\end{align*}$$


#### Media y Varianza Geométrica

Si `$X\sim g(p)$`, entonces se puede probar que la media y varianza de
la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=\frac{1}{p} \quad \quad Var(X)=\frac{1-p}{p^2}\end{align*}$$


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
Suponga que por experiencia se sabe que \(1\) de cada \(5\) personas que
solicitan la Visa Americana en la embajada de Estados Unidos en la
Ciudad de Bogotá, es rechazada. Basados en lo anterior,
</p>
<ol>
<li>
Cuál es la probabilidad de que más de \(3\) personas deban solicitar la
Visa hasta que la Embajada otorgue la primera Visa?.
</li>
<li>
Cuál es el número promedio y desviación estándar de personas que deben
solicitar la Visa hasta que la Embajada de Estados Unidos decida otorgar
la primera Visa Americana?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En este caso nos preguntan, por la probabilidad de que más de \(3\)
personas deban presentarse a la embajada de Estados Unidos, hasta que la
Embajada de Estados Unidos otorgue la primera Visa Americana, esto es
$$\begin{align*}
\mathbb{P}(X>3)
\end{align*}$$

Donde \(X\): representa el número de solicitantes que se presentan para
solicitar la Visa. Entonces, como estamos en una situación en la cual
nos preguntan por el número de ensayos que hay que realizar, hasta
obtener \(1\) éxito, estamos en una situación asociada a una
distribución Geométrica, la cual tiene la estructura $$\begin{align*}
p(x) = p(1-p)^{x-1} \quad \quad x = 1,2,\ldots
\end{align*}$$ En donde se sabe por experiencia que \(1\) de cada \(5\)
personas que solicitan la Visa es rechazada, y por tanto, como nuestro
éxito está asociado a que se otorgue la Visa, se tendrá que a \(4\) de
cada \(5\) personas que solicitan la Visa, se les otorga de forma
satisfactoriamente, es decir que al aplicar la definición de frecuencia
relativa, tendremos que la proporción \(p\), estará dada por
$$\begin{align*}
p &= \frac{\text{# éxitos}}{\text{total Ensayos}} \\
  &= \frac{4}{5} \\
  &= 0.80
\end{align*}$$

Ahora, al emplear la función de distribución Geométrica con \(p=0.80\),
tendremos que la probabilidad de interés estará dada por

$$\begin{align*}
\mathbb{P}(X>3) &= 1 - \mathbb{P}(X\leq 3) \\
                &= 1 - \sum_{x=1}^3 0.80(1-0.80)^{x-1} \\
                &= 1 - \left(0.80(0.20)^{1-1} + 0.80(0.20)^{2-1} + 0.80(0.20)^{3-1}\right) \\
                &= 1 - (0.80 + 0.16 + 0.032) \\
                &= 1 - 0.992 \\
                &= 0.008
\end{align*}$$

En consecuencia, se tendrá un \(0.8\%\) de probabilidad, de que más de
\(3\) personas deban solicitar la Visa Americana, hasta que la embajada
de Estados Unidos decida otorgar la primera.
</li>
<li>

En esta ocasión estamos interesados en conocer el promedio y desviación
estándar del número de personas que deben presentarse a la embajada de
Estados Unidos, hasta que éstos le otorguen la primera Visa Americana. Y
para ello podemos emplear la formula de la esperanza matemática, de la
distribución Geométrica, para realiza el cálculo

$$\begin{align*}
\mathbb{E}(X)=\frac{1}{p}
\end{align*}$$

Entonces, como \(4\) de \(5\) personas que se presentan a la embajada,
obtienen la Visa, entonces se tendrá que la proporción \(p=0.80\), y en
consecuencia,

$$\begin{align*}
\mathbb{E}(X) &= \frac{1}{0.80} \\
              &= 1.25
\end{align*}$$

lo cual significa, que en promedio deberán presentarse \(1.25\)
personas, hasta que la embajada de Estados Unidos decida otorgar la
primera Visa Americana. <br> <br> Ahora, para completar la
interpretación anterior, realizaremos el cálculo de la desviación
estándar del número de personas que deben presentarse a la embajada de
Estados Unidos hasta que éstos ortorguen la primera Visa, en donde,
requerimos calcular inicialmente la Varianza del número de personas, tal
que, al emplear la definición de Varianza para el caso de una
distribución Geométrica, se tendrá que $$\begin{align*}
Var(X) &= \frac{1-p}{p^2} \\
       &= \frac{1-0.8}{0.8^2} \\
       &= 0.3125
\end{align*}$$ y con este valor calculamos la desviación estándar,
mediante la ecuación $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.3125} \\
      &= 0.559017
\end{align*}$$

Y por tanto se tendrá que en promedio \(1.25\) personas con una
desviación estándar de \(0.559017\) personas, deben presentarse a la
embajada de Estados Unidos, con el fin de que éstos decidan otorgar la
primera Visa Americana.
</li>
</ol>
</main>

### Distribución Binomial Negativa

Sea `$X$` el número de ensayos necesarios para generar `$k$` éxitos en
un experimento Binomial Negativo, entonces se dice que
`$X\sim b^*(k,p)$` si su función de probabilidad es de la forma

$$\begin{align*}p(x) = \left(\begin{array}{c}x-1\\ k-1\end{array}\right)p^k(1-p)^{x-k} \quad \quad x=k, k+1, \ldots\end{align*}$$


#### Media y Varianza Binomial Negativa

Si `$X\sim b^*(k,p)$`, entonces se puede probar que la media y varianza
de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=\frac{k}{p} \quad \quad Var(X)=k\frac{(1-p)}{p^2}\end{align*}$$


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
Suponga que por experiencia se sabe que \(1\) de cada \(5\) personas que
solicitan la Visa Americana en la embajada de Estados Unidos en la
Ciudad de Bogotá, es rechazada. Basados en lo anterior,
</p>
<ol>
<li>
Cuál es la probabilidad de que más de \(10\) pero a lo más \(15\)
personas deban solicitar la Visa Americana, para que la Embajada otorgue
la octava Visa?.
</li>
<li>
Cuál es el número promedio y desviación estándar de personas que deben
solicitar la Visa Americana hasta que la Embajada de Estados Unidos
decida otorgar la décima Visa Americana?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En este ejercicio, nos piden la probabilidad de que más de \(10\) pero a
lo más \(15\) personas deban presentarse a la embajada de Estados
Unidos, hasta que la Embajada decida otorgar la octava Visa Americana,
esto es $$\begin{align*}
\mathbb{P}(10<X\leq 15)
\end{align*}$$

Donde \(X\): representa el número de personas que se presentan a la
embajada de Estados Unidos para solicitar la Visa, hasta que éstos
decidan otorgar la octava Visa. Entonces, como estamos en una situación
en la cual nos preguntan por el número de ensayos que hay que realizar,
hasta obtener \(8\) éxitos, estamos en una situación asociada a una
distribución Binomial Negativa, la cual tiene la estructura
$$\begin{align*}
p(x) = \left(\begin{array}{c}x-1\\ k-1\end{array}\right)p^k(1-p)^{x-k} \quad \quad x=k, k+1, \ldots
\end{align*}$$

en donde, \(k=8\): representa el número de visas otorgadas por la
embajada de Estados Unidos. Entonces como se sabe por experiencia que
\(1\) de cada \(5\) personas que solicitan la Visa es rechazada, se
tendrá que a \(4\) de cada \(5\) personas que solicitan la Visa, se les
otorga ésta de forma satisfactoriamente, es decir que al aplicar la
definición de frecuencia relativa, tendremos que la proporción \(p\),
estará dada por $$\begin{align*}
p &= \frac{\text{# éxitos}}{\text{total Ensayos}} \\
  &= \frac{4}{5} \\
  &= 0.80
\end{align*}$$

Ahora, al emplear la función de distribución Binomial Negativa con
\(p=0.80\) y \(k=8\) tendremos que la probabilidad de interés estará
dada por

$$\begin{align*}
\mathbb{P}(10<X\leq 15) &= \sum_{x=11}^{15} \left(\begin{array}{c}x-1\\ 8-1\end{array}\right)(0.80)^8(1-0.80)^{x-8} \\
                        &= \left(\begin{array}{c}11-1\\ 8-1\end{array}\right)(0.80)^8(1-0.80)^{11-8} + \ldots + \left(\begin{array}{c}15-1\\ 8-1\end{array}\right)(0.80)^8(1-0.80)^{15-8} \\
                        &= 0.3179607
\end{align*}$$

En consecuencia, se tendrá un \(31.79\%\) de probabilidad, de que más de
\(10\) pero como máximo \(15\) personas deban solicitar la Visa
Americana, hasta que la embajada de Estados Unidos decida otorgar la
octava Visa.
</li>
<li>

En esta ocasión estamos interesados en conocer el promedio y desviación
estándar del número de personas que deben presentarse a la embajada de
Estados Unidos, hasta que éstos decidan otorgar la octava Visa
Americana. Y para ello podemos emplear la formula de la esperanza
matemática, de la distribución Binomial negativa, tal que
$$\begin{align*}
\mathbb{E}(X)=\frac{k}{p}
\end{align*}$$

Entonces, como \(4\) de \(5\) personas que se presentan a la embajada
obtienen la Visa, estamos interesados en el octavo éxito, entonces se
tendrá que \(p=0.80\) y \(k=8\), con lo cual obtendremos un número
promedio de personas igual a

$$\begin{align*}
\mathbb{E}(X) &= \frac{8}{0.80} \\
              &= 10
\end{align*}$$

Ahora, para calcular la desviación estándar, realizamos primero el
cálculo de la varianza para el número de personas que deben presentarse
a la embajada, hasta que éstos decidan otorgar la octava visa, tal que
$$\begin{align*}
Var(X) &= k\frac{(1-p)}{p^2} \\
       &= 8\left(\frac{1-0.8}{0.8^2}\right) \\
       &= 8(0.3125) \\
       &= 2.5
\end{align*}$$ y basados en este resultado, procedemos con el cálculo de
la desviación estándar, mediante la ecuación $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{2.5} \\
      &= 0.559017
\end{align*}$$

De lo anterior se tiene que en promedio deberán presentarse \(10\)
personas a la embajada Americana, con una desviación estándar de
\(0.559017\), para que estos otorguen \(8\) Visas.
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

3.  La probabilidad de que ocurra más de un resultado en un intervalo de
    tiempo corto o región pequeña es insignificante.

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

#### Media y Varianza Poisson

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