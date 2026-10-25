---
title: "Clase 08: Votante Mediano, Gasto Público y Corrupción"
course: "microeconomia-ii"
order: 9
classType: "clase"
description: "Preferencias unimodales vs. irreconciliables, Teorema del Votante Mediano de Black, análisis comparativo de Pluralidad, Condorcet, Borda, Approval Voting y Segunda Vuelta, modelo de gasto público y corrupción, y funciones de bienestar social."
math: true
conceptos: ["Votante mediano", "Preferencias unimodales", "Frontera de posibilidades de utilidad"]
---

## 1. Restricción del Conjunto de Elección y Preferencias Unimodales

En la clase anterior vimos que cuando las preferencias individuales no tienen ninguna restricción de forma, la votación por mayoría cae en la Paradoja de Condorcet. ¿Qué ocurre si las alternativas pueden ordenarse a lo largo de **una sola dimensión** `(por ejemplo, nivel de gasto público: **Bajo `$<$ Medio $<$ Alto`**, o espectro ideológico de izquierda a derecha)`?

### Preferencias Irreconciliables (No Unimodales) en un Dominio Unidimensional

Considere tres personas `$(i, j, k)$` que evalúan tres niveles de gasto público ordenados de menor a mayor (**Gasto Bajo**, **Gasto Medio**, **Gasto Alto**):

| Votante | Gasto Bajo vs. Gasto Medio | Gasto Medio vs. Gasto Alto | Gasto Alto vs. Gasto Bajo | ¿Es Unimodal? |
| :--- | :---: | :---: | :---: | :--- |
| **Persona `$i$`** | `$\text{Bajo} \succcurlyeq \text{Medio}$` | `$\text{Medio} \succcurlyeq \text{Alto}$` | `$\text{Alto} \preccurlyeq \text{Bajo}$` | **Sí** (Pico en Bajo; cae monótonamente hacia Alto). |
| **Persona `$j$`** | `$\text{Bajo} \preccurlyeq \text{Medio}$` | `$\text{Medio} \succcurlyeq \text{Alto}$` | `$\text{Alto} \succcurlyeq \text{Bajo}$` | **Sí** (Pico en Medio; cae hacia ambos lados). |
| **Persona `$k$`** | **`$\text{Bajo} \succcurlyeq \text{Medio}$`** | `$\text{Medio} \preccurlyeq \text{Alto}$` | `$\text{Alto} \succcurlyeq \text{Bajo}$` | **No (Bimodal / Valle en Medio):** Prefiere los dos extremos (Alto y Bajo) antes que la opción intermedia (Medio). |

* **Diagnóstico:** La **Persona `$k$`** tiene preferencias **no unimodales** (su gráfica tiene forma de "V" con un valle en el centro: prefiere Gasto Alto en 1.er lugar, Gasto Bajo en 2.º lugar y Gasto Medio en último lugar). Esa sola preferencia en "V" basta para generar el ciclo intransitivo de Condorcet.
* **Corrección hacia la unimodalidad:** Si la Persona `$k$` (cuyo ideal es el Gasto Alto) ordena coherentemente las opciones según su cercanía a su pico (`$\text{Alto} \succ \text{Medio} \succ \text{Bajo}$`, cambiando `$\text{Bajo} \succcurlyeq \text{Medio}$` por **`$\text{Bajo} \preccurlyeq \text{Medio}$`**), entonces las tres preferencias se vuelven **unimodales** (un solo pico) y **el Gasto Medio derrota por mayoría tanto al Gasto Bajo como al Gasto Alto**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/unimodal-valle-light.svg" alt="Curva en valle frente a tres curvas de un solo pico sobre el eje Bajo-Medio-Alto." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/unimodal-valle-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: con un solo pico el mediano decide; con un valle no hay equilibrio estable.</figcaption>
</figure>



## 2. El Teorema de Black y el Votante Mediano

**Duncan Black (1948)** demostró la salida más importante al dilema de la agregación por mayoría:

> **Teorema del Votante Mediano (Teorema de Black):**
> *"Las votaciones por mayoría siempre dan resultados de equilibrio (transitivos y sin ciclos) cuando **la cuestión sobre la que se vota es unidimensional** y **las preferencias de todos los votantes son unimodales**."*

### Consideraciones Clave del Teorema de Black

