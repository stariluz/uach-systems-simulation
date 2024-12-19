Agosto 15
---
# Simulación de sistemas
### Oscar Ramsés Ruiz Varela

Simuldor $\to$ Programa
Emulador $\to$ Hardware + Software


#### STEM. Science Technology Engineering Math
Los perceptones no son capacez de resolver la operación XOR individualmente.
| A   | B   | Salida |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 0      |

Ley de Coulomb.
Nos dice la fuerza ejercida entre cargas positivas y negaticas.

### Heurística
Inducir es obtener las reglas a partir de las situaciones.
Intuitiva y deductiva. Implica obtener una conclusión a partir de las observaciones.
Deducir es predecir las situaciones a partir de la inducción.

El objetivo de la heurística es que la inducción y la deducción la realice una máquina.

> Ver Lex Fridman. Vehículos autónomos.

Un arduino trabaja a 16kb y a 16MHz.
Una computadora a 16Gb y a 3.5GHz.

#### Ejemplo
Trayectoria de un avión es un problema P.
Dado el viento, y la velocidad del avión podemos obtener la respuesta.

Un problema NP la computadora quiza lo puede resolver pero no sabemos si lo resolvera o cuando lo hará.


Codec Decodec. Se utiliza la transformada de Fourier para no perder calidad en la compresión y decompresión.
Michael Faraday.

Alemania es el país que hace el mejor acero del mundo.

---

Agosto 16
---
El profe hara un electrocardiografo y nosotros harfemos un simulador de un corazón.

Los simuladores se utilizan para practicar, para familiarizarnos con el funcionamiento de un equipo.

Lo vamos a hacer en Python. Simular una condición normal y 4 enfermedades.

La salida de nuestro código serán numeros, que resultarán en la información que muestra un electrocardiograma al leer un corazón.

Tendremos que hacer varios ejemplos para cada padecimiento, va a ser estocástico.

# Unidad 1. Modelo matemático
Gráfico, ecuación, tabla, red neuronal.

Una red WAN es para todo el mundo. Una red LAN es una red local. Al abrirnos a una red publica, pueden obtener toda la información de la computadora.
Las VPN manejan nuestra información de manera encriptada. Es decir, se pueden manejar sobre internet pero nadie más de internet tendra información sobre las transacciones de datos realizadas. 
Nuestros sistemas deben tener acceso a internet.

---

Agosto 22
---
### Ejercicio. Caracterizar un potenciometro.

Al medir un potenciometro 

Ley de Ohm
$V=IR$

$I=\frac{V}{R}$

Cuando la resistencia tiende a cero la corriente tiende a 0.

Un arduino entrega $100mA$.
Un led consume $10mA$.

$I=0.075mA=\frac{1.5V}{20K\omega}$

El monoblock es el motor de una sola pieza.

¿Que voltaje utilizan las baterias de los carros?
Las baterias tienen 12V pero en uso tendrán más voltaje por que el voltaje se cae, no se mantiene.

A un amplificador se le debe poner una bocina que tenga la imperancia que indica. De poner una bocina que no es de la imperancia se puede quemar dado que va a almacenar la potencia.

Los sensores se quedan con parte de la señal. Como queremos que esta salga del sensor, utilizaremos un amplificador operacional.

El tipo de amplificador operacional mas sencillo que existe es el amplificador inversor.

RF Es una retroalimentación (RetroFeedback).

El sensor es una fuente de voltaje.

El ruido del ambiente es de 60 htz.

Un amplificador barato es un 741.

Los amplificadores buenos pueden costar hasta 70 pesos.

Hay que conseguir un potenciometro.

Conectar multimetro en medio y a las orillasn del potenciometro. COlocar una aguja.
Con el multimetro medir resistencia.
Con la aguja medir los grados y medir las resistencias en cada grado.
Hacer la tabla de valores y calcular la regresion lineal y el error.


---

Agosto 23
---
### 1.2 Caracterización de un dispositivo electrónico
Diodo rectificador


