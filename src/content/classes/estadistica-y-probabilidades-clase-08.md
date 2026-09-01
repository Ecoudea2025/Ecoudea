---
title: "Clase 09"
course: "estadistica-y-probabilidades"
order: 13
classType: "clase"
description: "Distribuciones de probabilidad continuas: - Distribución Uniforme Continua - Distribución Gamma - Distribución Exponencial &nbsp * Propiedad de carencia de memoria."
math: true
bibliography: "../../referencias.bib"
---

Distribuciones de probabilidad continuas
----------------------------------------

### Distribución Uniforme Continua

Se dice que la variable aleatoria `$X$` tiene una distribución uniforme
continua, definida en el intervalo `$(a,b)$`, si su función de
probabilidad está dada por

$$\begin{align*}f(x) = \begin{cases} \frac{1}{b-a} \quad \quad & a\leq x\leq b \\ 0 \quad \quad & \text{en otro caso}\end{cases}\end{align*}$$


#### Media y varianza Uniforme Continua

Si `$X\sim Unif(a,b)$`, entonces se puede probar que la media y varianza
de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X) = \frac{b+a}{2} \quad \quad Var(X)=\frac{(b-a)^2}{12}\end{align*}$$


#### Distribución Acumulada Uniforme Continua

Si `$X\sim Unif(a,b)$`, entonces se puede probar que la función de
distribución acumulada de la variable aleatoria `$X$` es de la forma

$$\begin{align*}F(x) = \frac{x-a}{b-a} \quad \quad & a\leq x\leq b\end{align*}$$


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
Suponga que el tiempo máximo que se puede reservar una sala de
conferencias grande en cierta empresa son cuatro horas. Por experiencia
se sabe que la sala es reservada con mucha frecuencia, tanto para
conferencias extensas como para conferencias breves, de hecho, se puede
suponer que la duración \(X\) de una conferencia tiene una distribución
uniforme en horas en el intervalo \([0, 4]\). Basado en lo anterior
</p>
<ol>
<li>
Calcule la función de densidad de probabilidad \(f(x)\) y la función de
distribución acumulada \(F(X)\) para el tiempo que dura una conferencia.
</li>
<li>
Cuál es la probabilidad de que una conferencia dure menos de \(2\)
horas?
</li>
<li>
Si una conferencia lleva más de \(2\) horas, cuál es la probabilidad de
que dure a lo más \(3\) horas?
</li>
<li>
Cuál es el tiempo medio y la desviación estándar de la duración de una
conferencia?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

Del enunciado anterior, se menciona que la duración de las conferencias
sigue una distribución uniforme con límite mínimo \(a=0\), y límite
máximo \(b=4\), y por tanto, se tendrá que la función de densidad de
probabilidad estará dada por $$\begin{align*}
f(x) = \frac{1}{4-0} = \frac{1}{4} \quad \text{ para } 0\leq x\leq 4
\end{align*}$$

Ahora, al calcular la función de distribución acumulada se tendrá que
$$\begin{align*}
F(x) = \frac{x-0}{4-a} = \frac{x}{4} \quad \text{ para } 0\leq x\leq 4
\end{align*}$$

</li>
<li>

En este punto estamos interesados en calcular la probabilidad de que una
conferencia dure menos de \(2\) horas, es decir, estamos interesados en
calcular $$\begin{align*}
\mathbb{P}(X<2)
\end{align*}$$

en donde, al estar en una situación de una distribución continua, se
tendrá que la probabilidad planteada es equivalente a $$\begin{align*}
\mathbb{P}(X<2) = \mathbb{P}(X \leq 2)
\end{align*}$$

y por tanto, al emplear la función de distribución acumulada
\(F(X)=\mathbb{P}(X\leq x)\) se tendrá que

$$\begin{align*}
\mathbb{P}(X<2) &= F(2) \\
                &= \frac{2}{4} \\
                &= \frac{1}{2} \\
                &= 0.5
\end{align*}$$

Y por tanto se tendrá una probabilidad del \(50\%\) de que una
conferencia en particular tarde menos de \(2\) horas.
</li>
<li>

A diferencia del caso anterior, en éste punto estamos interesados en
calcular una probabilidad condicional, en donde nos piden la
probabilidad de que una conferencia dure como máximo \(3\) horas, cuando
se sabe que ésta conferencia ya lleva más de \(2\) horas y aún no
termina, es decir $$\begin{align*}
\mathbb{P}(X\leq 3 | X>2)
\end{align*}$$

