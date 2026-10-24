---
title: "Clase 13: Estática Comparativa de la Inversión: Derivadas, Signos e Interpretación"
course: "macroeconomia-i"
order: 13
classType: "clase"
description: "Cálculo paso a paso, verificación de signos, análisis de concavidad e interpretación económica de todas las derivadas parciales de la función de inversión neoclásica."
math: true
---

---
---

La Ecuación Estructural de la Inversión
---------------------------------------

Partimos de la función de inversión óptima con costos de ajuste deducida en la clase anterior:

$$
\begin{align*}I_t = \epsilon \left[ \left( \frac{P_t \alpha A}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} N - K_t \right], \quad \text{con } 0 < \epsilon < 1, \; 0 < \alpha < 1\end{align*}
$$

Para simplificar la escritura durante las derivaciones, llamemos `$K^*$` al stock de capital deseado:

$$
\begin{align*}K^* \equiv \left( \frac{P_t \alpha A}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} N > 0\end{align*}
$$

Como todos los parámetros e insumos (`$P_t, P_K, \alpha, A, r, \delta, N$`) son estrictamente positivos y `$0 < \alpha < 1$`, el exponente cumple que:

$$
\begin{align*}\frac{1}{1 - \alpha} > 1 > 0\end{align*}
$$

A continuación, calculamos paso a paso las **siete derivadas parciales** de la función de inversión, verificamos analíticamente su signo y explicamos su intuición económica.


1. Derivada respecto a la Tasa de Interés Real ($r$)
----------------------------------------------------

Reescribimos el término dependiente de `$r$` con exponente negativo: `$(r + \delta)^{-\frac{1}{1 - \alpha}}$`. Aplicando la regla de la cadena:

$$
\begin{align*}\frac{\partial I_t}{\partial r} &= \epsilon N \left( \frac{P_t \alpha A}{P_K} \right)^{\frac{1}{1 - \alpha}} \left( -\frac{1}{1 - \alpha} \right) (r + \delta)^{-\frac{1}{1 - \alpha} - 1} \\ &= -\frac{\epsilon}{1 - \alpha} \frac{K^*}{r + \delta} < 0\end{align*}
$$

* **Verificación del signo:** Como `$\epsilon > 0$`, `$1 - \alpha > 0$`, `$K^* > 0$` y `$r + \delta > 0$`, el signo menos inicial garantiza que **`$\frac{\partial I_t}{\partial r} < 0$`**.
* **Interpretación económica:** Un aumento en la tasa de interés real encarece el costo financiero de endeudarse para comprar maquinaria (y eleva el costo de oportunidad de los fondos propios). Esto reduce el stock de capital deseado `$K^*$`, achica la brecha `$K^* - K_t$` y contrae la inversión agregada.


2. Derivada respecto a la Tasa de Depreciación ($\delta$)
---------------------------------------------------------

Dado que `$\delta$` entra de forma aditiva y simétrica con `$r$` en el denominador `$(r + \delta)$`, su derivada es idéntica:

$$
\begin{align*}\frac{\partial I_t}{\partial \delta} &= -\frac{\epsilon}{1 - \alpha} N \left( \frac{P_t \alpha A}{P_K} \right)^{\frac{1}{1 - \alpha}} (r + \delta)^{-\frac{1}{1 - \alpha} - 1} \\ &= -\frac{\epsilon}{1 - \alpha} \frac{K^*}{r + \delta} < 0\end{align*}
$$

* **Verificación del signo:** Estrictamente negativo (**`$\frac{\partial I_t}{\partial \delta} < 0$`**).
* **Interpretación económica:** Una mayor tasa de desgaste físico u obsolescencia tecnológica reduce la rentabilidad neta de cada máquina instalada, elevando el costo de uso del capital y desincentivando la inversión.


3. Derivada respecto al Coeficiente Tecnológico ($A$)
-----------------------------------------------------

Derivamos respecto a la productividad total de los factores `$A$`:

