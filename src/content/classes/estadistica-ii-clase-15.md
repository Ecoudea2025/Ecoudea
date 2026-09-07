---
title: "Clase 08"
course: "estadistica-ii"
order: 10
classType: "clase"
description: "Método de estimación puntual - Método de momentos - Método de máxima verosimilitud"
math: true
bibliography: "../../referencias.bib"
---

## Métodos de Estimación Puntual

### Método de momentos

Es un procedimiento que se usa para hallar un estimador para uno o más
parámetros poblacionales a partir de los momentos muestrales.

Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria de una distribución
`$X_i;\theta_1, \theta_2, \ldots \theta_k$`, y sea el `$k$`-ésimo
momento alrededor del origen dado por

$$\begin{align*}\mu_k' = \mathbb{E}(X^k)\end{align*}$$


y sea el `$k$`-ésimo momento muestral dado por

$$\begin{align*}m_k' = \frac{1}{n}\sum_{i=1}^{n} x_i^k\end{align*}$$


entonces, los estimadores
`$(\hat{\theta}_1, \hat{\theta}_2, \ldots \hat{\theta}_k)$` para
`$(\theta_1, \theta_2, \ldots \theta_k)$` se obtiene al igualas los
correspondientes momentos poblacionales y muestrales para despejar los
estimadores deseados.

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

Sea $X_1, X_2, \ldots, X_n$ una muestra aleatoria de una distribución
chi-cuadrado con parámetro desconocido $\nu$ y función de distribución
dada por $$\begin{align*}
  f(x) = \frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}} x^{\frac{\nu}{2} - 1} e^{-\frac{x}{2}} \quad \text{ para } \quad x > 0; \nu > 0
\end{align*}$$

Encuentre el estimador del parámetro $\nu$ por el método de momentos.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>

Para poder encontrar el estimador del parámetro $\nu$ por el método de
los momentos, es necesario en primer lugar calcular el primer momento
poblacional asociado a la distribución chi-cuadrado, tal que
$$\begin{align*}
  \mu_1' &= \mathbb{E}(X) \\
         &= \int_{0}^{\infty} x f(x) dx\\
         &= \int_{0}^{\infty} x \frac{1}{\Gamma\left(\frac{\nu}{2}\right)2^{\frac{\nu}{2}}} x^{\frac{\nu}{2} - 1} e^{-\frac{x}{2}} dx\\ 
         &=\frac{1}{\Gamma\left( \frac{\nu}{2} \right)2^{\frac{\nu}{2}}} \int_{0}^{\infty} x^{\frac{\nu}{2}} e^{-\frac{x}{2}} dx
\end{align*}$$
En donde, al realizar un cambio de variable para
facilitar la integral se tiene que $$\begin{align*}
  u=\frac{x}{2} &=>2u =x\\
  du= \frac{1}{2} dx&=> 2du = dx
\end{align*}$$

obteniendo entonces que $$\begin{align*}
  \mu_1' &=\frac{1}{\Gamma\left( \frac{\nu}{2} \right)2^{\frac{\nu}{2}}} \int_{0}^{\infty} x^{\frac{\nu}{2}} e^{-\frac{x}{2}} dx\\
         &=\frac{1}{\Gamma\left( \frac{\nu}{2} \right)2^{\frac{\nu}{2}}} \int_{0}^{\infty} (2u)^{\frac{\nu}{2}} e^{-u} 2du\\
         &=\frac{2^{\frac{\nu}{2}+1}}{ \Gamma\left( \frac{\nu}{2} \right)2^{\frac{\nu}{2}}} \int_{0}^{\infty} u^{\frac{\nu}{2}} e^{-u} du\\
         &=\frac{2}{\Gamma\left( \frac{\nu}{2} \right)} \int_{0}^{\infty} u^{\frac{\nu}{2}} e^{-u} du\\
         &=\frac{2}{\Gamma\left( \frac{\nu}{2} \right)} \int_{0}^{\infty} u^{(\frac{\nu}{2} + 1)-1} e^{-u} du
\end{align*}$$

En donde se observa que la integral tiene la forma de una función gamma
y por tanto se tendrá que $$\begin{align*}
  \mu_1' &= \frac{2}{\Gamma\left( \frac{\nu}{2} \right)} \int_{0}^{\infty} u^{(\frac{\nu}{2} + 1)-1} e^{-u} du\\
         &= \frac{2}{\Gamma\left( \frac{\nu}{2} \right)} \Gamma\left(\frac{\nu}{2} + 1\right)\\
         &=\frac{2}{\Gamma\left( \frac{\nu}{2} \right)} \left(\frac{\nu}{2}\right)\Gamma\left(\frac{\nu}{2}\right)\\
         &=\nu
\end{align*}$$

En segundo lugar, será necesario definir el primer momento muestral, el
cual está dado por $$\begin{align*}
  m_1 &= \frac{1}{n} \sum_{i=1}^{n} x_i\\
      &= \bar{X}
\end{align*}$$