entonces, al aplicar la definición de probabilidad condicional,
tendremos que $$\begin{align*}
\mathbb{P}(X\leq 3 | X>2) &= \frac{\mathbb{P}(X\leq 3 \cap X>2)}{\mathbb{P}(X>2)} \\
                          &= \frac{\mathbb{P}(2 \leq X\leq 3)}{1 - \mathbb{P}(X\leq 2)} \\
                          &= \frac{\mathbb{P}(X\leq 3) - \mathbb{P}(X\leq 2)}{1 - \mathbb{P}(X\leq 2)} \\
\end{align*}$$

Ahora, al aplicar la función de distribución acumulada
\(F(X)=\mathbb{P}(X\leq x)\) se tendrá que $$\begin{align*}
\mathbb{P}(X\leq 3 | X>2) &= \frac{\mathbb{P}(X\leq 3) - \mathbb{P}(X\leq 2)}{1 - \mathbb{P}(X\leq 2)} \\
                          &= \frac{F(3) - F(2)}{1 - F(2)} \\
                          &=\frac{\frac{3-0}{4-0} - \frac{2-0}{4-0}}{1 - \frac{2-0}{4-0}} \\
                          &=\frac{\frac{3}{4} - \frac{2}{4}}{1 - \frac{2}{4}} \\
                          &=\frac{\frac{1}{4}}{\frac{2}{4}} \\
                          &= \frac{1}{2} \\
                          &= 0.5
\end{align*}$$

Y en consecuencia, se tendrá que si una conferencia ha durado más de
\(2\) horas y aún no termina, la probabilidad de que cure como máximo
\(3\) horas es de \(50\%\).
</li>
<li>

Finalmente, estamos interesados en calcular el promedio y desviación
estándar, del número de horas que se reserva la sala de conferencias, y
como, la distribución de probabilidad asociada a la variable aleatoria
es una uniforme, tendremos que la media de la distribución estará dada
por $$\begin{align*}
\mathbb{E}(X) &= \frac{4+0}{2} \\
              &= \frac{4}{2} \\
              &= 2
\end{align*}$$

mientras que la varianza estará dada por $$\begin{align*}
Var(X) &= \frac{(4-0)^2}{12} \\
       &= \frac{4^2}{12} \\
       &= \frac{16}{12} \\
       &= 1.33333
\end{align*}$$ En donde, dada la relación de la varianza con la
desviación estándar, tendremos que $$\begin{align*}
Sd(X) &= \sqrt{Var(X)}\\
      &= \sqrt{1.33333}\\
      &= 1.154699
\end{align*}$$

Por lo cual tendremos que, el número promedio de horas que se reserva la
sala de conferencias es de \(2\) horas, con una desviación estándar de
\(1.15\) horas.
</li>
</ol>
</main>

### Función Gamma

La función gamma se define como

$$\begin{align*}\Gamma(\alpha) = \int^\infty_0 t^{\alpha-1}e^{-t} dt\end{align*}$$


#### Propiedades Función Gamma

<ol type="a">
<li>
\(\Gamma(\alpha) = (\alpha-1)\Gamma(\alpha -1)\), para todo \(\alpha>0\)
</li>
<li>
\(\Gamma(n) = (n-1)!\), siendo \(n\) un entero positivo.
</li>
<li>
\(\Gamma(1/2) = \sqrt{\pi}\)
</li>
</ol>
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
Suponga que se tiene interés en calcular los siguiente valores con la
función gamma
</p>
<ol>
<li>
\(\Gamma(5)\)
</li>
<li>
\(\Gamma(3.5)\)
</li>
<li>
\(\Gamma(2.9)\)
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
En este caso estamos interesados en calcular el valor de la función
gamma, cuando \(\alpha=5\), en donde se observa que este valor es un
entero y por tanto $$\begin{align*}
\Gamma(5) &= (5-1)!\\
          &= 4! \\
          &= 4\times 3 \times 2 \times 1
          &= 24
