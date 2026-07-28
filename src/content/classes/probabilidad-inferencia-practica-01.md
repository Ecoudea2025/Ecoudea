---
title: "Práctica 05"
course: "probabilidad-inferencia"
order: 27
classType: "practica"
description: "Ejercicio sobre: - Errores tipo I y tipo II - Pruebas de hipótesis - Pruebas de bondad de ajuste"
math: true
bibliography: "../../referencias.bib"
---

## Lista de ejercicios

1.  Se realiza un estudio para determinar si los habitantes de dos islas
    ubicadas en el Pacífico poseen o no la misma ascendencia racial, y
    para ello un antropólogo decide emplear los índices cefálicos de
    `$12$` hombres adultos de la isla `$A$` y `$18$` de la isla `$B$`
    obteniendo los sigiuentes resultados
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td colspan="10" style="text-align:center;font-weight: bold">
    Isla A
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    78.96
    </td>
    <td>
    79.30
    </td>
    <td>
    78.79
    </td>
    <td>
    75.59
    </td>
    <td>
    74.52
    </td>
    <td>
    75.97
    </td>
    <td>
    74.69
    </td>
    <td>
    73.31
    </td>
    <td>
    76.78
    </td>
    <td>
    80.86
    </td>
    </tr>
    <tr>
    <td>
    81.09
    </td>
    <td>
    76.94
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    </tr>
    </tbody>
    </table>
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td colspan="10" style="text-align:center;font-weight: bold">
    Isla B
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    72.27
    </td>
    <td>
    71.40
    </td>
    <td>
    74.25
    </td>
    <td>
    73.55
    </td>
    <td>
    73.87
    </td>
    <td>
    71.17
    </td>
    <td>
    73.38
    </td>
    <td>
    72.39
    </td>
    <td>
    72.09
    </td>
    <td>
    73.81
    </td>
    </tr>
    <tr>
    <td>
    68.23
    </td>
    <td>
    71.57
    </td>
    <td>
    72.89
    </td>
    <td>
    74.89
    </td>
    <td>
    73.46
    </td>
    <td>
    76.79
    </td>
    <td>
    70.98
    </td>
    <td>
    69.58
    </td>
    <td>
    </td>
    <td>
    </td>
    </tr>
    </tbody>
    </table>
    Mediante el empleo de un nivel de significancia del `$8\%$` pruebe
    si es razonable suponer que las dos poblaciones poseen en promedio
    índices cefálicos similares.
2.  Se realiza un estudio en un río para observar la concentración de
    zinc que éste posee, y para ello se realiza una muestra aleatoria de
    `$36$` sitios diferentes y se encuentra que la concentración
    promedio de zinc es de `$2.8$` gramos por mililitro con una
    desviación estándar de `$0.6$` gramos por mililitro. Si la función
    de probabilidad no es conocida, pero se sabe su desviación estándar
    es de `$0.3$` gramos por mililitro, pruebe con un nivel de confianza
    del `$5\%$` si la concentración media de zinc es de al menos `$3$`
    gramos por mililitro.
3.  Un botánico desea probar la hipótesis de que el diámetro promedio de
    las flores de una planta en particular es `$9.6_{cm}$`, y para
    probar ésto, decide tomar una muestra aleatoria de `$80$` flores y
    no rechazar la hipótesis si la media de la muestra cae entre
    `$9.3_{cm}$` y `$9.9_{cm}$`; si la media de esta muestra cae fuera
    de este intervalo, el botánico rechazará tal hipótesis. ¿Qué
    decisión deberá tomará el botánico y qué situación estará ocurriendo
    si
    <ol type="a">
    <li>
    obtiene una media muestral de \(10.2_{cm}\) y la verdadera media
    \(\mu=9.6_{cm}\)
    </li>
    <li>
    obtiene una media muestral de \(10.2_{cm}\) y la verdadera media
    \(\mu=9.8cm\)
    </li>
    <li>
    obtiene una media muestral de \(9.4_{cm}\) y la verdadera media
    \(\mu=9.6cm\)
    </li>
    <li>
    obtiene una media muestral de \(9.4_{cm}\) y la verdadera media
    \(\mu=9.8cm\)
    </li>
    <li>
    Si la desviación estándar es igual a \(2_{cm}\), calcule la
    probabilidad de cometer Error Tipo I.
    </li>
    <li>
    Si la desviación estándar es igual a \(2_{cm}\), Calcule la
    probabilidad de cometer Error Tipo II, si la verdadera media
    \(\mu=9.8cm\).
    </li>
    </ol>
4.  Suponga que el contenido de ácido sulfúrico, en litros, de una
    muestra aleatoria de `$7$` contenedores similares es de
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td>
    9.8
    </td>
    <td>
    10.2
    </td>
    <td>
    10.4
    </td>
    <td>
    9.8
    </td>
    <td>
    10.0
    </td>
    <td>
    10.2
    </td>
    <td>
    9.6
    </td>
    </tr>
    </thead>
    </table>
    Emplee el P-valor para verificar si hay evidencia sobre que el
    contenido promedio de todos los contenedores de ácido sulfúrico es
    de más de `$10$` litros.
5.  Para un experimento de pruebas psicológicas se seleccionan al azar
    `$25$` sujetos de prueba y se les mide sus tiempos de reacción, en
    segundos, ante un estímulo particular, obteniendo que el tiempo
    promedio de reacción de los sujetos es de `$6.2$` segundos con una
    desviación estándar de `$1.3$` segundos. La experiencia sugiere que
    la varianza en los tiempos de reacción ante los diferentes tipos de
    estímulos es de `$4_{s^2}$` y que la distribución de probabilidad
    para los tiempos de reacción es aproximadamente normal. Basado en lo
    anterior, emplee un nivel de significancia del `$98\%$` para probar
    si el tiempo medio de reacción de todos los individuos es como
    máximo de `$5.5$` segundos.
