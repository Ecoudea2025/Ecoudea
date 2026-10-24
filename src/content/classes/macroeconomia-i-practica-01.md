---
title: "Práctica 01: Consumo Intertemporal, Inversión y Política Fiscal"
course: "macroeconomia-i"
order: 17
classType: "practica"
description: "Ejercicios sobre: - Restricción Presupuestaria Intertemporal y Condición de Transversalidad - Optimización con Preferencias Cobb-Douglas, CES y CRRA - Impuestos Distorsionantes y Estática Comparativa - Teoría del Ingreso Permanente, Ciclo de Vida e Incertidumbre - Restricciones de Liquidez y Riesgo de Impago - Teoría de la Inversión, Costo de Uso, Costos de Ajuste y q de Tobin - Política Fiscal, Inflación y Sostenibilidad de la Deuda Pública"
math: true
---

## Lista de ejercicios

1.  Suponga un consumidor que vive dos períodos (`$t = 1, 2$`) y cuyas
    preferencias están representadas por una función de utilidad con
    Elasticidad de Sustitución Constante (CES) de la forma:

    $$
    \begin{align*}U(C_1, C_2) = \bar{C} \left[ \alpha C_1^{1/\rho} + (1 - \alpha) C_2^{1/\rho} \right]^\rho, \quad \text{con } 0 < \alpha < 1, \; \rho > 1\end{align*}
    $$

    sujeta a la restricción presupuestaria intertemporal con impuestos de
    suma alzada `$T_1$` y `$T_2$`:

    $$
    \begin{align*}C_1 + \frac{C_2}{1 + r} = Y_1 - T_1 + \frac{Y_2 - T_2}{1 + r}\end{align*}
    $$

    <ol type="a">
    <li>
    Explique el significado económico de cada uno de los tres parámetros
    de la función de utilidad ($\bar{C}$, $\alpha$ y $\rho$).
    </li>
    <li>
    Explique por qué en esta formulación no aparece explícitamente el
    parámetro del factor subjetivo de descuento $\beta = \frac{1}{1+\delta}$
    y cuál de los parámetros de la función recoge implícitamente la
    impaciencia del individuo (y bajo qué condición matemática el agente
    prefiere el consumo presente sobre el futuro).
    </li>
    <li>
    Plantee el Lagrangiano, encuentre las condiciones de primer orden y
    deduzca paso a paso las demandas óptimas de consumo $C_1^*$ y $C_2^*$.
    </li>
    <li>
    Explique detalladamente por qué la función de consumo encontrada
    ofrece una teoría superior a la función de consumo keynesiana
    tradicional ($C_t = \bar{C} + cY_t$).
    </li>
    </ol>

2.  Ahora suponga una economía de tres períodos (`$t = 1, 2, 3$`) donde las
    preferencias del hogar son de tipo Cobb-Douglas:

    $$
    \begin{align*}U(C_1, C_2, C_3) = \bar{C} C_1^\alpha C_2^\eta C_3^{1 - \alpha - \eta}, \quad \text{con } \alpha > \eta > 1 - \alpha - \eta > 0\end{align*}
    $$

    y la restricción presupuestaria intertemporal incorpora impuestos
    distorsionantes sobre el consumo (`$\tau_c$`) y sobre el ingreso
    laboral (`$\tau_y$`):

    $$
    \begin{align*}(1 + \tau_c)C_1 + \frac{(1 + \tau_c)C_2}{1 + r} + \frac{(1 + \tau_c)C_3}{(1 + r)^2} = (1 - \tau_y)Y_1 + \frac{(1 - \tau_y)Y_2}{1 + r} + \frac{(1 - \tau_y)Y_3}{(1 + r)^2}\end{align*}
    $$

    <ol type="a">
    <li>
    Plantee el Lagrangiano y demuestre paso a paso que la demanda óptima
    de consumo en el primer período viene dada por:
    $$C_1^* = \frac{\alpha}{1 + \tau_c} \left[ Y_1(1 - \tau_y) + \frac{Y_2(1 - \tau_y)}{1 + r} + \frac{Y_3(1 - \tau_y)}{(1 + r)^2} \right]$$
    </li>
    <li>
    Indique y justifique formalmente si la ecuación de presupuesto
    intertemporal de este problema cumple con la condición de
    transversalidad (y qué supuestos sobre $A_1$ y $A_4$ están implícitos).
    </li>
    <li>
    Calcule analíticamente las derivadas parciales $\frac{\partial C_1^*}{\partial r}$,
    $\frac{\partial C_1^*}{\partial \tau_c}$ y $\frac{\partial C_1^*}{\partial \tau_y}$,
    verifique sus signos e interprete las distorsiones fiscales y el
    balance entre efecto sustitución y efecto riqueza.
    </li>
    </ol>