\end{align*}$$
</li>
<li>
A diferencia del caso anterior, en éste el valor de la función gamma que
nos piden no es un entero, y por tanto, como \(\alpha=3.5\) entonces el
valor de la función gamma será de la forma $$\begin{align*}
\Gamma(3.5) &= (3.5-1)\Gamma(3.5 -1) \\
            &= (2.5)\Gamma(2.5) \\
            &= (2.5)(2.5-1)\Gamma(2.5 -1) \\
            &= (2.5)(1.5)\Gamma(1.5) \\
            &= (2.5)(1.5)(1.5 - 1)\Gamma(1.5 - 1) \\
            &= (2.5)(1.5)(0.5)\Gamma(0.5) \\
\end{align*}$$ Y como \(\Gamma(0.5)=\sqrt{\pi}\), entonces tendremos que
$$\begin{align*}
\Gamma(3.5) &= (2.5)(1.5)(0.5)\Gamma(0.5) \\
            &=(2.5)(1.5)(0.5)(\sqrt{\pi})\\
            &= 3.323351
\end{align*}$$
</li>
<li>
A diferencia del caso anterior, en éste el valor de la función gamma que
nos piden no es un entero, y por tanto, como \(\alpha=3.5\) entonces el
valor de la función gamma será de la forma $$\begin{align*}
\Gamma(3.5) &= (3.5-1)\Gamma(3.5 -1) \\
            &= (2.5)\Gamma(2.5) \\
            &= (2.5)(2.5-1)\Gamma(2.5 -1) \\
            &= (2.5)(1.5)\Gamma(1.5) \\
            &= (2.5)(1.5)(1.5 - 1)\Gamma(1.5 - 1) \\
            &= (2.5)(1.5)(0.5)\Gamma(0.5) \\
\end{align*}$$ Y como por propiedades tenemos que
\(\Gamma(0.5)=\sqrt{\pi}\), entonces al reemplazar tendremos que
$$\begin{align*}
\Gamma(3.5) &= (2.5)(1.5)(0.5)\Gamma(0.5) \\
            &=(2.5)(1.5)(0.5)(\sqrt{\pi})\\
            &= 3.323351
\end{align*}$$
</li>
<li>
En este punto estamos interesados en calcular el valor de la función
gamma de \(2.9\), pero en este caso no podremos calcular mediante
propiedades el valor de la función ya que $$\begin{align*}
\Gamma(2.9) &= (2.9-1)\Gamma(2.9 -1) \\
            &= (1.9)\Gamma(1.9) \\
            &= (1.9)(1.9-1)\Gamma(1.9 -1) \\
            &= (1.9)(0.9)\Gamma(0.9)
\end{align*}$$ No es posible calcular de forma manual mediante
propiedades el valor de la función Gamma cuando el valor \(\alpha\) no
es un entero o terminado en \(0.5\), y en consecuencia para calcular el
valor de interés, se requerirá hacer una aproximación numérica para la
integral $$\begin{align*}
\Gamma(0.9) = \int_{0}^\infty t^{0.9 -  1} e^{-t} dt
\end{align*}$$ la cual puede realizarse con la calculadora, o un
software tal como lo es <tt>R</tt> mediante la función <tt>gamma()</tt>,
o Excel mediante la función <tt>GAMMA()</tt>, las cuales arrojan que el
valor de la función gamma para \(0.9\) será $$\begin{align*}
\Gamma(0.9) = 1.068629
\end{align*}$$ Y por tanto el valor de la función gamma de interés será
igual a $$\begin{align*}
\Gamma(2.9) &= (1.9)(0.9)\Gamma(0.9) \\
            &= (1.9)(0.9)(1.068629)\\
            &= 1.827355
\end{align*}$$ Alternativamente se puede buscar en la calculadora o en
los software, el valor de la gamma de \(2.9\) directamente, en donde
$$\begin{align*}
\Gamma(2.9) &= \int_{0}^\infty t^{2.9 -  1} e^{-t} dt \\
            &= 1.827355
\end{align*}$$ y en consecuencia se deberá obtener el mismo valor.
</li>
</ol>
</main>

### Distribución Gamma

Se dice que la variable aleatoria `$X$` tiene una distribución Gamma con
parámetro de forma `$\alpha$` y de razón `$\beta$`, si su función de
densidad de probabilidad está dada por

$$\begin{align*}f(x) = \begin{cases} \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-{\frac{x}{\beta}}} \quad \quad & x>0; \alpha>0; \beta>0 \\ 0 \quad \quad & \text{en otro caso}\end{cases}\end{align*}$$


#### Media y Varianza Gamma

