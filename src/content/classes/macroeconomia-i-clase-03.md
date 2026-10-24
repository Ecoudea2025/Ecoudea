---
title: "Clase 03: Optimización Intertemporal, Ecuación de Euler y Función CRRA"
course: "macroeconomia-i"
order: 3
classType: "clase"
description: "Resolución del problema del consumidor en dos períodos por sustitución y Lagrange, deducción de la Ecuación de Euler, análisis gráfico y estudio de la función CRRA."
math: true
---


El Problema de Optimización del Consumidor
------------------------------------------

Habiendo formalizado la restricción presupuestaria intertemporal (los recursos) y la función de utilidad intertemporal (las preferencias), el consumidor racional busca resolver un problema de **maximización de utilidad sujeto a su restricción de recursos**.

En su formulación general para un horizonte de `$N$` períodos con certidumbre:

$$
\begin{align*}\max_{\{C_{t+i}\}_{i=0}^N} \quad & \sum_{i=0}^N \beta^i u(C_{t+i}) \\ \text{s.a.} \quad & \sum_{i=0}^N \frac{C_{t+i}}{(1 + r)^i} = (1 + r)A_t + \sum_{i=0}^N \frac{Y_{\ell t+i} - T_{t+i}}{(1 + r)^i} \\ & C_{t+i} > 0, \quad \forall i = 0, 1, \ldots, N\end{align*}
$$

Este problema involucra `$N+1$` variables de decisión (las elecciones de consumo en cada fecha). Al plantear el Lagrangiano, se obtiene un sistema de `$N+1$` ecuaciones con `$N+1$` incógnitas cuya solución está garantizada y es única debido a la estricta concavidad de `$u(\cdot)$` y la linealidad de la restricción presupuestaria.


El Modelo Fundamental en Dos Períodos ($t=1, 2$)
-------------------------------------------------

Para estudiar la mecánica económica con máxima claridad analítica y gráfica, analizamos el caso de dos períodos (`$t = 1, 2$`), asumiendo que el agente inicia sin activos previos (`$A_1 = 0$`) y no deja herencias (`$A_3 = 0$`):

* Función objetivo de utilidad intertemporal:

$$
\begin{align*}U(C_1, C_2) = u(C_1) + \beta u(C_2), \quad \text{con } \beta = \frac{1}{1 + \rho}\end{align*}
$$

* Restricción presupuestaria intertemporal en dos períodos:

$$
\begin{align*}C_1 + \frac{C_2}{1 + r} = Y_1 + \frac{Y_2}{1 + r}\end{align*}
$$


Deducción Paso a Paso de la Ecuación de Euler
---------------------------------------------

Presentamos a continuación los dos métodos matemáticos fundamentales para derivar la regla óptima de consumo.

### Método 1: Sustitución Directa

1. **Despejar `$C_1$` de la restricción presupuestaria:**
   
$$
\begin{align*}C_1 = Y_1 + \frac{Y_2}{1 + r} - \frac{C_2}{1 + r}\end{align*}
$$

2. **Sustituir `$C_1$` en la función de utilidad intertemporal:**
   
El problema se reduce a optimizar respecto a una única variable, `$C_2$`:

$$
\begin{align*}\max_{C_2} \quad u\left( Y_1 + \frac{Y_2}{1 + r} - \frac{C_2}{1 + r} \right) + \beta u(C_2)\end{align*}
$$

3. **Condición de Primer Orden (FOC):**
   
Derivando respecto a `$C_2$` mediante la regla de la cadena e igualando a cero:

$$
\begin{align*}\frac{\partial U}{\partial C_2} = u'(C_1) \cdot \frac{\partial C_1}{\partial C_2} + \beta u'(C_2) = 0\end{align*}
$$

Dado que `$\frac{\partial C_1}{\partial C_2} = -\frac{1}{1 + r}$`:

$$
\begin{align*}-\frac{u'(C_1)}{1 + r} + \beta u'(C_2) = 0\end{align*}
$$

4. **Reorganización final:**
   
$$
\begin{align*}u'(C_1) = \beta (1 + r) u'(C_2) \iff \frac{u'(C_1)}{\beta u'(C_2)} = 1 + r\end{align*}
$$

### Método 2: Multiplicadores de Lagrange

1. **Definición de la función Lagrangiana:**
   
$$
\begin{align*}\mathcal{L}(C_1, C_2, \lambda) = u(C_1) + \beta u(C_2) + \lambda \left[ Y_1 + \frac{Y_2}{1 + r} - C_1 - \frac{C_2}{1 + r} \right]\end{align*}
$$

2. **Condiciones de primer orden:**
   
$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_1} &= u'(C_1) - \lambda = 0 \implies \lambda = u'(C_1) \tag{3.1} \\ \frac{\partial \mathcal{L}}{\partial C_2} &= \beta u'(C_2) - \frac{\lambda}{1 + r} = 0 \implies \lambda = \beta(1 + r) u'(C_2) \tag{3.2} \\ \frac{\partial \mathcal{L}}{\partial \lambda} &= Y_1 + \frac{Y_2}{1 + r} - C_1 - \frac{C_2}{1 + r} = 0 \tag{3.3}\end{align*}
$$

