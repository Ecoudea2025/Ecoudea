---
title: "Clase 05: Frontera de Posibilidades de Producción (FPP) y Ventaja Comparativa: Robinson y Venus"
course: "microeconomia-ii"
order: 5
classType: "clase"
description: "Deducción paso a paso de las fronteras de posibilidades de producción individuales y conjunta de Robinson y Venus, parametrización por proporciones de tiempo y ganancias de la especialización."
math: true
conceptos: ["Frontera de posibilidades de producción", "Especialización", "Costo de oportunidad"]
---

## De la Economía de Intercambio Puro a la Economía con Producción

En las clases anteriores supusimos que los bienes caían del cielo como dotaciones fijas `$W_i$`. A partir de esta clase incorporamos la **producción**: los agentes disponen de un factor productivo escaso `(su **tiempo de trabajo `$L$`**)` y de tecnologías que transforman las horas trabajadas en distintos bienes de consumo.

Siguiendo el modelo desarrollado en clase por el profesor David Tobón (*FPP Robinson y Venus*), estudiaremos cómo se construye paso a paso la **Frontera de Posibilidades de Producción (FPP)** individual y agregada cuando dos personas con distintas habilidades productivas deciden unir esfuerzos.


## 1. Las Fronteras de Posibilidades de Producción Individuales

Consideremos dos náufragos en una isla, **Robinson `$(R)$`** y **Venus `$(V)$`**, quienes disponen cada uno de una dotación diaria de **`$8$` horas de trabajo** para producir dos bienes: **Cocos `$(C)$`** y **Pescado `$(P)$`**.

### Caso 1: La Tecnología y FPP de Robinson `$(R)$`

Robinson reparte sus `$8$` horas de trabajo entre recolectar cocos `$(L_{RC})$` y pescar `$(L_{RP})$`:

$$
\begin{align*}8 = L_{RC} + L_{RP}\end{align*}
$$

En cada hora dedicada a los cocos produce `$20$` unidades, y en cada hora dedicada a la pesca obtiene `$10$` unidades:

$$
\begin{align*}C_R = 20 L_{RC} \implies L_{RC} = \frac{C_R}{20}, \qquad \qquad P_R = 10 L_{RP} \implies L_{RP} = \frac{P_R}{10}\end{align*}
$$

**Deducción paso a paso de la FPP de Robinson:**
1. Sustituimos las horas requeridas `$L_{RC}$` y `$L_{RP}$` dentro de su restricción de tiempo total `$(8\text{ horas})$`:

$$
\begin{align*}8 = \frac{C_R}{20} + \frac{P_R}{10}\end{align*}
$$

2. Multiplicamos toda la ecuación por `$20$` y despejamos `$C_R$` en función de `$P_R$`:

$$
\begin{align*}160 = C_R + 2 P_R \implies \boxed{C_R = 160 - 2 P_R}\end{align*}
$$

* **Tasa Marginal de Transformación (Costo de oportunidad de Robinson):** `$\frac{\text{d}C_R}{\text{d}P_R} = -2$`. Para producir `$1$` pescado adicional, Robinson debe sacrificar **`$2$` cocos** `(o equivalentemente, `$1$` coco le cuesta `$\frac{1}{2}$` pescado)`.

### Caso 2: La Tecnología y FPP de Venus `$(V)$`

Venus también dispone de `$8$` horas diarias repartidas entre cocos `$(L_{VC})$` y pescado `$(L_{VP})$`:

$$
\begin{align*}8 = L_{VC} + L_{VP}\end{align*}
$$

Sus productividades por hora son opuestas a las de Robinson: obtiene `$10$` cocos por hora o `$20$` pescados por hora:

$$
\begin{align*}C_V = 10 L_{VC} \implies L_{VC} = \frac{C_V}{10}, \qquad \qquad P_V = 20 L_{VP} \implies L_{VP} = \frac{P_V}{20}\end{align*}
$$

**Deducción paso a paso de la FPP de Venus:**
1. Reemplazamos `$L_{VC}$` y `$L_{VP}$` en la restricción de `$8$` horas de Venus:

$$
\begin{align*}8 = \frac{C_V}{10} + \frac{P_V}{20}\end{align*}
$$

2. Multiplicamos ambos lados por `$10$` y despejamos `$C_V$`:

$$
\begin{align*}80 = C_V + \frac{1}{2} P_V \implies \boxed{C_V = 80 - \frac{1}{2} P_V}\end{align*}
$$