1. **Votación de 2 en 2:** Se refiere a votaciones mayoritarias por pares (criterio de Condorcet).
2. **Coincidencia con el Votante Mediano:** El resultado de equilibrio coincide exactamente con el punto ideal del **votante mediano** `(aquel individuo cuya posición ideal `$M$` divide a la población exactamente en dos mitades: 50% a su izquierda y 50% a su derecha)`.
3. **¿Es un dictador?** En términos formales, el votante mediano ocupa el lugar del "decisor" del Teorema de Arrow porque su preferencia siempre gana, **pero NO es un tirano ni un dictador**, ya que su poder proviene únicamente de estar situado en el centro estadístico de las preferencias de los demás ciudadanos.
4. **Ejemplo de clase (Reforma a la Salud en Colombia):** Si cinco congresistas o líderes de opinión se ordenan en un índice unidimensional de control estatal en salud: Rafael Nieto `$(0\%)$`, María Clara Posada `$(30\%)$`, **Jennifer Pedraza `$(50\%)$`**, Andrea Padilla `$(70\%)$` y Carolina Corcho `$(100\%)$`, con preferencias unimodales la propuesta ganadora por mayoría será exactamente el **`$50\%$`** correspondiente a la votante mediana (Jennifer Pedraza).
5. **Limitaciones reales del Votante Mediano:**
   * En la realidad, la mayoría de los problemas políticos son **multidimensionales** (y en múltiples dimensiones reaparecen los ciclos de caos).
   * Además, **la unimodalidad en una dimensión garantiza que exista un ganador de Condorcet por mayoría, pero NO garantiza que otros sistemas de votación (como Borda o Segunda Vuelta) sean inmunes a la manipulación estratégica** si los votantes mienten sobre sus preferencias.


## 3. Mecanismos de Votación y Problemas de Agencia Política

En las democracias representativas rara vez se somete todo a referendo directo (**votación indirecta**), lo que genera un **problema de agencia** entre los ciudadanos (principales) y los políticos (agentes):
* **¿De qué dependen las preferencias de los políticos?** De sus percepciones sobre lo que desea el electorado, su propia concepción del bien público, la presión y financiación de **grupos de interés (*lobby*)** y sus motivaciones personales.
* **El elector como *free-rider* (polizón):** Dado que la probabilidad de que un solo voto individual decida una elección nacional es casi nula, el ciudadano individual tiene incentivos a actuar como *free-rider* (no informarse a fondo o abstenerse).

### Comparación Rigurosa de los Cinco Mecanismos de Votación

| Mecanismo de Votación | Regla Operativa de Conteo | Propiedades, Ventajas y Fallos (Según Arrow) |
| :--- | :--- | :--- |
| **1. Pluralidad** (Simple, Calificada o Absoluta) | Cada votante da **`$1$` punto a su primera opción** y `$0$` a las demás. Gana quien tenga más votos `(o `$\geq 50\%$` / `$\geq 66\%$`)`. | Muy simple, pero incentiva el **voto útil / estratégico** (no sinceridad para evitar que gane la peor opción) y permite que gane un candidato rechazado por la mayoría absoluta. |
| **2. Método de Condorcet** | Elección por mayoría absoluta enfrentando a los candidatos **de dos en dos** `$(A\text{ vs. }B, \; A\text{ vs. }C, \; B\text{ vs. }C)$`. | Elige al candidato que vence a todos los demás mano a mano (**Ganador de Condorcet**). Problema: puede no existir ganador si las preferencias no son unimodales (ciclos). |
| **3. Cuenta de Borda** | Con `$m$` opciones, el votante da **`$m$` puntos a su 1.ª opción, `$m-1$` a la 2.ª, ..., y `$1$` punto a la última**. Gana quien sume más puntos. | Pondera el consenso completo, pero **viola la Independencia de Alternativas Irrelevantes (IIA)**: introducir o retirar opciones irrelevantes altera el ganador inicial, y es altamente manipulable. |
| **4. Approval Voting** (Voto Aprobatorio) | Cada votante da **`$1$` punto a todas las opciones que apruebe** (una o varias) y `$0$` a las que rechaza. Gana quien sume más aprobaciones. | Favorece a candidatos "unificadores" sobre los "polarizadores", reduce campañas negativas y evita que partidos minoritarios actúen como saboteadores (*spoilers*). *(Nota: no garantiza por sí solo que alguien supere el `$50\%+1$` de los votantes si el electorado sólo aprueba de a un candidato).* |
| **5. Segunda Vuelta** (*Runoff Voting*) | Si nadie alcanza mayoría absoluta en 1.ª vuelta, **pasan a 2.ª vuelta los dos más votados** y se elige entre ellos. | Garantiza apoyo mayoritario en el balotaje final, pero **viola la Independencia de Alternativas Irrelevantes (IIA)** (la entrada de un tercer candidato altera quiénes pasan a 2.ª vuelta) y **viola el principio de capacidad de respuesta positiva (monotonicidad)**. |


