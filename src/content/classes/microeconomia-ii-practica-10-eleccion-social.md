---
title: "Práctica 01B: Elección Social y Votación"
course: "microeconomia-ii"
order: 10
classType: "practica"
description: "Bloque III más taller de votación: mecanismos, Condorcet, IIA y voto estratégico."
math: true
conceptos: ["Votación por mayoría", "Independencia de alternativas irrelevantes", "Manipulación estratégica"]
---
## Lista de ejercicios

### Bloque III: Elección Social, Votaciones y Votante Mediano (Guía de Elección Social, Ejercicios 1 a 12)

8.  **Preguntas Teóricas y Conceptuales sobre Arrow, Black y Sistemas Electorales (Guía Elección Social, P1 a P6):**
    * **a)** *(P1)* ¿Cuándo se pueden eludir las implicaciones del Teorema de la Imposibilidad de Arrow entre las opciones dadas (`a` a `f`), y por qué son necesarias **ambas** condiciones del Teorema de Black?
    * **b)** *(P2 y P3)* Evalúe con V, F o I: (P2) *"Se puede garantizar que las preferencias son no manipulables cuando las cuestiones sobre las que se vota son unidimensionales"*; y (P3) *"Si las preferencias son unimodales y las opciones unidimensionales, los mecanismos de decisión social pueden llevar a soluciones no dictatoriales"*.
    * **c)** *(P4 y P5)* Evalúe con V, F o I: (P4) *"En Colombia se elige el presidente usando el mecanismo de segunda vuelta, porque ésta blinda la elección de la alteración de la decisión social sobre las opciones iniciales al aparecer opciones irrelevantes"*; y (P5) *"Si los candidatos a la alcaldía de Medellín se pueden ordenar en función de su perfil ideológico basta con aplicar el mecanismo de Approval voting para garantizar que el elegido obtenga una votación mayor al 50%+1"*.
    * **d)** *(P6)* Articule la cita de Adam Smith sobre la Mano Invisible y el político presuntuoso utilizando simultáneamente la teoría del equilibrio general y la teoría de la elección social.

9.  **Estabilidad de Afinidades Electivas (Guía Elección Social, Ejercicio 7):**
    Analice el siguiente sistema de preferencias entre tres parejas actualmente conformadas (**Pareja 1:** Luisa y Luis; **Pareja 2:** Fer y Fercho; **Pareja 3:** Ana y Ananías) y determine formalmente si es estable o inestable (identificando todas las parejas bloqueadoras):

    | Orden | Pareja 1: Luisa | Pareja 1: Luis | Pareja 2: Fer | Pareja 2: Fercho | Pareja 3: Ana | Pareja 3: Ananías |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **1.º** | Ananías | Luisa | Luis | Fer | Fercho | Fer |
    | **2.º** | Fercho | Fer | Ananías | Luisa | Luis | Luisa |
    | **3.º** | Luis | Ana | Fercho | Ana | Ananías | Ana |

10. **Transferencias de EPM en el Concejo de Medellín (Guía Elección Social, Ejercicio 8):**
    El Concejo de Medellín tiene `$23$` representantes que deben decidir entre tres sistemas de transferencias de EPM al municipio, ordenados de menor a mayor porcentaje de transferencia:
    * **Conservador `$(C)$`:** Mantener el tradicional `$(38\%\text{ de las utilidades})$`.
    * **Razonable `$(R)$`:** Mantener el `$38\%$` y permitir transferencias extraordinarias según indicadores de solvencia.
    * **Social `$(S)$`:** Volver permanentes las transferencias extraordinarias `(subir al `$50\%$`)`.

    El perfil de preferencias de los `$23$` concejales es:
    * `$7$` concejales: `$R \succ C \succ S$`.
    * `$7$` concejales: `$S \succ R \succ C$`.
    * `$9$` concejales: `$C \succ S \succ R$`.

    * **a)** ¿Son consistentes las preferencias sociales bajo votación mayoritaria por pares (Condorcet) o existe un ciclo? Identifique cuál de los tres grupos de concejales **no tiene preferencias unimodales** en el eje `$C - R - S$`.
    * **b)** Proponga la reordenación unimodal para dicho grupo y determine la preferencia social antes y después de la corrección usando **Mayoría (Pluralidad)**, **Condorcet** y **Cuenta de Borda**.

