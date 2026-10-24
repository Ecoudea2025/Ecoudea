---
title: "Clase 01: La Restricción Presupuestaria Intertemporal"
course: "macroeconomia-i"
order: 1
classType: "clase"
description: "Deducción paso a paso de la ley de acumulación de activos y la restricción presupuestaria intertemporal en horizonte finito e infinito."
math: true
conceptos: ["Restricción presupuestaria intertemporal", "Ley de movimiento de activos", "Riqueza"]
---

## De la Microeconomía Estática a la Macroeconomía Dinámica

En los cursos de microeconomía tradicional, la decisión del consumidor se analiza comúnmente en un marco **estático**. Se asume que el individuo dispone de un ingreso o riqueza monetaria fija `$M$` en un momento determinado del tiempo y debe decidir cómo distribuirlo entre dos o más bienes:

$$
\begin{align*}P_1 X_1 + P_2 X_2 = M\end{align*}
$$

En ese entorno sin dimensión temporal, no existe la posibilidad de ahorrar ni de pedir prestado: los recursos que no se gastan en el presente simplemente se pierden, y el individuo no puede consumir anticipando ingresos futuros.

Por el contrario, la **macroeconomía moderna** se fundamenta en un marco **dinámico e intertemporal**. Los hogares enfrentan flujos de ingresos laborales que fluctúan a lo largo del tiempo (por ciclos económicos, etapas productivas de la vida o choques inesperados). A través del sistema financiero, los individuos pueden:

1. **Ahorrar en el presente:** Sacrificar consumo hoy para transferir poder adquisitivo hacia el futuro a través de la compra de activos que devengan una tasa de interés.

2. **Endeudarse en el presente:** Consumir por encima de sus ingresos corrientes respaldando dicha deuda con sus ingresos laborales futuros.

El objetivo de esta primera clase es deducir formalmente, paso a paso, la **restricción presupuestaria intertemporal (RPI)** que delimita el conjunto de canastas de consumo factibles a lo largo del horizonte de vida del agente económico.

## Definición de Variables y Flujos de Recursos

Consideremos una economía en tiempo discreto indexedada por los períodos `$t = 0, 1, 2, \ldots, N$`. Todas las variables se expresan en términos reales (canastas de bienes de consumo), eliminando por el momento la distorsión inflacionaria:

* `$C_t$`: Consumo real de los hogares en el período `$t$`.

* `$Y_{\ell t}$`: Ingreso laboral real (*labor income*) recibido por el individuo en el período `$t$`. Representa la retribución al esfuerzo productivo.

* `$A_t$`: Stock de activos financieros netos al **inicio** del período `$t$`. Puede ser positivo (posición acreedora neta: depósitos bancarios, bonos, acciones) o negativo (posición deudora neta).

* `$r$`: Tasa de interés real constante entre períodos.

* `$r A_t$`: Ingresos financieros generados por el stock de activos mantenido al inicio del período.

* `$Y_t$`: Ingreso total del período, compuesto por la suma del ingreso laboral y el ingreso financiero:

$$
\begin{align*}Y_t = Y_{\ell t} + r A_t\end{align*}
$$

* `$S_t$`: Ahorro privado real generado en el período `$t$`.

## Identidades Básicas y Ley de Movimiento de Activos

En cualquier período `$t$`, los ingresos totales de la familia deben distribuirse exactamente entre lo que se consume y lo que se ahorra:

$$
\begin{align*}Y_{\ell t} + r A_t = C_t + S_t\end{align*}
$$

El ahorro `$S_t$` se define conceptualmente como la variación en el stock de activos financieros entre el inicio del período corriente y el inicio del período siguiente:

$$
\begin{align*}S_t \equiv \Delta A_t = A_{t+1} - A_t \implies A_{t+1} = S_t + A_t\end{align*}
$$

### Deducción de la Ley de Movimiento

Despejando el ahorro de la restricción del período corriente:

$$
\begin{align*}S_t = Y_{\ell t} + r A_t - C_t\end{align*}
$$

Sustituyendo esta expresión en la ecuación de acumulación de activos `$A_{t+1} = S_t + A_t$`:

$$
\begin{align*}A_{t+1} &= (Y_{\ell t} + r A_t - C_t) + A_t \\ A_{t+1} &= Y_{\ell t} + (1 + r)A_t - C_t\end{align*}
$$

Esta relación es la **ecuación recursiva de acumulación de activos** (o ley de movimiento de activos). Nos muestra que la riqueza financiera con la que el individuo entra al período `$t+1$` (`$A_{t+1}$`) proviene de dos fuentes:

1. El valor capitalizado de la riqueza previa más sus rendimientos financieros: `$(1 + r)A_t$`.

2. El saldo neto entre su ingreso laboral y su consumo corriente: `$(Y_{\ell t} - C_t)$`.

## Deducción Paso a Paso por Iteración Hacia Adelante

La relación obtenida para `$A_{t+1}$` vincula el período corriente con el período inmediatamente siguiente. Sin embargo, para tomar decisiones óptimas de consumo a lo largo de la vida, el agente debe ligar todos los períodos futuros con el presente. Para lograr esto, aplicamos el método de **iteración hacia adelante**.

### Paso 1: Formulación en los períodos siguientes

