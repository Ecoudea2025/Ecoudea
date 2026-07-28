---
title: "Práctica 05"
course: "estadistica-i"
order: 26
classType: "practica"
description: "Ejercicios sobre: - Distribución Uniforme Continua - Distribución Gamma - Distribución Exponencial - Distribución Normal - Teoremas de Aproximación - Momentos - Función generadora de momentos"
math: true
bibliography: "../../referencias.bib"
---

## Lista de ejercicios

1.  Suponga que por Ley, la vida máxima de la patente para un nuevo
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
    Calcule el primer momento alrededor del origen.
    </li>
    <li>
    Calcule el segundo momento alrededor del origen.
    </li>
    <li>
    Calcule el segundo momento central.
    </li>
    </ol>
2.  La cantidad diaria de café, en litros, que sirve la maquina de las
    burbujas, es una variable aleatoria uniforme en el intervalo de
    `$6.8$` hasta `$10$` litros.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, la maquina
    sirva más de \(8\) litros?
    </li>
    <li>
    ¿Cuál es la probabilidad de que en un día cualquiera, la maquina
    sirva más de \(8.8\) litros, si en lo que va del día ya ha servido
    \(7.8\)?
    </li>
    </ol>
3.  Suponga que a partir de gran cantidad de datos históricos se sabe
    que `$X$`, el número de automóviles que llegan a una intersección
    específica durante un periodo de `$20$` segundos, se determina
    mediante la siguiente función de probabilidad discreta
    
$$\begin{align*}p(x)=\frac{e^{-\lambda} \lambda^x}{x!} \text{  para  } x=0,1,2,\dots\end{align*}$$

    <ol type="a">
    <li>
    Encuentre su función generadora de momentos de la variable aleatoria
    \(X\).
    </li>
    <li>
    Encuentre la media, varianza, asimetría y exceso de curtosis de la
    variable aleatoria \(X\) mediante la función generadora de momentos.
    </li>
    </ol>
4.  Suponga que el número de llamadas telefónicas que entran a un
    conmutador particular siguen un proceso de Poisson con un promedio
    de `$5$` llamadas entrantes por minuto.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que transcurra hasta un minuto en el
    momento en que ha entrado \(1\) llamada al conmutador?
    </li>
    <li>
    ¿Cuál es la probabilidad de que transcurra hasta un minuto en el
    momento en que han entrado \(3\) llamadas al conmutador?
    </li>
    </ol>
5.  Sea `$X$` una variable aleatoria con función de masa de probabilidad
    geométrica dada por
    
$$\begin{align*}p(x)=p(1-p)^{x-1} \text{  para  }  x=1,2,3,\ldots\end{align*}$$

    <ol type="a">
    <li>
    Encuentre su función generadora de momentos de la variable aleatoria
    \(X\).
    </li>
    <li>
    Encuentre la media, varianza, asimetría y exceso de curtosis de la
    variable aleatoria \(X\) mediante la función generadora de momentos.
    </li>
    </ol>
6.  Considere a `$X$` la variable aleatoria que representa la suma de
    las caras para el lanzamiento de dos dados, con función de masa de
    probabilidad dada por
    
$$\begin{align*}p(x)=\frac{6-|7-x|}{36} \text{  para  } x = 2,3,\ldots,12\end{align*}$$

    Calcule el segundo momento central.
7.  El tiempo entre arribos de taxis al acopio de una estación del metro
    tiene una media de `$60$` segundos.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que la llegada del próximo taxi tarde al
    menos \(40\) segundos?.
    </li>
    <li>
    ¿Cuál es la probabilidad de que la llegada del próximo taxi tarde al
    menos \(40\) segundos, si ya han pasado \(20\) segundos y aún no
    llega ningún taxi al acopio del metro?
    </li>
    <li>
    ¿Cuál es la probabilidad de que lleguen al acopio más de \(10\) pero
    no menos de \(15\) taxis en un intervalo de \(20\) minutos.
    </li>
    </ol>
8.  Demuestre que el `$r$`-ésimo momento alrededor del origen de la
    distribución gamma es
    
$$\begin{align*}\mu'_r=\mathbb{E}(X^r)=\frac{\beta^r\Gamma(\alpha + r)}{\Gamma(\alpha)}\end{align*}$$

    y calcule la media, varianza, asimetría y exceso de curtosis de la
    distribución Gamma.
9.  Luego de varios semestres, un profesor de estadística encuentra que
    los resultados que obtienen los estudiantes en el examen final de
    estadística, tienen una distribución normal con media `$3.2$` y
    varianza `$0.1225$`. Si un estudiante necesita al menos un `$4$`
    para que la nota acumulada le quede sobre `$2.96$`, cuál es la
    probabilidad de que luego de presentar el parcial gane la materia?
