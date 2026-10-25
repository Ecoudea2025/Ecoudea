---
title: "Clase 11: Riesgo, Seguros e Información Asimétrica"
course: "microeconomia-ii"
order: 13
classType: "clase"
description: "Utilidad esperada de Von Neumann-Morgenstern, equivalente cierto, prima por riesgo, medidas de aversión al riesgo de Arrow-Pratt, mercado de seguros, selección adversa (limones de Akerlof y señalización) y riesgo moral (Principal-Agente)."
math: true
conceptos: ["Equivalente cierto", "Prima por riesgo", "Selección adversa"]
---

## 1. Elección bajo Riesgo y Utilidad Esperada (Von Neumann-Morgenstern)

Cuando levantamos el supuesto de certidumbre del modelo walrasiano básico, las decisiones económicas se convierten en **loterías** o activos contingentes. Considere una lotería `$L$` que entrega la riqueza `$W_1$` con probabilidad `$p \in (0, 1)$` y la riqueza `$W_2$` con probabilidad `$(1 - p)$`:

* **Valor Esperado Monetario de la lotería `$( \mathbb{E}[W] )$`:**

$$
\begin{align*}\mathbb{E}[W] = p W_1 + (1 - p) W_2\end{align*}
$$

* **Utilidad Esperada de Von Neumann-Morgenstern `$( \mathbb{E}[u(W)] )$`:**
  Un individuo racional bajo incertidumbre no maximiza el dinero esperado (como demostró la *Paradoja de San Petersburgo* de Bernoulli), sino el **valor esperado de la utilidad** asignada a cada resultado posible:

  $$
  \begin{align*}\mathbb{E}[u(W)] = p u(W_1) + (1 - p) u(W_2)\end{align*}
  $$

### Actitudes hacia el Riesgo, Equivalente Cierto y Prima por Riesgo

Por la **Desigualdad de Jensen**, la actitud de un agente frente al riesgo queda determinada por la curvatura de su función de utilidad de Bernoulli `$u(W)$` `(con `$u'(W) > 0$`)`:

1. **Averso al riesgo `$(u''(W) < 0, \text{ función estrictamente cóncava})$`:** Prefiere recibir con certeza el valor esperado antes que jugar la lotería:

$$
\begin{align*}u\big(\mathbb{E}[W]\big) > \mathbb{E}[u(W)]\end{align*}
$$

2. **Neutral al riesgo `$(u''(W) = 0, \text{ función lineal})$`:** `$u\big(\mathbb{E}[W]\big) = \mathbb{E}[u(W)]$`.
3. **Amante o propenso al riesgo `$(u''(W) > 0, \text{ función convexa})$`:** `$u\big(\mathbb{E}[W]\big) < \mathbb{E}[u(W)]$`.

Definimos dos conceptos operativos esenciales para cualquier agente averso al riesgo:
* **Equivalente Cierto `$(EC)$`:** Es la cantidad de dinero **segura** que le brinda al individuo exactamente la misma utilidad esperada que la lotería riesgosa:

$$
\begin{align*}u(EC) = \mathbb{E}[u(W)] \implies \boxed{EC = u^{-1}\Big( p u(W_1) + (1 - p) u(W_2) \Big)}\end{align*}
$$

* **Prima por Riesgo `$( \Pi )$`:** Es la cantidad máxima de dinero esperado a la que el individuo está dispuesto a renunciar para eliminar el riesgo (la diferencia entre el valor esperado y el equivalente cierto):

$$
\begin{align*}\boxed{\Pi = \mathbb{E}[W] - EC > 0} \quad \text{(para todo agente averso al riesgo)}\end{align*}
$$

### Medidas de Aversión al Riesgo de Arrow-Pratt

Dado que la utilidad esperada es invariante ante transformaciones lineales positivas `$(v(W) = a + b u(W) \text{ con } b > 0)$`, la segunda derivada sola `$u''(W)$` no es una medida invariante. **Kenneth Arrow y John Pratt** definieron los dos coeficientes canónicos de aversión al riesgo:

