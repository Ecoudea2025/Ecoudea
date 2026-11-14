---
title: "Clase 15: Externalidades ambientales, equilibrio general y mecanismos de regulación"
course: "microeconomia-ii"
order: 15
classType: "clase"
description: "Teoría de las externalidades ambientales: modelo de equilibrio general con un consumidor y una empresa, impuesto pigouviano, teorema de Coase, comparación impuestos vs. normas, y decisiones simultáneas con tecnologías de mitigación (Tobón y Vasco)."
math: true
---

## Motivación: cuando los precios dejan de decir la verdad

En el Primer Teorema Fundamental del Bienestar demostramos que, bajo mercados completos y competencia perfecta, la asignación de equilibrio walrasiano es eficiente en el sentido de Pareto porque el sistema de precios transmite toda la escasez relativa de los recursos. Sin embargo, cuando existen **externalidades**, los precios de mercado omiten costos o beneficios reales que recaen sobre terceros.

Una **externalidad** es el efecto indirecto de una actividad de producción o consumo sobre el conjunto de producción, el conjunto de consumo, las funciones de producción o las funciones de utilidad de otros agentes. Sus dos particularidades esenciales son:
1. **Alteridad:** quien genera el efecto es distinto de quien lo recibe.
2. **Ausencia de registro mercantil:** el mercado no registra ni valora en un precio este efecto negativo o positivo.

Desde la Revolución Industrial —con las máquinas a vapor y el deterioro atmosférico urbano— hasta fenómenos contemporáneos como el desplazamiento altitudinal de los ecosistemas del Chimborazo documentado por Morueta-Holme et al. (2015), el riesgo de extinción masiva de especies por calentamiento global (Urban, 2015) o la contaminación atmosférica del Valle de Aburrá (*"Si Medellín no tuviera humos seguiría siendo un pueblo muy bonito"*, Tomás Carrasquilla), las externalidades ambientales constituyen uno de los problemas centrales de la microeconomía moderna.

---

## 1. Taxonomía de los mecanismos de regulación económica ambiental

Antes de formalizar los modelos matemáticos, conviene ordenar el abanico de instrumentos disponibles para corregir una externalidad ambiental en tres grandes familias:

| Categoría | Instrumentos específicos | Mecanismo de acción |
| :--- | :--- | :--- |
| **Normas de Comando y Control (C&C)** | Planes de Ordenamiento Territorial (POT), usos del suelo y zonas protegidas; normas sobre emisiones por unidad o techos globales `$(\text{Cap})$`; normas técnicas sobre insumos, cadena de valor, *end of pipe* (filtros al final del proceso) o *changing the production process*; responsabilidad extendida en el consumo (5R: Reducir, Reutilizar, Reciclar, Reparar y Recuperar). | Restricción regulatoria directa sobre cantidades, ubicaciones o tecnologías permitidas; su incumplimiento conlleva sanciones económicas, clausuras, revocación de licencias e incluso responsabilidad penal en daños graves, dolosos o negligentes. |
| **Instrumentos Económicos** | Impuestos pigouvianos y tasas ambientales; sistemas *Cap and Trade* (intercambio de permisos de emisiones, como mercados de carbono); depósitos reembolsables; pagos por servicios ambientales (compensaciones); subsidios a la descontaminación. | Modificación de los precios relativos o creación de mercados de derechos para internalizar el costo marginal social dentro de la decisión privada de la firma o del consumidor. |
| **Iniciativas Privadas** | Responsabilidad Social Corporativa (CSR); mercados voluntarios y bonos verdes; mercados verdes (consumidores dispuestos a pagar sobreprecios por bienes limpios); 5R voluntarias. | Autorregulación empresarial, presión de *stakeholders* o diferenciación de producto por preferencias ambientales. |

> **Debate sobre la responsabilidad social de la empresa:** Mientras Milton Friedman (1970) sostenía que en una sociedad libre *"existe una y solo una responsabilidad social de los negocios: usar sus recursos y emprender actividades diseñadas para incrementar sus utilidades, siempre que se mantenga dentro de las reglas del juego"*, el enfoque contemporáneo concibe la firma como una **coalición de participantes** —inversionistas, distribuidores, consumidores, proveedores, acreedores, empleados e instituciones—, donde los accionistas dejan de ser los únicos reclamantes residuales y la gerencia debe equilibrar demandas de múltiples grupos de interés (Barney, 2018; Tobón et al., 2024).

