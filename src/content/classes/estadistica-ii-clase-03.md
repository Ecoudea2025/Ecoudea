---
title: "Clase 18"
course: "estadistica-ii"
order: 22
classType: "clase"
description: "Análisis de Regresión - Regresión lineal múltiple - Notación matricial - Estimación de parámetros"
math: true
bibliography: "../../referencias.bib"
---

## Introducción

En la
<a href="https://jiperezga.github.io/EstadisticaII/EstIIClase17.html" target="\_blank">Clase
17</a> se estudió el modelo de regresión lineal simple, en el cual la
variable respuesta $Y$ se explica en función de **una única** variable
explicativa $X$. Sin embargo, en la mayoría de los problemas
prácticos, la variable de interés no depende de una sola variable, sino
que **es explicada de forma simultánea por dos o más variables
independientes**.

Por ejemplo, retomando el Caso 2 de la clase anterior, es razonable
pensar que las donaciones recibidas para la construcción de parques y
bibliotecas no dependen únicamente del gasto en publicidad, sino también
de otras variables como el número de eventos de recaudación realizados
durante el mes, el número de voluntarios, la época del año, entre otras.

Cuando la relación entre la variable respuesta y las $k$ variables
explicativas se supone lineal, el modelo que permite estudiar dicha
relación se conoce como **modelo de regresión lineal múltiple**.

### Regresión Lineal Múltiple

Suponga que se tiene una variable respuesta $Y$ y un conjunto de $k$
variables explicativas $X_1, X_2, \ldots, X_k$. El modelo de regresión
lineal múltiple está dado por

$$\begin{align*}Y=\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \varepsilon \quad \quad (I)\end{align*}$$


donde

- $\beta_0, \beta_1, \ldots, \beta_k$: son $k+1$ constantes
  desconocidas denominadas parámetros del modelo o coeficientes de
  regresión, estimados a partir de los datos.
- $\beta_0$ representa el intercepto, es decir, el valor medio de
  $Y$ cuando todas las variables explicativas toman el valor de cero.
- $\beta_j$ para $j=1,2,\ldots,k$, representa el cambio esperado en
  la variable respuesta $Y$ por cada unidad de cambio en $X_j$,
  **cuando las demás variables explicativas permanecen constantes**,
  razón por la cual los $\beta_j$ se conocen como coeficientes de
  regresión parciales.
- $\varepsilon$ representa al componente de error aleatorio, el cual
  recoge los efectos de todas las variables no consideradas en el
  modelo, errores de medición u otras consideraciones no tenidas en
  cuenta por el investigador.

**Nota:** El término “lineal” hace referencia a que el modelo es lineal
**en los parámetros** $\beta_0, \beta_1, \ldots, \beta_k$, y no
necesariamente en las variables explicativas. Por ejemplo, el modelo
polinomial

$$\begin{align*}Y=\beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon\end{align*}$$

es un modelo de regresión lineal múltiple, ya que puede reescribirse
tomando $X_1 = X$ y $X_2=X^2$.

#### Supuestos del modelo de regresión lineal múltiple

1.  Se tiene una muestra aleatoria de $n$ observaciones
    $(y_i, x_{i1}, x_{i2}, \ldots, x_{ik})$ para $i=1,2,\ldots,n$,
    con $n > k+1$, las cuales se supone que satisfacen el modelo
    $(I)$, tal que
    
$$\begin{align*}y_i=\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_k x_{ik} + \varepsilon_i \quad \text{ para } i =1,2, \ldots, n \quad \quad (II)\end{align*}$$

    donde $y_i$ es la i-ésima observación de la variable $Y$, y
    $x_{ij}$ es la i-ésima observación de la j-ésima variable
    explicativa.

2.  Del modelo $(II)$ suponga que los $\varepsilon_i$ son variables
    aleatorias independientes con media $\mathbb{E}(\varepsilon_i)=0$
    y varianza $Var(\varepsilon_i)=\sigma^2$, de tal forma que
    
$$\begin{align*}\mathbb{E}(y_i)=\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_k x_{ik}\end{align*}$$

    y
    
