---
title: "Clase 10: Precio relativo y numerario"
course: "economia-clasica"
order: 10
classType: "clase"
description: "Precio relativo, numerario, precio absoluto y por qué la teoría empieza por el trueque generalizado."
math: true
---

## Puente: del excedente físico al intercambio

La unidad 2 detectó el excedente sin precios. Pero en una sociedad de mercado nadie recibe trigo "por reparto": todo pasa por el intercambio. Para que `$n$` bienes circulen hacen falta reglas de cambio. Esta clase las define y elige la vara de medir.

## Variables

* `$p_{ij} = p_i/p_j$`: precio relativo de `$i$` en términos de `$j$`.
* **Numerario**: bien (o conjunto) cuyo precio se fija como referencia.
* **Precio absoluto**: unidades de medio de pago por unidad del bien.

<Definicion>
**Precio relativo**: cuántas unidades de otro bien hay que entregar por una unidad del primero. **Numerario**: el bien-referencia; su precio es `$1$` por convención analítica.
</Definicion>

## Deducción paso a paso

### Paso 1: Contar relaciones

Con `$n$` bienes hay `$n(n-1)/2$` relaciones (la de `$i$` en sí misma es `$1$` y fijada una queda fijada la inversa). Ejemplo grano-hierro: si `$1$` arroba de grano = `$1/10$` de tonelada de hierro, entonces `$p_{gh} = 1/10$` y `$p_{hg} = 10$`.

<Ejemplo>

Con los 4 bienes de la clase 02 (trigo numerario), supón precios observados: hierro `$= 5$` (trigo), tela `$= 2$`, café `$= 4$`. Las 3 relaciones bastan; las otras 3 se deducen por arbitraje: `$p_{\text{hierro-tela}} = 5/2 = 2{,}5$`, `$p_{\text{hierro-café}} = 5/4 = 1{,}25$`, `$p_{\text{tela-café}} = 2/4 = 0{,}5$`. Si alguien ofreciera hierro por tela a `$3$`, comprarías hierro con trigo (`$5$`) y lo revenderías por tela hasta cerrar la brecha: el arbitraje impone la consistencia.

</Ejemplo>

### Paso 2: Elegir numerario

Bastan `$n-1$` relaciones en términos del bien elegido. Si el numerario es además el medio de pago, los relativos son a la vez absolutos y el precio del numerario es `$1$`.

### Paso 3: Separar relativo de absoluto

Con `$p_h/p_g = 10$` caben infinitos absolutos (`$p_g = 6 \Rightarrow p_h = 60$`; `$p_g = 12 \Rightarrow p_h = 120$`...). **Los absolutos pueden variar en la misma proporción con relativos constantes.** Por eso la teoría clásica investiga `$p_{ij}$`, no `$p_i$` aislados —como anuncia Ricardo: variaciones del valor **relativo**, no absoluto.

## Interpretación económica

1. **El numerario es convención, no mercancía especial**: cualquier bien sirve; lo que importa son las proporciones.
2. **Abstracción del dinero (análisis real)**: primero trueque generalizado; el dinero entra después como medio eficiente, no como condición de existencia de los precios.
3. **Puente a sistemas**: cada sistema de producción tendrá **un** sistema de precios (unicidad, clase 11).

<Ejercicio>
Dado `$p_h/p_g = 10$` y `$p_h = 120$`, halla `$p_g$`. Luego duplica ambos absolutos y verifica que el relativo no cambia. Un párrafo: ¿por qué esto justifica estudiar relativos primero?
</Ejercicio>