11. **Elección de Vacaciones de los 27 Estudiantes y Elecciones Presidenciales (Guía Elección Social, Ejercicios 9 y 10):**
    * **a)** *(Ejercicio 9)* En un salón hay `$27$` estudiantes divididos en tres grupos de tamaño `$11$`, `$9$` y `$7$`, quienes eligen entre 4 destinos para vacaciones: **Bogotá `$(B)$`**, **Mar `$(M)$`**, **Montañas `$(Mo)$`** y **Llanos `$(Ll)$`**:
      * **Grupo 1 `$(11\text{ estudiantes})$`:** `$B \succ M \succ Mo \succ Ll$`.
      * **Grupo 2 `$(9\text{ estudiantes})$`:** `$M \succ Ll \succ Mo \succ B$`.
      * **Grupo 3 `$(7\text{ estudiantes})$`:** `$Mo \succ B \succ Ll \succ M$`.
      Evalúe si las preferencias son unimodales y aplique paso a paso los criterios de **Condorcet**, **Pluralidad**, **Approval Voting** (aprobando las 2 primeras opciones) y **Cuenta de Borda** `$(4, 3, 2, 1\text{ puntos})$`. ¿Son equivalentes los resultados?
    * **b)** *(Ejercicio 10)* En una elección presidencial entre las candidaturas **Paloma `$(P)$`**, **Cepeda `$(C)$`**, **Tigre `$(T)$`** y **Fajardo `$(F)$`**, los votantes `(en millones, total `$24$` millones)` ordenan sus preferencias así:
      * **Grupo 1 `$(10\text{ millones})$`:** `$T \succ P \succ F \succ C$`.
      * **Grupo 2 `$(11\text{ millones})$`:** `$C \succ F \succ P \succ T$`.
      * **Grupo 3 `$(2\text{ millones})$`:** `$P \succ T \succ F \succ C$`.
      * **Grupo 4 `$(1\text{ millón})$`:** `$F \succ T \succ C \succ P$`.
      Evalúe si las preferencias son unimodales (ordenando el espectro político de derecha a izquierda o viceversa) y determine exactamente quién gana bajo: (1) **Pluralidad**, (2) **Approval Voting** (aprobando las 2 primeras opciones), (3) **Cuenta de Borda**, (4) **Segunda Vuelta** y (5) **Condorcet**.

12. **Votante Mediano vs. Óptimo de Pareto: Gasto Público y Corrupción en Colombia (Guía Elección Social, Ejercicios 11 y 12):**
    Considere una economía de `$n = 53\,000\,000$` habitantes donde el ingreso mensual del votante mediano es `$Y_M = 600\text{ USD}$` y el PIB per cápita mensual promedio es `$\bar{Y} = 6\,850\text{ USD}$`. El presupuesto público se financia con un impuesto proporcional `$t$` sobre el ingreso `$y_i$`.
    * **a)** *(Ejercicio 11)* Con `$U_i = C_i + \ln(g)$` y `$g = \sum_{i=1}^n t y_i$`, calcule numérica y analíticamente el gasto público deseado por el votante mediano `$(g_M^*)$` y el gasto público Pareto óptimo `$(g_{PO}^*)$`.
    * **b)** *(Ejercicio 12)* Con `$U_i = C_i + 2\sqrt{g} - \frac{K^2}{2}$` y `$g + K = \sum_{i=1}^n t y_i$`, encuentre los niveles de `$g$` y `$K$` deseados por el votante mediano y por el planificador social, y responda con V, F o I las preguntas `12c`, `12d` y `12e`.




## Solucionario y Guía Analítica Paso a Paso