---

## 2. Modelo de Equilibrio General con Externalidades: un consumidor y una empresa

Para comprender con rigor por qué falla el mercado y cómo funcionan exactamente las soluciones de Pigou y Coase, formalicemos una economía de equilibrio general con dos agentes —una firma productora del bien `$x$` y un consumidor representativo— y dos bienes —manufacturas `$x$` y trabajo/ocio `$\ell$`—.

### 2.1 Variables, notación y tecnología

* **Notación:** el subíndice `$c$` denota uso o consumo del individuo, y el nombre del bien denota el total producido o dotado.
* **Producción:** el bien `$x$` se produce utilizando únicamente trabajo `$L_x$` mediante la función de producción `$x = f(L_x)$`, estrictamente creciente y cóncava.
* **Dotación de tiempo:** el consumidor posee una dotación fija de trabajo `$\bar{L}$`, que reparte entre trabajar para la firma `$L_x$` y disfrutar de ocio `$\ell_c$`, de modo que `$\bar{L} = L_x + \ell_c$`.
* **Externalidad negativa:** cada unidad producida de `$x$` genera una unidad de contaminación (relación `1` a `1`) que afecta negativamente al consumidor. Por ello, la función de utilidad depende del consumo privado `$x_c$`, del ocio `$\ell_c$` y del nivel agregado de producción contaminante `$x$`:

$$
\begin{align*}
U = U(x_c, \ell_c, x) \quad \text{con } \frac{\partial U}{\partial x_c} > 0, \quad \frac{\partial U}{\partial \ell_c} > 0, \quad \frac{\partial U}{\partial x} < 0
\end{align*}
$$

### 2.2 Asignación de eficiencia (problema del planificador social)

Un planificador central que busca maximizar el bienestar social resuelve:

$$
\begin{align*}
\max_{x_c, \ell_c, x, L_x} \; U(x_c, \ell_c, x) \quad \text{s.a.} \quad
\begin{cases}
x = f(L_x) \\
\bar{L} = L_x + \ell_c \\
x = x_c
\end{cases}
\end{align*}
$$

**Paso 1: Planteamiento del Lagrangiano.** Introducimos los multiplicadores `$\lambda_x$`, `$\mu_L$` y `$\mu_x$` asociados a cada restricción:

$$
\begin{align*}
\mathcal{L} = U(x_c, \ell_c, x) + \lambda_x \big[f(L_x) - x\big] + \mu_L \big[\bar{L} - L_x - \ell_c\big] + \mu_x \big[x - x_c\big]
\end{align*}
$$

**Paso 2: Condiciones de Primer Orden (C.P.O.).** Derivamos respecto a cada variable de decisión:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial x_c} &= \frac{\partial U}{\partial x_c} - \mu_x = 0 \\
\frac{\partial \mathcal{L}}{\partial \ell_c} &= \frac{\partial U}{\partial \ell_c} - \mu_L = 0 \\
\frac{\partial \mathcal{L}}{\partial x} &= \frac{\partial U}{\partial x} - \lambda_x + \mu_x = 0 \\
\frac{\partial \mathcal{L}}{\partial L_x} &= \lambda_x \frac{\partial f}{\partial L_x} - \mu_L = 0
\end{align*}
$$

**Paso 3: Eliminación de multiplicadores.** Dividiendo `$(1)$` entre `$(2)$` y despejando `$\lambda_x$` de `$(4)$`:

$$
\begin{align*}
\frac{\frac{\partial U}{\partial x_c}}{\frac{\partial U}{\partial \ell_c}} &= \frac{\mu_x}{\mu_L} \\
\lambda_x &= \frac{\mu_L}{\frac{\partial f}{\partial L_x}}
\end{align*}
$$

**Paso 4: Sustitución de `$(5)$` en `$(3)$` y división por `$\mu_L$`.** Reemplazamos `$\lambda_x$` en la ecuación `$(3)$`:

$$
\begin{align*}
\frac{\partial U}{\partial x} - \frac{\mu_L}{\frac{\partial f}{\partial L_x}} + \mu_x = 0 \implies \frac{\mu_L}{\frac{\partial f}{\partial L_x}} - \frac{\partial U}{\partial x} = \mu_x
\end{align*}
$$