## 4. Modelo Analítico: Votante Mediano vs. Planificador Social (Gasto Público y Corrupción)

En la Guía de Estudio de Elección Social (Ejercicios 11 y 12), el profesor David Tobón formula un modelo matemático exacto para contrastar la decisión de gasto público bajo democracia mayoritaria (**votante mediano**) frente a la eficiencia social (**planificador de Pareto**).

### Modelo A: Gasto Público Puro sin Corrupción (Ejercicio 11)

En una sociedad de `$n = 53\,000\,000$` habitantes, cada individuo `$i$` tiene un ingreso `$y_i$` y una función de utilidad cuasilineal sobre su consumo privado `$C_i$` y el bien público `$g$`:

$$
\begin{align*}U_i = C_i + \ln(g), \quad \forall i = 1, \ldots, n\end{align*}
$$

El gasto público se financia mediante un impuesto proporcional `$t \in (0, 1)$` sobre el ingreso de cada persona:

$$
\begin{align*}g = \sum_{i=1}^n t \cdot y_i = t \sum_{i=1}^n y_i = t (n \bar{Y}) \implies \boxed{t = \frac{g}{n \bar{Y}}}\end{align*}
$$

donde `$\bar{Y} = \frac{1}{n}\sum_{i=1}^n y_i = 6\,850\text{ USD}$` es el **ingreso promedio (PIB per cápita)**, mientras que el ingreso del **colombiano mediano** es `$Y_M = 600\text{ USD}$`.

Como el consumo privado del individuo `$i$` después de impuestos es `$C_i = (1 - t) y_i = y_i - t y_i = y_i - g \left(\frac{y_i}{n \bar{Y}}\right)$`, sustituimos `$C_i$` en su función de utilidad:

$$
\begin{align*}U_i(g) = y_i - g \left( \frac{y_i}{n \bar{Y}} \right) + \ln(g)\end{align*}
$$

1. **Nivel de gasto público `$g_M^*$` deseado por el Votante Mediano `$(y_i = Y_M)$`:**
   Derivamos la utilidad del votante mediano respecto a `$g$` e igualamos a cero:

   $$
   \begin{align*}\frac{\partial U_M}{\partial g} = -\frac{Y_M}{n \bar{Y}} + \frac{1}{g} = 0 \implies \boxed{g_M^* = n \left( \frac{\bar{Y}}{Y_M} \right)}\end{align*}
   $$

   Con `$Y_M = 600$` y `$\bar{Y} = 6\,850$`, el cociente de asimetría distributiva es `$\frac{\bar{Y}}{Y_M} = \frac{6\,850}{600} \approx 11.4167$`, por lo que `$g_M^* = 53\,000\,000 \times \frac{6\,850}{600} \approx 605\,083\,333.33\text{ USD}$` `(o en términos per cápita, `$\frac{g_M^*}{n} = \frac{\bar{Y}}{Y_M} = 11.42\text{ USD}$`)`.

2. **Nivel de gasto público `$g_{PO}^*$` Pareto Óptimo (Socialmente Deseado):**
   Un planificador social utilitarista maximiza la suma de las utilidades de todos los `$n$` ciudadanos `$(W = \sum_{i=1}^n U_i)$`:

   $$
   \begin{align*}\max_{\{g\}} \quad W = \sum_{i=1}^n \left[ y_i - g \left( \frac{y_i}{n \bar{Y}} \right) + \ln(g) \right] = n \bar{Y} - g \underbrace{\left( \frac{\sum_{i=1}^n y_i}{n \bar{Y}} \right)}_{= 1} + n \ln(g) = n \bar{Y} - g + n \ln(g)\end{align*}
   $$

   Derivando `$W$` respecto a `$g$` e igualando a cero (Condición de Samuelson):