Si `$X\sim Gamma(\alpha,\beta)$`, entonces se puede probar que la media
y varianza de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X) = \frac{\alpha}{\beta} \quad \quad Var(X)=\frac{\alpha}{\beta^2}\end{align*}$$


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
Suponga que se realiza un estudio sobre el tiempo de transferencia de
datos de un sistema de red informática, en milisegundos. Si se encuentra
que el tiempo de transferencia se distribuye gamma con media
\(37.5_{ms}\) y desviación estándar de \(21.36196_{ms}\)
</p>
<ol>
<li>
Cuales son los valores de los parámetros de la distribución Gamma?
</li>
<li>
Cual es la probabilidad de que el tiempo de transferencia de datos
exceda \(50_{ms}\)?
</li>
<li>
Si el tiempo de transferencia ya ha superado \(20_{ms}\), cuál es la
probabilidad de que no supere los \(70_{ms}\)?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

En el enunciado nos mencionan que las transferencias de datos en un
sistema de red informática, sigue una distribución gamma con media y
desviación estándar dadas por \(37_{ms}\) y \(21.36196_{ms}\),
respectivament, y nos piden que calculemos el valor de los parámetros de
la misma. Y por ello debemos despejar de las fórmulas de media y
varianza el valor de los dos parámetros, tal que $$\begin{align*}
\mathbb{E}(X) &= \frac{\alpha}{\beta} \\
37 &= \frac{\alpha}{\beta}\\
\end{align*}$$ mientras que $$\begin{align*}
Var(X)     &= \frac{\alpha}{\beta^2} \\
Sd(X)^2    &= \frac{\alpha}{\beta^2} \\
21.36196^2 &= \frac{\alpha}{\beta^2}
\end{align*}$$

Entonces estamos en una situación dada por dos ecuaciones y dos
incognitas, y por tanto, podemos despejar uno de los parámetros de una
de las ecuaciones y reemplazar en la otra, para obtener el valor de uno
de los parametros tal que $$\begin{align*}
37    &= \frac{\alpha}{\beta}\\
\beta &= \frac{\alpha}{37}
\end{align*}$$ entonces al reemplazar el resultado anterior en la
fórmula de la varianza tendremos que el valor del parámetro \(\alpha\)
será igual a $$\begin{align*}
21.36196^2 &= \frac{\alpha}{\left(\frac{\alpha}{37}\right)^2}\\
21.36196^2 &= \frac{37^2}{\alpha}\\
\alpha     &= \frac{37^2}{21.36196^2} \\
\alpha     &= 3
\end{align*}$$ ahora al reemplazar el valor de \(\alpha=3\) en la
fórmula de la media tendremos que $$\begin{align*}
37    &= \frac{3}{\beta}\\
\beta &= \frac{3}{37}
\end{align*}$$ Y por tanto, se tendrá que las transferencias de datos en
un sistema de red informática tendrá una distribución
\(Gamma(\alpha= 3, \beta = 3/37)\).
</li>
<li>

Basados en los parámetros calculados en el punto anterior, estamos
interesados en calcular la probabilidad de que el tiempo de
transferencia de datos exceda los \(50_{ms}\), es decir $$\begin{align*}
\mathbb{P}(X>50) 
\end{align*}$$ la cual, al emplear la distribución
\(Gamma(\alpha=3, \beta=3/37)\) se tendrá que $$\begin{align*}
\mathbb{P}(X>50) &= \int_{50}^{\infty} \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-{x\beta}} dx \\
                 &= \int_{50}^{\infty} \frac{(3/37)^3}{\Gamma(3)} x^{3-1}e^{-{\frac{3x}{37}}} dx \\
                 &= \frac{3^3}{\Gamma(3)(37)^3}\int_{50}^{\infty}  x^{2}e^{-{\frac{3x}{37}}} dx
\end{align*}$$