6.  El gerente de una gran tabacalera afirma en una conferencia de
    prensa que el contenido promedio de alquitrán de los cigarrillos que
    produce es de `$14$` mg/cigarrillo. Un ingeniero realiza `$5$`
    mediciones del contenido de alquitrán de cierta clase de cigarrillos
    para observar si la afirmación del gerente sobre el contenido de
    alquitrán es cierta, y obtiene en la muestra los siguientes
    resultados
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td>
    14.5
    </td>
    <td>
    14.2
    </td>
    <td>
    14.4
    </td>
    <td>
    14.3
    </td>
    <td>
    14.6
    </td>
    </tr>
    </tbody>
    </table>
    ¿Encuentra apoyo la afirmación del gerente de la tabacalera?, emplee
    un nivel de significancia del `$5\%$` para su conclusión.
7.  Suponga que el grupo ALIADO, realiza un estudio sobre la altura que
    poseen los estudiantes de la Universidad, y para ello, toma una
    muestra aleatoria de `$38$` estudiantes universitarios y encuentra
    que la estatura promedio fue de `$174.5$` centímetros con una
    desviación estándar de `$6.9$` centímetros. Empleando un nivel de
    significancia del `$2\%$`, pruebe si la altura promedio de todos los
    estudiantes de la universidad es de al menos `$173$` centímetros.
8.  El gerente de una planta sospecha que el número promedio de piezas
    que produce un trabajador en particular por día, es menor que el
    número promedio de piezas de los demás trabajadores. Por ello, el
    gerente decide observar el número de piezas que produce este
    trabajador durante diez días, seleccionados al azar, obteniendo los
    siguientes resultados
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td>
    15
    </td>
    <td>
    12
    </td>
    <td>
    28
    </td>
    <td>
    13
    </td>
    <td>
    12
    </td>
    <td>
    15
    </td>
    <td>
    16
    </td>
    <td>
    9
    </td>
    <td>
    8
    </td>
    <td>
    14
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Si se sabe que la desviación estándar para todos los trabajadores es
    de \(2\) unidades, emplee un nivel de significancia del \(2\%\) para
    probar si tiene o no apoyo la sospecha del gerente de que el número
    promedio de unidades producidas por el trabajador es menor a \(15\)
    unidades? Obtener el P-valor para el contraste.
    </li>
    <li>
    Emplee un nivel de significancia del \(5\%\) para probar si la
    proporción de días que el trabajador produce menos de \(15\)
    unidades es mayor al \(80\%\).
    </li>
    </ol>
9.  ¿Está menguando el romance de los estadounidenses con el cine?, En
    una encuesta realizada por la empresa Gallup a `$800$` adultos
    seleccionados de forma aleatoria, se encontró que `$45\%$` de los
    encuestados indicaron que el cine estaba mejorando, mientras que,
    `$43\%$` de los encuestados dijeron que el cine estaba empeorando.
    Basados en lo anterior, emplee un nivel de significancia del
    `$12\%$` para probar si la proporción total de adultos que piensan
    que el cine está mejorando es superior al `$50\%$`.
10. Un estudio del número de comidas de negocios que los ejecutivos de
    las industrias de seguros y bancos reclaman mensualmente como gastos
    deducibles, se basó en muestras aleatorias y produjo los siguientes
    resultados
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td>
    </td>
    <td style="font-weight: bold">
    Seguros
    </td>
    <td style="font-weight: bold">
    Bancos
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="font-weight: bold">
    Muestra
    </td>
    <td>
    40
    </td>
    <td>
    50
    </td>
    </tr>
    <tr>
    <td style="font-weight: bold">
    Media muestral
    </td>
    <td>
    9.1
    </td>
    <td>
    8.0
    </td>
    </tr>
    <tr>
    <td style="font-weight: bold">
    Desviación estándar muestral
    </td>
    <td>
    1.9
    </td>
    <td>
    2.1
    </td>
    </tr>
    </tbody>
    </table>
    Use un nivel del `$5\%$` de significancia para probar si el gasto
    promedio deducible de ambas poblaciones es igual. Encuentre el
    P-valor para esta prueba.
11. A la mayoría de estadounidenses les gusta participar en eventos
    deportivos o al menos verlos. Algunos sienten que los deportes
    tienen más que sólo valor de entretenimiento, tanto así, que en una
    encuesta realizada a `$1000$` adultos, realizada por KRC Research &
    Consulting, se encontró que `$68\%$` sintieron que los deportes de
    gran atractivo tienen un efecto positivo en la sociedad. Emplee un
    nivel de significancia del `$5\%$` para probar si la mayoría de
    estadounidenses piensan que los deportes tienen un efecto positivo
    en la sociedad.
12. Para una comparación de los porcentajes de piezas defectuosas
    producidas por dos líneas de montaje, de cada línea se seleccionaron
    muestras aleatorias independientes de `$100$` piezas. La línea `$A$`
    produjo `$18$` piezas defectuosas en la muestra y la línea `$B$`
    contenía `$12$` piezas defectuosas. Emplee un nivel de significancia
    del `$2\%$` para probar si una línea de montaje produce una
    proporción más alta de piezas defectuosas que la otra.
13. Se tiene la creencia que las profesoras de la Universidad suelen
    gastar en promedio más dinero en café que los profesores en un mes.
    Para probar ésto, se realiza un estudio en el cual se toma una
    muestra aleatoria de profesoras y profesores y se registra el gasto
    que tuvieron durante el mes, obteniendo los siguientes resultados,
    en miles de pesos
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td>
    </td>
    <td style="font-weight: bold">
    Profesores
    </td>
    <td style="font-weight: bold">
    Profesoras
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="font-weight: bold">
    Muestra
    </td>
    <td>
    20
    </td>
    <td>
    28
    </td>
    </tr>
    <tr>
    <td style="font-weight: bold">
    Media muestral
    </td>
    <td>
    33
    </td>
    <td>
    38.5
    </td>
    </tr>
    <tr>
    <td style="font-weight: bold">
    Desviación estándar muestral
    </td>
    <td>
    2.9
    </td>
    <td>
    3.1
    </td>
    </tr>
    </tbody>
    </table>
    Use un nivel del `$5\%$` de significancia para probar la hipótesis
    planteada. Emplee el P-valor en sus conclusión.
