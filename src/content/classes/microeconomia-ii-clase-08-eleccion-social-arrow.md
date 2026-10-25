---
title: "Clase 07: Elección Social, Parejas Estables y Teorema de Arrow"
course: "microeconomia-ii"
order: 8
classType: "clase"
description: "Agregación de preferencias colectivas, estabilidad en sistemas de emparejamiento (afinidades electivas), ciclos de votación de Condorcet, axiomas y demostración paso a paso del Teorema de la Imposibilidad de Arrow."
math: true
conceptos: ["Paradoja de Condorcet", "Teorema de Arrow", "Elección social"]
---

## El Problema Fundamental de la Elección Social

En las primeras seis clases vimos cómo el mecanismo de precios coordina las decisiones privadas de consumo y producción. Sin embargo, toda sociedad debe tomar decisiones colectivas que afectan a todos sus miembros (nivel de impuestos, gasto público, leyes, elección de gobernantes).

El problema central de la **Teoría de la Elección Social** consiste en encontrar un **criterio o regla razonable para agregar las preferencias individuales** `$(\succcurlyeq_1, \succcurlyeq_2, \ldots, \succcurlyeq_n)$` en una **preferencia social consistente `$( \succcurlyeq_S )$`** sobre problemas y decisiones colectivas.

Como veremos en esta clase, aun cuando cada individuo sea perfectamente racional (con preferencias completas y transitivas), **puede que sea imposible ordenar transitivamente las preferencias de la sociedad**.


## 1. Afinidades Electivas y Estabilidad de Parejas (Emparejamientos)

Antes de analizar votaciones políticas, el profesor David Tobón ilustra cómo las preferencias individuales pueden generar inestabilidad y ciclos en un problema clásico de asignación bilateral: las **afinidades electivas** (el problema de los matrimonios estables de Gale y Shapley).

### Definición de Sistema de Parejas Estable vs. Inestable

Dado un conjunto de parejas actualmente conformadas (Pareja 1, Pareja 2, Pareja 3), decimos que la asignación es **inestable** si existe al menos un hombre y una mujer que **no están juntos actualmente**, pero que **se prefieren mutuamente por encima de sus parejas actuales** (formando una **pareja bloqueadora** que tiene incentivos para romper sus relaciones actuales y fugarse juntos). Si no existe ninguna pareja bloqueadora, el sistema es **estable**.

### Ejemplo Analítico de Clase: Alil, Alice, Bob, Beth, Carl y Carol

Supongamos tres parejas inicialmente conformadas:
* **Pareja 1:** Alil y Alice.
* **Pareja 2:** Bob y Beth.
* **Pareja 3:** Carl y Carol.

El orden de preferencias individuales (del primer lugar más preferido al tercer lugar menos preferido) se presenta en la siguiente tabla:

| Orden de Preferencia | Pareja 1: ALIL | Pareja 1: ALICE | Pareja 2: BOB | Pareja 2: BETH | Pareja 3: CARL | Pareja 3: CAROL |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1.ª opción (Más preferida)** | Beth | Alil | Beth | Carl | Alice | Bob |
| **2.ª opción (Intermedia)** | Alice | Carl | Alice | Alil | Beth | Carl |
| **3.ª opción (Menos preferida)** | Carol | Bob | Carol | Bob | Carol | Alil |

**Análisis paso a paso de estabilidad:**
1. **Situación actual de cada pareja:**
   * En la **Pareja 1 (Alil–Alice)**: Alice está feliz porque Alil es su 1.ª opción, pero para Alil su esposa Alice es su 2.ª opción (él prefiere a **Beth**).
   * En la **Pareja 2 (Bob–Beth)**: Bob está feliz porque Beth es su 1.ª opción, pero para Beth su esposo Bob es su última opción (ella prefiere a **Carl** en 1.er lugar y a **Alil** en 2.º lugar).
   * En la **Pareja 3 (Carl–Carol)**: Tanto para Carl como para Carol su pareja actual es su peor o intermedia opción (Carl prefiere a **Alice** y a **Beth**; Carol prefiere a **Bob**).
