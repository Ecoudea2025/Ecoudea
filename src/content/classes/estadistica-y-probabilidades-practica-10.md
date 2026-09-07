---
title: "Práctica 03"
course: "estadistica-y-probabilidades"
order: 11
classType: "practica"
description: "Ejercicios sobre: - Variables aleatorias discretas - Esperanza matemática - Varianza - Distribuciones de probabilidad discretas"
math: true
bibliography: "../../referencias.bib"
---

Lista de ejercicios
===================

1.  Suponga que $30\%$ de los solicitantes para cierto trabajo
    industrial posee capacitación avanzada en programación
    computacional. Los candidatos son elegidos aleatoriamente entre la
    población y entrevistados en forma sucesiva. Encuentre la
    probabilidad de que el primer solicitante con capacitación avanzada
    en programación sea el quinto o séptimo entrevistado.

2.  Suponga que por Ley, la vida máxima de la patente para un nuevo
    medicamento es $17$ años. Si restamos el tiempo requerido por la
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
    $X$ (Años)
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
    $p(x)$
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
    Encuentre la función de distribución acumulada del número de
    patentes para nuevos medicamentos.
    </li>
    <li>
    Encuentre el tiempo de vida real promedio de las patentes para
    nuevos medicamentos.
    </li>
    <li>
    Encuentre la probabilidad de que el tiempo de vida real de las
    patentes se encuentre al menos a $1.5$ desviaciones estándar de la
    vida real promedio.
    </li>
    </ol>

3.  Suponga que se realiza un estudio en la ciudad de Medellín para
    observar el número de fotomultas que se le han impuesto a las
    personas que conducen motocicletas de alto cilindraje. Luego de
    recolectar la información, la secretaría de movilidad presenta un
    gráfico de distribución acumulada de la cual se obtiene la siguiente
    tabla.
    
$$\begin{align*}F(x) = \begin{cases}           0  & x<0 \\           0.0134 & 0\leq x<1 \\           0.0420 & 1\leq x<2 \\           0.0992 & 2\leq x<3 \\           0.1909 & 3\leq x<4 \\           0.3130 & 4\leq x<5 \\           0.4526 & 5\leq x<6 \\           0.5922 & 6\leq x<7 \\           0.7162 & 7\leq x<9 \\           0.8155 & 9\leq x<11 \\           0.9377 & 11\leq x<15 \\           1 & x\geq 15         \end{cases}\end{align*}$$

    A partir de esta función de probabilidad
    <ol type="a">
    <li>
    Verifique si la función de distribución acumulada está bien
    definida, y de estarlo, calcule la función de masa de probabilidad
    del número de fotomultas por persona.
    </li>
    <li>
    Si se selecciona una persona al azar, cuál sería la probabilidad de
    que el número de fotomultas que tenga sea más de $3$, pero a lo
    más $8$.
    </li>
    </ol>

4.  En una tienda de barrio, el dueño exhibe $15$ ollas arroceras de
    la misma marca, $9$ negras y $6$ grises. Suponga que en el día,
    $7$ clientes compran cada uno, una olla en momentos diferentes.
    ¿Cuál es la probabilidad de que más de $2$ clientes hayan comprado
    arroceras de color gris?

5.  Sea $X$ una variable aleatoria discreta con distribución de
    probabilidades $p(x)$ dada por:
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td style="text-align:center;">
    $X$
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
    $p(x)$
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
    
$$\begin{align*}\gamma_{1}&=\frac{\mathbb{E}(X^3)-3\mathbb{E}(X^2)\mathbb{E}(X)+2\mathbb{E}(X)^3}{\left[\mathbb{E}(X^2)- \mathbb{E}(X)^2)\right]^{3/2}}\end{align*}$$

6.  Suponga la siguiente función de masa de probabilidad
    
$$\begin{align*}p(x)=\frac{\binom{2}{x}\binom{3}{3-x}}{\binom{5}{3}} \quad \quad \text{ para }x=0,1,2\end{align*}$$

    Calcule el coeficiente de exceso de curtosis, el cual está dado por
    
$$\begin{align*}\gamma_2&=\frac{\mathbb{E}(X^4)-4\mathbb{E}(X^3)\mathbb{E}(X)+6\mathbb{E}(X^2)\mathbb{E}(X)^2 -3\mathbb{E}(X)^4}{\left[\mathbb{E}(X^2) - \mathbb{E}(X)^2\right]^2} -3\end{align*}$$

