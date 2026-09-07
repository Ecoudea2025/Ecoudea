---
title: "Clase 06"
course: "estadistica-y-probabilidades"
order: 9
classType: "clase"
description: "Variables aleatorias discretas - Varianza Distribuciones de probabilidad discretas: - Ensayo Bernoulli - Distribución Binomial - Distribución Hipergeométrica"
math: true
bibliography: "../../referencias.bib"
---

Variables aleatorias discretas
------------------------------

### Varianza caso discreto

Sea `$X$` una variable aleatoria con *fmp* `$p(x)$`, entonces si
`$m(X) = (X - \mathbb{E}(X))^2$`, se tendrá que la varianza de `$X$` que
se denota `$Var(X)$` o `$\sigma^2$` estará dada por

$$\begin{align*}Var(X) = \mathbb{E}\left[\left(X-\mathbb{E}(X)\right)^2\right]=\sum_x(x-\mathbb{E}(X))^2p(x)\end{align*}$$


Puede demostrarse a partir de la ecuación anterior, que una alternativa
para el cálculo de la `$Var(X)$` es de la forma


$$\begin{align*}Var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2\end{align*}$$


además, la raíz cuadrada de la varianza de `$X$` se llama desviación
estándar de `$X$`, se denota por `$Sd(X)$` o `$\sigma$` y se define como

$$\begin{align*}Sd(X) = \sqrt{Var(X)}\end{align*}$$


<button id="Show6" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito6">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga un experimento aleatorio que consta en consultar una familia
conformada por $3$ hijos, en donde, se asume que la probabilidad de
ser niño o niña es la misma. Entonces, si se define la variable
aleatoria $X$, el número de niñas que hay en la familia.
</p>
<ol>
<li>
Calcule la $Var(X)$.
</li>
<li>
Calcule la $Sd(X)$.
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<p>
Como la función de varianza es en sí, es una esperanza matemática,
entonces iniciamos con el cálculo de la función de masa de probabilidad
para el número de niñas que hay en una familia que posee $3$ hijos.
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
<ol>
<li>

A partir de la tabla anterior, se procede a realizar el cálculo de
$Var(X)$, a partir de los valores ya calculado de
$\mathbb{E}(X^2)=3$ y $\mathbb{E}(X)=1.5$, tal que

$$\begin{align*}
Var(X)&=\mathbb{E}(X^2) - \mathbb{E}(X)^2 \\
        &=3 - (1.5)^2 \\
        &=3 - 2.25 \\
        &=0.75
\end{align*}$$

Y en consecuencia, se tendrá que la varianza del número de niña que hay
en una familia que posee $3$ hijos es de $0.75$ hijos$^2$.
</li>
<li>

Basado en el valor de la varianza $Var(X)=0.75$, se procede a realizar
el cálculo de la desviación estándar de la variable aleatoria $X$,
$Sd(X)$, tal que

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.75} \\
      &= 0.8660
\end{align*}$$

Es decir, se tendrá que el número promedio de niñas que tiene una
familia que posee $3$ hijos es de $1.5$ niñas, con una desviación
estándar de $0.8660$ niñas.
</li>
</ol>
</main>

Distribuciones de probabilidad discretas
----------------------------------------

### Proceso Bernoulli

Un proceso Bernoulli es aquel que cumple

1.  El experimento consta de ensayos repetidos.

2.  Cada ensayo produce un resultado que se puede clasificar como éxito
    o fracaso.

3.  La probabilidad de éxito se denota por `$p$`, mientras que la
    probabilidad de fracaso se denota por `$q=1-p$`, y estas
    probabilidades permanecen constante de un ensayo a otro.

4.  Los ensayos repetidos son independientes.

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
como Procesos Bernoulli, debido a que cumplen las $4$ condiciones
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

Si la probabilidad de éxito de un experimento es `$p$`, entonces se
tendrá que la probabilidad de fallo será `$1-p$`, y por tanto, la
función de probabilidad de la variable aleatoria `$X\sim Be(p)$` de un
ensayo Bernoulli es

$$\begin{align*}p(x) = p^x(1-p)^{1-x} \quad \quad x=0,1\end{align*}$$