Dividiendo toda la expresión entre `$\mu_L$` obtenemos la ecuación `$(6)$`:

$$
\begin{align*}
\frac{1}{\frac{\partial f}{\partial L_x}} - \frac{\frac{\partial U}{\partial x}}{\mu_L} = \frac{\mu_x}{\mu_L}
\end{align*}
$$

Finalmente, sustituyendo `$\mu_L = \frac{\partial U}{\partial \ell_c}$` de `$(2)$` en `$(6)$`, llegamos a la **condición de eficiencia de Pareto `$((7))$`**:

$$
\begin{align*}
\frac{\frac{\partial U}{\partial x_c}}{\frac{\partial U}{\partial \ell_c}} = \frac{\mu_x}{\mu_L} = \frac{1}{\frac{\partial f}{\partial L_x}} - \frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}}
\end{align*}
$$

> **Intuición económica:** Como `$\frac{\partial U}{\partial x} < 0$`, el término `$-\frac{\partial U / \partial x}{\partial U / \partial \ell_c} > 0$` representa el **daño marginal** que cada unidad adicional de `$x$` inflige al consumidor, medido en unidades de ocio. En el óptimo social, la Relación Marginal de Sustitución entre el bien `$x$` y el ocio debe igualar la **Tasa Marginal de Transformación Social**, que suma el costo marginal técnico de producir una unidad de `$x$` en términos de trabajo `$(\frac{1}{\partial f / \partial L_x})$` más el daño marginal ambiental.

### 2.3 Equilibrio de mercado competitivo sin intervención

Sea `$P^* = (P_x^*, w^*)$` el vector de precios de equilibrio, donde `$P_x$` es el precio del bien `$x$` y `$w$` es el salario.

* **El productor** maximiza beneficios tomando precios como dados:

$$
\begin{align*}
\max_{L_x} \; \Pi_x = P_x f(L_x) - w L_x \implies \frac{\partial \Pi_x}{\partial L_x} = P_x \frac{\partial f}{\partial L_x} - w = 0 \implies \frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x}{w}
\end{align*}
$$

* **El consumidor** recibe las utilidades `$\Pi_x$` de la firma y el valor de su dotación de tiempo `$w\bar{L}$`, maximizando `$U(x_c, \ell_c, x)$` tomando `$x$` como un parámetro exógeno fuera de su control:

$$
\begin{align*}
\max_{x_c, \ell_c} \; U(x_c, \ell_c, x) \quad \text{s.a.} \quad \Pi_x + w\bar{L} = P_x x_c + w\ell_c
\end{align*}
$$

Planteando `$\mathcal{L} = U(x_c, \ell_c, x) + \lambda[\Pi_x + w\bar{L} - P_x x_c - w\ell_c]$`, sus C.P.O. son `$\frac{\partial U}{\partial x_c} - \lambda P_x = 0$` y `$\frac{\partial U}{\partial \ell_c} - \lambda w = 0$`, de donde:

$$
\begin{align*}
\frac{\frac{\partial U}{\partial x_c}}{\frac{\partial U}{\partial \ell_c}} = \frac{P_x}{w}
\end{align*}
$$

En el equilibrio de mercado donde los mercados se aclaran —`$x^*(P_x^*, w^*) = x_c(P_x^*, w^*)$` y `$\bar{L} - \ell^*(P_x^*, w^*) = L_x(P_x^*, w^*)$`—, se cumple que:

$$
\begin{align*}
\frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x^*}{w^*} = \frac{\frac{\partial U}{\partial x_c}}{\frac{\partial U}{\partial \ell_c}}
\end{align*}
$$

Al comparar esta igualdad con `$(7)$`, falta el término del daño marginal `$-\frac{\partial U / \partial x}{\partial U / \partial \ell_c}$`. Por tanto, **un equilibrio de mercado competitivo con externalidades es ineficiente**: la firma ignora el costo ambiental y produce en exceso.

---

## 3. Corrección de la ineficiencia: Pigou vs. Teorema de Coase

### 3.1 Solución A: Impuesto Pigouviano ("el que contamina paga")

Consiste en cobrar a quien contamina un impuesto por unidad producida `$t$` igual al valor del daño marginal evaluado en el óptimo social.

La firma `$x$` ahora maximiza beneficios netos del impuesto:

