---
title: "Clase 14: Elección bajo riesgo, utilidad esperada y modelo CAPM"
course: "microeconomia-ii"
order: 14
classType: "clase"
description: "Teoría de la elección bajo riesgo: loterías, paradoja de San Petersburgo, utilidad esperada de von Neumann-Morgenstern, medidas de Arrow-Pratt, seguros, modelo media-varianza, CAPM y paradojas conductuales."
math: true
---

## Motivación: del mundo determinista a las decisiones contingentes

Hasta ahora, en el análisis del consumidor y del equilibrio general, hemos supuesto que los agentes eligen cestas de bienes con **certeza absoluta**: si el consumidor compra un bien `$x$` al precio `$P_x$`, obtiene con probabilidad `$1$` la utilidad `$U(x)$`. Sin embargo, la mayoría de las decisiones económicas relevantes ocurren en un entorno de **incertidumbre o riesgo**: el estado futuro de la salud, el rendimiento de un activo financiero, estudiar una carrera universitaria, aceptar un empleo o realizar una inversión productiva.

Frente al riesgo, tanto las personas como las empresas despliegan cuatro estrategias fundamentales de administración:

1. **Retener el riesgo:** asumir internamente las posibles pérdidas sin contratar cobertura (no hacer nada).
2. **Evitar el riesgo:** abstenerse de realizar la actividad que genera exposición a la pérdida.
3. **Prevenir el riesgo:** realizar esfuerzos o inversiones preventivas que reduzcan la probabilidad de ocurrencia del siniestro o la magnitud del daño.
4. **Gestionar y transferir el riesgo:** trasladar la exposición a otros agentes dispuestos a asumirla a cambio de una prima o precio, mediante mercados de seguros, instituciones financieras, bolsas de valores o fondos mutuos.

Para modelar formalmente cómo deciden los agentes racionales en estos escenarios, debemos extender la teoría del consumidor hacia el **consumo contingente** y las **loterías**.

---

## 1. Consumo contingente y loterías

Cuando el futuro es incierto, al consumidor le interesa conocer la **distribución de probabilidades** asociada a las distintas cestas de bienes que podría obtener según ocurra un acontecimiento aleatorio u otro.

### 1.1 Probabilidad, estados de la naturaleza y consumo contingente

* **Probabilidad frecuentista u objetiva:** en términos generales, la probabilidad de que un hecho ocurra se interpreta como la frecuencia relativa y condicionada con la que se produce en repeticiones independientes. Por ejemplo:
  * Al lanzar una moneda equilibrada al aire, la probabilidad de obtener cara o sello es `$\frac{1}{2}$`.
  * Al lanzar un dado equilibrado, la probabilidad de obtener cualquiera de sus seis caras es `$\frac{1}{6}$`.
  * Eventos económicos agregados: la probabilidad de que la tasa de cambio supere los `$4.000\text{ COP}$` en enero, o la probabilidad de que cesen los atentados contra la infraestructura pública.
* **Probabilidad compuesta (lotería reducida):** cuando un resultado depende de dos o más eventos aleatorios secuenciales (por ejemplo, al comprar un billete de lotería interesan dos eventos: extraer el número elegido y extraer la serie elegida), el agente evalúa la **probabilidad reducida** multiplicando o componiendo las probabilidades condicionales.
* **Estados de la naturaleza y plan de consumo contingente:** llamamos *estados de la naturaleza* a los posibles resultados mutuamente excluyentes de un acontecimiento aleatorio (por ejemplo, ocurre un siniestro o no ocurre). Un **plan de consumo contingente** especifica exactamente qué cesta de bienes se consumirá en cada uno de los estados de la naturaleza posibles. Como la palabra *contingente* indica dependencia respecto a un evento aún incierto, los individuos tienen preferencias sobre planes de consumo contingentes del mismo modo que tienen preferencias sobre cestas bajo certeza.

### 1.2 Formalización de las loterías monetarias

Para simplificar el análisis, reducimos las cestas de consumo contingente a **loterías monetarias**. Suponemos que las loterías son:
1. **Objetivas:** las probabilidades son conocidas por el decisor y no dependen de creencias subjetivas ambiguas.
2. **Conocidas y monetarias:** cada estado arroja un pago monetario neto bien definido.
3. **Reducidas:** cualquier lotería compuesta ya ha sido simplificada a una única distribución sobre premios finales.

> **Ejemplo intuitivo (Decisión de compra en Medellín):** Suponga que desea comprar una botella de whisky y su disponibilidad máxima a pagar es de `$\$400.000$`. Tiene dos alternativas:
> * **Opción 1 (Almacén Éxito):** el precio es `$\$300.000$` con certeza, por lo que su excedente seguro es `$E_1 = \$100.000$`.
> * **Opción 2 (El Hueco):** existe un `$50\%$` de probabilidad de no encontrar el whisky y tener que llevar ron (con un excedente reducido equivalente a `$5$` unidades), y un `$50\%$` de probabilidad de encontrarlo a `$\$200.000$`, obteniendo un excedente de `$E_{22} = \$200.000$`.
>
> En unidades reducidas (decenas de miles de pesos), estas alternativas se representan como las loterías `$L_1 = (10,\, 1)$` y `$L_2 = (5,\, 0.5;\; 15,\, 0.5)$`, donde el primer componente de cada par indica el pago monetario neto y el segundo su probabilidad de ocurrencia.