2. **Identificación de parejas bloqueadoras (deserciones mutuas):**
   * **¿Alil y Beth bloquean?** Alil prefiere a Beth (1.ª) sobre su pareja actual Alice (2.ª), y Beth prefiere a Alil (2.ª) sobre su pareja actual Bob (3.ª). ¡Ambos mejoran si dejan a sus parejas y se juntan!
   * **¿Carl y Beth bloquean?** Carl prefiere a Beth (2.ª) sobre su pareja actual Carol (3.ª), y Beth prefiere a Carl (1.ª) sobre su pareja actual Bob (3.ª). ¡También forman una pareja bloqueadora!
3. **Conclusión:** El sistema inicial de parejas es **inestable**.


## 2. La Paradoja de Condorcet y los Ciclos de Votación

Traslademos ahora el problema a un comité o sociedad compuesta por tres personas `(o tres grupos de igual tamaño: **Persona `$i$`** de bajos ingresos, **Persona `$j$`** de clase media y **Persona `$k$`** de altos ingresos)` que deben elegir por **regla de la mayoría** entre tres programas de impuestos o gasto público `$(X, Y, Z \text{ o Programas } A, B, C)$`:

| Orden de Preferencia | Personas `$i$` (Bajos ingresos) | Personas `$j$` (Clase media) | Personas `$k$` (Altos ingresos) |
| :---: | :---: | :---: | :---: |
| **1.ª opción** | `$X$` (Programa A: 20) | `$Y$` (Programa C: 21) | `$Z$` (Programa B: 24) |
| **2.ª opción** | `$Y$` (Programa B: 18) | `$Z$` (Programa A: 20) | `$X$` (Programa C: 22) |
| **3.ª opción** | `$Z$` (Programa C: 17) | `$X$` (Programa B: 18) | `$Y$` (Programa A: 20) |

### Votación por Mayoría de Dos en Dos (Pares de Condorcet)

Comparemos las tres opciones enfrentándolas de dos en dos mediante votación mayoritaria:

1. **Enfrentamiento `$X$` vs. `$Y$`:**
   * Las personas `$i$` prefieren `$X \succ_i Y$`.
   * Las personas `$k$` prefieren `$X \succ_k Y$`.
   * Solo las personas `$j$` prefieren `$Y \succ_j X$`.
   * **Resultado social:** **`$X$` derrota a `$Y$` por 2 votos contra 1 `$(X \succ_S Y)$`**.
2. **Enfrentamiento `$Y$` vs. `$Z$`:**
   * Las personas `$i$` prefieren `$Y \succ_i Z$`.
   * Las personas `$j$` prefieren `$Y \succ_j Z$`.
   * Solo las personas `$k$` prefieren `$Z \succ_k Y$`.
   * **Resultado social:** **`$Y$` derrota a `$Z$` por 2 votos contra 1 `$(Y \succ_S Z)$`**.
3. **Enfrentamiento `$X$` vs. `$Z$`:**
   * Si la preferencia social fuera transitiva, dado que `$X \succ_S Y$` e `$Y \succ_S Z$`, debería cumplirse que `$X \succ_S Z$`.
   * Sin embargo, al votar entre `$X$` y `$Z$`, tanto las personas `$j$` `$(Z \succ_j X)$` como las personas `$k$` `$(Z \succ_k X)$` votan a favor de `$Z$`.
   * **Resultado social:** **`$Z$` derrota a `$X$` por 2 votos contra 1 `$(Z \succ_S X)$`**.

   $$
   \begin{align*}X \succ_S Y \quad \land \quad Y \succ_S Z \quad \land \quad Z \succ_S X \quad \implies \quad \text{Ciclo intransitivo interminable}\end{align*}
   $$

> **Paradoja de Condorcet:** Los sistemas de votación por la regla de la mayoría tal vez **no lleguen a ningún equilibrio**, sino que pueden circular indefinidamente de una a otra de las opciones alternativas `$(X \to Y \to Z \to X)$`. En presencia de un ciclo de Condorcet, **quien controla el orden del día (el fijador de la agenda)** tiene el poder de manipular qué par se vota primero para hacer ganar su opción favorita.