$$
\begin{align*}
\max_{L_x} \; \Pi_x = (P_x - t) f(L_x) - w L_x \implies \frac{\partial \Pi_x}{\partial L_x} = (P_x - t)\frac{\partial f}{\partial L_x} - w = 0
\end{align*}
$$

Despejando la inversa del producto marginal del trabajo:

$$
\begin{align*}
\frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x - t}{w} \implies \frac{1}{\frac{\partial f}{\partial L_x}} + \frac{t}{w} = \frac{P_x}{w}
\end{align*}
$$

Como el consumidor sigue cumpliendo `$\frac{P_x}{w} = \frac{\partial U / \partial x_c}{\partial U / \partial \ell_c}$`, comparamos directamente con la ecuación de eficiencia `$(7)$`:

$$
\begin{align*}
\frac{t}{w} = -\frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}} \implies t^* = -\frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}} \cdot w
\end{align*}
$$

Es decir, el impuesto óptimo `$t^*$` es exactamente igual al **valor monetario del daño marginal**. Con este impuesto, el equilibrio de mercado recupera la eficiencia de Pareto.

* **Problemas prácticos del impuesto pigouviano:**
  1. Estimar el daño marginal requiere un esfuerzo multidisciplinario complejo; si hay múltiples contaminadores, imputar el daño marginal individual resulta difícil.
  2. El daño marginal puede manifestarse en el largo plazo y generar altos costos institucionales de medición, contabilización, vigilancia y control.
  3. Los afectados tienen incentivos a **sobreestimar** el daño declarado; además, si el impuesto se calcula mal, reajustarlo tiene un alto costo político.
  4. Desde otras disciplinas suele criticarse *"el que contamina paga"* como un *"pago por indulgencias"*.

### 3.2 Solución B: Asignación de Derechos de Propiedad (Teorema de Coase)

Ronald Coase (1961) criticó el principio unilateral de *"quien contamina paga"*, argumentando que las externalidades no son un problema moral entre "buenos y malos", sino **un problema de naturaleza recíproca**: evitar el daño al afectado implica infligir un costo al causante. Además, los impuestos recaudados generan efectos renta que deben considerarse.

> **Teorema de Coase:** Si los derechos de propiedad sobre el recurso transmisor de la externalidad están **bien definidos** y los **costos de transacción** de usar el mercado son suficientemente bajos, la creación de un mercado de derechos a precio `$P_D$` conduce a un equilibrio de mercado competitivo **eficiente**, sin importar a favor de quién se asignen inicialmente esos derechos.

Demostremos matemáticamente esta invariancia en nuestro modelo de equilibrio general bajo las dos asignaciones posibles.

#### Caso 1: Los derechos de propiedad se asignan a favor del consumidor

El consumidor es dueño del ambiente limpio y puede vender derechos de contaminación `$D_o$` al precio `$P_D$`. La firma debe comprar derechos demandados `$D_d = x$` —dado que genera una unidad de polución por unidad de producto—.

* **Problema de la firma:**

$$
\begin{align*}
\max_{L_x} \; \Pi_x = P_x x - w L_x - P_D D_d = (P_x - P_D) f(L_x) - w L_x
\end{align*}
$$

Derivando e igualando a cero:

$$
\begin{align*}
\frac{\partial \Pi_x}{\partial L_x} = (P_x - P_D)\frac{\partial f}{\partial L_x} - w = 0 \implies \frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x - P_D}{w}
\end{align*}
$$

* **Problema del consumidor:** recibe el ingreso `$P_D D_o$` por ofrecer derechos, y como en equilibrio `$x = D_o$`, la utilidad depende de `$D_o$`:

$$
\begin{align*}
\max_{x_c, \ell_c, D_o} \; U(x_c, \ell_c, D_o) \quad \text{s.a.} \quad \Pi_x + w\bar{L} + P_D D_o = P_x x_c + w\ell_c
\end{align*}
$$

Planteando el Lagrangiano `$\mathcal{L} = U(x_c, \ell_c, D_o) + \lambda[\Pi_x + w\bar{L} + P_D D_o - P_x x_c - w\ell_c]$`, obtenemos las C.P.O.:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial x_c} &= \frac{\partial U}{\partial x_c} - \lambda P_x = 0 \\
\frac{\partial \mathcal{L}}{\partial \ell_c} &= \frac{\partial U}{\partial \ell_c} - \lambda w = 0 \\
\frac{\partial \mathcal{L}}{\partial D_o} &= \frac{\partial U}{\partial D_o} + \lambda P_D = 0
\end{align*}
$$