3. **Eliminación del multiplicador de Lagrange `$\lambda$`:**
   
Igualando las expresiones (1) y (2):

$$
\begin{align*}u'(C_1) = \beta(1 + r)u'(C_2) \iff \frac{u'(C_1)}{\beta u'(C_2)} = 1 + r\end{align*}
$$

### Interpretación Económica y Microfundamentos

Esta regla se conoce como la **Ecuación de Euler para el consumo** (o ecuación de transición del consumo).

En microeconomía del consumidor, la condición de tangencia óptima establece que la Relación Marginal de Sustitución (`$RMS$`) debe igualar la razón de precios:

$$
\begin{align*}RMS_{X_1, X_2} = \frac{UmgX_1}{UmgX_2} = \frac{P_1}{P_2}\end{align*}
$$

En el contexto intertemporal:
* La utilidad marginal del consumo presente es `$UmgC_1 = u'(C_1)$`.
* La utilidad marginal descontada del consumo futuro es `$\beta UmgC_2 = \beta u'(C_2)$`.
* El precio del consumo presente es `$P_1 = 1$` y el precio del consumo futuro en términos presentes es `$P_2 = \frac{1}{1 + r}$`. Por ende, el precio relativo del presente frente al futuro es:

$$
\begin{align*}\frac{P_1}{P_2} = \frac{1}{\frac{1}{1 + r}} = 1 + r\end{align*}
$$

La Ecuación de Euler expresa el principio de arbitraje intertemporal: en el óptimo, la pérdida de bienestar de renunciar a una unidad de consumo hoy (`$u'(C_1)$`) debe ser exactamente igual a la ganancia de bienestar obtenida al prestar esa unidad a la tasa `$r$` y consumir `$(1+r)$` unidades en el futuro (`$\beta (1+r) u'(C_2)$`).


Análisis Gráfico en el Plano ($C_1, C_2$) y Estática Comparativa
---------------------------------------------------------------

Despejando `$C_2$` en función de `$C_1$` a partir de la restricción presupuestaria:

$$
\begin{align*}C_2 = (1 + r)Y_1 + Y_2 - (1 + r)C_1\end{align*}
$$

Esta es la ecuación de una línea recta en el plano `$(C_1, C_2)$` con:
* **Pendiente:** `$-(1 + r)$`.
* **Punto de dotación:** Siempre pasa por la canasta de dotación inicial `$(Y_1, Y_2)$`.

### Tipología de Agentes: Ahorradores vs. Prestatarios

* **Acreedor o Ahorrador:** Si `$C_1^* < Y_1$`, el individuo consume menos de lo que ingresa en el período 1. Su ahorro es positivo:

$$
\begin{align*}S_1 = Y_1 - C_1^* > 0\end{align*}
$$

* **Deudor o Prestatario:** Si `$C_1^* > Y_1$`, el individuo consume por encima de su dotación corriente. Su ahorro es negativo (se endeuda):

$$
\begin{align*}S_1 = Y_1 - C_1^* < 0\end{align*}
$$

### Estática Comparativa 1: Variación en la Tasa de Interés ($r$)

Un aumento en `$r$` hace que la recta presupuestaria rote en sentido de las agujas del reloj alrededor del punto fijo de dotación `$(Y_1, Y_2)$`, volviéndose más empinada:

1. **Efecto Sustitución (ES):** El consumo presente `$C_1$` se vuelve relativamente más costoso frente a `$C_2$`. El agente sustituye consumo presente por consumo futuro (`$\Delta r \implies \nabla C_1$`, `$\Delta C_2$`, incentiva el ahorro `$\Delta S_1$`).
2. **Efecto Ingreso (EI):**
   * Para un **ahorrador** (`$S_1 > 0$`), el alza en `$r$` eleva los ingresos por intereses futuros. El individuo se enriquece, estimulando un aumento tanto de `$C_1$` como de `$C_2$`. En consecuencia, para un ahorrador el EI y el ES operan en direcciones opuestas sobre `$C_1$`.
   * Para un **deudor** (`$S_1 < 0$`), el alza en `$r$` encarece el servicio de la deuda. El individuo se empobrece, lo que refuerza la reducción de `$C_1$`.

### Estática Comparativa 2: Variación en el Ingreso Laboral ($Y_1$)

Un incremento en `$Y_1$` desplaza la recta presupuestaria paralelamente hacia afuera:

$$
\begin{align*}\frac{\partial C_1}{\partial Y_1} > 0, \quad \frac{\partial C_2}{\partial Y_1} > 0\end{align*}
$$