3.  A partir de la función de consumo óptimo `$C_1^*$` obtenida en el
    Ejercicio 2, analice la respuesta del consumidor frente a distintos
    choques en su sendero de ingresos:
    <ol type="a">
    <li>
    Determine la propensión marginal a consumir hoy ante un choque
    transitorio concentrado en el primer período ($\Delta Y_1 &gt; 0$, con
    $\Delta Y_2 = \Delta Y_3 = 0$) y compárela con un choque transitorio
    anunciado para el tercer período ($\Delta Y_3 &gt; 0$). ¿Qué ocurre con
    el ahorro corriente $S_1^*$ en cada uno de los dos casos?
    </li>
    <li>
    Utilizando el diferencial total, calcule la propensión marginal a
    consumir ante una variación permanente del ingreso en todos los
    períodos ($\Delta Y_1 = \Delta Y_2 = \Delta Y_3 = \Delta \bar{Y}$).
    Demuestre matemáticamente por qué $PMC_{\text{permanente}} &gt; PMC_{\text{transitorio}}$.
    </li>
    <li>
    <b>Entorno de incertidumbre:</b> Suponga que el individuo asigna una
    probabilidad subjetiva $p \in (0, 1)$ a que un aumento del ingreso hoy
    sea exclusivamente transitorio, y una probabilidad $(1 - p)$ a que se
    trate de una mejora permanente. Formule el valor esperado
    $\mathbb{E}[PMC]$ y analice cómo responde el consumo y el ahorro ante
    variaciones en el grado de incertidumbre $p$.
    </li>
    </ol>

4.  Considere un consumidor con preferencias aditivas separables y
    función de utilidad instantánea de Aversión Relativa al Riesgo
    Constante (CRRA):

    $$
    \begin{align*}u(C_t) = \frac{C_t^{1 - \sigma} - 1}{1 - \sigma}, \quad \sigma > 0\end{align*}
    $$

    <ol type="a">
    <li>
    Explique mediante la <b>Desigualdad de Jensen</b> por qué la
    concavidad estricta de $u(C_t)$ implica aversión a las fluctuaciones
    bruscas del consumo y demuestre paso a paso (usando la Regla de
    L'Hôpital) que cuando $\sigma \to 1$ se obtiene $u(C_t) = \ln(C_t)$.
    </li>
    <li>
    A partir de la demanda óptima en dos períodos:
    $$C_1^* = \left[ Y_1 + \frac{Y_2}{1 + r} \right] \left( 1 + (1 + r)^{\frac{1}{\sigma} - 1} \beta^{\frac{1}{\sigma}} \right)^{-1}$$
    asuma inicialmente que $Y_2 = 0$ y demuestre analíticamente cómo el
    signo de $\frac{\partial C_1^*}{\partial r}$ y de $\frac{\partial S_1^*}{\partial r}$
    depende de los tres regímenes del parámetro $\sigma$ ($\sigma = 1$,
    $0 &lt; \sigma &lt; 1$ y $\sigma &gt; 1$).
    </li>
    <li>
    Explique cómo se modifica su resultado anterior cuando $Y_2 &gt; 0$,
    particularmente en el caso logarítmico ($\sigma = 1$).
    </li>
    </ol>

5.  En presencia de imperfecciones en el mercado de capitales, los
    hogares enfrentan restricciones de liquidez cuantitativas o vía
    precios por riesgo de impago:
    <ol type="a">
    <li>
    Si la tasa de interés libre de riesgo es $r^*$ y existe una
    probabilidad $p \in [0, 1)$ de que el deudor incumpla el pago de su
    deuda (recibiendo el banco $0$ en caso de impago), deduzca la tasa de
    interés efectiva $r$ que cobra un intermediario financiero competitivo
    y analice sus límites cuando $p \to 0$ y $p \to 1$.
    </li>
    <li>
    Explique y contraste gráficamente en el plano $(C_1, C_2)$ la pérdida
    de bienestar que sufre un consumidor deudor cuando enfrenta una
    <b>restricción cuantitativa total</b> ($C_1 \leq Y_1$) frente a cuando
    enfrenta una <b>prima por riesgo de impago</b> ($r &gt; r^*$ para $C_1 &gt; Y_1$),
    distinguiendo entre las asignaciones <i>First Best</i>, <i>Second Best</i>
    y solución de esquina.
    </li>
    </ol>

6.  Considere un individuo que planifica su consumo bajo la **Teoría del
    Ciclo de Vida** en un horizonte infinito con tasa de interés real
    constante `$r > 0$`, activos iniciales `$A_t$` e ingresos laborales
    gravados a una tasa proporcional `$\tau$`:
    <ol type="a">
    <li>
    Si el agente desea mantener un flujo de consumo constante $C_{t+i}^* = \bar{C}$,
    demuestre paso a paso utilizando las propiedades de las series
    geométricas ($\phi \equiv \frac{1}{1+r} &lt; 1$) que el nivel óptimo de
    consumo permanente viene dado por:
    $$\bar{C} = r A_t + \frac{r}{1 + r} \sum_{i=0}^\infty \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i}$$
    </li>
    <li>
    Particione la expresión anterior en las tres etapas vitales (edad no
    productiva de $0$ a $15$ años, edad productiva de $16$ a $60$ años, y
    retiro de $61$ a $78$ años) e interprete el comportamiento del ahorro
    en cada etapa.
    </li>
    </ol>

