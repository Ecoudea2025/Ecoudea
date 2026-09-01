---
title: "Clase 17"
course: "estadistica-ii"
order: 21
classType: "clase"
description: "Análisis de Regresión - Regresión lineal simple - Estimación de parámetros"
math: true
bibliography: "../../referencias.bib"
---

## Análisis de Regresión

El análisis de regresión es una técnica estadística que **se emplea para
investigar y modelar la relación existente entre variables**.

Existen numerosas aplicaciones del análisis de regresión, las cuales se
dan en casi cualquier campo de estudio como lo es en ingeniería,
economía, biología, medicina, ciencias sociales, entre otras, y por
tanto **puede ser considerada como la técnica estadística más usada en
la práctica**.

Para entender este tipo de relación, se suponen inicialmente dos
variables, la primera variable será la variable `$Y$` la cual es
variable dependiente o variable respuesta, mientras que la segunda
variable será la variable `$X$` la cual es la variable independiente o
variable explicativa.

El objetivo será estudiar la relación asociada entre `$Y$` y `$X$` (la
cual no es necesariamente de causa-efecto), y para ello miraremos los
siguientes casos de estudio.

<ol>
<li>

<strong>Caso 1 (Diseño experimental controlado)</strong>: Se realiza un
estudio en un supermercado para observar la relación existente entre el
espacio asignado para la exhibición de licores y las ventas semanales de
licores que se realizan. Suponga que durante \(15\) semanas se decide
distribuir de forma aleatoria el espacio disponible para la exhibición,
usando como referencia el número de estanterías iguales a \(3\), \(5\) y
\(7\). Los resultados para las \(15\) semanas se registran a
continuación.

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<th>
Espacio asignado
</th>
<th>
Ventas semanales
</th>
</thead>
<tbody>
<tr>
<td>
3
</td>
<td>
491
</td>
</tr>
<tr>
<td>
7
</td>
<td>
534
</td>
</tr>
<tr>
<td>
3
</td>
<td>
495
</td>
</tr>
<tr>
<td>
3
</td>
<td>
500
</td>
</tr>
<tr>
<td>
5
</td>
<td>
496
</td>
</tr>
<tr>
<td>
7
</td>
<td>
527
</td>
</tr>
<tr>
<td>
5
</td>
<td>
491
</td>
</tr>
<tr>
<td>
3
</td>
<td>
476
</td>
</tr>
<tr>
<td>
5
</td>
<td>
512
</td>
</tr>
<tr>
<td>
5
</td>
<td>
492
</td>
</tr>
<tr>
<td>
7
</td>
<td>
546
</td>
</tr>
<tr>
<td>
7
</td>
<td>
532
</td>
</tr>
<tr>
<td>
5
</td>
<td>
492
</td>
</tr>
<tr>
<td>
3
</td>
<td>
461
</td>
</tr>
<tr>
<td>
7
</td>
<td>
529
</td>
</tr>
</tbody>
</table>
<ul>
<strong>Interés - Objetivos</strong>
<li>
Investigar la relación existente entre las ventas semanales y el espacio
asignado.
</li>
<li>
Determinar si hay una relación significativa entre el espacio asignado a
los licores y las ventas semanales.
</li>
<li>
Hacer la estimación de las ventas semanales cuando se asigna un espacio
para exhibición de licor de \(7\) estanterías.
</li>
<li>
Predecir el valor de las ventas semanales si para la semana siguiente se
asigna un espacio de \(4\) estanterías para exhibir licor.
</li>
</ul>
</li>
<li>

