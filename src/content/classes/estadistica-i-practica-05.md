---
title: "Práctica 04"
course: "estadistica-i"
order: 22
classType: "practica"
description: "Ejercicios sobre: - Esperanza matemática - Esperanza condicional - Varianza - Teorema de Chebyshev - Distribuciones de Probabilidad Discretas - Teoremas de Aproximación"
math: true
bibliography: "../../referencias.bib"
---

Lista de ejercicios
-------------------

1.  Suponga que `$30\%$` de los solicitantes para cierto trabajo
    industrial posee capacitación avanzada en programación
    computacional. Los candidatos son elegidos aleatoriamente entre la
    población y entrevistados en forma sucesiva. Encuentre la
    probabilidad de que el primer solicitante con capacitación avanzada
    en programación sea el quinto o séptimo entrevistado.
2.  Suponga que por Ley, la vida máxima de la patente para un nuevo
    medicamento es `$17$` años. Si restamos el tiempo requerido por la
    FDA para someter a pruebas y aprobar el medicamento, se obtiene la
    vida real de la patente para el medicamento, es decir, el tiempo que
    la compañía tiene para recuperar los costos de investigación,
    desarrollo y obtener una utilidad. La distribución de los tiempos de
    vida reales de las patentes para nuevos medicamentos se da a
    continuación:
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td style="text-align:center;">
    Años, \(x\)
    </td>
    <td style="text-align:left;">
    3
    </td>
    <td style="text-align:left;">
    4
    </td>
    <td style="text-align:left;">
    5
    </td>
    <td style="text-align:left;">
    6
    </td>
    <td style="text-align:center;">
    7
    </td>
    <td style="text-align:left;">
    8
    </td>
    <td style="text-align:left;">
    9
    </td>
    <td style="text-align:left;">
    10
    </td>
    <td style="text-align:left;">
    11
    </td>
    <td style="text-align:center;">
    12
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    \(f(x)\)
    </td>
    <td style="text-align:left;">
    0.03
    </td>
    <td style="text-align:left;">
    0.05
    </td>
    <td style="text-align:left;">
    0.07
    </td>
    <td style="text-align:left;">
    0.10
    </td>
    <td style="text-align:center;">
    0.14
    </td>
    <td style="text-align:left;">
    0.20
    </td>
    <td style="text-align:left;">
    0.18
    </td>
    <td style="text-align:left;">
    0.12
    </td>
    <td style="text-align:left;">
    0.07
    </td>
    <td style="text-align:center;">
    0.04
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Encuentre el tiempo de vida real promedio de las patentes para
    nuevos medicamentos.
    </li>
    <li>
    Encuentre la probabilidad de que el tiempo de vida real de las
    patentes se encuentre al menos a \(1.5\) desviaciones estándar de la
    vida real promedio, y compare este resultado con el obtenido con el
    teorema de Chebyshev.
    </li>
    </ol>
3.  Por experiencia se sabe que el `$20\%$` de las inversiones
    realizadas por un experto en finanzas terminan en pérdida. Si se
    seleccionan aleatoriamente `$5$` inversiones realizadas por el
    experto
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que una o tres, no terminen en pérdida?.
    </li>
    <li>
    ¿Cuál es el número promedio de inversiones que no terminen en
    pérdida?.
    </li>
    </ol>
4.  En una tienda de barrio, el dueño exhibe `$15$` ollas arroceras de
    la misma marca, `$9$` negras y `$6$` grises. Suponga que en el día,
    `$7$` clientes compran cada uno, una olla en momentos diferentes.
    ¿Cuál es la probabilidad de que más de `$2$` clientes hayan comprado
    arroceras de color gris?
5.  Suponga que se tiene un total de tres cajas exactamente iguales,
    donde cada una contiene un animal encerrado, un conejo, un hamster y
    una cobaya. Si se trata de adivinar qué clase de animal hay en cada
    caja y `$X$` representa la variable aleatoria discreta del numero de
    aciertos. Escriba la función de masa de probabilidad de la variable
    aleatoria `$X$` y calcule la esperanza y varianza de `$Z= X-3X^2$`.