7.  Considere el modelo neoclásico de inversión donde una firma
    competitiva opera con tecnología Cobb-Douglas `$Y_t = A_t K_t^\alpha N_t^{1-\alpha}$`
    y enfrenta costos cuadráticos de ajuste del capital:
    <ol type="a">
    <li>
    Enuncie las cuatro propiedades matemáticas de la función de
    producción neoclásica y deduzca el stock de capital deseado $K_t^*$ a
    partir de la maximización de beneficios $\Pi_t = P_t Y_t - W_t N_t - R_t K_t$.
    </li>
    <li>
    Deduzca la expresión del costo de uso del capital
    $$R_t = P_K \left[ r + \delta - \left( \frac{\Delta P_K}{P_K} - \pi \right) \right]$$
    y explique qué implica una alta tasa de inflación general $\pi$ (y la
    falta de indexación tributaria de la depreciación) para la
    acumulación de capital.
    </li>
    <li>
    Minimizando la función de costos de ajuste $C(I_t) = \epsilon(K_{t+1} - K^*)^2 + (1 - \epsilon)(K_{t+1} - K_t)^2$,
    deduzca la ecuación de inversión neta:
    $$I_t = \epsilon \left[ \left( \frac{P_t \alpha A_t}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} N_t - K_t \right]$$
    Explique el significado económico de $\epsilon \in (0, 1)$, por qué es
    costoso operar fuera de $K^*$, y calcule e interprete el signo de
    $\frac{\partial I_t}{\partial r}$, $\frac{\partial I_t}{\partial A_t}$ y $\frac{\partial I_t}{\partial K_t}$.
    </li>
    </ol>

8.  Suponga que una firma competitiva maximiza el valor presente de sus
    flujos de beneficios intertemporales sujeta a la ley de acumulación
    `$K_{t+1} = (1 - \delta)K_t + I_t$` y a una función de costos de
    ajuste del capital de la forma:

    $$
    \begin{align*}C(I_t) = \bar{C} + \psi (K_{t+1} - K_t)^2, \quad \psi > 0\end{align*}
    $$

    *(o en su formulación general convexa `$C(I_t)$`)*:
    <ol type="a">
    <li>
    Explique económicamente esta función de costos de ajuste y resuelva
    el problema de optimización intertemporal de la firma para encontrar
    la condición de primer orden respecto a $K_{t+1}$.
    </li>
    <li>
    Defina la $q$ marginal de Tobin ($q_t \equiv 1 + C'(I_t)$) y explique
    las siguientes dos expresiones fundamentales:
    $$q_t = \frac{f'(K_{t+1}) - \delta + q_{t+1}}{1 + r} \qquad \text{y} \qquad r = \frac{f'(K_{t+1}) - \delta}{q_t} + \frac{\Delta q_{t+1}}{q_t}$$
    </li>
    <li>
    Itere hacia adelante la ecuación de $q_t$, enuncie la condición de
    transversalidad (ausencia de burbujas especulativas) y formule el
    valor esperado $\mathbb{E}_t[q_t]$ cuando la productividad futura
    puede tomar dos estados discretos: un escenario favorable $\bar{A}$
    con probabilidad $\theta$ y un escenario adverso $\underline{A}$ con
    probabilidad $(1 - \theta)$.
    </li>
    </ol>

9.  Considere la restricción presupuestaria del gobierno y la dinámica de
    la deuda pública:
    <ol type="a">
    <li>
    Partiendo de la identidad del déficit total $\Delta B_{t+1} = B_{t+1} - B_t = G_t - T_t + r B_t$,
    itere hacia adelante para deducir la Restricción Presupuestaria
    Intertemporal del Gobierno:
    $$(1 + r)B_t = \sum_{s=0}^\infty \frac{T_{t+s} - G_{t+s}}{(1 + r)^s}$$
    Explique su significado económico y argumente analíticamente por qué
    es indispensable la condición de no-juego Ponzi.
    </li>
    <li>
    Demuestre cómo se transforma la ley de evolución de la deuda al
    expresarla primero en términos reales con inflación $\pi$, y luego
    como proporción del PIB real ($b_t = B_t / Y_t$) cuando la economía
    crece a la tasa $\gamma_y$:
    $$b_{t+1} = \frac{g_t - t_t}{1 + \gamma_y} + \left( \frac{1 + r}{1 + \gamma_y} \right) b_t \iff b_{t+1} - b_t = \frac{g_t - t_t}{1 + \gamma_y} + \left( \frac{r - \gamma_y}{1 + \gamma_y} \right) b_t$$
    </li>
    <li>
    Definiendo $\varphi \equiv \frac{g_t - t_t}{1 + \gamma_y}$ y $\rho \equiv \frac{1 + r}{1 + \gamma_y}$,
    itere la ecuación $N$ períodos hacia adelante ($b_{t+N} = \sum_{i=1}^N \varphi \rho^{i-1} + \rho^N b_t$),
    distinga el comportamiento de la deuda cuando $r &gt; \gamma_y$ frente a
    cuando $r &lt; \gamma_y$, y deduzca el nivel de deuda de estado
    estacionario $\bar{b} = \frac{g_t - t_t}{\gamma_y - r}$.
    </li>
    <li>
    Demuestre matemáticamente que si la deuda pública como proporción del
    PIB es sostenible, también se cumple la restricción de presupuesto
    intertemporal del gobierno.
    </li>
    </ol>


## Solucionario y Guía Analítica Paso a Paso

### Solución Ejercicio 1: Utilidad CES en Dos Períodos

* **a) Significado de los parámetros:**
  * `$\bar{C} > 0$`: Parámetro de escala positiva (transformación monótona que no altera las decisiones óptimas).
  * `$\alpha \in (0, 1)$` y `$(1 - \alpha)$`: Ponderadores distributivos que miden el peso subjetivo que el consumidor asigna al consumo presente (`$C_1$`) y al consumo futuro (`$C_2$`).
  * `$\rho$`: Parámetro de curvatura que determina la **Elasticidad de Sustitución Intertemporal (`$EIS$`)**. En esta parametrización con exponente interno `$1/\rho$`, la elasticidad de sustitución es `$EIS = \frac{1}{1 - 1/\rho} = \frac{\rho}{\rho - 1}$`.

