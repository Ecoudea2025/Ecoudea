---
title: "Práctica 02"
course: "estadistica-ii"
order: 11
classType: "practica"
description: "Ejercicio sobre: - Estimadores puntuales. - Métodos de estimación puntual."
math: true
bibliography: "../../referencias.bib"
---

## Lista de ejercicios

1.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de un
    proceso Bernoulli con parámetro desconocido `$p$` y función de
    distribución dada por
    
$$\begin{align*}f(x) = p^x(1-p)^{1-x} \text{ para } x=0,1; \quad 0\leq p \leq 1\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(p\) por el método de los
    momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro \(p\)
    y pruebe si el estimador encontrado efectivamente maximiza la
    función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores insesgado del parámetro \(p\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(p\) y pruebe si los
    estimadores encontrado en \(a)\) y \(b)\) alcanzan dicha cota (son
    un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrados en \(a)\) y \(b)\) son
    estimadores consistentes para el parámetro \(p\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(p\).
    </li>
    </ol>
2.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Binomial con parámetros desconocido `$p$` y parámetro
    `$k$` conocido o desconocido, con función de distribución dada por
    
$$\begin{align*}f(x) = \left(\begin{array}{c}k\\ x\end{array}\right)p^x(1-p)^{k-x} \text{ para } x=0,1,\ldots, k; \quad 0\leq p \leq 1\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(p\) por el método de los
    momentos, si se supone que \(k\) es conocida.
    </li>
    <li>
    Calcule el estimador para los parámetros \(k\) y \(p\) por el método
    de los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(p\), si se supone \(k\) conocida y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(c)\) son
    estimadores insesgado del parámetro \(p\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(p\) y pruebe si los
    estimadores encontrado en \(a)\) y \(c)\) alcanzan dicha cota (son
    un MVUE).
    </li>
    <li>
    Pruebe cuál de los estimadores encontrados en \(a)\) y \(c)\) es más
    eficiente para el parámetro \(p\).
    </li>
    <li>
    Pruebe si los estimadores encontrados en \(a)\) y \(c)\) son
    estimadores consistentes para el parámetro \(p\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(p\).
    </li>
    </ol>
3.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Geométrica con parámetro desconocido `$p$` y función de
    distribución dada por
    
$$\begin{align*}f(x) = p(1-p)^{x-1} \text{ para } x=1,2,3,\ldots; \quad 0\leq p \leq 1\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(p\) por el método de los
    momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro \(p\)
    y pruebe si el estimador encontrado efectivamente maximiza la
    función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) mediante la
    transformación \(\frac{1}{\hat{p}}\) son estimadores insesgados para
    la media de la distribución.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) mediante la
    transformación \(\frac{1}{\hat{p}}\) son estimadores consistentes
    para la media de la distribución.
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(p\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(p\).
    </li>
    </ol>
4.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Poisson con parámetro desconocido `$\lambda$` y función
    de distribución dada por
    
$$\begin{align*}f(x) = \frac{e^{-\lambda}\lambda^x}{x!} \text{ para } x=0,1,2,\ldots; \quad \lambda > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\lambda\) por el método de
    los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\lambda\) y pruebe si el estimador encontrado efectivamente
    maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores insesgados del parámetro \(\lambda\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\lambda\) y pruebe si
    los estimadores encontrado en \(a)\) y \(b)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores consistentes para el parámetro \(\lambda\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(\lambda\).
    </li>
    </ol>
5.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Exponencial con parámetro desconocido `$\beta$` y
    función de distribución dada por
    
$$\begin{align*}f(x) = \frac{1}{\beta}e^{-\frac{x}{\beta}} \text{ para } x>0; \quad \beta > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\beta\) por el método de
    los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\beta\) y pruebe si el estimador encontrado efectivamente maximiza
    la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores insesgados del parámetro \(\beta\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\beta\) y pruebe si
    los estimadores encontrado en \(a)\) y \(b)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores consistentes para el parámetro \(\beta\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(\beta\).
    </li>
    </ol>
6.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Normal con parámetros conocidos o desconocidos `$\mu$`
    y `$\sigma^2$`, con función de distribución dada por
    
$$\begin{align*}f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x - \mu)^2}{2\sigma^2}} \text{ para } -\infty<\mu<\infty; \quad -\infty<x<\infty; \quad \sigma^2 > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\mu\) por el método de los
    momentos, si se supone \(\sigma^2\) conocida.
    </li>
    <li>
    Calcule el estimador para los parámetros \(\mu\) y \(\sigma\) por el
    método de los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\mu\), si se supone \(\sigma^2\) conocido y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\sigma^2\), si se supone \(\mu\) conocido y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\mu\) y \(\sigma^2\), y pruebe si el estimador encontrado
    efectivamente maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(c)\) son
    estimadores insesgados para el parámetro \(\mu\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\mu\) y pruebe si los
    estimadores encontrado en \(a)\) y \(c)\) alcanzan dicha cota (son
    un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores consistentes para el parámetro \(\mu\).
    </li>
    </ol>
7.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Lognormal con parámetros conocidos o desconocidos
    `$\mu$` y `$\sigma^2$`, con función de distribución dada por
    
$$\begin{align*}f(x) = \frac{1}{\sqrt{2\pi\sigma^2} x}e^{-\frac{(\ln(x) - \mu)^2}{2\sigma^2}} \text{ para } x>0; \quad -\infty<\mu<\infty; \quad \sigma^2 > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\mu\) por el método de los
    momentos, si se supone \(\sigma^2\) conocida.
    </li>
    <li>
    Calcule el estimador para el parámetro \(\sigma\) por el método de
    los momentos, si se supone \(\mu\) conocida.
    </li>
    <li>
    Calcule el estimador para los parámetros \(\mu\) y \(\sigma\) por el
    método de los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\mu\), si se supone \(\sigma^2\) conocido y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\sigma^2\), si se supone \(\mu\) conocido y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\mu\) y \(\sigma^2\), y pruebe si el estimador encontrado
    efectivamente maximiza la función.
    </li>
    </ol>
