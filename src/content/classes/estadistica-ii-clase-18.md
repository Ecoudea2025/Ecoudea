---
title: "Clase 05"
course: "estadistica-ii"
order: 7
classType: "clase"
description: "Estimación puntual Insesgadez - Estimador insesgado - Estimador asintóticamente insesgado Eficiencia - Eficiencia relativa"
math: true
bibliography: "../../referencias.bib"
---

## Estimación puntual

Cómo su nombre lo indica, es un único valor que se calcula a partir de
una muestra, con el fin de realizar una aproximación al verdadero valor
desconocido del parámetro de interés.

Es de anotar, que en muchas situaciones prácticas es posible encontrar
varias estimaciones puntuales del mismo parámetro y por ello deben
tenerse en cuenta una serie de criterios para seleccionar el parámetro
más adecuado.

## Insesgadez

### Estimador insesgado

Un estimador `$\hat{\theta}$` es un estimador insesgado del parámetro
`$\theta$` si y solo si se cumple que


$$\begin{align*}\mathbb{E}(\hat{\theta})=\theta\end{align*}$$


En otro caso se dice que el estimador `$\hat{\theta}$` es sesgado y su
sesgo está dado por


$$\begin{align*}\mathbb{B}(\hat{\theta})=\mathbb{E}(\hat{\theta}) - \theta\end{align*}$$


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

Sea una muestra aleatoria $X_1, X_2, \ldots, X_n$ con media
$\mathbb{E}(X)=\mu$ y varianza desconocida $Var(X) =\sigma^2$,
entonces si se define el estimador $\tilde{S}^2$ tal que

$$\begin{align*}
  \tilde{S}^2=\frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2
\end{align*}$$

Muestre si el estimador $\tilde{S}^2$ es un estimador insesgado del
parámetro $\sigma^2$. De no serlo, calcule el valor del sesgo.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Con el fin de probar si el estimador de interés es insesgado o no, se
aplica el concepto de valor esperado al estadístico de interés, tal que
$$\begin{align*}
\mathbb{E}(\tilde{S}^2)=\mathbb{E}\left(\frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2\right)   
\end{align*}$$

Entonces, al desarrollar la esperanza matemática, a través de sus
propiedades, se tendrá que

$$\begin{align*}
\mathbb{E}(\tilde{S}^2)&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n (X_i - 
\bar{X})^2\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n (X_i^2 - 2X_i\bar{X} + \bar{X}^2)\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n X_i^2 - \sum_{i=1}^n2X_i\bar{X} + \sum_{i=1}^n\bar{X}^2\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n X_i^2 - 2\bar{X}\sum_{i=1}^nX_i + \sum_{i=1}^n\bar{X}^2\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n X_i^2 - 2\bar{X}n\bar{X} + n\bar{X}^2\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n X_i^2 - 2n\bar{X}^2 + n\bar{X}^2\right]  \\
&=\frac{1}{n}\mathbb{E}\left[ \sum_{i=1}^n X_i^2 - n\bar{X}^2 \right]  \\
&=\frac{1}{n}\left[\sum_{i=1}^n \mathbb{E}\left(X_i^2\right) - n\mathbb{E}\left(\bar{X}^2 \right)\right] \\
&=\frac{1}{n}\left[\sum_{i=1}^n (\sigma^2 + \mu^2) - n\left(\frac{\sigma^2}{n} + \mu  \right)\right] \\
&=\frac{1}{n}\left[n\sigma^2 + n\mu^2 - \sigma^2 - n\mu^2\right] \\
&=\frac{1}{n}\left[n\sigma^2 - \sigma^2 \right] \\
&=\frac{(n-1)\sigma^2}{n}
\end{align*}$$

y como $\frac{(n-1)\sigma^2}{n} \neq \sigma^2$ se concluye que el
estimador $\tilde{S}^2$ no es un estimador insesgado de $\sigma^2$ y
su sesgo es igual a

$$\begin{align*}
 \mathbb{B}(\tilde{S}^2)&=\mathbb{E}(\tilde{S}^2) - \sigma^2\\
&= \frac{(n-1)\sigma^2}{n} - \sigma^2\\
&= \frac{(n-1)\sigma^2- n\sigma^2}{n} \\
&= \frac{n\sigma^2-\sigma^2- n\sigma^2}{n} \\
&= -\frac{\sigma^2}{n} \\
\end{align*}$$
</p>
</main>

### Estimador asintóticamente insesgado

Si `$\hat{\theta}$` es un estimador sesgado
`$\mathbb{E}(\hat{\theta})\neq \theta$`, entonces se dice que el
estimador `$\hat{\theta}$` es asintóticamente insesgado si y solo si


