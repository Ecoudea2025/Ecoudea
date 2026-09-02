---
title: "Clase 04"
course: "probabilidad-inferencia"
order: 6
classType: "clase"
description: "Introducción a la estadística descriptiva. Tipos de datos. Escala de medición. Medidas estadísticas: - Medidas de tendencia central"
math: true
bibliography: "../../referencias.bib"
---

## Introducción

La Estadística es una **fuerte herramienta** empleada en las diferentes
disciplinas científicas, debido a su gran potencial para **recolectar,
analizar y presentar** de forma amigable, la información que se genera
en las distintas áreas del conocimiento, para así poder argumentar y
soportar de mejor manera las investigaciones realizadas.

Adicionalmente, la estadística tiene como ventaja respecto a otras
áreas, que permite extraer información de **variables tanto númerida
como categórica** de la población de interés o de una muestra de la
misma, permitiendo con ello, establecer conclusiones acerca de la misma
población, o de alguno de los parámetros que la conforman. Dado lo
anterior, no es de sorprender que la estadística sea concebida como
**uno de los pilares fundamental** dentro de la investigación científica
teórica y aplicada.

En general, el análisis estadístico puede dividirse en dos partes:

-   La **Estadística descriptiva**, la cual se encarga de resumir la
    información suministrada mediante el empleo de tablas, gráficas y
    medidas numéricas, junto con el análisis de las mismas, para
    facilitar la interpretación y la presentación de la información.
-   La **Inferencia estadística**, la cual se encarga de la inferencias,
    modelamiento y predicción de la información, para facilitar la
    obtención de conclusiones y toma decisiones.

## Estadística descriptiva

En general, la importancia del análisis estadístico radica en la
**resolución de problemas vinculados con datos**, en donde la
variabilidad de los mísmos es quién guiará la importancia del empleo de
diferentes ténicas para el manejo de la información. Desde este punto de
vista, se discute en esta sección sobre la implementación de resúmenes
de información, así como la presentación por medio de cuadros, diagramas
o gráficos, cálculo y uso de medidas estadísticas de tendencia central,
localización, variabilidad y forma.

