---
title: "Clase 07: Teoría del Ingreso Permanente y Teoría del Ciclo de Vida"
course: "macroeconomia-i"
order: 7
classType: "clase"
description: "Deducción formal de la hipótesis del ingreso permanente de Friedman y del ciclo de vida de Modigliani, respuesta del consumo y ahorro ante choques transitorios frente a permanentes."
math: true
---


Fundamentos de las Teorías Modernas del Consumo
-----------------------------------------------

En el Capítulo 3 de De Gregorio se estudian las dos piedras angulares que superaron las limitaciones de la función de consumo keynesiana estática (`$C_t = \bar{C} + cY_t$`):

1. **La Teoría del Ciclo de Vida (Franco Modigliani):** Enfatiza que el ingreso laboral varía sistemáticamente a lo largo de las etapas biológicas de las personas (juventud, etapa productiva adulta y vejez/jubilación), por lo que los individuos utilizan el ahorro y el endeudamiento para mantener un consumo estable a lo largo de su vida.
2. **La Hipótesis del Ingreso Permanente (Milton Friedman):** Enfatiza que el ingreso sufre fluctuaciones aleatorias, y que la respuesta del consumidor depende crucialmente de si percibe que un cambio en su ingreso es **transitorio** o **permanente**.

Ambas teorías comparten el mismo corazón microfundamentado: la restricción presupuestaria intertemporal y el deseo de suavizar el consumo.


El Modelo Base de Suavización Perfecta
--------------------------------------

Para deducir con total transparencia algebraica cómo reacciona el consumo ante distintos tipos de choques, partimos de los siguientes supuestos simplificadores:

1. Tasa de interés real nula e impuestos nulos: `$r = 0$` y `$T_t = 0$`.
2. Deseo de suavización perfecta del consumo a lo largo de los `$N$` períodos de vida:

$$
\begin{align*}C_t = \bar{C}, \quad \forall t\end{align*}
$$

### Deducción de la Regla de Consumo Promedio

Partimos de la Restricción Presupuestaria Intertemporal para un horizonte de `$N$` períodos:

$$
\begin{align*}\sum_{i=0}^N \frac{C_{t+i}}{(1 + r)^i} = \sum_{i=0}^N \frac{Y_{\ell t+i}}{(1 + r)^i}\end{align*}
$$

Imponiendo `$r = 0$` (con lo cual `$(1+r)^i = 1$`) y `$C_{t+i} = \bar{C}$`:

$$
\begin{align*}\sum_{i=0}^N \bar{C} = \sum_{i=0}^N Y_{\ell t+i}\end{align*}
$$

Contabilizando `$N$` períodos de planificación, la suma de una constante `$\bar{C}$` es `$N \bar{C}$`:

$$
\begin{align*}N \bar{C} = \sum_{i=0}^N Y_{\ell t+i} \implies \bar{C} = \frac{1}{N} \sum_{i=0}^N Y_{\ell t+i}\end{align*}
$$

### Incorporación de Expectativas Racionales

Dado que el futuro no se conoce con certeza absoluta en el período `$t$`, introducimos el **operador de expectativas matemáticas condicionales `$E_t\{\cdot\}$`**, el cual procesa toda la información disponible en el instante `$t$`:

$$
\begin{align*}\bar{C} = \frac{1}{N} E_t \left\{ \sum_{i=0}^N Y_{\ell t+i} \right\}\end{align*}
$$

Esta ecuación nos dice que el consumo corriente es igual al **ingreso permanente**, entendido como el flujo promedio esperado de ingresos a lo largo de toda la vida del individuo.


Respuesta ante un Choque Transitorio vs. Permanente
---------------------------------------------------

Utilizando nuestra ecuación fundamental, comparemos rigurosamente qué sucede con el consumo (`$\bar{C}$`) y con el ahorro corriente (`$S = Y - C$`) bajo dos escenarios opuestos.

### Caso 1: Cambio Transitorio en el Ingreso

Supongamos que en el período corriente el individuo experimenta un aumento extraordinario de tamaño `$\Delta Y_t$` (por ejemplo, una bonificación única o una cosecha excepcional), pero espera que en todos los demás períodos su ingreso siga exactamente igual.