---

## 2. Valor esperado y la Paradoja de San Petersburgo

Un primer criterio ingenuo para ordenar loterías consiste en elegir aquella que ofrezca el mayor **valor esperado** monetario.

### 2.1 Definición en el caso discreto y continuo

Sea una lotería que ofrece `$n$` premios distintos `$x_1, x_2, \dots, x_n$` (algunos pueden ser cero o negativos), con probabilidades de ocurrir `$\pi_1, \pi_2, \dots, \pi_n$` tales que `$\pi_i \ge 0$` y `$\sum_{i=1}^{n} \pi_i = 1$`. Suponiendo que al jugador se le entrega un único premio, el **valor esperado** es el promedio ponderado de los pagos:

$$
\begin{align*}
E(x) = \sum_{i=1}^{n} \pi_i x_i
\end{align*}
$$

Si los resultados posibles pertenecen a un continuo, las probabilidades se describen mediante una función de densidad `$f(x)$` tal que `$\int_{-\infty}^{\infty} f(x)\,dx = 1$`, y el valor esperado se define como:

$$
\begin{align*}
E(x) = \int_{-\infty}^{\infty} x f(x)\,dx
\end{align*}
$$

* **Aplicación a un juego justo:** suponga que John y Samara lanzan una moneda equilibrada una sola vez. Si cae cara, John paga `$\$1$` a Samara; si cae sello, Samara paga `$\$1$` a John. Para Samara, los premios son `$x_1 = +\$1$` y `$x_2 = -\$1$` con probabilidad `$\frac{1}{2}$` cada uno:

$$
\begin{align*}
E(x) = \frac{1}{2}(1) + \frac{1}{2}(-1) = 0
\end{align*}
$$

Cuando el juego se repite muchas veces, es poco probable que uno aventaje sistemáticamente al otro en términos esperados.

### 2.2 La Paradoja de San Petersburgo (Bernoulli, 1713)

¿Por qué el criterio del valor esperado falla como regla general de decisión? Considere el célebre juego propuesto por Nicolás Bernoulli y resuelto por Daniel Bernoulli en 1713: se lanza una moneda equilibrada repetidamente hasta que aparezca la primera cara. Si la primera cara aparece en la tirada `$i$`, el jugador recibe un premio de `$x_i = 2^i$` dólares.

* Para `$i = 1$`: `$x_1 = 2$`, con probabilidad `$\pi_1 = \frac{1}{2}$`.
* Para `$i = 2$`: `$x_2 = 4$`, con probabilidad `$\pi_2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$`.
* Para `$i = 3$`: `$x_3 = 8$`, con probabilidad `$\pi_3 = \left(\frac{1}{2}\right)^3 = \frac{1}{8}$`.
* En general, para la tirada `$i$`: `$x_i = 2^i$` con probabilidad `$\pi_i = \left(\frac{1}{2}\right)^i$`.

Calculemos el valor esperado de este juego:

$$
\begin{align*}
E(x) = \sum_{i=1}^{\infty} \pi_i x_i = \sum_{i=1}^{\infty} \left(\frac{1}{2}\right)^i 2^i = \sum_{i=1}^{\infty} 1 = 1 + 1 + 1 + \dots = \infty
\end{align*}
$$

El valor esperado es **infinito**. Según el criterio del valor esperado, una persona debería estar dispuesta a pagar cualquier suma finita —por ejemplo, `$\$1.000.000$` de dólares— por participar en este juego, dado que `$\$1.000.000 \ll \infty$`. Sin embargo, en la realidad casi nadie pagaría siquiera unos pocos dólares por jugarlo.

> **Solución de Bernoulli (1713) e intuición económica:** *"Las personas no valoran el dinero únicamente sobre la base de su valor nominal, sino también sobre la base del valor subjetivo (utilidad) que tiene para ellas."* Si la utilidad de la riqueza crece a tasa decreciente —por ejemplo, `$U(x) = \ln(x)$`—, entonces cada dólar adicional reporta menos satisfacción que el anterior.

Calculando la **utilidad esperada** con `$U(x) = \ln(x)$`:

$$
\begin{align*}
E[U(x)] = \sum_{i=1}^{\infty} \left(\frac{1}{2}\right)^i \ln(2^i) = \ln(2) \sum_{i=1}^{\infty} \frac{i}{2^i} = 2\ln(2) < \infty
\end{align*}
$$

La utilidad esperada es finita y moderada —equivale a un premio seguro de apenas `$\$4$`—, lo cual resuelve la paradoja y da origen a la función de utilidad cardinal bajo riesgo.

---