Un aspecto importante a tener en cuenta al realizar análisis
estadísticos, es señalado por Esquivel ([2016, p.
29](#ref-Esquivel2016)), el cual menciona que dentro de un análisis con
información estadística, se debe tener en cuenta las siguientes etapas:

1.  **Leer entre los datos**: que consiste en llevar a cabo una lectura
    literal de la información, sin interpretar su contenido.
2.  **Leer dentro de los datos**: implica no solamente interpretar los
    datos sino integrarlos dentro del contexto.
3.  **Leer más allá de los datos**: significa tomar los datos como
    referente para identificar patrones que transciendan el grupo de
    datos observado, ya sea mediante la interpolación o extrapolación de
    resultados.
4.  **Leer detrás de los datos**: consiste en llevar a cabo un análisis
    crítico de la información que se estudia, esto implica analizar
    integralmente el problema, desde su origen, el tipo de dato que se
    utiliza, su validez y fiabilidad para analizar el problema y la
    posibilidad de generalizar los hallazgos.

### Finalidad de la estadística

-   Conocer el grado de incertidumbre que posee un fenómeno.
-   Conocer la realidad de un fenómeno y determinar los cambios y las
    causas que lo originan.
-   Hacer estimaciones y pronósticos sobre el comportamiento de
    variables.

### Tipos de datos

En términos generales, los datos son cualquier pieza de información
recolectada del fenómeno que se pretende analizar, y que, dependiendo de
las características que posean, deben clasificarse dentro de una
determinada categoría.

-   **Cuantitativos**: Son datos que pueden ser medidos o cuantificados.
    Estos se subdividen en dos categorías:
    -   **Datos cuantitativos discretos**: Son aquellos datos que
        provienen de procesos que involucran conteos, y por tanto, solo
        pueden tomar valores enteros. Por ejemplo: **Edad de una
        persona, número de estudiantes que perdieron un curso, cantidad
        de profesores que dictan Probabilidad e Inferencia Estadística**
    -   **Datos cuantitativos continuos**: Son aquellos datos que
        provienen de procesos que involucran mediciones, y por tanto,
        solo pueden tomar cualquier valor real dentro de un intervalo.
        Por ejemplo: **Temperatura de congelación del agua, Tiempo que
        dura una clase, Utilidad diaria de un negocio.**
-   **Cualitativos**: Son datos asociados a una cualidad o propiedad, y
    por tanto, no pueden representarse numéricamente, a pesar de poder
    caracterizarse alfanúmericamente. Por ejemplo: **Estrato
    socioeconómico, tipo de animales en una granja, nivel de
    satisfacción con el método planteado para dictar el curso.**

### Escala de medición

Las escalas o niveles de medición se utilizan para medir variables o
atributos que posea un conjunto de datos. A saber, las escalas de
medición se dividen en cuatro, **nominal, ordinal, intervalos y razón**.
Las dos primeras (nominal y ordinal) se conocen como escalas categóricas
usadas comúnmente para variables cualitativas, mientras que las dos
últimas (intervalo y razón) se conocen como escalas numéricas, usadas
comúnmente para variables cuantitativas.

-   **Nominal**: Son aquellos factores que establecen etiquetas o
    categorías a los datos, sin estar sujetos a un orden específico. Por
    ejemplo: **Partido político, Comuna de residencia**
-   **Ordinal**: Son aquellos factores que establecen etiquetas o
    categorías a los datos, junto a una estructura jerárquica. Por
    ejemplo: **Nivel de una enfermedad, Grado de escolaridad**
-   **Intervalo**: Son aquellas mediciones cuantitativas que establecen
    la distancia entre una medida y otra, en términos de una unidad de
    medición fija, donde **el cero se selecciona de forma arbitraria y
    no indica ausencia del tributo**, ni indica conceptos como
    ‘ninguno’, ‘vacío’ o ‘nada’. Por ejemplo: **Unidades de medida en
    centígrados o Fahrenheit**
-   **Razón**: Son aquellas mediciones cuantitativas que establece la
    distancia exacta de una categoría debido a que **el cero es
    absoluto, no es arbritario, e indica ausencia del atributo**. Por
    ejemplo **Índice de masa corporal, Salario**

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
Clasifique las variables según el tipo de dato y su escala de medición
</p>
<ol>
<li>
Evaluación de conocimientos
</li>
<li>
Tipo de universidad
</li>
<li>
Posición en un reinado de belleza
</li>
<li>
Calidad de vida en una ciudad
</li>
<li>
Escalas de los test psicológicos
</li>
<li>
Litros de agua consumidos por persona al día
</li>
<li>
Número del documento de identidad
</li>
<li>
Goles marcados por un futbolista en un partido
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
<strong> Evaluación de conocimientos: </strong> Suponga que es una
calificación obtenida en un intervalo de $0$ a $5$, y en
consecuencia, se tendrá que la variable será de tipo
<strong>Cuantitativa continua</strong>, con una escala de medición de
tipo <strong>intervalo</strong>, debido a que tener un $0$ en una
evaluación de conocimiento no significa necesariamente que no se tenga
ningún conocimiento sobre el tema evaluado
</li>
<li>
<strong> Tipo de universidad:</strong> Dado que las universidades pueden
ser públicas o privadas, se tendrá una variable de tipo
<strong>Cualitativa</strong>, con una escala de medición de tipo
<strong>nominal</strong>, debido a que no existe una jerarquía o un
ordenamiento natural en donde se siga que las universidades públicas son
superiores a las privadas, o viceversa.
</li>
<li>
<strong> Posición en un reinado de belleza:</strong> La posición
obtenida en un reinado de belleza se divide en muchas competencias como
Reina, Virreina, Primera princesa, Segunda Princesa y Tercera princesa,
por tanto, se tendrá que la variable será de tipo
<strong>Cualitativa</strong>, con una escala de medición de tipo
<strong>ordinal</strong> debido a que hay una jerarquía entre las
posiciones obtenidas, siendo la posición más alta la Reina, cual es la
que gana la competencia, seguida por la Virreina la cual es quién queda
en la segunda posición en la competencia, y así sucesivamente.
</li>
<li>
<strong> Calidad de vida en una ciudad:</strong> Suponiendo que la
medición se hace en niveles de Alta, Media y Baja, se tendrá que la
variable será de tipo <strong>Cualitativa</strong>, con una escala de
medición de tipo <strong>ordinal</strong> debido a que hay una persona
que tenga una calidad de vida alta, va a estar en una mejor posición
económica que tenga una calidad de vida baja. Aunque ésto podría ser
planteado de forma diferente, debido a que hay diferentes definiciones
de calidad de vida.
</li>
<li>
<strong> Escalas de los test psicológicos:</strong> son pruebas que
miden diferentes características, por ejemplo, la inteligencia emocional
o altruismo. Éstas por lo general poseen calificaciones que van de $0$
a $100$, por lo cual se tendrá que la variable será de tipo
<strong>Cuantitativa discreta</strong>, con una escala de medición de
tipo <strong>intervalo</strong>, debido a que en este tipo de
calificaciones el $0$ se elige de forma arbitraria por quienes
desarrollaron dichos test.
</li>
<li>
<strong> Litros de agua consumidos por persona al día:</strong> Dado que
una persona puede consumir hasta $7$ litros de agua por día antes de
sufrir de hiperhidratación o intoxicación por agua, diremos que es una
variable de tipo <strong>Cuantitativa continua</strong>, con una escala
de medición de tipo <strong>razón</strong> debido que consumir cero
litros de agua en el día, significa que hubo ausencia total del consumo.
</li>
<li>
<strong> Número del documento de identidad:</strong> Aunque la variable
sea literalmente númerica, no significa que tenga un valor numérico como
tal, en su lugar, éste sirve un como identificador para las personas, y
por tanto se tendrá que dicha variable es de tipo
<strong>Cualitativa</strong>, con una escala de medición de tipo
<strong>nominal</strong>, debido a que el número de identidad en
particular no simboliza una jerarquía mayor a menor respecto a números
de identidad menores o mayores, respectivamente.
</li>
<li>
<strong> Goles marcados por un futbolista en un partido:</strong> Un
futbolista puede no anotar goles en un partido, o anotar $1$ gol,
$2$ goles, $3$ goles, $\ldots$, $n$ goles. Dado lo anterior, se
observa que un jugador solo puede anotar un número entero de goles, y
por tanto, se tendrá que la variable será de tipo <strong>Cuantitativa
discreta</strong>, con una escala de medición de tipo
<strong>razón</strong> debido que no meter goles en un partido significa
que hubo una ausencia de goles de parte del jugador en dicho partido.
</li>
</ol>
</main>

## Medidas estadísticas

Las medidas estadísticas tienen por objetivo resumir la información
contenida en un conjunto de datos, en pocos valores numéricos que
representan diferentes características. **Estas medidas estadísticas nos
darán información sobre la situación, dispersión, forma, asociación que
posee un conjunto de datos** de manera que sea posible captar
rápidamente la estructura de los mismos.

#### Caso de estudio

Suponga que se está interesado en observar la evolución en el desempeño
que tuvo un grupo de `$10$` estudiantes en el curso de Probabilidad e
Inferencia Estadística. Para ello se toma de referencia la nota obtenida
en el primer y cuarto parcial de la materia, obteniendo los siguientes
resultados

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:right;">
1
</th>
<th style="text-align:right;">
2
</th>
<th style="text-align:right;">
3
</th>
<th style="text-align:right;">
4
</th>
<th style="text-align:right;">
5
</th>
<th style="text-align:right;">
6
</th>
<th style="text-align:right;">
7
</th>
<th style="text-align:right;">
8
</th>
<th style="text-align:right;">
9
</th>
<th style="text-align:right;">
10
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Parcial 1
</td>
<td style="text-align:right;">
2.7
</td>
<td style="text-align:right;">
4.0
</td>
<td style="text-align:right;">
3.1
</td>
<td style="text-align:right;">
2.7
</td>
<td style="text-align:right;">
2.9
</td>
<td style="text-align:right;">
1.3
</td>
<td style="text-align:right;">
2.6
</td>
<td style="text-align:right;">
2.8
</td>
<td style="text-align:right;">
3.3
</td>
<td style="text-align:right;">
2.1
</td>
</tr>
<tr>
<td style="text-align:left;">
Parcial 4
</td>
<td style="text-align:right;">
1.8
</td>
<td style="text-align:right;">
4.7
</td>
<td style="text-align:right;">
3.4
</td>
<td style="text-align:right;">
0.7
</td>
<td style="text-align:right;">
4.1
</td>
<td style="text-align:right;">
3.6
</td>
<td style="text-align:right;">
4.5
</td>
<td style="text-align:right;">
3.2
</td>
<td style="text-align:right;">
3.4
</td>
<td style="text-align:right;">
2.0
</td>
</tr>
</tbody>
</table>

### Medidas de tendencia central

Estas medidas tienen por objetivo buscar valores que muestren el lugar
en el cual se encuentra el centro de un conjunto de observaciones. Si se
define `$x_1, x_2, \ldots, x_n$` como un conjunto de `$n$`
observaciones, entonces

#### Media

Es el promedio numérico de las `$n$` observaciones.

$$\begin{align*}\bar{X}=\sum_{i=1}^n\frac{x_i}{n}=\frac{x_1+x_2+\ldots+x_n}{n}\end{align*}$$


En <tt>R</tt>, puede calcularse el valor promedio de un conjunto de
observaciones mediante la función `mean(datos)`.

<button id="Show2" class="btn btn-secondary">
Mostrar Ejercicio Manual
</button>
<button id="Hide2" class="btn btn-info">
Ocultar Ejercicio Manual
</button>
<main id="botoncito2">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la nota promedio obtenida por los $10$ estudiantes en el
primer y cuarto parcial del curso de Probabilidad e Inferencia
Estadística de forma manual.
</p>
<h3 data-toc-skip>
Solución Manual
</h3>
<p>

La nota promedio obtenida por los estudiantes durante el primer y cuarto
parcial del curso de Probabilidad e Inferencia Estadística estará dada
por

$$\begin{align*}
  \bar{X}_{P_1}=\frac{2.7 + 4.0 + \ldots + 2.1}{10} = 2.75 \\
  \bar{X}_{P_4}=\frac{1.8 + 4.7 + \ldots + 2.0}{10} = 3.14 
\end{align*}$$

Lo anterior significa que, el valor promedio obtenido por los
estudiantes en el parcial $1$ del curso de Probabilidad e Inferencia
Estadística fue de $2.75$, mientras que el valor promedio obtenido en
el parcial $4$ fue de $3.14$. Es decir, se aprecia que hubo una
mejora en la nota promedio por los estudiantes de $0.39$.
</p>
</main>
<button id="Show3" class="btn btn-secondary">
Mostrar Ejercicio en <tt>R</tt>
</button>
<button id="Hide3" class="btn btn-info">
Ocultar Ejercicio en <tt>R</tt>
</button>
<main id="botoncito3">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la nota promedio obtenida por los $10$ estudiantes en el
primer y cuarto parcial del curso de Probabilidad e Inferencia
Estadística con <tt>R</tt>.
</p>
<h3 data-toc-skip>
Solución en <tt>R</tt>
</h3>
<p>
Para realizar el cálculo en <tt>R</tt> de la nota promedio obtenida por
los estudiantes en los dos parciales se emplea la función
<code>mean()</code> tal que
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se guardan los datos en R</span><span class="w">
</span><span class="n">P1</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="m">2.7</span><span class="p">,</span><span class="w"> </span><span class="m">4.0</span><span class="p">,</span><span class="w"> </span><span class="m">3.1</span><span class="p">,</span><span class="w"> </span><span class="m">2.7</span><span class="p">,</span><span class="w"> </span><span class="m">2.9</span><span class="p">,</span><span class="w"> </span><span class="m">1.3</span><span class="p">,</span><span class="w"> </span><span class="m">2.6</span><span class="p">,</span><span class="w"> </span><span class="m">2.8</span><span class="p">,</span><span class="w"> </span><span class="m">3.3</span><span class="p">,</span><span class="w"> </span><span class="m">2.1</span><span class="p">)</span><span class="w">
</span><span class="n">P4</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="m">1.8</span><span class="p">,</span><span class="w"> </span><span class="m">4.7</span><span class="p">,</span><span class="w"> </span><span class="m">3.4</span><span class="p">,</span><span class="w"> </span><span class="m">0.7</span><span class="p">,</span><span class="w"> </span><span class="m">4.1</span><span class="p">,</span><span class="w"> </span><span class="m">3.6</span><span class="p">,</span><span class="w"> </span><span class="m">4.5</span><span class="p">,</span><span class="w"> </span><span class="m">3.2</span><span class="p">,</span><span class="w"> </span><span class="m">3.4</span><span class="p">,</span><span class="w"> </span><span class="m">2.0</span><span class="p">)</span><span class="w">

