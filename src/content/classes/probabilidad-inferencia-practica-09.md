---
title: "Práctica 03"
course: "probabilidad-inferencia"
order: 19
classType: "practica"
description: "Ejercicio sobre: - Variables aleatorias. - Distribuciones de probabilidad."
math: true
bibliography: "../../referencias.bib"
---

# Lista de ejercicios

1.  Suponga que por Ley, la vida máxima de la patente para un nuevo
    medicamento es `$17$` años. Si restamos el tiempo requerido por la
    FDA para someter a pruebas y aprobar el medicamento, se obtiene la
    vida real de la patente para el medicamento, es decir, el tiempo que
    la compañía tiene para recuperar los costos de investigación,
    desarrollo y obtener una utilidad. La distribución de los tiempos de
    vida reales de las patentes para nuevos medicamentos se da a
    continuación:
    <table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
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
    \(p(x)\)
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
    Encuentre la función de distribución acumulada \(F(x)\).
    </li>
    <li>
    Calcule la probabilidad de que el tiempo de vida en años de la
    patente sea a lo más \(9\) años.
    </li>
    </ol>
2.  Sea `$X$` la variable aleatoria del número de clientes que llegan a
    un centro comercial en un periodo de una hora. Si la distribución
    acumulada de `$X$` es:
    
$$\begin{align*}F(x) =\begin{cases}0 & x < 0\\0.03 & 0\leq x < 1 \\ 0.12 & 1\leq x < 2 \\ 0.21 & 2\leq x < 3\\ 0.33 & 3\leq x < 4\\ 0.52 & 4\leq x < 5\\ 0.74 & 5\leq x < 6 \\ 0.89 & 6\leq x < 7 \\ 0.96 & 7\leq x < 8 \\ 1.00 & 8\geq x\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Encuentre la función de masa de probabilidad de la variable
    aleatoria \(X\).
    </li>
    <li>
    Calcule la \(\mathbb{P}(X \gt  4.3)\).
    </li>
    <li>
    Calcule la \(\mathbb{P}(3\leq X\leq 7)\).
    </li>
    <li>
    Calcule la \(\mathbb{P}(X=5)\).
    </li>
    <li>
    Calcule la media y desviación estándar del número de clientes que
    llegan a un centro comercial en una hora.
    </li>
    </ol>
3.  Considere la función de densidad
    
$$\begin{align*}f(x) =\begin{cases}k\sqrt{x}, & 0< x < 1\\ 0, & \text{En otro caso} \end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Encuentre el valor de \(k\) para que \(f(x)\) sea una función de
    densidad de probabilidad bien definida.
    </li>
    <li>
    Calcule la función de distribución acumulada \(F(x)\) y utilice el
    resultado para calcular \(\mathbb{P}(0.24 \lt  X \lt  0.63)\).
    </li>
    <li>
    Calcule el valor promedio y desviación estándar de la variable
    aleatoria \(X\).
    </li>
    </ol>
4.  Suponga que el tiempo medido en unidades de `$100$` horas, en las
    cuales, se usa una licuadora en un hogar durante un año, es una
    variable aleatoria continua `$X$` con función de densidad de
    probabilidad dada por:
    
$$\begin{align*}f(x) =\begin{cases}x & 0< x < 1 \\ 2-x & 1\leq x < 2 \\ 0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Pruebe si efectivamente es una función de densidad de probabilidad
    bien definida, de no serlo, multiplique la función por una constante
    \(k\) que hace a \(p(x)\) estar bien definida.
    </li>
    <li>
    Calcule la función de distribución acumulada \(F(x)\).
    </li>
    <li>
    Calcule la probabilidad de que en un año una familia use la
    licuadora entre \(65\) y \(100\) horas.
    </li>
    <li>
    Calcule la media y la varianza del tiempo de uso de la licuadora,
    medido en unidades de \(100\) horas.
    </li>
    </ol>
