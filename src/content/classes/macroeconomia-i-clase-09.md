---
title: "Clase 09: Ejercicio de Optimización Intertemporal CES en Tres Períodos"
course: "macroeconomia-i"
order: 9
classType: "clase"
description: "Desarrollo directo paso a paso del problema de maximización con utilidad CES en tres períodos e impuestos, obtención de demandas óptimas y cálculo e interpretación de derivadas parciales."
math: true
---


Planteamiento del Ejercicio
---------------------------

El individuo vive tres períodos (`$t = 1, 2, 3$`) y busca maximizar una función de utilidad intertemporal con Elasticidad de Sustitución Constante (CES) sujeta a su restricción presupuestaria intertemporal con impuestos al consumo (`$\tau_c$`) e impuestos/ajustes al ingreso (`$\tau_y$`):

$$
\begin{align*}\max_{\{C_1, C_2, C_3\}} \quad & U(C_1, C_2, C_3) = \left[ \alpha_1 C_1^\rho + \alpha_2 C_2^\rho + (1 - \alpha_1 - \alpha_2) C_3^\rho \right]^{\frac{1}{\rho}} \\ \text{s.a.} \quad & (1 + \tau_c)C_1 + \frac{(1 + \tau_c)C_2}{1 + r} + \frac{(1 + \tau_c)C_3}{(1 + r)^2} = (1 + \tau_y)Y_1 + \frac{(1 + \tau_y)Y_2}{1 + r} + \frac{(1 + \tau_y)Y_3}{(1 + r)^2}\end{align*}
$$

> **Nota de notación:** Para compactar el álgebra intermedia, llamemos `$\alpha_3 \equiv 1 - \alpha_1 - \alpha_2$` al peso del tercer período, y definamos la riqueza fiscalmente ajustada (lado derecho de la restricción) como `$W$`:
> $$W \equiv (1 + \tau_y)Y_1 + \frac{(1 + \tau_y)Y_2}{1 + r} + \frac{(1 + \tau_y)Y_3}{(1 + r)^2}$$
> *(Si en una variante del problema el impuesto a la renta resta ingreso disponible, basta cambiar `$(1 + \tau_y)$` por `$(1 - \tau_y)$` sin que cambie ningún paso del despeje).*


Paso 1: Planteamiento del Lagrangiano
-------------------------------------

Construimos la función Lagrangiana integrando la función objetivo y la restricción presupuestaria multiplicada por `$\lambda$`:

$$
\begin{align*}\mathcal{L} = \left[ \alpha_1 C_1^\rho + \alpha_2 C_2^\rho + (1 - \alpha_1 - \alpha_2) C_3^\rho \right]^{\frac{1}{\rho}} + \lambda \left[ W - (1 + \tau_c)C_1 - \frac{(1 + \tau_c)C_2}{1 + r} - \frac{(1 + \tau_c)C_3}{(1 + r)^2} \right]\end{align*}
$$


Paso 2: Las Tres Derivadas (Condiciones de Primer Orden)
--------------------------------------------------------

Llamemos `$B \equiv \alpha_1 C_1^\rho + \alpha_2 C_2^\rho + (1 - \alpha_1 - \alpha_2) C_3^\rho$` al corchete interno. Al derivar respecto a cada consumo, baja el exponente `$\frac{1}{\rho}$`, el cual se cancela inmediatamente con el `$\rho$` que baja de `$C_t^\rho$`:

1. **Derivada respecto a `$C_1$`:**

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_1} = \frac{1}{\rho} B^{\frac{1}{\rho} - 1} \left( \rho \alpha_1 C_1^{\rho - 1} \right) - \lambda (1 + \tau_c) = 0 \implies B^{\frac{1}{\rho} - 1} \alpha_1 C_1^{\rho - 1} = \lambda (1 + \tau_c) \tag{9.1}\end{align*}
$$

2. **Derivada respecto a `$C_2$`:**

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_2} = \frac{1}{\rho} B^{\frac{1}{\rho} - 1} \left( \rho \alpha_2 C_2^{\rho - 1} \right) - \lambda \frac{1 + \tau_c}{1 + r} = 0 \implies B^{\frac{1}{\rho} - 1} \alpha_2 C_2^{\rho - 1} = \lambda \frac{1 + \tau_c}{1 + r} \tag{9.2}\end{align*}
$$

3. **Derivada respecto a `$C_3$`:**

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial C_3} = \frac{1}{\rho} B^{\frac{1}{\rho} - 1} \left( \rho (1 - \alpha_1 - \alpha_2) C_3^{\rho - 1} \right) - \lambda \frac{1 + \tau_c}{(1 + r)^2} = 0 \implies B^{\frac{1}{\rho} - 1} (1 - \alpha_1 - \alpha_2) C_3^{\rho - 1} = \lambda \frac{1 + \tau_c}{(1 + r)^2} \tag{9.3}\end{align*}
$$

4. **Derivada respecto a `$\lambda$`:**