Escribimos la ley de movimiento para los períodos `$t+1$` y `$t+2$`:

$$
\begin{align*}A_{t+2} &= Y_{\ell t+1} + (1 + r)A_{t+1} - C_{t+1} \\ A_{t+3} &= Y_{\ell t+2} + (1 + r)A_{t+2} - C_{t+2}\end{align*}
$$

### Paso 2: Despejar los activos futuros en valor presente

De la ecuación para `$A_{t+2}$`, despejamos el término `$A_{t+1}$`:

$$
\begin{align*}A_{t+1} = \frac{A_{t+2} + C_{t+1} - Y_{\ell t+1}}{1 + r}\end{align*}
$$

De manera análoga, despejamos `$A_{t+2}$` de la ecuación para `$A_{t+3}$`:

$$
\begin{align*}A_{t+2} = \frac{A_{t+3} + C_{t+2} - Y_{\ell t+2}}{1 + r}\end{align*}
$$

### Paso 3: Sustitución sucesiva en la ecuación corriente

Tomamos la ley de movimiento original:

$$
\begin{align*}A_{t+1} = Y_{\ell t} + (1 + r)A_t - C_t\end{align*}
$$

Sustituimos la expresión obtenida para `$A_{t+1}$`:

$$
\begin{align*}\frac{A_{t+2} + C_{t+1} - Y_{\ell t+1}}{1 + r} = Y_{\ell t} + (1 + r)A_t - C_t\end{align*}
$$

Aislamos el término que contiene la riqueza inicial `$(1 + r)A_t$`:

$$
\begin{align*}(1 + r)A_t = (C_t - Y_{\ell t}) + \frac{C_{t+1} - Y_{\ell t+1}}{1 + r} + \frac{A_{t+2}}{1 + r}\end{align*}
$$

Ahora sustituimos el término `$\frac{A_{t+2}}{1 + r}$` utilizando la expresión despejada de `$A_{t+2}$`:

$$
\begin{align*}\frac{A_{t+2}}{1 + r} = \frac{\frac{A_{t+3} + C_{t+2} - Y_{\ell t+2}}{1 + r}}{1 + r} = \frac{C_{t+2} - Y_{\ell t+2}}{(1 + r)^2} + \frac{A_{t+3}}{(1 + r)^2}\end{align*}
$$

Reemplazando en la ecuación acumulada:

$$
\begin{align*}(1 + r)A_t = (C_t - Y_{\ell t}) + \frac{C_{t+1} - Y_{\ell t+1}}{1 + r} + \frac{C_{t+2} - Y_{\ell t+2}}{(1 + r)^2} + \frac{A_{t+3}}{(1 + r)^2}\end{align*}
$$

### Paso 4: Generalización para $N$ períodos

Si repetimos este procedimiento algebraico sucesivamente `$N$` períodos hacia adelante, los flujos intermedios de activos se van cancelando telescópicamente, dejando:

$$
\begin{align*}(1 + r)A_t = \sum_{i=0}^N \frac{C_{t+i} - Y_{\ell t+i}}{(1 + r)^i} + \frac{A_{t+N+1}}{(1 + r)^N}\end{align*}
$$

Separando la sumatoria entre consumo e ingreso laboral y reordenando los términos:

$$
\begin{align*}\sum_{i=0}^N \frac{C_{t+i}}{(1 + r)^i} + \frac{A_{t+N+1}}{(1 + r)^N} = (1 + r)A_t + \sum_{i=0}^N \frac{Y_{\ell t+i}}{(1 + r)^i}\end{align*}
$$

## Interpretación Económica y Concepto de Riqueza

La expresión obtenida constituye la **restricción presupuestaria intertemporal en horizonte finito**:

$$
\begin{align*}\underbrace{\sum_{i=0}^N \frac{C_{t+i}}{(1 + r)^i}}_{\text{Valor Presente del Consumo}} + \underbrace{\frac{A_{t+N+1}}{(1 + r)^N}}_{\text{Herencia / Activo Terminal Descontado}} = \underbrace{(1 + r)A_t}_{\text{Riqueza Financiera Inicial}} + \underbrace{\sum_{i=0}^N \frac{Y_{\ell t+i}}{(1 + r)^i}}_{\text{Riqueza Humana (VP Ingresos Laborales)}}\end{align*}
$$

1. **Riqueza Financiera Inicial `$(1 + r)A_t$`:** Es el acervo neto acumulado desde el pasado, listo para generar intereses y financiar consumo presente y futuro.

2. **Riqueza Humana:** Es el valor presente descontado de todos los ingresos laborales que el agente espera recibir a lo largo de su vida activa. Representa el valor de mercado de su capacidad de trabajo.

3. **El término terminal `$\frac{A_{t+N+1}}{(1 + r)^N}$`:** Representa los recursos que quedan al final del horizonte de planificación. En la siguiente clase analizaremos su comportamiento a través de la condición de transversalidad.

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/linea-tiempo-light.svg" alt="Línea de tiempo con nodos de t a t+3, flechas de ingreso y consumo, y transferencia del ahorro capitalizado." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/linea-tiempo-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: en cada período entra el ingreso y sale el consumo; el ahorro viaja capitalizado por el carril (1+r)A y se suma al consumo del último período.</figcaption>
</figure>