<strong>Caso 2 (Mediciones Repetidas)</strong>: Un estudiante de gestión
socioeconómica de proyectos quiere observar si hay una relación entre el
gasto en campañas publicitarias y las donaciones recibidas para la
construcción de parques y bibliotecas para sectores de la población con
bajos recursos. Para realizar el estudio se toma como referencia \(10\)
meses en los cuales hicieron gastos en publicidad y obtuvieron los
siguientes datos en millones de pesos

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<th>
Gasto en Publicidad
</th>
<th>
Donaciones recibidas
</th>
</thead>
<tbody>
<tr>
<td>
40
</td>
<td>
385
</td>
</tr>
<tr>
<td>
20
</td>
<td>
400
</td>
</tr>
<tr>
<td>
25
</td>
<td>
395
</td>
</tr>
<tr>
<td>
20
</td>
<td>
365
</td>
</tr>
<tr>
<td>
30
</td>
<td>
475
</td>
</tr>
<tr>
<td>
50
</td>
<td>
440
</td>
</tr>
<tr>
<td>
40
</td>
<td>
490
</td>
</tr>
<tr>
<td>
20
</td>
<td>
420
</td>
</tr>
<tr>
<td>
50
</td>
<td>
560
</td>
</tr>
<tr>
<td>
40
</td>
<td>
525
</td>
</tr>
</tbody>
</table>
<ul>
<strong>Interés - Objetivos</strong>
<li>
Investigar la relación existente entre las donaciones recibidas y el
gasto en publicidad.
</li>
<li>
Ajustar un modelo que permita explicar las donaciones recibidas en
función del gasto en publicidad.
</li>
<li>
Predecir el valor de las donaciones realizadas en caso de gastar en
publicidad \(53\) millones de pesos.
</li>
</ul>
</li>
<li>

<strong>Caso 3 (Datos Históricos)</strong>: Un perito desea determinar
si existe alguna relación entre el costo de una propiedad y el valor
registrado en el predial. Para ello selecciona \(10\) propiedades de una
base de datos y registra el valor de la propiedad para verificar el
valor registrado en el predial obteniendo los siguientes resultados en
millones de pesos

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<th>
Costo propiedad
</th>
<th>
Valor predial
</th>
</thead>
<tbody>
<tr>
<td>
214.199
</td>
<td>
112.361
</td>
</tr>
<tr>
<td>
284.061
</td>
<td>
238.541
</td>
</tr>
<tr>
<td>
239.673
</td>
<td>
159.144
</td>
</tr>
<tr>
<td>
269.327
</td>
<td>
212.431
</td>
</tr>
<tr>
<td>
192.689
</td>
<td>
74.433
</td>
</tr>
<tr>
<td>
250.846
</td>
<td>
178.492
</td>
</tr>
<tr>
<td>
260.795
</td>
<td>
196.032
</td>
</tr>
<tr>
<td>
246.879
</td>
<td>
172.886
</td>
</tr>
<tr>
<td>
238.412
</td>
<td>
156.830
</td>
</tr>
<tr>
<td>
223.949
</td>
<td>
191.174
</td>
</tr>
</tbody>
</table>
<ul>
<strong>Interés - Objetivos</strong>
<li>
Ajustar un modelo de regresión que explique el valor comercial de la
propiedad en función del valor del predial
</li>
<li>
Predecir el valor de una propiedad cuyo valor en el predial es de
\(180\) millones de pesos.
</li>
</ul>
<strong>Nota:</strong> Note que en este último caso, el costo de la
propiedad \(Y\), puede estar determinada por otras variables además del
predial, pero inicialmente solo nos concentraremos en la relación lineal
entre el costo y el predial.
</li>
</ol>

### Regresión Lineal Simple

Si se supone que la relación entre `$Y$` y `$X$` es lineal, un modelo
adecuado estaría dado por

$$\begin{align*}Y=\beta_0 + \beta_1 X+ \varepsilon \quad \quad (I)\end{align*}$$


donde

- `$\beta_0$` y `$\beta_1$`: son dos constantes desconocidas denominadas
  parámetros del modelo, estimados a partir de los datos.
- `$\beta_0$` representa el intercepto.
- `$\beta_1$` representa la pendiente.
- `$\varepsilon$` representa al componente de error aleatorio denominado
  error estadístico, el cual explica por qué el modelo de regresión
  lineal simple no ajusta exactamente los datos.

**Nota:** Es de anotar que el término de error `$\varepsilon$` contiene
todos los efectos de otras variables que no fueron consideradas en el
modelo, errores de medición u otras consideraciones no tenidas en cuenta
por el investigador.

#### Supuestos del modelo de regresión lineal simple

1.  Se tiene una muestra aleatoria de `$n$` parejas
    `$(y_1, x_1), (y_2, x_2), \ldots, (y_n, x_n)$`, en donde el objetivo
    principal del análisis de regresión es encontrar la recta que mejor
    ajuste a los pares de observaciones, y por tanto se supone que las
    parejas satisfacen el modelo `$(I)$`, tal que
    
