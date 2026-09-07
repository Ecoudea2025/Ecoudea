---
title: "Clase 19"
course: "estadistica-ii"
order: 23
classType: "clase"
description: "Análisis de Regresión Lineal Simple - Prueba de hipótesis - Intervalos de confianza Análisis de Regresión Lineal Múltiple - Prueba de hipótesis - Intervalos de confianza Revisión de supuestos del modelo - Linealidad - Normalidad - Homocedasticidad - Independencia - Multicolinealidad"
bibliography: "../../referencias.bib"
---

## Análisis de Regresión Lineal Simple

### Prueba de hipótesis

Note que $\hat{\beta}_0$ y $\hat{\beta}_1$ son combinaciones
lineales de $y_i$, que son normales e independientes, entonces por
propiedades de la distribución normal se obtiene que

$$\begin{align*}\hat{\beta}_0 &\sim N\left(\beta_0, \left[\frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\right]\sigma^2\right)  \\  \hat{\beta}_1 &\sim N\left(\beta_1, \frac{\sigma^2}{S_{xx}}\right)\end{align*}$$


en donde, dado que la varianza $\sigma^2$ es desconocida, se reemplaza
por su estimador insesgado $\sigma^2_e$, y por tanto los estadísticos
asociados dejarán de seguir una distribución normal para seguir una
distribución t-student con $n-2$ grados de libertad.

Entonces, para realizar el contraste de hipótesis $\beta_0$ y
$\beta_1$ de la forma

$$\begin{align*}H_0: \beta_0 = \beta_{00} \quad & \quad H_0: \beta_1 = \beta_{10}\\  H_1: \beta_0 \neq \beta_{00} \quad & \quad H_1: \beta_1 \neq \beta_{10}\\\end{align*}$$


se tendrá que los estadísticos de prueba serían de la forma

$$\begin{align*}t_{\hat{\beta}_{0}}= \frac{\hat{\beta}_0 - \beta_{00}}{\sqrt{\left[\frac{1}{n} + \frac{\bar{X}^2}{S_{xx}}\right]\sigma^2_e}} \quad & \quad t_{\hat{\beta}_{1}}= \frac{\hat{\beta}_1 - \beta_{10}}{\sqrt{\frac{\sigma^2_e}{S_{xx}}}}\end{align*}$$


y para tomar la decisión si se rechaza o no la hipótesis se emplea la
región crítica la cual está dada por

$$\begin{align*}RC:\{t|t < -t_{\frac{\alpha}{2}, n-2} \quad ó \quad t > t_{\frac{\alpha}{2}, n-2}\}\end{align*}$$

en donde si $t_{\hat{\beta}_{i}} \in RC$ para $i=0,1$, se rechaza
$H_0$. Mientras que el P-valor está dado por

$$\begin{align*}\text{P-valor}= 2\mathbb{P}(t_{n-2}\geq |t_{\hat{\beta}_i}|) \quad \text{ para } i = 0,1\end{align*}$$


en donde si P-valor es menor al nivel de significancia $\alpha$,
entonces se rechaza $H_0$.

**Nota**

- Usualmente se quiere probar si $\beta_{0}=0$ y $\beta_{1}=0$, ya
  que se quiere probar la significancia de los parámetros.
- Observe que rechazar $H_0:\beta_{1}=0$, en la prueba de
  significancia, permite afirmar que la relación entre las variables
  $Y$ y $X$ se pueden aproximar mediante una linea recta.
- Si no se rechaza $H_0:\beta_{1}=0$, significa que independiente del
  valor de $X$, el valor de $Y$ será el mismo, y por tanto, no habrá
  una relación lineal entre $Y$ y $X$.
- Estas pruebas son las que reporta la función <tt>summary()</tt> de
  <tt>R</tt> en las columnas <tt>t value</tt> y <tt>Pr(&gt;|t|)</tt>
  para cada uno de los coeficientes del modelo ajustado mediante la
  función <tt>lm()</tt>.

### Intervalo de confianza

El intervalo de confianza para $\beta_0$ está dado por

$$\begin{align*}\hat{\beta}_0 - t_{\frac{\alpha}{2}, n-2} \sqrt{\left(\frac{1}{n}+\frac{\bar{X}^2}{S_{xx}}\right)\sigma^2_{e}} < \beta_0 < \hat{\beta}_0 + t_{\frac{\alpha}{2}, n-2} \sqrt{\left(\frac{1}{n}+\frac{\bar{X}^2}{S_{xx}}\right)\sigma^2_{e}}\end{align*}$$


para el caso de $\beta_1$, el intervalo de confianza está dado por