8.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Gamma con parámetros conocidos o desconocidos
    `$\alpha$` y `$\beta$`, con función de distribución dada por
    
$$\begin{align*}f(x) = \frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-\frac{x}{\beta}} \text{ para } x>0; \quad \alpha > 0; \quad \beta > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\alpha\) por el método de
    los momentos, si se supone \(\beta\) conocida.
    </li>
    <li>
    Calcule el estimador para el parámetro \(\beta\) por el método de
    los momentos, si se supone \(\alpha\) conocida.
    </li>
    <li>
    Calcule el estimador para los parámetros \(\alpha\) y \(\beta\) por
    el método de los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\beta\), si se supone \(\alpha\) conocido y pruebe si el estimador
    encontrado efectivamente maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrados de \(\beta\) en \(b)\) y
    \(d)\) son estimadores insesgados del parámetro \(\beta\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\beta\) y pruebe si
    los estimadores encontrado en \(b)\) y \(d)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(b)\) y \(d)\) son
    estimadores consistentes para el parámetro \(\beta\).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i\) es un estimador suficiente para el
    parámetro \(\beta\), si se asume \(\alpha\) conocida.
    </li>
    </ol>
9.  Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Rayleigh con parámetro desconocido `$\theta$` y función
    de distribución dada por
    