De `$(10)$` y `$(11)$` se mantiene `$\frac{\partial U / \partial x_c}{\partial U / \partial \ell_c} = \frac{P_x}{w}$`. De `$(11)$` despejamos `$\lambda = \frac{\partial U / \partial \ell_c}{w}$`, y sustituyendo en `$(12)$`:

$$
\begin{align*}
P_D = -\frac{\frac{\partial U}{\partial D_o}}{\lambda} = -\frac{\frac{\partial U}{\partial D_o}}{\frac{\partial U}{\partial \ell_c}} \cdot w
\end{align*}
$$

En equilibrio de mercado de derechos `$D_o = D_d = x$`, por lo que `$\frac{\partial U}{\partial D_o} = \frac{\partial U}{\partial x}$`:

$$
\begin{align*}
P_D = -\frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}} \cdot w
\end{align*}
$$

Reemplazando `$(13)$` en `$(9)$`, despejamos `$\frac{P_x}{w}$`:

$$
\begin{align*}
\frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x}{w} + \frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}} \implies \frac{1}{\frac{\partial f}{\partial L_x}} - \frac{\frac{\partial U}{\partial x}}{\frac{\partial U}{\partial \ell_c}} = \frac{P_x}{w} = \frac{\frac{\partial U}{\partial x_c}}{\frac{\partial U}{\partial \ell_c}}
\end{align*}
$$

¡Se recupera exactamente la condición de eficiencia de Pareto `$(7)$`!

#### Caso 2: Los derechos de propiedad se asignan a favor de la firma

Ahora la firma posee el derecho a emitir hasta una **contaminación potencial máxima `$\bar{Q}$`**. Si produce `$x$` unidades, le sobran derechos `$D_o = \bar{Q} - x$` que puede vender al consumidor al precio `$P_D$`.

* **Problema de la firma:**

$$
\begin{align*}
\max_{L_x} \; \Pi_x = P_x x - w L_x + P_D(\bar{Q} - x) = (P_x - P_D)f(L_x) - w L_x + P_D \bar{Q}
\end{align*}
$$

Como `$P_D \bar{Q}$` es una constante, la C.P.O. respecto a `$L_x$` es idéntica a `$(9)$`:

$$
\begin{align*}
\frac{\partial \Pi_x}{\partial L_x} = (P_x - P_D)\frac{\partial f}{\partial L_x} - w = 0 \implies \frac{1}{\frac{\partial f}{\partial L_x}} = \frac{P_x - P_D}{w}
\end{align*}
$$

* **Problema del consumidor:** compra derechos `$D_d$` para reducir la contaminación efectiva que soporta a `$k = \bar{Q} - D_d$`:

$$
\begin{align*}
\max_{x_c, \ell_c, D_d} \; U(x_c, \ell_c, \bar{Q} - D_d) \quad \text{s.a.} \quad \Pi_x + w\bar{L} = P_x x_c + w\ell_c + P_D D_d
\end{align*}
$$

Planteando `$\mathcal{L} = U(x_c, \ell_c, \bar{Q} - D_d) + \lambda[\Pi_x + w\bar{L} - P_x x_c - w\ell_c - P_D D_d]$`, las C.P.O. son:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial x_c} &= \frac{\partial U}{\partial x_c} - \lambda P_x = 0 \\
\frac{\partial \mathcal{L}}{\partial \ell_c} &= \frac{\partial U}{\partial \ell_c} - \lambda w = 0 \\
\frac{\partial \mathcal{L}}{\partial D_d} &= \frac{\partial U}{\partial k}(-1) - \lambda P_D = 0
\end{align*}
$$

De `$(16)$` y `$(17)$` resulta `$\frac{\partial U / \partial x_c}{\partial U / \partial \ell_c} = \frac{P_x}{w}$`, y de `$(18)$` con `$\lambda = \frac{\partial U / \partial \ell_c}{w}$` se obtiene `$P_D = -\frac{\partial U / \partial k}{\partial U / \partial \ell_c} \cdot w$`. Como en equilibrio `$k = \bar{Q} - D_d = \bar{Q} - (\bar{Q} - x) = x$`, el precio `$P_D$` y la asignación de producción `$x^*$` vuelven a ser **eficientes**.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/coase-edgeworth-light.svg" alt="Caja de Edgeworth de Coase con dinero y humo." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/coase-edgeworth-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: ambas asignaciones X y X son eficientes aunque difiere el bienestar.</figcaption>
</figure>

