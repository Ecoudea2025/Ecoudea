---
title: "Clase 15: Gobierno y Política Fiscal: Déficit, Restricción Intertemporal e Inflación"
course: "macroeconomia-i"
order: 15
classType: "clase"
description: "Definición de déficit primario y déficit total, deducción iterativa de la restricción presupuestaria intertemporal del gobierno, condición de solvencia y efecto de la inflación sobre la deuda real."
math: true
---


Contabilidad Fiscal: Déficit Primario y Déficit Total
-----------------------------------------------------

Habiendo estudiado a las familias (Cap. 3) y a las empresas (Cap. 4), incorporamos ahora al tercer gran actor macroeconómico: **el Gobierno y la Política Fiscal**, siguiendo el Capítulo 5 de De Gregorio (*Macroeconomía: teoría y políticas*).

Definimos las cuatro variables fundamentales de las cuentas públicas en el período `$t$`:

* **`$G_t$`:** Gasto público no financiero (compras finales de bienes y servicios, salarios públicos, inversión en infraestructura y transferencias).
* **`$T_t$`:** Recaudo tributario (ingresos por impuestos directos e indirectos netos de subsidios).
* **`$B_t$`:** Stock de deuda pública neta vigente al inicio del período `$t$`.
* **`$i_t$`:** Tasa de interés nominal que el Estado paga por su deuda pública.

### 1. El Déficit Primario ($DF_t$)

El **déficit primario** (también llamado déficit operacional) mide la diferencia entre los gastos corrientes del programa de gobierno y sus ingresos tributarios, **excluyendo el pago de intereses de la deuda**:

$$
\begin{align*}\boxed{DF_t \equiv G_t - T_t = \text{Déficit primario del gobierno}}\end{align*}
$$

* **Si `$G_t > T_t$`:** El fisco incurre en un **déficit primario** (`$DF_t > 0$`).
* **Si `$T_t > G_t$`:** El fisco genera un **superávit primario** (`$T_t - G_t > 0$`), lo que le deja recursos netos disponibles para abonar al pago de su deuda.

### 2. Servicio de la Deuda y Déficit Total (Global)

Además de sus gastos programáticos `$G_t$`, el gobierno debe pagar los intereses generados por la deuda heredada del pasado:

$$
\begin{align*}i_t B_t = \text{Servicio de intereses de la deuda pública}\end{align*}
$$

Al sumar el déficit primario más el servicio de intereses, obtenemos el **déficit fiscal total (o global)**, el cual representa la **necesidad total de financiamiento** del Estado en el período `$t$`:

$$
\begin{align*}G_t - T_t + i_t B_t = \boxed{\text{Déficit total}} = \text{Necesidad de financiamiento}\end{align*}
$$

### 3. Ley de Movimiento de la Deuda Pública

Cuando los gastos totales (incluyendo intereses) superan a los impuestos, el gobierno debe cubrir esa brecha emitiendo **nueva deuda pública** (`$\Delta B_{t+1} = B_{t+1} - B_t$`):

$$
\begin{align*}\text{Déficit total} = \Delta B_{t+1} = B_{t+1} - B_t = G_t - T_t + i_t B_t\end{align*}
$$

Pasando `$B_t$` a sumar al lado derecho y factorizando, obtenemos la **ecuación dinámica de acumulación de la deuda pública**:

$$
\begin{align*}\boxed{B_{t+1} = G_t - T_t + (1 + i_t) B_t}\end{align*}
$$


Construcción Paso a Paso de la R.P.I. del Gobierno
--------------------------------------------------

Al igual que los hogares, el Estado enfrenta una restricción presupuestaria intertemporal. Escribamos la ecuación de evolución de la deuda para los períodos sucesivos `$t, t+1, t+2$`:

$$
\begin{align*}B_{t+1} &= G_t - T_t + (1 + i_t) B_t \\ B_{t+2} &= G_{t+1} - T_{t+1} + (1 + i_{t+1}) B_{t+1} \\ B_{t+3} &= G_{t+2} - T_{t+2} + (1 + i_{t+2}) B_{t+2}\end{align*}
$$

Supongamos que la tasa de interés `$i$` es constante y que medimos las variables sin inflación (`$\pi_t = 0$`, de modo que `$i = r$`).

### Paso 1: Despejar los stocks de deuda de cada período

