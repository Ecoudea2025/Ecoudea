---
title: "Clase 07"
course: "estadistica-ii"
order: 9
classType: "clase"
description: "Consistencia Suficiencia"
math: true
bibliography: "../../referencias.bib"
---

## Consistencia

### Estimador Consistente

Es razonable pensar que **un buen estimador es aquel que mejore** en su
estimación a medida que va **aumentando el tamaño de la muestra**. Esto
es lo que se conoce como consistencia de un estimador.

Si `$\hat{\theta}$` es un estimador del parámetro `$\theta$`, tal que

1.  `$\hat{\theta}$` es un estimador insesgado o asintóticamente
    insesgado tal que
    
$$\begin{align*}\lim_{n\to \infty}\mathbb{E}(\hat{\theta}) = \theta \quad \text{ ó }\quad \lim_{n\to \infty}\mathbb{B}(\hat{\theta}) = 0\end{align*}$$

2.  A medida que aumenta el tamaño de muestra, las estimaciones de
    `$\hat{\theta}$` se aproximan cada vez más al parámetro `$\theta$`,
    tal que
    
$$\begin{align*}\lim_{n\to \infty}Var(\hat{\theta}) = 0\end{align*}$$


entonces de cumplirse estas dos condiciones se dice que el estimador
`$\hat{\theta}$` del parámetro `$\theta$` es un estimador consistente.

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
desconocida $\mathbb{E}(X)=\mu$ y varianza $Var(X) =\sigma^2$,
entonces si se define el estimador $\bar{X}_1$ como

$$\begin{align*}
  \bar{X}_{2}=\frac{1}{n}\sum_{i=1}^{n-5}X_i
\end{align*}$$

Muestre si este estimador es consistente para el parámetro $\mu$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para probar si el estimador propuesto es consistente, debemos calcular
inicialmente si el estimador es insesgado o asintóticamente insesgado, y
para ello debemos calcular inicialmente el valor esperado del estimador,
tal que

$$\begin{align*}
  \mathbb{E}(\bar{X}_{2}) &= \mathbb{E}\left(\frac{1}{n}\sum_{i=1}^{n-5}X_i\right)\\
                 &= \frac{1}{n}\mathbb{E}\left(\sum_{i=1}^{n-5}X_i\right)\\
                 &= \frac{1}{n}\sum_{i=1}^{n-5}\mathbb{E}\left(X_i\right)\\
                 &= \frac{1}{n}\sum_{i=1}^{n-5}\mu\\
                 &= \frac{1}{n}\left(\underbrace{\mu + \mu + \mu + \ldots + \mu}_{n-5 \; veces} \right)\\
                 &= \frac{1}{n}\left(n-5\right)\mu\\
                 &= \left(1 - \frac{5}{n}\right)\mu
\end{align*}$$

Y por tanto como el valor esperado del estimador no es igual a $\mu$,
entonces se tendrá que el estimador es sesgado con un sesgo igual a
$$\begin{align*}
  \mathbb{B}(\bar{X}_{2}) &= \mathbb{E}(\bar{X}_{2}) - \mu\\
                          &= \left(1 - \frac{5}{n}\right)\mu - \mu\\
                          &= \mu - \frac{5\mu}{n} - \mu\\
                          &= -\frac{5\mu}{n}
\end{align*}$$

Entonces, al emplear el sesgo del estimador, se procede a probar si el
estimador es asintóticamente insesgado, tal que $$\begin{align*}
  \lim_{n\to\infty}\mathbb{B}(\bar{X}_{2}) &= \lim_{n\to\infty} -\frac{5\mu}{n}\\
                          &= -\frac{5\mu}{\infty}\\
                          &= 0
\end{align*}$$

Encontrando con ésto, que el estimador $\bar{X}_2$ es un estimador
asintóticamente insesgado, probando con ello la primera parte que se
requiere para que un estimador sea consistente. <br> <br> Ahora bien,
para probar la segunda parte que se requiere para que un estimador sea
consistente, es necesario inicialmente calcular la varianza del
estimador, la cual es igual a

$$\begin{align*}
  Var(\bar{X}_{2}) &= Var\left(\frac{1}{n}\sum_{i=1}^{n-5}X_i\right)\\
                 &= \left(\frac{1}{n}\right)^2Var\left(\sum_{i=1}^{n-5}X_i\right)\\
                 &= \frac{1}{n^2}\sum_{i=1}^{n-5}Var\left(X_i\right)\\
                 &= \frac{1}{n^2}\sum_{i=1}^{n-5}\sigma^2\\
                 &= \frac{1}{n^2}\left(\underbrace{\sigma^2 + \sigma^2 + \sigma^2 + \ldots + \sigma^2}_{n-5 \; veces} \right)\\
                 &= \frac{1}{n^2}\left(n-5\right)\sigma^2\\
                 &= \frac{n-5}{n^2}\sigma^2
\end{align*}$$

Y ahora, al aplicarle límite cuando $n\to\infty$ a la varianza del
estimador, se tiene que

