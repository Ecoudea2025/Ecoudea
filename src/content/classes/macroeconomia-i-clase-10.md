---
title: "Clase 10: Modelo del Ciclo de Vida, Series Geométricas y Etapas Productivas"
course: "macroeconomia-i"
order: 10
classType: "clase"
description: "Deducción algebraica del consumo constante en el modelo del ciclo de vida mediante series geométricas convergentes y partición temporal en edad no productiva, productiva y retiro."
math: true
---


El Modelo del Ciclo de Vida
---------------------------

El principio rector de la **Teoría del Ciclo de Vida** (desarrollada por Franco Modigliani) establece que **el consumo y el ahorro de cada individuo están determinados por la etapa biológica y laboral en la que se encuentra dentro de su ciclo vital**.

A lo largo del tiempo `$t$`, la vida económica de una persona se divide en tres grandes etapas:

1. **Edad no productiva (Juventud / Formación):** El individuo aún no genera ingresos laborales propios, pero requiere consumir.
2. **Edad productiva (Madurez Laboral):** El individuo trabaja, genera ingresos crecientes que superan su consumo, paga deudas previas y acumula activos para el futuro.
3. **Jubilación / Retiro (Vejez):** El individuo se retira del mercado laboral y financia su consumo desahorrando los activos acumulados o recibiendo transferencias pensionales.


Deducción Algebraica del Consumo Constante ($\bar{C}$)
------------------------------------------------------

Supongamos que el consumidor planifica en un horizonte largo (aproximado por `$\infty$`) y desea mantener un **nivel de consumo perfectamente estable** en todos los períodos:

$$
\begin{align*}C_{t+i}^* = \bar{C}, \quad \forall i = 0, 1, 2, \ldots\end{align*}
$$

Partimos de la Restricción Presupuestaria Intertemporal con activos iniciales `$A_t$` e ingresos laborales gravados a una tasa impositiva proporcional `$\tau$`:

$$
\begin{align*}\sum_{i=0}^\infty \frac{C_{t+i}^*}{(1 + r)^i} = (1 + r)A_t + \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}\end{align*}
$$

Sustituyendo `$C_{t+i}^* = \bar{C}$` y extrayendo la constante fuera de la sumatoria:

$$
\begin{align*}\bar{C} \sum_{i=0}^\infty \frac{1}{(1 + r)^i} = (1 + r)A_t + \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}\end{align*}
$$

### Paso a Paso: Resolución de la Serie Geométrica Infinita

Para encontrar el valor exacto de la sumatoria `$\sum_{i=0}^\infty \frac{1}{(1 + r)^i}$`, definimos el factor de descuento como `$\phi$`:

$$
\begin{align*}\phi \equiv \frac{1}{1 + r} < 1 \quad (\text{dado que } r > 0)\end{align*}
$$

1. **Planteamos la suma parcial `$S$` hasta el término `$N$`:**

$$
\begin{align*}S = 1 + \phi + \phi^2 + \phi^3 + \ldots + \phi^{N - 1} + \phi^N \tag{10.1}\end{align*}
$$

2. **Multiplicamos toda la ecuación `(1)` por `$\phi$`:**

$$
\begin{align*}\phi S = \phi + \phi^2 + \phi^3 + \phi^4 + \ldots + \phi^N + \phi^{N + 1} \tag{10.2}\end{align*}
$$

3. **Restamos miembro a miembro `(1)` menos `(2)` (`$S - \phi S$`):**

Observemos que todos los términos intermedios (`$\phi, \phi^2, \phi^3, \ldots, \phi^N$`) se cancelan diagonalmente, sobreviviendo únicamente el primer término de `$S$` y el último término de `$\phi S$`:

$$
\begin{align*}S - \phi S &= 1 - \phi^{N + 1} \\ S(1 - \phi) &= 1 - \phi^{N + 1} \\ S &= \frac{1 - \phi^{N + 1}}{1 - \phi}\end{align*}
$$

4. **Tomamos el límite cuando `$N \to \infty$`:**

Como `$0 < \phi < 1$`, al elevar `$\phi$` a una potencia infinita el término `$\phi^{N + 1}$` converge a cero (`$\lim_{N \to \infty} \phi^{N + 1} = 0$`):

$$
\begin{align*}\lim_{N \to \infty} \frac{1 - \phi^{N + 1}}{1 - \phi} = \frac{1}{1 - \phi}\end{align*}
$$