Finalmente, será cuestión de igualar el primer momento muestral al
primer momento poblacional, tal que $$\begin{align*}
  \mu_1' &= m_1 \\
  \nu    &= \bar{X}
\end{align*}$$

Encontrando que el estimador por el método de momentos para el parámetro
desconocido $\nu$ es igual a $$\begin{align*}
  \hat{\nu} &= \bar{X}
\end{align*}$$
</p>
</main>

### Método de máxima verosimilitud

Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria iid de una
distribución `$f(x; \theta_1, \theta_2, \ldots, \theta_k)$`, con función
de verosimilitud dada por


$$\begin{align*}L(\theta|x_i) &= L(\theta_1, \theta_2, \ldots, \theta_k| X_1, X_2, \ldots, X_k)\\                 &= \prod_{i=1}^{n} f(x_i, \theta_1, \theta_2, \ldots, \theta_k)\end{align*}$$


Entonces el estimador de máxima verosimilitud de `$\hat{\theta}_{MV}$`
para el parámetro `$\theta$`, es el valor que maximiza
`$L(\theta| x_i)$`, es decir,


$$\begin{align*}L(\hat{\theta}_{MV}| X_1, X_2, \ldots, X_k) = \max_{\theta} L(\theta_1, \theta_2, \ldots, \theta_k| X_1, X_2, \ldots, X_k)\end{align*}$$


#### Observación

Cómo `$L(\theta| X)$` es el producto de `$n$` funciones, es recomendable
usar la función monótona creciente `$Ln(\cdot)$` antes de maximizar
`$L(\theta|X)$`, debido a que es más sencillo hallar la derivada de
`$\ell(\theta|X)=Ln(L(\theta|X))$` que hallar la derivada de la
multiplicación de `$n$` funciones.

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

Sea $X_1, X_2, \ldots, X_n$ una muestra aleatoria de una distribución
Uniforme en el intervalo ($a$, $10$) con parámetro desconocido $a$
y función de distribución dada por $$\begin{align*}
  f(x) = \frac{1}{10-a} \quad \text{ para } \quad a < x < 10
\end{align*}$$

Encuentre el estimador del parámetro $a$ por el método de mínimos
cuadrados.
</p>
<h3 data-toc-skip>
Solución
</h3>
<p>
Para encontrar el estimador del parámetro $a$ de mínimos cuadrados
debemos seguir una serie de pasos los cuales se presentan a continuación
<ol>
<li>
Calcular la función de verosimilitud. <br> Para ello debemos calcular el
productorio de la función de probabilidad para $i=1, 2, \ldots, n$,
tal que $$\begin{align*}
  L(x_i|a) &= \prod_{i=1}^{n} f(x_i) \\
           &= \prod_{i=1}^{n} \frac{1}{10-a} \\
           &= \left[\frac{1}{10-a}\right]^n \\
           &= \frac{1}{\left[10-a\right]^n}
\end{align*}$$
</li>
<li>
Calcular la función de log-verosimilitud. <br> Para ello debemos
calcular el logaritmo natural de la función de verosimilitud que
calculamos en el punto anterior, tal que $$\begin{align*}
  \ln[L(x_i|a)] &= \ln\left( \frac{1}{\left[10-a\right]^n}\right)\\
  \ell(x_i|a)   &= \ln\left(\left[10-a\right]^{-n}\right)\\
                &= -n\ln\left(10-a\right)
\end{align*}$$
</li>
<li>
Calcular la primera derivada de cada uno de los parámetros de interés.
<br> Para ello será cuestión de calcular la primera derivada de la
función de log-verosimilitud respecto a cada uno de los parámetro de
interés, en donde en este caso será cuestión solamente de derivar
respecto al parámetro $a$, tal que $$\begin{align*}
  \frac{\partial\ell(x_i|a)}{\partial a} &= \frac{\partial -n\ln(10-a)}{\partial a} \\                
  &= -n\frac{\partial \ln(10-a)}{\partial a}\\
  &= -n \left(\frac{1}{10-a} (-1)\right) \\
  &= \frac{n}{10-a}
\end{align*}$$
</li>
<li>
Igualar la primera derivada a cero y despejar el parámetro de interés
$$\begin{align*}
  \frac{\partial\ell(x_i|a)}{\partial a} &= 0 \\     \frac{n}{10-a} &= 0 \\
  n &= 0 (10 - a)\\
  n &= 0
\end{align*}$$
Encontrando que no hay forma de despejar en este caso el
parámetro $a$ de la derivada de la función de log-verosimilitud, y por
tanto no es posible encontrar un estimador por el método de máxima
verosimilitud para el parámetro $a$.
</li>
<li>
En caso de que hubiera un estimador en el paso anterior, se debería
calcular la segunda derivada de la función de log-verosimilitud y probar
si el estimador encontrado era un máximo, tratando de probar si la
segunda derivada era menor a $0$, pero dado que no existe un estimador
para el parámetro, no se realiza este paso en el caso de esta
distribución.
</li>
</ol>
</p>
</main>