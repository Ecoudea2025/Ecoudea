---
title: "Clase 16: Externalidades de red, economía digital y mercados bilaterales"
course: "microeconomia-ii"
order: 16
classType: "clase"
description: "Economía de la información y bienes digitales, externalidades de red directas e indirectas, equilibrios múltiples y masa crítica, mercados bilaterales (two-sided markets), poder de mercado en plataformas y modelos de negocio digitales."
math: true
---

## Motivación: bits, átomos y la economía del mundo digital

La gestión de la información ha impulsado una nueva revolución industrial que transforma de manera radical cómo se producen, distribuyen y consumen tanto los contenidos digitales como los bienes tradicionales. Sin embargo, como destacan Susan Athey y Hal Varian, **no se requiere una teoría económica nueva** para analizar el mundo digital: la economía no se ocupa de los objetos físicos en sí, sino de las personas y de cómo interactúan y toman decisiones. Las preferencias, creencias, dotaciones y restricciones tecnológicas siguen gobernando los mercados de información.

Lo que sí cambia drásticamente es la **estructura de costos y la tecnología** de los bienes basados en información:

| Dimensión | Bienes físicos —átomos— | Bienes de información —bits (*binary digit*)— |
| :--- | :--- | :--- |
| **Costo marginal** | Positivo y frecuentemente creciente a partir de cierta escala. | Prácticamente **cero** para reproducir copias adicionales, tras incurrir en altos costos fijos iniciales. |
| **Distribución** | Sujeta a costos logísticos, inventarios y tiempos físicos de transporte. | Instantánea, **a la velocidad de la luz**, con alcance global simultáneo. |
| **Depreciación física** | Se desgastan, consumen o deterioran con el uso y el tiempo. | **Nunca se deterioran** físicamente por el uso repetido. |

---

## 1. Externalidades de red: concepto y dinámica de demanda

Una **externalidad de red** ocurre cuando la utilidad que reporta un bien o servicio a una persona depende directamente del **número de personas `$n$` que también lo consumen**.

* **Externalidades de red directas:** el valor para cada usuario crece al aumentar el tamaño de la red de usuarios idénticos o compatibles. Ejemplos cotidianos son los *smartphones*, las redes sociales, las aplicaciones de mensajería y los programas informáticos. Incluso fenómenos culturales o de moda exhiben este efecto: el deseo de llevar un *piercing* en la nariz depende, en buena medida, de cuántas personas lo hayan adoptado.
* **Externalidades de red indirectas —bienes complementarios—:** la demanda de un bien depende del tamaño de la base instalada de su complemento. Por ejemplo, la demanda de videojuegos de PlayStation depende del número de consolas PlayStation vendidas, y a su vez la demanda de consolas depende de la variedad y cantidad de juegos disponibles.

> **¿Por qué la curva de demanda tiene forma de U invertida?** A medida que la red crece desde cero, el efecto red domina y la disposición a pagar de los consumidores aumenta. Sin embargo, a partir de cierto tamaño crítico, aparecen efectos negativos como la **congestión** o la **pérdida de exclusividad**, haciendo que la disposición marginal a pagar decrezca hasta anularse.

---

## 2. Modelo formal de externalidades de red y equilibrios múltiples

Formalicemos el modelo clásico de Varian para entender cómo surgen múltiples equilibrios y qué determina que una red despegue o fracase.

### 2.1 Derivación de la curva inversa de demanda

Suponga una población de `$1000$` consumidores potenciales indexados por `$V = 1, 2, \dots, 1000$`, ordenados según su valoración intrínseca por el bien.

* **Referencia sin efecto red:** si el precio es `$p$` y no hubiera externalidad de red, el número `$n$` de personas que piensan que el bien vale al menos `$p$` sería simplemente `$n = 1000 - p$`.
* **Con externalidad de red:** la disposición a pagar de cada consumidor `$V$` es proporcional al tamaño esperado de la red `$n$`, es decir, `$\text{DAP}(V, n) = V \cdot n$`. Si denotamos por `$\hat{V}$` al **consumidor marginal** —aquel que es exactamente indiferente entre comprar y no comprar el bien al precio vigente `$p$`—, entonces comprarán todas las personas cuya valoración supere a `$\hat{V}$`:

$$
\begin{align*}
n = 1000 - \hat{V} \implies \hat{V} = 1000 - n
\end{align*}
$$

Como el consumidor marginal `$\hat{V}$` está indiferente al precio de mercado `$p$`, su disposición a pagar iguala al precio:

$$
\begin{align*}
p = \hat{V} \cdot n
\end{align*}
$$

Sustituyendo `$(1)$` en `$(2)$`, obtenemos la **curva inversa de demanda** con forma de parábola cóncava —U invertida—:

$$
\begin{align*}
p(n) = n(1000 - n) = 1000n - n^2
\end{align*}
$$

Observe que `$p(0) = 0$`, `$p(1000) = 0$`, y el máximo de disposición a pagar se alcanza en `$n = 500$` con `$p_{\max} = 250.000$`.