</span><span class="c1">## Se calcula la media de cada conjunto de datos</span><span class="w">
</span><span class="c1"># Media Parcial 1</span><span class="w">
</span><span class="n">mean</span><span class="p">(</span><span class="n">P1</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 2.75
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Media Parcial 4</span><span class="w">
</span><span class="n">mean</span><span class="p">(</span><span class="n">P4</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 3.14
</code></pre>
</section>
</section>
</main>

#### Mediana

Es el valor que ocupa el lugar central en un conjunto de datos, es
decir, el valor que divide el conjunto de observaciones en dos partes
que contienen el 50% de las observaciones. Para realizar el cálculo de
la mediana es necesario ordenar inicialmente el conjunto de
observaciones de forma ascendente.

$$\begin{align*}\tilde{X}=\begin{cases}x_{\left[\frac{(n+1)}{2}\right]} & \text{si } n \text{ es impar}\\\frac{1}{2}\left(x_{\left[\frac{n}{2}\right]}+x_{\left[\frac{n}{2}+1\right]}\right) & \text{si } n \text{ es par}\end{cases}\end{align*}$$

donde `$x_{\left[j\right]}$` representa la `$j$`-ésima observación
ordenada. En <tt>R</tt> puede calcularse la mediana de un conjunto de
observaciones mediante la función `median(datos)`.

<button id="Show4" class="btn btn-secondary">
Mostrar Ejercicio Manual
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejercicio Manual
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la nota mediana obtenida por los $10$ estudiantes en el primer
y cuarto parcial del curso de Probabilidad e Inferencia Estadística de
forma manual.
</p>
<h3 data-toc-skip>
Solución Manual
</h3>
<p>

Inicialmente, se observa que el total de estudiantes es $10$, por lo
cual, se tiene que $n$ es un número par, haciendo que la ecuación
empleada sea

$$\begin{align*}
  \tilde{X} &= \frac{1}{2}\left(x_{\left[\frac{n}{2}\right]}+x_{\left[\frac{n}{2}+1\right]}\right) \\
            &= \frac{1}{2}\left(x_{\left[\frac{10}{2}\right]}+x_{\left[\frac{10}{2}+1\right]}\right) \\
            &= \frac{1}{2}\left(x_{\left[5\right]}+x_{\left[6\right]}\right)
\end{align*}$$

En donde se observa que debe localizarse la observación que ocupa la
posición número $5$ y $6$ en las notas obtenidas <strong>luego de
ordenarlas de menor a mayor</strong>. Realizando el ordenamiento para el
parcial $1$ se tendrá
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 1
</td>
<td style="text-align:left;">
1.3
</td>
<td style="text-align:left;">
2.1
</td>
<td style="text-align:left;">
2.6
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.8
</td>
<td style="text-align:left;">
2.9
</td>
<td style="text-align:left;">
3.1
</td>
<td style="text-align:left;">
3.3
</td>
<td style="text-align:left;">
4.0
</td>
</tr>
</tbody>
</table>
<p>
donde se observa que las observaciones $5$ y $6$ para el parcial
$1$ están dadas por $x_{[5]}=2.7$ y $x_{[6]}=2.8$,
respectivamente. Mientras que, realizando el ordenamiento para el
parcial $4$ se tendrá
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 4
</td>
<td style="text-align:left;">
0.7
</td>
<td style="text-align:left;">
1.8
</td>
<td style="text-align:left;">
2.0
</td>
<td style="text-align:left;">
3.2
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.6
</td>
<td style="text-align:left;">
4.1
</td>
<td style="text-align:left;">
4.5
</td>
<td style="text-align:left;">
4.7
</td>
</tr>
</tbody>
</table>
<p>

donde se evidencia que las observaciones $5$ y $6$ para el parcial
$4$ están dadas por $x_{[5]}=3.4$ y $x_{[6]}=3.4$,
respectivamente.

Con dichos valores se realiza entonces, el cálculo de la mediana para
los parciales $1$ y $4$,tal que

$$\begin{align*}
  \tilde{X}_{P_1} =\frac{1}{2}(2.7+2.8)=2.75 \\
  \tilde{X}_{P_4} =\frac{1}{2}(3.4+3.4)=3.4
\end{align*}$$

De lo anterior se aprecia que para el parcial $1$, la mitad de los
estudiantes del curso de Probabilidad e Inferencia Estadística
obtuvieron notas menores o iguales a $2.75$, mientras la otra mitad
obtuvo notas mayores o iguales a $2.75$. Similarmente, se observa para
el parcial $4$, que el $50\%$ inferior de los estudiantes obtuvieron
una nota de a lo más $3.4$, mientras el $50\%$ superior de los
estudiantes obtuvo una nota de al menos $3.4$.
</p>
</main>
<button id="Show5" class="btn btn-secondary">
Mostrar Ejercicio en <tt>R</tt>
</button>
<button id="Hide5" class="btn btn-info">
Ocultar Ejercicio en <tt>R</tt>
</button>
<main id="botoncito5">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la nota mediana obtenida por los $10$ estudiantes en el primer
y cuarto parcial del curso de Probabilidad e Inferencia Estadística con
<tt>R</tt>.
</p>
<h3 data-toc-skip>
Solución en <tt>R</tt>
</h3>
<p>
Para realizar el cálculo en <tt>R</tt> de la nota mediana obtenida por
los estudiantes en los dos parciales se emplea la función
<code>median()</code> tal que
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1">## Se calcula la mediana de cada conjunto de datos</span><span class="w">
</span><span class="c1"># Mediana Parcial 1</span><span class="w">
</span><span class="n">median</span><span class="p">(</span><span class="n">P1</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 2.75
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Mediana Parcial 4</span><span class="w">
</span><span class="n">median</span><span class="p">(</span><span class="n">P4</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 3.4
</code></pre>
</section>
</section>
</main>

#### Moda

Es el valor que ocurre con mayor frecuencia en un conjunto de datos, es
decir, es la observación que se repite con mayor frecuencia. Es de
anotar que en un conjunto de observaciones, se puede tener más de una
moda, en cuyo caso se dirá que el conjunto de datos es bimodal, trimodal
o multimodal.

Entre las funciones base del programa <tt>R</tt> no hay ninguna función
que calcule la moda de un conjunto de observaciones, y por tanto, debe
crearse una función que realice el cálculo, de la forma

``` r
# Función para el cálculo de la moda
Moda <- function(x) {
    keys <- na.omit(unique(x))
    keys[which.max(tabulate(match(x, keys)))]
}
```

Una vez creada la función, puede calcularse la moda de un conjunto de
observaciones mediante la función `Moda(datos)`.

<button id="Show6" class="btn btn-secondary">
Mostrar Ejercicio Manual
</button>
<button id="Hide6" class="btn btn-info">
Ocultar Ejercicio Manual
</button>
<main id="botoncito6">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la moda de las nota obtenida por los $10$ estudiantes en el
primer y cuarto parcial del curso de Probabilidad e Inferencia
Estadística de forma manual.
</p>
<h3 data-toc-skip>
Solución Manual
</h3>
<p>
Para encontrar la nota modal de los parciales, es necesario localizar la
nota que más se repita en cada parcial. Con el fin de ilustrar cuales
son éstas, se presenta nuevamente la tabla con la nota registrada para
cada uno de los 10 estudiantes.
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:right;">
</th>
<th style="text-align:right;">
1
</th>
<th style="text-align:right;">
2
</th>
<th style="text-align:right;">
3
</th>
<th style="text-align:right;">
4
</th>
<th style="text-align:right;">
5
</th>
<th style="text-align:right;">
6
</th>
<th style="text-align:right;">
7
</th>
<th style="text-align:right;">
8
</th>
<th style="text-align:right;">
9
</th>
<th style="text-align:right;">
10
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Parcial 1
</td>
<td style="text-align:right;">
Parcial 1
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: #974c55 !important;">2.7</span>
</td>
<td style="text-align:right;">
4.0
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: transparency !important;">3.1</span>
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: #974c55 !important;">2.7</span>
</td>
<td style="text-align:right;">
2.9
</td>
<td style="text-align:right;">
1.3
</td>
<td style="text-align:right;">
2.6
</td>
<td style="text-align:right;">
2.8
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: transparency !important;">3.3</span>
</td>
<td style="text-align:right;">
2.1
</td>
</tr>
<tr>
<td style="text-align:left;">
Parcial 4
</td>
<td style="text-align:right;">
Parcial 4
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: transparency !important;">1.8</span>
</td>
<td style="text-align:right;">
4.7
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: #974c55 !important;">3.4</span>
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: transparency !important;">0.7</span>
</td>
<td style="text-align:right;">
4.1
</td>
<td style="text-align:right;">
3.6
</td>
<td style="text-align:right;">
4.5
</td>
<td style="text-align:right;">
3.2
</td>
<td style="text-align:right;">
<span
style="     border-radius: 4px; padding-right: 4px; padding-left: 4px; background-color: #974c55 !important;">3.4</span>
</td>
<td style="text-align:right;">
2.0
</td>
</tr>
</tbody>
</table>
<p>

De la tabla anterior, se observa que para el caso del parcial $1$, se
observa que nota modal obtenida por los estudiantes de Probabilidad e
Inferencia Estadística es de $2.7$, ya que es la única nota que se
repite dos veces en el conjunto de observaciones.

Similarmente, para el parcial $4$, se aprecia que la nota modal es de
$3.4$ dado que es la nota que más se repite de las $10$ notas
registradas.
</p>
</main>
<button id="Show7" class="btn btn-secondary">
Mostrar Ejercicio en <tt>R</tt>
</button>
<button id="Hide7" class="btn btn-info">
Ocultar Ejercicio en <tt>R</tt>
</button>
<main id="botoncito7">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la moda de las notas obtenidas por los $10$ estudiantes en el
primer y cuarto parcial del curso de Probabilidad e Inferencia
Estadística con <tt>R</tt>.
</p>
<h3 data-toc-skip>
Solución en <tt>R</tt>
</h3>
<p>
Para realizar el cálculo en <tt>R</tt> de la nota modal obtenida por los
estudiantes en los dos parciales se emplea la función
<code>Moda()</code>, la cual se definió anteriormente
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Se corre inicialmente la función Moda para crearla</span><span class="w">
</span><span class="n">Moda</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="k">function</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="n">keys</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">na.omit</span><span class="p">(</span><span class="n">unique</span><span class="p">(</span><span class="n">x</span><span class="p">))</span><span class="w">
    </span><span class="n">keys</span><span class="p">[</span><span class="n">which.max</span><span class="p">(</span><span class="n">tabulate</span><span class="p">(</span><span class="n">match</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="n">keys</span><span class="p">)))]</span><span class="w">
</span><span class="p">}</span><span class="w">

</span><span class="c1">## Se calcular la moda de cada conjunto de datos</span><span class="w">
</span><span class="c1"># Moda Parcial 1</span><span class="w">
</span><span class="n">Moda</span><span class="p">(</span><span class="n">P1</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 2.7
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Moda Parcial 4</span><span class="w">
</span><span class="n">Moda</span><span class="p">(</span><span class="n">P4</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 3.4
</code></pre>
</section>
</section>
</main>

#### Media recortada

Es una medida similar a la media, con la diferencia de que, en este
caso, se ordenan las observaciones de forma ascendente, y luego se
recortan un número `$r$` observaciones superiores e inferiores, tal que
`$r=n\times trim$`, `$trim$` un valor porcentual entre 0 y 0.5


$$\begin{align*}\bar{X}_{trim}=\frac{1}{n-2r}\sum_{i={r+1}}^{n-r}x_i\end{align*}$$


En <tt>R</tt>, puede calcularse el valor de la media recortada de un
conjunto de observaciones mediante la función
`mean(datos, trim = trim)`.

<button id="Show8" class="btn btn-secondary">
Mostrar Ejercicio Manual
</button>
<button id="Hide8" class="btn btn-info">
Ocultar Ejercicio Manual
</button>
<main id="botoncito8">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la media recortada al $10\%$ de las notas obtenidas por los
$10$ estudiantes en el primer y cuarto parcial del curso de
Probabilidad e Inferencia Estadística de forma manual.
</p>
<h3 data-toc-skip>
Solución Manual
</h3>
<p>

Para encontrar la nota promedio de los parciales, al eliminar el efecto
del $10\%$ de notas más altas y más bajas, es necesario ordenar de
forma ascendente las notas obtenidas en los parciales. Dado que se
tienen $10$ observaciones, de tendrá que eliminar entonces la nota más
alta y la nota más baja.

Entonces, para el caso del parcial $1$ se tendrá que el conjunto de
observaciones ordenadas es
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 1
</td>
<td style="text-align:left;">
1.3
</td>
<td style="text-align:left;">
2.1
</td>
<td style="text-align:left;">
2.6
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.8
</td>
<td style="text-align:left;">
2.9
</td>
<td style="text-align:left;">
3.1
</td>
<td style="text-align:left;">
3.3
</td>
<td style="text-align:left;">
4.0
</td>
</tr>
</tbody>
</table>
<p>
en donde, al eliminar la nota más baja y la nota más alta se tendrá que
el conjunto de observaciones usadas para calcular la media recortada
será
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 1
</td>
<td style="text-align:left;">
2.1
</td>
<td style="text-align:left;">
2.6
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.7
</td>
<td style="text-align:left;">
2.8
</td>
<td style="text-align:left;">
2.9
</td>
<td style="text-align:left;">
3.1
</td>
<td style="text-align:left;">
3.3
</td>
</tr>
</tbody>
</table>
<p>
Similarmente, se realiza el mismo procedimiento para el caso del parcial
$4$, en donde el conjunto de notas ordenados de menor a mayor será
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 4
</td>
<td style="text-align:left;">
0.7
</td>
<td style="text-align:left;">
1.8
</td>
<td style="text-align:left;">
2.0
</td>
<td style="text-align:left;">
3.2
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.6
</td>
<td style="text-align:left;">
4.1
</td>
<td style="text-align:left;">
4.5
</td>
<td style="text-align:left;">
4.7
</td>
</tr>
</tbody>
</table>
<p>
donde se aprecia que la nota más baja es $0.7$, mientras que la más
alta es $4.7$. Al eliminar dichas observaciones, se tendrá que
conjunto de notas usadas para calcular la media recortada al $10\%$
estarán dada por
</p>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="text-align:left;">
Parcial 4
</td>
<td style="text-align:left;">
1.8
</td>
<td style="text-align:left;">
2.0
</td>
<td style="text-align:left;">
3.2
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.4
</td>
<td style="text-align:left;">
3.6
</td>
<td style="text-align:left;">
4.1
</td>
<td style="text-align:left;">
4.5
</td>
</tr>
</tbody>
</table>
<p>

Al realizar el cálculo de la media recortada al $10\%$ para cada
parcial se encuentran los siguientes resultados

$$\begin{align*}
  \bar{X}_{0.1_{P_1}}=\frac{2.1 + 2.6 + \ldots + 3.3}{8} = 2.775 \\
  \bar{X}_{0.1_{P_4}}=\frac{1.8 + 2.0 + \ldots + 4.5}{8} = 3.25 
\end{align*}$$

De los resultados anteriores, se observa que para ambos casos, la
eliminación del $10\%$ de las notas más altas y más bajas, se obtiene
como resultado un incremento en la nota promedio, pasando de $2.75$
con el total de notas, a $2.775$ con la eliminación del $10\%$ de
las notas extremas, para el caso del parcial $1$, y pasando de
$3.14$ a $3.25$ para el caso del parcial $4$. <br> <br> De los
hallazgos encontrados al comparar los resultados de la media contra la
media recortada al $10\%$, se tiene que el valor el efecto que tienen
las notas más bajas es mayor al efecto de las notas más altas, pues se
observa que al eliminar la nota más alta y más baja, se tienen un
incremento en la nota promedio obtenida por el curso.
</p>
</main>
<button id="Show9" class="btn btn-secondary">
Mostrar Ejercicio en <tt>R</tt>
</button>
<button id="Hide9" class="btn btn-info">
Ocultar Ejercicio en <tt>R</tt>
</button>
<main id="botoncito9">
<h3 data-toc-skip>
Ejercicio Caso de Estudio
</h3>
<p>
Calcule la media recortada al $10\%$ de las notas obtenidas por los
$10$ estudiantes en el primer y cuarto parcial del curso de
Probabilidad e Inferencia Estadística con <tt>R</tt>.
</p>
<h3 data-toc-skip>
Solución en <tt>R</tt>
</h3>
<p>
Para realizar el cálculo en <tt>R</tt> de la nota promedio recortada al
$10\%$ de los estudiantes en los dos parciales se emplea la función
<code>mean()</code> con el argumento <code>trim = 0.1</code>, tal que
</p>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1">## Se calcula la media recortada al 10% de cada conjunto de datos</span><span class="w">
</span><span class="c1"># Media recortada al 10% Parcial 1</span><span class="w">
</span><span class="n">mean</span><span class="p">(</span><span class="n">P1</span><span class="p">,</span><span class="w"> </span><span class="n">trim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0.1</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 2.775
</code></pre>
</section>
</section>
<section class="language-r highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code><span class="c1"># Media recortada al 10% Parcial 4</span><span class="w">
</span><span class="n">mean</span><span class="p">(</span><span class="n">P4</span><span class="p">,</span><span class="w"> </span><span class="n">trim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0.1</span><span class="p">)</span><span class="w">
</span></code></pre>
</section>
</section>
<section class="highlighter-rouge">
<section class="highlight">
<pre class="highlight"><code>[1] 3.25
</code></pre>
</section>
</section>
</main>

## Referencias

<h7 id="ref-Esquivel2016"></h7>

Esquivel, E. (2016). La enseñanza de la estadı́stica y la probabilidad,
más allá de procedimientos y técnicas. *Cuadernos de Investigación y
Formación En Educación Matemática*, 21–31.