$$\begin{align*}f(x) = \frac{x}{\theta^2}e^{-\frac{x^2}{2\theta^2}} \text{ para } x>0; \quad \theta > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\theta\) por el método de
    los momentos.
    </li>
    <li>
    Calcule el estimador para el parámetro \(\theta^2\) por el método de
    los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\theta\) y pruebe si el estimador encontrado efectivamente
    maximiza la función.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\theta^2\) y pruebe si el estimador encontrado efectivamente
    maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(d)\) son
    estimadores insesgados para el parámetro \(\theta\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\theta\) y pruebe si
    los estimadores encontrado en \(a)\) y \(c)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\theta^2\) y pruebe si
    los estimadores encontrado en \(b)\) y \(d)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Muestre que \(\sum_{i=1}^n x_i^2\) es un estimador suficiente para
    el parámetro \(\theta^2\).
    </li>
    </ol>
10. Sea `$X_1, X_2, \ldots, X_n$` una muestra aleatoria `$iid$` de una
    distribución de probabilidad continua con parámetros conocido
    `$\alpha$`, parámetro desconocido `$\theta$` y función de
    distribución dada por
    
$$\begin{align*}f(x) = \frac{1}{\theta}\alpha x^{\alpha-1}e^{-\frac{x^\alpha}{\theta}} \text{ para } x>0; \quad \theta > 0\end{align*}$$

    <ol type="a">
    <li>
    Calcule el estimador para el parámetro \(\theta\) por el método de
    los momentos.
    </li>
    <li>
    Calcule el estimador de máxima verosimilitud para el parámetro
    \(\theta\) y pruebe si el estimador encontrado efectivamente
    maximiza la función.
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores insesgados para el parámetro \(\theta\).
    </li>
    <li>
    Calcule la Cota de Cramér-Rao del parámetro \(\theta\) y pruebe si
    los estimadores encontrado en \(a)\) y \(b)\) alcanzan dicha cota
    (son un MVUE).
    </li>
    <li>
    Pruebe si los estimadores encontrado en \(a)\) y \(b)\) son
    estimadores consistentes para el parámetro \(\theta\).
    </li>
    <li>
    Encuentre el estadístico suficiente para \(\theta\).
    </li>
    </ol>
11. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de una
    variable aleatoria continua Exponencial tal que `$X\sim Exp(\beta)$`
    y suponga los siguientes estimadores.
    
$$\begin{align*}\hat{\beta}_1&=X_1 \\     \hat{\beta}_2&=\frac{X_1+X_2+X_5}{3} \\     \hat{\beta}_3&=\frac{X_1+2X_2-3X_4+4X_7}{4} \\      \hat{\beta}_4&=\bar{X}\end{align*}$$

    <ol type="a">
    <li>
    Demuestre si los estimadores propuestos son insesgados, de no serlo,
    calcule su sesgo y pruebe si son asintóticamente insesgados.
    </li>
    <li>
    Encuentre la eficiencia relativa de los estimadores
    \(\hat{\beta}_1\), \(\hat{\beta}_2\) y \(\hat{\beta}_3\) respecto
    \(\hat{\beta}_4\). Qué se puede concluir?
    </li>
    </ol>
12. Suponga `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de
    una variable aleatoria continua Uniforme tal que
    `$X\sim Unif(\theta, \theta + 1)$` y suponga los siguientes
    estimadores
    
$$\begin{align*}\hat{\theta}_1&=\bar{X}-\frac{1}{2} \\     \hat{\theta}_2&=X_{(n)}-\frac{n}{n+1}\end{align*}$$
  
    <ol type="a">
    <li>
    Demuestre si los estimadores propuestos son insesgados, de no serlo,
    calcule su sesgo y pruebe si son asintóticamente insesgados.
    </li>
    <li>
    Encuentre la eficiencia relativa de \(\hat{\theta}_1\) respecto
    \(\hat{\theta}_2\). Qué se puede concluir?
    </li>
    </ol>
13. Suponga `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de
    una variable aleatoria discreta Poisson tal que
    `$X\sim Pois(\lambda)$` y suponga los siguientes estimadores
    