$$
\begin{align*}\frac{\partial I_t}{\partial A} &= \epsilon N \left( \frac{P_t \alpha}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} \left( \frac{1}{1 - \alpha} \right) A^{\frac{1}{1 - \alpha} - 1} \\ &= \frac{\epsilon}{1 - \alpha} \frac{K^*}{A} > 0\end{align*}
$$

* **Verificación del signo:** Todos los factores son positivos, por lo que **`$\frac{\partial I_t}{\partial A} > 0$`**.
* **Interpretación económica:** Un choque tecnológico positivo (innovación, digitalización, mejoras de procesos) eleva la productividad marginal del capital para cualquier nivel de insumos, disparando el capital deseado `$K^*$` y acelerando la inversión.
* **Nota sobre la curvatura:** Como el exponente es `$\frac{1}{1 - \alpha} > 1$`, la segunda derivada respecto a `$A$` es positiva (`$\frac{\partial^2 I_t}{\partial A^2} = \frac{\epsilon \alpha}{(1 - \alpha)^2} \frac{K^*}{A^2} > 0$`), mientras que si definimos la variable compuesta `$x \equiv \left(\frac{\alpha A}{r+\delta}\right)^{\frac{1}{1-\alpha}}$`, la respuesta ante el costo de uso es convexa.


4. Derivada respecto al Nivel de Empleo ($N$)
---------------------------------------------

Como `$N$` entra linealmente multiplicando al paréntesis:

$$
\begin{align*}\frac{\partial I_t}{\partial N} = \epsilon \left( \frac{P_t \alpha A}{P_K (r + \delta)} \right)^{\frac{1}{1 - \alpha}} = \epsilon \frac{K^*}{N} > 0\end{align*}
$$

* **Verificación del signo:** Estrictamente positivo (**`$\frac{\partial I_t}{\partial N} > 0$`**).
* **Interpretación económica:** Refleja la **complementariedad estratégica entre trabajo y capital** en una tecnología Cobb-Douglas. Más trabajadores contratados hacen que cada máquina existente sea más productiva (`$\frac{\partial PMgK}{\partial N} > 0$`), induciendo a la firma a expandir su planta física.


5. Derivada respecto al Precio Relativo ($P_t / P_K$)
-----------------------------------------------------

Sea `$p_r \equiv \frac{P_t}{P_K}$` la razón entre el precio de venta del producto final y el precio de compra del bien de capital. Derivando respecto a `$p_r$`:

$$
\begin{align*}\frac{\partial I_t}{\partial (P_t / P_K)} &= \epsilon N \left( \frac{\alpha A}{r + \delta} \right)^{\frac{1}{1 - \alpha}} \left( \frac{1}{1 - \alpha} \right) \left( \frac{P_t}{P_K} \right)^{\frac{1}{1 - \alpha} - 1} \\ &= \frac{\epsilon}{1 - \alpha} \frac{K^*}{(P_t / P_K)} > 0\end{align*}
$$

* **Verificación del signo:** Estrictamente positivo (**`$\frac{\partial I_t}{\partial (P_t / P_K)} > 0$`**).
* **Interpretación económica:** Si sube el precio al que la firma vende su producto (`$P_t$`) o si se abarata el costo de adquirir maquinaria importada/nacional (`$P_K$`, por ejemplo mediante rebajas arancelarias o subsidios a los bienes de capital), la rentabilidad de invertir aumenta y la inversión crece.


6. Derivada respecto al Stock de Capital Inicial ($K_t$)
--------------------------------------------------------

Derivando linealmente respecto a `$K_t$`:

$$
\begin{align*}\frac{\partial I_t}{\partial K_t} = -\epsilon < 0\end{align*}
$$

* **Verificación del signo:** Estrictamente negativo (**`$\frac{\partial I_t}{\partial K_t} < 0$`**).
* **Interpretación económica:** Si la empresa ya cuenta con un stock de capital inicial elevado (o cercano a `$K^*$`), la brecha por cubrir es pequeña y requiere menos inversión nueva. Por el contrario, si el capital inicial es muy bajo (por ejemplo, tras un desastre natural o en un país en vías de desarrollo), la brecha `$K^* - K_t$` es enorme y la tasa de inversión es muy alta.