Debido a que las curvas de indiferencia son estrictamente convexas, el individuo busca **suavizar su consumo** (*consumption smoothing*). No consume todo el aumento de ingreso en el período 1; ahorra una parte significativa para elevar también su consumo en el período 2.


La Función de Utilidad CRRA (Constant Relative Risk Aversion)
-------------------------------------------------------------

La función de utilidad más empleada en la macroeconomía contemporánea es la familia CRRA:

$$
\begin{align*}u(C) = \begin{cases} \frac{C^{1-\sigma} - 1}{1 - \sigma} & \text{si } \sigma > 0, \; \sigma \neq 1 \\ \ln(C) & \text{si } \sigma = 1 \end{cases}\end{align*}
$$

donde `$\sigma$` es el coeficiente de aversión relativa al riesgo.

### Demostración del Caso Logarítmico vía L'Hôpital

Para demostrar que `$\lim_{\sigma \to 1} \frac{C^{1-\sigma}-1}{1-\sigma} = \ln(C)$`, reescribimos la potencia usando la función exponencial:

$$
\begin{align*}C^{1-\sigma} = e^{(1-\sigma)\ln(C)}\end{align*}
$$

Al evaluar el límite cuando `$\sigma \to 1$`, encontramos una indeterminación de la forma `$\frac{0}{0}$`. Aplicando la regla de L'Hôpital respecto al parámetro `$\sigma$`:

$$
\begin{align*}\lim_{\sigma \to 1} \frac{e^{(1-\sigma)\ln(C)} - 1}{1 - \sigma} &= \lim_{\sigma \to 1} \frac{\frac{\text{d}}{\text{d}\sigma}\left[ e^{(1-\sigma)\ln(C)} - 1 \right]}{\frac{\text{d}}{\text{d}\sigma}[1 - \sigma]} \\ &= \lim_{\sigma \to 1} \frac{-\ln(C) e^{(1-\sigma)\ln(C)}}{-1} \\ &= \ln(C) e^{0} = \ln(C)\end{align*}
$$

### Propiedades de Concavidad

Calculamos la primera y segunda derivada de `$u(C)$`:

$$
\begin{align*}u'(C) &= C^{-\sigma} > 0, \quad \forall C > 0 \\ u''(C) &= -\sigma C^{-\sigma-1} < 0, \quad \forall \sigma > 0\end{align*}
$$

La estricta concavidad (`$u''(C) < 0$`) formaliza el principio de que los individuos detestan los saltos bruscos en su nivel de consumo y prefieren combinaciones suaves a lo largo del tiempo.

### Aplicación de CRRA a la Ecuación de Euler

Sustituyendo `$u'(C) = C^{-\sigma}$` en la Ecuación de Euler:

$$
\begin{align*}C_1^{-\sigma} = \beta (1 + r) C_2^{-\sigma}\end{align*}
$$

Reordenando los términos:

$$
\begin{align*}\left( \frac{C_2}{C_1} \right)^\sigma = \beta(1 + r) \implies \frac{C_2}{C_1} = [\beta (1 + r)]^{1/\sigma}\end{align*}
$$

### Elasticidad de Sustitución Intertemporal (EIS)

La **Elasticidad de Sustitución Intertemporal (EIS)** mide la sensibilidad porcentual del crecimiento del consumo ante cambios en el precio relativo intertemporal:

$$
\begin{align*}EIS \equiv -\frac{\partial \ln(C_1 / C_2)}{\partial \ln(1 + r)} = \frac{1}{\sigma}\end{align*}
$$

* **Si `$\sigma < 1 \iff EIS > 1$`:** El individuo está muy dispuesto a posponer consumo si la tasa de interés sube. Domina el efecto sustitución (`$\frac{\partial S_1}{\partial r} > 0$`).
* **Si `$\sigma > 1 \iff EIS < 1$`:** El individuo tiene una fuerte preferencia por la estabilidad del consumo. Domina el efecto ingreso para un ahorrador.
* **Si `$\sigma = 1 \iff EIS = 1$` (Caso Logarítmico):** El efecto sustitución y el efecto ingreso se compensan exactamente cuando la dotación futura es cero, haciendo que la tasa de ahorro sea independiente de `$r$`.

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/equilibrio-light.svg" alt="Recta presupuestaria tangente a una curva de indiferencia en el óptimo, con punto de dotación marcado." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/equilibrio-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: tangencia entre la recta presupuestaria y la indiferencia más alta, con dotación W y óptimo E estrella.</figcaption>
</figure>

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/alza-r-light.svg" alt="Dos rectas presupuestarias que rotan sobre la dotación, con óptimo inicial y nuevo óptimo." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/alza-r-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: un alza de la tasa de interés rota la restricción sobre la dotación, del óptimo E0 al E1.</figcaption>
</figure>

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/jensen-light.svg" alt="Función cóncava con cuerda por debajo y punto medio destacado sobre la curva." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/jensen-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: con utilidad cóncava, el valor en el promedio supera el promedio de los valores.</figcaption>
</figure>