5.  El tiempo que pasa, en minutos, para que un radar detecte entre
    conductores sucesivos a los que exceden los límites de velocidad es
    una variable aleatoria continua con una función de distribución
    acumulativa
    
$$\begin{align*}F(x) =\begin{cases}0, & 0< x\\ 1-e^{-x/10}, & x \geq 0 \end{cases}\end{align*}$$

    Calcule la probabilidad de que el tiempo que pase para que el radar
    detecte entre conductores sucesivos a los que exceden los límites de
    velocidad sea menor de `$12$` minutos
    <ol type="a">
    <li>
    Usando la función de distribución acumulativa de \(X\).
    </li>
    <li>
    Utilizando la función de densidad de probabilidad de \(X\).
    </li>
    </ol>
6.  Sea `$X$` una variable aleatoria continua que representa el tiempo,
    en minutos, que tarda un hamster en superar un laberinto, tal que,
    la función de densidad de probabilidad `$f(x)$` está dada por:
    
$$\begin{align*}f(x)=\begin{cases}\frac{x}{\theta^2}e^{-x^2/(2\theta^2)} & x > 0;\quad \theta > 0,\\0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Verifique si \(f(x)\) es efectivamente una función de densidad de
    probabilidad.
    </li>
    <li>
    Suponga que \(\theta = 100\). Cuál es la probabilidad de que el
    hamster tarde a lo más de \(200\) minutos en superar el laberinto? y
    cuál es la probabilidad de que tarde al menos \(200\) minutos?.
    </li>
    <li>
    Suponga nuevamente que \(\theta = 100\). ¿Cuál es el valor esperado
    y varianza de del tiempo que tarda el hamster en superar el
    laberinto?.
    </li>
    <li>
    De una expresión para la función de confiabilidad
    \(R(x) = \mathbb{P}(X \gt  x)\)?.
    </li>
    </ol>
7.  Considere a `$X$` la variable aleatoria que representa la suma de
    las caras para el lanzamiento de dos dados, con función de masa de
    probabilidad dada por
    
$$\begin{align*}p(x)=\begin{cases}6-|7-x| & x = 2,3,\ldots,12 ,\\0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Compruebe si \(f(x)\) es es efectivamente una función de masa de
    probabilidad bien definida. De no serlo, encuentre el valor \(k\)
    que haría a \(f(x)\) bien definida.
    </li>
    <li>
    Calcule la función de distribución acumulada, \(F(x)\).
    </li>
    <li>
    Calcule la probabilidad de que la suma de las caras se encuentren
    entre \(5\) y \(9\) inclusive.
    </li>
    <li>
    Calcule la probabilidad de que la suma de las caras sean mayores que
    \(7\) o a lo más \(4\).
    </li>
    </ol>
8.  El `$20\%$` de las inversiones realizadas por un experto en finanzas
    terminan en pérdida. Si se seleccionan aleatoriamente `$5$`
    inversiones realizadas por el experto, ¿Cuál es la probabilidad de
    que una o tres, no terminen en pérdida?
9.  Suponga que se realiza un estudio en la ciudad de Medellín para
    observar el número de fotomultas que se le han impuesto a las
    personas que conducen motocicletas de alto cilindraje. Luego de
    recolectar la información, la secretaría de movilidad presenta un
    gráfico de distribución acumulada de la cual se obtiene la siguiente
    tabla.
    
$$\begin{align*}F(x) = \begin{cases}      0.0026  & x<2 \\      0.0134 & 2\leq x<3 \\      0.0420 & 3\leq x<4 \\      0.0992 & 4\leq x<5 \\      0.1909 & 5\leq x<6 \\      0.3130 & 6\leq x<7 \\      0.4526 & 7\leq x<9 \\      0.5922 & 9\leq x<11 \\      0.7162 & 11\leq x<12 \\      0.8155 & 12\leq x<14 \\      0.9377 & 14\leq x<15 \\      1 & x\geq 15 \end{cases}\end{align*}$$

    A partir de esta función de probabilidad
    <ol type="a">
    <li>
    Verifique si la función de distribución acumulada está bien
    definida, y de estarlo, calcule la función de masa de probabilidad
    del número de fotomultas por persona.
    </li>
    <li>
    Si se selecciona una persona al azar, cuál sería la probabilidad de
    que el número de fotomultas que tenga sea más de 3, pero a lo más 8.
    </li>
    </ol>