$$\begin{align*}
  \lim_{n\to\infty}Var(\bar{X}_{2}) &= \lim_{n\to\infty} \frac{n-5}{n^2}\sigma^2\\
                 &=\lim_{n\to\infty} \left(\frac{n}{n^2}- \frac{5}{n^2}\right)\sigma^2\\
                 &=\lim_{n\to\infty} \left(\frac{1}{n}- \frac{5}{n^2}\right)\sigma^2\\
                 &=\left(\frac{1}{\infty}- \frac{5}{\infty^2}\right)\sigma^2\\
                 &= \left(0-0\right)\sigma^2\\
                 &=0
\end{align*}$$
Encontrando que al cumplir también la segunda condición
que se requiere para que el estimador sea consistente, se concluirá que
el estimador $\bar{X}_{2}$ es un estimador consistente para el
parámetro $\mu$.
</p>
</main>

## Suficiencia

### Estimador Suficiente

Se dice que un estimador `$\hat{\theta}$` es suficiente para el
parámetro `$\theta$`, cuando éste tiene tanta información sobre el
parámetro como al propia muestra, es decir, cuando es capaz de recoger o
resumir toda la información de la muestra aleatoria sin depender del
parámetro que está intentando estimar.

#### Teorema de Factorización Neyman

Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria de tamaño `$n$` de
una distribución `$f(X;\theta)$`, entonces un estadístico
`$\hat{\theta}$` basado en una muestra aleatoria es suficiente para la
estimación de `$\theta$` si y solo si se puede factorizar en dos
funciones no negativas.

$$\begin{align*}L(X_1, X_2, \ldots, X_n|\theta) = g(\hat{\theta}, \theta)h(X_1, X_2,\ldots, X_n)\end{align*}$$


donde `$L(X_1, X_2, \ldots, X_n|\theta)=\prod_{i=1}^{n}f(x_i;\theta)$`
es la función de verosimilitud de la muestra aleatoria,
`$g(\hat{\theta}, \theta)$` es una función solo de `$\hat{\theta}$` y
`$\theta$`, y `$h(X_1, X_2,\ldots, X_n)$` es una función que depende
solo de la muestra y no depende del parámetro `$\theta$`.

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
Sea $X_1, X_2, ,X_n$ una muestra aleatoria $iid$ de una distribución
Chi-Cuadrado con parámetros desconocido $\nu$. Muestre que
$\sum_{i=1}^{n} x_i$ es un estimador suficiente para el parámetro
$\nu$.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para probar si $\sum_{i=1}^{n} x_i$ es un estimador suficiente para el
parámetro $\nu$, debemos primer establecer la función de probabilidad
de una distribución Chi-Cuadrado, la cual es de la forma
$$\begin{align*}
  f(x)=\frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}}x^{\frac{\nu}{2}} e^{-\frac{x}{2}} \quad \text{ para } x>0; \nu >0
\end{align*}$$

Entonces, para poder probar si es un estimador suficiente, es necesario
calcular la función de verosimilitud de la distribución de probabilidad,
tal que $$\begin{align*}
  L(x,\nu)&=\prod_{i=1}^{n} f(x_i)\\
          &=\prod_{i=1}^{n}\left[\frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}}x_i^{\frac{\nu}{2}} e^{-\frac{x_i}{2}} \right]\\
          &= \left[\prod_{i=1}^{n}\frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}}\right]\left[\prod_{i=1}^{n}x_i^{\frac{\nu}{2}}\right] \left[\prod_{i=1}^{n}e^{-\frac{x_i}{2}} \right]\\
          &= \left[\prod_{i=1}^{n}\frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}}\right]\left[\prod_{i=1}^{n}x_i^{\frac{\nu}{2}}\right] \left[\prod_{i=1}^{n}e^{-\frac{x_i}{2}} \right]\\
          &= \frac{1}{\left[\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}\right]^n}\left[\prod_{i=1}^{n}x_i^{\frac{\nu}{2}}\right] e^{-\frac{\sum_{i=1}^{n}x_i}{2}}
\end{align*}$$

Una vez calculada la función de verosimilitud, es necesario dividir la
función de probabilidad en dos términos, uno que dependa del parámetro
$\nu$ y de $\sum_{i=1}^{n}x_i$ y otro que dependa solo de la muestra
$X_1, X_2, \ldots, X_n$, tal que

$$\begin{align*}
  g\left(\nu,\sum_{i=1}^{n}x_i\right)&= \frac{1}{\left[\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}\right]^n}\left[\prod_{i=1}^{n}x_i^{\frac{\nu}{2}}\right] e^{-\frac{\sum_{i=1}^{n}x_i}{2}}\\
  h(x_1,x_2,\ldots, x_n)&=1
\end{align*}$$

Y por tanto se tendrá que el $\sum_{i=1}^{n}x_i$ es un estimador
suficiente para el parámetro $\nu$.
</p>
</main>