* **Limitaciones prácticas de Coase:** definición y cumplimiento de los derechos de propiedad, altos costos de transacción y regulación, y problemas de acción colectiva cuando hay múltiples afectados que deben coordinarse para comprar derechos al contaminador (incentivo al *free rider*).

---

## 4. Impuestos vs. Normas: análisis gráfico y de bienestar

Supongamos que la autoridad ambiental fija una **norma** igual al nivel de daño permisible `$q_S$` (producción socialmente eficiente) o una **tasa/impuesto `$t$`** calibrado para alcanzar exactamente esa misma cantidad `$q_S$`. ¿Quién gana y quién pierde bajo cada instrumento?

### 4.1 Caso 1: Firma precio-aceptante con demanda perfectamente elástica —`$P$` fijo—

Cuando la empresa enfrenta un precio de mercado fijo `$P$` (demanda horizontal), no puede trasladar el impuesto al consumidor porque perdería todo el mercado:

* **Equilibrio sin intervención `$(E)$`:** `$P = CMg_T(q_E)$`, con producción privada `$q_E$`.
* **Óptimo social `$(C)$`:** `$P = CMg_S(q_S) = CMg_T(q_S) + CMg_c(q_S)$`, con producción `$q_S < q_E$`.
* **Impuesto requerido `$(t)$`:** `$t = P - f = C - d$`, donde `$f = CMg_T(q_S)$`.

Comparación de impactos sobre el excedente (áreas del gráfico):

| Agente | Bajo Norma `$(q \le q_S)$` | Bajo Impuesto `$(t = C - d)$` |
| :--- | :--- | :--- |
| **Empresa** | Pierde el triángulo `$ECd$` `$(-)$` | Pierde el triángulo `$ECd$` más el rectángulo recaudado `$acdf$` `$(-)$` |
| **Consumidor** | `$0$` —precio fijo; si busca sustituir completamente, no asume alza de precio— | `$0$` |
| **Gobierno** | `$0$` | Recauda el rectángulo `$acdf$` `$(+)$` |
| **Ganancia ambiental** | Área bajo `$CMg_c$` entre `$q_S$` y `$q_E$`: trapecio `$\alpha \beta \gamma \delta$` `$(+)$` | Trapecio `$\alpha \beta \gamma \delta$` `$(+)$` |

<figure class="eco-figure">
  <img src="/assets/figures/micro2/impuestos-normas-fijo-light.svg" alt="Impuestos frente a normas con precio fijo." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/impuestos-normas-fijo-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: areas de perdida, recaudacion y ganancia ambiental.</figcaption>
</figure>

### 4.2 Caso 2: Equilibrio general con demanda de pendiente negativa `$(DD)$`

Cuando toda la industria es regulada y la demanda agregada `$DD$` tiene pendiente negativa, las empresas logran **trasladar parte del impuesto al consumidor**:

* **Equilibrio privado `$(E)$`:** intersección de `$DD$` y `$CMg_T$`, con cantidad `$q_E$` y precio `$P_E$`.
* **Equilibrio social `$(g)$`:** intersección de `$DD$` y `$CMg_S$`, con cantidad `$q_S$` y precio al consumidor `$h > P_E$`. El precio neto recibido por la firma baja a `$f < P_E$`, y la cuña fiscal es `$t = h - f$` —segmento `$gd$`—.

Comparación de impactos bajo demanda con pendiente negativa:

| Agente | Bajo Norma `$(q \le q_S)$` | Bajo Impuesto `$(t = h - f)$` |
| :--- | :--- | :--- |
| **Empresa** | Pierde `$ECd$` `$(-)$` | Pierde `$ECd + acdf$` `$(-)$` |
| **Consumidor** | Pierde el triángulo `$gEc$` `$(-)$` por menor cantidad a mayor valoración | Pierde `$gEc + hgca$` `$(-)$` |
| **Gobierno** | `$0$` | Recauda el rectángulo `$hgdf$` `$(+)$` |
| **Ganancia ambiental** | Trapecio `$\alpha \beta \gamma \delta$` `$(+)$` | Trapecio `$\alpha \beta \gamma \delta$` `$(+)$` |