7.  Un granjero cultiva peras en su finca para posteriormente venderlas
    en la minorista. Dado que los pedidos realizados en la minorista son
    tan grandes, el granjero corre el riesgo de que algunas peras se
    echen a perder durante el tiempo de entrega. Suponga que en una
    entrega de $1000$ peras, el $10\%$ están echadas a perder. Con
    el fin de aceptar dicho pedido, en la minorista realizan una
    selección aleatoria de $15$ peras, y si encuentran más de $5$
    peras echadas a perder, rechazan el pedido del granjero.
    <ol type="a">
    <li>
    Cuál es el número promedio de peras echadas a perder en la muestra
    de $15$?.
    </li>
    <li>
    Si entre las $15$ peras seleccionadas, ya han encontrado $3$
    echadas a perder, ¿Cuál es la probabilidad de que no rechacen el
    pedido?.
    </li>
    </ol>

8.  Una empresa de exploración petrolera va a hacer una serie de
    perforaciones de sondeo en una zona determinada en busca de un pozo
    productivo. La probabilidad de que tenga éxito en un intento dado es
    $0.2$.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que como máximo la tercera perforación
    sea la primera en dar un pozo productivo?.
    </li>
    <li>
    Si la empresa puede darse el lujo de perforar a lo sumo diez pozos,
    ¿cuál es la probabilidad de que no encuentre un pozo productivo?.
    </li>
    </ol>

9.  Dado que ya hemos lanzado al aire una moneda balanceada diez veces y
    no obtuvimos caras, ¿cuál es la probabilidad de que debamos lanzar
    la moneda al menos dos veces más, para obtener la primera cara?

10. Suponga que el número promedio de fallas que puede presentar una
    máquina de ensamble en una empresa al mes es de $6$ fallas.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que en un mes cualquiera, la impresora
    presente a lo más $7$ fallas?
    </li>
    <li>
    Si la impresora ya ha presentado $2$ fallas, ¿Cuál es la
    probabilidad de que al finalizar el mes ésta presente exactamente
    $3$ fallas?
    </li>
    </ol>

11. Suponga que el transito de Medellín afirma que $3$ de cada $10$
    accidentes de tráfico se debe a que al menos uno de los implicados
    no pasó la prueba de alcoholemia. Si ocurren $15$ accidentes de
    tráfico un día cualquiera. ¿Cuál es la probabilidad de que al menos
    $4$ pero menos de $7$ accidentes, no hayan sido causados por
    personas en estado de embriagues?.

12. Una venta particular comprende cuatro artículos seleccionados al
    azar de un lote voluminoso que se sabe contiene $10\%$ de
    artículos defectuosos. Denote con $Y$ el número de artículos
    defectuosos entre los cuatro vendidos. Si los artículos defectuosos
    son devueltos para su reparación, y el costo de reparación está dado
    por $C = 3Y^2 + Y + 2$. Encuentre el costo esperado de reparación
    de los artículos.

13. La Facultad de Ingeniería de la UdeM realiza una encuesta a
    $13000$ estudiantes de Ingeniería Industrial y Ingeniería
    Financiera de último año, en la cual se observa que el $70\%$ de
    los encuestados, no están conformes con su carrera. Si se
    seleccionan al azar $200$ de los encuestados y se les pide su
    opinión, ¿Cuál es la probabilidad de que más de $60$ pero más de
    $80$ no estén conformes con su carrera?.

14. Suponga en un proceso de producción, el número de fallas que tiene
    una maquina en un día antes de apagarse, es una variable aleatoria
    discreta $X$ con función de densidad de probabilidad dada por
    
$$\begin{align*}p(x)=\frac{(x^2+4)}{30} \quad \quad x=0,1,2,3\end{align*}$$

    <ol type="a">
    <li>
    Calcule la función de distribución acumulada para el número de
    fallas que tiene una máquina en un día antes de apagarse.
    </li>
    <li>
    Calcule el valor promedio y desviación estándar para el número de
    fallas que tiene una máquina en un día antes de apagarse.
    </li>
    <li>
    Encuentre la probabilidad de que el número de fallas que tiene una
    máquina en un día antes de apagarse, se encuentre a lo más a $1.5$
    desviaciones estándar de su media.
    </li>
    </ol>

15. De una población de consumidores, $60\%$ tienen fama de preferir
    una marca $A$ de pasta dental. Si se entrevista a un grupo de
    consumidores escogidos al azar,
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que al menos $5$ personas tengan que
    ser entrevistadas para hallar el primer consumidor que prefiera la
    marca $A$ de pasta dental?
    </li>
    <li>
    ¿Cuál es la probabilidad de que a lo más $12$ personas tengan que
    ser entrevistadas para hallar el tercer consumidor que prefiera la
    marca $A$ de pasta dental?
    </li>
    </ol>