* **b) Ausencia de $\beta$ explícito e impaciencia implícita:**
  * No aparece `$\beta$` multiplicando un segundo sumando separado porque la función no está escrita en forma aditiva separable (`$u(C_1) + \beta u(C_2)$`), sino como un agregado CES ponderado por `$\alpha$` y `$(1 - \alpha)$`.
  * El parámetro que recoge el descuento subjetivo es **`$\alpha$`** en relación con **`$(1 - \alpha)$`**: la razón `$\frac{1 - \alpha}{\alpha}$` cumple exactamente el rol del factor subjetivo de descuento `$\beta$`. Para que el individuo sea impaciente y prefiera el presente sobre el futuro, debe cumplirse que **`$\alpha > 1 - \alpha \iff \alpha > 0.5$`**.

* **c) Derivación paso a paso de $C_1^*$ y $C_2^*$:**
  Definamos la riqueza neta de impuestos como `$W \equiv Y_1 - T_1 + \frac{Y_2 - T_2}{1 + r}$` y `$B \equiv \alpha C_1^{1/\rho} + (1 - \alpha)C_2^{1/\rho}$`. Planteamos el Lagrangiano:

  $$
  \begin{align*}\mathcal{L} = \bar{C} B^\rho + \lambda \left[ W - C_1 - \frac{C_2}{1 + r} \right]\end{align*}
  $$

  Condiciones de primer orden (notando que `$\rho \cdot \frac{1}{\rho} = 1$`):

  $$
  \begin{align*}\frac{\partial \mathcal{L}}{\partial C_1} &= \bar{C} B^{\rho - 1} \alpha C_1^{\frac{1}{\rho} - 1} - \lambda = 0 \implies \lambda = \bar{C} B^{\rho - 1} \alpha C_1^{\frac{1 - \rho}{\rho}} \tag{17.1} \\ \frac{\partial \mathcal{L}}{\partial C_2} &= \bar{C} B^{\rho - 1} (1 - \alpha) C_2^{\frac{1}{\rho} - 1} - \frac{\lambda}{1 + r} = 0 \implies \lambda = (1 + r) \bar{C} B^{\rho - 1} (1 - \alpha) C_2^{\frac{1 - \rho}{\rho}} \tag{17.2}\end{align*}
  $$

  Igualando `(1)` y `(2)` y cancelando `$\bar{C} B^{\rho - 1}$`:

  $$
  \begin{align*}\alpha C_1^{\frac{1 - \rho}{\rho}} = (1 - \alpha)(1 + r) C_2^{\frac{1 - \rho}{\rho}} \implies \left( \frac{C_2}{C_1} \right)^{\frac{\rho - 1}{\rho}} = \frac{(1 - \alpha)(1 + r)}{\alpha}\end{align*}
  $$

  Elevando a la potencia `$\frac{\rho}{\rho - 1}$`, despejamos `$C_2$`:

  $$
  \begin{align*}C_2 = \left[ \frac{(1 - \alpha)(1 + r)}{\alpha} \right]^{\frac{\rho}{\rho - 1}} C_1\end{align*}
  $$

  Sustituyendo `$C_2$` en la R.P.I. `$C_1 + \frac{C_2}{1 + r} = W$`:

  $$
  \begin{align*}C_1^* = \left( Y_1 - T_1 + \frac{Y_2 - T_2}{1 + r} \right) \left[ 1 + \left( \frac{1 - \alpha}{\alpha} \right)^{\frac{\rho}{\rho - 1}} (1 + r)^{\frac{1}{\rho - 1}} \right]^{-1}\end{align*}
  $$

