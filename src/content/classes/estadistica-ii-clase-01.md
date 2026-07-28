---
title: "Clase 20"
course: "estadistica-ii"
order: 24
classType: "clase"
description: "Análisis de Regresión Lineal Simple - Análisis de varianza - Coeficiente de determinación Análisis de Regresión Lineal Múltiple - Análisis de varianza - Coeficiente de determinación Respuesta media y predicción de nuevas observaciones - Respuesta media en regresión lineal simple - Predicción de nuevas observaciones en regresión lineal simple - Respuesta media en regresión lineal múltiple - Predicción de nuevas observaciones en regresión lineal múltiple"
math: true
bibliography: "../../referencias.bib"
---

## Análisis de Regresión Lineal Simple

### Análisis de varianza

Una forma equivalente de hacer la prueba de significancia de la
regresión

$$\begin{align*}H_0:\beta_1=0 \text{ vs } H_1:\beta_1\neq0\end{align*}$$


es a partir del análisis de varianza, donde se descompone la varianza
total de `$Y$` (`$SCT$`) en dos fuentes, la variabilidad explicada por
el modelo (`$SCR$`) y la variabilidad no explicada por el modelo
(`$SCE$`).

- `$SCT = \sum_{i=1}^n (y_i-\bar{Y})^2$`
- `$SCR = \sum_{i=1}^n (\hat{y}_i-\bar{Y})^2$`
- `$SCE = \sum_{i=1}^n (y_i-\hat{y}_i)^2$`

Observe que las diferencias de las `$y_i$` con respecto a su media
`$\bar{Y}$` pueden escribirse como


$$\begin{align*}(y_i - \bar{Y}) = (\hat{y}_i - \bar{Y}) + (\underbrace{y_i - \hat{y_i}}_{e_i})\end{align*}$$


lo cual puede reescribirse como

$$\begin{align*}SCT = SCR + SCE\end{align*}$$


al elevar al cuadrado y aplicar la función de sumatoria a ambos lados de
la ecuación.

**Nota**
<ol>
<li>
Para llegar a la ecuación anterior se puede verificar que el término
cruzado se anula, tal que
</li>

$$\begin{align*}
 \sum_{i=1}^{n}(\hat{y}_i - \bar{Y})e_i = \sum_{i=1}^{n}(\hat{y}_i - \bar{Y}) (y_i - \hat{y_i}) = 0
\end{align*}$$

<li>
Las expresiones de \(SCT\), \(SCR\) y \(SCE\) pueden ser reescritas como
$$\begin{align*}
 &SCT = \sum_{i=1}^{n}y_i^2 - n\bar{Y}^2\\
 &SCR = \hat{\beta}_1S_{xy} = \hat{\beta}_1^2 S_{xx}\\
\end{align*}$$ y luego se podrá calcular \(SCE\) como $$\begin{align*}
 &SCE = SCT - SCR
\end{align*}$$
</li>
<li>
Cada suma de cuadrados tiene asociado un número de grados de libertad
diferentes, tal que $$\begin{align*}
 \underbrace{SCT}_{n-1} = \underbrace{SCR}_{1} + \underbrace{SCE}_{n-2}
\end{align*}$$
</li>
</ol>

con base en lo anterior es posible construir estimadores independientes
de `$\sigma^2$`, usando la respectiva suma de cuadrados dividida entre
sus grados de libertad, denominados cuadrados medios, tal que


$$\begin{align*}CMR = \frac{SCR}{1} \quad \quad CME = \frac{SCE}{n-2}\end{align*}$$


finalmente se establece el estadístico de prueba bajo el supuesto de
normalidad

$$\begin{align*}F_c= \frac{CMR}{CME} = \frac{SCR / 1}{SCE / (n-2)} \sim F_{1, n-2}\end{align*}$$


En donde el criterio de decisión estará dado por la región crítica, la
cual está dada por

$$\begin{align*}RC:\{F|F>F_{\alpha, 1, n-2}\}\end{align*}$$


o por el P-valor, el cual está dado por

$$\begin{align*}\text{P-valor} =  \mathbb{P}(F_{1,n-2} > F_c)\end{align*}$$


donde si P-valor es menor al nivel de significancia `$\alpha$` se
rechaza la hipótesis nula y se concluye que el modelo lineal propuesto
es significativo para explicar el comportamiento de `$Y$`.

Estos resultados suelen resumirse en la denominada **tabla ANOVA**, dada
por