16. Dos estudiantes apuestan sobre el número de ejercicios correctos
    realizados por un profesor de matemáticas hasta que cometa un error.
    Si la probabilidad de que el profesor cometa una error en un
    ejercicio es de $0.08$.
    <ol type="a">
    <li>
    ¿Cuál es el promedio del número de ejercicios realizados por el
    profesor hasta cometer un error?.
    </li>
    <li>
    Calcule la desviación estándar de la variable aleatoria $X$.
    </li>
    <li>
    Si van $7$ ejercicios y aún no se equivoca, ¿Cuál es la
    probabilidad de que se equivoque en el décimo ejercicio?
    </li>
    </ol>

17. Suponga que se realiza un estudio estadístico en la UdeM y se
    encuentra que el número promedio de clientes que llegan a la
    cafetería de Ingeniería cada media hora, es de $12$ clientes.
    <ol type="a">
    <li>
    ¿Cuál es el número promedio y desviación estándar de clientes que
    llegan a la cafetería de Ingeniería en $2$ horas?
    </li>
    <li>
    Encuentre la probabilidad de que el número de clientes que llegan a
    la cafetería $2$ horas, se encuentre al menos a $2$ desviaciones
    estándar de su media.
    </li>
    </ol>

18. En una noche de tragos dos estudiantes de Estadística y
    Probabilidades van a un bar que posee una diana de dardos, y deciden
    apostar sobre el número de dardos lanzados por las personas, que
    golpearán o no la diana. Suponga que la probabilidad que una persona
    cualquiera golpe en la diana es de $10\%$, y suponga además, que
    esa noche se lanzan un total de $300$ dardos. Si $X$ es la
    variable aleatoria del número de dardos que golpean la diana. ¿Cuál
    es la probabilidad de que golpeen al menos $42$ pero a lo más
    $50$ dardos?

19. La cantidad diaria de tazas de café que toma un profesor
    normalmente, es una variable aleatoria discreta con un promedio de
    $7$ tazas de café.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, un profesor
    tome más de $3$ pero no más de $6$ tazas de café?.
    </li>
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, el número de
    tazas de café que toma un profesor se encuentre a más de $1.2$
    desviaciones estándar de la media?
    </li>
    </ol>

20. Se cree que de los $10000$ votantes que residen en una ciudad,
    $4000$ están a favor de la iniciativa de talar arboles para
    construir nuevas vías. Se seleccionan al azar $60$ votantes de los
    $10000$ y se les pregunta si están o no de acuerdo con dicha
    iniciativa.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que entre $30$ y $40$ votantes,
    inclusive, estén a favor de dicha iniciativa?.
    </li>
    <li>
    ¿Cuál es el número esperado de votantes que estarán a favor de la
    iniciativa?
    </li>
    </ol>

21. Dos personas, por turnos, tiran un dado imparcial hasta que una de
    ellas lanza un $6$. La persona $A$ tiró primero, la $B$ en
    segundo, $A$ en tercero y así sucesivamente. En vista de que la
    persona $B$ tiró el primer $6$, ¿cuál es la probabilidad de que
    $B$ obtenga el primer $6$ en su segundo tiro (es decir, en el
    cuarto tiro total)?

22. En una industria automotriz, se sabe que $10\%$ de los motores
    fabricados en una línea de ensamble son defectuosos. Si los motores
    se seleccionan al azar uno a la vez y se prueban,
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que el primer motor no defectuoso sea
    hallado en el segundo motor revisado?.
    </li>
    <li>
    ¿Cuál es la probabilidad de los primeros $6$ motores revisados, se
    encuentren no más de $2$ defectuoso?.
    </li>
    </ol>

23. Luego de una revisión exhaustiva, se encuentra que en promedio una
    oblea de silicio producidas por un fabricante tienen dos defectos
    grandes. Si $X$ representa al número de defectos que posee una
    oblea, ¿Cuál es la probabilidad de que una oblea de silicio tenga
    más de cinco defectos grandes?

24. Suponga que la Alcaldía de Medellín decide encuestar familias que
    posean $3$ hijos para observar si hay mayor predominancia en que
    haya más niños o más niñas en la familia. Si la Alcaldía encuentra
    que la probabilidad de ser niño o niña es la misma,
    <ol type="a">
    <li>
    Encuentre la función de distribución de probabilidad para el número
    de niños que hay en una familia que posee $3$ hijos.
    </li>
    <li>
    Encuentre la función de distribución acumulada para el número de
    niñas que hay en una familia que posee $3$ hijos.
    </li>
    </ol>

25. Por experiencia se sabe que el $20\%$ de las inversiones
    realizadas por un experto en finanzas terminan en pérdida. Si se
    seleccionan aleatoriamente $5$ inversiones realizadas por el
    experto,
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que una o tres, no terminen en pérdida?.
    </li>
    <li>
    ¿Cuál es el número promedio de inversiones que no terminen en
    pérdida?.
    </li>
    </ol>