$$\begin{align*}\hat{\beta}_1 - t_{\frac{\alpha}{2}, n-2} \sqrt{\frac{\sigma^2_{e}}{S_{xx}}} < \beta_1 < \hat{\beta}_1 + t_{\frac{\alpha}{2}, n-2} \sqrt{\frac{\sigma^2_{e}}{S_{xx}}}\end{align*}$$


**Nota**

- Si el Intervalo de Confianza de $\beta_1$ no contiene el cero, se
  puede afirmar que la variable $Y$ está relacionada linealmente con
  la variable independiente $X$. En caso contrario, no existe relación
  lineal entre $X$ y $Y$, es decir, la variable $X$ no es adecuada
  para predecir el comportamiento de $Y$.
- En <tt>R</tt>, los intervalos de confianza para todos los coeficientes
  del modelo pueden obtenerse mediante la función <tt>confint(modelo,
  level = 0.95)</tt>.

## Análisis de Regresión Lineal Múltiple

### Prueba de hipótesis

Para el caso del modelo de regresión lineal múltiple estudiado en la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase18.html" target="\_blank">Clase
18</a>, se presentan a continuación las **pruebas de significancia
individual**, las cuales evalúan el aporte de cada una de las variables
explicativas por separado. Adicional a estas pruebas, existe la prueba
de significancia global de la regresión, la cual evalúa el aporte
conjunto de todas las variables explicativas del modelo mediante el
análisis de varianza, y la cual será estudiada en la siguiente clase.

#### Prueba de significancia individual

Recordando de la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase18.html" target="\_blank">Clase
18</a> que si
$\boldsymbol{\varepsilon} \sim N_n(\mathbf{0},\sigma^2\mathbf{I}_n)$,
entonces
$\hat{\boldsymbol{\beta}} \sim N_{k+1}(\boldsymbol{\beta}, \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1})$,
se tendrá que cada coeficiente estimado de forma individual se
distribuye

$$\begin{align*}\hat{\beta}_j \sim N\left(\beta_j, \sigma^2 C_{jj}\right) \quad \text{ para } j = 0,1,\ldots,k\end{align*}$$


donde $C_{jj}$ es el j-ésimo elemento de la diagonal de la matriz
$(\mathbf{X}^\top\mathbf{X})^{-1}$. Nuevamente, dado que la varianza
$\sigma^2$ es desconocida, se reemplaza por su estimador insesgado
$\hat{\sigma}^2_e = \frac{SCE}{n-k-1}$, y los estadísticos asociados
seguirán una distribución t-student, ahora con $n-k-1$ grados de
libertad.

Entonces, para realizar el contraste de hipótesis sobre el coeficiente
$\beta_j$ de la forma

$$\begin{align*}H_0&: \beta_j = \beta_{j0}\\  H_1&: \beta_j \neq \beta_{j0}\end{align*}$$


se tendrá que el estadístico de prueba será de la forma

$$\begin{align*}t_{\hat{\beta}_{j}}= \frac{\hat{\beta}_j - \beta_{j0}}{\sqrt{\hat{\sigma}^2_e C_{jj}}}\end{align*}$$


y para tomar la decisión si se rechaza o no la hipótesis se emplea la
región crítica la cual está dada por

$$\begin{align*}RC:\{t|t < -t_{\frac{\alpha}{2}, n-k-1} \quad ó \quad t > t_{\frac{\alpha}{2}, n-k-1}\}\end{align*}$$


en donde si $t_{\hat{\beta}_{j}} \in RC$, se rechaza $H_0$. Mientras
que el P-valor está dado por

$$\begin{align*}\text{P-valor}= 2\mathbb{P}(t_{n-k-1}\geq |t_{\hat{\beta}_j}|)\end{align*}$$


en donde si P-valor es menor al nivel de significancia $\alpha$,
entonces se rechaza $H_0$.

**Nota**

- Usualmente se quiere probar si $\beta_{j}=0$, es decir, la
  significancia individual del parámetro. Rechazar $H_0:\beta_{j}=0$
  permite afirmar que la variable $X_j$ aporta significativamente a la
  explicación de $Y$, **dado que las demás variables ya se encuentran
  incluidas en el modelo**.
- Lo anterior implica que la prueba de significancia individual es una
  **prueba de aporte marginal o parcial**, ya que evalúa la contribución
  de $X_j$ en presencia de las demás variables explicativas. Por
  tanto, si no se rechaza $H_0:\beta_{j}=0$, no significa
  necesariamente que $X_j$ no esté relacionada con $Y$, sino que
  dicha variable no aporta información adicional una vez las demás
  variables se encuentran en el modelo.