<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<th>
Fuente de variación
</th>
<th>
Grados de libertad
</th>
<th>
Suma de cuadrados
</th>
<th>
Cuadrado medio
</th>
<th>
Estadístico F
</th>
<th>
P-valor
</th>
</thead>
<tbody>
<tr>
<td>
Regresión
</td>
<td>
<script type="math/tex">1</script>
</td>
<td>
<script type="math/tex">SCR</script>
</td>
<td>
<script type="math/tex">CMR = \frac{SCR}{1}</script>
</td>
<td>
<script type="math/tex">F_c = \frac{CMR}{CME}</script>
</td>
<td>
<script type="math/tex">\mathbb{P}(F_{1,n-2} > F_c)</script>
</td>
</tr>
<tr>
<td>
Error
</td>
<td>
<script type="math/tex">n-2</script>
</td>
<td>
<script type="math/tex">SCE</script>
</td>
<td>
<script type="math/tex">CME = \frac{SCE}{n-2}</script>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Total
</td>
<td>
<script type="math/tex">n-1</script>
</td>
<td>
<script type="math/tex">SCT</script>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

**Nota:** En el caso de la regresión lineal simple, la prueba F del
análisis de varianza es equivalente a la prueba de significancia
individual `$H_0:\beta_1=0$` vista en la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase19.html" target="\_blank">Clase
19</a>, ya que se cumple que `$F_c = t^2_{\hat{\beta}_1}$`.

### Coeficiente de determinación

Una forma de medir la bondad del ajuste del modelo de regresión es
mediante el coeficiente de determinación `$R^2$`, el cual se define como

$$\begin{align*}R^2=\frac{SCR}{SCT} = 1 - \frac{SCE}{SCT}\end{align*}$$


y representa la proporción de variación total de `$Y$`, explicada por su
relación lineal con `$X$`.

Dado que `$R^2$` se encuentra entre `$0$` y `$1$`, entonces valores
cercanos a cero indican que la relación entre `$X$` y `$Y$` es muy
pobre, mientras que, valores cercanos a uno, indican que la recta
ajustada se aproxima relativamente bien a los puntos.

**Nota**: Un `$R^2$` alto no garantiza necesariamente que el modelo
regresión lineal ajustado sea adecuado para los datos, debido a que hay
factores que afectan a este valor, como lo es el número de datos usados.

## Análisis de Regresión Lineal Múltiple

### Análisis de varianza

Para el caso del modelo de regresión lineal múltiple, el análisis de
varianza permite realizar la **prueba de significancia global de la
regresión** mencionada en la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase19.html" target="\_blank">Clase
19</a>, la cual determina si existe una relación lineal entre la
variable respuesta `$Y$` y **al menos una** de las variables
explicativas `$X_1, X_2, \ldots, X_k$`, mediante el siguiente juego de
hipótesis

$$\begin{align*}H_0&: \beta_1 = \beta_2 = \cdots = \beta_k = 0\\  H_1&: \beta_j \neq 0 \quad \text{ para al menos un } j\end{align*}$$


La descomposición de la variabilidad total es exactamente la misma del
caso simple, `$SCT = SCR + SCE$`, en donde las sumas de cuadrados pueden
calcularse empleando la notación matricial de la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase18.html" target="\_blank">Clase
18</a>, tal que

- `$SCT = \mathbf{Y}^\top\mathbf{Y} - n\bar{Y}^2$`, con `$n-1$` grados
  de libertad.
- `$SCR = \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y} - n\bar{Y}^2$`,
  con `$k$` grados de libertad, ya que el modelo posee `$k$` variables
  explicativas.
- `$SCE = \mathbf{Y}^\top\mathbf{Y} - \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y}$`,
  con `$n-k-1$` grados de libertad.

en donde, bajo la hipótesis nula, el estadístico de prueba sigue una
distribución F con `$k$` y `$n-k-1$` grados de libertad, tal que

$$\begin{align*}F_c = \frac{CMR}{CME} = \frac{SCR/k}{SCE/(n-k-1)} \sim F_{k, \, n-k-1}\end{align*}$$


Dado que valores grandes del estadístico `$F_c$` indican que la
variabilidad explicada por el modelo es grande en comparación con la
variabilidad no explicada, la región crítica de la prueba es de una sola
cola y está dada por

$$\begin{align*}RC:\{F|F > F_{\alpha, \, k, \, n-k-1}\}\end{align*}$$


mientras que el P-valor está dado por

$$\begin{align*}\text{P-valor}= \mathbb{P}(F_{k, \, n-k-1} > F_c)\end{align*}$$


en donde si `$F_c \in RC$`, o de forma equivalente, si el P-valor es
menor al nivel de significancia `$\alpha$`, se rechaza `$H_0$`.

**Nota**