10. Según una página de estadísticas deportivas, el número promedio de
    goles que anota el Barcelona por partido es de `$2.61$`. ¿Cuál es la
    probabilidad de que en un determinado partido anote más de `$2$`
    goles?.
11. Suponga que el número de llamadas telefónicas que entran a un
    conmutador particular siguen un proceso de Poisson con un promedio
    de `$5$` llamadas entrantes por minuto.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que transcurra hasta un minuto en el
    momento en que han entrado \(1\) llamada al conmutador?
    </li>
    <li>
    ¿Cuál es la probabilidad de que transcurra hasta un minuto en el
    momento en que han entrado \(3\) llamadas al conmutador?
    $$\begin{align*}
    f(x)=\frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-\frac{x}{\beta}} \quad x>0,\; \alpha>0, \;\beta>0
    \end{align*}
    $$
    </li>
    </ol>
12. En el artículo de W. Pang, et. al (2001) “*Parameter Estimation with
    Only One Complete Failure Observation, International Journal of
    Reliability, Quality, and Safety Engineering, 2001:109-122*”, se
    modela la duración, en horas, de cierto tipo de cojinete con la
    distribución de Weibull(`$\alpha = 2.25, \beta = 2109.705$`).
    <ol type="a">
    <li>
    Determine la probabilidad de que un cojinete dure más de \(1000\)
    horas.
    </li>
    <li>
    Determine la probabilidad de que un cojinete dure menos de \(2000\)
    horas.
    </li>
    <li>
    Determine la media y desviación estándar de la duración de un
    cojinete.
    </li>
    <li>
    ¿Cuál es el riesgo en \(t = 2000\) horas?.
    </li>
    </ol>
13. El periodo de vida de una broca en una operación mecánica, en horas,
    tiene una distribución de Weibull con `$\alpha = 1/2$` y
    `$\beta = 35$`. Calcule la probabilidad de que la broca falle antes
    de `$10$` horas de uso.
14. El número de automóviles que llegan a cierta intersección por minuto
    tiene una distribución de Poisson con una media de `$3$`. Existe
    interés por el tiempo que transcurre antes de que `$4$` automóviles
    aparezcan en la intersección.
    <ol type="a">
    <li>
    Cuál es la probabilidad de que más de \(4\) automóviles aparezcan en
    la intersección durante cualquier minuto determinado.
    </li>
    <li>
    Cuál es la probabilidad de que transcurran más de 2 minutos antes de
    que lleguen \(4\) autos.
    </li>
    <li>
    Determine la media y desviación estándar del tiempo que transcurre
    hasta que aparece un automóvil en la intersección.
    </li>
    </ol>
15. Suponga que se realiza un estudio estadístico y se encuentra que
    número de clientes que llega donde Pastora en media hora, es una
    variable aleatoria Poisson con media de `$4$`.
    <ol type="a">
    <li>
    ¿Cuál es el tiempo promedio y la desviación para la llegada de cada
    cliente?.
    </li>
    <li>
    Si en los \(10\) primeros minutos no ha llegado ningún cliente,
    ¿Cuál es la probabilidad de que llegue un cliente en los próximos
    \(10\) minutos?.
    </li>
    </ol>