$$\begin{align*}Var(y_i)=Var(\varepsilon_i) = \sigma^2\end{align*}$$

    en donde, si además se cumple que
    $\varepsilon_i\sim N(0,\sigma^2)$, entonces se tendrá que
    
$$\begin{align*}y_i\sim N(\beta_0 + \beta_1 x_{i1} + \cdots + \beta_k x_{ik}, \; \sigma^2)\end{align*}$$

3.  Las variables explicativas $X_1, X_2, \ldots, X_k$ no presentan
    una relación lineal exacta entre ellas (ausencia de
    multicolinealidad perfecta).

### Notación matricial

Dado que el modelo de regresión lineal múltiple involucra $n$
ecuaciones (una por cada observación), resulta mucho más conveniente
expresar el modelo empleando notación matricial. Así, el conjunto de
ecuaciones dado en $(II)$ puede reescribirse como

$$\begin{align*}\mathbf{Y}=\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}\end{align*}$$


donde


$$\begin{align*}\mathbf{Y}=\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}, \qquad \mathbf{X}=\begin{bmatrix}  1 & x_{11} & x_{12} & \cdots & x_{1k}\\  1 & x_{21} & x_{22} & \cdots & x_{2k}\\  \vdots & \vdots & \vdots & \ddots & \vdots\\  1 & x_{n1} & x_{n2} & \cdots & x_{nk} \end{bmatrix}, \qquad \boldsymbol{\beta}=\begin{bmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_k \end{bmatrix}, \qquad \boldsymbol{\varepsilon}=\begin{bmatrix} \varepsilon_1 \\ \varepsilon_2 \\ \vdots \\ \varepsilon_n \end{bmatrix}\end{align*}$$


- $\mathbf{Y}$ es el vector de observaciones de dimensión
  $n\times 1$.
- $\mathbf{X}$ es la matriz de diseño de dimensión $n\times (k+1)$,
  cuya primera columna es un vector de unos asociado al intercepto.
- $\boldsymbol{\beta}$ es el vector de parámetros de dimensión
  $(k+1)\times 1$.
- $\boldsymbol{\varepsilon}$ es el vector de errores aleatorios de
  dimensión $n\times 1$, con
  $\mathbb{E}(\boldsymbol{\varepsilon})=\mathbf{0}$ y
  $Var(\boldsymbol{\varepsilon})=\sigma^2\mathbf{I}_n$, siendo
  $\mathbf{I}_n$ la matriz identidad de dimensión $n \times n$.

De esta forma, los supuestos del modelo pueden resumirse como

$$\begin{align*}\mathbb{E}(\mathbf{Y})=\mathbf{X}\boldsymbol{\beta} \qquad \text{y} \qquad Var(\mathbf{Y})=\sigma^2\mathbf{I}_n\end{align*}$$


### Estimación de parámetros

Al igual que en el caso de la regresión lineal simple, el objetivo será
estimar el vector de parámetros $\boldsymbol{\beta}$ y la varianza
$\sigma^2$, para lo cual puede emplearse el método de mínimos
cuadrados o el método de máxima verosimilitud.

#### Método de Máxima Verosimilitud

Bajo el supuesto de que
$\boldsymbol{\varepsilon} \sim N_n(\mathbf{0},\sigma^2\mathbf{I}_n)$,
entonces
$\mathbf{Y} \sim N_n(\mathbf{X}\boldsymbol{\beta}, \sigma^2\mathbf{I}_n)$,
luego la función de verosimilitud está dada por

$$\begin{align*}L(\boldsymbol{\beta}, \sigma^2; \mathbf{Y}) = \frac{1}{(2\pi\sigma^2)^{n/2}}e^{-\frac{1}{2\sigma^2}(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})}\end{align*}$$


Al maximizar la función de verosimilitud respecto a
$\boldsymbol{\beta}$ y $\sigma^2$, se encuentra que los estimadores
de máxima verosimilitud están dados por

$$\begin{align*}\hat{\boldsymbol{\beta}} &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}\\ \hat{\sigma}^2 &= \frac{(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})}{n}\end{align*}$$


