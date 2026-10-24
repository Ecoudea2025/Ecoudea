---
title: "Clase 06: Métodos, sistema y excedente"
course: "economia-clasica"
order: 6
classType: "clase"
description: "Método de producción, sistema viable y excedente social con el ejemplo trigo-hierro de 2 sectores."
math: true
conceptos: ["Métodos de producción", "Subsistencias", "Excedente"]
---

## Puente: la producción como punto de partida

El enfoque clásico detecta los determinantes de los precios **en la esfera de la producción**, no en el cambio. Por eso el primer paso técnico es describir el substrato material: qué se produce, con qué y con cuánto trabajo. Todo lo demás (precios, distribución) se apoyará en esta base.

## Variables

* **Método de producción**: combinación específica (insumos + trabajo + producto) para un bien.
* **Sistema de producción**: conjunto de métodos vigentes, interdependientes (el producto de uno es insumo de otro).
* **Viabilidad**: el sistema repone lo gastado. **Excedente `$\mathbf{E}$`**: lo que sobra.

<Definicion>
**Método**: `$\text{medios} \oplus \text{trabajo} \to \text{producto}$`. **Sistema viable**: produce al menos lo que consume. **Excedente**: `$\text{PT} - \text{CPT} > 0$` (producto total menos consumo productivo total).
</Definicion>

## El ejemplo trigo-hierro (2 sectores)

### Paso 1: Los dos métodos

$$
\begin{align*}\text{3.587.500 trigo} \oplus \text{1.500.000 hierro} \oplus \text{100.000 trabajo} &\to \text{10.250.000 trigo} \\ \text{3.895.000 trigo} \oplus \text{0 hierro} \oplus \text{40.000 trabajo} &\to \text{3.000.000 hierro}\end{align*}
$$

### Paso 2: Agregar subsistencias

Con `$\mathbf{s} = [5{,}125\ \text{trigo},\ 0]$` por unidad de trabajo, las subsistencias (`$512{,}500$` y `$205{,}000$` de trigo) se suman a los insumos. El sistema queda en términos de `$\mathbf{B}$`.

### Paso 3: Calcular el excedente

$$
\begin{align*}\mathbf{E} = [\text{10.250.000} - \text{8.200.000},\ \text{3.000.000} - \text{1.500.000}] = [\text{2.050.000 trigo},\ \text{1.500.000 hierro}]\end{align*}
$$

Hay sobreproducto en ambos bienes: el sistema es viable **con** excedente, luego admite varias estructuras productivas (no una única, como en el caso estrictamente viable).

<figure class="eco-figure">
  <img src="/assets/figures/clasica/circuito-produccion-light.svg" alt="Circuito circular: insumos y trabajo entran a la producción, sale el producto total, se reponen insumos y subsistencias, y queda el excedente." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/clasica/circuito-produccion-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: la producción es circular — las mercancías son a la vez resultado y punto de partida; el excedente es lo que queda tras reponerlo todo.</figcaption>
</figure>

## Interpretación económica

1. **Producción circular**: no hay "factores originarios" que entren desde fuera; todo insumo fue producto antes.
2. **El excedente es físico antes que valor**: se detecta comparando cantidades, sin conocer precios.
3. **Viabilidad como precondición**: sin sistema viable no hay precios que estudiar; por eso las hipótesis 1–10 (clase 08) blindan este punto.

<IdeaClave>
Si dominas el ejemplo trigo-hierro (métodos → subsistencias → `$\mathbf{E}$`), dominas el 80% del aparato formal del curso: el resto es ponerle precios.
</IdeaClave>