1. **Nuevo nivel de consumo (`$\bar{C}_1$`):**

$$
\begin{align*}\bar{C}_1 = \frac{1}{N} \left\{ \sum_{i=0}^N Y_{\ell t+i} + \Delta Y_t \right\}\end{align*}
$$

2. **Variación en el consumo (`$\Delta \bar{C} = \bar{C}_1 - \bar{C}$`):**

$$
\begin{align*}\Delta \bar{C} &= \frac{1}{N} \left\{ \sum_{i=0}^N Y_{\ell t+i} + \Delta Y_t \right\} - \frac{1}{N} \left\{ \sum_{i=0}^N Y_{\ell t+i} \right\} \\ \Delta \bar{C} &= \frac{1}{N} \Delta Y_t \quad \left( \text{o bajo incertidumbre: } \Delta \bar{C} = \frac{1}{N} E_t\{\Delta Y_t\} \right)\end{align*}
$$

De aquí se deduce que la **Propensión Marginal a Consumir un ingreso transitorio (`$PMgC_{Y_T}$`)** es pequeña y decrece con el horizonte de vida `$N$`:

$$
\begin{align*}PMgC_{Y_T} = \frac{\Delta \bar{C}}{\Delta Y_t} = \frac{1}{N} < 1\end{align*}
$$

3. **Variación en el ahorro corriente (`$\Delta S$`):**

Partiendo de la identidad `$S = Y - C$`, tomamos diferencias:

$$
\begin{align*}\Delta S &= \Delta Y - \Delta \bar{C} = \Delta Y - \frac{1}{N} \Delta Y \\ \Delta S &= \Delta Y \left( 1 - \frac{1}{N} \right) = \Delta Y \left( \frac{N - 1}{N} \right) > 0\end{align*}
$$

> **Intuición económica:** Si el aumento del ingreso es **transitorio**, el individuo **no se gasta todo el ingreso adicional de una sola vez**. Solo consume una fracción `$\frac{1}{N}$` hoy y **ahorra la gran mayoría (`$\frac{N-1}{N} \Delta Y$`)** para repartir ese bienestar uniformemente en los `$N-1$` períodos restantes de su vida.

### Caso 2: Cambio Permanente en el Ingreso

Supongamos ahora que el incremento `$\Delta Y$` es **permanente**, es decir, el ingreso sube en la magnitud `$\Delta Y$` hoy y en todos los períodos futuros (por ejemplo, un ascenso estructural de carrera o una mejora tecnológica permanente).

1. **Nuevo nivel de consumo (`$\bar{C}_2$`):**

$$
\begin{align*}\bar{C}_2 = \frac{1}{N} \left\{ \sum_{i=0}^N Y_{\ell t+i} + \sum_{i=0}^N \Delta Y_{\ell t+i} \right\}\end{align*}
$$

2. **Variación en el consumo (`$\Delta \bar{C} = \bar{C}_2 - \bar{C}$`):**

$$
\begin{align*}\Delta \bar{C} = \frac{1}{N} \sum_{i=0}^N \Delta Y_{\ell t+i} = \frac{N \Delta Y}{N} = \Delta Y\end{align*}
$$

Por lo tanto, la **Propensión Marginal a Consumir un ingreso permanente (`$PMgC_{Y_P}$`)** es unitaria:

$$
\begin{align*}PMgC_{Y_P} = \frac{\Delta \bar{C}}{\Delta Y} = 1\end{align*}
$$

3. **Variación en el ahorro corriente (`$\Delta S$`):**

$$
\begin{align*}\Delta S = \Delta Y - \Delta \bar{C} = \Delta Y - \Delta Y = 0\end{align*}
$$

> **Conclusión fundamental de Friedman:**
> $$PMgC_{Y_P} > PMgC_{Y_T} \quad \left( 1 > \frac{1}{N} \right)$$
> Los choques permanentes se traducen íntegramente en mayor consumo sin alterar el ahorro, mientras que los choques transitorios se destinan primordialmente al ahorro.


Generalización con Tasa de Interés Positiva ($r > 0$)
-----------------------------------------------------