$$\begin{align*}\hat{\lambda}_1&=\bar{X} \\     \hat{\lambda}_2&=\frac{X_1+X_5+2X_7+X_9}{3} \\     \hat{\lambda}_3&=\frac{1}{n} \sum_{i=1}^{n-3}X_i\\     \hat{\lambda}_4&= 2X_{21} - X_{13}\end{align*}$$

    <ol type="a">
    <li>
    Demuestre si los estimadores son insesgados, de no serlo, calcule su
    sesgo y pruebe si son asintóticamente insesgados.
    </li>
    <li>
    Ordene los estimadores del más eficiente al ménos eficiente si
    consideramos que \(n=30\).
    </li>
    </ol>
14. Suponga `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de
    una variable aleatoria continua Normal tal que
    `$X\sim N(\mu, \sigma^2)$`, muestre si  
    
$$\begin{align*}S^2_n=\frac{1}{n}\sum_{i=1}^{n}(X_i-\mu)^2\end{align*}$$

    <ol type="a">
    <li>
    Muestre si dicho estimador es un estimador insesgado de
    \(\sigma^2\), de no serlo, calcule su sesgo y pruebe si es un
    estimador asintóticamente insesgado.
    </li>
    <li>
    Muestre si dicho estimador es un estimador consistente de
    \(\sigma^2\).
    </li>
    </ol>
15. Suponga `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de
    una variable aleatoria continua Normal tal que
    `$X\sim N(0, \sigma^2)$`, muestre si
    
$$\begin{align*}\hat{\sigma}^2 = \sum_{i=1}^{n}\frac{X^2_i}{n}\end{align*}$$

    <ol type="a">
    <li>
    Muestre si dicho estimador es un estimador insesgado de
    \(\sigma^2\), de no serlo, calcule su sesgo y pruebe si es un
    estimador asintóticamente insesgado.
    </li>
    <li>
    Muestre si dicho estimador es un estimador consistente de
    \(\sigma^2\).
    </li>
    </ol>