---

Agosto 29
---
Practica diodo

---

Septiembre 6
---
En el condensador internamente no tiene corriente. Se carga del lado positivo, mientras se descarga del lado derecho, no obstante al ser un asilante, no puede pasar corriente. La corriente que se obtiene al otro lado se origina en el condensador.

La raspberry trabaja a 3V, el esp 32 tambien
El arduino trabaja a 5 volts


Al mandarle una señal cuadrada de picos de 12V al micro Atmega (5V) se quemará.
Con 2 miliampers funciona.

En la realidad no es necesario preocuparnos por que en el pin de entrada se caerán 3 o 4 volts.


---

Septiembre 18
---
# Practica divisor de voltaje
Calcular los valores de resistencia para $R_5$ para obtener los siguientes voltajes en el punto de conexión 
de ambos componentes  
 
1v 5v 2.5v -2v 
 
$V_{CC} = 5V$

$R_4 = 4.7 k\varOmega$

$R_T = R_5 + R_4 = R_5 + 4.7 k\varOmega$

$V_{out} = V_{in} \times \frac{R_4}{R_4 + R_5}$

$R_5 = V_{in} \times \frac{R_4}{V_{out}} - R_4$

---

$V_5 = 4V$

$V_4 = 1V$

$R_5 = \frac{4}{5}R_T$ 

$R_T = \frac{4}{5}R_T + 4.7 k\varOmega$

$R_T - \frac{4}{5}R_T = 4.7 k\varOmega$

$\frac{1}{5}R_T = 4.7 k\varOmega$

$R_T = \frac{5}{1}(4.7) k\varOmega = 23.5 k\varOmega$

> $R_5 = \frac{4}{5}(23.5) k\varOmega = 18.8 k\varOmega$ 

$R_5 = 5V \times \frac{4.7 k\varOmega}{1V} - 4.7 k\varOmega = 18.8 k\varOmega$

---

$V_5 = 0V$

$V_4 = 5V$

> $R_5 = \frac{0}{5}R_T k\varOmega = 0 k\varOmega$ 

$R_T = 4.7 k\varOmega$

$R_5 = 5V \times \frac{4.7 k\varOmega}{5V} - 4.7 k\varOmega = 0 k\varOmega$

---

$V_5 = 2.5V$

$V_4 = 2.5V$

$R_5 = \frac{1}{2}R_T$ 

$R_T = \frac{1}{2}R_T + 4.7 k\varOmega$

$R_T - \frac{1}{5}R_T = 4.7 k\varOmega$

$\frac{1}{2}R_T = 4.7 k\varOmega$

$R_T = \frac{2}{1}(4.7) k\varOmega = 9.4 k\varOmega$

> $R_5 = \frac{1}{2}(9.4) k\varOmega = 4.7 k\varOmega$ 

$R_5 = 5V \times \frac{4.7 k\varOmega}{2.5V} - 4.7 k\varOmega = 4.7 k\varOmega$

---

$V_5 = 7V$

$V_4 = -2V$

$R_5 = \frac{7}{5}R_T$ 

$R_T = \frac{7}{5}R_T + 4.7 k\varOmega$

$R_T - \frac{7}{5}R_T = 4.7 k\varOmega$

$\frac{-2}{5}R_T = 4.7 k\varOmega$

$R_T = \frac{5}{-2}(4.7) k\varOmega = -11.75 k\varOmega$

> $R_5 = \frac{7}{5}(-11.75) k\varOmega = -16.45 k\varOmega$ 

$R_5 = 5V \times \frac{4.7 k\varOmega}{-2V} - 4.7 k\varOmega = -16.45 k\varOmega$






Calcular los valores de resistencia para R_5 para obtener las corrientes 
Máxima Mínima Media 
 
$V_5 = 5V$

$V_4 = 0V$

$R_5 = \frac{5}{5}R_T = R_T$ 