$$\begin{align*}y_i=\beta_0 + \beta_1 x_i+ \varepsilon_i \quad \text{ para } i =0,1,2, \ldots, n \quad \quad (II)\end{align*}$$

    donde `$y_i$` es la i-ésima observación de la variable `$Y$`, dado
    que `$X$` es igual a `$x_i$`.

2.  Del modelo `$(II)$` suponga que las `$\varepsilon_i$` son variables
    aleatorias independientes con media `$\mathbb{E}(\varepsilon_i)=0$`
    y varianza `$Var(\varepsilon_i)=\sigma^2$`, de tal forma que
    
$$\begin{align*}\mathbb{E}(y_i)=\beta_0 + \beta_1 x_i+ \mathbb{E}(\varepsilon_i) = \beta_0 + \beta_1 x_i\end{align*}$$

    y
    
$$\begin{align*}Var(y_i)=Var(\varepsilon_i) = \sigma^2\end{align*}$$

    en donde, si además se cumple que
    `$\varepsilon_i\sim N(0,\sigma^2)$`, entonces se tendrá que
    
$$\begin{align*}y_i\sim N(\beta_0+\beta_1x_i, \sigma^2)\end{align*}$$


### Estimación de parámetros

El objetivo de un modelo de regresión será entonces estimar los
parámetros `$\beta_0, \beta_1, \sigma^2$` del modelo lineal, y para ello
puede recurrirse a diferentes métodos, entre los cuales destaca el
método de Máxima Verosimilitud y el método de mínimos cuadrados.

#### Método de Máxima Verosimiliud

Bajo el supuesto de que
`$\varepsilon \stackrel{iid}{\sim} N(0,\sigma^2)$`, entonces
`$y_i|x_i \stackrel{iid}{\sim} N(\beta_0 + \beta_1 x_i, \sigma^2)$`,
luego la función de verosimilitud asociada a los pares `$(y_1, x_1)$`,
`$(y_2, x_2)$`, `$\ldots$`, `$ (y_n,x_n)$` está dada por

$$\begin{align*}L(\beta_0, \beta_1, \sigma^2; (y_i, x_i)) &= \prod_{i=1}^n f(y_i; \beta_0, \beta_1, \sigma^2)\\   &= \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sqrt{\sigma^2}}e^{-\frac{1}{2}\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{\sigma^2}}\end{align*}$$


Entonces, al maximizar la función de probabilidad tal como se enseño en
la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase08.html#método-de-máxima-verosimilitud" target="\_blank">Clase
08</a> se encontrará que los estimadores de `$\beta_0$`, `$\beta_1$` y
`$\sigma^2$` que maximizan `$L(\cdot)$` están dados por


$$\begin{align*}\hat{\beta}_0&=\bar{Y} - \hat{\beta}_1\bar{X}\\   \hat{\beta}_1&=\frac{S_{xy}}{S_{xx}}= \frac{\sum_{i=1}^n (x_i - \bar{X})(y_i - \bar{Y})}{\sum_{i=1}^{n}(x_i - \bar{X})^2} = \frac{\sum_{i=1}^{n}(x_i-\bar{X}) y_i}{\sum_{i=1}^{n} (x_i - \bar{X})^2}\\    \hat{\sigma}^2&= \frac{\sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2}{n}\end{align*}$$


<button id="Show1" class="btn btn-secondary">
Mostrar Demostración
</button>
<button id="Hide1" class="btn btn-info">
Ocultar Demostración
</button>
<main id="botoncito1">
<h3 data-toc-skip>
Demostración
</h3>
<p>

Dado que resulta más sencillo maximizar el logaritmo natural de la
función de verosimilitud que la función de verosimilitud misma, y que
ambas funciones alcanzan su máximo en el mismo punto por ser el
logaritmo una función monótona creciente, se procede a calcular la
función de log-verosimilitud, tal que