16. Suponga `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de
    una variable aleatoria continua Normal tal que
    `$X\sim N(\mu, \sigma^2)$`, muestre si  
    
$$\begin{align*}S^2_{n-2}=\frac{1}{n-2}\sum_{i=1}^{n}(X_i-\bar{X})^2\end{align*}$$

    <ol type="a">
    <li>
    Muestre si dicho estimador es un estimador insesgado de
    \(\sigma^2\), de no serlo, calcule su sesgo y pruebe si es un
    estimador asintóticamente insesgado.
    </li>
    <li>
    Muestre si dicho estimador es un estimador consistente de
    \(\sigma^2\).
    </li>
    </ol>
17. Si se consideran los estimadores `$S^2_{n}$`, `$S^2_{n-1}$`, y
    `$S^2_{n-2}$` del parámetro `$\sigma^2$` de una distribución
    `$N(\mu,\sigma^2)$`.
    <ol type="a">
    <li>
    Determine cuál de estos estimadores es más eficaz, si se considera
    sólo la varianza de los estimadores.
    </li>
    <li>
    Determine cuál de estos estimadores es más eficaz si se tiene en
    cuenta si es o no insesgado.
    </li>
    </ol>
18. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de una
    variable aleatoria discreta Binomial tal que `$X\sim Bin(n,p)$` y
    suponga los estimadores
    
$$\begin{align*}\hat{p}_1&=\frac{X}{n}; \\       \hat{p}_2&=\frac{X+\sqrt{n/2}}{n+\sqrt{n}}; \\   \hat{p}_3&=\frac{X+1}{n+2}\end{align*}$$

    <ol type="a">
    <li>
    Demuestre si los estimadores planteados son insesgados, de no serlo,
    calcule su sesgo y pruebe si son asintóticamente insesgados.
    </li>
    <li>
    Muestre si los estimadores planteados son estimadores consistentes.
    </li>
    <li>
    Ordene los estimadores del más eficiente al menos eficiente si
    consideramos que \(n = 50\).
    </li>
    </ol>
19. Sea `$X_1$` y `$X_2$` una muestra aleatoria de dos observaciones de
    una población Normal con media `$\mu$` y varianza `$\sigma^2$`.
    Considere los siguientes tres estimadores puntuales de `$\mu$`:
    
$$\begin{align*}\bar{X}^{(1)}&=\frac{1}{3}X_1+\frac{1}{3}X_2 \\     \bar{X}^{(2)}&=\frac{1}{4}X_1+\frac{1}{4}X_2 \\     \bar{X}^{(3)}&=\frac{1}{2}X_1+\frac{1}{2}X_2\end{align*}$$

    <ol type="a">
    <li>
    Demuestre si los estimadores planteados son insesgados, de no serlo,
    calcule su sesgo y pruebe si son asintóticamente insesgados.
    </li>
    <li>
    Muestre cuál de los tres estimadores es más eficiente.
    </li>
    </ol>
20. Sea `$X_1$`, `$X_2$` y `$X_3$` una muestra aleatoria de tres
    observaciones de una población Normal con media `$\mu$` y varianza
    `$\sigma^2$`. Considere los siguientes dos estimadores puntuales de
    `$\mu$`:
    
$$\begin{align*}\vec{X}^{(1)}&=\frac{X_1+2X_2+3X_3}{6}\\     \vec{X}^{(2)}&=\frac{X_1+4X_2+X_3}{6}\end{align*}$$

    <ol type="a">
    <li>
    Probar que los dos estimadores son insesgados.
    </li>
    <li>
    Cuál de los dos estimadores es más eficiente.
    </li>
    <li>
    Proponga un estimador insesgado para la media poblacional que sea
    más eficiente que los dos estimadores propuestos y que sea diferente
    a \(\bar{X}\).
    </li>
    </ol>
21. Sea `$X_1, X_2, X_3$` y `$X_4$` una muestra aleatoria de cuatro
    observaciones de una población Binomial con parámetro `$p$`
    desconocido. Demuestre si los siguientes estimadores son o no
    consistentes para la proporción poblacional `$p$`
    
$$\begin{align*}\breve{p}_{1}&=\frac{2X_1-X_2}{n+2}\\     \breve{p}_{2}&=\frac{4X_1-3X_2+2X_3}{n}\\     \breve{p}_{3}&=\frac{X_1-2X_2+5X_3}{n^2+5}\\     \breve{p}_{4}&=\frac{X_1-2X_2+5X_3+3X_4}{n^3-2n^2+5} \\\end{align*}$$

22. Sea `$X_1, X_2, X_3$` y `$X_4$` una muestra aleatoria de cuatro
    observaciones de una población `$N(\mu, \sigma^2)$`. Demuestre si
    los siguientes estimadores son o no consistentes para el parámetro
    `$\mu$`.
    
$$\begin{align*}\breve{\mu}_{1}&=2x_1+3x_2-6x_3 \\     \breve{\mu}_{2}&=\frac{4x_1-3x_2+2x_3}{n} \\     \breve{\mu}_{3}&=\frac{x_1-2x_2+5x_3}{n+5}\end{align*}$$

23. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria de un
    distribución con función de densidad de probabilidad dada por
    
$$\begin{align*}f(x,\theta)=\frac{3\theta^3}{x^4} \quad para \quad \theta<x<\infty; \quad \theta>0\end{align*}$$

    <ol type="a">
    <li>
    Determine el estimador de \(\theta\) por el método de momentos.
    </li>
    <li>
    Determine el estimador de máxima verosimilitud de \(\theta\).
    </li>
    <li>
    Determine si los estimadores a. y b. son insesgados para el
    parámetro \(\theta\).
    </li>
    <li>
    Pruebe si los estimadores encontrados en a. y b. son estimadores
    consistentes para el parámetro \(\theta\).
    </li>
    </ol>
24. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria de un
    distribución con función de distribución acumulada dada por
    
$$\begin{align*}F(x,\theta)=-e^{-\frac{x}{4\theta}} \quad para \quad x>0\end{align*}$$

    <ol type="a">
    <li>
    Determine el estimador de \(\theta\) por el método de momentos.
    </li>
    <li>
    Determine el estimador de máxima verosimilitud de \(\theta\).
    </li>
    <li>
    Determine si los estimadores a. y b. son insesgados para el
    parámetro \(\theta\).
    </li>
    <li>
    Pruebe si los estimadores encontrados en a. y b. son estimadores
    consistentes para el parámetro \(\theta\).
    </li>
    </ol>
25. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria de un
    distribución Uniforme con función de distribución acumulada dada por
    
$$\begin{align*}F(x,\theta)=\frac{x}{\theta} \quad para \quad 0<x<\theta; \quad \theta>0\end{align*}$$

    <ol type="a">
    <li>
    Determine el estimador de \(\theta\) por el método de momentos.
    </li>
    <li>
    Determine el estimador de máxima verosimilitud de \(\theta\).
    </li>
    <li>
    Determine si los estimadores a. y b. son insesgados para el
    parámetro \(\theta\).
    </li>
    <li>
    Pruebe si los estimadores encontrados en a. y b. son estimadores
    consistentes para el parámetro \(\theta\).
    </li>
    </ol>
26. Sean `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de una
    distribución Pareto tal que `$X \sim Pareto(\alpha, \beta)$`, con
    función de densidad de probabilidad dada por
    