$$
\begin{align*}\frac{\text{d}W}{\text{d}g} = -1 + \frac{n}{g} = 0 \implies \boxed{g_{PO}^* = n = 53\,000\,000\text{ USD}} \quad \left(\text{es decir, } \frac{g_{PO}^*}{n} = 1\text{ USD per cápita}\right)\end{align*}
$$

> **Interpretación económica profunda:** Como en países desiguales el ingreso mediano es mucho menor que el ingreso promedio `$(Y_M = 600 \ll \bar{Y} = 6\,850)$`, el precio fiscal que paga el votante mediano por cada peso de gasto público `$\left(\frac{Y_M}{n \bar{Y}}\right)$` es muy bajo (los ricos pagan la mayor parte de la factura tributaria). Por eso **el votante mediano demanda un gasto público `$11.42$` veces mayor que el nivel Pareto eficiente `$(g_M^* > g_{PO}^*)$`**, y a medida que aumenta el ingreso del votante mediano `$Y_M$`, su demanda de gasto público `$g_M^*$` **disminuye** `$\left(\frac{\partial g_M^*}{\partial Y_M} < 0\right)$`.

### Modelo B: Gasto Público y Corrupción Política `$K$` (Ejercicio 12)

Ahora supongamos que el recaudo tributario total se reparte entre el gasto público productivo `$g$` y la parte `$K$` que se apropian los hacedores de política (**corrupción**):

$$
\begin{align*}g + K = \sum_{i=1}^n t \cdot y_i = t (n \bar{Y}) \implies t = \frac{g + K}{n \bar{Y}}\end{align*}
$$

La función de utilidad incorpora una valoración de raíz cuadrada por el bien público `$(2\sqrt{g})$` y una desutilidad cuadrática por la corrupción `$\left(-\frac{K^2}{2}\right)$`:

$$
\begin{align*}U_i = C_i + 2\sqrt{g} - \frac{K^2}{2} = y_i - (g + K)\left( \frac{y_i}{n \bar{Y}} \right) + 2 g^{1/2} - \frac{K^2}{2}\end{align*}
$$

1. **Elección del Votante Mediano `$(y_i = Y_M)$`:**
   * Respecto a `$g$`:

   $$
   \begin{align*}\frac{\partial U_M}{\partial g} = -\frac{Y_M}{n \bar{Y}} + g^{-1/2} = 0 \implies \sqrt{g_M^*} = \frac{n \bar{Y}}{Y_M} \implies \boxed{g_M^* = \left( \frac{n \bar{Y}}{Y_M} \right)^2}\end{align*}
   $$

   * Respecto a la corrupción `$K$` `(sujeto a `$K \geq 0$`)`:

$$
\begin{align*}\frac{\partial U_M}{\partial K} = -\frac{Y_M}{n \bar{Y}} - K < 0, \quad \forall K \geq 0 \implies \boxed{K_M^* = 0}\end{align*}
$$

2. **Elección del Planificador Social `$(W = \sum_{i=1}^n U_i = n\bar{Y} - (g + K) + 2n\sqrt{g} - n\frac{K^2}{2})$`:**
   * Respecto a `$g$`:

   $$
   \begin{align*}\frac{\partial W}{\partial g} = -1 + n g^{-1/2} = 0 \implies \boxed{g_{PO}^* = n^2}\end{align*}
   $$

   * Respecto a `$K$`: `$\frac{\partial W}{\partial K} = -1 - n K < 0 \implies \boxed{K_{PO}^* = 0}$`. Tanto el votante mediano como la sociedad desean **cero corrupción `$(K^* = 0)$`**, pero si `$K$` representara un bien con beneficio marginal positivo decreciente, el costo marginal tributario percibido por el votante mediano seguiría siendo menor que el costo social cuando `$Y_M < \bar{Y}$`.


## 5. Funciones Sociales de Bienestar y Criterios de Justicia Distributiva