14. Suponga que nos encontramos en época de elecciones, y que el
    responsable de la campaña política del candidato `$A$` piensa en el
    ambiente de las últimas semanas previas a las elecciones. Él piensa
    que su candidato se encuentra en igual posición que su oponente, el
    candidato `$B$`, pero han ocurrido algunos reveses en forma
    reciente. El responsable lleva a cabo una encuesta de percepción
    electoral a `$1500$` ciudadanos. Si de los `$1500$`, `$737$` indican
    una preferencia por el candidato `$A$`, ¿existe alguna razón para
    creer que el candidato `$A$` se encuentra en desventaja con relación
    al candidato `$B$`?, Use un nivel de significancia del `$5\%$`.
15. Una bióloga quiere probar la hipótesis de que la envergadura media
    de cierta clase de insectos es `$12.3_{mm}$` contra la alternativa
    de que no es de `$12.3_{mm}$`. Suponga que la envergadura de los
    insectos puede asumirse normal con una desviación estándar conocida
    e igual a `$0.8_{mm}$`. Si se toma una muestra aleatoria de `$12$`
    insectos y se decide aceptar la hipótesis nula si y sólo si la media
    de la muestral cae entre `$12.0_{mm}$` y `$12.6_{mm}$`,
    <ol type="a">
    <li>
    Calcule la probabilidad de cometer un error tipo I.
    </li>
    <li>
    Calcule la probabilidad de cometer un error tipo II, si la media
    real de la envergadura de los insectos es de \(12.5_{mm}\)
    </li>
    <li>
    ¿Qué decisión estaría tomando la bióloga si obtiene de la muestra un
    media de \(12.9_{mm}\), y se tiene que la media real de la
    envergadura de los insectos es \(12.5mm\)?
    </li>
    <li>
    ¿Qué decisión estaría tomando la bióloga si obtiene de la muestra un
    media de \(12.9_{mm}\), y se tiene que la media real de la
    envergadura de los insectos es \(12.3_{mm}\)?
    </li>
    </ol>
16. Las calificaciones del Examen de Evaluación Escolar (SAT por sus
    siglas en inglés), que han bajado lentamente desde el inicio del
    examen, ahora han empezado a subir. Originalmente, una calificación
    de `$500$` estaba considerada como promedio. Las calificaciones
    medias para el `$2005$` fueron aproximadamente `$520$` para el
    examen verbal y `$508$` para el examen de matemáticas. Una muestra
    aleatoria de las calificaciones del examen, de `$20$` alumnos de
    último año de una preparatoria urbana de gran tamaño, produjo las
    medias y desviaciones estándar citadas en la tabla siguiente
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td>
    </td>
    <td style="font-weight: bold">
    Verbal
    </td>
    <td style="font-weight: bold">
    Matemáticas
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="font-weight: bold">
    Media muestral
    </td>
    <td>
    505
    </td>
    <td>
    495
    </td>
    </tr>
    <tr>
    <td style="font-weight: bold">
    Desviación estándar muestral
    </td>
    <td>
    57
    </td>
    <td>
    69
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Suponiendo normalidad, emplee un nivel de significancia del \(10\%\)
    para observar si la calificación promedio del SAT verbal obtenida
    por los alumnos de último año es superior a \(520\) puntos.
    </li>
    <li>
    Suponiendo normalidad, emplee un nivel de significancia del \(10\%\)
    para observar si la calificación promedio del SAT de matemáticas
    obtenida por los alumnos de último año es a lo más de \(508\)
    puntos.
    </li>
    <li>
    Suponiendo normalidad, emplee un nivel de significancia del \(10\%\)
    para observar si la variabilidad en la calificación obtenida por los
    estudiantes en el SAT verbal y el SAT de matemáticas es la misma.
    </li>
    </ol>
17. Se está considerando un nuevo sistema de lanzamiento de cohetes para
    el despliegue de cohetes pequeños, de corto alcance. Suponga que por
    experiencia, se sabe que la probabilidad de que el sistema existente
    tenga un lanzamiento exitoso es del `$80\%$`. Si se toma una muestra
    de `$40$` lanzamientos experimentales con el nuevo sistema y `$34$`
    resultan exitosos. Emplee un nivel de significancia del `$8\%$` para
    probar si el nuevo sistema es mejor que el sistema actual.
18. Es frecuente que los químicos orgánicos purifiquen compuestos
    orgánicos por medio de un método conocido como cristalización
    fraccional. Un experimentador desea preparar y purificar `$4.85$`
    gramos de anilina. Diez especímenes de `$4.85$` gramos de anilina se
    prepararon y purificaron para producir acetanilida. Se obtuvieron
    los siguientes resultados en seco:
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td>
    3.85
    </td>
    <td>
    3.88
    </td>
    <td>
    3.90
    </td>
    <td>
    3.62
    </td>
    <td>
    3.72
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    3.80
    </td>
    <td>
    3.85
    </td>
    <td>
    3.36
    </td>
    <td>
    4.01
    </td>
    <td>
    3.82
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Emplee un nivel de significancia del \(2\%\) para probar si la
    cantidad promedio de gramos de acetanilida que se puede recuperar de
    \(4.85\) gramos de anilina es superior a \(3.85\) gramos.
    </li>
    <li>
    Emplee un nivel de significancia del \(10\%\) para probar si al
    emplear \(4.85\) gramos de anilina, la proporción de experimentos
    que recuperan una cantidad de acetanilida superior a \(3.85\) gramos
    es superior al \(20\%\).
    </li>
    </ol>