6.  Si `$X$` y `$Y$` son variables aleatorias discretas con función de
    probabilidad dada por:
    
$$\begin{align*}f(x,y)=k\left(\frac{x+y}{xy}\right) \quad \quad x = 1,2,3; y = 2,3\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor \(k\) que hace a la función de masa de
    probabilidad, una función de probabilidad bien definida.
    </li>
    <li>
    Encuentre la correlación entre \(X\) y \(Z\) donde \(Z = 6X\).
    </li>
    </ol>
7.  Sea `$X$` una variable aleatoria discreta con distribución de
    probabilidades `$f(x)$` dada por:
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td style="text-align:center;">
    \(x\)
    </td>
    <td style="text-align:left;">
    1
    </td>
    <td style="text-align:left;">
    3
    </td>
    <td style="text-align:left;">
    4
    </td>
    <td style="text-align:left;">
    5
    </td>
    <td style="text-align:center;">
    7
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    \(f(x)\)
    </td>
    <td style="text-align:left;">
    0.31
    </td>
    <td style="text-align:left;">
    0.13
    </td>
    <td style="text-align:left;">
    0.15
    </td>
    <td style="text-align:left;">
    0.18
    </td>
    <td style="text-align:center;">
    0.23
    </td>
    </tr>
    </tbody>
    </table>
    Encuentre el coeficiente de asimetría, el cuál está dado por
    
$$\begin{align*}\gamma_{1}&= \mathbb{E}\left[\left({\frac{X-\mu}{\sigma}}\right)^{3}\right]={\frac{\mu_{3}}{\sigma^{3}}}={\frac{\mathbb{E}\left[(X-\mu)^{3}\right]}{(\mathbb{E}\left[(X-\mu)^{2}\right])^{3/2}}}\\ \gamma_{1}&=\frac{\mathbb{E}(X^3)-3\mathbb{E}(X^2)\mathbb{E}(X)+2\mathbb{E}(X)^3}{\left[\mathbb{E}(X^2)- \mathbb{E}(X)^2)\right]^{3/2}}\end{align*}$$

8.  Un granjero cultiva peras en su finca para posteriormente venderlas
    en la minorista. Dado que los pedidos realizados en la minorista son
    tan grandes, el granjero corre el riesgo de que algunas peras se
    echen a perder durante el tiempo de entrega. Suponga que en una
    entrega de `$1000$` peras, el `$10\%$` están echadas a perder. Con
    el fin de aceptar dicho pedido, en la minorista realizan una
    selección aleatoria de `$15$` peras, y si encuentran más de `$5$`
    peras echadas a perder, rechazan el pedido del granjero.
    <ol type="a">
    <li>
    Cuál es el número promedio de peras echadas a perder en la muestra
    de \(15\)?.
    </li>
    <li>
    Si entre las \(15\) peras seleccionadas, ya han encontrado \(3\)
    echadas a perder, ¿Cuál es la probabilidad de que no rechacen el
    pedido?.
    </li>
    </ol>
9.  Una empresa de exploración petrolera va a hacer una serie de
    perforaciones de sondeo en una zona determinada en busca de un pozo
    productivo. La probabilidad de que tenga éxito en un intento dado es
    `$0.2$`.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que la tercera perforación sea la
    primera en dar un pozo productivo?.
    </li>
    <li>
    Si la empresa puede darse el lujo de perforar a lo sumo diez pozos,
    ¿cuál es la probabilidad de que no encuentre un pozo productivo?.
    </li>
    </ol>
10. A partir de la siguiente función de masa de probabilidad
    
$$\begin{align*}f(x)=\frac{\binom{2}{x}\binom{3}{3-x}}{\binom{5}{3}} \quad \quad \text{ para }x=0,1,2\end{align*}$$

    Calcule el coeficiente de exceso de curtosis, el cual está dado por
    