En donde para calcular tan integral debemos realizar integración por
partes dos veces, debido a que el parámetro \(\alpha=3\), tal que
$$\begin{align*}
\mathbb{P}(X>50) &= \frac{3^3}{\Gamma(3)(37)^3}\int_{50}^{\infty}  x^{2}e^{-{\frac{3x}{37}}} dx\\
                 &=> u=x^2 \quad \quad \; dv = e^{-{\frac{3x}{37}}} dx \\
                 &=> du= 2x dx \quad v = - \frac{37}{3} e^{-{\frac{3x}{37}}} \\
                 &= \frac{3^3}{\Gamma(3)(37)^3} \left[-\frac{37}{3}x^2 e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty + \frac{(2)(37)}{3}\int_{50}^{\infty}  xe^{-{\frac{3x}{37}}} dx\right] \\
                 &=> u=x \quad \quad \; dv = e^{-{\frac{3x}{37}}} dx \\
                 &=> du= dx \quad v = - \frac{37}{3} e^{-{\frac{3x}{37}}} \\
                 &= \frac{3^3}{\Gamma(3)(37)^3} \left[-\frac{37}{3}x^2 e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty + \frac{(2)(37)}{3} \left\{-\frac{37}{3}x e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty+ \frac{37}{3} \int_{50}^\infty e^{-{\frac{3x}{37}}}dx\right\} \right] \\
                 &= \frac{3^3}{\Gamma(3)(37)^3} \left[-\frac{37}{3}x^2 e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty + \frac{(2)(37)}{3} \left\{-\frac{37}{3} xe^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty - \frac{37^2}{3^2}   e^{-{\frac{3x}{37}}}\Bigg|_{50}^\infty\right\} \right] \\
                 &= \frac{3^3}{\Gamma(3)(37)^3} \left[-\frac{37}{3}x^2 e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty -\frac{(2)(37^2)x}{3^2} e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty - \frac{(2)(37^3)}{3^3}   e^{-{\frac{3x}{37}}}\Bigg|_{50}^\infty \right] \\
                 &= \frac{3^3}{\Gamma(3)(37)^3} \left[-\frac{37}{3}x^2 e^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty -\frac{(2)(37^2)}{3^2} xe^{-{\frac{3x}{37}}} \Bigg|_{50}^\infty - \frac{(2)(37^3)}{3^3}   e^{-{\frac{3x}{37}}}\Bigg|_{50}^\infty \right] \\
                 &= \left(-\frac{3^2}{\Gamma(3)(37)^2}x^2 e^{-{\frac{3x}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} xe^{-{\frac{3x}{37}}} - \frac{(2)}{\Gamma(3)}   e^{-{\frac{3x}{37}}}\right)\Bigg|_{50}^\infty 
\end{align*}$$ Por tanto al evaluar la variable \(x\) en los límites de
interés tendremos que $$\begin{align*}
\mathbb{P}(X>50) &= \left(-\frac{3^2}{\Gamma(3)(37)^2}x^2 e^{-{\frac{3x}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} xe^{-{\frac{3x}{37}}} - \frac{(2)}{\Gamma(3)}   e^{-{\frac{3x}{37}}}\right)\Bigg|_{50}^\infty \\
                 &= \left(0 + 0 + 0 \right) - \left(-\frac{3^2}{\Gamma(3)(37)^2}(50^2) e^{-{\frac{3(50)}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} (50)e^{-{\frac{3(50)}{37}}} - \frac{(2)}{\Gamma(3)} e^{-{\frac{3(50)}{37}}}\right) \\
                 &= \frac{3^2}{\Gamma(3)(37)^2}(50^2) e^{-{\frac{3(50)}{37}}} + \frac{(2)(3)}{\Gamma(3)(37)} (50)e^{-{\frac{3(50)}{37}}} + \frac{(2)}{\Gamma(3)} e^{-{\frac{3(50)}{37}}} \\
                 &= 0.14259 + 0.07035 + 0.01735 \\
                 &= 0.23029
\end{align*}$$ Es decir, que la probabilidad de que el tiempo de
transferencia de datos exceda los \(50_{ms}\), es del \(23.029\%\).
</li>
<li>
En este punto estamos interesados en calcula la probabilidad de que el
tiempo de transferencia de datos sea como máximo \(70_{ms}\), cuando se
sabe que ya ha superado los \(20_{ms}\), por lo cual se tendrá una
probabilidad condicional de la forma $$\begin{align*}
\mathbb{P}(X\leq 70 | X>20) &= \frac{\mathbb{P}(X\leq 70 \cap X>20)}{\mathbb{P}(X>20)} \\
                            &= \frac{\mathbb{P}(20 < X \leq 70)}{\mathbb{P}(X>20)}
\end{align*}$$ Por tanto debemos calcular dos probabilidades diferentes,
y luego realizar la división de las mismas, en donde, al emplear la
integral realizada en el punto anterior, tendremos que la probabilidad
del numerador será igual a $$\begin{align*}
\mathbb{P}(20 < X \leq 70) &= \left(-\frac{3^2}{\Gamma(3)(37)^2}x^2 e^{-{\frac{3x}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} xe^{-{\frac{3x}{37}}} - \frac{(2)}{\Gamma(3)}   e^{-{\frac{3x}{37}}}\right)\Bigg|_{20}^{70} \\
                 &= \left(-\frac{3^2}{\Gamma(3)(37)^2}(70^2) e^{-{\frac{3(70)}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} (70)e^{-{\frac{3(70)}{37}}} - \frac{(2)}{\Gamma(3)} e^{-{\frac{3(70)}{37}}}\right) \\
                 & \quad \quad - \left(-\frac{3^2}{\Gamma(3)(37)^2}(20^2) e^{-{\frac{3(20)}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} (20)e^{-{\frac{3(20)}{37}}} - \frac{(2)}{\Gamma(3)} e^{-{\frac{3(20)}{37}}}\right) \\
                 &= \left(- 0.05522 - 0.01946 - 0.00343\right) - \left(- 0.25978 - 0.32040 - 0.19758\right) \\
                 &= (-0.07811) - (- 0.77776) \\
                 &= 0.69965
\end{align*}$$ Ahora, calculamos la probabilidad asociada al denominador
de la misma forma $$\begin{align*}
\mathbb{P}(X > 20) &= \left(-\frac{3^2}{\Gamma(3)(37)^2}x^2 e^{-{\frac{3x}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} xe^{-{\frac{3x}{37}}} - \frac{(2)}{\Gamma(3)}   e^{-{\frac{3x}{37}}}\right)\Bigg|_{20}^{\infty} \\
                 &= \left(0 + 0 + 0\right) - \left(-\frac{3^2}{\Gamma(3)(37)^2}(20^2) e^{-{\frac{3(20)}{37}}} - \frac{(2)(3)}{\Gamma(3)(37)} (20)e^{-{\frac{3(20)}{37}}} - \frac{(2)}{\Gamma(3)} e^{-{\frac{3(20)}{37}}}\right) \\
                 &= - \left(- 0.25978 - 0.32040 - 0.19758\right) \\
                 &= 0.77776
\end{align*}$$ Y por tanto, al reemplazar estos valores en la
probabilidad condicional tendremos que $$\begin{align*}
\mathbb{P}(X\leq 70 | X>20) &= \frac{\mathbb{P}(20 < X \leq 70)}{\mathbb{P}(X>20)} \\
                            &= \frac{0.69965}{0.77776} \\
                            &= 0.8995706
\end{align*}$$ Y por tanto, si el tiempo de transferencia de datos ha
superado \(20_{ms}\), se tendrá una probabilidad del \(89.96\%\) de que
el tiempo de transferencia será como máximo de \(70_{ms}\).
</li>
</ol>
</main>

### Distribución Exponencial

Se dice que la variable aleatoria `$X$` tiene una distribución
Exponencial con parámetro de razón `$\lambda$`, si su función de
densidad de probabilidad está dada por

$$\begin{align*}f(x) = \begin{cases} \lambda e^{-x\lambda} \quad \quad & x>0; \lambda>0 \\ 0 \quad \quad & \text{en otro caso}\end{cases}\end{align*}$$

en donde se observa que ésta distribución es un caso particular de la
distribución Gamma cuando `$\alpha=1$`.

#### Media y Varianza Exponencial

Si `$X\sim Exp(\lambda)$`, entonces se puede probar que la media y
varianza de la variable aleatoria `$X$` están dadas por

$$\begin{align*}\mathbb{E}(X) = \frac{1}{\lambda} \quad \quad Var(X)= \frac{1}{\lambda^2}\end{align*}$$


#### Distribución Acumulada Exponencial

Si `$X\sim Exp(\lambda)$`, entonces se puede probar que la función de
distribución acumulada de la variable aleatoria `$X$` es de la forma

$$\begin{align*}F(x) =  1 - e^{-x\lambda} \quad \quad & x>0; \lambda>0\end{align*}$$


<button id="Show4" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide4" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito4">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga que el tiempo entre llegadas sucesiva de personas a un cajero de
Bancolombia, posee una distribución Exponencial con un tiempo promedio
de \(0.8\) minutos. Entonces, basados en ésto
</p>
<ol>
<li>
Calcule la probabilidad de que la próxima persona en llegar al cajero
tarde más de \(4\) minutos?
</li>
<li>
Si han pasado \(2\) minutos y aún no llega ningúna persona al cajero,
cuál es la probabilidad de que la próxima persona tarde más de \(4\)
minutos?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>
Para calcular la probabilidad de que la próxima persona tarde más de
\(4\) minutos en llegar al cajero, debemos primero encontrar el valor
del parámetro de la distribución Exponencial, en donde, nos dicen en el
enunciado, que el tiempo promedio entre llegadas sucesivas es de \(0.8\)
minutos, tal que $$\begin{align*}
\mathbb{E}(X) &= 0.8 = \frac{4}{5}
\end{align*}$$ Entonces como para la distribución Exponencial se tiene
que el valor de la esperanza matemática está dada por $$\begin{align*}
\mathbb{E}(X) &= \frac{1}{\lambda}
\end{align*}$$ se tendrá que el parámetro \(\lambda\) de la distribución
Exponencial será igual a $$\begin{align*}
\lambda &= \frac{5}{4}
\end{align*}$$ Ahora, con el valor de este parámetro podemos calcular la
probabilidad de interés empleando la función de distribución acumulada
Exponencial, tal que $$\begin{align*}
\mathbb{P}(X>4) &= 1 - \mathbb{P}(X\leq 4) \\
                &= 1 - F(4) \\
                &= 1 - \left(1 - e^{-{\frac{4(5)}{4}}}\right) \\
                &= 1 - \left(1 - e^{-5}\right) \\
                &= e^{-5} \\
                &= 0.006737947
\end{align*}$$ Es decir que la probabilidad de que la próxima persona en
llegar cajero de Bancolombia tarde más de \(4\) minutos es de
\(0.67\%\).
</li>
<li>

En esta ocasión estamos interesados en calcular una probabilidad
condicional, en donde nos piden la probabilidad de que una persona tarde
más de \(4\) minutos en llegar al cajero de Bancolombia, si se sabe que
ya han pasado \(2\) minutos y aún no llega ningúna persona al cajero, es
decir $$\begin{align*}
\mathbb{P}(X>4|X>2) &= \frac{\mathbb{P}(X>4 \cap X>2)}{\mathbb{P}(X>2)} \\
                    &= \frac{\mathbb{P}(X>4)}{\mathbb{P}(X>2)} \\
                    &= \frac{1 - \mathbb{P}(X \leq 4)}{1 - \mathbb{P}(X \leq 2)} \\
                    &= \frac{1 - F(4)}{1 - F(2)} \\
                    &= \frac{1 - \left(1 - e^{-{\frac{4}{0.8}}}\right)}{1 - \left(1 - e^{-{\frac{2}{0.8}}}\right)} \\
                    &= \frac{e^{-{\frac{4}{0.8}}}}{e^{-{\frac{2}{0.8}}}} \\
                    &= \frac{0.006737947}{0.082085} \\
                    &= 0.082085
\end{align*}$$

Y por tanto se tendrá una probabilidad de \(8.21\%\) de que la próxima
persona que llega al cajero de Bancolombia tarde más de \(4\) minutos,
dado que ya han pasado \(2\) minutos y aún no ha llegado ninguna
persona.
</li>
</ol>
</main>

#### Propiedad de carencia de memoria

Suponga que `$X$` es una variable aleatoria tal que
`$X\sim Exp(\lambda)$`, entonces sean dos reales positivos `$a$` y
`$b$`, entonces se puede probar que

1.  `$\mathbb{P}(X\geq a+b | x \geq b) = \mathbb{P}(X\geq a)$`

2.  `$\mathbb{P}(X\leq a+b | x \geq b) = \mathbb{P}(X\leq a)$`

<button id="Show5" class="btn btn-secondary">
Mostrar Ejercicio
</button>
<button id="Hide5" class="btn btn-info">
Ocultar Ejercicio
</button>
<main id="botoncito5">
<h3 data-toc-skip>
Ejercicio
</h3>
<p>
Suponga que el tiempo entre llegadas sucesiva de personas a un cajero de
Bancolombia, posee una distribución Exponencial con un tiempo promedio
de \(0.8\) minutos. Entonces, basados en ésto
</p>
<ol>
<li>
Cuál es la probabilidad de que la próxima persona tarde a lo más \(2\)
minutos, si ya han pasado \(0.8\) minutos y aún no llega ninguna persona
al cajero?
</li>
<li>
Si han pasado \(2\) minutos y aún no llega ningúna persona al cajero,
cuál es la probabilidad de que la próxima persona tarde más de \(4\)
minutos?
</li>
</ol>
<h3 data-toc-skip>
Solución
</h3>
<ol>
<li>

Dado que para este ejercicio tenemos que el tiempo que tarda una persona
en llegar a un cajero de Bancolombia se distribuye Exponencialmente con
parámetro \(\lambda=5/4\), tendremos que, la probabilidad de que la
próxima persona tarde a lo más \(2\) minutos, dado que ya han pasado
\(0.8\) minutos y no llega ninguna persona, estará dada por una
probabilidad condicional de la forma $$\begin{align*}
\mathbb{P}(X\leq2|X>0.8) 
\end{align*}$$ la cual se podrá calcular mediante mediante la definición
de probabilidad condicional, de la forma

$$\begin{align*}
\mathbb{P}(X\leq2|X>0.8) = \frac{\mathbb{P}(X\leq2 \cap X>0.8) }{\mathbb{P}(X>0.8)}
\end{align*}$$

Otra alternativa surge debido a que el tiempo que tarda una persona en
llegar a un cajero de Bancolombia posee una distribución Exponencial, y
por tanto, por propiedad de carencia de memoria, la probabilidad
condicional será igual a $$\begin{align*}
\mathbb{P}(X\leq2|X>0.8) &= \mathbb{P}(X\leq2 - 0.8 + 0.8|X>0.8) \\
                         &= \mathbb{P}(X\leq1.2 + 0.8|X>0.8)
\end{align*}$$

En donde, por propiedad de carencia de memoria de la distribución
exponencial se tendrá una estructura similar a $$\begin{align*}
\mathbb{P}(X\leq a+b | x \geq b) = \mathbb{P}(X\leq a)
\end{align*}$$ y por tanto, la probabilidad de interés será de la forma
$$\begin{align*}
\mathbb{P}(X\leq2|X>0.8) &= \mathbb{P}(X\leq1.2 + 0.8|X>0.8) \\
                         &= \mathbb{P}(X\leq1.2) \\
                         &= F(1.2) \\
                         &= 1 - e^{-\frac{(1.2)5}{4}} \\
                         &= 1 - 0.2231302 \\
                         &= 0.7768698
\end{align*}$$

lo cual significa, que exite una probablidad de \(77.69\%\) de que una
persona tarde como maximo \(2\) minutos en llegar a un cajero, si ya han
pasado a lo más \(0.8\) minutos y aún no ha llegado ninguna persona.
</li>
<li>

Similar al punto anterior, estamos interesado en calcular una
probabilidad condicional, en donde para este caso, nos piden la
probabilidad de que una persona tarde más de \(4\) minutos en llegar al
cajero de Bancolombia, si se sabe que ya han pasado \(2\) minutos y aún
no llega ningúna persona al cajero, tal que $$\begin{align*}
\mathbb{P}(X>4|X>2) 
\end{align*}$$ Entonces, al aplicar la propiedad de carencia de memoria
de la distribución Exponencial, se tendrá que $$\begin{align*}
\mathbb{P}(X\geq a+b | x \geq b) = \mathbb{P}(X\geq a)
\end{align*}$$ y por tanto la probabilidad de interés será igual a
$$\begin{align*}
\mathbb{P}(X>4|X>2) &= \mathbb{P}(X > 4 - 2 + 2|X > 2) \\
                    &= \mathbb{P}(X > 2 + 2|X > 2) \\
                    &= \mathbb{P}(X > 2) \\
                    &= 1 - \mathbb{P}(X \leq 2) \\
                    &= 1 - F(2) \\
                    &= 1 - \left(1 - e^{-\frac{2}{0.8}} \right) \\
                    &= e^{-\frac{2}{0.8}} \\
                    &= 0.082085
\end{align*}$$

Y por tanto se tendrá una probabilidad de \(8.21\%\) de que la próxima
persona que llega al cajero de Bancolombia tarde más de \(4\) minutos,
dado que ya han pasado \(2\) minutos y aún no ha llegado ninguna
persona.
</li>
</ol>
</main>