Cuando la tasa de interés es positiva (`$r > 0$`) y el individuo vive `$N$` períodos con preferencias tipo Cobb-Douglas generalizadas, la función de consumo óptimo en el período 1 toma la forma:

$$
\begin{align*}C_1^* = \alpha_1 \left\{ Y_1 + \frac{Y_2}{1 + r} + \frac{Y_3}{(1 + r)^2} + \ldots + \frac{Y_N}{(1 + r)^{N - 1}} \right\}\end{align*}
$$

### 1. Comparación de Choques Transitorios en Distintas Fechas Futuras

Comparemos el impacto sobre el consumo hoy (`$C_1^*$`) de un aumento anunciado en el ingreso del período 3 frente a un aumento idéntico en el período 6:

$$
\begin{align*}\frac{\partial C_1^*}{\partial Y_3} = \frac{\alpha_1}{(1 + r)^2} \qquad \text{vs.} \qquad \frac{\partial C_1^*}{\partial Y_6} = \frac{\alpha_1}{(1 + r)^5}\end{align*}
$$

Dado que `$r > 0$`, se cumple que `$(1 + r)^2 < (1 + r)^5$`, por lo cual:

$$
\begin{align*}\frac{\partial C_1^*}{\partial Y_3} > \frac{\partial C_1^*}{\partial Y_6} > 0\end{align*}
$$

Cuanto más lejano en el futuro ocurra un choque de ingreso transitorio, mayor es su descuento financiero y menor es su impacto sobre la riqueza presente y el consumo actual.

### 2. Choque Permanente con Descuento Financiero

Si todos los ingresos presentes y futuros aumentan simultáneamente en una cuantía constante `$\Delta Y_i = \Delta \bar{Y}$`, el diferencial total sobre `$C_1^*$` es:

$$
\begin{align*}\Delta C_1^* = \sum_{i=1}^N \frac{\partial C_1^*}{\partial Y_i} \Delta \bar{Y} = \alpha_1 \Delta \bar{Y} \left[ 1 + \frac{1}{1 + r} + \frac{1}{(1 + r)^2} + \ldots + \frac{1}{(1 + r)^{N - 1}} \right]\end{align*}
$$


Conexión con la Teoría del Ciclo de Vida
----------------------------------------

En el esquema del Ciclo de Vida de Modigliani (De Gregorio, Sección 3.4), la trayectoria laboral de una persona atraviesa tres fases:

1. **Etapa I (Juventud / Formación):** El ingreso laboral es bajo e inferior al consumo constante deseado (`$Y_{\ell t} < \bar{C}$`). El joven se **endeuda** (desahorra, acumulando pasivos netos) para financiar su educación y consumo inicial.
2. **Etapa II (Madurez Productiva):** El ingreso laboral alcanza su máximo y supera al consumo (`$Y_{\ell t} > \bar{C}$`). El individuo **ahorra**: primero paga las deudas contraídas en su juventud y luego acumula un stock positivo de activos financieros (`$A_t > 0$`).
3. **Etapa III (Jubilación / Vejez):** El ingreso laboral cae a cero. El individuo **desahorra** consumiendo el capital y los intereses acumulados durante su vida activa hasta agotar sus activos al final de su horizonte vital (`$A_{N+1} = 0$`).

| Concepto | Choque Transitorio ($\Delta Y_T > 0$) | Choque Permanente ($\Delta Y_P > 0$) |
| :--- | :--- | :--- |
| **Impacto en Consumo ($\Delta C$)** | Pequeño (`$\frac{1}{N} \Delta Y$`) | Total (`$\Delta Y$`) |
| **Propensión Marginal ($PMgC$)** | `$\frac{1}{N} \ll 1$` | `$1$` |
| **Impacto en Ahorro ($\Delta S$)** | Aumenta fuertemente (`$\frac{N-1}{N} \Delta Y > 0$`) | No se altera (`$\Delta S = 0$`) |

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/ciclo-vida-light.svg" alt="Ingreso acampanado, consumo constante y activos netos con etapas de deuda, ahorro y desahorro." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/ciclo-vida-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: en la juventud se gasta más de lo que se gana, en la madurez se ahorra y en la vejez se vive de lo acumulado.</figcaption>
</figure>