16. Cada semestre se presentan miles de personas para ganar uno de los
    `$260$` cupos que se abren para el programa de ingeniería
    industrial. Si el puntaje obtenido por los estudiantes se distribuye
    aproximadamente normal con media de `$52.7$` puntos y desviación
    estándar de `$15.3$` puntos.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que una persona que se presenta a
    ingeniería industrial sea admitida si se tiene que el puntaje de
    corte es de \(67.14\) puntos?.
    </li>
    <li>
    Si se sabe que una persona sacó más de \(57.3\) puntos, ¿Cuál es la
    probabilidad de que haya superado el puntaje de corte de \(67.14\)
    puntos?.
    </li>
    </ol>
17. Se sabe que los resultados en cierto examen de estadística, tienen
    una distribución normal, con media `$3.1$` y desviación estándar
    `$0.35$`. ¿Cuál es la probabilidad de que un estudiante obtenga una
    nota entre `$3$` y `$3.5$`?
18. La magnitud de temblores registrados en una región de América del
    Norte puede modelarse como si tuviera una distribución exponencial
    con media `$2.4$`, según se mide en la escala de Richter. Encuentre
    la probabilidad de que un temblor que ocurra en esta región
    <ol type="a">
    <li>
    Sea mayor que 3.0 en la escala de Richter.
    </li>
    <li>
    Caiga entre 2.0 y 3.0 en la escala de Richter.
    </li>
    </ol>
19. El tiempo `$Y$` necesario para completar una operación clave en la
    construcción de casas tiene una distribución exponencial con media
    de `$10$` horas. La fórmula `$C = 100 + 40Y + 3Y^2$` relaciona el
    costo `$C$` de completar esta operación con el cuadrado del tiempo
    para completarla. Encuentre la media y la varianza de `$C$`.
20. Suponga que el transito de Medellín afirma que `$3$` de cada `$10$`
    accidentes de tráfico se debe a que al menos uno de los implicados
    no pasó la prueba de alcoholemia. Si ocurren `$15$` accidentes de
    tráfico un día cualquiera. ¿Cuál es la probabilidad de que al menos
    `$4$` pero menos de `$7$` accidentes, no hayan sido causados por
    “borrachitos”.
21. Sea `$X$` una variable aleatoria discreta con distribución de
    probabilidades `$f(x)$` dada por:
    <table class="table table-striped" style="color: black; width: auto !important; margin-left: auto; margin-right: auto;">
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
    \(p(x)\)
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
    
$$\begin{align*}\gamma_{1}&= \mathbb{E}\left[\left({\frac{X-\mu}{\sigma}}\right)^{3}\right]={\frac{\mu_{3}}{\sigma^{3}}}={\frac{\mathbb{E}\left[(X-\mu)^{3}\right]}{(\mathbb{E}\left[(X-\mu)^{2}\right])^{3/2}}}\\ \gamma_{1}&=\frac{\mathbb{E}(X^3)-3\mathbb{E}(X^2)\mathbb{E}(X)+2\mathbb{E}(X)^3}{[\mathbb{E}(X^2)- \mathbb{E}(X)^2)]^{3/2}}\end{align*}$$

22. A partir de la siguiente función de masa de probabilidad
    
$$\begin{align*}p(x)=\frac{\binom{2}{x}\binom{3}{3-x}}{\binom{5}{3}} \quad \quad \text{ para }x=0,1,2\end{align*}$$

    Calcule el coeficiente de exceso de curtosis, el cual está dado por
    
$$\begin{align*}\gamma_{2}&= \mathbb{E}\left[\left({\frac{X-\mu}{\sigma}}\right)^{4}\right] -3={\frac{\mu_{4}}{\sigma^{4}}} -3 ={\frac{\mathbb{E}\left[(X-\mu)^{4}\right]}{(\mathbb{E}\left[(X-\mu)^{2}\right])^{4/2}}} -3\\ \gamma_2&=\frac{\mathbb{E}(X^4)-4\mathbb{E}(X^3)\mathbb{E}(X)+6\mathbb{E}(X^2)\mathbb{E}(X)^2 -3\mathbb{E}(X)^4}{[\mathbb{E}(X^2) - \mathbb{E}(X)^2]^2} -3\end{align*}$$