7. Derivada respecto a la Elasticidad del Capital ($\alpha$)
------------------------------------------------------------

Dado que `$\alpha$` aparece tanto en la base como en el exponente `$\frac{1}{1 - \alpha}$`, aplicamos **derivación logarítmica** sobre `$K^*(\alpha) = N \left[ \frac{P_t \alpha A}{P_K (r + \delta)} \right]^{\frac{1}{1 - \alpha}}$`.

Definamos `$Z \equiv \frac{P_t A}{P_K (r + \delta)}$`, de modo que `$K^*(\alpha) = N (Z \alpha)^{\frac{1}{1 - \alpha}}$`. Tomando logaritmo natural:

$$
\begin{align*}\ln K^*(\alpha) = \ln N + \frac{1}{1 - \alpha} \ln(Z \alpha) = \ln N + \frac{\ln Z + \ln \alpha}{1 - \alpha}\end{align*}
$$

Derivando respecto a `$\alpha$` mediante la regla del cociente:

$$
\begin{align*}\frac{\text{d} \ln K^*}{\text{d} \alpha} = \frac{1}{K^*} \frac{\partial K^*}{\partial \alpha} = \frac{\frac{1}{\alpha}(1 - \alpha) - (\ln Z + \ln \alpha)(-1)}{(1 - \alpha)^2} = \frac{\frac{1 - \alpha}{\alpha} + \ln(Z \alpha)}{(1 - \alpha)^2}\end{align*}
$$

Por lo tanto, la derivada de la inversión respecto a `$\alpha$` es:

$$
\begin{align*}\frac{\partial I_t}{\partial \alpha} = \epsilon \frac{\partial K^*}{\partial \alpha} = \frac{\epsilon K^*}{(1 - \alpha)^2} \left[ \frac{1 - \alpha}{\alpha} + \ln\left( \frac{P_t \alpha A}{P_K (r + \delta)} \right) \right]\end{align*}
$$

* **Signo e interpretación:** Siempre que el producto marginal supere la unidad de costo de uso (`$P_t \alpha A > P_K(r+\delta)$`, que es el caso económicamente relevante donde `$K^* > N$`), ambos sumandos son positivos y **`$\frac{\partial I_t}{\partial \alpha} > 0$`**: una tecnología más intensiva en capital demanda un mayor stock óptimo de maquinaria.


Resumen de Estática Comparativa de la Inversión
-----------------------------------------------

| Determinante | Derivada Parcial | Signo | Efecto sobre la Curva de Inversión $I(r)$ |
| :--- | :--- | :---: | :--- |
| **Tasa de interés real (`$r$`)** | `$\frac{\partial I_t}{\partial r}$` | **`$< 0$`** | Movimiento a lo largo de la curva `$I(r)$` |
| **Depreciación (`$\delta$`)** | `$\frac{\partial I_t}{\partial \delta}$` | **`$< 0$`** | Desplazamiento hacia la izquierda |
| **Tecnología (`$A$`)** | `$\frac{\partial I_t}{\partial A}$` | **`$> 0$`** | Desplazamiento hacia la derecha |
| **Empleo (`$N$`)** | `$\frac{\partial I_t}{\partial N}$` | **`$> 0$`** | Desplazamiento hacia la derecha |
| **Precio relativo (`$P_t / P_K$`)** | `$\frac{\partial I_t}{\partial (P_t / P_K)}$` | **`$> 0$`** | Desplazamiento hacia la derecha |
| **Capital inicial (`$K_t$`)** | `$\frac{\partial I_t}{\partial K_t}$` | **`$< 0$`** | Desplazamiento hacia la izquierda |

> **Espacio para gráfica 1:** *Curva de demanda de inversión `$I(r)$` y sus desplazamientos.*
> En el plano `$(I, r)$`, se traza la curva de inversión con pendiente negativa respecto a la tasa de interés real `$r$`, mostrando cómo aumentos en `$A$`, `$N$` o `$\frac{P_t}{P_K}$` desplazan la curva hacia la derecha, mientras que aumentos en `$\delta$` o `$K_t$` la desplazan hacia la izquierda.