### Solución Ejercicio 8: Preguntas Conceptuales de Elección Social (Guía Elección Social, P1–P6)

* **a) Pregunta 1:** Si se evalúan las opciones una por una por separado, la respuesta estricta es **`b. Se acepta que las preferencias sociales son manipulables`** (al relajar IIA) o **`f. Ninguna`** (porque para el Teorema de Black no basta `d` sola ni `e` sola: se requiere la **conjunción simultánea de `d` y `e`**, es decir, que las cuestiones sean unidimensionales **y** las preferencias sean unimodales).
* **b) Pregunta 2 — FALSO:** La unidimensionalidad sola no impide ni los ciclos ni la manipulación estratégica (Teorema de Gibbard-Satterthwaite). **Pregunta 3 — VERDADERO:** Es exactamente el **Teorema de Black** (el equilibrio por mayoría coincide con el votante mediano, que no es un dictador).
* **c) Pregunta 4 — FALSO:** La segunda vuelta **NO** blinda la elección frente a alternativas irrelevantes (viola el axioma IIA de Arrow: la entrada de un tercer candidato altera quiénes pasan al balotaje). **Pregunta 5 — FALSO:** En *Approval voting* cada votante aprueba tantas opciones como desee, por lo que no está garantizado que el ganador supere el `$50\% + 1$` de los votantes (por ejemplo, si todos aprueban un solo candidato, es idéntico a pluralidad simple).
* **d) Pregunta 6 (Ensayo corto sobre Adam Smith):** Véase la guía en 4 pasos desarrollada en la **Clase 01**, contrastando la eficiencia del Primer Teorema del Bienestar en mercados privados frente a los problemas de información dispersa, agencia política, buscadores de rentas y Teorema de Arrow cuando un político pretende sustituir al mercado.


### Solución Ejercicio 9: Afinidades Electivas (Guía Elección Social, Ejercicio 7)

Analizamos las tres parejas actuales (**P1:** Luisa–Luis; **P2:** Fer–Fercho; **P3:** Ana–Ananías):
* **Luisa** tiene a Luis en su **3.er (último) lugar**: ella prefiere tanto a **Ananías (1.º)** como a **Fercho (2.º)**.
* Miremos qué piensa **Ananías** de Luisa: Ananías está actualmente con Ana (que es su **3.ª y última opción**), y tiene a **Luisa en 2.º lugar** `$( \text{Luisa} \succ_{\text{Ananías}} \text{Ana} )$`.
  * **¡Primera pareja bloqueadora: Luisa y Ananías!** Ambos se prefieren mutuamente por encima de sus parejas actuales `$( \text{Ananías} \succ_{\text{Luisa}} \text{Luis} \text{ y } \text{Luisa} \succ_{\text{Ananías}} \text{Ana} )$`.
* Miremos a **Fer y Ananías**: Fer prefiere a Ananías en 2.º lugar sobre su pareja actual Fercho en 3.er lugar, y Ananías tiene a Fer como su 1.ª opción absoluta, formando una **segunda pareja bloqueadora sumamente fuerte: Fer y Ananías**.
* **Conclusión:** El sistema de parejas es **inestable**.


### Solución Ejercicio 10: Transferencias de EPM en el Concejo de Medellín (Guía Elección Social, Ejercicio 8)