- Rechazar `$H_0$` en la prueba de significancia global permite concluir
  que **al menos una** de las variables explicativas aporta
  significativamente a la explicación de `$Y$`, es decir, que el modelo
  es globalmente significativo. Sin embargo, la prueba no indica
  **cuáles** son las variables significativas, por lo cual, una vez
  rechazada la hipótesis nula global, se debe recurrir a las pruebas de
  significancia individual vistas en la
  <a href="https://jiperezga.github.io/EstadisticaII/EstIIClase19.html" target="\_blank">Clase
  19</a> para identificarlas.
- No rechazar `$H_0$` indica que ninguna de las variables explicativas
  del modelo tiene una relación lineal significativa con la variable
  respuesta, y por tanto el modelo planteado no es adecuado.
- Note que la tabla ANOVA del caso simple corresponde al caso particular
  en que `$k=1$`.
- En <tt>R</tt>, esta prueba corresponde al <tt>F-statistic</tt> y su
  respectivo P-valor reportados en la última línea de la salida de la
  función <tt>summary()</tt>, mientras que la tabla ANOVA puede
  obtenerse mediante la función <tt>anova(modelo)</tt>.

### Coeficiente de determinación ajustado

En el modelo de regresión lineal múltiple, el coeficiente de
determinación `$R^2 = \frac{SCR}{SCT}$` presenta el inconveniente de que
**siempre aumenta al agregar variables al modelo**, sean éstas
relevantes o no, por lo cual no resulta adecuado para comparar modelos
con diferente número de variables explicativas.

Por tal razón, se prefiere el **coeficiente de determinación ajustado**,
el cual está dado por

$$\begin{align*}R^2_{adj} = 1 - \frac{SCE/(n-k-1)}{SCT/(n-1)} = 1 - (1-R^2)\frac{n-1}{n-k-1}\end{align*}$$


el cual penaliza la inclusión de variables que no aportan a la
explicación de `$Y$`, ya que al agregar una variable irrelevante al
modelo, la disminución de la `$SCE$` no compensa la pérdida de un grado
de libertad, y por tanto el `$R^2_{adj}$` disminuye. De esta forma, el
`$R^2_{adj}$` sí permite comparar modelos con diferente número de
variables explicativas.

Ambos coeficientes son reportados por la función <tt>summary()</tt> de
<tt>R</tt> como <tt>Multiple R-squared</tt> y <tt>Adjusted
R-squared</tt> respectivamente.

## Respuesta media y predicción de nuevas observaciones

Una importante utilidad del modelo de regresión es que nos permite la
estimación de la media de la distribución de `$Y$` para un valor dado de
`$X$`, y además nos permite realizar predicciones sobre una nueva
variable `$y_0$` correspondiente a un nivel especificado de variables
`$x_0$`.

### Respuesta media en regresión lineal simple

Considere un valor determinado `$x = x_0$`, y el objetivo será estimar
su respuesta media `$\mathbb{E}(Y|x_0)$`. La estimación puede ser
puntual o por intervalo, y donde, **la estimación es válida solo para
valores de `$x_0$` dentro del rango de valores originales de `$X$`, que
se usaron para ajustar el modelo**.

Entonces el estimador puntual de la respuesta media de `$Y$` dado
`$x_0$`

$$\begin{align*}\hat{y_0}= \hat{\mathbb{E}}(Y|x_0)= \hat{\beta}_0 + \hat{\beta}_1 x_0\end{align*}$$


donde se puede probar que

$$\begin{align*}\mathbb{E}(\hat{y_0}) &= \beta_0 + \beta_1 x_0 \\  Var(\hat{y_0}) &= \sigma^2\left[\frac{1}{n} + \frac{(x_0 - \bar{X})^2}{S_{xx}}\right]\end{align*}$$


en donde la varianza `$\sigma^2$`, al ser desconocida, se estima
mediante `$\hat{\sigma}^2_e$`.

Además, para un nivel de confianza del `$100(1-\alpha)\%$` un intervalo
de confianza para la respuesta media será de la forma


$$\begin{align*}\hat{y}_0 \pm t_{\frac{\alpha}{2}, n-2} \sqrt{\hat{\sigma}^2_e\left[\frac{1}{n}+ \frac{(x_0 - \bar{X})^2}{S_{xx}}\right]}\end{align*}$$


Es de anotar que si se decide construir un intervalo de confianza para
todos los posibles valores de X, se obtendrán las bandas de confianza
del `$100(1-\alpha)\%$` para la respuesta media `$\beta_0+\beta_1x_i$`.
En <tt>R</tt>, este intervalo puede obtenerse mediante la función
<tt>predict(modelo, newdata, interval = “confidence”)</tt>.