* **d) Superioridad frente a la función keynesiana:**
  La función keynesiana (`$C_t = \bar{C} + c(Y_t - T_t)$`) es estática, adolece de falta de microfundamentos y asume que el consumo depende mecánicamente solo del ingreso corriente. Nuestra función intertemporal la supera porque incorpora: (1) expectativas de ingresos e impuestos futuros (`$Y_2 - T_2$`), (2) el costo de oportunidad intertemporal medido por la tasa de interés real (`$r$`), y (3) los parámetros profundos de preferencias (`$\alpha$` y `$\rho$`), permitiendo distinguir entre choques transitorios y permanentes.


### Solución Ejercicio 2: Cobb-Douglas en Tres Períodos con Impuestos

* **a) Lagrangiano y despeje de $C_1^*$:**
  Sea `$W_{\text{neta}} \equiv (1 - \tau_y)\left[ Y_1 + \frac{Y_2}{1 + r} + \frac{Y_3}{(1 + r)^2} \right]$`. El Lagrangiano es:

  $$
  \begin{align*}\mathcal{L} = \bar{C} C_1^\alpha C_2^\eta C_3^{1 - \alpha - \eta} + \lambda \left[ W_{\text{neta}} - (1 + \tau_c)C_1 - \frac{(1 + \tau_c)C_2}{1 + r} - \frac{(1 + \tau_c)C_3}{(1 + r)^2} \right]\end{align*}
  $$

  Derivando e igualando a cero (recordando que `$\frac{\partial U}{\partial C_1} = \frac{\alpha U}{C_1}$`, `$\frac{\partial U}{\partial C_2} = \frac{\eta U}{C_2}$`, `$\frac{\partial U}{\partial C_3} = \frac{(1 - \alpha - \eta)U}{C_3}$`):

  $$
  \begin{align*}\lambda = \frac{\alpha U}{(1 + \tau_c)C_1} = \frac{\eta U (1 + r)}{(1 + \tau_c)C_2} = \frac{(1 - \alpha - \eta)U (1 + r)^2}{(1 + \tau_c)C_3}\end{align*}
  $$

  Cancelando `$U$` y `$(1 + \tau_c)$`, despejamos `$C_2$` y `$C_3$` en función de `$C_1$`:

  $$
  \begin{align*}C_2 = \frac{\eta}{\alpha}(1 + r)C_1, \qquad \qquad C_3 = \frac{1 - \alpha - \eta}{\alpha}(1 + r)^2 C_1\end{align*}
  $$

  Reemplazando en la R.P.I., los factores `$(1 + r)$` y `$(1 + r)^2$` se cancelan:

  $$
  \begin{align*}(1 + \tau_c)C_1 \left[ 1 + \frac{\eta}{\alpha} + \frac{1 - \alpha - \eta}{\alpha} \right] = (1 + \tau_c)C_1 \left[ \frac{\alpha + \eta + 1 - \alpha - \eta}{\alpha} \right] = \frac{(1 + \tau_c)C_1}{\alpha} = W_{\text{neta}}\end{align*}
  $$

  Por tanto:

  $$
  \begin{align*}C_1^* = \frac{\alpha}{1 + \tau_c} \left[ Y_1(1 - \tau_y) + \frac{Y_2(1 - \tau_y)}{1 + r} + \frac{Y_3(1 - \tau_y)}{(1 + r)^2} \right]\end{align*}
  $$