## 3. Teoría de la Utilidad Esperada de von Neumann-Morgenstern (VNM)

En 1944, John von Neumann y Oskar Morgenstern axiomatizaron el comportamiento racional bajo riesgo, demostrando que si las preferencias sobre loterías cumplen ciertos axiomas básicos, pueden representarse mediante el valor esperado de un índice de utilidad `$U(\cdot)$`:

$$
\begin{align*}
EU(x) &= \sum_{i=1}^{n} \pi_i U(x_i) \quad \text{(caso discreto)} \\
EU(x) &= \int_{-\infty}^{\infty} U(x) f(x)\,dx \quad \text{(caso continuo)}
\end{align*}
$$

### 3.1 Comparación de loterías mediante el índice VNM

Considere un individuo racional que elige entre dos jugadas riesgosas:
* **Jugada 1:** ofrece `$x_2$` con probabilidad `$q$` y `$x_3$` con probabilidad `$(1 - q)$`.
* **Jugada 2:** ofrece `$x_5$` con probabilidad `$t$` y `$x_6$` con probabilidad `$(1 - t)$`.

El individuo elegirá la Jugada 1 sobre la Jugada 2 si y solo si la utilidad esperada de la primera excede a la de la segunda:

$$
\begin{align*}
EU(1) &> EU(2) \\
q U(x_2) + (1 - q) U(x_3) &> t U(x_5) + (1 - t) U(x_6)
\end{align*}
$$

Si denotamos por `$\mu_k = U(x_k)$` el número de utilidad del índice VNM asignado al premio `$x_k$`, la condición de elección es simplemente:

$$
\begin{align*}
q\mu_2 + (1 - q)\mu_3 > t\mu_5 + (1 - t)\mu_6
\end{align*}
$$

### 3.2 Propiedades y axiomas de la función de utilidad VNM

1. **Forma aditiva (lineal en las probabilidades):** la función de utilidad esperada es una combinación lineal de las utilidades de cada resultado contingente ponderadas por sus probabilidades.
2. **Unicidad salvo transformaciones afines positivas:** en la teoría del consumidor bajo certeza, la utilidad es *ordinal* (cualquier transformación monótona creciente preserva el orden). En cambio, bajo riesgo, el índice VNM tiene carácter *cardinal*: **solo es único salvo transformaciones afines positivas**.
   * **Demostración:** sea `$\tilde{U}(x) = \alpha U(x) + \gamma$` con `$\alpha > 0$` y `$\gamma \in \mathbb{R}$`. Evaluemos si la desigualdad `$EU(1) > EU(2)$` se mantiene bajo `$\tilde{U}$`:

$$
\begin{align*}
E\tilde{U}(1) &= q(\alpha U(x_2) + \gamma) + (1 - q)(\alpha U(x_3) + \gamma) \\
&= \alpha\left[q U(x_2) + (1 - q) U(x_3)\right] + (q + 1 - q)\gamma \\
&= \alpha EU(1) + \gamma
\end{align*}
$$

   * De forma análoga, `$E\tilde{U}(2) = \alpha EU(2) + \gamma$`. Como `$\alpha > 0$`, se cumple que:

$$
\begin{align*}
EU(1) > EU(2) \iff \alpha EU(1) + \gamma > \alpha EU(2) + \gamma \iff E\tilde{U}(1) > E\tilde{U}(2)
\end{align*}
$$

   * Cualquier transformación **no afín** —por ejemplo, `$\ln(U)$` o `$U^2$`— altera la curvatura de `$U$` y, con ello, cambia las preferencias frente al riesgo.
3. **Axioma de continuidad:** pequeños cambios en las probabilidades no alteran la naturaleza del orden estricto entre dos loterías.
   * *Ejemplo:* si un agradable paseo en moto por Llanogrande es preferible a quedarse en casa, entonces una mezcla del paseo en moto por Llanogrande con una probabilidad suficientemente pequeña de sufrir un accidente sigue siendo preferible a quedarse en casa.
4. **Axioma de independencia:** las elecciones que planean los individuos entre dos estados o loterías `$L_1$` y `$L_2$` no deben verse afectadas al mezclarlas en la misma proporción con un tercer estado o lotería común `$L_3$`:

$$
\begin{align*}
L_1 \succ L_2 \iff \alpha L_1 + (1 - \alpha) L_3 \succ \alpha L_2 + (1 - \alpha) L_3 \quad \forall \alpha \in (0, 1]
\end{align*}
$$

---

## 4. Aversión al riesgo y Desigualdad de Jensen

¿Qué determina que un individuo rechace una apuesta justa? La clave está en la **concavidad** de su función de utilidad de Bernoulli `$U(W)$`.

### 4.1 Apuesta justa y clasificación de actitudes frente al riesgo

Considere una persona con riqueza inicial cierta `$X$` —o `$W$`— y un activo riesgoso o apuesta `$\epsilon$` que paga `$\epsilon_1 > 0$` con probabilidad `$p$` y `$\epsilon_2 < 0$` con probabilidad `$(1 - p)$`. Decimos que `$\epsilon$` es una **apuesta justa** si su valor esperado es cero:

$$
\begin{align*}
E(\epsilon) = p\epsilon_1 + (1 - p)\epsilon_2 = 0
\end{align*}
$$

Una persona es **estrictamente aversa al riesgo** si rechaza cualquier apuesta justa, es decir, si prefiere conservar su riqueza cierta `$X + E(\epsilon) = X$` antes que enfrentar la lotería `$(X + \epsilon_1, p;\; X + \epsilon_2, 1-p)$`:

$$
\begin{align*}
U\big(X + E(\epsilon)\big) > p\, U(X + \epsilon_1) + (1 - p)\, U(X + \epsilon_2)
\end{align*}
$$

Esto es una aplicación directa de la **Desigualdad de Jensen**: para toda variable aleatoria `$W$` con esperanza finita `$E(W)$` y toda función cóncava `$U$`, la utilidad del valor esperado es mayor o igual que la esperanza de la utilidad:

$$
\begin{align*}
U\big(E(W)\big) \ge E\big(U(W)\big)
\end{align*}
$$

Resumiendo las cuatro categorías de actitud frente al riesgo según la curvatura de `$U(W)$`:

| Actitud frente al riesgo | Relación de preferencias | Desigualdad de Jensen | Curvatura de `$U(W)$` |
| :--- | :--- | :--- | :--- |
| **Estrictamente averso** | `$U(E(W)) \succ E(U(W))$` | `$U(E(W)) > E(U(W))$` | Estrictamente cóncava `$(U''(W) < 0)$` |
| **Averso al riesgo** | `$U(E(W)) \succcurlyeq E(U(W))$` | `$U(E(W)) \ge E(U(W))$` | Cóncava `$(U''(W) \le 0)$` |
| **Neutral al riesgo** | `$U(E(W)) \sim E(U(W))$` | `$U(E(W)) = E(U(W))$` | Lineal `$(U''(W) = 0)$` |
| **Amante al riesgo** | `$E(U(W)) \succ U(E(W))$` | `$E(U(W)) > U(E(W))$` | Estrictamente convexa `$(U''(W) > 0)$` |

### 4.2 Ejemplo numérico y representación gráfica

Retomemos la lotería de riqueza `$L = (5, 0.5;\; 15, 0.5)$`. Su valor esperado es:

$$
\begin{align*}
E(W) = \frac{1}{2}(5) + \frac{1}{2}(15) = 10
\end{align*}
$$

Para una persona estrictamente aversa al riesgo —por ejemplo, con `$u(W) = \sqrt{W}$`—, se cumple que:

$$
\begin{align*}
u(10) = \sqrt{10} \approx 3.162 > \frac{1}{2}u(5) + \frac{1}{2}u(15) = \frac{\sqrt{5} + \sqrt{15}}{2} \approx 3.055
\end{align*}
$$

Geométricamente, el punto correspondiente a la utilidad esperada `$\big(10,\, 0.5u(5) + 0.5u(15)\big)$` se encuentra sobre la **cuerda** que une los puntos `$(5, u(5))$` y `$(15, u(15))$`, la cual queda estrictamente por debajo de la curva cóncava `$u(W)$` en el punto `$W = 10$`.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/utilidad-esperada-light.svg" alt="Curva de utilidad concava con cuerda y brecha de certeza." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/utilidad-esperada-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la cuerda queda bajo la curva y la brecha en W = 10 mide la ganancia de la certeza.</figcaption>
</figure>

---

## 5. Medidas de aversión al riesgo, equivalente cierto y probabilidad de premio

Para comparar el grado de aversión al riesgo entre distintas personas, países o niveles de riqueza, no basta con observar `$U''(W)$`, ya que `$U''(W)$` cambia si multiplicamos `$U$` por una constante positiva `$\alpha > 0$` (transformación afín). Necesitamos medidas invariantes ante transformaciones afines.

### 5.1 Coeficientes de Arrow-Pratt

* **Coeficiente de aversión absoluta al riesgo `$(\gamma_A(W))$`:**