$$\begin{align*}f(x)=\alpha\beta^{\alpha}x^{-(\alpha+1)} \quad para \quad x>\beta; \quad \alpha>0; \quad \beta>0\end{align*}$$

    Demuestre que si `$\beta$` es conocida, entonces se tendrá que
    `$\prod_{i=1}^{n} X_i$` es un estadístico suficiente para
    `$\alpha$`.
27. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria de una función de
    densidad de probabilidad dada por
    
$$\begin{align*}f(x;\theta)= e^{-(x-\theta)}; \quad x>\theta\end{align*}$$

    Demuestre que `$X_{(1)} = min(X_1, X_2, \ldots, X_n)$` es un
    estadístico suficiente para `$\theta$`.
28. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria de una función de
    densidad de probabilidad dada por
    
$$\begin{align*}f(x;\theta)= \frac{3x^2}{\theta^3}; \quad 0\leq x\leq \theta;\quad \theta>0\end{align*}$$

    Demuestre que `$X_{(n)} = max(X_1, X_2, \ldots, X_n)$` es un
    estadístico suficiente para `$\theta$`.
29. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de una
    variable aleatoria continua Weibull tal que
    `$X\sim Wei(\alpha, \beta)$`, con función de densidad de
    probabilidad dada por
    
$$\begin{align*}f(x)= \frac{1}{\alpha}\beta x^{\beta-1}e^{-\frac{x^\beta}{\alpha}}; \quad x\geq 0;\quad \alpha>0; \quad \beta>0\end{align*}$$

    Demuestre que, para un valor `$\beta$` conocido,
    `$\sum_{i=1}^{n}X_i^\beta$` es suficiente para `$\alpha$`.
30. Sea `$X_1, X_2, \dots, X_n$` una muestra aleatoria `$iid$` de una
    variable aleatoria de una familia de distribuciones potencias con
    parámetros `$\alpha$` y `$\theta$`, con función de densidad de
    probabilidad dada por
    
$$\begin{align*}f(x)= \frac{\alpha x^{\alpha-1}}{\theta^\alpha}; \quad 0\leq x\leq\theta; \quad \alpha >0; \quad \theta>0\end{align*}$$

    Si `$\theta=3$` demuestre que
    `$\mathbb{E}(X)=\theta\alpha/(\alpha+1)$` y encuentre el estimador
    de `$\alpha$` por el método de los momentos.
    <!-- Preguntar también por segundo momento-->