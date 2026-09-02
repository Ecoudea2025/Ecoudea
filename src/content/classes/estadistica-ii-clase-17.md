---
title: "Clase 06"
course: "estadistica-ii"
order: 8
classType: "clase"
description: "Eficiencia - Estimador insesgado de varianza mínima - Error cuadrático medio"
math: true
bibliography: "../../referencias.bib"
---

## Eficiencia

### Estimador insesgado de varianza mínima (MVUE)

Si entre todos los estimadores insesgados de `$\theta$` podemos
encontrar uno cuya varianza sea más pequeña que los demás estimadores,
entonces, usando como criterio el sesgo y la eficiencia, se habrá
conseguido el estimador óptimo de `$\theta$`.

Diremos que `$\hat{\theta}$` es un estimador insesgado y de varianza
mínima si `$\mathbb{E}(\hat{\theta})=\theta$` y para cualquier otro
estimador `$\mathbb{E}(\hat{\Phi})=\theta$` se verifica que


$$\begin{align*}Var(\hat{\theta}) \leq Var(\hat{\Phi})\end{align*}$$


se dice entonces que `$\hat{\theta}$` es un MVUE de `$\theta$`.

#### Cota de Cramer-Rao

Si `$\hat{\theta}$` es un estimador insesgado del parámetro `$\theta$`,
se verifica en condiciones generales que


$$\begin{align*}Var(\hat{\theta}) \geq \frac{1}{I_n(\theta)}\end{align*}$$


donde `$I_n(\theta)$` se conoce como la matriz de información de Fisher
asociada a una muestra aleatoria de tamaño `$n$`, y está dada por


$$\begin{align*}I_n(\theta)&=n\mathbb{E}\left[\left(\frac{\partial Ln\left(f(x;\theta)\right)}{\partial \theta}\right)^2\right]\end{align*}$$


Una forma alternativa que brinda el mismo resultado y que en ocasiones
puede ser más sencilla de calcular `$I_n(\theta)$` es mediante

$$\begin{align*}I_n(\theta)&= -n\mathbb{E}\left[\frac{\partial^2 Ln\left(f(x;\theta)\right)}{\partial \theta^2}\right]\end{align*}$$


De lo anterior se tendrá que si `$\hat{\theta}$` es un estimador
insesgado de mínima varianza de `$\theta$`, entonces

$$\begin{align*}CCR(\hat{\theta}) = \frac{1}{I_n(\theta)}\end{align*}$$


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
Sea $X_1, X_2, \ldots, X_20$ una muestra aleatoria iid de una
distribución Poisson parámetro desconocido $\lambda$, pruebe que el
estimador $\tilde{\lambda} = \bar{X}$ es el MVUE del parámetro
$\lambda$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Con el estimador $\tilde{\lambda}$ es igual a $\bar{X}$ se tendrá
que la esperanza matemática del estimador $\tilde{\lambda}$ estará
dado por

$$\begin{align*}
\mathbb{E}(\bar{X}) = \mathbb{E}(\tilde{\lambda}) = \mu
\end{align*}$$

mientras que el valor de la varianza del estimador $\tilde{\lambda}$
estará dada por

$$\begin{align*}
Var(\bar{X}) = Var(\tilde{\lambda}) = \frac{\sigma^2}{20}
\end{align*}$$

En donde, como la muestra aleatoria proviene de una distribución Poisson
donde $\mathbb{E}(X_i) = \mu = \lambda$ y
$Var(X_i)= \sigma^2 = \lambda$, entonces se tendrá que

$$\begin{align*}
\mathbb{E}(\tilde{\lambda}) = \lambda \quad \quad Var(\tilde{\lambda}) = \frac{\lambda}{20}
\end{align*}$$

Verificado que el estimador $\tilde{\lambda}$ es un estimador
insesgado, se procede a comparar la varianza del estimador
$\tilde{\lambda}$ con la varianza del estimador MVUE para la
distribución Poisson, tal que el valor de la matriz de información de
Fisher $I_n(\theta)$ es igual a

$$\begin{align*}
  I_n(\lambda)&=n\mathbb{E}\left[\left(\frac{\partial Ln\left(f(x;\theta)\right)}{\partial \lambda}\right)^2\right] \\
             &=20 \mathbb{E}\left[\left(\frac{\partial Ln\left(\frac{e^{-\lambda}\lambda^x}{x!}\right)}{\partial \lambda}\right)^2\right] \\
             &=20 \mathbb{E}\left[\left(\frac{\partial \left(-\lambda  + xLn(\lambda) - x!\right)}{\partial \lambda}\right)^2\right] \\
             &=20 \mathbb{E}\left[\left(-1  + \frac{x}{\lambda}\right)^2\right] \\
             &=20 \mathbb{E}\left[1^2 - 2\frac{x}{\lambda} + \left(\frac{x}{\lambda}\right)^2\right] \\
             &=20 \left[\mathbb{E}(1) - 2\frac{\mathbb{E}(X)}{\lambda} + \frac{\mathbb{E}(X^2)}{\lambda^2}\right] \\
             &=20 \left[1 - 2\frac{\mathbb{E}(X)}{\lambda} + \frac{Var(X) + \mathbb{E}(X)^2}{\lambda^2}\right] \\
             &=20 \left[1 - 2\frac{\lambda}{\lambda} + \frac{\lambda + \lambda^2}{\lambda^2}\right] \\
             &=20 \left[1 - 2 + \frac{1}{\lambda} + 1\right] \\
             &= \frac{20}{\lambda}
\end{align*}$$

Entonces, al reemplazar la matriz de información de Fisher
$I_n(\lambda)$ en la fórmula de la Cota de Cramer Rao, se tendrá que
el estimador de mínima varianza será aquel que tenga una varianza igual
a