Orden natural unidimensional del monto de transferencias de EPM: **Conservador `$(C = 38\%)$` `$<$ Razonable `$(R = 38\% + \text{extra})$` $<$ Social `$(S = 50\%)$`**.
Perfil de los `$23$` concejales:
* Grupo 1 `$(7\text{ concejales})$`: `$R \succ C \succ S$` `(Unimodal con pico en `$R$`)`.
* Grupo 2 `$(7\text{ concejales})$`: `$S \succ R \succ C$` `(Unimodal con pico en `$S$`)`.
* Grupo 3 `$(9\text{ concejales})$`: **`$C \succ S \succ R$`** `(**NO unimodal**: tiene pico en el extremo bajo `$C$`, pero prefiere el extremo opuesto `$S$` antes que la opción intermedia `$R$`)`.

* **a) Inconsistencia (Ciclo de Condorcet) con el perfil original:**
  * **`$C$` vs. `$S$`:** Gana **`$C$`** por `$7 + 9 = 16$` votos contra `$7$` `$(C \succ_M S)$`.
  * **`$S$` vs. `$R$`:** Gana **`$S$`** por `$7 + 9 = 16$` votos contra `$7$` `$(S \succ_M R)$`.
  * **`$R$` vs. `$C$`:** Gana **`$R$`** por `$7 + 7 = 14$` votos contra `$9$` `$(R \succ_M C)$`.
  * Hay un **ciclo intransitivo**: `$R \succ_M C \succ_M S \succ_M R$`.
  * **Bajo Pluralidad simple (perfil original):** Gana **`$C$`** con `$9$` votos `(frente a `$7$` de `$R$` y `$7$` de `$S$`)`.
  * **Bajo Cuenta de Borda `$(3, 2, 1\text{ puntos, perfil original})$`:**
    * `$P(C) = 7(2) + 7(1) + 9(3) = 14 + 7 + 27 = \mathbf{48}\text{ puntos}$`.
    * `$P(R) = 7(3) + 7(2) + 9(1) = 21 + 14 + 9 = 44\text{ puntos}$`.
    * `$P(S) = 7(1) + 7(3) + 9(2) = 7 + 21 + 18 = 46\text{ puntos}$`.
    * Gana **`$C$`** con `$48$` puntos.

* **b) Reordenación unimodal del Grupo 3 `$(9\text{ concejales pasan a } C \succ R \succ S)$`:**
  Si los `$9$` concejales conservadores ordenan unimodalmente según la cercanía a `$C$` (**`$C \succ R \succ S$`**):
  * **Por Condorcet (Mayoría por pares):** **`$R$`** (la opción del votante mediano) vence a `$C$` por `$14$` a `$9$` y vence a `$S$` por `$16$` a `$7$`. **Gana `$R$` (Ganador de Condorcet)**.
  * **Por Cuenta de Borda corregida:** `$P(R) = 7(3) + 7(2) + 9(2) = \mathbf{53}\text{ puntos}$`, superando a `$C$` `$(48)$` y a `$S$` `$(37)$`. **Gana `$R$`**, que es la opción técnica y financieramente más conveniente al combinar transferencias con criterios de solvencia de EPM.


### Solución Ejercicio 11: los 27 Estudiantes y las Elecciones Presidenciales (Guía Elección Social, Ejercicios 9 y 10)

* **a) Vacaciones de los 27 estudiantes (Ejercicio 9):**
  * **¿Son unimodales?** No existe ningún orden lineal de los 4 destinos en el que los tres grupos sean simultáneamente unimodales `(por ejemplo, el Grupo 1 tiene en los extremos a `$B$` y `$Ll$`, el Grupo 2 tiene en los extremos a `$M$` y `$B$`, y el Grupo 3 tiene en los extremos a `$Mo$` y `$M$`)`.
  * **1. Pluralidad (1.ª opción):** **Bogotá `$(B)$`** = `$11$` votos; **Mar `$(M)$`** = `$9$`; **Montañas `$(Mo)$`** = `$7$`; **Llanos `$(Ll)$`** = `$0$`. **Gana Bogotá `$(11\text{ votos})$`**.
  * **2. Condorcet `(Mayoría absoluta = `$14$` de `$27$` votos)`:**
    * `$B$` vs. `$M$`: Grupo 1 `$(11)$` y Grupo 3 `$(7)$` prefieren `$B \succ M \implies$` **`$B$` gana `$18$` a `$9$`** `$(B \succ M)$`.
    * `$M$` vs. `$Mo$`: Grupo 1 `$(11)$` y Grupo 2 `$(9)$` prefieren `$M \succ Mo \implies$` **`$M$` gana `$20$` a `$7$`** `$(M \succ Mo)$`.
    * `$Mo$` vs. `$B$`: Grupo 2 `$(9)$` y Grupo 3 `$(7)$` prefieren `$Mo \succ B \implies$` **`$Mo$` gana `$16$` a `$11$`** `$(Mo \succ B)$`.
    * `(Todas vencen a Llanos `$Ll$`)`. **No hay ganador de Condorcet**: existe un ciclo en el tope **`$B \succ M \succ Mo \succ B$**.
  * **3. Cuenta de Borda `$(4, 3, 2, 1\text{ puntos})$`:**
    * **`$B$`:** `$11(4) + 9(1) + 7(3) = 44 + 9 + 21 = \mathbf{74}\text{ puntos}$`.
    * **`$M$`:** `$11(3) + 9(4) + 7(1) = 33 + 36 + 7 = \mathbf{76}\text{ puntos}$`.
    * **`$Mo$`:** `$11(2) + 9(2) + 7(4) = 22 + 18 + 28 = 68\text{ puntos}$`.
    * **`$Ll$`:** `$11(1) + 9(3) + 7(2) = 11 + 27 + 14 = 52\text{ puntos}$`.
    * **Gana el Mar `$(M)$` con `$76$` puntos**.
  * **4. Approval Voting (aprobando las 2 primeras opciones de cada grupo):**
    * **`$M$`:** Aprobado por Grupo 1 `$(11)$` + Grupo 2 `$(9)$` = **`$20$` votos**.
    * **`$B$`:** Aprobado por Grupo 1 `$(11)$` + Grupo 3 `$(7)$` = **`$18$` votos**.
    * **`$Ll$`:** Aprobado por Grupo 2 `$(9)$` = `$9$` votos.
    * **`$Mo$`:** Aprobado por Grupo 3 `$(7)$` = `$7$` votos.
    * **Gana el Mar `$(M)$` con `$20$` votos**. Los métodos **no son equivalentes** (Pluralidad elige Bogotá, Condorcet cicla, y Borda y Approval eligen el Mar).

