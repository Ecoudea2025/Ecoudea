---
title: "Clase 06: Sensibilidad del Consumo a la Tasa de Interés y Restricciones de Liquidez"
course: "macroeconomia-i"
order: 6
classType: "clase"
description: "Derivación analítica general del impacto de la tasa de interés según el parámetro sigma, neutralidad, efectos sustitución e ingreso, y modelación de restricciones de liquidez cuantitativas y por riesgo de impago."
math: true
---


Análisis General de $\frac{\partial C_1^*}{\partial r}$ bajo Preferencias CRRA
------------------------------------------------------------------------------

Partimos de la función de consumo óptimo deducida en la clase anterior:

$$
\begin{align*}C_1^* = \left[ Y_1 + \frac{Y_2}{1 + r} \right] \left( 1 + \frac{(1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}}}{1 + r} \right)^{-1}\end{align*}
$$

Utilizando leyes de exponentes (`$\frac{(1+r)^{1/\sigma}}{1+r} = (1+r)^{\frac{1}{\sigma} - 1}$`), podemos reescribir esta expresión de tres formas equivalentes muy útiles para derivar:

$$
\begin{align*}C_1^* &= \left[ Y_1 + \frac{Y_2}{1 + r} \right] \left( 1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right)^{-1} \\ &= \left[ Y_1 + \frac{Y_2}{1 + r} \right] \left[ \frac{1}{1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}}} \right]\end{align*}
$$

Para aislar con precisión quirúrgica la pugna entre el **efecto sustitución** y el **efecto ingreso** del ahorro frente al **efecto riqueza humana** de los ingresos futuros, dividimos el análisis en dos escenarios: primero cuando `$Y_2 = 0$` y luego cuando `$Y_2 > 0$`.


Escenario 1: Sin Ingreso Futuro ($Y_2 = 0$)
-------------------------------------------

Supongamos que el individuo solo recibe ingresos en el primer período (`$Y_1 > 0, Y_2 = 0$`), por lo que necesariamente es un ahorrador para poder financiar su consumo en `$t=2$`. La función de consumo se simplifica a:

$$
\begin{align*}C_1^* = Y_1 \left[ 1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right]^{-1}\end{align*}
$$

### Derivación Paso a Paso respecto a $r$

Aplicando la regla de la cadena sobre el corchete elevado a la `$-1$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -Y_1 \left[ 1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right]^{-2} \cdot \frac{\partial}{\partial r} \left( (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right)\end{align*}
$$

Calculamos la derivada interna y reordenamos:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -Y_1 \underbrace{\left( \frac{1}{\sigma} - 1 \right)}_{\text{Signo } ?} \underbrace{\left[ 1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right]^{-2} (1 + r)^{\frac{1}{\sigma} - 2} \beta^{\frac{1}{\sigma}}}_{\text{Estrictamente } > 0}\end{align*}
$$

Observemos que `$Y_1 > 0$` y todo el bloque derecho es producto de potencias positivas, por lo cual es estrictamente mayor que cero. En consecuencia, **el signo de `$\frac{\partial C_1^*}{\partial r}$` depende exclusivamente del signo del término `$\left( \frac{1}{\sigma} - 1 \right)$`**, acompañado del signo menos inicial.

Como sabemos que `$\sigma > 0$` y que el ahorro es `$S_1^* = Y_1 - C_1^*$` (por lo que `$\frac{\partial S_1^*}{\partial r} = -\frac{\partial C_1^*}{\partial r}$`), emergen tres casos:

### 1. Caso $\sigma = 1$ (Neutralidad a la Tasa de Interés)

$$
\begin{align*}\sigma = 1 \implies \frac{1}{\sigma} - 1 = 0 \implies \frac{\partial C_1^*}{\partial r} = 0 \implies \frac{\partial S_1^*}{\partial r} = 0\end{align*}
$$

Existe **neutralidad del consumo y del ahorro respecto a la tasa de interés**: el efecto sustitución (que incentiva ahorrar más) y el efecto ingreso (que permite ahorrar menos para lograr la misma meta futura) se cancelan exactamente.

### 2. Caso $0 < \sigma < 1$ (Predominio del Efecto Sustitución)

Si `$0 < \sigma < 1$`, entonces la Elasticidad de Sustitución Intertemporal es alta (`$EIS = \frac{1}{\sigma} > 1$`):

$$
\begin{align*}\left( \frac{1}{\sigma} - 1 \right) > 0 \implies \frac{\partial C_1^*}{\partial r} = (-)\cdot(+)\cdot(+) < 0 \implies \frac{\partial S_1^*}{\partial r} > 0\end{align*}
$$

Cuando `$0 < \sigma < 1$`, **predomina el efecto sustitución sobre el efecto ingreso**: ante un alza en la tasa de interés, el individuo reduce su consumo presente y aumenta su ahorro.

### 3. Caso $\sigma > 1$ (Predominio del Efecto Ingreso)

Si `$\sigma > 1$`, el individuo es altamente averso a las fluctuaciones (`$EIS = \frac{1}{\sigma} < 1$`):

$$
\begin{align*}\left( \frac{1}{\sigma} - 1 \right) < 0 \implies \frac{\partial C_1^*}{\partial r} = (-)\cdot(-)\cdot(+) > 0 \implies \frac{\partial S_1^*}{\partial r} < 0\end{align*}
$$

Cuando `$\sigma > 1$`, **predomina el efecto ingreso sobre el efecto sustitución**: como sus ahorros ahora rinden más intereses en `$t=2$`, el individuo aprovecha esa mayor riqueza para elevar también su consumo en `$t=1$`, ahorrando menos hoy.


Escenario 2: Caso General con Ingresos en Ambos Períodos ($Y_1 \neq 0, Y_2 \neq 0$)
-----------------------------------------------------------------------------------

Definamos la riqueza total descontada como `$W = Y_1 + \frac{Y_2}{1+r}$` y el denominador como `$D = 1 + (1+r)^{\frac{1}{\sigma}-1} \beta^{\frac{1}{\sigma}}$`, de modo que:

$$
\begin{align*}C_1^* = W \cdot D^{-1}\end{align*}
$$

### Derivación mediante Regla del Producto

Derivamos respecto a `$r$` considerando que tanto `$W$` como `$D^{-1}$` dependen de `$r$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = \frac{-Y_2}{(1 + r)^2} D^{-1} - W \left( \frac{1}{\sigma} - 1 \right) D^{-2} (1 + r)^{\frac{1}{\sigma} - 2} \beta^{\frac{1}{\sigma}}\end{align*}
$$