* **b) Condición de transversalidad:**
  Sí cumple estrictamente con la condición de transversalidad en horizonte finito. La ausencia de activos iniciales (`$A_1 = 0$`) y la ausencia de un término terminal `$\frac{A_4}{(1 + r)^2}$` en la R.P.I. implican que se ha impuesto `$A_4 = 0$`: el individuo no deja activos sin consumir al morir (no saciación) ni muere con deudas impagas (no-Ponzi).

* **c) Derivadas parciales e interpretación:**

  $$
  \begin{align*}\frac{\partial C_1^*}{\partial r} &= -\frac{\alpha(1 - \tau_y)}{1 + \tau_c} \left[ \frac{Y_2}{(1 + r)^2} + \frac{2 Y_3}{(1 + r)^3} \right] < 0 \\ \frac{\partial C_1^*}{\partial \tau_c} &= -\frac{\alpha}{(1 + \tau_c)^2} \left[ Y_1(1 - \tau_y) + \frac{Y_2(1 - \tau_y)}{1 + r} + \frac{Y_3(1 - \tau_y)}{(1 + r)^2} \right] < 0 \\ \frac{\partial C_1^*}{\partial \tau_y} &= -\frac{\alpha}{1 + \tau_c} \left[ Y_1 + \frac{Y_2}{1 + r} + \frac{Y_3}{(1 + r)^2} \right] < 0\end{align*}
  $$


### Solución Ejercicio 3: Choques Transitorios, Permanentes e Incertidumbre

* **a) Choques transitorios en $t = 1$ vs. $t = 3$ y efecto sobre el ahorro:**

  $$
  \begin{align*}PMC_{\text{transitorio, } 1} = \frac{\partial C_1^*}{\partial Y_1} = \frac{\alpha(1 - \tau_y)}{1 + \tau_c} > \frac{\partial C_1^*}{\partial Y_3} = \frac{\alpha(1 - \tau_y)}{(1 + \tau_c)(1 + r)^2} > 0\end{align*}
  $$

  Sobre el ahorro corriente `$S_1^* = Y_1(1 - \tau_y) - (1 + \tau_c)C_1^*$`:
  * Si sube `$Y_1$`: `$\frac{\partial S_1^*}{\partial Y_1} = (1 - \tau_y)(1 - \alpha) > 0$` (ahorra la fracción no consumida).
  * Si sube `$Y_3$`: `$\frac{\partial S_1^*}{\partial Y_3} = -\frac{\alpha(1 - \tau_y)}{(1 + r)^2} < 0$` (desahorra hoy anticipando la bonanza futura).

* **b) Choque permanente ($\Delta Y_1 = \Delta Y_2 = \Delta Y_3 = \Delta \bar{Y}$):**

  $$
  \begin{align*}PMC_{\text{permanente}} = \frac{\text{d}C_1^*}{\text{d}\bar{Y}} = \frac{\alpha(1 - \tau_y)}{1 + \tau_c} \underbrace{\left[ 1 + \frac{1}{1 + r} + \frac{1}{(1 + r)^2} \right]}_{\equiv \phi > 1} > PMC_{\text{transitorio, } 1}\end{align*}
  $$

* **c) Valor esperado bajo incertidumbre ($p$ y $1 - p$):**

  $$
  \begin{align*}\mathbb{E}[PMC] = p \cdot \frac{\alpha(1 - \tau_y)}{1 + \tau_c} + (1 - p) \cdot \frac{\alpha(1 - \tau_y)}{1 + \tau_c} \left[ 1 + \frac{1}{1 + r} + \frac{1}{(1 + r)^2} \right]\end{align*}
  $$

  Al derivar respecto a `$p$`, se observa que `$\frac{\partial \mathbb{E}[PMC]}{\partial p} < 0$`: cuanto mayor sea la probabilidad `$p$` de que el choque sea meramente transitorio, más prudente es el consumidor hoy, menor es el aumento de su consumo y mayor es su ahorro precautorio.


### Solución Ejercicio 4: Función CRRA y Regímenes de $\sigma$