* **b) Elecciones Presidenciales en Colombia: `$P, C, T, F$` `(Ejercicio 10, total `$24$` millones de votos)`:**
  * **¿Son unimodales las preferencias?** Si ordenamos a los candidatos en el espectro ideológico como **`$C - F - P - T$`** `(o de derecha a izquierda **`$T - P - F - C$`)`:
    * Grupo 1 `$(10\text{ M}, \; T \succ P \succ F \succ C)$`: **Unimodal** `(pico en `$T$`, cae monótonamente hacia `$C$`)`.
    * Grupo 2 `$(11\text{ M}, \; C \succ F \succ P \succ T)$`: **Unimodal** `(pico en `$C$`, cae monótonamente hacia `$T$`)`.
    * Grupo 3 `$(2\text{ M}, \; P \succ T \succ F \succ C)$`: **Unimodal** `(pico en `$P$`, cae hacia ambos lados `$T$` y `$F \to C$`)`.
    * Grupo 4 `$(1\text{ M}, \; F \succ T \succ C \succ P)$`: **NO es unimodal** en el orden `$T - P - F - C$` `(su pico está en `$F$`, pero salta al extremo `$T$` y al otro extremo `$C$` dejando en último lugar a su vecino contiguo `$P$`)`.
  * **1. Pluralidad simple (1.ª vuelta):**
    * **Cepeda `$(C)$`** = **`$11\text{ millones}$`** (Gana por pluralidad simple).
    * **Tigre `$(T)$`** = `$10\text{ millones}$`.
    * **Paloma `$(P)$`** = `$2\text{ millones}$`.
    * **Fajardo `$(F)$`** = `$1\text{ millón}$`.
  * **2. Segunda Vuelta `(pasan los dos más votados: `$C$` con `$11\text{ M}$` y `$T$` con `$10\text{ M}$`)`:**
    * Votan por **`$T$`**: Grupo 1 `$(10\text{ M})$` + Grupo 3 `$(2\text{ M}, \text{ pues } T \succ C)$` + Grupo 4 `$(1\text{ M}, \text{ pues } T \succ C)$` = **`$13\text{ millones}$`**.
    * Votan por **`$C$`**: Grupo 2 = **`$11\text{ millones}$`**.
    * **Gana Tigre `$(T)$` en Segunda Vuelta `$(13\text{ M a }11\text{ M})$`**.
  * **3. Cuenta de Borda `$(4, 3, 2, 1\text{ puntos por millón de votos})$`:**
    * **`$P$`:** `$10(3) + 11(2) + 2(4) + 1(1) = 30 + 22 + 8 + 1 = \mathbf{61}\text{ millones de puntos}$`.
    * **`$T$`:** `$10(4) + 11(1) + 2(3) + 1(3) = 40 + 11 + 6 + 3 = 60\text{ millones de puntos}$`.
    * **`$F$`:** `$10(2) + 11(3) + 2(2) + 1(4) = 20 + 33 + 4 + 4 = \mathbf{61}\text{ millones de puntos}$`.
    * **`$C$`:** `$10(1) + 11(4) + 2(1) + 1(2) = 10 + 44 + 2 + 2 = 58\text{ millones de puntos}$`.
    * **Empate en el primer lugar bajo Borda entre Paloma `$(P)$` y Fajardo `$(F)$` con `$61$` puntos**, seguidos por `$T$` `$(60)$` y `$C$` `$(58)$`.
  * **4. Approval Voting (aprobando las 2 primeras opciones de cada votante):**
    * **`$T$`:** Grupo 1 `$(10\text{ M})$` + Grupo 3 `$(2\text{ M})$` + Grupo 4 `$(1\text{ M})$` = **`$13\text{ millones de aprobaciones}$`**.
    * **`$P$`:** Grupo 1 `$(10\text{ M})$` + Grupo 3 `$(2\text{ M})$` = `$12\text{ millones}$`.
    * **`$F$`:** Grupo 2 `$(11\text{ M})$` + Grupo 4 `$(1\text{ M})$` = `$12\text{ millones}$`.
    * **`$C$`:** Grupo 2 `$(11\text{ M})$` = `$11\text{ millones}$`.
    * **Gana Tigre `$(T)$` con `$13\text{ millones}$` de aprobaciones**.