> **Intuición económica:** **Las normas son más baratas para la empresa** —porque no pagan por las unidades que sí se les permite producir hasta `$q_S$`—, pero **los impuestos benefician a la sociedad** al generar ingresos fiscales reciclables y mantener un incentivo dinámico permanente para adoptar o desarrollar tecnologías más limpias.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/impuestos-normas-dd-light.svg" alt="Impuestos frente a normas con demanda de pendiente negativa." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/impuestos-normas-dd-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el impuesto se traslada en parte al consumidor.</figcaption>
</figure>

---

## 5. Modelo de decisiones simultáneas con tecnologías de mitigación (Tobón y Vasco)

En la práctica, cuando una firma enfrenta un impuesto ambiental `$t$`, no solo decide cuánto producir: puede instalar tecnologías de mitigación al final del proceso (*end of pipe*) y decidir simultáneamente **cuánto produce, cuánto descontamina y cuánto paga por impuestos**.

### 5.1 Equilibrio parcial: empresa productora de talco

Considere una empresa competitiva productora de talco con estructura de costos `$C_T = 0.7 q_T^2$` y precio internacional fijo `$P_T = 1$`. Su contaminación genera un daño estimado de `$C_c = 0.6 q_c^2$` (suponiendo `1` unidad de contaminación por unidad de talco).

1. **Equilibrio privado:** `$P_T = CMg_T \implies 1 = 1.4 q_T \implies q_T = 0.7143$`.
2. **Equilibrio social:** `$P_T = CMg_S = CMg_T + CMg_c \implies 1 = 1.4 q_S + 1.2 q_S = 2.6 q_S \implies q_S = 0.3846 < q_T$`.
3. **Impuesto pigouviano `$(t)$`:** en la formulación ad-valorem `$P_T(1 - t) = CMg_T(q_S)$`, tenemos `$1(1 - t) = 1.4(0.3846) = 0.5384 \implies t = 0.462$` —equivalente a `$\$0.462$` por unidad cuando `$P_T = 1$`—.

Ahora introducimos una tecnología de mitigación (filtros para reducir el polvo de los esquistos) con costo `$C_D(q_D)$`. Evaluamos dos regímenes:

#### Régimen A: Tecnología de mitigación barata `$(CMg_D < CMg_c)$`

Sea `$C_D = 0.4 q_D^2 \implies CMg_D = 0.8 q_D$`. Primero medimos el **potencial de mitigación** igualando el costo marginal de descontaminar al impuesto:

$$
\begin{align*}
CMg_D = t \implies 0.8 q_D = 0.462 \implies q_D = 0.578 > q_S
\end{align*}
$$

Como el potencial de la máquina excede incluso la producción social óptima, resulta siempre más barato descontaminar que pagar impuestos.

* **Corolario:** cuando `$CMg_D < CMg_c$`, la empresa **descontamina toda su producción**, **no paga impuestos** y produce `$q_{TD}$` tal que el precio cubre la suma de los costos marginales de producción y descontaminación:

$$
\begin{align*}
P_T = CMg_{TD} = CMg_T + CMg_D \implies 1 = 1.4 q_{TD} + 0.8 q_{TD} = 2.2 q_{TD} \implies q_{TD} = 0.4545
\end{align*}
$$

Observe que `$q_S = 0.3846 < q_{TD} = 0.4545 < q_T = 0.7143$`: la sociedad obtiene mayor producción que sin tecnología de mitigación y cero contaminación neta.

#### Régimen B: Tecnología de mitigación costosa `$(CMg_D > CMg_c)$`

Sea ahora `$C_D = 0.8 q_D^2 \implies CMg_D = 1.6 q_D$`. Calculamos primero hasta dónde conviene usar el filtro:

$$
\begin{align*}
CMg_D = t \implies 1.6 q_D = 0.462 \implies q_D = 0.2888 \approx 0.29
\end{align*}
$$