## 3. El Teorema de la Imposibilidad de Arrow (1950)

¿Es este defecto exclusivo de la regla de la mayoría simple, o existe algún otro método de votación más sofisticado que nunca genere contradicciones? **Kenneth Arrow (Premio Nobel 1972)** demostró que el problema es universal.

### Las Cinco Condiciones (Axiomas) Exigidas por Arrow

Buscamos un mecanismo de decisión social que transforme perfiles de preferencias individuales racionales en un orden social `$\succcurlyeq_S$` satisfaciendo cinco condiciones deseables:

1. **Dominio no restringido (Completitud universal):** El mecanismo debe clasificar **todos** los estados sociales posibles para cualquier configuración lógicamente posible de preferencias individuales:

$$
\begin{align*}\text{O bien } X \succcurlyeq_S Y, \quad Y \succcurlyeq_S X \quad \text{o} \quad X \sim_S Y, \quad \forall X, Y\end{align*}
$$

2. **Transitividad social:** La clasificación social debe ser internamente coherente:

$$
\begin{align*}\text{Si } X \succcurlyeq_S Y \;\land\; Y \succcurlyeq_S Z \implies X \succcurlyeq_S Z, \quad \forall X, Y, Z\end{align*}
$$

3. **Relación positiva con las preferencias individuales (Criterio de Pareto / Unanimidad):** Si todos los individuos prefieren `$X$` sobre `$Y$`, la sociedad debe preferir `$X$` sobre `$Y$`:

$$
\begin{align*}\text{Si } X \succcurlyeq_{i, j} Y \implies X \succcurlyeq_S Y\end{align*}
$$

4. **Independencia de Alternativas Irrelevantes (IIA):** Si surgen o desaparecen nuevos estados u opciones `$(D)$`, **no se debería afectar la ordenación social entre los estados iniciales `$(X, Y)$`**. La preferencia social entre `$X$` e `$Y$` debe depender única y exclusivamente de cómo los individuos ordenan a `$X$` frente a `$Y$`, y no de cómo ordenen a una tercera opción `$Z$` o `$D$`.
5. **No Dictadura:** Las preferencias de un solo agente no pueden determinar automáticamente las preferencias de toda la sociedad en contra de los demás.


## 4. Demostración Paso a Paso del Teorema de Arrow (Caso de 2 Personas y 3 Opciones)

Siguiendo exactamente la demostración formal de las diapositivas del profesor David Tobón, consideremos dos personas `$(i, j)$` y tres opciones `$(X, Y, Z)$`, con el siguiente perfil de preferencias individuales transitivas:

* **Persona `$i$`:** `$X \succcurlyeq_i Y \;\land\; Y \succcurlyeq_i Z \to X \succcurlyeq_i Z$` `(su orden es `$X \succ_i Y \succ_i Z$`)`.
* **Persona `$j$`:** `$Z \succcurlyeq_j X \;\land\; X \succcurlyeq_j Y \to Z \succcurlyeq_j Y$` `(su orden es `$Z \succ_j X \succ_j Y$`)`.

Intentemos construir un orden social `$\succcurlyeq_S$` que respete simultáneamente las 5 condiciones de Arrow:

### Paso 1: Comparación Social entre `$Y$` y `$Z$`

* La persona `$i$` prefiere `$Y$` sobre `$Z$` `$(Y \succcurlyeq_i Z)$`, mientras que la persona `$j$` prefiere `$Z$` sobre `$Y$` `$(Z \succcurlyeq_j Y)$`.
* Si la sociedad declarara `$Y \succ_S Z$`, estaría imponiendo la preferencia exclusiva del agente `$i$`; si declarara `$Z \succ_S Y$`, estaría imponiendo la preferencia exclusiva del agente `$j$`.
* Por lo tanto, para **no incumplir la condición (5) de No Dictadura**, la sociedad debe declararse indiferente entre `$Y$` y `$Z$`:

$$
\begin{align*}Y \succcurlyeq_i Z \;\land\; Z \succcurlyeq_j Y \implies \boxed{Y \sim_S Z}\end{align*}
$$

### Paso 2: Comparación Social entre `$X$` e `$Y$` (Unanimidad)

* Observemos cómo clasifican ambos individuos a `$X$` frente a `$Y$`: tanto la persona `$i$` `$(X \succcurlyeq_i Y)$` como la persona `$j$` `$(X \succcurlyeq_j Y)$` prefieren `$X$` sobre `$Y$`.
* Por las condiciones **(1) Completitud** y **(3) Relación positiva / Pareto**, la sociedad está obligada a preferir `$X$` sobre `$Y$`:

$$
\begin{align*}X \succcurlyeq_i Y \;\land\; X \succcurlyeq_j Y \implies \boxed{X \succcurlyeq_S Y}\end{align*}
$$

### Paso 3: Deducción por Transitividad Social entre `$X$` y `$Z$` (Contradicción)

* Ahora combinamos los resultados del Paso 1 `$(Y \sim_S Z)$` y del Paso 2 `$(X \succcurlyeq_S Y)$` aplicando la condición **(2) de Transitividad Social**:

$$
\begin{align*}X \succcurlyeq_S Y \;\land\; Y \sim_S Z \implies \boxed{X \succcurlyeq_S Z}\end{align*}
$$

* **¡Pero miremos quiénes preferían `$X$` frente a `$Z$`!** La persona `$i$` prefería `$X \succcurlyeq_i Z$`, mientras que la persona `$j$` prefería estrictamente lo contrario `$(Z \succcurlyeq_j X)$`.
* Al verse forzada por la transitividad a concluir `$X \succcurlyeq_S Z$`, **se vuelve a incumplir la condición (5) de No Dictadura**, porque la sociedad termina imponiendo las preferencias de un solo agente `(el agente `$i$`)` en el desacuerdo entre `$X$` y `$Z$`.

> **Enunciado del Teorema de la Imposibilidad de Arrow:**
> *Las cinco condiciones requeridas son **incompatibles entre sí**. Si un mecanismo de decisión social satisface las propiedades de Dominio No Restringido (1), Transitividad (2), Pareto (3) e Independencia de Alternativas Irrelevantes (4), entonces **debe ser necesariamente una dictadura** (todas las ordenaciones sociales terminan siendo las ordenaciones de una sola persona).*


## 5. ¿Qué Hacer frente a la Imposibilidad de Arrow?

Dado que no existe ningún mecanismo perfecto para agregar preferencias individuales cualesquiera, toda sociedad democrática tiene únicamente **dos caminos para eludir o relajar el Teorema de Arrow**:

1. **Renunciar a la propiedad de Independencia de Alternativas Irrelevantes (IIA):** Permitir que la decisión social entre dos opciones dependa también de la intensidad o posición que ocupan frente a otras opciones (como hace la **Cuenta de Borda**, aunque esto abre la puerta a que **las preferencias sociales sean manipulables / estratégicas**).
2. **Restringir el dominio del conjunto de elección (Preferencias Unimodales en una Dimensión):** Como veremos en la Clase 08 con el **Teorema de Black**, si la cuestión sobre la que se vota es **unidimensional** y las preferencias de todos los votantes son **unimodales**, desaparecen los ciclos de Condorcet y la votación por mayoría alcanza un equilibrio no dictatorial en el **votante mediano**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/condorcet-arrow-light.svg" alt="Triángulo dirigido X-Y-Z-X de mayorías por parejas y esquema de la deducción imposible de Arrow." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/condorcet-arrow-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: mayorías por parejas giran en círculo; exigirlo todo a la vez crea un dictador.</figcaption>
</figure>


<IdeaClave>

Con tres o más alternativas, ninguna regla de votación cumple todo lo razonable a la vez.

</IdeaClave>