23. Considere la siguiente función de densidad de probabilidad
    
$$\begin{align*}f(x) =\begin{cases}kx^{3/2}, & 0< x < 1\\ 0, & \text{en otro caso} \end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de \(1/X\).
    </li>
    <li>
    Calcule la esperanza de \(2/X^2\)
    </li>
    </ol>
24. Suponga que cierto tipo de pequeñas empresas de procesamiento de
    datos están tan especializadas que algunas tienen dificultades para
    obtener utilidades durante su primer año de operación. La función de
    densidad de probabilidad que caracteriza la proporción `$Y$` que
    obtiene utilidades está dada por
    
$$\begin{align*}f(y)=\begin{cases}ky^4(1-y)^3 & 0\leq y \leq 1\\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    ¿Cuál es el valor de \(k\) que hace de la anterior una función de
    densidad válida?
    </li>
    <li>
    Calcule la varianza de la variable aleatoria \(Z=3Y-4\).
    </li>
    </ol>
25. El tiempo que trabaja en horas un profesor normalmente, posee una
    distribución exponencial con parámetro de escala `$6$`.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, un profesor
    trabaje entre \(5\) y \(6\) horas?.
    </li>
    <li>
    Cuál es la media y la desviación estándar del tiempo en horas que
    trabaja una profesor en un día.
    </li>
    <li>
    Si en un día un profesor ya ha trabajado \(5\) horas, cuál es la
    probabilidad de que trabaje menos de \(3\) horas más?.
    </li>
    </ol>
26. Un proveedor de queroseno tiene un tanque de `$150$` galones que se
    llena al empezar cada semana. Su demanda semanal muestra un
    comportamiento de frecuencia relativo que aumenta de manera continua
    hasta `$100$` galones y luego se nivela entre `$100$` y `$150$`
    galones. Si `$Y$` denota la demanda semanal en cientos de galones,
    la frecuencia relativa de demanda puede ser modelada por
    
$$\begin{align*}p(y)=\begin{cases}y & 0\leq y\leq 1 \\1 & 1<y\leq 1.5 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

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
27. Unas partículas están suspendidas en un medio líquido con
    concentración de seis partículas por `$mL$`. Se agita por completo
    un volumen grande de la suspensión, y después se extrae `$3_{mL}$`.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que sólo se retiren \(15\) partículas?
    </li>
    <li>
    ¿Cuál es la probabilidad de que se retiren menos de \(8\) o más de
    \(18\) partículas?
    </li>
    <li>
    Cuál es el número promedio y desviación estándar de partículas que
    se retirarían, si se extrae un total de \(4_{mL}\)?.
    </li>
    </ol>
28. Suponga que se tiene cierto tipo de tablero de circuitos que
    contiene un total de `$250$` diodos. Si se sabe por experiencia que
    la probabilidad de que falle cualquier diodo es de `$0.002$`.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que fallen exactamente dos diodos?
    </li>
    <li>
    ¿Cuál es la probabilidad de que fallen más de \(45\) diodos?
    </li>
    <li>
    ¿Cuál es la media del número de diodos que falla?
    </li>
    <li>
    ¿Cuál es la desviación estándar del número de diodos que falla?
    </li>
    <li>
    Un tablero funciona si ninguno de sus diodos falla. ¿Cuál es la
    probabilidad de que funcione un tablero?
    </li>
    <li>
    Se envían cinco tableros a un cliente. ¿Cuál es la probabilidad de
    que cuatro o más de ellos funcione?
    </li>
    </ol>
29. Un fabricante de alimentos usa una máquina de moldeo por inyección
    (que produce galletas del tamaño de un bocado y botanas) que
    proporciona un ingreso para la empresa a razón de `$200$` por hora
    cuando está en operación. No obstante, la máquina se descompone a un
    promedio de dos veces por cada día que trabaja. Si `$Y$` denota el
    número de descomposturas por día, el ingreso diario generado por la
    máquina es `$R = 1600 – 50Y^2$`. Encuentre el ingreso diario
    esperado por usar la máquina.