$$\begin{align*}
  \ell(\beta_0, \beta_1, \sigma^2) &= \ln L(\beta_0, \beta_1, \sigma^2; (y_i, x_i))\\
  &= \ln \left[\prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sqrt{\sigma^2}}e^{-\frac{1}{2}\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{\sigma^2}}\right]\\
  &= -\frac{n}{2}\ln(2\pi) - \frac{n}{2}\ln(\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2
\end{align*}$$

Ahora, para encontrar los estimadores que maximizan la función
\(\ell(\cdot)\), se deriva parcialmente la función de log-verosimilitud
respecto a cada uno de los parámetros y se iguala a cero. Derivando
inicialmente respecto a \(\beta_0\) se tiene

$$\begin{align*}
  \frac{\partial \ell}{\partial \beta_0} = \frac{1}{\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) = 0
\end{align*}$$

de donde se obtiene que

$$\begin{align*}
  \sum_{i=1}^n y_i - n\hat{\beta}_0 - \hat{\beta}_1\sum_{i=1}^n x_i &= 0\\
  n\bar{Y} - n\hat{\beta}_0 - n\hat{\beta}_1\bar{X} &= 0
\end{align*}$$

y por tanto

$$\begin{align*}
  \hat{\beta}_0 = \bar{Y} - \hat{\beta}_1\bar{X}
\end{align*}$$

Derivando ahora respecto a \(\beta_1\) se tiene

$$\begin{align*}
  \frac{\partial \ell}{\partial \beta_1} = \frac{1}{\sigma^2}\sum_{i=1}^n x_i(y_i - \beta_0 - \beta_1 x_i) = 0
\end{align*}$$

de donde se obtiene que

$$\begin{align*}
  \sum_{i=1}^n x_iy_i - \hat{\beta}_0\sum_{i=1}^n x_i - \hat{\beta}_1\sum_{i=1}^n x_i^2 = 0
\end{align*}$$

y al reemplazar \(\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1\bar{X}\) en la
expresión anterior

$$\begin{align*}
  \sum_{i=1}^n x_iy_i - (\bar{Y} - \hat{\beta}_1\bar{X})n\bar{X} - \hat{\beta}_1\sum_{i=1}^n x_i^2 &= 0\\
  \sum_{i=1}^n x_iy_i - n\bar{X}\bar{Y} - \hat{\beta}_1\left(\sum_{i=1}^n x_i^2 - n\bar{X}^2\right) &= 0
\end{align*}$$

Entonces, recordando que
\(S_{xy}=\sum_{i=1}^n (x_i - \bar{X})(y_i - \bar{Y}) = \sum_{i=1}^n x_iy_i - n\bar{X}\bar{Y}\)
y que
\(S_{xx}=\sum_{i=1}^{n}(x_i - \bar{X})^2 = \sum_{i=1}^n x_i^2 - n\bar{X}^2\),
se concluye que

$$\begin{align*}
  \hat{\beta}_1 = \frac{\sum_{i=1}^n x_iy_i - n\bar{X}\bar{Y}}{\sum_{i=1}^n x_i^2 - n\bar{X}^2} = \frac{S_{xy}}{S_{xx}}
\end{align*}$$

Finalmente, derivando la función de log-verosimilitud respecto a
\(\sigma^2\) se tiene

$$\begin{align*}
  \frac{\partial \ell}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 = 0
\end{align*}$$

y al multiplicar ambos lados de la igualdad por \(2\hat{\sigma}^4\) y
evaluar en \(\hat{\beta}_0\) y \(\hat{\beta}_1\) se obtiene

$$\begin{align*}
  -n\hat{\sigma}^2 + \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 = 0
\end{align*}$$

concluyendo entonces que

$$\begin{align*}
  \hat{\sigma}^2 = \frac{\sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2}{n}
\end{align*}$$
</p>
</main>

#### Método de Mínimos Cuadrados

Sea una muestra aleatoria `$(y_1, x_1), (y_2, x_2), \ldots, (y_n, x_n)$`
a partir de la cual se desea ajustar el siguiente modelo

$$\begin{align*}y_i=\beta_0 + \beta_1 x_i+ \varepsilon_i\end{align*}$$


donde `$\varepsilon_i$` es una variable aleatoria desconocida con
distribución de probabilidad independiente e idénticamente distribuida
con media `$\mathbb{E}(\varepsilon_i)=0$` y varianza
`$Var(\varepsilon_i)=\sigma^2$`.

Entonces si denotamos a `$\hat{\beta}_0, \hat{\beta}_1$`, los
estimadores de los parámetros `$\beta_0, \beta_1$`, entonces la recta de
regresión estimada será

$$\begin{align*}\hat{y_i}=\hat{\beta}_0 + \hat{\beta}_1 x_i\end{align*}$$


donde `$\hat{y}_i$` es el estimador de `$\mathbb{E}(y_i|x=x_i)$`.
Entonces la diferencia entre `$y_i$` y `$\hat{y_i}$` se conoce como
error de estimación del ajuste `$e_i$` y está dado por

$$\begin{align*}e_i = y_i - \hat{y}_i = y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i\end{align*}$$


**Supuestos**

- `$e_i\sim N(0,\sigma^2_e)$`, varianza constante (homocedasticidad)
- `$cov(e_i. e_j)=0$` para todo `$i \neq j$`.

**Cálculo estimadores**

A partir de la ecuación anterior será posible encontrar los estimadores
`$\hat{\beta}_0$` y `$\hat{\beta}_1$` mediante la minimización de la
suma de los cuadrados de los errores.


$$\begin{align*}SCE=\sum_{i=1}^n e_i^2 = \sum_{i=1}^n (y_i - \hat{y}_i)^2 =   \sum_{i=1}^n (y_i -\hat{\beta}_0 - \hat{\beta}_1 x_i)^2\end{align*}$$


de la forma


$$\begin{align*}\frac{\partial SCE}{\partial \hat{\beta}_i} = 0\end{align*}$$


Al resolver el sistema de ecuaciones se obtendrá que


$$\begin{align*}\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i-\bar{X})(y_i-\bar{Y})}{\sum_{i=1}^n (x_i-\bar{X})^2} = \frac{S_{xy}}{S_{xx}}\\ \hat{\beta}_0 &= \bar{Y} - \hat{\beta}_1\bar{X}\end{align*}$$