* **a) Desigualdad de Jensen y L'Hôpital:**
  Como `$u''(C) = -\sigma C^{-\sigma-1} < 0$`, para toda combinación convexa `$\bar{C} = \lambda C_1 + (1 - \lambda)C_2$` se cumple `$u(\bar{C}) > \lambda u(C_1) + (1 - \lambda)u(C_2)$`. Para `$\sigma \to 1$`:

  $$
  \begin{align*}\lim_{\sigma \to 1} \frac{e^{(1 - \sigma)\ln C_t} - 1}{1 - \sigma} \stackrel{\text{L'H}}{=} \lim_{\sigma \to 1} \frac{-\ln C_t \cdot e^{(1 - \sigma)\ln C_t}}{-1} = \ln C_t\end{align*}
  $$

* **b) y c) Derivada respecto a $r$ según $\sigma$:**
  Con `$Y_2 = 0$`, `$\frac{\partial C_1^*}{\partial r} = -Y_1 \left(\frac{1}{\sigma} - 1\right) D^{-2} (1 + r)^{\frac{1}{\sigma} - 2} \beta^{\frac{1}{\sigma}}$`:
  1. Si `$\sigma = 1 \implies \frac{\partial C_1^*}{\partial r} = 0$` y `$\frac{\partial S_1^*}{\partial r} = 0$` (neutralidad: ES y EI se cancelan).
  2. Si `$0 < \sigma < 1 \implies \frac{\partial C_1^*}{\partial r} < 0$` y `$\frac{\partial S_1^*}{\partial r} > 0$` (domina el efecto sustitución).
  3. Si `$\sigma > 1 \implies \frac{\partial C_1^*}{\partial r} > 0$` y `$\frac{\partial S_1^*}{\partial r} < 0$` (domina el efecto ingreso).
  Cuando `$Y_2 > 0$`, aparece el efecto riqueza humana negativo `$- \frac{Y_2}{(1 + r)^2} D^{-1} < 0$`, haciendo que incluso para `$\sigma = 1$` se cumpla `$\frac{\partial C_1^*}{\partial r} < 0$`.


### Solución Ejercicio 5: Restricciones de Liquidez y Riesgo de Impago

* **a) Tasa efectiva con riesgo de no pago:**
  Por condición de cero beneficios extraordinarios del banco neutral al riesgo:

  $$
  \begin{align*}r^* = p(0) + (1 - p)r \implies r = \frac{r^*}{1 - p}\end{align*}
  $$

  Cuando `$p \to 0 \implies r \to r^*$` (*First Best*); cuando `$p \to 1 \implies r \to \infty$` (exclusión crediticia).

* **b) Contraste de bienestar:**
  El consumidor sin restricciones alcanza la curva más alta `$I_{FB}$` con `$C_1^{FB} > Y_1$`. Con prima de riesgo (`$r > r^*$`), la restricción rota hacia adentro a la derecha de `$Y_1$`, ubicándolo en una tangencia interior *Second Best* (`$Y_1 < C_1^{SB} < C_1^{FB}$`) sobre `$I_{SB} < I_{FB}$`. Con restricción cuantitativa total, el conjunto factible se trunca verticalmente en `$Y_1$`, forzándolo a la esquina `$(Y_1, Y_2)$` sobre `$I_{\text{esquina}} < I_{SB} < I_{FB}$`.


### Solución Ejercicio 6: Ciclo de Vida y Series Geométricas

* **a) y b) Consumo permanente $\bar{C}$:**
  Con `$\phi = \frac{1}{1+r} < 1$`, la serie geométrica infinita converge a `$\sum_{i=0}^\infty \phi^i = \frac{1}{1 - \phi} = \frac{1 + r}{r}$`. Despejando `$\bar{C}$` de la R.P.I. y particionando por edades:

  $$
  \begin{align*}\bar{C} = r A_t + \frac{r}{1 + r} \left[ \sum_{i=0}^{15} 0 + \sum_{i=16}^{60} \frac{Y_{\ell t+i}(1 - \tau)}{(1 + r)^i} + \sum_{i=61}^{78} \frac{Y_{t+i}^p}{(1 + r)^i} \right]\end{align*}
  $$


### Solución Ejercicio 7: Inversión Neoclásica y Costo de Uso

* **a) Capital óptimo:** De `$\frac{\partial \Pi_t}{\partial K_t} = 0 \implies P_t \alpha A_t K_t^{\alpha - 1} N_t^{1 - \alpha} = R_t \implies K_t^* = \left(\frac{P_t \alpha A_t}{R_t}\right)^{\frac{1}{1 - \alpha}} N_t$`.
* **b) Costo de uso e inflación:** `$R_t = P_K(i + \delta - \pi_K) = P_K[r + \delta - (\pi_K - \pi)]$`. Si la inflación `$\pi$` sube más rápido que el precio de las máquinas (`$\pi > \pi_K$`) o si la depreciación contable histórica no está indexada a la inflación (De Gregorio, Sección 4.10), el valor real de las deducciones tributarias por depreciación cae, encareciendo el costo efectivo del capital y deprimiendo la inversión.
* **c) Costos de ajuste y derivadas:** Minimizando `$C(I_t)$` respecto a `$K_{t+1}$` se obtiene `$I_t = \epsilon(K^* - K_t)$`. Operar fuera de `$K^*$` es costoso porque si `$K_t < K^*$` se dejan de percibir ganancias potenciales (`$P_t PMgK_t > R_t$`) y si `$K_t > K^*$` se incurre en pérdidas netas (`$P_t PMgK_t < R_t$`). Las derivadas cumplen `$\frac{\partial I_t}{\partial r} < 0$`, `$\frac{\partial I_t}{\partial A_t} > 0$` y `$\frac{\partial I_t}{\partial K_t} = -\epsilon < 0$`.