5. **Sustituimos de vuelta `$\phi = \frac{1}{1 + r}$`:**

$$
\begin{align*}\frac{1}{1 - \frac{1}{1 + r}} = \frac{1}{\frac{1 + r - 1}{1 + r}} = \frac{1}{\frac{r}{1 + r}} = \frac{1 + r}{r}\end{align*}
$$

> **Espacio para gráfica 1:** *Convergencia de la serie geométrica del factor de descuento `$\phi^i$`.*
> En el plano `$(i, \phi^i)$`, se muestra cómo la envolvente exponencial `$\phi^i = \left(\frac{1}{1+r}\right)^i$` parte de `$1$` en `$i=0$` y decae asintóticamente hacia el eje horizontal a medida que `$i \to \infty$`, garantizando que el área acumulada bajo la curva sea finita e igual a `$\frac{1+r}{r}$`.

### Despeje Final del Consumo Permanente ($\bar{C}$)

Reemplazamos el valor de la serie `$\frac{1 + r}{r}$` en nuestra restricción presupuestaria:

$$
\begin{align*}\bar{C} \left( \frac{1 + r}{r} \right) = (1 + r)A_t + \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}\end{align*}
$$

Multiplicando ambos lados por `$\frac{r}{1 + r}$`, obtenemos la **ecuación fundamental del consumo en el Ciclo de Vida**:

$$
\begin{align*}\bar{C} = r A_t + \frac{r}{1 + r} \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}\end{align*}
$$

* **`$r A_t$`:** Es el rendimiento financiero permanente que entrega el stock de riqueza física/financiera inicial (el individuo consume solo los intereses sin comerse el capital base).
* **`$\frac{r}{1 + r} \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}$`:** Es el **valor de anualidad** de su riqueza humana neta de impuestos.


Descomposición por Etapas Vitales
---------------------------------

Podemos particionar la sumatoria infinita de ingresos según las edades específicas de un individuo que vive hasta los `$78$` años:
* **De `$i = 0$` a `$15$` años (Edad no productiva):** El ingreso laboral es nulo (`$Y_{\ell t+i} = 0$`).
* **De `$i = 16$` a `$60$` años (Edad productiva):** El individuo trabaja y percibe ingresos laborales netos de impuestos `$Y_{\ell t+i}(1 - \tau)$`.
* **De `$i = 61$` a `$78$` años (Jubilación / Retiro):** El individuo deja de trabajar y percibe flujos de retiro o pensión `$Y_{t+i}^p$` (o `$0$` si depende exclusivamente de su ahorro privado).

La ecuación de consumo constante se desglosa explícitamente como:

$$
\begin{align*}\bar{C} = r A_t + \frac{r}{1 + r} \left[ \underbrace{\sum_{i=0}^{15} 0}_{\text{Edad no productiva}} + \underbrace{\sum_{i=16}^{60} \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}}_{\text{Edad productiva}} + \underbrace{\sum_{i=61}^{78} \frac{Y_{t+i}^p}{(1 + r)^i}}_{\text{Jubilación / Retiro}} \right]\end{align*}
$$

> **Espacio para gráfica 2:** *Perfil del Ciclo de Vida por etapas de edad (`$0$`, `$15$`, `$60$`, `$78$` años).*
> En el eje horizontal se marca el tiempo `$t$` dividido en tres tramos: **Edad no productiva** (`$0$` a `$15$`), **Edad productiva** (`$15$` a `$60$`) y **Jubilación/retiro** (`$60$` en adelante). Se traza la línea horizontal de consumo estable `$\bar{C}$`:
> 1. Entre `$0$` y `$15$`, el ingreso está sobre el eje horizontal (`$0$`) y el área bajo `$\bar{C}$` (sombreada en verde) representa el consumo en la niñez/juventud financiado por transferencias familiares o deuda.
> 2. Entre `$15$` y `$60$`, la curva de ingreso laboral `$Y_{\ell t}$` salta por encima de `$\bar{C}$` y crece con la experiencia laboral; el área entre `$Y_{\ell t}$` y `$\bar{C}$` (sombreada en rojo) representa el **ahorro acumulado** durante la vida activa.
> 3. A partir de `$60$`, el ingreso laboral cae de nuevo a cero y el consumo `$\bar{C}$` se sostiene gracias a los activos acumulados en la etapa productiva.