- Estas pruebas son las que reporta la función <tt>summary()</tt> de
  <tt>R</tt> en las columnas <tt>t value</tt> y <tt>Pr(&gt;|t|)</tt>
  para cada uno de los coeficientes del modelo ajustado mediante la
  función <tt>lm()</tt>.

### Intervalos de confianza

De forma análoga al caso de la regresión lineal simple, y empleando la
distribución t-student con $n-k-1$ grados de libertad, el intervalo de
confianza del $(1-\alpha)100\%$ para el coeficiente $\beta_j$ está
dado por

$$\begin{align*}\hat{\beta}_j - t_{\frac{\alpha}{2}, n-k-1} \sqrt{\hat{\sigma}^2_{e} C_{jj}} < \beta_j < \hat{\beta}_j + t_{\frac{\alpha}{2}, n-k-1} \sqrt{\hat{\sigma}^2_{e} C_{jj}} \quad \text{ para } j = 0,1,\ldots,k\end{align*}$$


donde $C_{jj}$ es el j-ésimo elemento de la diagonal de la matriz
$(\mathbf{X}^\top\mathbf{X})^{-1}$.

**Nota**

- Si el intervalo de confianza de $\beta_j$ no contiene el cero, se
  puede afirmar que la variable $X_j$ aporta significativamente a la
  explicación de $Y$, dado que las demás variables se encuentran en el
  modelo. En caso contrario, la variable $X_j$ no aporta información
  adicional en presencia de las demás variables explicativas.
- En <tt>R</tt>, los intervalos de confianza para todos los coeficientes
  del modelo pueden obtenerse mediante la función <tt>confint(modelo,
  level = 0.95)</tt>.

## Revisión de supuestos del modelo

Existe una serie de supuestos que deben ser corroborados para asegurar
que el modelo de regresión lineal esté correctamente desarrollado. Es de
anotar que estos supuestos aplican **tanto para el modelo de regresión
lineal simple como para el modelo de regresión lineal múltiple**, y su
verificación se realiza de la misma forma en ambos casos, ya que ésta se
efectúa sobre los residuales del modelo ajustado. Entre los supuestos a
verificar tenemos:

### Linealidad

Uno de los primeros supuestos que se debe probar es que haya una
relación lineal entre la variable dependiente y las independientes, y
para ello se debe examinar la relación entre los términos de error
(residuales) y los valores ajustados, en donde:

<ol>
<li>
Se verifica que la media de los residuales tenga media 0, y se
distribuya de forma aleatoria a lo largo de la línea horizontal.
</li>
<li>
No debe exhibirse en el diagrama de dispersión una tendencia clara o
forma sistemática.
</li>
<li>
La dispersión de los residuos debe ser aproximadamente constante a lo
largo de los valores ajustados.
</li>
</ol>

Para probar en <tt>R</tt> el supuesto de linealidad, es posible
calcularle la relación entre los residuales y los valores ajustados
mediante la función <tt>plot(modelo,1)</tt>.

Una forma alternativa sería generando el gráfico entre la variable
dependiente e independiente con la función <tt>plot(x,y)</tt> (útil
únicamente en el caso de la regresión lineal simple), o usando la prueba
RESET de Ramsey que permite validar si un modelo lineal tiene la forma
funcional correcta o si se han omitido términos no lineales o
interacciones entre las variables.

El juego de hipótesis de la prueba RESET de Ramsey está dada por


$$\begin{align*}&H_0: \text{El modelo lineal está bien especificado}\\  &H_1: \text{El modelo lineal está mal especificado}\end{align*}$$


Esta prueba puede realizarse en <tt>R</tt> mediante la función
<tt>resettest(modelo)</tt> de la librería <tt>lmtest</tt>.

### Normalidad

El segundo supuesto que se debe considerar es que los términos de error
(residuales) de la regresión se distribuyan normalmente, debido a que si
éstos se distribuyen normalmente, se tendrá que la variable respuesta
$Y$ también se distribuya normalmente, habilitando que las ecuaciones
del cálculo de los estimadores sean correctas.

Para probar la normalidad del los residuales es cuestión de usar alguna
de las pruebas de normalidad vistas en pruebas de bondad de ajuste,
tales como la Shapiro-Wilk, Anderson Darling, Cramer-Von Mises
(<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase16.html#prueba-de-bondad-de-ajuste" target="\_blank">Ver
Clase 16</a>), donde el juego de hipótesis a probar está dada por


$$\begin{align*}&H_0: \text{Los errores de estimación de la regresión se distribuyen normalmente}\\  &H_1: \text{Los errores de estimación de la regresión NO se distribuyen normalmente}\end{align*}$$