19. Para comparar dos clases de protectores de defensas, se muestrearon
    `$6$` de cada clase en cierta marca de auto compacto. Entonces cada
    auto se hizo chocar contra una pared de concreto a `$5$` millas por
    hora, y los siguientes son los costos de las reparaciones (en
    dólares):
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td colspan="6" style="text-align:center;font-weight: bold">
    Protector de defensas 1
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    120
    </td>
    <td>
    127
    </td>
    <td>
    168
    </td>
    <td>
    143
    </td>
    <td>
    165
    </td>
    <td>
    122
    </td>
    </tr>
    </tbody>
    </table>
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <thead>
    <tr>
    <td colspan="6" style="text-align:center;font-weight: bold">
    Protector de defensas 2
    </td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    154
    </td>
    <td>
    135
    </td>
    <td>
    132
    </td>
    <td>
    171
    </td>
    <td>
    153
    </td>
    <td>
    149
    </td>
    </tr>
    </tbody>
    </table>
    Use el nivel `$10\%$` de significancia para probar si la diferencia
    entre las medias de estas dos muestras es significativa.
20. El propietario de una automóvil compacto sospecha que la distancia
    promedio por galón que ofrece su carro es menor que la especificada
    por la EPA, la cual es de `$30$` millas por galón. El propietario
    observa la distancia recorrida por galón en `$9$` ocasiones y
    obtiene los siguientes datos:
    <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr>
    <td>
    28.3
    </td>
    <td>
    31.2
    </td>
    <td>
    29.4
    </td>
    <td>
    27.2
    </td>
    <td>
    30.8
    </td>
    </tr>
    <tr>
    <td>
    28.7
    </td>
    <td>
    29.2
    </td>
    <td>
    26.5
    </td>
    <td>
    28.1
    </td>
    <td>
    </td>
    </tr>
    </tbody>
    </table>
    Después de una investigación el propietario concluye que la
    distancia por galón es una variable aleatoria que se distribuye
    normal con una desviación estándar conocida de `$1.4$` millas por
    galón. Con base en esta información,
    <ol type="a">
    <li>
    ¿Se encuentra apoyada la sospecha del propietario con un nivel de
    significancia del \(1\%\)? ¿Cuál es el P-valor en este caso?
    </li>
    <li>
    ¿Está de acuerdo con la afirmación de normalidad realizada por el
    propietario?
    </li>
    </ol>