$$\begin{align*}\gamma_{2}&= \mathbb{E}\left[\left({\frac{X-\mu}{\sigma}}\right)^{4}\right] -3={\frac{\mu_{4}}{\sigma^{4}}} -3 ={\frac{\mathbb{E}\left[(X-\mu)^{4}\right]}{(\mathbb{E}\left[(X-\mu)^{2}\right])^{4/2}}} -3\\ \gamma_2&=\frac{\mathbb{E}(X^4)-4\mathbb{E}(X^3)\mathbb{E}(X)+6\mathbb{E}(X^2)\mathbb{E}(X)^2 -3\mathbb{E}(X)^4}{\left[\mathbb{E}(X^2) - \mathbb{E}(X)^2\right]^2} -3\end{align*}$$

11. Dado que ya hemos lanzado al aire una moneda balanceada diez veces y
    no obtuvimos caras, ¿cuál es la probabilidad de que debamos lanzar
    la moneda al menos dos veces más, para obtener la primera cara?
12. Sea `$X$` el número de veces que fallará cierta máquina de control
    numérico: 1, 2 o 3 veces en un día dado, y `$Y$` denota el número de
    veces que se llama a un técnico para una emergencia. Suponga que su
    distribución de probabilidad conjunta estará dada como
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td rowspan="2" colspan="2" style="text-align:center; vertical-align: middle;">
    <script type="math/tex">p(x,y)</script>
    </td>
    <td style="text-align:center;" colspan="3">
    <script type="math/tex">X</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{2}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{3}</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;vertical-align: middle !important;" rowspan="3">
    <script type="math/tex">Y</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.05</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.05</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.10</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{3}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.05</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.10</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.35</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{5}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">k</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.20</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.10</script>
    </td>
    </tr>
    </tbody>
    </table>
    Calcule el `$Corr(X,Y^2)$`.
13. Una moneda se lanza dos veces. Sea `$X$` el número de caras en el
    primer lanzamiento y `$Y$` el número total de caras en los `$2$`
    lanzamientos. Si la moneda no está balanceada y la probabilidad de
    sello es dos veces la probabilidad de cara, calcule
    <ol type="a">
    <li>
    la media y varianza de \(X\) y \(Y\)
    </li>
    <li>
    el coeficiente de asimetría de \(X\) y \(Y\)
    </li>
    <li>
    la correlación de \(3X\) y \(2Y\)
    </li>
    </ol>
14. Un sistema químico que surge de una reacción química tiene dos
    componentes importantes, entre otros, en una mezcla. La distribución
    conjunta que describe las proporciones `$X$` y `$Y$` de estos dos
    componentes está dada por
    
$$\begin{align*}f(x,y)=\begin{cases}2  & 0<x<y<1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Determine la esperanza condicional \(\mathbb{E}(Y | X)\)
    </li>
    <li>
    Determine la esperanza condicional \(\mathbb{E}(X | Y)\)
    </li>
    </ol>
15. El número de problemas que puede presentar la impresora del centro
    de documentación de la facultad al mes, es una variable aleatoria
    uniforme en el conjunto cerrado de `$1$` a `$6$` errores.
    <ol type="a">
    <li>
    ¿Cuál es el número esperado de fallas que tenga la impresora?
    </li>
    <li>
    Si la impresora ya ha presentado al menos \(2\) fallas, ¿Cuál es la
    probabilidad de que presente exactamente \(3\)?
    </li>
    </ol>
16. Considere la siguiente función de densidad de probabilidad
    
$$\begin{align*}f(x) =\begin{cases}\frac{3}{2}\sqrt{x}, & 0< x < 1\\ 0, & \text{en otro caso} \end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de \(1/X\).
    </li>
    <li>
    Calcule la esperanza de \(2/X^2\)
    </li>
    </ol>
17. Suponga que el transito de Medellín afirma que `$3$` de cada `$10$`
    accidentes de tráfico se debe a que al menos uno de los implicados
    no pasó la prueba de alcoholemia. Si ocurren `$15$` accidentes de
    tráfico un día cualquiera. ¿Cuál es la probabilidad de que al menos
    `$4$` pero menos de `$7$` accidentes, no hayan sido causados por
    personas en estado de embriagues?.
18. Calcule la covarianza de las variables aleatorias `$X$` y `$Y$` que
    tienen la siguiente función de densidad de probabilidad conjunta
    
$$\begin{align*}f(x,y)=\begin{cases}x+y & 0<x<1,\quad 0<y<1,\\0 & \text{en otro caso}\end{cases}\end{align*}$$