Una alternativa, es hacer una validación de forma gráfica mediante la
construcción de un QQ-Plot que puede generarse con la función
<tt>plot(modelo, 2)</tt>.

### Homocedasticidad

El tercer supuesto busca probar que la variabilidad de los residuales
estudentizados sea constante a lo largo de las observaciones, es decir,
que no vaya aumentando (disminuyendo) a medida que aumentan (disminuyen)
los valores ajustados.

Para probar este supuesto, es posible plantearse un gráfico de diagrama
de dispersión de los residuos estudentizados frente a los valores
ajustados usando la función <tt>plot(modelo, 3)</tt>.

Otra alternativa es mediante el uso de la prueba Breusch-Pagan, la cual
busca probar la hipótesis de que los términos de error son
homocedásticos, contra la alternativa, de que los términos de error son
heterocedásticos.

El juego de hipótesis de la prueba Breusch-Pagan está dada por


$$\begin{align*}&H_0: \text{La varianza de los errores es constante para todas las observaciones (Existe homocedasticidad)}\\  &H_1: \text{La varianza de los errores no es constante y depende de una o más variables independientes (Existe heterocedasticidad)}\end{align*}$$


Esta prueba puede realizarse en <tt>R</tt> con la función
<tt>bptest(modelo)</tt> de la librería <tt>lmtest</tt>.

### Independencia

El cuarto supuesto del modelo de regresión lineal lo que busca es
verificar si los residuales están incorrelacionados, y por tanto, se
tendrá que la covarianza de los términos de error será igual a $0$.

Para probar este supuesto, es posible plantear una gráfica entre los
residuos contra el orden de las observaciones, para verificar que si los
residuos están distribuidos de manera aleatoria sin mostrar ningún
patrón o tendencia sistemática a lo largo del orden de las
observaciones, lo cual indicaría que el supuesto de independencia se
cumple. Lo anterior puede realizarse en <tt>R</tt> mediante la función
<tt>plot(residuals(modelo), type = ‘o’)</tt>.

Alternativamente, se suele utilizar la prueba Durbin-Watson, la cual
verifica la hipótesis de que hay independencia para los términos de
error contra la alternativa de que hay dependencia.

El juego de hipótesis de la prueba Durbin-Watson está dada por


$$\begin{align*}&H_0: \text{Los errores de estimación de la regresión son independientes}\\  &H_1: \text{Los errores de estimación de la regresión NO son independientes}\end{align*}$$


Para realizar esta prueba en <tt>R</tt> se puede utilizar la prueba
Durbin-Watson con la función <tt>dwtest(modelo)</tt> de la librería
<tt>lmtest</tt>.

### Multicolinealidad

Finalmente, para el caso **exclusivo del modelo de regresión lineal
múltiple**, se debe verificar adicionalmente que no exista una relación
lineal fuerte entre las variables explicativas del modelo, fenómeno
conocido como **multicolinealidad**.

La presencia de multicolinealidad, aunque no afecta el insesgamiento de
los estimadores, infla las varianzas
$Var(\hat{\beta}_j)=\sigma^2 C_{jj}$ de los coeficientes estimados,
generando estimaciones inestables, intervalos de confianza muy amplios y
pruebas de significancia individual poco confiables.

Para detectar la multicolinealidad se emplea el **factor de inflación de
la varianza** (VIF por sus siglas en inglés), el cual se calcula para
cada variable explicativa como

$$\begin{align*}VIF_j = \frac{1}{1-R^2_j} \quad \text{ para } j = 1,2,\ldots,k\end{align*}$$


donde $R^2_j$ es el coeficiente de determinación obtenido al ajustar
una regresión de la variable $X_j$ en función de las demás variables
explicativas del modelo.

**Umbrales de Decisión**

- $VIF = 1$: Ausencia total de colinealidad. Las variables
  independientes no están correlacionadas en absoluto. Es el escenario
  ideal.
- $1 < VIF < 5$: Multicolinealidad baja/moderada. Es el rango normal y
  aceptable. No afecta la confiabilidad de los resultados de tu
  regresión.
- $VIF ≥ 5$: Multicolinealidad preocupante. Sugiere que los errores
  estándar están empezando a inflarse y los coeficientes se vuelven
  inestables.
- $VIF ≥ 10$: Multicolinealidad grave. Indica que la colinealidad está
  sesgando severamente el modelo, inflando los errores estándar y
  ocultando variables que podrían ser significativas.

Para calcular el VIF de cada una de las variables explicativas del
modelo en <tt>R</tt>, se emplea la función <tt>vif(modelo)</tt> de la
librería <tt>car</tt>.