Si el productor usara la máquina indistintamente para toda su producción `$(P_T = CMg_T + CMg_D = 1.4 q + 1.6 q = 3.0 q = 1)$`, produciría `$q_{TD} = 0.333 < q_S = 0.3846$`, lo cual es irracional. La decisión óptima combina ambos instrumentos mediante un **salto de curvas**:
* Para las primeras `$q_D = 0.29$` unidades, es más barato descontaminar que pagar el impuesto `$(CMg_D < t)$`: la firma se mueve sobre la curva `$CMg_{TD}$` y descontamina esas `$0.29$` unidades.
* Para las unidades restantes entre `$q_D = 0.29$` y `$q_S = 0.3846$`, es más barato pagar el impuesto `$(t < CMg_D)$`: la firma salta a la curva `$CMg_T$` y paga el impuesto `$t = 0.462$` por cada unidad restante `$(q_S - q_D = 0.0946)$`.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/mitigacion-tobon-light.svg" alt="Mitigacion con salto de curvas y pago de impuestos." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/mitigacion-tobon-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: conviene descontaminar hasta qD y pagar impuesto por el resto.</figcaption>
</figure>

### 5.2 Extensión a Equilibrio General (oferta y demanda agregadas)

Si pasamos a una economía con demanda agregada inversa `$D_T = 5 - 0.6 q_T^2$` manteniendo `$C_T = 0.7 q_T^2$` y `$C_c = 0.6 q_c^2$`:

1. **Equilibrio de mercado:** `$1.4 q_T = 5 - 0.6 q_T^2 \implies q_T = 1.94$`, `$P_T = 2.72$`.
2. **Equilibrio social:** `$2.6 q_S = 5 - 0.6 q_S^2 \implies q_S = 1.44$`, `$P_{ST} = 3.75$`. A diferencia del equilibrio parcial, aquí parte del impuesto se traslada al consumidor —`$P_T$` sube de `$2.72$` a `$3.75$`—, y la producción cae menos que en el caso parcial; el impuesto que implementa este óptimo es `$P_{ST}(1 - t) = CMg_T(q_S) \implies t = 0.46$`.
3. **Con tecnología barata `$(C_D = 0.4 q_D^2)$`:** `$CMg_T + CMg_D = 2.2 q_{TD} = 5 - 0.6 q_{TD}^2 \implies q_{TD} = 1.59$`, `$P_{TD} = 3.49$`, mejorando el bienestar frente al escenario sin mitigación.
4. **Con tecnología costosa `$(C_D = 0.8 q_D^2)$`:** la firma descontamina hasta `$CMg_D = t$` `$(q_D = 0.29)$`, produce `$q_S = 1.44$` y paga impuestos `$t(q_S - q_D)$`.

---

## 6. Casos y políticas ambientales en Colombia y resiliencia ecológica

En el contexto colombiano, estos instrumentos se reflejan en políticas concretas estudiadas en el curso:
* **Regulación de movilidad y emisiones:** *Pico y Placa* y su exención onerosa en Bogotá y Medellín; estándares para fuentes móviles terrestres (Resolución 2254 de 2017, Ley 1972 de 2019 y Resolución 0762 de 2022).
* **Impuesto al carbono y mercados de carbono:** tarifa indexada al `$\text{IPC} + 1\%$` desde 2017 `$(\$29.070\text{ COP/tCO}_2\text{e})$`, coexistiendo con mercados voluntarios y debates regulatorios sobre el límite de no causación del `$50\%$`.
* **Tasas retributivas y ruido:** tasas por uso del agua y por vertimientos (DBO y SST); Ley 2450 de 2025 contra el ruido; impuesto nacional y prohibición gradual de bolsas plásticas (Ley 2232 de 2022).
* **Aplicación distributiva — Caso Coveñas:** en las playas de Coveñas, la población local de bajos ingresos y alta informalidad contamina el entorno marino frecuentado por turistas paisas de ingreso medio-alto. Aplicar aquí un impuesto directo a los lugareños sería regresivo e inviable institucionalmente; una solución coaseana o de pagos por servicios ambientales —financiada mediante una tasa turística o contribución de los visitantes para remunerar la limpieza y conservación a cargo de la comunidad local— maximiza el valor de la producción social respetando la equidad distributiva.
* **Resiliencia de sistemas naturales (Vargas, Tobón y Vasco, 2023):** cuando los ecosistemas tienen un umbral crítico de resiliencia `$N_t$` por debajo del cual colapsan, las políticas híbridas —combinando límites de Comando y Control con impuestos ambientales `$\tau^*$`— son necesarias para evitar que la contaminación acumulada cruce el umbral irreversible entre periodos.