10. Suponga una variable aleatoria `$X$` la cual posee una función de
    masa de probabilidad uniforme discreta, de la forma
    
$$\begin{align*}p(x) = \frac{1}{k} \text{  para  } x = 1,2, \ldots, k\end{align*}$$

    Encuentre su función generadora de momentos de la variable aleatoria
    `$X$`.
11. El sistema de puntuación Elo es un método matemático empleado para
    calcular la habilidad relativa de los jugadores en algunos deportes
    tales como el Ajedrez. Suponga que el puntaje Elo promedio de los
    jugadores de cierta categoría es de `$1556$` con una desviación
    estándar de `$14$`. Si pruebas estadísticas han sugerido que el
    rendimiento de los ajedrecistas se distribuye normalmente. ¿Cuál es
    la probabilidad de que un ajedrecista de dicha categoría tenga un
    puntaje Elo superior a `$1603$`?.
12. La función generadora de momentos de cierta variable aleatoria de
    Poisson `$X$` es dada por
    
$$\begin{align*}M_x(t) = e^{4(e^t-1)}\end{align*}$$
 Calcule de
    forma exacta y mediante aproximación a una distribución normal la
    `$\mathbb{P}(\mu - 1.3\sigma<X< \mu + 2.3\sigma)$`.
13. Suponga que en una universidad se realizan pruebas de aptitud
    anuales para observar las habilidades y competencias de sus
    profesores. Si se sabe que el puntaje de estas pruebas se distribuye
    gamma con un promedio de de `$76.2$` y una varianza de `$1935.48$`.
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que un profesor obtenga un puntaje
    superior a \(79\) puntos?.
    </li>
    <li>
    Si el profesor sabe que tendrá una puntuación superior a \(66\)
    puntos, cuál es la probabilidad de que éste obtenga una puntuación
    menor a \(80\) puntos?
    </li>
    </ol>
14. Sea `$X$` una variable aleatoria con función de densidad de
    probabilidad chi-cuadrado dada por
    
$$\begin{align*}f(x) = \frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\frac{\nu}{2}-1}e^{-\frac{x}{2}} \text{  para  } x>0\end{align*}$$

    <ol type="a">
    <li>
    Encuentre su función generadora de momentos de la variable aleatoria
    \(X\).
    </li>
    <li>
    Encuentre la media y la varianza de la variable aleatoria \(X\)
    mediante la función generadora de momentos.
    </li>
    </ol>
15. Por experiencia se sabe que el `$20\%$` de las inversiones
    realizadas por un experto en finanzas terminan en pérdida. Si se
    seleccionan aleatoriamente `$60$` inversiones realizadas por el
    experto, ¿Cuál es la probabilidad de que más de `$37$` pero menos de
    `$45$`, no terminen en pérdida? Compare el resultado obtenido
    mediante una aproximación Normal.
16. Sea `$X$` una variable aleatoria con función de masa de probabilidad
    binomial dada por
    
$$\begin{align*}f(x) = \left(\begin{array}{c}n\\ x\end{array}\right) p^x(1-p)^{n-x} \text{  para  } x=0,1,2,\ldots,n\end{align*}$$

    <ol type="a">
    <li>
    Encuentre su función generadora de momentos de la variable aleatoria
    \(X\).
    </li>
    <li>
    Encuentre la media, varianza, asimetría y curtosis de la variable
    aleatoria \(X\) mediante la función generadora de momentos.
    </li>
    </ol>
17. Suponga que se realiza un estudio estadístico y se encuentra que el
    número de clientes que llega donde Pastora en media hora, es una
    variable aleatoria Poisson con media de `$4$` clientes. Basados en
    lo anterior
    <ol type="a">
    <li>
    ¿Cuál es la probabilidad de que el próximo cliente en llegar donde
    Pastora tarde al menos \(20\) minutos?
    </li>
    <li>
    ¿Cuál es la probabilidad de que lleguen donde Pastora en menos de
    \(50\) minutos, \(3\) clientes, si se sabe que han transcurrido
    \(24\) minutos y aún no llegan los \(3\) clientes?
    </li>
    </ol>
18. Suponga una variable aleatoria `$X$` con función de distribución de
    probabilidad exponencial dada por
    
$$\begin{align*}f(x) = \lambda e^{-\lambda x} \text{  para  } x>0, \lambda>0\end{align*}$$

    Basado en lo anterior, calcule el segundo momento central de la
    variable aleatoria.
19. Suponga que el tiempo de vida de un portátil MSI, en años, tiene una
    distribución de Gamma con parámetro de forma y de escala dados por
    `$3$` y `$1.5$` respectivamente. Calcule la probabilidad de que
    falle antes de `$6$` años de uso.