### 2.2 Equilibrios y estabilidad con oferta a costo constante

Suponga que la tecnología de provisión tiene un costo marginal constante `$c > 0$` —curva de oferta horizontal `$p = c$`—, con `$c < 250.000$`. Los puntos donde se cumplen las expectativas de los consumidores `$(p(n) = c)$` resuelven:

$$
\begin{align*}
1000n - n^2 = c \implies n^2 - 1000n + c = 0
\end{align*}
$$

Además del equilibrio de mercado nulo `$n_0 = 0$` —si nadie espera que otros compren, nadie está dispuesto a pagar `$c$`—, la ecuación cuadrática arroja dos soluciones positivas:

$$
\begin{align*}
n_1 &= \frac{1000 - \sqrt{1000^2 - 4c}}{2} \quad \text{(equilibrio inestable: masa crítica)} \\
n_2 &= \frac{1000 + \sqrt{1000^2 - 4c}}{2} \quad \text{(equilibrio estable de alto nivel)}
\end{align*}
$$

Analicemos la **estabilidad** de estos tres puntos observando las flechas de ajuste:
1. **Si `$0 < n < n_1$`:** la disposición a pagar `$p(n)$` está por debajo del costo `$c$`. Los consumidores se retiran y la red colapsa hacia **`$n_0 = 0$`**, que es un **equilibrio estable**.
2. **Si `$n = n_1$`:** es un **equilibrio inestable**. Cualquier perturbación hacia la izquierda hunde el mercado en `$0$`, mientras que cualquier impulso hacia la derecha hace que `$p(n) > c$`. Por eso `$n_1$` representa la **masa crítica** de la red.
3. **Si `$n_1 < n < n_2$`:** la disposición a pagar excede al costo `$(p(n) > c)$`, atrayendo nuevos usuarios hasta converger en **`$n_2$`**. Si `$n > n_2$` ocurre lo inverso `$(p(n) < c)$` y el tamaño retrocede hacia `$n_2$`. Así, `$n_2$` es el **equilibrio estable de alto nivel** deseado.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/red-equilibrios-light.svg" alt="Demanda con efecto red y tres equilibrios." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/red-equilibrios-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: n1 es la masa critica entre el colapso y la adopcion masiva.</figcaption>
</figure>

### 2.3 Ajuste de costos, masa crítica y estrategias de despegue

Si el costo inicial de provisión es demasiado alto `$(c > 250.000)$`, la recta de oferta queda por encima de toda la parábola y el único equilibrio posible es un mercado nulo `$(n = 0)$`. A medida que el progreso tecnológico reduce el costo hacia un nivel bajo, emergen los equilibrios positivos.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/red-ajuste-light.svg" alt="Ajuste de costes y despegue temporal de la red." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/red-ajuste-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: con coste alto solo hay equilibrio nulo; con coste bajo la red despega.</figcaption>
</figure>

Para "introducir ruido positivo sobre `$n$`" y superar la masa crítica `$n_1$` hasta alcanzar el equilibrio alto `$n_2$`, las empresas y reguladores emplean cinco palancas:
1. Factores aleatorios o efectos de contagio inicial.
2. Disminución progresiva de costos de hardware o conectividad.
3. **Estrategias de venta:** descuentos agresivos y versiones *beta* gratuitas, entrega de bienes complementarios a bajo precio —hasta precio cero— o alquiler de la red.
4. Publicidad masiva para coordinar expectativas optimistas de los usuarios.
5. Financiación pública inicial.

> **El caso histórico de los anuncios radiofónicos (David Sarnoff):** En los inicios de la radio (*Wireless World*), surgía la pregunta clave de bienes públicos y redes: *"¿Quién va a pagar por un mensaje que no se envía a alguien en particular?"* La historia económica muestra cinco modelos de financiación alternativos: donaciones del público —como **NPR**—, subvenciones a los contenidos por parte de los fabricantes de radios, publicidad comercial, impuestos específicos sobre las lámparas de radio —modelo clásico de la **BBC**— e impuestos generales —como **RTVC** en Colombia—.

---

## 3. Mercados bilaterales o de dos lados (*Two-Sided Markets*)

Muchos mercados digitales modernos conectan dos poblaciones distintas que interactúan a través de una plataforma intermediaria.

### 3.1 Definición y estructura de externalidades cruzadas

Un **mercado bilateral** es un mercado en el que un grupo de usuarios de tamaño `$n_1$` genera una **externalidad indirecta** sobre otro grupo distinto de tamaño `$n_2$`, y viceversa: la externalidad es **mutua** y existe una plataforma que los pone en contacto.

* **Efectos de red indirectos:** cuantos más usuarios hay de un lado, más atractivo se vuelve el otro lado.
  * *Tarjetas de crédito:* cuantos más comercios acepten una tarjeta, más atractiva es para los consumidores; y cuantos más consumidores la usen, más comercios la aceptarán.
  * *Transporte y delivery:* más pasajeros en Uber atraen más conductores, y más conductores reducen el tiempo de espera para los pasajeros.
  * *Ecosistemas digitales:* Acrobat y Distiller; iPod y música en formato AAC; consolas de videojuegos y estudios de desarrollo; redes sociales conectando usuarios y anunciantes.