$R_T = \frac{5}{5}R_T + 4.7 k\varOmega$

$R_T - \frac{7}{5}R_T = 4.7 k\varOmega$

$\frac{-2}{5}R_T = 4.7 k\varOmega$

$R_T = \frac{5}{-2}(4.7) k\varOmega = -11.75 k\varOmega$

> $R_5 = \frac{7}{5}(-11.75) k\varOmega = -16.45 k\varOmega$ 

$R_5 = 5V \times \frac{4.7 k\varOmega}{-2V} - 4.7 k\varOmega = -16.45 k\varOmega$

---

$I_{max} = \frac{V_{in}}{R_4} = \frac{5V}{4.7 k\varOmega} = 1.0638mA$

$I_{min} = 0A$

$I_{media} = \frac{I_{max} + I_{min}}{2} = \frac{I_{max}}{2} = \frac{1.0638mA}{2} = 0.5319mA$

 
Explicar en qué rango de valores de resistencia de R_5, el voltaje en el punto de conexión R_4-R_5  el circuito es lineal 
 

$V_{R_4} = V_{in} \times \frac{R_4}{R_4 + R_5}$

$V_{R_4} = 5V \times \frac{4.7 k\varOmega}{4.7 k\varOmega + R_5}$



 
Vx depende de la posición del potenciómetro. La resistencia limita la corriente aún en caso que el 
potenciómetro aporte resistencia cero. Vcc=5v. 

Calcular los valores de R_6 para obtener los siguientes voltajes en el punto de conexión de ambos componentes  
 

1v 5v 2.5v -2v 
 
$V_{CC} = 5V$

$R_7 = 4.7 k\varOmega$

$R_T = R_6 + R_7 = R_6 + 4.7 k\varOmega$

$V_{out} = V_{in} \times \frac{R_6}{R_6 + R_7}$

$R_6 = V_{out} \times \frac{R_7}{V_{in}-V_{out}}$

---

$V_7 = 4V$

$V_6 = 1V$

$R_6 = \frac{1}{5}R_T$ 

$R_T = \frac{1}{5}R_T + 4.7 k\varOmega$

$R_T - \frac{1}{5}R_T = 4.7 k\varOmega$

$\frac{4}{5}R_T = 4.7 k\varOmega$

$R_T = \frac{5}{4}(4.7) k\varOmega = 5.875 k\varOmega$

> $R_6 = \frac{1}{5}(5.875) k\varOmega = 1.175 k\varOmega$ 

$R_6 = 1V \times \frac{4.7 k\varOmega}{5V - 1V} = 1.175 k\varOmega$

---

$V_7 = 0V$

$V_6 = 5V$

$R_6 = 5V \times \frac{4.7 k\varOmega}{5V - 5V} = \infty k\varOmega$

---

$V_7 = 2.5V$

$V_6 = 2.5V$

$R_6 = 2.5V \times \frac{4.7 k\varOmega}{5V - 2.5V} = 4.7 k\varOmega$

---

$V_7 = 7V$

$V_6 = -2V$

$R_6 = -2V \times \frac{4.7 k\varOmega}{5V - (-2V)} = -1.3428 k\varOmega$

---

$I_{max} = \frac{V_{in}}{R_7} = \frac{5V}{4.7 k\varOmega} = 1.0638mA$

$I_{min} = 0A$

$I_{media} = \frac{I_{max} + I_{min}}{2} = \frac{I_{max}}{2} = \frac{1.0638mA}{2} = 0.5319mA$

 
---

$V_6 = 5V \times \frac{R_6}{R_6 + 4.7 k\varOmega}$

$R_6 = V_6 \times \frac{4.7 k\varOmega}{5V-V_6}$

---
Calculo de potencias

$P = I \times V$

$P = I^2 \times R$

Dado que la corriente máxima del circuito la calculamos en

$I_{max} = 1.0638mA$

$P_{max} = 1.0638mA(5V) = 5.319mW$

La potencia de la resistencia está dado por I