### Predicción de nuevas observaciones en regresión lineal simple

Suponga que `$x_0$` es un valor de interés para el cual se desea
predecir una nueva observación, entonces para obtener un valor único
`$y_0$`, podremos utilizar la fórmula de la recta de regresión tal que,
al igual que en el caso de la respuesta media, la estimación puntual de
`$Y$` dado `$x_0$` será

$$\begin{align*}\hat{y_0}= \hat{\beta}_0 + \hat{\beta}_1 x_0\end{align*}$$


Pero en este caso, al ser un valor predicho, tendremos que estimar la
varianza de la diferencia `$\hat{y}_0 - y_0$`, la cual tiene media

$$\begin{align*}\mathbb{E}(\hat{y_0} - y_0) &=\mathbb{E}[\hat{\beta}_0+\hat{\beta}_1x_0 - (\beta_0 + \beta_1 x_0 +\varepsilon)] = 0\end{align*}$$

y varianza

$$\begin{align*}Var(\hat{y_0} - y_0) &= \sigma^2\left[\frac{1}{n} + \frac{(x_0 - \bar{X})^2}{S_{xx}}\right] + \sigma^2\\   &=\sigma^2\left[1 + \frac{1}{n} + \frac{(x_0 - \bar{X})^2}{S_{xx}}\right]\end{align*}$$


ya que la nueva observación `$y_0$` es independiente de las
observaciones empleadas para ajustar el modelo, y por tanto la varianza
total corresponde a la suma de la varianza de la respuesta media y la
varianza del error de la nueva observación. Nuevamente, al ser
`$\sigma^2$` desconocida, ésta se estima mediante `$\hat{\sigma}^2_e$`.

Entonces, un intervalo de confianza del `$100(1-\alpha)\%$` para un
valor predicho `$y_0$`, denominado **intervalo de predicción**, se puede
construir de la forma


$$\begin{align*}\hat{y}_0 \pm t_{\frac{\alpha}{2}, n-2} \sqrt{\hat{\sigma}^2_e\left[1+\frac{1}{n}+ \frac{(x_0 - \bar{X})^2}{S_{xx}}\right]}\end{align*}$$


Es de anotar que si se decide construir un intervalo de confianza para
todos los posibles valores de X, se obtendrán las bandas de confianza
del `$100(1-\alpha)\%$` para la predicción individual. En <tt>R</tt>,
este intervalo puede obtenerse mediante la función <tt>predict(modelo,
newdata, interval = “prediction”)</tt>.

### Respuesta media en regresión lineal múltiple

Para el caso del modelo de regresión lineal múltiple, suponga que se
desea estimar la respuesta media de `$Y$` en un punto determinado de las
variables explicativas `$x_{01}, x_{02}, \ldots, x_{0k}$`, el cual puede
escribirse en forma vectorial como

$$\begin{align*}\mathbf{x}_0 = \begin{bmatrix} 1 \\ x_{01} \\ x_{02} \\ \vdots \\ x_{0k} \end{bmatrix}\end{align*}$$


en donde el primer elemento igual a `$1$` está asociado al intercepto
del modelo. Entonces, el estimador puntual de la respuesta media de
`$Y$` dado `$\mathbf{x}_0$` estará dado por

$$\begin{align*}\hat{y}_0= \hat{\mathbb{E}}(Y|\mathbf{x}_0)= \mathbf{x}_0^\top\hat{\boldsymbol{\beta}} = \hat{\beta}_0 + \hat{\beta}_1 x_{01} + \hat{\beta}_2 x_{02} + \cdots + \hat{\beta}_k x_{0k}\end{align*}$$


donde, empleando las propiedades de `$\hat{\boldsymbol{\beta}}$` vistas
en la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase18.html" target="\_blank">Clase
18</a>, se puede probar que

$$\begin{align*}\mathbb{E}(\hat{y}_0) &= \mathbf{x}_0^\top\mathbb{E}(\hat{\boldsymbol{\beta}}) = \mathbf{x}_0^\top\boldsymbol{\beta} \\  Var(\hat{y}_0) &= \mathbf{x}_0^\top Var(\hat{\boldsymbol{\beta}})\mathbf{x}_0 = \sigma^2\mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0\end{align*}$$


en donde la varianza `$\sigma^2$`, al ser desconocida, se estima
mediante `$\hat{\sigma}^2_e = \frac{SCE}{n-k-1}$`.

Además, para un nivel de confianza del `$100(1-\alpha)\%$` un intervalo
de confianza para la respuesta media será de la forma


$$\begin{align*}\hat{y}_0 \pm t_{\frac{\alpha}{2}, n-k-1} \sqrt{\hat{\sigma}^2_e \, \mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0}\end{align*}$$