### Solución Ejercicio 12: Gasto Público y Corrupción (Guía Elección Social, Ejercicios 11 y 12)

Con `$n = 53\,000\,000$`, `$Y_M = 600\text{ USD}$` y `$\bar{Y} = 6\,850\text{ USD}$` (desarrollo algebraico completo en la **Clase 08, Sección 4**):
* **Ejercicio 11:**
  * **a) Gasto deseado por el votante mediano:** `$g_M^* = n \left(\frac{\bar{Y}}{Y_M}\right) = 53\,000\,000 \times \frac{6\,850}{600} \approx \mathbf{605\,083\,333.33\text{ USD}}$` `$(11.42\text{ USD per cápita})$`.
  * **b) Gasto Pareto óptimo:** `$g_{PO}^* = n = \mathbf{53\,000\,000\text{ USD}}$` `$(1\text{ USD per cápita})$`.
* **Ejercicio 12:**
  * **a) Votante mediano:** `$g_M^* = \left(\frac{n \bar{Y}}{Y_M}\right)^2 = \left(53\,000\,000 \times \frac{6\,850}{600}\right)^2 \approx 3.66 \times 10^{17}\text{ USD}$`, y corrupción deseada **`$K_M^* = 0$`**.
  * **b) Planificador social:** `$g_{PO}^* = n^2 = (53\,000\,000)^2 = 2.809 \times 10^{15}\text{ USD}$`, y corrupción deseada **`$K_{PO}^* = 0$`**.
  * **c) ¿A medida que aumenta el ingreso del votante mediano `$Y_M$` prefiere un mayor `$g$`? — FALSO:** Como `$g_M^* = \left(\frac{n\bar{Y}}{Y_M}\right)^2$`, se cumple que `$\frac{\partial g_M^*}{\partial Y_M} < 0$` (al subir su ingreso, el votante mediano paga una tajada mayor de impuestos y modera su demanda de gasto público).
  * **d) ¿A medida que aumenta el ingreso del votante mediano disminuye su preferencia por `$K$`? — VERDADERO / INCIERTO:** Su desutilidad marginal por peso de corrupción es `$-\frac{Y_M}{n\bar{Y}} - K$`, la cual se vuelve **aún más negativa** cuando sube `$Y_M$` `(rechaza con más fuerza la corrupción porque le cuesta más impuestos, aunque en niveles reales `$K_M^* = 0$` permanece en la esquina cero)`.
  * **e) ¿La preferencia social por la corrupción es menor que la del votante mediano? — VERDADERO `(en costo marginal cuando `$Y_M < \bar{Y}$`)` / IGUAL EN CERO:** Como `$Y_M = 600 < \bar{Y} = 6\,850$`, el costo marginal tributario de `$K$` para toda la sociedad `$(1 + nK)$` es mayor que el costo marginal percibido por el votante mediano `$\left(\frac{Y_M}{n\bar{Y}} + K\right)$`, si bien ambos eligen la esquina `$K^* = 0$`.