### 3.2 Equilibrio en un mercado bilateral

En un mercado de dos lados, la participación óptima del grupo `$1$` es una función creciente del tamaño del grupo `$2$`, `$n_1 = f_1(n_2)$`, y la participación del grupo `$2$` depende crecientemente de `$n_1$`, `$n_2 = f_2(n_1)$`. En general, la intersección de ambas curvas de respuesta genera **tres equilibrios** en el plano `$(n_1, n_2)$`: el origen nulo `$(0, 0)$` (estable), un equilibrio interior intermedio de masa crítica (inestable) y un equilibrio estable de alta adopción conjunta.

<figure class="eco-figure">
  <img src="/assets/figures/micro2/bilateral-light.svg" alt="Mercado bilateral y dinamica de adopcion." class="fig-light w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <img src="/assets/figures/micro2/bilateral-dark.svg" alt="" aria-hidden="true" class="fig-dark w-full h-auto rounded-xl border border-border-subtle" loading="lazy" decoding="async" />
  <figcaption>Figura: por debajo del umbral hay colapso; por encima, adopcion conjunta.</figcaption>
</figure>

### 3.3 Fijación de precios asimétrica, concentración y poder de mercado

Una lección fundamental de los mercados bilaterales es que **no se puede analizar cada lado del mercado de forma aislada**: una decisión de precio en un lado altera la participación y el valor del otro lado.

1. **Subsidios cruzados estratégicos:** tiene pleno sentido económico estandarizar, subvencionar o incluso **regalar `$(P = 0)$`** el acceso al bien o grupo de menor valor agregado o mayor elasticidad-precio para impulsar la demanda del lado de mayor valor monetizable.
2. **Trampa de la gratuidad en análisis de competencia:** una plataforma puede cobrar `$0\text{ COP}$` a los consumidores y financiarse cobrando a los anunciantes o a los comercios. Por ejemplo, suponga una plataforma de pagos que cobra `$0\text{ COP}$` al consumidor y una comisión del `$3\%$` al comercio. Si un regulador observa únicamente el lado del consumidor, concluiría erróneamente que el mercado es hipercompetitivo porque el servicio es gratuito; sin embargo, si la plataforma reúne millones de consumidores, los comercios prácticamente no pueden permitirse rechazarla, otorgando a la plataforma un **poder de mercado considerable** sobre el lado comercial.
3. **Concentración y barreras de entrada:** los efectos de red indirectos tienden a concentrar el mercado en una o pocas plataformas dominantes. Aunque esa concentración puede generar ganancias de eficiencia por escala y liquidez, también levanta barreras de entrada muy altas para nuevos competidores.

---

## 4. Plataformas digitales y modelos de negocio

No toda empresa digital es una plataforma: lo verdaderamente distintivo de una **plataforma digital** es la **intermediación multilateral** mediante una infraestructura e interfaz digital que conecta dos o más grupos interdependientes —usuarios consumidores y productores complementadores— diseñando algoritmos, reglas de acceso, precios, datos y mecanismos de confianza.

De acuerdo con la literatura contemporánea (Eisenmann et al., 2006; Hagiu y Wright, 2015; Parker et al., 2016; Botella-Andreu et al., 2025), toda plataforma articula cuatro elementos teóricos básicos:
1. **Intermediación multilateral:** conecta usuarios, proveedores, anunciantes o desarrolladores.
2. **Altos costos fijos iniciales de plataforma:** define reglas, estándares, precios, acceso y mecanismos de control para coordinar el ecosistema.
3. **Efectos de red y aprendizaje de datos:** el valor crece con la base de usuarios, la personalización y la reputación, sujeto al límite de congestión y pérdida de exclusividad.
4. **Captura de valor:** monetización vía suscripción, comisión por transacción, publicidad o venta de complementos.

Las categorías de modelos de negocio son analíticas y no excluyentes —una misma empresa suele combinar varias—:

| Modelo de negocio | Lógica de creación y captura de valor | Ejemplos característicos |
| :--- | :--- | :--- |
| **Proveedor de producto digital** | Entrega contenido o servicios digitales directamente al usuario final; monetiza mediante suscripción o pago recurrente. | Netflix, Spotify, Deezer |
| **Marketplace y transacción** | Conecta oferta y demanda y captura una comisión o margen por cada intercambio facilitado. | Amazon, Airbnb, Uber, inDrive, Rappi |
| **Comunidad, atención y publicidad** | El valor surge de la interacción entre usuarios y la capacidad de segmentar audiencia, datos y atención para anunciantes. | Instagram, TikTok, YouTube |
| **Matching y comunicación** | Facilita el encuentro entre usuarios o la comunicación dentro de una red; la utilidad depende de la densidad y actividad de la base. | WhatsApp, Tinder, LinkedIn, Microsoft Teams |