<!--        \item  Una organización de salud se interesa en actualizar su información con respecto a la proporción de hombres que fuman. Con base en estudios previos, se cree que la proporción es de 40\%. La organización lleva a cabo una encuesta en la que se selecciona en forma aleatoria 1200 hombres a los cuales se les pregunta sus hábitos de fumador. De los 1200, 420 son fumadores. Con un nivel de significancia del $1\%$ -->
<!--        \begin{enumerate} -->
<!--            \item ¿Será que la evidencia anterior apoya la noción de que la proporción de hombres que fuman es diferente a 40\%? ¿Cuál es el $p$-valor de la prueba? -->
<!--            \item Si la verdadera proporción es de 30\% cual es la probabilidad de cometer un error tipo II? -->
<!--        \end{enumerate} -->
<!--        \item Un fabricante de detergente afirma que el contenido de los paquetes que vende pesa, por término medio, al menos $200gr$. Se sabe que la distribución de los pesos es normal, con desviación típica $4gr$. Una muestra aleatoria de 16 paquetes da un peso medio muestral de $198.4gr$. Contrastar, al nivel de significación del $7\%$, la hipótesis del fabricante. -->
<!--        \item Después de la creación de la Pension Benefit Guarantee Corporation en Estados Unidos, se examinaron los cambios porcentuales en las pensiones prometidas de 76 planes de pensiones elegidos aleatoriamente. El cambio medio porcentual en la muestra fue 0.078 y la desviación típica 0.201. Pruebe si hubo cambio porcentual en las pensiones prometidas con la creación de la Pension Benefit Guarantee Corporation. Hallar e interpretar el $p$-valor del contraste de hipótesis. -->
<!--        \item Una máquina produce láminas de plástico que periódicamente son examinadas para detectar posibles fluctuaciones en su grosor. Si la verdadera varianza del grosor supera los 2.25 milímetros cuadrados, se despierta inquietud por la calidad del producto. Los grosores medidos para una muestra aleatoria de 10 láminas producidas fueron los siguientes (en milímetros): $226$, $226$, $232$, $227$, $225$, $228$, $225$, $228$, $229$, $230$. Use un nivel de significancia del $5\%$ para contrastar dicha hipótesis. -->
<!--        \item En las negociaciones para un contrato, una compañía afirma que un nuevo sistema de incentivos ha producido en promedio, unos ingresos mensuales de 160000  pesetas para todos los trabajadores. Un representante sindical toma una muestra aleatoria de 15 trabajadores y comprueba que sus ingresos mensuales tienen una media de 152540 pesetas con una desviación típica de 19440 pesetas. Suponga que esta muestra se distribuye normal. -->
<!--        \begin{enumerate} -->
<!--            \item Pruebe con un nivel de significancia del $5\%$ si se encuentra apoyada la afirmación de la compañía. -->
<!--            \item Si se hubieran obtenido con una muestra aleatoria de 78 empleados los mismos resultados y con un nivel de significancia del $1\%$, ¿estaría apoyada la afirmación de la compañía? -->
<!--        \end{enumerate} -->
<!--        \item Una academia ofrece cursos de preparación a los estudiantes para superar exámenes de estadística II. Como parte de un experimento para evaluar la eficiencia del curso, se eligen doce estudiantes y se dividen en seis parejas, de manera que los dos miembros de cada pareja tengan similares expedientes académicos. Antes de realizar el examen, se elige aleatoriamente un miembro de cada pareja para asistir al curso de preparación, mientras que el otro miembro no toma el curso. La tabla adjunta muestra las puntuaciones conseguidas en el examen. Asumiendo que las diferencias en las puntuaciones siguen una distribución normal, contrastar al nivel del $5\%$, si la asistencia al curso mejora en promedio la preparación de los estudiantes para los exámenes de estadística II. -->
<!--        \begin{table}[H] -->
<!--            \centering -->
<!--            \begin{tabular}{ccc} -->
<!--                \hline -->
<!--                \textbf{\begin{tabular}[c]{@{}c@{}}Pareja de\\ estudiantes\end{tabular}} & \textbf{Asistente} & \textbf{No Asistente} \\ \hline -->
<!--                1 & 82 & 75 \\ -->
<!--                2 & 73 & 71 \\ -->
<!--                3 & 59 & 52 \\ -->
<!--                4 & 48 & 46 \\ -->
<!--                5 & 69 & 70 \\ -->
<!--                6 & 93 & 83 \\ \hline -->
<!--            \end{tabular} -->
<!--        \end{table} -->
<!--        \item Los auditores se dedican principalmente a la detección de posibles fraudes. Se conjetura que, como ayuda para evaluar las posibilidades de fraude, los auditores pueden utilizar un “cuestionario indicador”, es decir, una lista de síntomas potenciales de fraude que deben ser valorados. Para confirmar esta conjetura se seleccionaron aleatoriamente varios auditores y se les presentó información de auditorías en las que se detectó fraude. Se pidió a los auditores que evaluasen la posibilidad de fraude en una escala de 0 a 100. Treinta tres auditores elegidos aleatoriamente usaron el cuestionario indicador. Su valoración media fue de 36.21 con una desviación típica de 22.93. Otros 36 auditores elegidos aleatoriamente, y de forma independiente a los anteriores, no usaron el cuestionario y la media muestral y la desviación típica de sus valoraciones fueron respectivamente 40.56 y 23.52. Asumiendo que las dos poblaciones tienen distribución normal. Con un nivel de significancia del $8\%$ ¿Se puede pensar que la valoración promedio de los auditores es igual? -->
<!--        \item De acuerdo a las normas establecidas para una prueba de compresión de lectura, estudiantes del último año de primaria deben promediar más de 84.3 con una desviación estándar de 8.6. Si 45 estudiantes de último año de primaria seleccionados aleatoriamente de cierto distrito escolar promediaron 83.8. Use un nivel de significancia del $6\%$ y encuentre el $p$-valor para esta prueba para probar si se están cumpliendo o no las normas establecidas de comprensión lectora. -->
<!--        \item Se interrogó a una muestra aleatoria de 50 gerentes de pequeñas compañías sobre sus expectativas en las entrevistas de trabajo. De ellos, 28 estuvieron de acuerdo en que el entrevistador normalmente, espera que el entrevistado haya estudiado de antemano al máximo sobre la compañía. Contrastar la hipótesis de que al menos la mitad de los entrevistadores tienen estas expectativas. Use un nivel de significancia del $3\%$ -->
<!--        \item por experiencia se sabe que el tiempo que se requiere para que los estudiantes de preparatoria de último año contesten una prueba estandarizada es una variable aleatoria normal con una media de 30 minutos y una desviación estándar de 6 minutos. De una m.a de los tiempos para realizar la prueba de 20 estudiantes de preparatoria de último año tienen una media de 34 minutos y una desviación estándar de 4.51 minutos. Estaría de acuerdo con que la desviación es de menos de 6 minutos? Use un nivel de significancia del $5\%$ -->
<!--        \item Un economista al servicio del estado desea determinar si la frecuencia de desempleo en dos áreas urbanas del estado son diferentes. Con base en m.a de tamaño 500 de cada ciudad, el economista encuentra en una ciudad 35 personas desempleadas, y en la otra 25 en la otra. Bajo la suposiciones apropiadas y con un nivel de significancia del $5\%$. ¿Existe alguna razón para creer que la frecuencia de desempleo en las dos áreas son diferentes? ¿Cuál es el $p$-valor? -->
<!-- 17. Dos nuevos medicamentos se dieron a pacientes con hipertensión. El primero de ellos bajó la presión sanguínea de `$16$` pacientes en un promedio de `$11$` puntos, con una desviación estándar de `$6$` puntos; el segundo bajó la presión de otros `$20$` pacientes en un promedio de `$12$` puntos, con desviación estándar de `$8$` puntos. Basado en la información anterior -->
<!-- <ol type ="a"> -->
<!--   <li> Determine un intervalo de confianza de $95\%$ para la diferencia de las reducciones medias en presión sanguínea, suponiendo que las mediciones están distribuidas normalmente. -->
<!--   </li> -->
<!--   <li>Calcule la probabilidad de la diferencia de las reducciones medias en la presión sanguínea con el medicamento $A$ sea menor que la reducción media que ofrece el medicamento $B$, suponiendo que las mediciones están distribuidas normalmente. -->
<!--   </li> -->
<!-- </ol> -->
<!-- 18. ¿El precio pagado por el atún depende del método de empaque? *Consumer Reports* da el precio promedio estimado para una lata de `$6$` onzas o una bolsa de `$7.06$` onzas de atún, con base en precios pagados a nivel nacional en supermercados. Los precios se registran para una variedad de marcas de atún en la tabla siguiente: -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <tbody><tr> -->
<!-- <td rowspan="1" colspan="2" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold;">Atún Claro  -->
<!-- en Agua</td><td rowspan="1" colspan="2" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold;">Atún Blanco  -->
<!-- en Agua</td> -->
<!-- <td rowspan="1" colspan="2" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold;">Atún Blanco  -->
<!-- en Aceite</td> -->
<!-- <td rowspan="1" colspan="2" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold;">Atún Claro  -->
<!-- en Aceite</td> -->
<!-- </tr><tr> -->
<!--     <td style="text-align:center;">0.99</td> -->
<!--     <td style="text-align:center;">0.53</td> -->
<!--     <td style="text-align:center;">1.27</td> -->
<!--     <td style="text-align:center;">1.22</td> -->
<!--     <td style="text-align:center;">1.49</td> -->
<!--     <td style="text-align:center;">1.29</td> -->
<!--     <td style="text-align:center;">2.56</td> -->
<!--     <td style="text-align:center;">0.62</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">1.92</td> -->
<!--     <td style="text-align:center;">1.41</td> -->
<!--     <td style="text-align:center;">1.19</td> -->
<!--     <td style="text-align:center;">1.22</td> -->
<!--     <td style="text-align:center;">1.29</td> -->
<!--     <td style="text-align:center;">1.00</td> -->
<!--     <td style="text-align:center;">1.92</td> -->
<!--     <td style="text-align:center;">0.66</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">1.23</td> -->
<!--     <td style="text-align:center;">1.12</td> -->
<!--     <td style="text-align:center;">1.18</td> -->
<!--     <td style="text-align:center;">1.03</td> -->
<!--     <td style="text-align:center;">1.27</td> -->
<!--     <td style="text-align:center;">1.27</td> -->
<!--     <td style="text-align:center;">1.30</td> -->
<!--     <td style="text-align:center;">0.62</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">0.85</td> -->
<!--     <td style="text-align:center;">0.63</td> -->
<!--     <td style="text-align:center;">1.28</td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;">1.35</td> -->
<!--     <td style="text-align:center;">1.28</td> -->
<!--     <td style="text-align:center;">1.79</td> -->
<!--     <td style="text-align:center;">0.65</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">0.65</td> -->
<!--     <td style="text-align:center;">0.67</td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;">1.23</td> -->
<!--     <td style="text-align:center;">0.60</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">0.69</td> -->
<!--     <td style="text-align:center;">0.60</td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;">0.67</td> -->
<!--     <td style="text-align:center;"></td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">0.60</td> -->
<!--     <td style="text-align:center;">0.66</td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!--     <td style="text-align:center;"></td> -->
<!-- </tr> -->
<!-- </tbody> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Suponga que las marcas de atún incluidas en el estudio representan una muestra aleatoria de todas las marcas de atún existentes en Estados Unidos, y que estos precios se encuentran normalmente distribuidos.  -->
<!-- <ol type ="a"> -->
<!--   <li> Calcule la probabilidad de que el precio promedio de atún blanco empacado en aceite sea a lo más $1.4$ dolares. -->
<!--   </li> -->
<!--   <li> Calcule la probabilidad de que la variabilidad del precio del atún blanco empacado en agua, sea mayor a la variabilidad del precio del atún claro empacado en agua. -->
<!--   </li> -->
<!--   <li> Calcule un intervalo de confianza del $92\%$ para el precio promedio de atún claro empacado en aceite. Interprete el intervalo. Específicamente, ¿a qué se refiere el "$95\%$"? -->
<!--   </li> -->
<!--   <li> Calcule un intervalo de confianza de $90\%$ para la diferencia en el precio medio de atún claro empacado en agua y atún claro empacado en aceite. -->
<!--   </li> -->
<!-- </ol> -->
<!-- 19. Un experimentador desea comprobar la variabilidad de mediciones obtenidas al usar equipo diseñado para medir el volumen de una fuente de audio. Tres mediciones independientes registradas por este equipo para la misma fuente de sonido fueron `$4.1$`, `$5.2$` y `$10.2$`. Calcule la probabilidad de que la variabilidad del volumen de una fuente de audio sea cuando mucho `$12.53$`. Suponga normalidad. -->
<!-- 20. La Environmental Protection Agency (*EPA*) ha establecido un máximo nivel de ruido de `$83_{dB}$` para camiones pesados. La forma en la que se aplique este límite afectará considerablemente al público y a la industria del transporte por carretera. Una forma de aplicar los límites es exigir que todos los camiones se apeguen al límite de ruido. Un segundo método menos satisfactorio es exigir que el nivel medio de ruido de la flota de camiones sea menor al límite. Si se adopta esta última regla, la variación en el nivel de ruido de un camión a otro se hace importante porque una variabilidad grande, implicaría que muchos camiones rebasen ese límite, incluso si el nivel medio de la flota fuera de `$83_{dB}$`. Una muestra aleatoria de seis camiones pesados produjo los siguientes niveles de ruido (en decibeles): -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td>85.4</td> -->
<!--     <td>86.8</td> -->
<!--     <td>85.3</td> -->
<!--     <td>84.8</td> -->
<!--     <td>86.0</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Basados en esta información y bajo el supuesto de normalidad -->
<!-- <ol type ="a"> -->
<!--   <li> Calcule la probabilidad de que la varianza de las lecturas de emisión de ruido de camiones, sea mayor a $2_{dB}$. Interprete sus resultados. -->
<!--   </li> -->
<!--   <li> Calcule la probabilidad de que la diferencia entre la media real y muestral sea como máximo de $0.4_{dB}$. -->
<!--   </li> -->
<!-- </ol> -->
<!-- 21. En el trabajo de laboratorio es deseable realizar cuidadosas verificaciones de la variabilidad de lecturas producidas en muestras estándar. En un estudio de la cantidad de calcio en agua potable realizado como parte de una evaluación de calidad del agua, la misma muestra estándar se hizo pasar por el laboratorio seis veces en intervalos aleatorios. Las seis lecturas, en partes por millón, fueron  -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td>9.32</td> -->
<!--     <td>9.48</td> -->
<!--     <td>9.70</td> -->
<!--     <td>9.46</td> -->
<!--     <td>9.26</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Si asumimos normalidad, cuál es la probabilidad de que la variabilidad de las lectura sea a lo más de `$0.4$` partes por millón. -->
<!-- 22. Un instrumento de precisión usado para la medición de la profundidad de una cuenca hidroeléctrica, garantiza dar lecturas que no varían en más de `$2$` unidades. Una muestra de ocho lecturas del instrumento en el mismo punto de la cuenca dio las siguientes mediciones  -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td>353</td> -->
<!--     <td>358</td> -->
<!--     <td>351</td> -->
<!--     <td>363</td> -->
<!--     <td>375</td> -->
<!--     <td>365</td> -->
<!--     <td>369</td> -->
<!--     <td>348</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Si asumimos que las mediciones se distribuyen normalmente con una media desconocida pero con una varianza de `$3$`, -->
<!-- <ol type ="a"> -->
<!--   <li> Calcule la probabilidad de que el promedio desconocido de las mediciones realizadas por el instrumento de precisión se encuentre entre $358$ y $363$. -->
<!--   </li> -->
<!--   <li> Construya un intervalo de confianza del $84\%$ para la medición promedio de todas las mediciones realizadas por el instrumento de precisión. -->
<!--   </li> -->
<!-- </ol> -->
<!-- 23. El Departamento de zoología de Virginia Tech llevó a cabo un estudio para estimar la diferencia en la cantidad de ortofósforo químico medido en dos estaciones diferentes del río James. El ortofósforo se mide en miligramos por litro. Se reunieron `$15$` muestras de la estación `$1$` y `$12$` muestras de la estación `$2$`. Las `$15$` muestras de la estación `$1$` tuvieron un contenido promedio de ortofósforo de `$3.84$` miligramos por litro y una desviación estándar de `$3.07$` miligramos por litro; en tanto que las `$12$` muestras de la estación `$2$` tuvieron un contenido promedio de `$1.49$` miligramos por litro y una desviación estándar de `$0.80$` miligramos por litro. Calcule un intervalo de confianza de `$95\%e$` para la diferencia en el contenido promedio verdadero de ortofósforo en estas dos estaciones. Suponga que las observaciones provienen de poblaciones normales. -->
<!-- 24. Una conjetura de un catedrático del departamento de microbiología, de la Facultad de Odontología de la Universidad de Washington, en St. Louis, Missouri, afirma que un par de tasas diarias de té verde o negro proporciona suficiente flúor para evitar el deterioro de los dientes. ¿Qué tan grande debería ser la muestra para estimar la proporción de habitantes de cierta ciudad que están a favor de tener agua fluorada, si se desea tener al menos un `$99\%$` de confianza en que el estimado está dentro del `$1\%$` del porcentaje verdadero? -->
<!-- 25. Un experimento publicado en Popular Science comparó el ahorro de combustible para dos tipos de camiones compactos que funcionan con diesel y están equipados de forma similar. Suponga que se utilizaron `$12$` camiones Volkswagen y `$10$` Toyota en pruebas con una velocidad constante de `$90$` kilómetros por hora. Si los `$12$` camiones Volkswagen promedian `$16$` kilómetros por litro con una desviación estándar de `$1.0$` kilómetros por litro, y los `$10$` Toyota promedian `$11$` kilómetros por litro con una desviación estándar de `$0.8$` kilómetros por litro, construya un intervalo de confianza del `$90\%$` para la diferencia entre los kilómetros promedio por litro de estos dos camiones compactos. Suponga que las distancias por litro para cada modelo de camión están distribuidas de forma aproximadamente normal. -->
<!-- 26. Una empresa de taxis trata de decidir si comprará neumáticos de la marca `$A$` o de la marca `$B$` para su flotilla de taxis. Para estimar la diferencia entre las dos marcas realiza un experimento utilizando `$12$` neumáticos de cada marca, los cuales utiliza hasta que se desgastan. Los resultados son,  -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -8rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td></td> -->
<!--     <td style="font-weight: bold">Marca A</td> -->
<!--     <td style="font-weight: bold">Marca B</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- <tbody> -->
<!--   <tr> -->
<!--     <td style="font-weight: bold">Media muestral</td> -->
<!--     <td>36300</td> -->
<!--     <td>38100</td> -->
<!--   </tr> -->
<!--   <tr> -->
<!--     <td style="font-weight: bold">Desviación estándar muestral</td> -->
<!--     <td>5000</td> -->
<!--     <td>6100</td> -->
<!--   </tr> -->
<!-- </tbody> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Calcule un intervalo de confianza del `$95\%$` para la diferencia entre los promedios de las dos marcas de neumáticos, suponiendo que las poblaciones se distribuyen de forma aproximadamente normal. -->
<!-- 27. Los anunciantes en televisión pueden creer erróneamente que casi todas las personas que ven Televisión entienden la mayor parte de los anuncios que ven y escuchan. Un estudio de investigación reciente pidió a `$2300$` personas de más de `$13$` años de edad que vieran extractos de publicidad de televisión de `$30$` segundos de duración. De éstos, `$1914$` televidentes entendieron mal todo o parte del extracto que vieron. Encuentre un intervalo de confianza de `$95\%$` para la proporción de todos los teleespectadores (de los cuales la muestra es representativa) que entenderán mal el total o parte de los extractos de televisión empleados en este estudio. -->
<!-- 28. Se considera usar dos marcas diferentes de pintura vinílica, y para ello, se decide seleccionar `$15$` especímenes de cada tipo de pintura, y se realizó la medición de los tiempos de secado en horas, obteniendo los siguientes resultados: -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <tbody><tr> -->
<!-- <td rowspan="1" colspan="5" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold; border-right-width: thick;">Pintura A</td><td rowspan="1" colspan="5" style="text-align:center;vertical-align: middle;width: 4.5rem;font-weight: bold;">Pintura B</td> -->
<!-- </tr><tr> -->
<!--     <td style="text-align:center;">3.5</td> -->
<!--     <td style="text-align:center;">2.7</td> -->
<!--     <td style="text-align:center;">3.9</td> -->
<!--     <td style="text-align:center;">4.2</td> -->
<!--     <td style="text-align:center; border-right-width: thick;">3.6</td> -->
<!--     <td style="text-align:center;">4.7</td> -->
<!--     <td style="text-align:center;">3.9</td> -->
<!--     <td style="text-align:center;">4.5</td> -->
<!--     <td style="text-align:center;">5.5</td> -->
<!--     <td style="text-align:center;">4.0</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">2.7</td> -->
<!--     <td style="text-align:center;">3.3</td> -->
<!--     <td style="text-align:center;">5.2</td> -->
<!--     <td style="text-align:center;">4.2</td> -->
<!--     <td style="text-align:center; border-right-width: thick;">2.9</td> -->
<!--     <td style="text-align:center;">5.3</td> -->
<!--     <td style="text-align:center;">4.3</td> -->
<!--     <td style="text-align:center;">6.0</td> -->
<!--     <td style="text-align:center;">5.2</td> -->
<!--     <td style="text-align:center;">3.7</td> -->
<!-- </tr> -->
<!-- <tr> -->
<!--     <td style="text-align:center;">4.4</td> -->
<!--     <td style="text-align:center;">5.2</td> -->
<!--     <td style="text-align:center;">4.0</td> -->
<!--     <td style="text-align:center;">4.1</td> -->
<!--     <td style="text-align:center; border-right-width: thick;">3.4</td> -->
<!--     <td style="text-align:center;">5.5</td> -->
<!--     <td style="text-align:center;">6.2</td> -->
<!--     <td style="text-align:center;">5.1</td> -->
<!--     <td style="text-align:center;">5.4</td> -->
<!--     <td style="text-align:center;">4.8</td> -->
<!-- </tr> -->
<!-- </tbody> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Si se supone que los tiempos de secado se distribuye normalmente. Calcule un intervalo de confianza del `$95\%$` para la diferencia promedio entre los tiempos medios de secado de la Pintura B y la Pintura A. -->
<!-- 29. A dos grupos de ratas diabéticas se les suministran dos niveles de dosis de insulina (alto y bajo) para verificar la capacidad de fijación de esta hormona. Se obtuvieron los siguientes datos. -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td></td> -->
<!--     <td style="font-weight: bold">Dosis baja</td> -->
<!--     <td style="font-weight: bold">Dosis alta</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- <tbody> -->
<!--   <tr> -->
<!--     <td style="font-weight: bold">Tamaño muestra</td> -->
<!--     <td>8</td> -->
<!--     <td>13</td> -->
<!--   </tr> -->
<!--   <tr> -->
<!--     <td style="font-weight: bold">Media muestral</td> -->
<!--     <td>1.98</td> -->
<!--     <td>1.30</td> -->
<!--   </tr> -->
<!--   <tr> -->
<!--     <td style="font-weight: bold">Desviación estándar muestral</td> -->
<!--     <td>0.51</td> -->
<!--     <td>0.35</td> -->
<!--   </tr> -->
<!-- </tbody> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Determine un intervalo de confianza del `$95\%$` para la diferencia en la capacidad promedio verdadera de fijación de la insulina entre las dos muestras. -->
<!-- 30. Un fabricante de baterías para automóvil afirma que sus baterías durarán, en promedio, `$3$` años con una varianza de `$1$` año. Suponga que se toma una muestra aleatoria de `$15$` de estas baterías y se les mide su tiempo de duración, en años, obteniendo los siguientes reusltados -->
<!-- <pre style="font-family: 'Open Sans',sans-serif; margin-bottom: -4rem; margin-top: -2rem; font-size: 98%;"> -->
<!-- <table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;"> -->
<!-- <thead> -->
<!--   <tr> -->
<!--     <td>1.9</td> -->
<!--     <td>2.4</td> -->
<!--     <td>3.0</td> -->
<!--     <td>3.5</td> -->
<!--     <td>4.2</td> -->
<!--     <td>3.6</td> -->
<!--     <td>2.7</td> -->
<!--     <td>1.5</td> -->
<!--     <td>3.5</td> -->
<!--     <td>2.7</td> -->
<!--     <td>2.9</td> -->
<!--     <td>3.1</td> -->
<!--     <td>3.7</td> -->
<!--     <td>1.9</td> -->
<!--     <td>4.4</td> -->
<!--   </tr> -->
<!-- </thead> -->
<!-- </table> -->
<!-- </pre> -->
<!-- Suponiendo que la duración de todas las baterías se distribuye de forma aproximadamente normal. -->
<!-- <ol type ="a"> -->
<!--   <li> Calcule la probabilidad de que el tiempo promedio de durabilidad de todas las baterías sea de $3$ o más años. -->
<!--   </li> -->
<!--   <li> Construya un intervalo de confianza del $92\%$ para el promedio de durabilidad de todas las baterías y después decida si la afirmación del fabricante sobre que el promedio de durabilidad es de $3$, es o no válida. -->
<!--   </li> -->
<!-- </ol> -->
<!-- 31. Dos marcas de refrigeradores, denotadas por `$A$` y `$B$` poseen garantías de `$3$` año. Suponga que en una muestra aleatoria de `$50$` refrigeradores de la marca `$A$`, se encontró que el tiempo medio de vida de lo refrigeradores es de `$4.3$` años con una desviación estándar de `$1.2$` años, mientras que, en una muestra aleatoria independiente de `$60$` refrigeradores de la marca `$B$`, se encontró que el tiempo promedio de vida de los refrigeradores es de `$5.5$` años con una desviación estándar de `$1.7$` años.  -->
<!-- <ol type ="a"> -->
<!--   <li> Calcule con un nivel de confianza del $90\%$ un intervalo para la diferencia los tiempos promedio de vida de los refrigeradores de las marcas $A$ y $B$.</li> -->
<!--   <li> ¿Podría concluirse que hay evidencia suficiente para afirma que existen diferencia significativas entre los tiempos de vida promedio para las dos marcas de refrigeradores? ¿Por qué?</li>  -->
<!-- </ol> -->
<!-- Un investigador de la <tt>ucla</tt> afirma que la esperanza de vida de los ratones se puede extender hasta en `$25\%$` cuando se reduce aproximadamente `$40\%$` de las calorías de su dieta desde el momento en que son destetados, en donde, la dieta restringida se enriquece hasta niveles normales con vitaminas y proteínas. Si se supone que a partir de estudios previos se sabe el aumento de vida de los ratones se distribuye normalmente con una desviación estándar de `$5.8$` meses, ¿cuántos ratones se deberían incluir en la muestra para tener un `$99\%$` de confianza en que la vida media esperada de la muestra estará dentro de `$2$` meses a partir de la media de la población para todos los ratones sujetos a la dieta reducida? -->