observando nuevamente que el EMV para $\boldsymbol{\beta}$ coincide
con el estimador de mínimos cuadrados.

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
  \ell(\boldsymbol{\beta}, \sigma^2) &= \ln L(\boldsymbol{\beta}, \sigma^2; \mathbf{Y})\\
  &= -\frac{n}{2}\ln(2\pi) - \frac{n}{2}\ln(\sigma^2) - \frac{1}{2\sigma^2}(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})
\end{align*}$$

Ahora, para derivar respecto al vector $\boldsymbol{\beta}$, se
expande inicialmente la forma cuadrática

$$\begin{align*}
  (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) &= \mathbf{Y}^\top\mathbf{Y} - \mathbf{Y}^\top\mathbf{X}\boldsymbol{\beta} - \boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{Y} + \boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}\\
  &= \mathbf{Y}^\top\mathbf{Y} - 2\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{Y} + \boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}
\end{align*}$$

en donde el segundo y tercer término se agrupan ya que
$\mathbf{Y}^\top\mathbf{X}\boldsymbol{\beta}$ es un escalar, y por
tanto es igual a su transpuesta
$\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{Y}$. Luego, empleando
las reglas de derivación matricial
$\frac{\partial (\mathbf{a}^\top\mathbf{b})}{\partial \mathbf{b}} = \mathbf{a}$
y
$\frac{\partial (\mathbf{b}^\top\mathbf{A}\mathbf{b})}{\partial \mathbf{b}} = 2\mathbf{A}\mathbf{b}$
para $\mathbf{A}$ simétrica, se tiene

$$\begin{align*}
  \frac{\partial \ell}{\partial \boldsymbol{\beta}} = -\frac{1}{2\sigma^2}\left(- 2\mathbf{X}^\top\mathbf{Y} + 2\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}\right) = \frac{1}{\sigma^2}\left(\mathbf{X}^\top\mathbf{Y} - \mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}\right)
\end{align*}$$

e igualando a cero se obtiene

$$\begin{align*}
  \mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{Y}
\end{align*}$$

y dado que la matriz $\mathbf{X}^\top\mathbf{X}$ es invertible por el
supuesto de ausencia de multicolinealidad perfecta, se concluye que

$$\begin{align*}
  \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}
\end{align*}$$

Derivando ahora la función de log-verosimilitud respecto a $\sigma^2$
se tiene

$$\begin{align*}
  \frac{\partial \ell}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4}(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) = 0
\end{align*}$$

y al multiplicar ambos lados de la igualdad por $2\hat{\sigma}^4$ y
evaluar en $\hat{\boldsymbol{\beta}}$ se obtiene

$$\begin{align*}
  -n\hat{\sigma}^2 + (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) = 0
\end{align*}$$

concluyendo entonces que

$$\begin{align*}
  \hat{\sigma}^2 = \frac{(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})}{n} 
\end{align*}$$
</p>
</main>

#### Método de Mínimos Cuadrados

Si denotamos por
$\hat{\boldsymbol{\beta}}=(\hat{\beta}_0, \hat{\beta}_1, \ldots, \hat{\beta}_k)^\top$
al estimador del vector de parámetros $\boldsymbol{\beta}$, entonces
el vector de valores ajustados estará dado por

$$\begin{align*}\hat{\mathbf{Y}}=\mathbf{X}\hat{\boldsymbol{\beta}}\end{align*}$$


y el vector de errores de estimación del ajuste será

$$\begin{align*}\mathbf{e} = \mathbf{Y} - \hat{\mathbf{Y}} = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}\end{align*}$$


El método de mínimos cuadrados consiste en encontrar el vector
$\hat{\boldsymbol{\beta}}$ que minimiza la suma de los cuadrados de
los errores, la cual en notación matricial está dada por

$$\begin{align*}SCE=\sum_{i=1}^n e_i^2 = \mathbf{e}^\top\mathbf{e} &= (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})\\ &= \mathbf{Y}^\top\mathbf{Y} - 2\hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y} + \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}}\end{align*}$$


Derivando la expresión anterior respecto a $\hat{\boldsymbol{\beta}}$
e igualando a cero

$$\begin{align*}\frac{\partial SCE}{\partial \hat{\boldsymbol{\beta}}} = -2\mathbf{X}^\top\mathbf{Y} + 2\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{0}\end{align*}$$