19. Una venta particular comprende cuatro artículos seleccionados al
    azar de un lote voluminoso que se sabe contiene `$10\%$` de
    artículos defectuosos. Denote con `$Y$` el número de artículos
    defectuosos entre los cuatro vendidos. Si los artículos defectuosos
    son devueltos para su reparación, y el costo de reparación está dado
    por `$C = 3Y^2 + Y + 2$`. Encuentre el costo esperado de reparación
    de los artículos.
20. La función de densidad de probabilidad conjunta de las variables
    aleatorias `$X$`, `$Y$` y `$Z$` está dada por
    
$$\begin{align*}f(x,y,z)=\begin{cases}4xyz^2; &0< x,y <1; 0< z<3 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    Calcule
    <ol type="a">
    <li>
    la correlación de \(X\) y \(Y\).
    </li>
    <li>
    la correlación de \(X\) y \(Z\).
    </li>
    <li>
    la correlación de \(Y\) y \(Z\).
    </li>
    </ol>
21. Suponga que el tiempo medido en unidades de 100 horas, que se usa
    una licuadora en un hogar durante un año es una variable aleatoria
    continua `$X$` con función de densidad de probabilidad dada por:
    
$$\begin{align*}f(x) =\begin{cases}x & 0< x < 1 \\ 2-x & 1\leq x < 2 \\ 0 & \text{en otro caso} \end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la media y varianza de la variable aleatoria \(X\)
    </li>
    <li>
    Calcule la varianza de la variable aleatoria \(Y=2X+3\).
    </li>
    <li>
    Calcule la covarianza entre \(X\) y \(Y\).
    </li>
    </ol>
22. La Facultad de Ciencias Económicas de cierta universidad realiza a
    nivel nacional, una encuesta a `$13000$` estudiantes de economía y
    administración de último año, en la cual se observa que el `$70\%$`
    de los encuestados, no están conformes con su carrera. Si se
    seleccionan al azar `$200$` de los encuestados y se les pide su
    opinión, ¿Cuál es la probabilidad de que más de `$60$` pero no más
    de `$80$` no estén conformes con su carrera?.
23. Suponga en un proceso de producción, el número de fallas que tiene
    una maquina en un día antes de apagarse, es una variable aleatoria
    discreta `$X$` con función de masa de probabilidad dada por
    
$$\begin{align*}f(x)=\frac{(x^2+4)}{30} \quad \quad x=0,1,2,3\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor promedio de la variable aleatoria \(X\).
    </li>
    <li>
    Calcule la desviación estándar de la variable aleatoria \(X\).
    </li>
    <li>
    Encuentre la probabilidad de que la variable aleatoria \(X\), se
    encuentre a lo más a \(1.5\) desviaciones estándar de su media y
    compare el resultado obtenido con el teorema de Chebyshev.
    </li>
    </ol>
24. De una población de consumidores, `$60\%$` tienen fama de preferir
    una marca `$A$` de pasta dental. Si se entrevista a un grupo de
    consumidores escogidos al azar,
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que al menos \(5\) personas tengan que
    ser entrevistadas para hallar el primer consumidor que prefiera la
    marca \(A\) de pasta dental?
    </li>
    <li>
    ¿Cuál es la probabilidad de que a lo más \(12\) personas tengan que
    ser entrevistadas para hallar el tercer consumidor que prefiera la
    marca \(A\) de pasta dental?
    </li>
    </ol>
25. Dos estudiantes apuestan sobre el número de ejercicios correctos
    realizados por el profesor de matemáticas hasta que cometa un error.
    Si la probabilidad de que el profesor cometa una error en un
    ejercicio es de `$0.08$`.
    <ol type="a">
    <li>
    ¿Cuál es el promedio del número de ejercicios realizados por el
    profesor hasta cometer un error?.
    </li>
    <li>
    Calcule la desviación estándar de la variable aleatoria \(X\).
    </li>
    <li>
    Si van 7 ejercicios y aún no se equivoca, ¿Cuál es la probabilidad
    de que se equivoque en el décimo ejercicio?
    </li>
    </ol>
