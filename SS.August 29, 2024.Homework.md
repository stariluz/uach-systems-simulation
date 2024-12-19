#### 1)

![alt text](<WhatsApp Image 2024-08-29 at 19.52.44_c9592190.jpg>)

![alt text](<WhatsApp Image 2024-08-29 at 19.52.45_ebcc199f.jpg>)

![alt text](<WhatsApp Image 2024-08-29 at 19.52.45_736bddd1.jpg>)

![alt text](<WhatsApp Image 2024-08-29 at 19.52.45_dfdd1aaf.jpg>)

#### 2)
| Marca | Angulo | Resistencia (k$\Omega$) |
| ----- | ------ | ----------------------- |
| 1     | 0      | 0.00662                 |
| 2     | 10     | 0.0072                  |
| 3     | 20     | 0.0412                  |
| 4     | 30     | 6.06                    |
| 5     | 40     | 12.43                   |
| 6     | 50     | 23.11                   |
| 7     | 60     | 32.34                   |
| 8     | 70     | 40.64                   |
| 9     | 80     | 48.05                   |
| 10    | 90     | 56.81                   |
| 11    | 100    | 66.4                    |
| 12    | 110    | 72.6                    |
| 13    | 120    | 81.4                    |
| 14    | 130    | 90                      |
| 15    | 140    | 97.4                    |
| 16    | 150    | 105.9                   |
| 17    | 160    | 115.7                   |
| 18    | 170    | 122.2                   |
| 19    | 180    | 129.5                   |
| 20    | 190    | 136.2                   |
| 21    | 200    | 146                     |
| 22    | 210    | 154.7                   |
| 23    | 220    | 160.8                   |
| 24    | 230    | 168.7                   |
| 25    | 240    | 175.2                   |
| 26    | 250    | 179.1                   |
| 27    | 260    | 185.2                   |
| 28    | 270    | 191.9                   |
| 29    | 280    | 199.3                   |
| 30    | 290    | 204.7                   |
| 31    | 300    | 204.7                   |
| 32    | 310    | 204.8                   |

#### 3) 
Se dice que una función es lineal si tiene estas propiedades:

###### Homogeneidad:

$f(ax) = af(x)$

$f(2(150)) = 2f(150)$

$f(300) = 211.8$

El $f(200)$ de la muestra vale $204.7$, 

La diferencia entre $204.7$ y $211.8$ es de $7.1$ que cae dentro del $5\%$ de error. Por lo cual es lineal en este segmento.

##### Aditividad:
$f(x_1+x_2) = f(x_1) + f(x_2)$

Entonces para
$f(100 + 150)=f(100)+f(150)=66.4+105.9=172.3$

Comparando con el valor real $f(250)=179.1$

La diferencia entre $179.1$ y $172.3$ es de $8.75$ que cae dentro del $5\%$ de error. Por lo cual es lineal en este segmento.

##### Region de linealidad 

En la gráfica inferior se puede visualizar que la
región aproximada de linealidad es entre 25° y 280°.

#### 4)

Se utilizó el método númerico de mínimos cuadrados, el cual busca trazar la recta que más se acerque a los datos obtenidos.
La ecuación de la recta la da la ecuación.

$Y = C_1x+C_2+Error$

$C_1 = n \frac{\sum{X_iY_i}-\sum{X_i}\sum{Y_i}}{n \sum{X_i^2} - (\sum{X_i})^2}$

$C_2 = \frac{\sum{Y_i}}{n} - C_1 = \frac{\sum{X_i}}{n}$


#### 5)

El error se obtiene a partir de la suma de los cuadrados de la diferencia entre el valor obtenido experimentalmente y el valor esperado según la función de regresión.

$\textrm{Error} = \sum{(Y_i-C_2-C_iX_i)}^2$

![Imagen](./img/SS.August%2029,%202023.Homework.img%203.png)

El error de la función obtenida es del $5.55\%$

#### Fuentes bibliográficas
Khan Academy. (n.d.). https://es.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-dc-circuit-analysis/a/ee-linearity
Romero Rodriguez, E. (2007). Ajuste de curvas. https://www.geocities.ws/datos_universidad/MNumericos/AjusteDeCurvas