30. El tiempo de vida `$X$`, en horas, de un artículo en el taller
    mecánico tiene una distribución de Weibull con parámetro de escala
    `$10$` y de forma `$2$`.
    <ol type="a">
    <li>
    Cuál es la probabilidad de que falle antes de \(8\) horas de uso?
    </li>
    <li>
    Cómo es el comportamiento de su función de falla?
    </li>
    </ol>
31. Suponga el tiempo, en minutos, que tarda un camión en cruzar debajo
    del puente de la madre Laura, posee una función de densidad de
    probabilidad dada por
    
$$\begin{align*}f(x)=\begin{cases}\frac{e^{-(x-1)}}{\sqrt{21\pi}} & x \geq 0\\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Verifique si es una función de densidad de probabilidad bien
    definida.
    </li>
    <li>
    Calcule la función de distribución acumulada de \(X\).
    </li>
    <li>
    Calcule el valor esperado y la varianza del tiempo que tarda un
    camión en cruzar debajo del puente de la madre Laura.
    </li>
    <li>
    Calcule la probabilidad de que tarde más de \(2\) minutos, hasta que
    cruce un camión.
    </li>
    </ol>
32. En una empresa de call center, se encontró que el `$38\%$` de los
    trabajadores son mujeres cabeza de familia. Si se elige
    aleatoriamente `$30$` trabajadores de la empresa,
    <ol type="a">
    <li>
    Cuál es la probabilidad de que al menos \(18\) pero menos de \(23\)
    de los trabajadores, no sean mujeres cabeza de familia.
    </li>
    <li>
    Calcule el punto anterior, mediante una aproximación Normal y
    comente sobre qué tan precisa es la aproximación, y por qué puede
    deberse tal comportamiento?.
    </li>
    <li>
    Calcule el punto anterior, mediante una aproximación Poisson y
    comente sobre qué tan precisa es la aproximación, y por qué puede
    deberse tal comportamiento.
    </li>
    </ol>
33. Suponga que el tiempo que tarda la revisión de una moto en un
    taller, se distribuye exponencialmente con una media de `$23$`
    minutos.
    <ol type="a">
    <li>
    Si el tiempo de revisión de la motocicleta ya ha superado la media
    hora, Cuál es la probabilidad de que la revisión tarde no más de un
    cuarto de hora adicional?.
    </li>
    <li>
    Cuál es el tiempo de revisión de una motocicleta, si se sabe éste ha
    superado el \(10\%\) de los tiempos de revisión.
    </li>
    <li>
    Suponga que el costo de revisión de una motocicleta está dado por,
    \(C = 250 + 15 X\). Calcule la varianza para el costo de revisión de
    las motocicletas.
    </li>
    </ol>
34. Un jugador de baloncesto del equipo de la Universidad, es el mejor
    de su equipo, tanto así que es capaz de encestar desde cualquier
    punto `$8$` de cada `$9$` tiros que realiza. Si durante un partido,
    el jugador lanza `$30$` veces y se sabe que ha encestado al menos
    `$12$` tiros, cuál es la probabilidad de que haya encestado
    exactamente `$27$` tiros.
35. Sea `$X$` una variable aleatoria que representa el número de
    perforaciones que debe realizar una perforadora de petroleo para
    encontrar un yacimiento, tal que, su función de masa de probabilidad
    está dada por
    
$$\begin{align*}p(x)=p(1-p)^x \quad \quad \text{para } x=0,1,2,\ldots\end{align*}$$

    Si la probabilidad `$p$` de encontrar un yacimiento en una
    perforación es del `$18\%$`, cuál es la probabilidad de que se
    necesiten realizar no más de `$5$` perforaciones hasta encontrar un
    yacimiento.
36. Suponga que el tiempo, en minutos, que tarda una llamada en entrar a
    un Call Center en una, es una variable aleatoria `$X$` con función
    de densidad de probabilidad dada por
    