### Solución Ejercicio 8: Teoría $q$ de Tobin e Incertidumbre

* **a) y b) Con $C(I_t) = \bar{C} + \psi(K_{t+1} - K_t)^2$:**
  El costo marginal de ajuste es `$C'(I_t) = 2\psi(K_{t+1} - K_t) = 2\psi I_t$`. La condición de optimalidad intertemporal arroja `$q_t \equiv 1 + 2\psi I_t = \frac{f'(K_{t+1}) - \delta + q_{t+1}}{1 + r}$`. Reordenando se obtiene la condición de arbitraje `$r = \frac{f'(K_{t+1}) - \delta}{q_t} + \frac{\Delta q_{t+1}}{q_t}$`, que iguala la tasa de interés con el dividendo marginal más la ganancia de capital.
* **c) Iteración y productividad binaria ($\bar{A}, \underline{A}$):**
  Bajo la condición de transversalidad `$\lim_{T \to \infty} \frac{q_{t+T}}{(1 + r)^T} = 0$`, si `$A_{t+j}$` toma el valor `$\bar{A}$` con probabilidad `$\theta$` y `$\underline{A}$` con probabilidad `$(1 - \theta)$`, la productividad esperada es `$\mathbb{E}_t[A_{t+j}] = \theta \bar{A} + (1 - \theta)\underline{A}$`, por lo que:

  $$
  \begin{align*}\mathbb{E}_t[q_t] = \sum_{j=1}^\infty \frac{\alpha \big[ \theta \bar{A} + (1 - \theta)\underline{A} \big] K_{t+j}^{\alpha - 1} - \delta}{(1 + r)^j}\end{align*}
  $$


### Solución Ejercicio 9: Política Fiscal y Sostenibilidad de la Deuda

* **a) R.P.I. del Gobierno:** Iterando `$B_{t+1} = G_t - T_t + (1 + r)B_t$` y aplicando la condición de No-Ponzi `$\lim_{N \to \infty} \frac{B_{t+N+1}}{(1 + r)^N} = 0$`, se obtiene `$(1 + r)B_t = \sum_{s=0}^\infty \frac{T_{t+s} - G_{t+s}}{(1 + r)^s}$`: la deuda inicial capitalizada debe ser respaldada íntegramente por el valor presente de los superávits primarios futuros.
* **b) y c) Ratio Deuda/PIB y estado estacionario:** Dividiendo por `$Y_t = \frac{Y_{t+1}}{1 + \gamma_y}$`, se llega a `$b_{t+1} = \frac{g_t - t_t}{1 + \gamma_y} + \frac{1 + r}{1 + \gamma_y}b_t$`. Restando `$b_t$` a ambos lados:

  $$
  \begin{align*}b_{t+1} - b_t = \frac{g_t - t_t}{1 + \gamma_y} + \left( \frac{1 + r}{1 + \gamma_y} - 1 \right) b_t = \frac{g_t - t_t}{1 + \gamma_y} + \left( \frac{r - \gamma_y}{1 + \gamma_y} \right) b_t\end{align*}
  $$

  Para que la deuda sea sostenible (`$b_{t+1} - b_t \leq 0$`) cuando `$r > \gamma_y$`, el gobierno debe generar un superávit primario `$t_t - g_t \geq (r - \gamma_y)b_t$`. En el estado estacionario (`$b_{t+1} = b_t = \bar{b}$`), se cumple `$\bar{b} = \frac{g_t - t_t}{\gamma_y - r}$`.
* **d) Equivalencia entre sostenibilidad del ratio Deuda/PIB y la R.P.I. del Gobierno:**
  Si `$b_t = \frac{B_t}{Y_t}$` converge a una constante finita `$\bar{b}$`, entonces en el largo plazo la deuda real `$B_{t+N} = \bar{b} Y_{t+N} = \bar{b} Y_t (1 + \gamma_y)^N$` crece a la tasa `$\gamma_y$`. En una economía dinámicamente eficiente donde `$r > \gamma_y$`, el término terminal de la R.P.I. del gobierno satisface:

  $$
  \begin{align*}\lim_{N \to \infty} \frac{B_{t+N}}{(1 + r)^N} = \lim_{N \to \infty} \bar{b} Y_t \left( \frac{1 + \gamma_y}{1 + r} \right)^N = 0\end{align*}
  $$

  quedando demostrada la satisfacción exacta de la condición de transversalidad y de la Restricción Presupuestaria Intertemporal del Gobierno.