$$\begin{align*}
  CCR(\hat{\lambda}) &= \frac{1}{I_n(\lambda)} \\
                     &= \frac{1}{\frac{20}{\lambda}}\\
                     &= \frac{\lambda}{20}
\end{align*}$$

En donde se observa que la varianza del estimador $\tilde{\lambda}$
coincide con el estimador de la varianza mínima $\hat{\lambda}$

$$\begin{align*}
  CCR(\hat{\lambda}) &= Var(\tilde{\lambda}) = \frac{\lambda}{20}
\end{align*}$$

lo cual quiere decir que el estimador $\tilde{\lambda}$ es el MVUE del
parámetro desconocido $\lambda$.
</p>
</main>

### Error Cuadrático Medio (ECM)

Sea `$\hat{\theta}$` un estimador de un parámetro `$\theta$`, entonces
el ECM de `$\theta$` estará dado por


$$\begin{align*}ECM(\hat{\theta}) &= \mathbb{E}[(\hat{\theta} - \theta)^2]\\                     &= Var(\hat{\theta})  + \mathbb{B}(\hat{\theta})^2\end{align*}$$


en donde, además de tener en cuenta la variabilidad del estimador
(Precisión), tiene en cuenta el sesgo que éste posea (Exactitud), lo
cual permite al ECM ser una medida razonable de la calidad del estimador
puntual independientemente de que este sea o no insesgado.

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
desconocida $\mathbb{E}(X)=\mu$ y varianza $Var(X) =\sigma^2$,
entonces si se define el estimador $\bar{X}_1$ como

$$\begin{align*}
  \bar{X}_1=\frac{3X_1  + 2X_{n/2} + 3X_n}{6}
\end{align*}$$

Calcule el error cuadrático medio del estimador.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

En este caso estamos interesados en calcular el error cuadrático medio
para el estimador $\bar{X}_1$ y para ello debemos inicialmente
calcular si es o no insesgado, tal que

$$\begin{align*}
  \mathbb{E}(\bar{X}_1)&=\mathbb{E}\left(\frac{3X_1  + 2X_{n/2} + 3X_n}{6}\right) \\
                       &=\frac{1}{6}\mathbb{E}\left(3X_1  + 2X_{n/2} + 3X_n\right) \\
                       &=\frac{1}{6}\left[\mathbb{E}(3X_1)  + \mathbb{E}(2X_{n/2}) + \mathbb{E}(3X_n)\right] \\
                       &=\frac{1}{6}\left[3\mathbb{E}(X_1)  + 2\mathbb{E}(X_{n/2}) + 3\mathbb{E}(X_n)\right]
\end{align*}$$

En donde, como la distribución de probabilidad tiene media
$\mathbb{E}(X)=\mu$, entonces

$$\begin{align*}
  \mathbb{E}(\bar{X}_1)&=\frac{1}{6}\left[3\mathbb{E}(X_1)  + 2\mathbb{E}(X_{n/2}) + 3\mathbb{E}(X_n)\right]\\
                       &=\frac{1}{6}\left[3\mu  + 2\mu + 3\mu\right]\\
                       &=\frac{1}{6}\left[8\mu\right]\\
                       &=\frac{8}{6}\mu\\
                       &=\frac{4}{3}\mu
\end{align*}$$

Encontrando que el estimador planteado no es insesgado, lo cual quiere
decir que su sesgo está dado por $$\begin{align*}
  \mathbb{B}(\bar{X}_1)&=\mathbb{E}(\bar{X}_1) - \mu \\
                       &=\frac{4}{3}\mu - \mu\\
                       &=\frac{1}{3}\mu   
\end{align*}$$

Ahora, para realizar el cálculo del Error Cuadrático Medio, es necesario
calcular la varianza del estimador de interés, y por ello se procede a
su cálculo

$$\begin{align*}
  Var(\bar{X}_1)&=Var\left(\frac{3X_1  + 2X_{n/2} + 3X_n}{6}\right) \\
                       &=\frac{1}{6^2}Var\left(3X_1  + 2X_{n/2} + 3X_n\right) \\
                       &=\frac{1}{36}\left[Var(3X_1)  + \mathbb{E}(2X_{n/2}) + Var(3X_n)\right] \\
                       &=\frac{1}{36}\left[3^2Var(X_1)  + 2^2Var(X_{n/2}) + 3^2Var(X_n)\right]
\end{align*}$$

En donde, como la distribución de probabilidad tiene media
$Var(X)=\sigma^2$, entonces

$$\begin{align*}
  Var(\bar{X}_1)&=\frac{1}{36}\left[3^2Var(X_1)  + 2^2Var(X_{n/2}) + 3^2Var(X_n)\right]\\
                       &=\frac{1}{36}\left[9\sigma^2  + 4\sigma^2 + 9\sigma^2\right]\\
                       &=\frac{1}{36}\left[22\sigma^2\right]\\
                       &=\frac{22}{36}\sigma^2\\
                       &=\frac{11}{16}\sigma^2
\end{align*}$$

Y por tanto al reemplazar en la fórmula del Error Cuadrático Medio se
tendrá que $$\begin{align*}
  ECM(\bar{X}_1) &= Var(\bar{X}_1) + \mathbb{B}(\bar{X}_1)^2\\
                 &= \frac{11}{16}\sigma^2 + \left(\frac{1}{3}\mu\right)^2 \\
                 &= \frac{11}{16}\sigma^2 + \frac{1}{9}\mu^2
\end{align*}$$

Encontrando que el Error Cuadrático Medio para el estimador
$\bar{X}_1$, está dado por
$$ECM(\bar{X}_1) = \frac{11}{16}\sigma^2 + \frac{1}{9}\mu^2$$
</p>
</main>