$$\begin{align*}f(x)=\frac{1}{8} \quad \quad \text{para } 2\leq x\leq 10\end{align*}$$

    <ol type="a">
    <li>
    Cuál es la probabilidad de que el tiempo que tarda una llamada en
    entrar a un Call Center, se encuentre entre \(5\) y \(9\) minutos.
    </li>
    <li>
    Calcule el tiempo promedio y desviación estándar, del tiempo que
    tarda una llamada en entrar a un Call Center.
    </li>
    <li>
    Si el tiempo de espera ya superó el tiempo de espera promedio y no
    ha entrado ninguna llamada, cuál es la probabilidad de que entre una
    llamada en el siguiente minuto.
    </li>
    </ol>
37. El tiempo de vida útil, en años, de una computadora Hewlett-Packard,
    es una variable aleatoria con función de densidad dada por
    
$$\begin{align*}f(x)=\begin{cases}\frac{x}{9}e^{-x^2/18} & x > 0;\quad \theta > 0,\\0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la probabilidad de que la vida útil que tiene una
    computadora Hewlett-Packard se encuentre entre \(3.2\) y \(8.4\)
    años.
    </li>
    <li>
    Calcule la función de distribución acumulada, \(F(x)\).
    </li>
    <li>
    De una expresión para la tasa de fallas, \(h(t)\), y evalúe como es
    su comportamiento a medida que pasa el tiempo.
    </li>
    </ol>
38. El grupo ALIADO del Departamento de Ingeniería Industrial, realiza
    un estudio experimental sobre el tiempo que pasan los estudiantes en
    una computadora durante el día. En dicho estudio el grupo ALIADO
    revela que el tiempo que pasan los estudiante frente a la
    computadora, se distribuye normalmente con un promedio de `$4.8$`
    horas, y una desviación estándar de `$2.5$` horas. Si se selecciona
    un estudiante al azar
    <ol type="a">
    <li>
    Cuál es el tiempo, en horas, que pasa el \(82%\) superior de los
    estudiantes frente a la computadora?.
    </li>
    <li>
    Si se sabe que el estudiante pasa al menos \(3\) horas frente a la
    computadora, Cuál es la probabilidad de que pase más de \(5\) horas
    frente a ella?.
    </li>
    </ol>
39. Suponga que el número de vehículos que llegan a una esquina de un
    pueblo durante un periodo de `$5$` minutos, es una variable
    aleatoria discreta con función de masa de probabilidad dada por
    
$$\begin{align*}p(x)=\begin{cases}\frac{9x}{4^{x+1}} & x= 1, 2, 3, \ldots \\0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Construya una tabla para la función de masa de probabilidad
    \((x, p(x))\), para \(x = 1, 2, 3, 4, 5\) y \(6\) o más.
    </li>
    <li>
    Calcule la probabilidad de que el número de vehículos que llegan a
    la esquina no sea superior a \(4\) vehículos.
    </li>
    </ol>
40. Suponga que la distancia, en kilómetros, que recorre un atleta al
    día es una función de distribución de densidad de probabilidad dada
    por
    
$$\begin{align*}f(x)=\begin{cases}x^3 & 2\leq x < 4 \\ (x - 2)^2 & 4 \leq x < 8\\0 & \text{En otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Verifique si la función de densidad de probabilidad está bien
    definida, y de no estarlo, encuentre el valor de \(k\) para que
    \(f(x)\) sea una función de densidad de probabilidad bien definida.
    </li>
    <li>
    Calcule la función de distribución acumulada \(F(x)\), y utilice el
    resultado para calcular la probabilidad de que la distancia
    recorrida por un atleta se encuentre entre \(3.3\) y \(5.6\)
    kilómetros.
    </li>
    <li>
    Calcule el número promedio y desviación estándar de kilómetros que
    recorre un atleta en un día.
    </li>
    </ol>