#### Media y Varianza Bernoulli

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
Suponga que en un estudio se encontró que $2$ de cada $5$
estudiantes no desea tomar clases virtuales. Si se selecciona
aleatoriamente un estudiante, cuál es la probabilidad de que éste desee
tomar clases virtuales, y determine su media y desviación estándar.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en la variable $X$, que representa el
número de estudiantes que desean tomar clases virtuales, en donde
sabemos que si, $2$ de cada $5$ no quieren tomar clases virtuales,
entonces se tendrá que $3$ de cada $5$ si desean tomar clases
virtuales. Por tanto al aplicar la definición de frecuencia relativa se
tiene que

$$\begin{align*}
p &= \frac{\text{Número de éxitos}}{\text{Número de muestras}} \\
  &= \frac{3}{5} \\
  &= 0.6
\end{align*}$$ siendo $p$ la probabilidad de que un estudiante desee
tomar clases virtuales.

Ahora, la probabilidad de que se seleccione un estudiante al azar, y
éste desee tomar clases virtuales será $$\begin{align*}
\mathbb{P}(X = 1) &= p(1-p)^{1-x} \\
                  &= 0.6(0.4)^{1-1} \\
                  &= 0.6(0.4)^0 \\
                  &= 0.6
\end{align*}$$

es decir, que la probabilidad de que el estudiante seleccionado desee
tomar clases virtuales será del $60\%$.

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
es igual a $p$, esto es $$\begin{align*}
\mathbb{E}(X) &= p \\
              &= 0.6
\end{align*}$$ Por tanto, al seleccionar un solo estudiante, se espera
que $0.6$ estudiantes respondan que desean tomar clases virtuales, con
una desviación estándar de $0.489$.
</p>
</main>

### Distribución Binomial

Si `$X$` es la variable aleatoria del número de éxitos de `$n$` ensayos
de Bernoulli, con probabilidad de éxito `$p$`, entonces se dice que
`$X\sim b(n,p)$` tal que

$$\begin{align*}f(x) = \left(\begin{array}{c}n\\ x\end{array}\right)p^x(1-p)^{n-x} \quad \quad x=0,1,\ldots,n\end{align*}$$


**Nota:** Esta distribución es usada cuando se realiza muestreo **con
reemplazo** o en poblaciones infinitas en donde es posible **suponer que
la probabilidad de éxito `$p$` es la misma** en cada ensayo Bernoulli.

#### Media y Varianza Binomial

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
Suponga que en un estudio se encontró que $2$ de cada $5$
estudiantes no desea tomar clases virtuales. Si se selecciona
aleatoriamente $20$ estudiantes, calcule
<ol>
<li>
Cuál es la probabilidad de que no más de $3$ estudiantes deseen tomar
clases virtuales?
</li>
<li>
Cuál es la probabilidad de que no menos de $6$ pero menos de $12$
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

En este caso estamos interesados en la variable $X$, que representa el
número de estudiantes que desean tomar clases virtuales, en donde
sabemos que si, $2$ de cada $5$ no quieren tomar clases virtuales,
entonces se tendrá que $3$ de cada $5$ si desean tomar clases
virtuales. Por tanto al aplicar la definición de frecuencia relativa se
tiene que

$$\begin{align*}
p &= \frac{\text{Número de éxitos}}{\text{Número de muestras}} \\
  &= \frac{3}{5}\\ 
  &= 0.6
\end{align*}$$ siendo $p$ la probabilidad de que un estudiante desee
tomar clases virtuales.
</p>
<ol>
<li>
En este caso, estamos interesados en calcular la probabilidad de que no
más de $3$ estudiantes deseen tomar clases virtuales, lo cual puede
representarse mediante la siguiente probabilidad $$\begin{align*}
P(X\leq 3) &= \sum_{x=0}^3 \left(\begin{array}{c}20\\ x\end{array}\right)0.6^x(1-0.6)^{20-x} \\
           &= \left(\begin{array}{c}20\\ 0\end{array}\right)0.6^0(0.4)^{20-0} + \ldots + \left(\begin{array}{c}20\\ 3\end{array}\right)0.6^3(0.4)^{20-3} \\
           &= 0.00000001099512 + 0.0000003298535 + 0.000004700412 + 0.00004230371 \\
           &= 0.00004734497