$$\begin{align*}\lim_{n\to \infty}\mathbb{B}(\hat{\theta})=0\end{align*}$$


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

Sea una muestra aleatoria $X_1, X_2, \ldots, X_n$ con media
$\mathbb{E}(X)=\mu$ y varianza desconocida $Var(X) =\sigma^2$,
entonces si se define el estimador $\tilde{S}^2$ tal que

$$\begin{align*}
  \tilde{S}^2=\frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2
\end{align*}$$

Muestre si el estimador sesgado $\tilde{S}^2$ es un estimador
asintóticamente insesgado del parámetro $\sigma^2$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Con el fin de probar si el estimador sesgado $\tilde{S}^2$ es un
estimador asintóticamente insesgado, se debe aplicar el límite cuando
$n\to infty$ del sesgo del estimado $\mathbb{B}(\tilde{S}^2)$, para
observar si este tiende o no $0$, tal que $$\begin{align*}
\lim_{n\to \infty}\mathbb{B}(\tilde{S}^2) &= \lim_{n\to \infty} -\frac{\sigma^2}{n} \\
\end{align*}$$

En donde se observa que al estar el sesgo dividido por $n$ se tiene
que

$$\begin{align*}
\lim_{n\to \infty}\mathbb{B}(\tilde{S}^2) &= \lim_{n\to \infty} -\frac{\sigma^2}{n} \\
&= 0
\end{align*}$$

concluyendo que el estimador $\mathbb{B}(\tilde{S}^2)$ es un estimador
asintóticamente insesgado.
</p>
</main>

## Eficiencia

### Eficiencia Relativa

Sea `$\hat{\theta}_1$` y `$\hat{\theta}_2$` dos estimadores insesgados
de unparámetro `$\theta$`, obtenidos de una muestra aleatoria del mismo
tamaño, entonces

-   Se dice que `$\hat{\theta}_1$` es más eficiente que
    `$\hat{\theta}_2$` si `$Var(\hat{\theta}_1)$` &lt;
    `$Var(\hat{\theta}_2)$`
-   La eficiencia relativa (EFR) de un estimador respecto a otro puede
    calcularse mediante la ecuación


$$\begin{align*}EFR = \frac{Var(\hat{\theta_1})}{Var(\hat{\theta_2})}\end{align*}$$


y se interpretará de la siguiente manera

-   `$EFR < 1$`, entonces el estimador `$\hat{\theta}_1$` será más
    eficiente que el estimador `$\hat{\theta}_2$`.
-   `$EFR = 1$`, entonces `$\hat{\theta}_1$` y `$\hat{\theta}_2$` son
    estimadores igualmente eficientes.
-   `$EFR > 1$`, entonces el estimador `$\hat{\theta}_1$` será menos
    eficiente que el estimador `$\hat{\theta}_2$`.

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

Sea una muestra aleatoria $X_1, X_2, \ldots, X_50$ con media
desconocida $\mathbb{E}(X)=\mu$ y varianza $Var(X) =\sigma^2$,
entonces si se define el estimador $\bar{X}_1$ como

$$\begin{align*}
  \bar{X}_1=\frac{1}{50} \sum_{i=1}^{50} X_i
\end{align*}$$

y el estimador $\bar{X}_2$ como

$$\begin{align*}
  \bar{X}_2=\frac{1}{4} (X_1 + X_7 + X_{10} + X_{50})
\end{align*}$$ estimadores para la media desconocida $\mu$, calcule la
eficiencia relativa y concluya cuál de los dos estimadores es más
eficiente.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Con el fin de probar cuál de los dos estimadores para la media $\mu$,
se decide calcular el coeficiente de eficiencia relativa, basados en la
varianza de los dos estimadores, en donde la varianza del estimador
$\bar{X}_1$ es igual a $$\begin{align*}
Var(\bar{X}_1)=\frac{\sigma^2}{50}
\end{align*}$$

mientras que, el estimador $\bar{X}_2$ es igual a $$\begin{align*}
Var(\bar{X}_2)=\frac{\sigma^2}{4}
\end{align*}$$

Entonces al calcular la eficiencia relativa de los dos estimadores,
tendremos que

$$\begin{align*}
  EFR &= \frac{Var(\bar{X}_1)}{Var(\bar{X}_2)} \\
      &= \frac{\frac{\sigma^2}{50}}{\frac{\sigma^2}{4}} \\
      &= \frac{4\sigma^2}{50\sigma^2} \\
      &= \frac{4}{50} \\
      &= 0.08
\end{align*}$$

En donde se observa al ser $0.08 \lt  1$ se tendrá que $EFR \lt  1$ y por
tanto se concluirá que el estimador $\bar{X}_1$ será más eficiente que
el estimador $\bar{X}_2$.
</p>
</main>