$$
\begin{align*}ARA(W) \equiv -\frac{u''(W)}{u'(W)} \quad \text{(Aversión Absoluta al Riesgo)}, \qquad \qquad RRA(W) \equiv -\frac{W u''(W)}{u'(W)} \quad \text{(Aversión Relativa al Riesgo)}\end{align*}
$$

### Aplicación al Mercado de Seguros Competitivos

Suponga un individuo averso al riesgo `$(u'' < 0)$` con riqueza inicial `$W_0$` que enfrenta una probabilidad `$p$` de sufrir un siniestro de pérdida `$L$`. Puede comprar una cobertura de seguro `$q$` pagando una prima de `$\gamma q$` `(donde `$\gamma$` es el precio por peso asegurado)`:
* Riqueza sin siniestro `(probabilidad `$1 - p$`)`: `$W_{NS} = W_0 - \gamma q$`.
* Riqueza con siniestro `(probabilidad `$p$`)`: `$W_S = W_0 - L - \gamma q + q$`.

Maximizando `$\mathbb{E}[u] = (1 - p) u(W_{NS}) + p u(W_S)$` respecto a `$q$`:

$$
\begin{align*}\frac{\text{d}\mathbb{E}[u]}{\text{d}q} = -(1 - p)\gamma u'(W_{NS}) + p(1 - \gamma) u'(W_S) = 0 \implies \frac{u'(W_S)}{u'(W_{NS})} = \frac{\gamma (1 - p)}{p (1 - \gamma)}\end{align*}
$$

Si el mercado de seguros es competitivo y **actuarialmente justo** `$( \gamma = p )$`, el lado derecho es igual a `$1$`, lo que implica `$u'(W_S) = u'(W_{NS}) \implies W_S = W_{NS} \implies \boxed{q^* = L}$`: **todo agente estrictamente averso al riesgo se asegura al `$100\%$` (seguro completo) cuando la prima es actuarialmente justa**.


## 2. Asimetrías de Información I: Selección Adversa (Previa al Contrato)

En el mundo real, una de las partes del mercado suele tener información privada superior a la otra. Cuando la asimetría existe **antes de firmar el contrato (*ex ante*, información oculta sobre el "tipo" o calidad)**, surge el problema de **Selección Adversa**.

### El Mercado de los "Limones" de George Akerlof (1970)

Considere el mercado de automóviles usados donde existen dos tipos de autos en igual proporción `$(50\%\text{ cada uno})$`:
* **Autos buenos ("duraznos"):** Los vendedores los valoran en `$V_B = 10\,000$` y los compradores en `$W_B = 12\,000$`.
* **Autos malos ("limones"):** Los vendedores los valoran en `$V_M = 4\,000$` y los compradores en `$W_M = 6\,000$`.

Si la calidad fuera observable (información simétrica), ambos mercados funcionarían eficientemente. Pero si **sólo el vendedor conoce la calidad de su auto** y el comprador sólo conoce el promedio estadístico:

1. Un comprador neutral al riesgo calcula el valor esperado de un auto al azar:

$$
\begin{align*}\bar{W} = \frac{1}{2}(12\,000) + \frac{1}{2}(6\,000) = 9\,000\end{align*}
$$

2. Como el precio máximo que ofrece el comprador `$(P = 9\,000)$` es **menor que la valoración mínima de los dueños de autos buenos `$(V_B = 10\,000)$`**, **todos los dueños de autos buenos se retiran del mercado**.
3. Al saber los compradores que sólo quedan "limones" en venta, bajan su disposición a pagar a `$6\,000$`, destruyéndose por completo el mercado de autos de alta calidad (pérdida de ganancias del intercambio mutuo).

### Soluciones de Mercado a la Selección Adversa: Señalización y Cribado

* **Señalización (*Signaling* — Michael Spence, 1973):** La parte informada `(el vendedor de un buen auto o el trabajador de alta productividad `$\theta_H > \theta_L$`)` realiza una acción observable `(ofrecer garantía extendida o adquirir un título educativo `$e$`)`. Para que exista un **equilibrio separador**, debe cumplirse la **condición de cruce único de Spence-Mirrlees**: adquirir la señal debe ser significativamente más costoso en el margen para el agente de baja calidad que para el de alta calidad `$(c_L'(e) > c_H'(e))$`, de modo que al tipo bajo no le convenga imitar al tipo alto:

$$
\begin{align*}w_H - c_L(e^*) \leq w_L \implies e^* \geq \frac{w_H - w_L}{c_L} \quad \text{(Restricción de no imitación del tipo bajo)}\end{align*}
$$

* **Cribado (*Screening* — Rothschild y Stiglitz, 1976):** La parte desinformada (la aseguradora) diseña un **menú de contratos** `(Prima, Franquicia/Deducible)` para que los propios clientes se autoseleccionen revelando su verdadero riesgo: los clientes de alto riesgo eligen cobertura completa a prima alta, y los clientes de bajo riesgo aceptan un deducible alto a cambio de una prima baja.


## 3. Asimetrías de Información II: Riesgo Moral y el Problema Principal-Agente

Cuando la asimetría informativa ocurre **después de firmar el contrato (*ex post*, acción o esfuerzo oculto)**, estamos ante **Riesgo Moral** (el problema de agencia mencionado por el profesor David Tobón en las láminas de Contratos y de Votación Indirecta).

### Planteamiento Matemático del Modelo Principal-Agente

Un **Principal** (accionista, empleador o electorado) contrata a un **Agente** (gerente, trabajador o político) para que elija un nivel de esfuerzo `$e \in \{e_B, e_A\}$` `(Bajo o Alto, con costo de desutilidad `$c(e_A) > c(e_B)$`)`. El esfuerzo no es observable, pero determina la probabilidad `$p(e)$` de obtener un resultado alto `$Y_A$` frente a un resultado bajo `$Y_B$` `$(p(e_A) > p(e_B))$`.

Para inducir al Agente a realizar el esfuerzo alto `$e_A$`, el Principal diseña un contrato salarial contingente al resultado observable `$(w_A, w_B)$` que maximiza el beneficio esperado del Principal sujeto a **dos restricciones fundamentales**:

1. **Restricción de Participación `(o Racionalidad Individual — `$IR$`)`:** El contrato debe garantizarle al Agente al menos su utilidad de reserva `$\underline{u}$` (lo que ganaría en su mejor alternativa fuera de la empresa):

$$
\begin{align*}p(e_A) u(w_A) + \big(1 - p(e_A)\big) u(w_B) - c(e_A) \geq \underline{u} \qquad \text{(IR)}\end{align*}
$$

2. **Restricción de Compatibilidad de Incentivos `$(IC)$`:** Al Agente debe convenirle más esforzarse `$(e_A)$` que holgazanear `$(e_B)$`:

$$
\begin{align*}p(e_A) u(w_A) + \big(1 - p(e_A)\big) u(w_B) - c(e_A) \geq p(e_B) u(w_A) + \big(1 - p(e_B)\big) u(w_B) - c(e_B) \qquad \text{(IC)}\end{align*}
$$

Reordenando `(IC)` se obtiene la condición necesaria de todo contrato de incentivos:

$$
\begin{align*}\big[ p(e_A) - p(e_B) \big] \big( u(w_A) - u(w_B) \big) \geq c(e_A) - c(e_B) > 0 \implies \boxed{w_A > w_B}\end{align*}
$$

> **El *Trade-off* Fundamental entre Seguro e Incentivos:**
> * Si el esfuerzo fuera observable (*First Best*), el Principal neutral al riesgo aseguraría completamente al Agente averso al riesgo pagándole un salario fijo `$(w_A = w_B)$`.
> * Bajo riesgo moral (*Second Best*), para incentivar el esfuerzo `$(IC)$`, **el Principal se ve obligado a transferirle riesgo al Agente `$(w_A > w_B)$`**, sacrificando eficiencia en el reparto del riesgo para ganar eficiencia en los incentivos.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/riesgo-ce-prima-light.svg" alt="Logaritmo cóncavo con valor esperado, equivalente cierto y prima; umbral que separa costos de señalización." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/riesgo-ce-prima-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la concavidad descuenta el riesgo; el umbral separa a los productivos.</figcaption>
</figure>


<IdeaClave>

Riesgo e información asimétrica se modelan igual: lo que no se observa se revela con contratos, señales o cribas.

</IdeaClave>