\end{align*}$$ Es decir, la probabilidad de que como máximo $3$
estudiantes de los $20$ seleccionados, deseen tomar clases virtuales,
es del $0.0047\%$.
</li>
<li>
Ahora, se tiene interés en conocer la probabilidad de que no menos de
$6$ pero menos de $12$ deseen tomar clases virtuales. En este caso,
la probabilidad asociada puede calcularse de la siguiente manera.
$$\begin{align*}
P(6 \leq x < 12) &= \sum_{x=6}^{11} \left(\begin{array}{c}20\\ x\end{array}\right)0.6^x(1-0.6)^{20-x} \\
           &= \left(\begin{array}{c}20\\ 6\end{array}\right)0.6^6(0.4)^{20-6} + \ldots + \left(\begin{array}{c}20\\ 11\end{array}\right)0.6^{11}(0.4)^{20-11} \\
           &= 0.4027898
\end{align*}$$ Es decir que, la probabilidad de que como mínimo $6$
pero menos de $12$ estudiantes deseen tomar clases virtuales de los
$20$ seleccionados, es del $40.28\%$.
</li>
<li>

Finalmente, se tiene interés en conocer cual será el número promedio y
desviación estándar, de estudiantes que desean tomar clases virtuales,
cuando se realiza la selección aleatoria de $20$. Al aplicar la
formular de esperanza matemática para la distribución binomial, se tiene
que el valor esperado de estudiantes que desean tomar clases virtuales
es de $$\begin{align*}
\mathbb{E}(X) & = np \\
              & = 20(0.6)\\
              & = 12
\end{align*}$$

Se procede a realizar el cálculo de la varianza para poder calcular la
desviación estándar, del número de estudiantes que desean tomar clases
virtuales, tal que $$\begin{align*}
Var(X) &= np(1-p) \\
       &= 20(0.6)(1-0.6)\\
       & = 4.8
\end{align*}$$ y con este valor, se procede a calcular la desviación
estándar $$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{Var(4.8)} \\
      & = 2.19089
\end{align*}$$ De lo anterior se tiene que, al realizar la selección
aleatoria de $20$ estudiantes, es espera que $12$ estudiantes desean
tomar clases virtuales, con una desviación estándar de $2.19$
estudiantes.
</li>
</ol>
</main>

### Distribución Hipergeométrica

Si `$X$` es el número de éxitos de una muestra completamente aleatoria
de tamaño `$n$` extraída de una población `$N$` compuesta por `$M$`
éxitos y `$(N-M)$` fracasos, entonces la distribución de
`$X\sim h(N,M,n)$`, con función de masa de probabilidad

$$\begin{align*}p(x)=\frac{\left(\begin{array}{c}M\\ x\end{array}\right) \left(\begin{array}{c}N-M\\ n-x\end{array}\right)}{\left(\begin{array}{c}N\\ n\end{array}\right)}\end{align*}$$


con `$x$` un entero que satisface la condición
`$\max\{0, M-(N-n)\} \leq x \leq \min\{M,n\}$`.

**Nota:** Esta distribución es usada cuando se realiza muestreo **sin
reemplazo**, en poblaciones finitas donde hay `$M$` éxitos de un total
de `$N$` objetos, de los cuales se seleccionan `$n$` objetos a la vez.

#### Media y Varianza Hipergeométrica

Si `$X\sim h(N,M,n)$`, entonces se puede probar que la media y varianza
de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X)=n\frac{M}{N} \quad \quad Var(X)=n\left(\frac{M}{N}\right)\left(1-\frac{M}{N}\right)\left(\frac{N-n}{N-1}\right)\end{align*}$$


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
Suponga que una persona compra un container que contiene un lote de
$40$ repuestos para computadora. El comprador revisa el container
mediante un procedimiento de muestreo, y si encuentra $3$ o más
componentes defectuosos, devuelve el container a su proveedor.<br> <br>
El procedimiento de revisión consta en seleccionar una muestra aleatoria
de $10$ repuestos del lote de interés, y si se encuentran $3$ o más
repuestos defectuosos, se rechaza el lote y se devuelve al proveedor.
<br> <br> Si en un lote de repuestos de computadora hay un total de
$7$ defectuosos,
</p>
<ol>
<li>
Cuál es la probabilidad de que el comprador no devuelva el container?.
</li>
<li>
Cuál es la media y desviación estándar del número de repuestos
defectuosos?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En este primer punto estamos interesados en conocer la probabilidad de
que el comprador no devuelva el container, y para ello se requerirá que
en la muestra de $10$ repuestos que el comprador revisa, encuentren
menos de $3$ repuestos defectuosos, estos es $$\begin{align*}
\mathbb{P}(X<3)
\end{align*}$$