$$
\begin{align*}\frac{\partial \mathcal{L}}{\partial \lambda} = W - (1 + \tau_c)C_1 - \frac{(1 + \tau_c)C_2}{1 + r} - \frac{(1 + \tau_c)C_3}{(1 + r)^2} = 0 \tag{9.4}\end{align*}
$$


Paso 3: Despejar $\lambda$, Igualar y Cancelar
----------------------------------------------

Despejamos `$\lambda$` de las ecuaciones `(1)`, `(2)` y `(3)`:

$$
\begin{align*}\lambda = \frac{B^{\frac{1}{\rho} - 1} \alpha_1 C_1^{\rho - 1}}{1 + \tau_c} = \frac{B^{\frac{1}{\rho} - 1} \alpha_2 C_2^{\rho - 1} (1 + r)}{1 + \tau_c} = \frac{B^{\frac{1}{\rho} - 1} (1 - \alpha_1 - \alpha_2) C_3^{\rho - 1} (1 + r)^2}{1 + \tau_c}\end{align*}
$$

### 1. Igualamos (1) con (2) para despejar $C_2$ en función de $C_1$

Cancelamos `$B^{\frac{1}{\rho} - 1}$` y `$(1 + \tau_c)$` a ambos lados:

$$
\begin{align*}\alpha_1 C_1^{\rho - 1} = \alpha_2 C_2^{\rho - 1} (1 + r) \implies C_2^{\rho - 1} = \left[ \frac{\alpha_1}{\alpha_2 (1 + r)} \right] C_1^{\rho - 1}\end{align*}
$$

Elevamos ambos lados a la potencia `$\frac{1}{\rho - 1}$` (o invirtiendo la fracción interna con exponente `$\frac{1}{1 - \rho}$`):

$$
\begin{align*}C_2 = \left[ \frac{\alpha_2 (1 + r)}{\alpha_1} \right]^{\frac{1}{1 - \rho}} C_1 \tag{9.5}\end{align*}
$$

### 2. Igualamos (1) con (3) para despejar $C_3$ en función de $C_1$

Cancelamos nuevamente `$B^{\frac{1}{\rho} - 1}$` y `$(1 + \tau_c)$` a ambos lados:

$$
\begin{align*}\alpha_1 C_1^{\rho - 1} = (1 - \alpha_1 - \alpha_2) C_3^{\rho - 1} (1 + r)^2 \implies C_3^{\rho - 1} = \left[ \frac{\alpha_1}{(1 - \alpha_1 - \alpha_2)(1 + r)^2} \right] C_1^{\rho - 1}\end{align*}
$$

Despejando `$C_3$`:

$$
\begin{align*}C_3 = \left[ \frac{(1 - \alpha_1 - \alpha_2)(1 + r)^2}{\alpha_1} \right]^{\frac{1}{1 - \rho}} C_1 \tag{9.6}\end{align*}
$$


Paso 4: Reemplazar en la R.P.I. y Despejar $C_1^*$
--------------------------------------------------

Sustituimos `(5)` y `(6)` dentro de la restricción presupuestaria `(4)`:

$$
\begin{align*}(1 + \tau_c)C_1 + \frac{1 + \tau_c}{1 + r} \left[ \frac{\alpha_2 (1 + r)}{\alpha_1} \right]^{\frac{1}{1 - \rho}} C_1 + \frac{1 + \tau_c}{(1 + r)^2} \left[ \frac{(1 - \alpha_1 - \alpha_2)(1 + r)^2}{\alpha_1} \right]^{\frac{1}{1 - \rho}} C_1 = W\end{align*}
$$

Simplificamos las potencias de `$(1 + r)$` usando `$\frac{(1 + r)^{\frac{1}{1 - \rho}}}{1 + r} = (1 + r)^{\frac{1}{1 - \rho} - 1} = (1 + r)^{\frac{\rho}{1 - \rho}}$` y factorizamos `$(1 + \tau_c)C_1$`:

$$
\begin{align*}(1 + \tau_c)C_1 \underbrace{\left[ 1 + \left( \frac{\alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{\rho}{1 - \rho}} + \left( \frac{1 - \alpha_1 - \alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{2\rho}{1 - \rho}} \right]}_{\equiv \Omega(r)} = W\end{align*}
$$

Despejando `$C_1^*$`, obtenemos la **función de consumo óptimo del período 1**:

$$
\begin{align*}C_1^* = \frac{(1 + \tau_y)Y_1 + \dfrac{(1 + \tau_y)Y_2}{1 + r} + \dfrac{(1 + \tau_y)Y_3}{(1 + r)^2}}{(1 + \tau_c) \left[ 1 + \left( \dfrac{\alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{\rho}{1 - \rho}} + \left( \dfrac{1 - \alpha_1 - \alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{2\rho}{1 - \rho}} \right]} \equiv \frac{W}{1 + \tau_c} \Omega(r)^{-1}\end{align*}
$$


Paso 5: Cálculo e Interpretación de las Derivadas Solicitadas
-------------------------------------------------------------

### 1. Derivada de $C_1^*$ respecto a $\tau_c$

$$
\begin{align*}\frac{\partial C_1^*}{\partial \tau_c} = -\frac{W}{(1 + \tau_c)^2} \Omega(r)^{-1} < 0\end{align*}
$$

* **Interpretación:** Un aumento en el impuesto al consumo encarece el precio efectivo de la canasta en todos los períodos, reduciendo el poder adquisitivo real de la riqueza y contrayendo directamente el consumo en el período 1.

### 2. Derivadas de $C_1^*$ respecto a $Y_1$, $Y_2$ y $Y_3$

Derivando respecto a cada ingreso laboral por separado:

$$
\begin{align*}\frac{\partial C_1^*}{\partial Y_1} &= \frac{1 + \tau_y}{(1 + \tau_c)\Omega(r)} > 0 \\ \frac{\partial C_1^*}{\partial Y_2} &= \frac{1 + \tau_y}{(1 + \tau_c)\Omega(r)} \cdot \frac{1}{1 + r} > 0 \\ \frac{\partial C_1^*}{\partial Y_3} &= \frac{1 + \tau_y}{(1 + \tau_c)\Omega(r)} \cdot \frac{1}{(1 + r)^2} > 0\end{align*}
$$

* **Interpretación:** Cualquier aumento en el ingreso presente o futuro incrementa el consumo hoy (suavizamiento del consumo). Sin embargo, como `$r > 0$`, se cumple que:
  $$\frac{\partial C_1^*}{\partial Y_1} > \frac{\partial C_1^*}{\partial Y_2} > \frac{\partial C_1^*}{\partial Y_3} > 0$$
  Los ingresos más lejanos en el tiempo tienen menor impacto sobre el consumo corriente porque sufren un mayor descuento financiero.

### 3. Derivada de $C_1^*$ respecto a la tasa de interés $r$

Aplicando la regla del producto sobre `$C_1^* = \frac{1}{1 + \tau_c} W(r) \Omega(r)^{-1}$`:

$$
\begin{align*}\frac{\partial C_1^*}{\partial r} = \frac{1}{1 + \tau_c} \left[ \frac{\partial W}{\partial r} \Omega(r)^{-1} - W \Omega(r)^{-2} \frac{\partial \Omega(r)}{\partial r} \right]\end{align*}
$$

donde:
* **Efecto riqueza humana (`$\frac{\partial W}{\partial r} < 0$`):**

$$
\begin{align*}\frac{\partial W}{\partial r} = -\frac{(1 + \tau_y)Y_2}{(1 + r)^2} - \frac{2(1 + \tau_y)Y_3}{(1 + r)^3} < 0\end{align*}
$$

* **Efecto sustitución / ingreso financiero (`$\frac{\partial \Omega(r)}{\partial r}$`):**

$$
\begin{align*}\frac{\partial \Omega(r)}{\partial r} = \left( \frac{\rho}{1 - \rho} \right) \left[ \left( \frac{\alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{\rho}{1 - \rho} - 1} + 2 \left( \frac{1 - \alpha_1 - \alpha_2}{\alpha_1} \right)^{\frac{1}{1 - \rho}} (1 + r)^{\frac{2\rho}{1 - \rho} - 1} \right]\end{align*}
$$

* **Interpretación según `$\rho$`:**
  * Si **`$0 < \rho < 1$`** (alta sustituibilidad intertemporal, `$EIS = \frac{1}{1 - \rho} > 1$`): `$\frac{\partial \Omega}{\partial r} > 0$`, por lo que ambos términos dentro del corchete son negativos y inequívocamente **`$\frac{\partial C_1^*}{\partial r} < 0$`** (domina el efecto sustitución junto con el menor valor presente de `$Y_2$` y `$Y_3$`).
  * Si **`$\rho = 0$`** (caso límite Cobb-Douglas): `$\frac{\partial \Omega}{\partial r} = 0$` y queda únicamente el efecto riqueza negativo sobre los ingresos futuros (`$\frac{\partial C_1^*}{\partial r} < 0$`).
  * Si **`$\rho < 0$`** (baja sustituibilidad, `$EIS < 1$`): `$\frac{\partial \Omega}{\partial r} < 0$`, generándose un efecto ingreso positivo que compite contra la caída del valor presente de `$Y_2$` y `$Y_3$`.

### 4. Derivada del Ahorro $S_1^*$ respecto a $r$

El ahorro privado en el primer período es el ingreso neto menos el gasto total en consumo:

$$
\begin{align*}S_1^* = (1 + \tau_y)Y_1 - (1 + \tau_c)C_1^*\end{align*}
$$

Derivando respecto a `$r$`:

$$
\begin{align*}\frac{\partial S_1^*}{\partial r} = -(1 + \tau_c) \frac{\partial C_1^*}{\partial r}\end{align*}
$$

* **Interpretación:** El ahorro reacciona exactamente con el signo opuesto al del consumo presente. Cuando `$0 \leq \rho < 1$`, dado que `$\frac{\partial C_1^*}{\partial r} < 0$`, tenemos que **`$\frac{\partial S_1^*}{\partial r} > 0$`**: un incremento en la tasa de interés premia la postergación del consumo y estimula un mayor ahorro en el primer período.