<button id="Show2" class="btn btn-secondary">
Mostrar Demostración
</button>
<button id="Hide2" class="btn btn-info">
Ocultar Demostración
</button>
<main id="botoncito2">
<h3 data-toc-skip>
Demostración
</h3>
<p>

Para encontrar los valores de \(\hat{\beta}_0\) y \(\hat{\beta}_1\) que
minimizan la suma de los cuadrados de los errores, se deriva
parcialmente la función \(SCE\) respecto a cada uno de los estimadores y
se iguala a cero. Derivando inicialmente respecto a \(\hat{\beta}_0\) se
tiene

$$\begin{align*}
  \frac{\partial SCE}{\partial \hat{\beta}_0} = -2\sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0
\end{align*}$$

mientras que al derivar respecto a \(\hat{\beta}_1\) se tiene

$$\begin{align*}
  \frac{\partial SCE}{\partial \hat{\beta}_1} = -2\sum_{i=1}^n x_i(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0
\end{align*}$$

Al simplificar ambas expresiones se obtiene el sistema de ecuaciones
conocido como <strong>ecuaciones normales</strong>, dado por

$$\begin{align*}
  n\hat{\beta}_0 + \hat{\beta}_1\sum_{i=1}^n x_i &= \sum_{i=1}^n y_i\\
  \hat{\beta}_0\sum_{i=1}^n x_i + \hat{\beta}_1\sum_{i=1}^n x_i^2 &= \sum_{i=1}^n x_iy_i
\end{align*}$$

De la primera ecuación normal, al dividir ambos lados por \(n\), se
obtiene directamente que

$$\begin{align*}
  \hat{\beta}_0 = \bar{Y} - \hat{\beta}_1\bar{X}
\end{align*}$$

y al sustituir este resultado en la segunda ecuación normal se tiene

$$\begin{align*}
  (\bar{Y} - \hat{\beta}_1\bar{X})n\bar{X} + \hat{\beta}_1\sum_{i=1}^n x_i^2 &= \sum_{i=1}^n x_iy_i\\
  \hat{\beta}_1\left(\sum_{i=1}^n x_i^2 - n\bar{X}^2\right) &= \sum_{i=1}^n x_iy_i - n\bar{X}\bar{Y}
\end{align*}$$

de donde se concluye que

$$\begin{align*}
  \hat{\beta}_1 = \frac{\sum_{i=1}^n x_iy_i - n\bar{X}\bar{Y}}{\sum_{i=1}^n x_i^2 - n\bar{X}^2} = \frac{\sum_{i=1}^n (x_i-\bar{X})(y_i-\bar{Y})}{\sum_{i=1}^n (x_i-\bar{X})^2} = \frac{S_{xy}}{S_{xx}}
\end{align*}$$

</p>
</main>

**Nota sobre estimador** `$\sigma^2$`

Dado que el método de mínimos cuadrados no posee un estimador para la
varianza `$\sigma^2$`, se emplea entonces un estimador insesgado el cual
estará dado por

$$\begin{align*}\sigma^2_e &=\frac{1}{n-2}\sum_{i=1}^n e^2_i \\             &= \frac{1}{n-2}\sum_{i=1}^n (y_i - \hat{y}_i)^2 \\              &= \frac{S_{yy} - \hat{\beta}_1 S_{xy}}{n-2}\end{align*}$$


### Propiedades de `$\hat{\beta}_0, \hat{\beta}_1$`

<ul>
<li>
Los estimadores para \(\beta_0\) y \(\beta_1\) coinciden tanto para el
método de máxima verosimilitud cómo para el método de mínimos cuadrados.
</li>
<li>
Observe que los estimadores \(\hat{\beta}_0\) y \(\hat{\beta}_1\) pueden
ser reescritos como
</li>
</ul>


$$\begin{align*}\hat{\beta}_1 &= \sum_{i=1}^{n} y_ic_i \qquad \text{ donde } c_i=\frac{(x_i-\bar{X})}{\sum_{i=1}^{n}(x_i - \bar{X})^2}\\   \hat{\beta}_0 &= \sum_{i=1}^{n} y_i di \qquad \text{ donde } d_i=\left(\frac{1}{n} - c_i\bar{X}\right)\end{align*}$$


<ul>
<li>
Además, se puede probar que
<ul>
<li>
\(\sum_{i=1}^{n}c_i=0\)
</li>
<li>
\(\sum_{i=1}^{n}d_i=1\)
</li>
<li>
\(\sum_{i=1}^{n}c_ix_i=1\)
</li>
<li>
\(\sum_{i=1}^{n}d_ix_i=0\)
</li>
<li>
\(\sum_{i=1}^{n}c_i^2=\frac{1}{\sum_{i=1}^{n} (x_i-\bar{X})^2} = \frac{1}{S_{xx}}\)
</li>
<li>
\(\sum_{i=1}^{n}d_i^2=\frac{\sum_{i=1}^{n}x_i^2}{n\sum_{i=1}^{n} (x_i-\bar{X})^2} = \frac{\sum_{i=1}^{n}x_i^2}{nS_{xx}} = \frac{S_{xx} + n\bar{X}^2}{nS_{xx}} = \frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\)
</li>
</ul>
</li>
<li>
Basado en estas condiciones, se presentan algunas propiedades que
cumplen los estimadores \(\hat{\beta}_0, \hat{\beta}_1\).
<ul>
<li>
\(\mathbb{E}(\hat{\beta}_0) = \beta_0\)
</li>
<li>
\(\mathbb{E}(\hat{\beta}_1) = \beta_1\)
</li>
<li>
\(Var(\hat{\beta}_0) = \sigma^2 \left[\frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\right]\)
</li>
<li>
\(Var(\hat{\beta}_1) = \frac{1}{S_{xx}}\sigma^2\)
</li>
</ul>
</li>
</ul>
<button id="Show3" class="btn btn-secondary">
Mostrar Demostración
</button>
<button id="Hide3" class="btn btn-info">
Ocultar Demostración
</button>
<main id="botoncito3">
<h3 data-toc-skip>
Demostración
</h3>
<p>
Para la demostración de las cuatro propiedades se emplearán las formas
lineales \(\hat{\beta}_1 = \sum_{i=1}^{n} c_iy_i\) y
\(\hat{\beta}_0 = \sum_{i=1}^{n} d_iy_i\), junto con los resultados
\(\sum_{i=1}^{n}c_i=0\), \(\sum_{i=1}^{n}c_ix_i=1\),
\(\sum_{i=1}^{n}c_i^2=\frac{1}{S_{xx}}\) y
\(\sum_{i=1}^{n}d_i^2=\frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\), además
de recordar que bajo los supuestos del modelo
\(\mathbb{E}(y_i)=\beta_0+\beta_1x_i\), \(Var(y_i)=\sigma^2\) y que las
observaciones \(y_i\) son independientes entre sí.
</p>
<h4 data-toc-skip>
Demostración Esperanza de \(\hat{\beta}_1\)
</h4>
<p>

Dado que los \(c_i\) son constantes (ya que dependen únicamente de los
valores \(x_i\)), al aplicar el operador esperanza sobre
\(\hat{\beta}_1\) se tiene

$$\begin{align*}
  \mathbb{E}(\hat{\beta}_1) &= \mathbb{E}\left(\sum_{i=1}^{n} c_iy_i\right) = \sum_{i=1}^{n} c_i\mathbb{E}(y_i) = \sum_{i=1}^{n} c_i(\beta_0 + \beta_1x_i)\\
  &= \beta_0\sum_{i=1}^{n} c_i + \beta_1\sum_{i=1}^{n} c_ix_i\\
  &= \beta_0(0) + \beta_1(1)\\
  &= \beta_1
\end{align*}$$
</p>
<h4 data-toc-skip>
Demostración Esperanza de \(\hat{\beta}_0\)
</h4>
<p>

Empleando la definición \(\hat{\beta}_0=\bar{Y} - \hat{\beta}_1\bar{X}\)
junto con el resultado anterior, y notando que
\(\mathbb{E}(\bar{Y}) = \frac{1}{n}\sum_{i=1}^{n}\mathbb{E}(y_i) = \frac{1}{n}\sum_{i=1}^{n}(\beta_0 + \beta_1x_i) = \beta_0 + \beta_1\bar{X}\),
se tiene

$$\begin{align*}
  \mathbb{E}(\hat{\beta}_0) &= \mathbb{E}(\bar{Y} - \hat{\beta}_1\bar{X}) = \mathbb{E}(\bar{Y}) - \bar{X}\mathbb{E}(\hat{\beta}_1)\\
  &= \beta_0 + \beta_1\bar{X} - \bar{X}\beta_1\\
  &= \beta_0
\end{align*}$$
</p>
<h4 data-toc-skip>
Demostración Varianza de \(\hat{\beta}_1\)
</h4>
<p>

Dado que las observaciones \(y_i\) son independientes, la varianza de la
suma es la suma de las varianzas, y por tanto

$$\begin{align*}
  Var(\hat{\beta}_1) &= Var\left(\sum_{i=1}^{n} c_iy_i\right) \\
  &= \sum_{i=1}^{n} c_i^2Var(y_i) \\
  &= \sigma^2\sum_{i=1}^{n} c_i^2\\
  &= \sigma^2 \frac{1}{S_{xx}}\\
  &= \frac{\sigma^2}{S_{xx}}
\end{align*}$$
</p>
<h4 data-toc-skip>
Demostración Varianza de \(\hat{\beta}_0\)
</h4>
<p>

De forma análoga al caso anterior, empleando la forma lineal
\(\hat{\beta}_0 = \sum_{i=1}^{n} d_iy_i\) y la independencia de las
observaciones, se tiene

$$\begin{align*}
  Var(\hat{\beta}_0) &= Var\left(\sum_{i=1}^{n} d_iy_i\right) = \sum_{i=1}^{n} d_i^2Var(y_i) = \sigma^2\sum_{i=1}^{n} d_i^2
\end{align*}$$

donde, al desarrollar la suma \(\sum_{i=1}^{n} d_i^2\) empleando la
definición \(d_i = \frac{1}{n} - c_i\bar{X}\), se obtiene

$$\begin{align*}
  \sum_{i=1}^{n} d_i^2 &= \sum_{i=1}^{n} \left(\frac{1}{n} - c_i\bar{X}\right)^2 = \sum_{i=1}^{n} \left(\frac{1}{n^2} - \frac{2c_i\bar{X}}{n} + c_i^2\bar{X}^2\right)\\
  &= \frac{n}{n^2} - \frac{2\bar{X}}{n}\sum_{i=1}^{n}c_i + \bar{X}^2\sum_{i=1}^{n}c_i^2\\
  &= \frac{1}{n} - \frac{2\bar{X}}{n}(0) + \bar{X}^2\frac{1}{S_{xx}}\\
  &= \frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}
\end{align*}$$

y por tanto se concluye que

$$\begin{align*}
  Var(\hat{\beta}_0) = \sigma^2\left[\frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\right]
\end{align*}$$
</p>
</main>