$$
\begin{align*}
\gamma_A(W) = -\frac{U''(W)}{U'(W)}
\end{align*}
$$

  * **Invariancia ante transformaciones afines:** sea `$\tilde{U}(W) = \alpha U(W) + \gamma$` con `$\alpha > 0$`. Sus derivadas son `$\tilde{U}'(W) = \alpha U'(W)$` y `$\tilde{U}''(W) = \alpha U''(W)$`. Al dividir:

$$
\begin{align*}
\tilde{\gamma}_A(W) = -\frac{\tilde{U}''(W)}{\tilde{U}'(W)} = -\frac{\cancel{\alpha}\, U''(W)}{\cancel{\alpha}\, U'(W)} = -\frac{U''(W)}{U'(W)} = \gamma_A(W)
\end{align*}
$$

  El signo negativo asegura que `$\gamma_A(W) > 0$` cuando `$U''(W) < 0$` (aversión al riesgo).

* **Coeficiente de aversión relativa al riesgo `$(\gamma_R(W))$`:** expresa la aversión al riesgo como una proporción de la riqueza `$W$` (equivale a la elasticidad de la utilidad marginal respecto a la riqueza, cambiada de signo):

$$
\begin{align*}
\gamma_R(W) = -\frac{U''(W)}{U'(W)} \cdot W
\end{align*}
$$

  * *Referencia empírica:* en la literatura macroeconómica y financiera internacional (Mehra y Prescott; Lucas; Kaplow) se suelen calibrar valores de `$\gamma_R$` entre `$0.5$` y `$10$` (o incluso hasta `$20$` en modelos de ciclos reales), mientras que en **estudios aplicados a Colombia** los valores estimados suelen ubicarse en el rango `$\gamma_R \in [1.5,\, 4]$`.

### 5.2 Equivalente cierto y probabilidad de premio

1. **Equivalente cierto `$C(f, U)$`:** es la cantidad monetaria segura `$C$` que hace indiferente al individuo entre recibir `$C$` con certeza o jugar la lotería `$x$`:

$$
\begin{align*}
U(C) = EU(x) = \sum_{i=1}^{n} \pi_i U(x_i)
\end{align*}
$$

   Para un agente estrictamente averso al riesgo, `$C < E(x)$`. La diferencia `$\text{Prima de riesgo} = E(x) - C > 0$` mide cuánto dinero está dispuesto a sacrificar el agente respecto al valor esperado para eliminar completamente el riesgo.

2. **Probabilidad de premio `$\Pi(x, \epsilon, U)$`:** es la probabilidad `$\Pi$` —o exceso de probabilidad de ganar sobre `$\frac{1}{2}$`— que hace indiferente a la persona entre conservar el monto cierto `$x$` y enfrentar una lotería simétrica con resultados `$x + \epsilon$` y `$x - \epsilon$`:

$$
\begin{align*}
U(x) = \Pi\, U(x + \epsilon) + (1 - \Pi)\, U(x - \epsilon)
\end{align*}
$$

   Si la persona es aversa al riesgo, requerirá una probabilidad de ganar `$\Pi > \frac{1}{2}$` para aceptar la apuesta.

---

## 6. Aplicación al mercado de seguros y gestión del riesgo

Veamos cómo la teoría de la utilidad esperada explica la demanda de seguros.

### 6.1 El problema de Samara y el Teorema del Seguro Completo

Suponga que Samara tiene activos totales por `$W_0 = \$35.000\text{ USD}$`, pero enfrenta una probabilidad `$p = 0.03$` de sufrir un siniestro que le ocasionaría una pérdida de `$A = \$10.000\text{ USD}$`. Sin seguro, su distribución de riqueza es la lotería:
* Con probabilidad `$p = 0.03$`: `$W_S = \$25.000$`.
* Con probabilidad `$1 - p = 0.97$`: `$W_{NS} = \$35.000$`.

Ahora una aseguradora le ofrece una póliza con cobertura `$K$` (monto que la aseguradora indemniza si ocurre el siniestro) a una tasa de prima `$\gamma$` por cada dólar asegurado, de modo que el costo total de la póliza es `$\gamma K$`. En el caso particular en que la póliza cubre `$K = \$10.000$` a un precio total de `$\gamma K = \$300$` —es decir, `$\gamma = 0.03 = p$`—, la lotería resultante con seguro generaliza a:

$$
\begin{align*}
L = \big(p,\; W_0 - \gamma K - A + K;\;\; 1 - p,\; W_0 - \gamma K\big)
\end{align*}
$$

*(Si la riqueza inicial se separa en un activo libre de riesgo `$W$` y un activo sujeto a riesgo total `$R$`, la expresión equivalente es `$L = (p,\; W + R - \gamma K - R + K;\; 1 - p,\; W + R - \gamma K)$`.)*

### 6.2 Deducción paso a paso de la cobertura óptima `$K^*$`

Samara elige la cobertura `$K \ge 0$` para maximizar su utilidad esperada:

$$
\begin{align*}
\max_{K} \; EU(K) = p\, U(W_0 - \gamma K - A + K) + (1 - p)\, U(W_0 - \gamma K)
\end{align*}
$$

**Paso 1: Condición de Primer Orden (C.P.O.).** Derivamos respecto a `$K$` e igualamos a cero, llamando `$W_S = W_0 - \gamma K - A + K$` a la riqueza en el estado de siniestro y `$W_{NS} = W_0 - \gamma K$` a la riqueza sin siniestro:

$$
\begin{align*}
\frac{\partial EU}{\partial K} = p(1 - \gamma) U'(W_S) - (1 - p)\gamma U'(W_{NS}) = 0
\end{align*}
$$

**Paso 2: Reordenamiento como Relación Marginal de Sustitución.** Pasando el segundo término al lado derecho:

$$
\begin{align*}
\frac{p\, U'(W_S)}{(1 - p)\, U'(W_{NS})} = \frac{\gamma}{1 - \gamma}
\end{align*}
$$

**Paso 3: Análisis bajo prima actuarialmente justa `$(\gamma = p)$`.** Si la aseguradora cobra una prima igual a la probabilidad del siniestro —`$\gamma = p$`; en el ejemplo de Samara, `$\gamma = 0.03$`, lo que implica un costo de `$\$300$` por cubrir `$\$10.000$`—, el lado derecho se simplifica a `$\frac{p}{1 - p}$`, cancelándose con los pesos probabilísticos del lado izquierdo:

$$
\begin{align*}
\frac{\cancel{p}\, U'(W_S)}{\cancel{(1 - p)}\, U'(W_{NS})} = \frac{\cancel{p}}{\cancel{1 - p}} \implies U'(W_S) = U'(W_{NS})
\end{align*}
$$

Como Samara es estrictamente aversa al riesgo `$(U'' < 0)$`, su utilidad marginal `$U'(\cdot)$` es estrictamente decreciente y, por tanto, inyectiva:

$$
\begin{align*}
W_S = W_{NS} \implies W_0 - \gamma K^* - A + K^* = W_0 - \gamma K^* \implies K^* = A
\end{align*}
$$

> **Intuición económica (Teorema del Seguro Completo):** cuando el seguro es actuarialmente justo `$(\gamma = p)$`, todo individuo averso al riesgo adquiere **cobertura total `$(K^* = A)$`** para igualar su consumo en ambos estados de la naturaleza `$(W_S = W_{NS} = \$34.700)$`. Si la prima incluye un recargo administrativo `$(\gamma > p)$`, entonces `$U'(W_S) > U'(W_{NS})$`, lo que implica `$W_S < W_{NS}$` y una cobertura óptima parcial `$(K^* < A)$`.

### 6.3 Otros mecanismos de transferencia, cobertura y diversificación

Además de los seguros privados y colectivos (estos últimos pueden ser obligatorios con consumo requerido pagando una prima media, o voluntarios con prima ligeramente superior), existen instrumentos financieros y organizacionales para administrar el riesgo:

* **Mercado accionario:** quien emite acciones difunde el riesgo productivo entre múltiples inversionistas; quien compra acciones minimiza su riesgo idiosincrático repartiendo su capital en distintos títulos.
* **Cooperativas y mutuales:** acuerdos voluntarios basados en confianza y reciprocidad para acceder a servicios y protección compartida.
* **Instrumentos de cobertura (derivados):** *Forwards* (contratos bilaterales a medida), *Futuros* (contratos estandarizados negociados en bolsa con cámara de compensación) y *Opciones* (derechos no obligatorios de comprar o vender una cantidad `$q^*$` a un precio `$p^*$` en un plazo especificado).
* **Diversificación:** al combinar activos cuyos rendimientos no están perfectamente correlacionados de forma positiva, se reduce la varianza del portafolio. El caso límite ideal ocurre con **activos correlacionados negativamente de forma perfecta `$(\rho = -1)$`**: cuando uno sube, el otro baja exactamente en la proporción inversa, permitiendo eliminar el riesgo por completo y obtener un rendimiento seguro en cualquier estado de la naturaleza.

---

## 7. Demanda de activos inciertos: Modelo Media-Varianza y CAPM

En finanzas y macroeconomía aplicada resulta muy útil caracterizar los activos riesgosos únicamente por los **dos primeros momentos** de su distribución de rendimientos: la media —`$\mu$` o `$r$`— y la varianza —`$\sigma^2$`, o su raíz cuadrada, la desviación típica `$\sigma$`—.

### 7.1 Preferencias en el plano Media-Varianza

Si las decisiones de inversión pueden ordenarse mediante una función de utilidad definida sobre el rendimiento esperado (un *bien*) y la desviación típica (un *mal* para el averso al riesgo):

$$
\begin{align*}
U = U(\mu^+,\, \sigma^-) \quad \text{con } \frac{\partial U}{\partial \mu} > 0, \quad \frac{\partial U}{\partial \sigma} < 0
\end{align*}
$$

esta representación ordena las elecciones de manera equivalente a una función de utilidad esperada (cuando los rendimientos siguen una distribución normal o la utilidad es cuadrática).

<figure class="eco-figure">
  <img src="/assets/figures/micro2/distribuciones-AB-light.svg" alt="Distribuciones de rendimiento A de media positiva y B de media negativa." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/distribuciones-AB-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: A tiene media positiva y mayor dispersion; B, media negativa y menor dispersion.</figcaption>
</figure>

### 7.2 Decisión óptima de inversión con activo libre de riesgo

Suponga que un inversionista puede combinar un **activo libre de riesgo** que ofrece rendimiento cierto `$r_f$` —con `$\sigma_f = 0$`— y un **activo o portafolio riesgoso `$m$`** con rendimiento esperado `$r_m > r_f$` y desviación típica `$\sigma_m > 0$`. Si invierte una fracción `$w$` en el activo riesgoso y `$(1 - w)$` en el activo libre de riesgo:

$$
\begin{align*}
\mu_x &= w\, r_m + (1 - w)\, r_f = r_f + w(r_m - r_f) \\
\sigma_x &= w\, \sigma_m \implies w = \frac{\sigma_x}{\sigma_m}
\end{align*}
$$

Sustituyendo `$w$` en `$\mu_x$`, obtenemos la **recta presupuestaria en el plano `$(\sigma, r)$`**:

$$
\begin{align*}
\mu_x = r_f + \left(\frac{r_m - r_f}{\sigma_m}\right) \sigma_x
\end{align*}
$$

La pendiente de esta recta se denomina **precio del riesgo** `$p$` (o ratio de Sharpe):

$$
\begin{align*}
p = \frac{r_m - r_f}{\sigma_m}
\end{align*}
$$

Como el rendimiento esperado es un bien y la desviación típica un mal, las **curvas de indiferencia** en el plano `$(\sigma, \mu)$` son crecientes y convexas. En la elección óptima `$\big(\sigma_x^*, r_x^*\big)$`, la curva de indiferencia es tangente a la recta presupuestaria, igualando la Relación Marginal de Sustitución `$(RMS)$` al precio del riesgo:

$$
\begin{align*}
RMS = -\frac{\partial U / \partial \sigma}{\partial U / \partial \mu} = \frac{r_m - r_f}{\sigma_m}
\end{align*}
$$

<figure class="eco-figure">
  <img src="/assets/figures/micro2/riesgo-rendimiento-light.svg" alt="Recta presupuestaria y tangencia con curva de indiferencia." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/riesgo-rendimiento-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el optimo iguala la relacion marginal de sustitucion al precio del riesgo.</figcaption>
</figure>

### 7.3 Dominancia entre portafolios cuando existe activo libre de riesgo

Suponga que debe elegir entre combinar el activo libre de riesgo `$r_f$` con el activo riesgoso `$x$` o con el activo riesgoso `$y$` —donde `$r_y > r_x$` y `$(r_y - r_f)/\sigma_y > (r_x - r_f)/\sigma_x$`—.

* Si es posible **fraccionar** la inversión combinando con `$r_f$`, invertir en `$y$` y `$r_f$` domina estrictamente a invertir en `$x$` y `$r_f$`, porque la recta presupuestaria asociada a `$y$` tiene mayor pendiente y permite alcanzar una curva de indiferencia más alta.
* Por el contrario, si fuera una decisión de **"todo o nada"** —todo en `$x$` o todo en `$y$` sin acceso a `$r_f$`—, un agente muy averso al riesgo podría preferir `$x$` por su menor desviación típica.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/dos-activos-light.svg" alt="Dos rectas presupuestarias desde rf y dominancia del activo y." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/dos-activos-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la recta mas empinada permite alcanzar mayor utilidad.</figcaption>
</figure>

### 7.4 El Modelo CAPM (Capital Asset Pricing Model)

El valor de un activo individual `$i$` depende mucho más de **cómo se correlaciona su rendimiento con el resto del mercado** que de su propia varianza aislada, porque el riesgo idiosincrático se elimina diversificando. La contribución del activo `$i$` al riesgo total del portafolio de mercado `$m$` se mide mediante su coeficiente **beta `$(\beta_i)$`**:

$$
\begin{align*}
\beta_i = \frac{\text{cov}(\tilde{r}_i, \tilde{r}_m)}{\text{var}(\tilde{r}_m)}
\end{align*}
$$

El **riesgo relevante (sistemático)** del activo `$i$` es `$\beta_i \sigma_m$`. Multiplicando esta cantidad de riesgo por el precio del riesgo `$p = \frac{r_m - r_f}{\sigma_m}$`, obtenemos el **ajuste del riesgo** —prima de riesgo exigida al activo `$i$`—:

$$
\begin{align*}
\text{Ajuste del riesgo} = \beta_i \sigma_m \cdot p = \beta_i \cancel{\sigma_m} \cdot \frac{r_m - r_f}{\cancel{\sigma_m}} = \beta_i (r_m - r_f)
\end{align*}
$$

En equilibrio de mercado sin oportunidades de arbitraje, todos los activos `$i, j$` deben ofrecer el mismo rendimiento ajustado por riesgo:

$$
\begin{align*}
r_i - \beta_i(r_m - r_f) = r_j - \beta_j(r_m - r_f)
\end{align*}
$$

Comparando cualquier activo riesgoso `$i$` con el activo libre de riesgo `$f$` —cuyo `$\beta_f = 0$` y cuyo rendimiento es `$r_f$`—, obtenemos la ecuación fundamental del **Modelo CAPM**:

$$
\begin{align*}
r_i = r_f + \beta_i (r_m - r_f)
\end{align*}
$$

donde el rendimiento esperado de la acción se mide por su valoración intertemporal: `$r_i = E\left(\frac{p_1 - p_0}{p_0}\right)$`.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/sml-capm-light.svg" alt="Recta del mercado del CAPM." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/sml-capm-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el rendimiento esperado crece linealmente con beta.</figcaption>
</figure>

---

## 8. Paradojas de la elección bajo riesgo y racionalidad limitada

Aunque el modelo VNM es el estándar normativo en economía, diversos experimentos empíricos muestran que las personas violan sistemáticamente algunos de sus axiomas.

### 8.1 Paradoja de Allais (violación del axioma de independencia)

Considere tres posibles premios monetarios: `$(250.000,\, 500,\, 0)$`. Se pide elegir primero entre:
* `$L_1 = (0,\, 1,\, 0)$`: ganar `$500$` con certeza —`$100\%$` de probabilidad—.
* `$L_2 = (0.10,\, 0.89,\, 0.01)$`: `$10\%$` de ganar `$250.000$`, `$89\%$` de ganar `$500$`, y `$1\%$` de ganar `$0$`.

La mayoría de las personas prefiere **`$L_1 \succ L_2$`** (efecto certeza). Según la utilidad esperada VNM, esto exige:

$$
\begin{align*}
U(500) &> 0.10\, U(250.000) + 0.89\, U(500) + 0.01\, U(0) \\
0.11\, U(500) &> 0.10\, U(250.000) + 0.01\, U(0)
\end{align*}
$$

Ahora se presenta una segunda elección entre:
* `$L_1^* = (0,\, 0.11,\, 0.89)$`: `$11\%$` de ganar `$500$` y `$89\%$` de ganar `$0$`.
* `$L_2^* = (0.10,\, 0,\, 0.90)$`: `$10\%$` de ganar `$250.000$` y `$90\%$` de ganar `$0$`.

En los experimentos, la mayoría elige **`$L_2^* \succ L_1^*$`**! Sin embargo, bajo VNM eso implica:

$$
\begin{align*}
0.10\, U(250.000) + 0.90\, U(0) &> 0.11\, U(500) + 0.89\, U(0) \\
0.10\, U(250.000) + 0.01\, U(0) &> 0.11\, U(500)
\end{align*}
$$

Las desigualdades `$(24)$` y `$(25)$` son **matemáticamente contradictorias**: al restar el `$89\%$` común de probabilidad de obtener `$500$` (en el primer par) o de obtener `$0$` (en el segundo par), el axioma de independencia exigía mantener el mismo orden de preferencia.

### 8.2 Otras paradojas y anomalías conductuales

* **Paradoja de Machina:** suponga las preferencias estrictas `$\text{Viaje en moto a Cartagena } (M) \succ \text{Ver un video de Cartagena } (\text{Video}) \succ \text{Quedarse en casa } (\text{Casa})$`. Compare ahora `$L_1 = (M, 0.99;\; \text{Video}, 0.01)$` y `$L_2 = (M, 0.99;\; \text{Casa}, 0.01)$`. Aunque el axioma de independencia obliga a preferir `$L_1 \succ L_2$`, muchas personas prefieren `$L_2$` para evitar la decepción emocional de quedarse viendo un video en lugar de haber hecho el viaje.
* **Paradoja de Ellsberg (aversión a la ambigüedad):** cuando las personas deben elegir entre dos urnas o apuestas, la mayoría prefiere aquella donde la **probabilidad es conocida** (riesgo objetivo) frente a aquella donde la probabilidad es desconocida (incertidumbre o ambigüedad), incluso si la simetría sugiere probabilidades iguales.
* **Preferencias inducidas (dependencia del estado):** te invitan a cenar pescado `$(P)$` o carne `$(C)$` y eres indiferente entre ambos platos, pero debes llevar el vino correcto —tinto para carne `$T/C$`, blanco para pescado `$B/P$`—. Aunque no sabes qué te servirán y la lotería de la cena es `$(P, \frac{1}{2};\; C, \frac{1}{2})$`, no eres indiferente ante el tipo de vino si valoras evitar el mal emparejamiento.

### 8.3 Racionalidad limitada, heurísticos y sesgos cognitivos

La economía conductual (Herbert Simon, Daniel Kahneman, Barry Schwartz) explica estas desviaciones señalando que tomamos decisiones de forma **parcialmente irracional** debido a limitaciones cognitivas, de información y de tiempo:

* **Heurísticos:** atajos mentales o reglas generales que simplifican la toma de decisiones cotidiana, pero pueden inducir errores sistemáticos.
* **Sesgos cognitivos:** distorsiones en el procesamiento de la información (por ejemplo, el sesgo de anclaje: dar excesiva importancia a la primera información o referencia previa).
* **Paradoja de la elección y perfiles de decisión:** un exceso de opciones puede reducir el bienestar por arrepentimiento anticipado (*maximizadores* vs. *satisfactores*), mientras que la evaluación retrospectiva de una experiencia (*yo que recuerda*, dominado por el pico y el final) difiere de lo vivido momento a momento (*yo que experimenta*).