26. Sea `$X$` una variable aleatoria continua con distribución de
    probabilidades `$f(x)$` dada por
    
$$\begin{align*}f(x)=\begin{cases}kx^2 & -5 \leq x \leq 3, \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Encuentre el valor de \(k\) que haga a \(f(x)\) una función densidad
    de probabilidad.
    </li>
    <li>
    Calcule la media y la varianza de la variable aleatoria \(Y=X^2\).
    </li>
    <li>
    Encuentre la probabilidad de que la variable aleatoria \(X\), se
    encuentre a lo más a 2.3 desviaciones estándar de su media y compare
    el resultado obtenido con el teorema de Chebyshev.
    </li>
    </ol>
27. Calcule la probabilidad de que la siguiente función de densidad de
    probabilidad se encuentre a dos desviaciones estándar de la media y
    compare con el resultado dado por el teorema de Chebyshev.
    
$$\begin{align*}f(x)=6x(1-x), \quad 0<x<1\end{align*}$$

28. Suponga que cierto tipo de pequeñas empresas de procesamiento de
    datos están tan especializadas que algunas tienen dificultades para
    obtener utilidades durante su primer año de operación. La función de
    densidad de probabilidad que caracteriza la proporción `$Y$` que
    obtiene utilidades está dada por
    
$$\begin{align*}f(y)=\begin{cases}ky^4(1-y)^3 & 0\leq y \leq 1,\\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    ¿Cuál es el valor de \(k\) que hace de la anterior una función de
    densidad válida?
    </li>
    <li>
    Calcule la varianza de la variable aleatoria \(Z=3Y-4\).
    </li>
    </ol>
29. Suponga que se realiza un estudio estadístico y se encuentra que el
    número de clientes que llega donde Pastora en media hora, es una
    variable aleatoria Poisson con media de `$4$` clientes.
    <ol type="a">
    <li>
    ¿Cuál es el número promedio y desviación estándar de clientes que
    llegada donde pastora en \(2\) horas?
    </li>
    <li>
    Encuentre la probabilidad de que el número de clientes que llegan
    donde pastora en \(2\) horas, se encuentre al menos a \(2\)
    desviaciones estándar de su media y compare el resultado obtenido
    con el teorema de Chebyshev.
    </li>
    </ol>
30. Sean `$X$` y `$Y$` son variables aleatorias que poseen la siguiente
    función de densidad de probabilidad conjunta
    
$$\begin{align*}f(x,y)=xye^{-x-y},\quad x>0,y>0\end{align*}$$

    Entonces, a partir de ésta, calcule la covarianza de `$6X^2$` y
    `$3Y^3$`.
31. En una noche de tragos dos estudiantes de Estadística I van a un bar
    que posee una diana de dardos, y deciden apostar sobre el número de
    dardos lanzados por las personas, que golpearán o no la diana.
    Suponga que la probabilidad que una persona cualquiera golpe en la
    diana es de `$10\%$`, y suponga además, que esa noche se lanzan un
    total de `$300$` dardos. Si `$X$` es la variable aleatoria del
    número de dardos que golpean la diana. ¿Cuál es la probabilidad de
    que golpeen al menos `$42$` pero a lo más `$50$` dardos?
32. Una empresa dulcera distribuye cajas de chocolates con un surtido de
    cremas, chiclosos y envinados. Suponga que cada caja pesa `$1$`
    kilogramo, pero que los pesos individuales de cremas, chiclosos y
    envinados varían de una a otra caja. Para una caja seleccionada al
    azar, represente los pesos de las cremas y los chiclosos con `$X$` y
    `$Y$`, respectivamente, si se supone que la función de densidad
    conjunta de estas variables es
    
$$\begin{align*}f(x,y)=\begin{cases}24xy & 0\leq x\leq1;0\leq y\leq1; x+y\leq1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de \(Z = 3Y - 2X\)
    </li>
    <li>
    Calcule la varianza de \(Z\)
    </li>
    </ol>
