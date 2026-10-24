---
title: "Clase 11: Teoría de la Inversión, Capital Óptimo y Costos de Ajuste"
course: "macroeconomia-i"
order: 11
classType: "clase"
description: "Demanda de factores productivos, propiedades de la función de producción neoclásica, deducción paso a paso del stock de capital óptimo y modelo de inversión con costos cuadráticos de ajuste."
math: true
---


Demanda de Factores Productivos y el Problema de la Firma
---------------------------------------------------------

Pasamos ahora del estudio de las familias (el consumo) al estudio de las **firmas** (la inversión y la producción), siguiendo el Capítulo 4 de De Gregorio (*Macroeconomía: teoría y políticas*).

Las firmas son unidades económicas que **demandan trabajo (`$N_t$`) y capital físico (`$K_t$`)** para transformarlos en bienes finales mediante una **función de producción**:

$$
\begin{align*}Y_t = A F(K_t, N_t)\end{align*}
$$

donde:
* `$Y_t$`: Nivel de producto o producción física en el período `$t$`.
* `$A$`: Coeficiente tecnológico o Productividad Total de los Factores (PTF).
* `$K_t$`: Stock de capital físico (maquinaria, plantas, equipos, edificios).
* `$N_t$`: Cantidad de trabajo contratado.

### El Objetivo de la Firma Competitiva

El objetivo de la firma es **maximizar sus beneficios económicos nominales (`$\Pi_t$`)**, definidos como los ingresos por ventas menos el costo de contratar trabajo y arrendar capital:

$$
\begin{align*}\max_{\{N_t, K_t\}} \quad \Pi_t = P_t Y_t - W_t N_t - R_t K_t\end{align*}
$$

donde:
* `$P_t$`: Precio unitario del bien producido `$Y_t$`.
* `$W_t$`: Salario nominal pagado por cada unidad de trabajo.
* `$R_t$`: Renta nominal del capital (precio de arriendo o tasa de rendimiento exigida al capital físico).

Asumimos que **la firma es perfectamente competitiva**: no tiene poder de mercado para determinar los precios (`$P_t, W_t, R_t$` vienen dados exógenamente por el mercado) y, por lo tanto, **remunera a cada factor productivo según su productividad marginal**.


Propiedades de la Función de Producción Neoclásica
--------------------------------------------------

Para que el problema de maximización de beneficios esté bien comportado, la función de producción neoclásica `$Y_t = A F(K_t, N_t)$` satisface cuatro propiedades fundamentales:

### 1. Rendimientos Constantes a Escala (Homogeneidad de Grado 1)

Si multiplicamos todos los factores productivos por un escalar positivo `$\lambda > 0$`, la producción aumenta exactamente en la misma proporción `$\lambda$`:

$$
\begin{align*}A F(\lambda K_t, \lambda N_t) = \lambda A F(K_t, N_t) = \lambda Y_t\end{align*}
$$

### 2. Productividades Marginales Positivas y Decrecientes

Agregar más trabajo o más capital siempre incrementa la producción (primera derivada positiva), pero cada unidad adicional aporta menos que la anterior (segunda derivada negativa):

$$
\begin{align*}\frac{\partial Y}{\partial N} > 0, \quad \frac{\partial^2 Y}{\partial N^2} < 0, \qquad \qquad \frac{\partial Y}{\partial K} > 0, \quad \frac{\partial^2 Y}{\partial K^2} < 0\end{align*}
$$

### 3. Condiciones de Inada (Comportamiento en los Extremos)

Cuando un factor es extremadamente escaso (`$\to 0$`), su productividad marginal tiende a infinito; cuando se acumula en exceso (`$\to \infty$`), su productividad marginal tiende a cero:

$$
\begin{align*}\lim_{N \to 0} \frac{\partial Y}{\partial N} = \infty, \quad \lim_{N \to \infty} \frac{\partial Y}{\partial N} = 0, \qquad \qquad \lim_{K \to 0} \frac{\partial Y}{\partial K} = \infty, \quad \lim_{K \to \infty} \frac{\partial Y}{\partial K} = 0\end{align*}
$$

### 4. Condición de "No Free Lunch" (Esencialidad de los Factores)

No es posible producir nada sin insumos. Si cualquiera de los dos factores es cero, la producción total es cero:

$$
\begin{align*}F(0, N) = F(K, 0) = F(0, 0) = 0\end{align*}
$$


Deducción Paso a Paso del Capital Óptimo ($K_t^*$)
--------------------------------------------------

Adoptemos la especificación **Cobb-Douglas** para la función de producción:

$$
\begin{align*}Y_t = A_t K_t^\alpha N_t^{1 - \alpha}, \quad \text{con } 0 < \alpha < 1\end{align*}
$$

Sustituyendo en la función de beneficios de la firma:

$$
\begin{align*}\max_{\{N_t, K_t\}} \quad \Pi_t = P_t A_t K_t^\alpha N_t^{1 - \alpha} - W_t N_t - R_t K_t\end{align*}
$$

### Paso 1: Condiciones de Primer Orden (C.P.O.)

Derivamos respecto a `$N_t$` y respecto a `$K_t$` e igualamos a cero:

$$
\begin{align*}\frac{\partial \Pi_t}{\partial N_t} &= P_t PMgN_t - W_t = 0 \implies \frac{W_t}{P_t} = PMgN_t \tag{11.1} \\ \frac{\partial \Pi_t}{\partial K_t} &= P_t PMgK_t - R_t = 0 \implies \frac{R_t}{P_t} = PMgK_t \tag{11.2}\end{align*}
$$

La firma contrata trabajo hasta que el salario real (`$\frac{W_t}{P_t}$`) iguala la productividad marginal del trabajo, y arrienda capital hasta que el costo real de arriendo (`$\frac{R_t}{P_t}$`) iguala la productividad marginal del capital.

### Paso 2: Despeje Algebraico de $K_t^*$

¿Cuál es el stock de capital óptimo deseado por la firma? Tomamos la ecuación `(2)` y sustituimos `$PMgK_t = \alpha A_t K_t^{\alpha - 1} N_t^{1 - \alpha}$`:

$$
\begin{align*}\frac{R_t}{P_t} = \alpha A_t K_t^{\alpha - 1} N_t^{1 - \alpha}\end{align*}
$$

Aislamos el término que contiene a `$K_t$`:

$$
\begin{align*}K_t^{\alpha - 1} = \left( \frac{R_t}{P_t \cdot \alpha A_t} \right) \frac{1}{N_t^{1 - \alpha}}\end{align*}
$$

Elevamos ambos lados de la igualdad a la potencia `$\frac{1}{\alpha - 1}$`:

$$
\begin{align*}\left( K_t^{\alpha - 1} \right)^{\frac{1}{\alpha - 1}} = \left[ \left( \frac{R_t}{P_t \alpha A_t} \right) \frac{1}{N_t^{1 - \alpha}} \right]^{\frac{1}{\alpha - 1}}\end{align*}
$$

Como `$\frac{1}{\alpha - 1} = -\frac{1}{1 - \alpha}$`, invertimos la fracción interna para cambiar el signo del exponente y simplificamos el exponente de `$N_t$` (`$(1 - \alpha) \cdot \frac{1}{1 - \alpha} = 1$`):

$$
\begin{align*}K_t &= \left( \frac{R_t}{P_t \alpha A_t} \right)^{-\frac{1}{1 - \alpha}} \left( \frac{1}{N_t^{1 - \alpha}} \right)^{-\frac{1}{1 - \alpha}} \\ K_t^* &= \left( \frac{P_t \alpha A_t}{R_t} \right)^{\frac{1}{1 - \alpha}} N_t\end{align*}
$$

Esta ecuación nos entrega los **determinantes del capital óptimo (`$K_t^*$`)**:
* Aumenta con el precio del producto (`$P_t$`), con el avance tecnológico (`$A_t$`) y con el empleo (`$N_t$`, por complementariedad entre factores).
* Disminuye cuando sube el costo de arriendo del capital (`$R_t$`).

### Análisis Gráfico de Desequilibrios respecto a $K^*$

Si comparamos el ingreso marginal del capital (`$P_t PMgK_t$`, curva decreciente) con su costo marginal (`$R_t$`, recta horizontal):
* **Si `$K_t < K^*$`:** Se cumple que `$P_t PMgK_t > R_t$`. Existen **ganancias potenciales** desaprovechadas, lo que genera la necesidad de **aumentar el capital (`$\Delta K_t > 0$`)**.
* **Si `$K_t > K^*$`:** Se cumple que `$P_t PMgK_t < R_t$`. La firma incurre en **pérdidas efectivas** sobre las últimas unidades, lo que genera la necesidad de **reducir el capital (`$\nabla K_t < 0$`)**.

<figure class="eco-figure">
  <img src="/assets/figures/macroeconomia/capital-optimo-light.svg" alt="Producto marginal decreciente cruzando el costo horizontal con zonas de ganancia y pérdida." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/macroeconomia/capital-optimo-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: a la izquierda del óptimo cada máquina extra rinde más de lo que cuesta; a la derecha, al revés.</figcaption>