Si asumimos que es posible comparar las utilidades de las personas `$(U_1, U_2, \ldots, U_n)$`, podemos pasar de la Caja de Edgeworth (espacio de bienes) a la **Frontera de Posibilidades de Utilidad `$(O_S - O_J)$`** en el espacio de utilidades `$(U_S, U_J)$`.

Estar sobre la frontera `$O_S - O_J$` (eficiencia de Pareto) es **necesario pero no suficiente** para un óptimo social. Para elegir un punto específico sobre la frontera necesitamos una **Función de Bienestar Social `$W = W(U_1, U_2, \ldots, U_n)$`** creciente en la utilidad de cada persona:

| Criterio / Función de Bienestar | Expresión Matemática / Regla | Filosofía Distributiva y Propiedades |
| :--- | :--- | :--- |
| **1. Utilitarista Clásica (Benthamita)** | `$W(U_1, \ldots, U_n) = \sum_{i=1}^n U_i$` | *"La mayor felicidad para el mayor número de personas"*. Las curvas de isobienestar social son rectas con pendiente `$-1$`; es indiferente a la desigualdad extrema mientras la suma sea máxima. |
| **2. Bergson–Samuelson (Multiplicativa / Cobb-Douglas)** | `$W = W(U_1, \ldots, U_n)$`, ej.: `$W = U_1^{\alpha_1} U_2^{\alpha_2}$` | Curvas de isobienestar social estrictamente convexas al origen: pondera simultáneamente **eficiencia y equidad** (penaliza asignaciones extremas donde un agente tiene utilidad cercana a cero). |
| **3. Rawlsiana (Maximin — John Rawls)** | `$W(U_1, \ldots, U_n) = \min\{U_1, U_2, \ldots, U_n\}$` | El bienestar social depende exclusivamente del **individuo que se encuentra en la peor situación**. Emerge bajo el **velo de la ignorancia** `(curvas de isobienestar en forma de "L" sobre el rayo de `$45^\circ$` donde `$U_1 = U_2$`)`. |
| **4. Función Nietzscheana (Maximax)** | `$W(U_1, \ldots, U_n) = \max\{U_1, U_2, \ldots, U_n\}$` | El bienestar de una sociedad se mide únicamente por la utilidad alcanzada por su individuo más sobresaliente o mejor situado. |
| **5. Criterio Procesal de Robert Nozick** | Evaluación histórica / procesal | Rechaza las funciones de resultado final: el bienestar se evalúa por el **respeto a la situación inicial (propiedad legítima) y la voluntariedad del proceso de intercambio**, no por el resultado distributivo final. |
| **6. Criterio de Equidad de Hal Varian** | **Justicia = Eficiencia + Ausencia de Envidia** | Una asignación es **equitativa** si es **libre de envidias** `(ningún agente prefiere la canasta del otro sobre la suya propia: `$U_i(x_i) \geq U_i(x_j)$`)`. Si una asignación es **equitativa y eficiente en Pareto**, entonces es **justa**. |

### Epílogo Estratégico: Tabla de Reglas para Vivir (Carl Sagan, *Billones y billones*)

El curso cierra conectando la ética social con la **Teoría de Juegos repetidos** (el Dilema del Prisionero de Robert Axelrod citado por Carl Sagan):
* **Regla de Oro:** *Haz a los demás como te agradaría que te hicieran a ti.*
* **Regla de Plata:** *No le hagas a los demás lo que no te gustaría que te hicieran a ti.*
* **Regla de Bronce:** *Haz a los demás como ellos te hacen a ti.*
* **Regla de Hierro:** *Haz a los demás como te plazca, antes que ellos te lo hagan a ti.*
* **Regla Tal para Cual (*Tit for Tat*):** *Empiezas cooperando, y en cada encuentro subsecuente simplemente haz lo que hizo tu oponente la última vez* (la estrategia evolutivamente más robusta en el Dilema del Prisionero iterado).

<figure class="eco-figure">
  <img src="/assets/figures/micro2/fpu-optimo-light.svg" alt="Frontera de utilidad cóncava con rayo igualitario, punto utilitarista y tangencia con isobienestar social." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/fpu-optimo-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la frontera dice qué se puede; la función de bienestar elige el punto.</figcaption>
</figure>


<IdeaClave>

Si las preferencias tienen un solo pico, el votante mediano decide; el gasto público óptimo sale de comparar beneficios con impuestos.

</IdeaClave>