33. La cantidad diaria de vasos de café que toma un profesor
    normalmente, es una variable aleatoria uniforme en el conjunto
    cerrado de `$3$` hasta `$7$` vasos.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, un profesor
    tome entre \(5\) y \(6\) vasos, inclusive?.
    </li>
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, el número de
    tintos que toma un profesor se encuentre a más de \(1.2\)
    desviaciones estándar de la media? Compare el resultado con el
    obtenido mediante el teorema de Chebyshev.
    </li>
    </ol>
34. Si `$X$`, `$Y$` y `$Z$` tienen la siguiente función de densidad de
    probabilidad conjunta:
    
$$\begin{align*}f(x,y,z)=\begin{cases}kxy^2z& 0<x<1;\quad 0<y<1;\quad 0<z<2 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor \(k\) que hace que la función de densidad de
    probabilidad conjunta esté bien definida.
    </li>
    <li>
    Calcule \(\mathbb{E}(X |Y > \frac{1}{2}, 1 < Z < 2)\)
    </li>
    </ol>
35. Se cree que de los `$10000$` votantes que residen en una ciudad,
    `$4000$` están a favor de la iniciativa de talar arboles para
    construir nuevas vías. Se seleccionan al azar `$60$` votantes de los
    `$10000$` y se les pregunta si están o no de acuerdo con dicha
    iniciativa.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que entre \(30\) y \(40\) votantes,
    inclusive, estén a favor de dicha iniciativa?.
    </li>
    <li>
    ¿Cuál es el número esperado de votantes que estarán a favor de la
    iniciativa?
    </li>
    </ol>
36. Dos personas, por turnos, tiran un dado imparcial hasta que una de
    ellas lanza un `$6$`. La persona `$A$` tiró primero, la `$B$` en
    segundo, `$A$` en tercero y así sucesivamente. En vista de que la
    persona `$B$` tiró el primer `$6$`, ¿cuál es la probabilidad de que
    `$B$` obtenga el primer `$6$` en su segundo tiro (es decir, en el
    cuarto tiro total)?
37. En una industria automotriz, se sabe que diez por ciento de los
    motores fabricados en una línea de ensamble son defectuosos. Si los
    motores se seleccionan al azar uno a la vez y se prueban, ¿cuál es
    la probabilidad de que el primer motor no defectuoso sea hallado en
    el segundo intento?
38. Luego de una revisión exhaustiva, se encuentra que en promedio una
    oblea de silicio producidas por un fabricante tienen dos defectos
    grandes. Si `$X$` representa al número de defectos que posee una
    oblea, ¿Cuál es la probabilidad de que una oblea de silicio tenga
    más de cinco defectos grandes?
39. Un proveedor de queroseno tiene un tanque de `$150$` galones que se
    llena al empezar cada semana. Su demanda semanal muestra un
    comportamiento de frecuencia relativo que aumenta de manera continua
    hasta `$100$` galones y luego se nivela entre `$100$` y `$150$`
    galones. Si `$Y$` denota la demanda semanal en cientos de galones,
    la frecuencia relativa de demanda puede ser modelada por
    
$$\begin{align*}f(y)=\begin{cases}y & 0\leq y\leq 1 \\1 & 1<y\leq 1.5 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de la variable aleatoria \(Y\).
    </li>
    <li>
    Calcule la varianza de la variable aleatoria \(Y\).
    </li>
    <li>
    Calcule la asimetría de la variable aleatoria \(Y\).
    </li>
    <li>
    Calcule la curtosis de la variable aleatoria \(Y\).
    </li>
    </ol>
40. Sea `$X$` la variable aleatoria del número de clientes que llega a
    una centro comercial en un periodo de una hora. Si la distribución
    acumulada de `$X$` es:
    
$$\begin{align*}F(x) =\begin{cases}0 & x < 0\\0.03 & 0\leq x < 1 \\ 0.12 & 1\leq x < 2 \\ 0.21 & 2\leq x < 3\\ 0.33 & 3\leq x < 4\\ 0.52 & 4\leq x < 5\\ 0.74 & 5\leq x < 6 \\ 0.89 & 6\leq x < 7 \\ 0.96 & 7\leq x < 8 \\ 1.00 & 8\geq x\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de \(X\).
    </li>
    <li>
    Calcule la esperanza de \(Y=\sqrt{3X}\).
    </li>
    </ol>