* **Tasa Marginal de Transformación (Costo de oportunidad de Venus):** `$\frac{\text{d}C_V}{\text{d}P_V} = -\frac{1}{2}$`. Para producir `$1$` pescado adicional, Venus solo sacrifica **`$\frac{1}{2}$` coco** `(mientras que producir `$1$` coco le cuesta `$2$` pescados)`.

> **Análisis de Ventaja Comparativa:**
> * **Venus tiene ventaja comparativa (y absoluta) en Pescado:** Su costo de oportunidad por pescado `$(0.5\text{ cocos})$` es menor que el de Robinson `$(2\text{ cocos})$`.
> * **Robinson tiene ventaja comparativa (y absoluta) en Cocos:** Su costo de oportunidad por coco `$(0.5\text{ pescados})$` es menor que el de Venus `$(2\text{ pescados})$`.


## 2. Se Juntan Robinson y Venus: Formulación Paramétrica con `$\alpha$` y `$\beta$`

¿Qué ocurre con las posibilidades de producción de la economía cuando Robinson y Venus deciden integrarse? Siguiendo exactamente la formulación del profesor David Tobón:

* Sea **`$\alpha \in [0, 1]$`** la proporción de sus `$8$` horas que **Robinson** dedica a producir cocos `$(C)$`, y **`$(1 - \alpha)$`** la proporción que dedica a producir pescado `$(P)$`.
* Sea **`$\beta \in [0, 1]$`** la proporción de sus `$8$` horas que **Venus** dedica a producir cocos `$(C)$`, y **`$(1 - \beta)$`** la proporción que dedica a producir pescado `$(P)$`.

### Cantidades Producidas por Cada Agente según `$(\alpha, \beta)$`

* **Producción de Robinson:**

$$
\begin{align*}C_R = 20 \cdot (\alpha \cdot 8) = 160 \alpha, \qquad \qquad P_R = 10 \cdot \big((1 - \alpha) \cdot 8\big) = 80 (1 - \alpha)\end{align*}
$$

* **Producción de Venus:**

$$
\begin{align*}C_V = 10 \cdot (\beta \cdot 8) = 80 \beta, \qquad \qquad P_V = 20 \cdot \big((1 - \beta) \cdot 8\big) = 160 (1 - \beta)\end{align*}
$$

### Producción Agregada Conjunta `$(C, P)$`

Sumando las producciones de ambos individuos y factorizando `$80$`, obtenemos el **sistema paramétrico de producción conjunta**:

$$
\begin{align*}C &= C_R + C_V = 8 (20\alpha + 10\beta) = \boxed{80 (2\alpha + \beta)} \\ P &= P_R + P_V = 8 \big(10(1 - \alpha) + 20(1 - \beta)\big) = \boxed{80 \big((1 - \alpha) + 2(1 - \beta)\big)}\end{align*}
$$

### Evaluación de los Extremos y de Combinaciones `$(\alpha, \beta)$`

Observemos primero los dos extremos de especialización absoluta en el mismo bien:
* **Si `$\alpha = 1 \land \beta = 1$` (ambos dedican el 100% de su tiempo a cocos):**

$$
\begin{align*}C = 80(2(1) + 1) = 240, \qquad P = 80(0 + 0) = 0\end{align*}
$$

* **Si `$\alpha = 0 \land \beta = 0$` (ambos dedican el 100% de su tiempo a pescar):**

$$
\begin{align*}C = 0, \qquad P = 80(1 + 2(1)) = 240\end{align*}
$$

Ahora evaluemos sistemáticamente cómo varían `$C$` y `$P$` al asignar distintos valores a `$\alpha$` y `$\beta$` `(sabiendo que si `$\alpha$` aumenta, `$1 - \alpha$` cae, y lo mismo ocurre con `$\beta$` y `$1 - \beta$`)`:

| Fracción de Robinson en Cocos `$( \alpha )$` | Fracción de Venus en Cocos `$( \beta )$` | Cocos Totales `$C = 80(2\alpha + \beta)$` | Pescados Totales `$P = 80((1-\alpha) + 2(1-\beta))$` | Interpretación Económica de la Asignación |
| :---: | :---: | :---: | :---: | :--- |
| `$\alpha = 1$` | `$\beta = 1$` | `$240$` | `$0$` | Extremo superior: 100% dedicados a Cocos. |
| `$\alpha = 1$` | `$\beta = 0.5$` | `$200$` | `$80$` | **Eficiente (Tramo 1):** `$R$` se especializa en `$C$`; `$V$` reparte su tiempo. |
| `$\alpha = 1$` | `$\beta = 0.2$` | `$176$` | `$128$` | **Eficiente (Tramo 1):** `$R$` en `$C$`; `$V$` migra hacia su ventaja `$(P)$`. |
| **`$\alpha = 1$`** | **`$\beta = 0$`** | **`$160$`** | **`$160$`** | **Vértice Óptimo de Especialización Total** `$(R\text{ en }C, \; V\text{ en }P)$`. |
| `$\alpha = 0.5$` | `$\beta = 0$` | `$80$` | `$200$` | **Eficiente (Tramo 2):** `$V$` se especializa en `$P$`; `$R$` reparte su tiempo. |
| `$\alpha = 0.5$` | `$\beta = 0.5$` | `$120$` | `$120$` | **Ineficiente (Interior):** Ambos dividen su tiempo sin especializarse. |
| `$\alpha = 0.5$` | `$\beta = 1$` | `$160$` | `$40$` | **Ineficiente:** Venus produce `$C$` mientras Robinson produce `$P$`. |
| `$\alpha = 0.2$` | `$\beta = 1$` | `$112$` | `$64$` | **Ineficiente:** Asignación al revés de la ventaja comparativa. |
| `$\alpha = 0$` | `$\beta = 1$` | `$80$` | `$80$` | **Peor esquina interior:** Especialización invertida (contra natura). |
| `$\alpha = 0$` | `$\beta = 0$` | `$0$` | `$240$` | Extremo derecho: 100% dedicados a Pescado. |


## 3. La Ecuación Analítica por Tramos de la FPP Conjunta

Al observar la tabla anterior descubrimos una lección microeconómica fundamental: **no cualquier combinación de `$(\alpha, \beta)$` está sobre la Frontera de Posibilidades de Producción**.

* Por ejemplo, si ambos dedican la mitad de su tiempo a cada bien `$( \alpha = 0.5, \; \beta = 0.5 )$`, producen `$(C, P) = (120, 120)$`. Pero si se especializan según su ventaja comparativa `$( \alpha = 1, \; \beta = 0 )$`, ¡producen **`$(C, P) = (160, 160)$`**, ganando `$\Delta C = +40$` y `$\Delta P = +40$` sin trabajar ni un minuto más!
* Peor aún: si se especializan al revés de su ventaja comparativa `$( \alpha = 0, \; \beta = 1 )$`, solo obtienen `$(80, 80)$`.

Para estar sobre la **verdadera FPP eficiente**, la sociedad debe asignar cada tarea primero a quien tiene el **menor costo de oportunidad**:

1. **Primer Tramo Eficiente `(para `$0 \leq P \leq 160$`, con `$\alpha = 1$` y `$\beta \in [0, 1]$`)`:**
   Partiendo de `$C = 240$`, los primeros `$160$` pescados los debe pescar exclusivamente **Venus** `(cuyo costo de oportunidad es de solo `$\frac{1}{2}$` coco por pescado)`, mientras Robinson sigue dedicado 100% a los cocos `$( \alpha = 1 )$`:

   $$
   \begin{align*}C = 240 - \frac{1}{2} P, \quad \text{para } 0 \leq P \leq 160\end{align*}
   $$

2. **Segundo Tramo Eficiente `(para `$160 \leq P \leq 240$`, con `$\beta = 0$` y `$\alpha \in [0, 1]$`)`:**
   Una vez que Venus ya dedica sus `$8$` horas a pescar `$(P = 160, \; C = 160)$`, si la isla desea aún más pescado, **Robinson** debe empezar a dejar los cocos `(con un costo de oportunidad más alto, de `$2$` cocos por pescado)`:

   $$
   \begin{align*}C = 160 - 2(P - 160) = 480 - 2 P, \quad \text{para } 160 \leq P \leq 240\end{align*}
   $$

En consecuencia, la **FPP conjunta es cóncava hacia el origen** `(quebrada hacia afuera en el vértice `$(P, C) = (160, 160)$`)`, demostrando geométricamente la **ley del costo de oportunidad creciente**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/fpp-conjunta-light.svg" alt="Dos FPP lineales individuales y la conjunta quebrada exterior, con puntos ineficientes en el interior." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/fpp-conjunta-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: Figura: especializarse según el costo de oportunidad dibuja la frontera exterior.</figcaption>
</figure>


<IdeaClave>

La frontera conjunta es quebrada porque cada tramo lo produce quien tiene el menor costo de oportunidad.

</IdeaClave>
