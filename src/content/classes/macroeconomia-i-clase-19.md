---
title: "Clase 19: Oferta de Trabajo y Sustitución Intertemporal del Ocio"
course: "macroeconomia-i"
order: 19
classType: "clase"
description: "Deducción paso a paso de la función de oferta de trabajo a partir de las C.P.O. del consumidor, demostración de su pendiente positiva y análisis gráfico y analítico de sus desplazamientos ante cambios en la tasa de interés real."
math: true
---

Sistema de Condiciones de Primer Orden del Consumidor
----------------------------------------------------

Retomamos las cinco Condiciones de Primer Orden (C.P.O.) deducidas en la clase anterior para el problema intertemporal de las familias en el Modelo de Equilibrio General Real:

$$
\begin{align*}
\frac{\partial \mathcal{L}}{\partial C_1} &= \frac{\partial u(\cdot)}{\partial C_1} - \lambda = 0 \\
\frac{\partial \mathcal{L}}{\partial C_2} &= \beta \frac{\partial u(\cdot)}{\partial C_2} - \frac{\lambda}{1 + r} = 0 \\
\frac{\partial \mathcal{L}}{\partial N_1} &= -\frac{\partial u(\cdot)}{\partial \ell_1} + \lambda W_1 = 0 \\
\frac{\partial \mathcal{L}}{\partial N_2} &= -\beta \frac{\partial u(\cdot)}{\partial \ell_2} + \frac{\lambda W_2}{1 + r} = 0 \\
\frac{\partial \mathcal{L}}{\partial \lambda} &= -C_1 - \frac{C_2}{1 + r} + W_1 N_1 + \Pi_1 - T_1 + \frac{W_2 N_2 + \Pi_2 - T_2}{1 + r} = 0
\end{align*}
$$

Con base en este sistema de ecuaciones derivaremos formalmente la **función de oferta de trabajo `$(N^s)$`**, demostraremos por qué tiene pendiente positiva en el plano `$(N, W)$` y deduciremos hacia dónde se desplaza cuando varía la tasa de interés real `$r$`.


Deducción de la Curva de Oferta de Trabajo y Su Pendiente
---------------------------------------------------------

Combinando las ecuaciones **`(1)` y `(3)`** (despejando `$\lambda = U_{mg C_1}$` de `(1)` y reemplazando en `(3)`), obtenemos la ecuación que gobierna la **función de oferta de trabajo** en el período `$t = 1$`:

$$
\begin{align*}
U_{mg \ell_1} = U_{mg C_1} W_1
\end{align*}
$$

Recordemos las dos propiedades fundamentales de la utilidad marginal del ocio `$(U_{mg \ell_1})$`:

1. Es estrictamente positiva: `$U_{mg \ell_1} > 0$`.
2. Es estrictamente decreciente respecto al ocio (por concavidad de `$u$`):

$$
\begin{align*}
\frac{\partial U_{mg \ell_1}}{\partial \ell_1} = \frac{\partial^2 u(\cdot)}{\partial \ell_1^2} < 0
\end{align*}
$$

### Demostración de la Pendiente Positiva `$(\frac{\partial N}{\partial W} > 0)$`

Evaluemos qué sucede cuando sube el salario real `$W_1$` (manteniendo constante la utilidad marginal del consumo `$U_{mg C_1}$` para aislar el efecto sustitución puro). Derivamos el lado derecho de la condición intratemporal respecto a `$W_1$`:

$$
\begin{align*}
\frac{\partial [U_{mg C_1} W_1]}{\partial W_1} = U_{mg C_1} > 0
\end{align*}
$$

El hecho de que esta derivada sea estrictamente positiva implica que, al aumentar `$W_1$`, el lado derecho de `$U_{mg \ell_1} = U_{mg C_1} W_1$` aumenta. Para que la igualdad vuelva a cumplirse, el lado izquierdo `$(U_{mg \ell_1})$` también debe **aumentar**.

Ahora bien, como `$\frac{\partial U_{mg \ell_1}}{\partial \ell_1} < 0$`, la única manera de que aumente la utilidad marginal del ocio es **disminuyendo la cantidad de ocio `$(\nabla \ell_1)$`**. Y puesto que el tiempo total `$h$` es fijo `$(\ell_1 = h - N_1)$`, reducir el ocio equivale necesariamente a **aumentar las horas trabajadas `$(\Delta N_1)$`**:

$$
\begin{align*}
\Delta W_1 \implies \Delta (U_{mg C_1} W_1) \implies \Delta U_{mg \ell_1} \implies \nabla \ell_1 \implies \Delta N_1
\end{align*}
$$

Por consiguiente, la pendiente de la **curva de oferta de trabajo** es positiva:

$$
\begin{align*}
\frac{\partial N}{\partial W} > 0 \iff \text{Curva de oferta de trabajo creciente}
\end{align*}
$$

> **Intuición económica:** Un mayor salario real encarece el precio relativo del ocio: cada hora que el individuo decide descansar le cuesta más bienes de consumo que deja de comprar. Por este efecto sustitución, ofrece más horas de trabajo cuando sube `$W_1$`.


Desplazamiento de la Oferta de Trabajo ante Cambios en `$r$`
----------------------------------------------------------

Supongamos ahora que el salario corriente `$W_1$` permanece fijo, pero cambia la **tasa de interés real `$(r)$`**. ¿Se desplaza la curva de oferta de trabajo hacia la derecha o hacia la izquierda? Para demostrarlo analíticamente, utilizamos las dos condiciones del trabajo: las ecuaciones **`(3)` y `(4)`**.

### Paso 1: Relación Intertemporal entre Ocio Presente y Ocio Futuro

Despejamos el término con `$\lambda$` en cada ecuación:

- De **`(3)`**: `$U_{mg \ell_1} = \lambda W_1 \implies \lambda = \frac{U_{mg \ell_1}}{W_1}$`.
- De **`(4)`**: `$\beta U_{mg \ell_2} = \frac{\lambda W_2}{1 + r} \implies \lambda = \frac{\beta U_{mg \ell_2} (1 + r)}{W_2}$`.

Dividiendo la ecuación `(3)` entre la ecuación `(4)` (equivalentemente, igualando `$\lambda$` en ambas):

$$
\begin{align*}
\frac{U_{mg \ell_1}}{\beta U_{mg \ell_2}} = \frac{W_1 (1 + r)}{W_2}
\end{align*}
$$

Despejando `$U_{mg \ell_1}$` al multiplicar por `$\beta U_{mg \ell_2}$`:

$$
\begin{align*}
U_{mg \ell_1} = \beta U_{mg \ell_2} \left[ \frac{W_1 (1 + r)}{W_2} \right]
\end{align*}
$$

### Paso 2: Derivada Parcial Respecto a la Tasa de Interés Real `$(r)$`

Derivamos `$U_{mg \ell_1}$` respecto a `$r$` manteniendo constantes `$W_1$`, `$W_2$` y `$U_{mg \ell_2}$`:

$$
\begin{align*}
\frac{\partial U_{mg \ell_1}}{\partial r} = \frac{\beta U_{mg \ell_2} W_1}{W_2} > 0
\end{align*}
$$

Como `$\beta > 0$`, `$U_{mg \ell_2} > 0$` y `$W_1, W_2 > 0$`, esta derivada es **estrictamente positiva**. De aquí seguimos la cadena lógica completa:

1. **Si aumenta la tasa de interés real `$( \Delta r > 0 )$`:** aumenta `$U_{mg \ell_1}$`, lo cual exige **reducir el ocio presente `$( \nabla \ell_1 )$`**, es decir, **aumentar la oferta de trabajo hoy `$( \Delta N_1 )$`** para un mismo salario `$W_1$`. Gráficamente, la curva `$N^s$` se desplaza hacia la **derecha** (pasando de `$N_1$` a `$N_2$` al nivel `$W_1$`).
2. **Si disminuye la tasa de interés real `$( \nabla r )$`:** cae `$U_{mg \ell_1}$`, lo cual induce a **aumentar el ocio presente `$( \Delta \ell_1 )$`**, es decir, **reducir la oferta de trabajo hoy `$( \nabla N_1 )$`** para un mismo salario `$W_1$`. Gráficamente, la curva `$N^s$` se desplaza hacia la **izquierda**.

$$
\begin{align*}
\frac{\partial U_{mg \ell_1}}{\partial r} = \frac{\beta U_{mg \ell_2} W_1}{W_2} > 0 \iff \nabla \ell_1 \iff \Delta N_1
\end{align*}
$$

> **Intuición económica (Sustitución intertemporal del ocio):** Cuando sube la tasa de interés real `$r$`, cada peso ganado trabajando hoy y ahorrado en el mercado financiero rinde más consumo futuro `$(1 + r)$`. Por tanto, el consumidor sustituye ocio presente por trabajo presente: trabaja más hoy `$(N_1 \to N_2)$` para ahorrar ese ingreso adicional y disfrutar de mayor consumo y ocio mañana.

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/oferta-trabajo-light.svg" alt="Curva de oferta de trabajo creciente hacia la asintota de tiempo total; al subir r se desplaza a la derecha y al bajar a la izquierda." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/oferta-trabajo-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: mayor r desplaza la oferta de trabajo a la derecha (sustitución intertemporal del ocio).</figcaption>
</figure>