</figure>


Costos de Ajustar el Capital y la Función de Inversión
------------------------------------------------------

En la realidad, una empresa que tiene un capital `$K_t \neq K^*$` no salta instantáneamente a `$K^*$`, porque instalar nuevas plantas, importar maquinaria y entrenar personal es costoso.

Modelamos los **costos totales de ajuste del capital** mediante una función de pérdida cuadrática que pondera dos costos contrapuestos con el parámetro `$\epsilon \in (0, 1)$`:

$$
\begin{align*}C(I_t) = \underbrace{\epsilon (K_{t+1} - K^*)^2}_{\text{Costo de estar fuera del óptimo}} + \underbrace{(1 - \epsilon)(K_{t+1} - K_t)^2}_{\text{Costo de cambiar el capital}}\end{align*}
$$

### Minimización Paso a Paso respecto a $K_{t+1}$

La firma elige el capital del próximo período `$K_{t+1}$` para minimizar el costo total de ajuste:

$$
\begin{align*}\min_{\{K_{t+1}\}} \quad C(K_{t+1} - K_t) = \epsilon (K_{t+1} - K^*)^2 + (1 - \epsilon)(K_{t+1} - K_t)^2\end{align*}
$$

1. **Derivamos respecto a `$K_{t+1}$` e igualamos a cero:**

$$
\begin{align*}\frac{\partial C(\cdot)}{\partial K_{t+1}} = 2\epsilon (K_{t+1} - K^*) + 2(1 - \epsilon)(K_{t+1} - K_t) = 0\end{align*}
$$

2. **Dividimos toda la ecuación por `$2$` y expandimos los productos:**

$$
\begin{align*}\epsilon (K_{t+1} - K^*) + (1 - \epsilon)(K_{t+1} - K_t) &= 0 \\ \epsilon K_{t+1} - \epsilon K^* + (1 - \epsilon)K_{t+1} - (1 - \epsilon)K_t &= 0\end{align*}
$$

3. **Artificio algebraico para formar la inversión neta `$I_t = K_{t+1} - K_t$`:**

Sumamos y restamos el término `$\epsilon K_t$` en el lado izquierdo:

$$
\begin{align*}\epsilon K_{t+1} \underbrace{- \epsilon K^* + \epsilon K_t}_{-\epsilon(K^* - K_t)} - \epsilon K_t + (1 - \epsilon)K_{t+1} - (1 - \epsilon)K_t = 0\end{align*}
$$

Pasamos `$\epsilon(K^* - K_t)$` al lado derecho de la igualdad:

$$
\begin{align*}\epsilon K_{t+1} - \epsilon K_t + (1 - \epsilon)K_{t+1} - (1 - \epsilon)K_t = \epsilon (K^* - K_t)\end{align*}
$$

4. **Expandimos y cancelamos los términos con `$\epsilon$` en el lado izquierdo:**

$$
\begin{align*}\cancel{\epsilon K_{t+1}} + K_{t+1} - \cancel{\epsilon K_{t+1}} - \cancel{\epsilon K_t} - K_t + \cancel{\epsilon K_t} = \epsilon (K^* - K_t)\end{align*}
$$

Lo que se reduce limpiamente a la **ecuación de ajuste parcial de la inversión**:

$$
\begin{align*}I_t = K_{t+1} - K_t = \epsilon (K^* - K_t), \quad \text{con } 0 < \epsilon < 1\end{align*}
$$

### La Ecuación Estructural de Inversión

Finalmente, reemplazando la expresión del capital óptimo `$K^*$` dentro de la regla de inversión óptima, obtenemos:

$$
\begin{align*}I_t = \epsilon \left( \left( \frac{P_t \alpha A_t}{R_t} \right)^{\frac{1}{1 - \alpha}} N_t - K_t \right)\end{align*}
$$

### ¿Qué implica el tamaño del parámetro $\epsilon$?

La inversión óptima en cada período es una fracción `$\epsilon$` de la brecha existente entre el capital deseado y el capital actual (`$K^* - K_t$`):
* **Si `$\epsilon \to 1$` (muy grande):** El costo de estar fuera del óptimo domina sobre el costo de ajuste. La empresa cierra casi toda la brecha de inmediato (ajuste muy rápido).
* **Si `$\epsilon \to 0$` (muy pequeño):** El costo de instalar nuevo capital es muy alto. La empresa ajusta su stock de capital de forma muy lenta y gradual a lo largo de muchos períodos.