**Note que** en el caso particular en que `$k=1$`, se puede probar que
`$\mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0 = \frac{1}{n} + \frac{(x_0-\bar{X})^2}{S_{xx}}$`,
y por tanto la expresión anterior se reduce al intervalo de confianza de
la respuesta media del modelo de regresión lineal simple.

En <tt>R</tt>, el intervalo de confianza para la respuesta media se
obtienen de la misma forma que en el caso simple, mediante la función
<tt>predict()</tt>, especificando en el argumento <tt>newdata</tt> un
<tt>data.frame</tt> con el valor de cada una de las variables
explicativas del modelo, por ejemplo, <tt>predict(modelo, newdata =
data.frame(x1 = 42, x2 = 4), interval = “confidence”)</tt>.

### Predicción de nuevas observaciones en regresión lineal múltiple

De forma análoga al caso simple, si se desea predecir una nueva
observación `$y_0$` en el punto `$\mathbf{x}_0$`, la estimación puntual
coincide con la de la respuesta media, tal que

$$\begin{align*}\hat{y}_0= \mathbf{x}_0^\top\hat{\boldsymbol{\beta}}\end{align*}$$


Pero en este caso, al ser un valor predicho, se debe considerar la
varianza de la diferencia `$\hat{y}_0 - y_0$`, la cual tiene media

$$\begin{align*}\mathbb{E}(\hat{y}_0 - y_0) =\mathbb{E}[\mathbf{x}_0^\top\hat{\boldsymbol{\beta}} - (\mathbf{x}_0^\top\boldsymbol{\beta} +\varepsilon)] = \mathbf{x}_0^\top\boldsymbol{\beta} - \mathbf{x}_0^\top\boldsymbol{\beta} - \mathbb{E}(\varepsilon) = 0\end{align*}$$

y varianza

$$\begin{align*}Var(\hat{y}_0 - y_0) &= \sigma^2\mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0 + \sigma^2\\   &=\sigma^2\left[1 + \mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0\right]\end{align*}$$


ya que la nueva observación `$y_0$` es independiente de las
observaciones empleadas para ajustar el modelo, y por tanto la varianza
total corresponde a la suma de la varianza de la respuesta media y la
varianza del error de la nueva observación.

Entonces, un intervalo de predicción del `$100(1-\alpha)\%$` para una
nueva observación `$y_0$` se puede construir de la forma


$$\begin{align*}\hat{y}_0 \pm t_{\frac{\alpha}{2}, n-k-1} \sqrt{\hat{\sigma}^2_e\left[1 + \mathbf{x}_0^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_0\right]}\end{align*}$$


En <tt>R</tt>, el intervalo de predicción se obtienen de forma similar
que en el caso simple, mediante la función <tt>predict()</tt>,
especificando en el argumento <tt>newdata</tt> un <tt>data.frame</tt>
con el valor de cada una de las variables explicativas del modelo, por
ejemplo, <tt>predict(modelo, newdata = data.frame(x1 = 42, x2 = 4),
interval = “prediction”)</tt>.

**Nota**

- Observe que, tanto en el caso simple como en el múltiple, el intervalo
  de predicción para una nueva observación siempre será más amplio que
  el intervalo de confianza para la respuesta media en el mismo punto
  `$\mathbf{x}_0$`, ya que además de la incertidumbre asociada a la
  estimación del modelo, incorpora la variabilidad propia del error
  aleatorio `$\varepsilon$` de la nueva observación.
- Ambos intervalos alcanzan su menor amplitud en el centro de los datos
  (en el caso simple, cuando `$x_0 = \bar{X}$`), y se hacen más amplios
  a medida que el punto `$\mathbf{x}_0$` se aleja del centro de las
  observaciones, razón por la cual no se recomienda realizar
  estimaciones ni predicciones por fuera del rango de valores originales
  de las variables explicativas (extrapolación).
- En el caso de la regresión lineal múltiple se debe tener especial
  cuidado con la denominada **extrapolación oculta**, la cual ocurre
  cuando cada una de las coordenadas del punto `$\mathbf{x}_0$` se
  encuentra dentro del rango de su respectiva variable explicativa, pero
  el punto en conjunto se encuentra por fuera de la región que cubren
  las observaciones originales. Por ejemplo, si en los datos originales
  los valores altos de `$X_1$` siempre ocurren junto con valores altos
  de `$X_2$`, predecir en un punto con `$X_1$` alto y `$X_2$` bajo
  constituye una extrapolación, aun cuando ambos valores estén
  individualmente dentro de sus rangos.