se obtiene el sistema de **ecuaciones normales**

$$\begin{align*}\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{Y}\end{align*}$$


y dado que por el supuesto de ausencia de multicolinealidad perfecta la
matriz $\mathbf{X}^\top\mathbf{X}$ es invertible, el estimador de
mínimos cuadrados de $\boldsymbol{\beta}$ estará dado por

$$\begin{align*}\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}\end{align*}$$


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

Se presenta con mayor detalle el desarrollo de la minimización de la
suma de los cuadrados de los errores. Partiendo de la forma cuadrática,
se tiene

$$\begin{align*}
  SCE &= (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})\\
  &= \mathbf{Y}^\top\mathbf{Y} - \mathbf{Y}^\top\mathbf{X}\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y} + \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}}\\
  &= \mathbf{Y}^\top\mathbf{Y} - 2\hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y} + \hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}}
\end{align*}$$

en donde el segundo y tercer término se agrupan ya que
$\mathbf{Y}^\top\mathbf{X}\hat{\boldsymbol{\beta}}$ es un escalar de
dimensión $1\times 1$, y por tanto es igual a su transpuesta
$\hat{\boldsymbol{\beta}}^\top\mathbf{X}^\top\mathbf{Y}$.<br> <br>
Ahora, empleando las reglas de derivación matricial

$$\begin{align*}
  \frac{\partial (\mathbf{a}^\top\mathbf{b})}{\partial \mathbf{b}} = \mathbf{a} \qquad \text{y} \qquad \frac{\partial (\mathbf{b}^\top\mathbf{A}\mathbf{b})}{\partial \mathbf{b}} = 2\mathbf{A}\mathbf{b} \quad \text{ para } \mathbf{A} \text{ simétrica}
\end{align*}$$

y notando que la matriz $\mathbf{X}^\top\mathbf{X}$ es simétrica, ya
que $(\mathbf{X}^\top\mathbf{X})^\top = \mathbf{X}^\top\mathbf{X}$, se
deriva la $SCE$ respecto al vector $\hat{\boldsymbol{\beta}}$, tal
que

$$\begin{align*}
  \frac{\partial SCE}{\partial \hat{\boldsymbol{\beta}}} = -2\mathbf{X}^\top\mathbf{Y} + 2\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}}
\end{align*}$$

e igualando a cero se obtiene el sistema de ecuaciones normales

$$\begin{align*}
  \mathbf{X}^\top\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{Y}
\end{align*}$$

Dado que por el supuesto de ausencia de multicolinealidad perfecta la
matriz $\mathbf{X}$ tiene rango columna completo, la matriz
$\mathbf{X}^\top\mathbf{X}$ es invertible, y al premultiplicar ambos
lados del sistema por $(\mathbf{X}^\top\mathbf{X})^{-1}$ se concluye
que

$$\begin{align*}
  \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}
\end{align*}$$

Finalmente, note que la solución encontrada corresponde en efecto a un
mínimo de la función $SCE$, ya que la matriz de segundas derivadas
(matriz Hessiana) está dada por

$$\begin{align*}
  \frac{\partial^2 SCE}{\partial \hat{\boldsymbol{\beta}} \, \partial \hat{\boldsymbol{\beta}}^\top} = 2\mathbf{X}^\top\mathbf{X}
\end{align*}$$

la cual es definida positiva, dado que para cualquier vector
$\mathbf{v}\neq\mathbf{0}$ de dimensión $(k+1)\times 1$ se cumple
que

$$\begin{align*}
  \mathbf{v}^\top(2\mathbf{X}^\top\mathbf{X})\mathbf{v} = 2(\mathbf{X}\mathbf{v})^\top(\mathbf{X}\mathbf{v}) = 2\|\mathbf{X}\mathbf{v}\|^2 > 0
\end{align*}$$

en donde la desigualdad es estricta ya que, al tener $\mathbf{X}$
rango columna completo, $\mathbf{X}\mathbf{v}=\mathbf{0}$ si y solo si
$\mathbf{v}=\mathbf{0}$.
</p>
</main>

**Nota sobre estimador** $\sigma^2$