Donde $X$: representa el número de repuestos defectuosos. Además, de
la información suministrada tenemos que el total de artículos
defectuosos que hay en el lote de $40$ repuestos es de $7$ repuestos
defectuosos. Entonces, si llamamos a $N=40$: el número total de
repuestos, $n=10$: el total de repuestos que revisa el comprador y
$M=7$: el número de repuestos defectuosos que hay en el container, se
tendrá la siguiente distribución de probabilidad

$$\begin{align*}
p(x)=\frac{\left(\begin{array}{c}7\\ x\end{array}\right) \left(\begin{array}{c}33\\ 10-x\end{array}\right)}{\left(\begin{array}{c}40\\ 10\end{array}\right)}
\end{align*}$$

la cual está definida para $$\begin{align*}
\max\{0, M-(N-n)\} &\leq x \leq \min\{M,n\} \\
\max\{0, 7-(40-10)\} &\leq x \leq \min\{7,10\} \\
\max\{0, 7-(30)\} &\leq x \leq \min\{7,10\} \\ 
\max\{0, -23\} &\leq x \leq \min\{7,10\} \\
0 &\leq x \leq 7 \\
\end{align*}$$ en donde, al ser la distribución hipergeométrica una
distribución discreta, tendremos que el número de repuestos defectuosos
encontrados en la muestra puede ser de $x=0, 1, 2, \ldots 7$. <br>
<br> Ahora, al emplear esta función de distribución para calcular la
probabilidad de interés tendremos que

$$\begin{align*}
\mathbb{P}(X<3) &= \sum_{x=0}^2 \frac{\left(\begin{array}{c}7\\ x\end{array}\right) \left(\begin{array}{c}33\\ 10-x\end{array}\right)}{\left(\begin{array}{c}40\\ 10\end{array}\right)} \\
                &= \frac{\left(\begin{array}{c}7\\ 0\end{array}\right) \left(\begin{array}{c}33\\ 10\end{array}\right)}{\left(\begin{array}{c}40\\ 10\end{array}\right)} + \frac{\left(\begin{array}{c}7\\ 1\end{array}\right) \left(\begin{array}{c}33\\ 9\end{array}\right)}{\left(\begin{array}{c}40\\ 10\end{array}\right)} + \frac{\left(\begin{array}{c}7\\ 2\end{array}\right) \left(\begin{array}{c}33\\ 8\end{array}\right)}{\left(\begin{array}{c}40\\ 10\end{array}\right)} \\
                &= 0.1091959 + 0.318488 + 0.343967 \\
                &= 0.7716509
\end{align*}$$

En consecuencia, se tendrá un $77.16\%$ de probabilidad, de que el
comprador no rechace el container de repuestos para computadora.
</li>
<li>

En esta ocasión estamos interesados en calcular el número promedio y
desviación estándar del número de repuestos defectuosos que se esperan
encontrar cuando se revisa un total de $n=10$ repuestos de un
container que contiene $N=40$ repuestos para computadora, y en el cual
se sabe que hay $M=7$ repuestos defectuosos. Y para ello usamos la
formula de la media y la varianza asociadas a la distribución
hipergeométrica, tal que $$\begin{align*}
\mathbb{E}(X) &=n\frac{M}{N} \\
              &= 10 \left(\frac{7}{40}\right) \\
              &= 1.75
\end{align*}$$

Procedimiento similar se emplea para el cálculo de la desviación
estándar, en donde calculamos inicialmente la varianza del número de
repuestos defectuosos encontrados por el comprador, mediante la ecuación
$$\begin{align*}
Var(X)&=\left(\frac{N-n}{N-1}\right)\left(\frac{M}{N}\right)\left(1-\frac{M}{N}\right) \\
      &=\left(\frac{40-10}{40-1}\right)\left(\frac{7}{40}\right)\left(1-\frac{7}{40}\right) \\
      &= 0.1110577
\end{align*}$$

Y con este valor, procedemos al cálculo de la desviación estándar,
mediante la ecuación

$$\begin{align*}
Sd(X) &= \sqrt{Var(X)} \\
      &= \sqrt{0.1110577} \\
      &= 0.3332532
\end{align*}$$

Por tanto se tendrá que el comprador encontrará en sus revisiones un
promedio de $1.75$ repuestos defectuosos, en un container de $40$
repuestos para computadora, con una desviación estándar de $0.3332$
repuestos defectuosos.
</li>
</ol>
</main>