Notemos que podemos reescribir la potencia `$(1+r)^{\frac{1}{\sigma}-2} = \frac{(1+r)^{1/\sigma}}{(1+r)^2}$`. Factorizando el término común `$-\frac{1}{(1+r)^2} D^{-1}$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -\frac{1}{(1 + r)^2} D^{-1} \left\{ Y_2 + W \left( \frac{1}{\sigma} - 1 \right) D^{-1} (1 + r)^{\frac{1}{\sigma}} \beta^{\frac{1}{\sigma}} \right\}\end{align*}
$$

Analizamos nuevamente los tres regímenes del parámetro `$\sigma$`:

1. **Si `$\sigma = 1$`:** El término `$\left(\frac{1}{\sigma} - 1\right)$` se hace cero, anulando la segunda parte dentro de la llave:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = -\frac{Y_2}{(1 + r)^2} D^{-1} < 0 \implies \frac{\partial S_1^*}{\partial r} > 0\end{align*}
$$

2. **Si `$0 < \sigma < 1$`:** Como `$\left(\frac{1}{\sigma} - 1\right) > 0$`, ambos sumandos dentro de la llave son positivos, haciendo que toda la llave sea estrictamente mayor que cero:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} < 0 \implies \frac{\partial S_1^*}{\partial r} > 0\end{align*}
$$

3. **Si `$\sigma > 1$`:** Como `$\left(\frac{1}{\sigma} - 1\right) < 0$`, el segundo término dentro de la llave es negativo y compite contra `$Y_2 > 0$`. Si el segundo término domina en magnitud, entonces `$\frac{\partial C_1^*}{\partial r} > 0$` y `$\frac{\partial S_1^*}{\partial r} < 0$`.


Restricciones de Liquidez e Imperfecciones Crediticias
------------------------------------------------------

Hasta ahora hemos supuesto mercados de capitales perfectos donde cualquier individuo puede prestar o pedir prestado libremente a la misma tasa `$r$`. En la realidad (De Gregorio, Cap. 3), los hogares enfrentan **restricciones de liquidez** bajo dos modalidades principales:

1. **Restricción Cuantitativa:** El individuo sólo puede acceder a un monto de crédito inferior al que desea (o en el caso extremo, cero endeudamiento: `$C_1 \leq Y_1$`).
2. **Restricción vía Precios (Prima por Riesgo de Impago):** El sistema financiero cobra una tasa de interés activa más alta para compensar el riesgo de no pago.

### Modelación Matemática de la Tasa de Interés con Riesgo de Impago

Definamos las siguientes variables del mercado de crédito:
* `$r^*$`: Tasa de interés **libre de riesgo** (por ejemplo, el rendimiento de un bono del Tesoro).
* `$r$`: Tasa de interés efectiva cobrada a un crédito riesgoso otorgado al consumidor.
* `$p \in [0, 1)$`: Probabilidad de **no pago** (*default* o impago) de la deuda por parte del deudor.
* `$(1 - p)$`: Probabilidad de que el deudor cumpla y pague su obligación.

Un intermediario financiero competitivo debe obtener en valor esperado el mismo rendimiento prestando al consumidor riesgoso que invirtiendo en el activo libre de riesgo. Si el deudor no paga (con probabilidad `$p$`), el banco recibe `$0$`; si paga (con probabilidad `$1-p$`), recibe `$r$`:

$$
\begin{align*}r^* = p \cdot 0 + (1 - p) r \implies r = \frac{r^*}{1 - p}\end{align*}
$$

### Análisis Asintótico de la Prima por Riesgo

Evaluemos los casos límite de la ecuación `$r = \frac{r^*}{1 - p}$`:
* **Sin riesgo de impago (`$p \to 0$`):**

$$
\begin{align*}\lim_{p \to 0} \frac{r^*}{1 - p} = r^*\end{align*}
$$

El deudor enfrenta la tasa libre de riesgo y alcanza su óptimo sin distorsiones (*First Best*).

* **Certeza de impago (`$p \to 1$`):**

$$
\begin{align*}\lim_{p \to 1^-} \frac{r^*}{1 - p} = \infty\end{align*}
$$

A medida que la probabilidad de impago se acerca a `$1$`, la tasa de interés exigida tiende a infinito. Si en la economía existe una tasa máxima legal o de mercado `$\bar{r}$`, todo individuo cuya probabilidad de impago supere el umbral crítico queda racionado cuantitativamente fuera del mercado crediticio.

> **Espacio para gráfica 2:** *Tasa de interés efectiva `$r$` en función de la probabilidad de no pago `$p$`.*
> En el plano `$(p, r)$` con `$p \in [0, 1]$`, la curva `$r = \frac{r^*}{1-p}$` nace en el intercepto vertical `$r^*$` cuando `$p=0$` y crece de forma estrictamente convexa y asintótica hacia una recta vertical en `$p=1$`. Se traza una cota horizontal `$\bar{r}$` y se sombrea en azul la región superior donde `$\frac{r^*}{1-p} > \bar{r}$` (exclusión crediticia).

### Impacto Gráfico sobre el Bienestar del Consumidor

1. **Bajo Restricción Cuantitativa:** Si el consumidor es un deudor potencial (su óptimo sin restricciones cumple `$C_1^* > Y_1$` sobre la curva de indiferencia `$I_1$`), una prohibición o tope al endeudamiento trunca la recta presupuestaria quebrándola verticalmente en `$C_1 = Y_1$` (o con un segmento quebrado muy corto). El agente se ve obligado a ubicarse en la solución de esquina `$(Y_1, Y_2)$` sobre una curva de indiferencia inferior `$I_2$` o `$I_3$` (`$I_1 > I_2 > I_3$`), sufriendo una **pérdida irrecuperable de bienestar**.

2. **Bajo Restricción de Precio (Prima de Riesgo):** Para niveles de consumo `$C_1 < Y_1$` (cuando ahorra), el individuo enfrenta la pendiente suave `$-(1 + r^*)$`. Pero a la derecha del punto de dotación `$(Y_1, Y_2)$` (cuando pide prestado, `$C_1 > Y_1$`), enfrenta una tasa mayor `$r = \frac{r^*}{1-p} > r^*$`, haciendo que la recta presupuestaria rote en sentido horario y se vuelva más empinada. El nuevo punto de tangencia (*Second Best*) implica menor consumo presente (`$C_1^{**} < C_1^*$`) y menor utilidad que el *First Best*.

> **Espacio para gráfica 3:** *Restricción cuantitativa de liquidez y solución de esquina en el plano `$(C_1, C_2)$`.*
> Recta presupuestaria quebrada verticalmente en `$Y_1$` (trazo verde), mostrando cómo el consumidor no puede alcanzar la tangencia óptima `$C_1^*$` en `$I_1$` y queda atrapado en la dotación `$(Y_1, Y_2)$` sobre una curva de indiferencia inferior.

> **Espacio para gráfica 4:** *Restricción vía precios (diferencial de tasas por riesgo de impago).*
> En el plano `$(C_1, C_2)$`, recta presupuestaria azul con pendiente `$-(1+r^*)$` (*First Best*) y recta verde quebrada en `$(Y_1, Y_2)$` con pendiente más empinada `$-(1+r)$` para `$C_1 > Y_1$`, ilustrando la contracción del consumo presente y el paso a una curva de indiferencia más baja (*Second Best*).