Dado que el estimador de máxima verosimilitud de la varianza
$\sigma^2$ es sesgado, se emplea entonces un estimador insesgado el
cual estará dado por

$$\begin{align*}\hat{\sigma}^2_e &=\frac{SCE}{n-(k+1)} = \frac{\sum_{i=1}^n e^2_i}{n-k-1} \\             &= \frac{(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}})}{n-k-1}\end{align*}$$


conocido como el **cuadrado medio del error** ($CME$), en donde
$n-k-1$ son los grados de libertad asociados al error, ya que se
estiman $k+1$ parámetros a partir de las $n$ observaciones.

### Propiedades de $\hat{\boldsymbol{\beta}}$

A continuación se presentan algunas propiedades que cumple el estimador
$\hat{\boldsymbol{\beta}}$.

- $\mathbb{E}(\hat{\boldsymbol{\beta}}) = \boldsymbol{\beta}$, es
  decir, $\hat{\boldsymbol{\beta}}$ es un estimador insesgado de
  $\boldsymbol{\beta}$.
- $Var(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}$,
  en donde la varianza del estimador $\hat{\beta}_j$ corresponde al
  j-ésimo elemento de la diagonal de dicha matriz, tal que
  $Var(\hat{\beta}_j)=\sigma^2 C_{jj}$, siendo $C_{jj}$ el j-ésimo
  elemento de la diagonal de $(\mathbf{X}^\top\mathbf{X})^{-1}$.
- Si
  $\boldsymbol{\varepsilon} \sim N_n(\mathbf{0},\sigma^2\mathbf{I}_n)$,
  entonces
  $\hat{\boldsymbol{\beta}} \sim N_{k+1}(\boldsymbol{\beta}, \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1})$.

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

Para la demostración de las propiedades resulta conveniente reescribir
el estimador $\hat{\boldsymbol{\beta}}$ en función del vector de
errores $\boldsymbol{\varepsilon}$, tal que al reemplazar el modelo
$\mathbf{Y}=\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$
en el estimador se tiene

$$\begin{align*}
  \hat{\boldsymbol{\beta}} &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}\\
  &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top(\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon})\\
  &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta} + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\varepsilon}\\
  &= \boldsymbol{\beta} + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\varepsilon} \quad \quad (III)
\end{align*}$$
</p>
<h4 data-toc-skip>
Demostración Esperanza de $\hat{\boldsymbol{\beta}}$
</h4>
<p>

Dado que la matriz $\mathbf{X}$ es fija (no aleatoria), al aplicar el
operador esperanza sobre la expresión $(III)$ y emplear el supuesto
$\mathbb{E}(\boldsymbol{\varepsilon})=\mathbf{0}$, se tiene

$$\begin{align*}
  \mathbb{E}(\hat{\boldsymbol{\beta}}) &= \mathbb{E}\left[\boldsymbol{\beta} + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\varepsilon}\right]\\
  &= \boldsymbol{\beta} + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbb{E}(\boldsymbol{\varepsilon})\\
  &= \boldsymbol{\beta} + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{0}\\
  &= \boldsymbol{\beta} 
\end{align*}$$
</p>
<h4 data-toc-skip>
Demostración Varianza de $\hat{\boldsymbol{\beta}}$
</h4>
<p>

Empleando la propiedad de la matriz de varianzas y covarianzas de una
transformación lineal,
$Var(\mathbf{A}\mathbf{Z}) = \mathbf{A}Var(\mathbf{Z})\mathbf{A}^\top$
para $\mathbf{A}$ una matriz de constantes, y tomando
$\mathbf{A} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, se
tiene

$$\begin{align*}
  Var(\hat{\boldsymbol{\beta}}) &= Var\left[(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}\right]\\
  &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top \, Var(\mathbf{Y}) \, \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\\
  &= (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top \, \sigma^2\mathbf{I}_n \, \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\\
  &= \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\\
  &= \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1} 
\end{align*}$$

en donde se emplea el hecho de que la matriz
$(\mathbf{X}^\top\mathbf{X})^{-1}$ es simétrica, por ser la inversa de
una matriz simétrica.
</p>
</main>