Dividiendo cada ecuación entre `$(1 + i)$`:

$$
\begin{align*}\frac{B_{t+1}}{1 + i} &= \frac{G_t - T_t}{1 + i} + B_t \tag{15.1} \\ \frac{B_{t+2}}{1 + i} &= \frac{G_{t+1} - T_{t+1}}{1 + i} + B_{t+1} \implies B_{t+1} = \frac{B_{t+2}}{1 + i} - \frac{G_{t+1} - T_{t+1}}{1 + i} \tag{15.2} \\ \frac{B_{t+3}}{1 + i} &= \frac{G_{t+2} - T_{t+2}}{1 + i} + B_{t+2} \implies B_{t+2} = \frac{B_{t+3}}{1 + i} - \frac{G_{t+2} - T_{t+2}}{1 + i} \tag{15.3}\end{align*}
$$

### Paso 2: Sustitución recursiva hacia adelante

Sustituimos `$B_{t+1}$` de `(2)` en el lado izquierdo de `(1)`:

$$
\begin{align*}\frac{1}{1 + i} \left( \frac{B_{t+2}}{1 + i} - \frac{G_{t+1} - T_{t+1}}{1 + i} \right) &= \frac{G_t - T_t}{1 + i} + B_t \\ \frac{B_{t+2}}{(1 + i)^2} - \frac{G_{t+1} - T_{t+1}}{(1 + i)^2} &= \frac{G_t - T_t}{1 + i} + B_t\end{align*}
$$

Ahora sustituimos `$B_{t+2}$` usando `(3)`:

$$
\begin{align*}\frac{1}{(1 + i)^2} \left( \frac{B_{t+3}}{1 + i} - \frac{G_{t+2} - T_{t+2}}{1 + i} \right) - \frac{G_{t+1} - T_{t+1}}{(1 + i)^2} &= \frac{G_t - T_t}{1 + i} + B_t \\ \frac{B_{t+3}}{(1 + i)^3} - \frac{G_{t+2} - T_{t+2}}{(1 + i)^3} - \frac{G_{t+1} - T_{t+1}}{(1 + i)^2} &= \frac{G_t - T_t}{1 + i} + B_t\end{align*}
$$

### Paso 3: Multiplicación por $(1 + i)$ y Reordenamiento

Multiplicamos ambos lados de la ecuación por `$(1 + i)$`:

$$
\begin{align*}\frac{B_{t+3}}{(1 + i)^2} - \frac{G_{t+2} - T_{t+2}}{(1 + i)^2} - \frac{G_{t+1} - T_{t+1}}{1 + i} = G_t - T_t + (1 + i) B_t\end{align*}
$$

Despejamos la deuda inicial capitalizada `$(1 + i)B_t$`:

$$
\begin{align*}(1 + i) B_t = -(G_t - T_t) - \frac{G_{t+1} - T_{t+1}}{1 + i} - \frac{G_{t+2} - T_{t+2}}{(1 + i)^2} + \frac{B_{t+3}}{(1 + i)^2}\end{align*}
$$

Introduciendo el signo menos dentro de cada paréntesis (`$-(G - T) = T - G$`, que es el **superávit primario**) e iterando hasta el período `$t + N$`:

$$
\begin{align*}(1 + i) B_t = (T_t - G_t) + \frac{T_{t+1} - G_{t+1}}{1 + i} + \frac{T_{t+2} - G_{t+2}}{(1 + i)^2} + \ldots + \frac{T_{t+N} - G_{t+N}}{(1 + i)^N} + \frac{B_{t+N+1}}{(1 + i)^N}\end{align*}
$$

En forma compacta de sumatoria:

$$
\begin{align*}(1 + i) B_t = \sum_{j=0}^N \frac{T_{t+j} - G_{t+j}}{(1 + i)^j} + \frac{B_{t+N+1}}{(1 + i)^N}\end{align*}
$$


Condición de Solvencia Fiscal (No-Ponzi)
----------------------------------------

Para que el Estado sea **solvente**, no puede financiar perpetuamente su deuda emitiendo nueva deuda a una tasa igual o superior a `$i$` (esquema Ponzi). 

* En un horizonte finito: `$B_{t+N+1} = 0$`.
* En un horizonte infinito (`$N \to \infty$`): aun si `$B_{t+N+1} \neq 0$`, la deuda debe crecer más lento que la tasa de interés para que su valor presente converja a cero:

$$
\begin{align*}\lim_{N \to \infty} \frac{B_{t+N+1}}{(1 + i)^N} = 0 \quad \text{(Condición de Transversalidad / No-Ponzi)}\end{align*}
$$

Bajo esta condición, llegamos a la **Restricción Presupuestaria Intertemporal del Gobierno**:

$$
\begin{align*}\boxed{(1 + i) B_t = \sum_{j=0}^\infty \frac{T_{t+j} - G_{t+j}}{(1 + i)^j}}\end{align*}
$$

> **Regla de Oro de la Solvencia Fiscal:** *"La deuda pública vigente en el período `$t$` más sus intereses (`$(1 + i)B_t$`) tiene que ser exactamente igual al valor presente de los superávits primarios (`$T_{t+j} - G_{t+j}$`) que el gobierno generará en el futuro."* Un país que parte con deuda positiva no puede tener déficit primario permanente; tarde o temprano deberá ajustar sus finanzas para generar superávits primarios.


Efecto de la Inflación sobre la Evolución de la Deuda Real
----------------------------------------------------------

¿Qué ocurre con la dinámica de la deuda pública cuando existe inflación (`$\pi > 0$`)? Recordemos que el nivel de precios evoluciona según:

$$
\begin{align*}P_{t+1} = (1 + \pi) P_t \implies P_t = \frac{P_{t+1}}{1 + \pi}\end{align*}
$$

### Paso a Paso: De Deuda Nominal a Deuda Real

1. **Dividimos la ecuación nominal de la deuda entre el nivel de precios `$P_t$`:**

$$
\begin{align*}\frac{B_{t+1}}{P_t} = \frac{G_t - T_t}{P_t} + \frac{(1 + i) B_t}{P_t}\end{align*}
$$

2. **En el lado izquierdo, sustituimos `$P_t = \frac{P_{t+1}}{1 + \pi}$`:**

$$
\begin{align*}\frac{B_{t+1}}{\frac{P_{t+1}}{1 + \pi}} = \frac{B_{t+1}(1 + \pi)}{P_{t+1}} = \frac{G_t - T_t}{P_t} + (1 + i) \frac{B_t}{P_t}\end{align*}
$$

3. **Definimos las variables fiscales en términos reales con letras minúsculas:**
   * `$b_t \equiv \frac{B_t}{P_t}$` y `$b_{t+1} \equiv \frac{B_{t+1}}{P_{t+1}}$` (stock real de deuda pública).
   * `$g_t \equiv \frac{G_t}{P_t}$` (gasto público real).
   * `$t_t \equiv \frac{T_t}{P_t}$` (recaudo tributario real).

Sustituyendo las minúsculas en nuestra ecuación:

$$
\begin{align*}b_{t+1}(1 + \pi) = g_t - t_t + (1 + i) b_t\end{align*}
$$

4. **Dividimos toda la ecuación por `$(1 + \pi)$`:**

$$
\begin{align*}b_{t+1} = \frac{g_t - t_t}{1 + \pi} + \left( \frac{1 + i}{1 + \pi} \right) b_t\end{align*}
$$

Reconociendo la identidad exacta de Fisher `$\frac{1 + i}{1 + \pi} = 1 + r$`, obtenemos la **ecuación de evolución de la deuda pública real**:

$$
\begin{align*}\boxed{b_{t+1} = \frac{g_t - t_t}{1 + \pi} + (1 + r) b_t}\end{align*}
$$

* **Efecto licuación de la inflación:** Un aumento sorpresivo en la inflación `$\pi$` reduce el peso real del déficit primario corriente (`$\frac{g_t - t_t}{1 + \pi}$`) y, para una tasa nominal `$i$` contratada previamente en moneda local, reduce la tasa de interés real ex-post `$r$`, amortizando parte del valor real de la deuda.
* En la próxima clase introduciremos el segundo gran determinante de la sostenibilidad fiscal: **el crecimiento económico del PIB real (`$\gamma$` o `$\nu$`)**, analizando la evolución de la razón Deuda/PIB (`$\frac{B_t}{Y_t}$`).

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/superavits-light.svg" alt="Barra de déficit hoy seguida de barras decrecientes de superávits futuros." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/superavits-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: el déficit de hoy se paga con una senda de superávits futuros que cubre la deuda.</figcaption>
</figure>
