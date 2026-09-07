---
title: "Práctica 05"
course: "estadistica-y-probabilidades"
order: 20
classType: "practica"
description: "Ejercicios sobre: - Variables aleatorias conjuntas - Esperanza matemática - Esperanza matemática condicional - Varianza"
math: true
bibliography: "../../referencias.bib"
---

Lista de ejercicios
===================

1.  Sean $X$ y $Y$ dos variables aleatorias discretas las cuales
    pueden tomar como posibles valores $-1$, $0$, y $1$. En la
    siguiente tabla se dan las probabilidades conjuntas para todos los
    posibles valores de $X$ y $Y$.
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
    <script type="math/tex">\mathbf{-1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{0}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;vertical-align: middle !important;" rowspan="3">
    <script type="math/tex">Y</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{-1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{1}{16}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{3}{16}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{1}{16}</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{0}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{3}{16}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{3}{16}</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{1}{16}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{3}{16}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\frac{1}{16}</script>
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Obtenga las funciones de probabilidad marginales de $X$ y de
    $Y$.
    </li>
    <li>
    Pruebe si las variables aleatorias $X$ y $Y$ son independientes.
    </li>
    <li>
    Calcule la $\mathbb{P}(X=1|Y\leq 0)$.
    </li>
    </ol>

2.  Si $X$ y $Y$ son variables aleatorias discretas con función de
    probabilidad dada por:
    
$$\begin{align*}f(x,y)=k\left(\frac{x+y}{xy}\right) \quad \quad x = 1,2,3; y = 2,3\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor $k$ que hace a la función de masa de
    probabilidad, una función de probabilidad bien definida.
    </li>
    <li>
    Encuentre la correlación entre $X$ y $Z$ donde $Z = 6X$.
    </li>
    </ol>

3.  Suponga una función de densidad de probabilidad conjunta de las
    variables aleatorias $X$, $Y$ y $Z$, la cual se define como
    
$$\begin{align*}f(x,y,z)=\begin{cases}kxyz^2 & 0< x < 1; 0< y <1; 0< z<3 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    A partir de esta ecuación, calcule
    <ol type="a">
    <li>
    El valor $k$ que hace que la función $f(x,y,z)$, sea una función
    de densidad válida.
    </li>
    <li>
    La función de densidad marginal conjunta de $Y$ y $Z$.
    </li>
    <li>
    La densidad marginal de $Y$.
    </li>
    <li>
    $\mathbb{P}(\frac{1}{4}\lt  X \lt  \frac{1}{2}, Y \gt  \frac{1}{3}, 1 \lt  Z \lt  2)$
    </li>
    <li>
    $\mathbb{P}(0 \lt  X \lt  \frac{1}{2}| Y = \frac{1}{4} , Z = 2)$
    </li>
    </ol>

4.  Sea $X$ el número de veces que fallará cierta máquina de control
    numérico: 1, 2 o 3 veces en un día dado, y $Y$ denota el número de
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
    Calcule el $Corr(X,Y^2)$.

5.  Si $X$ y $Y$ son variables aleatorias con función de
    probabilidad conjunta dada por
    
$$\begin{align*}f(x,y)=xye^{-x-y},\quad x>0,y>0\end{align*}$$

    <ol type="a">
    <li>
    La $f(x,y)$ es efectivamente una función de densidad de
    probabilidad conjunta bien definida? de no serlo, por qué constante
    $k$ la multiplicaría?.
    </li>
    <li>
    Determine la distribución marginal de $X$.
    </li>
    <li>
    Determine la distribución marginal de $Y$.
    </li>
    <li>
    ¿Cuál es la probabilidad de $4\lt X\lt 6$ y $Y\gt 2$?.
    </li>
    <li>
    Determine la distribución condicional $f(X | 1\lt Y\lt 4)$.
    </li>
    <li>
    Si se sabe que $Y\gt 5$, entonces, cuál es la probabilidad de que
    $X\lt 8$.
    </li>
    </ol>

6.  Una moneda se lanza dos veces. Sea $X$ el número de caras en el
    primer lanzamiento y $Y$ el número total de caras en los $2$
    lanzamientos. Si la moneda no está balanceada y la probabilidad de
    sello es dos veces la probabilidad de cara, calcule
    <ol type="a">
    <li>
    la media y varianza de $X$ y $Y$
    </li>
    <li>
    el coeficiente de asimetría de $X$ y $Y$
    </li>
    <li>
    la correlación de $3X$ y $2Y$
    </li>
    </ol>

7.  Considere las variables aleatorias $X$ y $Y$ que representan el
    número de vehículos que llegan a dos esquinas de calles separadas
    durante cierto periodo de $2$ minutos. Estas esquinas de las
    calles están bastante cerca una de la otra, así que es importante
    que los ingenieros de tráfico se ocupen de ellas de manera conjunta
    si fuera necesario. Se sabe que la distribución conjunta de $X$ y
    $Y$ es
    
$$\begin{align*}f(x,y)=\begin{cases}\frac{9}{16}\frac{1}{4^{x+y}}  & x=0,1,2,\ldots;\quad y=0,1,2,\ldots \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    ¿Son independientes las dos variables aleatorias $X$ y $Y$?
    Justifique su respuesta.
    </li>
    <li>
    ¿Cuál es la probabilidad de que, durante el periodo en cuestión,
    lleguen menos de $4$ vehículos a las dos esquinas?.
    </li>
    </ol>

8.  Un sistema químico que surge de una reacción química tiene dos
    componentes importantes, entre otros, en una mezcla. La distribución
    conjunta que describe las proporciones $X$ y $Y$ de estos dos
    componentes está dada por
    
$$\begin{align*}f(x,y)=\begin{cases}2  & 0<x<y<1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Determine la esperanza condicional $\mathbb{E}(Y | X)$
    </li>
    <li>
    Determine la esperanza condicional $\mathbb{E}(X | Y)$
    </li>
    </ol>

9.  Si $X$ y $Y$ son variables aleatorias discretas con función de
    probabilidad dada por: $f(x,y)=k(\frac{x+y}{xy})$,para
    $x=1,2,3$; $y=1,2,3$.
    <ol type="a">
    <li>
    Encuentre el valor de $k$ que hace que $f(x,y)$ sea una función
    de masa de probabilidad conjunta.
    </li>
    <li>
    Encuentre la distribución marginal de $X$ y $Y$.
    </li>
    <li>
    Encuentre la distribución condicional de $X$ dado $Y=1$.
    </li>
    <li>
    las v.a $X$ y $Y$ son independientes?.
    </li>
    </ol>

10. Calcule la covarianza de las variables aleatorias $X$ y $Y$ que
    tienen la siguiente función de densidad de probabilidad conjunta
    
$$\begin{align*}f(x,y)=\begin{cases}x+y & 0<x<1,\quad 0<y<1,\\0 & \text{en otro caso}\end{cases}\end{align*}$$

11. Si la distribución de probabilidad conjunta de $X$ y $Y$ está
    dada por
    
$$\begin{align*}f(x,y)=\begin{cases}\frac{x+y}{30}  & x=0,1,2,3; y=0,1,2 \\0 & \text{en otro caso}\end{cases}\end{align*}$$
  
    Calcule
    <ol type="a">
    <li>
    $\mathbb{P}(X \leq 2, Y = 1)$
    </li>
    <li>
    $\mathbb{P}(X\gt Y)$.
    </li>
    <li>
    $\mathbb{P}(X+Y = 4)$.
    </li>
    <li>
    $\mathbb{P}(X\gt 2|Y\leq1)$.
    </li>
    </ol>

12. La función de densidad de probabilidad conjunta de las variables
    aleatorias $X$, $Y$ y $Z$ está dada por
    
$$\begin{align*}f(x,y,z)=\begin{cases}4xyz^2; &0< x,y <1; 0< z<3 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    Calcule
    <ol type="a">
    <li>
    la correlación de $X$ y $Y$.
    </li>
    <li>
    la correlación de $X$ y $Z$.
    </li>
    <li>
    la correlación de $Y$ y $Z$.
    </li>
    </ol>

13. Si $X$, $Y$ y $Z$ tienen la siguiente función de densidad de
    probabilidad conjunta:
    
$$\begin{align*}f(x,y,z)=\begin{cases}kxy^2z& 0<x<1;0<y<1; 0<z<2 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor $k$ para que hace que $f(x,y,z)$ sea una
    función de densidad de probabilidad conjunta.
    </li>
    <li>
    Calcule las distribuciones marginales $g(x)$, $h(y)$, $i(z)$,
    $j(x,y)$, $k(x,z)$ y $l(y,z)$.
    </li>
    <li>
    Calcule $\mathbb{P}(X \lt  \frac{1}{4}, Y \gt  \frac{1}{2}, 1 \lt  Z \lt  2)$.
    </li>
    <li>
    Calcule
    $\mathbb{P}(X \lt  \frac{1}{3} | Y \lt  \frac{1}{8}, Z \gt  \frac{2}{3})$.
    </li>
    </ol>

14. Sean $X$ y $Y$ son variables aleatorias que poseen la siguiente
    función de densidad de probabilidad conjunta
    
$$\begin{align*}f(x,y)=xye^{-x-y},\quad x>0,y>0\end{align*}$$

    Entonces, a partir de ésta, calcule la covarianza de $6X^2$ y
    $3Y^3$.

15. Una moneda se lanza dos veces. Sea $X$ el número de caras en el
    primer lanzamiento y $Y$ el número total de caras en los $2$
    lanzamientos. Si la moneda no está balanceada y la probabilidad de
    sello es dos veces la probabilidad de cara, calcule
    <ol type="a">
    <li>
    La distribución de probabilidad conjunta de $X$ y $Y$.
    </li>
    <li>
    La distribución marginal de $X$.
    </li>
    <li>
    La distribución marginal de $Y$.
    </li>
    <li>
    La probabilidad de que ocurra al menos $1$ cara.
    </li>
    </ol>

16. Una empresa dulcera distribuye cajas de chocolates con un surtido de
    cremas, chiclosos y envinados. Suponga que cada caja pesa $1$
    kilogramo, pero que los pesos individuales de cremas, chiclosos y
    envinados varían de una a otra caja. Para una caja seleccionada al
    azar, represente los pesos de las cremas y los chiclosos con $X$ y
    $Y$, respectivamente, si se supone que la función de densidad
    conjunta de estas variables es
    
$$\begin{align*}f(x,y)=\begin{cases}24xy & 0\leq x\leq1;0\leq y\leq1; x+y\leq1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la esperanza de $Z = 3Y - 2X$
    </li>
    <li>
    Calcule la varianza de $Z$
    </li>
    </ol>

17. Una empresa dulcera distribuye cajas de chocolates con un surtido de
    cremas, chiclosos y envinados. Suponga que cada caja pesa $1$
    kilogramo, pero que los pesos individuales de cremas, chiclosos y
    envinados varían de una a otra cajas. Para una caja seleccionada al
    azar, represente los pesos de las cremas y los chiclosos con $X$ y
    $Y$, respectivamente, y suponga que la función de densidad
    conjunta de estas variables es
    
$$\begin{align*}f(x,y)=\begin{cases}24xy; & 0\leq x\leq1;0\leq y\leq1; x+y\leq1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule la probabilidad de que en una caja dada los envinados
    representen más de la mitad del peso.
    </li>
    <li>
    Calcule la densidad marginal para el peso de las cremas.
    </li>
    <li>
    Calcule la probabilidad de que el peso de los chiclosos en una caja
    sea menor que $1/8$ de kilogramo, si se sabe que las cremas
    constituyen $3/4$ partes del peso.
    </li>
    </ol>

18. Si $X$, $Y$ y $Z$ tienen la siguiente función de densidad de
    probabilidad conjunta:
    
$$\begin{align*}f(x,y,z)=\begin{cases}kxy^2z& 0<x<1;\quad 0<y<1;\quad 0<z<2 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Calcule el valor $k$ que hace que la función de densidad de
    probabilidad conjunta esté bien definida.
    </li>
    <li>
    Calcule $\mathbb{E}(X |Y \gt  \frac{1}{2}, 1 \lt  Z \lt  2)$
    </li>
    </ol>

19. Sean $X$ y $Y$ dos variables aleatorias con función de
    probabilidad dada por
    
$$\begin{align*}f(x,y)=\begin{cases}k(3x-y) & 1 \leq x \leq 2, 1 \leq y \leq 3; x < y + 0.5 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Obtener el valor $k$ que hace que la función esté bien definida y
    encuentre la función de distribución acumulada conjunta.
    </li>
    <li>
    ¿Cuál es la probabilidad de que $X\lt 3/2$ y $Y\lt 2$?.
    </li>
    <li>
    Obtenga las funciones marginales para $X$ y $Y$.
    </li>
    <li>
    Obtenga las función de distribución acumulada de $X$ y de $Y$.
    </li>
    <li>
    Calcule $\mathbb{P}(0.8\lt X\lt 1.6)$ y $\mathbb{P}(Y\gt 2.3)$.
    </li>
    <li>
    Calcule $\mathbb{P}(0.8\lt X\lt 1.6|Y\gt 2.3)$.
    </li>
    <li>
    Pruebe si $X$ y $Y$ son independientes.
    </li>
    </ol>

20. Suponga que la función de probabilidad conjunta de un sistema
    químico puede ser representado como
    
$$\begin{align*}f(x,y)=\begin{cases}kx^2  & 0<x<y<1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Determine la distribución marginal $g(x)$ de la proporción $X$ y
    verifique que sea una función de densidad válida.
    </li>
    <li>
    ¿Cuál es la probabilidad de que la proporción $Y$ sea menor que
    $0.5$, dado que $X$ es $0.7$?.
    </li>
    <li>
    ¿Cuál es la probabilidad de que la proporción $X$ sea mayor que
    $0.5$, dado que $Y$ es $0.7$?.
    </li>
    </ol>

21. Sean $X$ y $Y$ variables aleatorias independientes tal que sus
    distribuciones marginales son $g(x)=3x^2$ para $0<x<1$ y
    $h(y)=2y$ para $0<y<1$. Calcule
    $\mathbb{P}(X\leq\frac{1}{3}|Y=\frac{1}{2})$.

22. Suponga la siguiente función de probabilidad para las variables
    aleatorias $X$ y $Y$
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
    <script type="math/tex">\mathbf{0}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{2}</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;vertical-align: middle !important;" rowspan="3">
    <script type="math/tex">Y</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{0}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.0600</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.1050</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.1350</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{1}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.0900</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.1575</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.2025</script>
    </td>
    </tr>
    <tr>
    <td style="text-align:center;">
    <script type="math/tex">\mathbf{2}</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.0500</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.0875</script>
    </td>
    <td style="text-align:center;">
    <script type="math/tex">0.1125</script>
    </td>
    </tr>
    </tbody>
    </table>
    <ol type="a">
    <li>
    Evalúe la distribución marginal de $X$.
    </li>
    <li>
    Evalué la distribución marginal de $Y$.
    </li>
    <li>
    Calcule $\mathbb{P}(Y = 2 | X = 1)$.
    </li>
    <li>
    Calcule $\mathbb{P}(X\lt 2|Y\leq1)$.
    </li>
    <li>
    Pruebe si las variables aleatorias $X$ y $Y$ son independientes.
    </li>
    </ol>

23. Un sistema químico que surge de una reacción química tiene dos
    componentes importantes, entre otros, en una mezcla. La distribución
    conjunta que describe las proporciones $X$ y $Y$ de estos dos
    componentes está dada por
    
$$\begin{align*}f(x,y)=\begin{cases}2  & 0<x<y<1 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Determine la distribución marginal de $X$.
    </li>
    <li>
    Determine la distribución marginal de $Y$.
    </li>
    <li>
    ¿Cuál es la probabilidad de que las proporciones del componente
    generen los resultados $X \lt  0.2$ y $Y \gt  0.5$?.
    </li>
    <li>
    Determine la distribución condicional $f(X | Y)$.
    </li>
    <li>
    Si se sabe que $Y\gt 0.2$, entonces, cuál es la probabilidad de que
    $X\lt 0.1$.
    </li>
    </ol>

24. Sea $X$ el número de veces que fallará cierta máquina de control
    numérico: $1$, $2$ o $3$ veces en un día dado. Y sea $Y$ el
    número de veces que se llama a un técnico para una emergencia, su
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
    <ol type="a">
    <li>
    Evalúe la distribución marginal de $X$.
    </li>
    <li>
    Evalué la distribución marginal de $Y$.
    </li>
    <li>
    Calcule $\mathbb{P}(Y = 3 | X = 2)$.
    </li>
    <li>
    Calcule $\mathbb{P}(X\geq2|Y\leq3)$.
    </li>
    <li>
    Pruebe si las variables aleatorias $X$ y $Y$ son independientes.
    </li>
    </ol>

25. En funcion de su prioridad, un programa para computadora espera en
    la fila de entrada cierto tiempo, después del cual lo ejecuta el
    procesador central en un lapso dado. La función de densidad conjunta
    para los tiempos de espera $X$ (en minutos) y ejecución $Y$ (en
    segundos) se determina por
    
$$\begin{align*}f(x,y)=\begin{cases}2e^{-\left(\frac{x}{5}+10y\right)} & x,y > 0 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    con función de distribución acumulada conjunta dada por
    
$$\begin{align*}F(x,y)=\begin{cases}\left[1-e^{-\frac{x}{5}}\right] \left[1-e^{-10y}\right]  & x,y > 0 \\0 & \text{en otro caso}\end{cases}\end{align*}$$

    <ol type="a">
    <li>
    Obtener la probabilidad conjunta de que el tiempo de espera no sea
    mayor de ocho minutos y el de ejecución no sea mayor de $12$
    segundos.
    </li>
    <li>
    Si se sabe que el tiempo de espera es mayor a seis minutos, calcule
    la probabilidad de que el tiempo de ejecición sea menor a $15$
    segundos.
    </li>
    <li>
    Obtener las funciones de densidad marginal y probar si estos lapsos
    de tiempo son variables aleatorias independientes.
    </li>
    </ol>

26. Sean $X$ y $Y$ variables aleatorias continuas distribuidas
    conjuntamente con
    
$$\begin{align*}f(x,y)=kxy \quad \text{ para } 0<x<5; \quad 1<y<x\end{align*}$$

    El valor de $k$ que hace que $f(x,y)$ sea una función de
    densidad de probabilidad conjunta es?