## Del Taller de Votación: La Facultad y el Fondo Extraordinario

La Facultad debe escoger una de cuatro alternativas para destinar un fondo extraordinario:

* **A**: becas de sostenimiento.
* **B**: fortalecimiento académico y monitorías.
* **C**: bienestar y salud mental.
* **D**: deporte, cultura y espacios de encuentro.

Las preferencias de 25 representantes estudiantiles son:

| N.º de votantes | Orden de preferencias |
| :--- | :--- |
| 8 | $A > B > C > D$ |
| 7 | $B > C > D > A$ |
| 6 | $C > D > B > A$ |
| 4 | $D > C > B > A$ |

### V1. Ganadores por Mecanismo

Calcule el ganador con cada regla y verifique:

| Mecanismo | Ganador | Resultado principal |
| :--- | :--- | :--- |
| Pluralidad | **A** | A obtiene 8 primeros lugares. |
| Condorcet | **B** | B derrota a todas las alternativas por parejas ($17$-$8$). |
| Borda | **C** | C obtiene 73 puntos. |
| Aprobación | **C** | C recibe 17 aprobaciones. |
| Segunda vuelta | **B** | B derrota a A por 17 votos contra 8. |

Concluya: las preferencias individuales permanecen iguales, pero **el ganador cambia con la regla electoral**; el procedimiento de agregación no es neutral.

### V2. Alternativa Irrelevante (IIA)

Suponga que la opción $D$ no puede ejecutarse y se retira. Recalcule únicamente Borda, asignando ahora $3$, $2$ y $1$ puntos. Ahora gana **B**, aunque antes $C$ superaba a $B$. La eliminación de $D$ alteró la relación social entre $B$ y $C$: violación directa de la **independencia de alternativas irrelevantes**.

### V3. Voto Estratégico (No Sinceridad)

Bajo pluralidad gana $A$. Si los cuatro votantes que prefieren $D$ anticipan que $D$ no tiene posibilidades, ¿tendrían incentivos a votar estratégicamente por $C$? Sí: si lo hacen, $C$ obtiene diez votos y derrota a $A$. Estos electores prefieren $C$ antes que $A$, por lo cual tienen incentivos a **no votar sinceramente** por su primera opción.

### V4. Recomiende un Mecanismo y Defiéndalo

Proponga una regla y defiéndala empleando al menos dos de estos criterios: respeto por las primeras preferencias; existencia de un ganador de Condorcet; resistencia a la manipulación; independencia de alternativas irrelevantes; facilidad de aplicación; intensidad o amplitud del apoyo.
