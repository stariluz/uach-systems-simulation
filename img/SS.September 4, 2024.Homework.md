### 1)
### 2)

La ecuación típica de la corriente en un diodo sigue la ley de Shockley, que tiene la forma:

$I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)$

Donde:
- $I$ es la corriente en el diodo.
- $I_s$ es la corriente de saturación.
- $V$ es el voltaje de entrada.
- $n$ es el factor de idealidad del diodo (usualmente entre 1 y 2).
- $V_T$ es la tensión térmica ($V_T \approx 26 \, \text{mV}$ a temperatura ambiente).
- $e$ es la constante de Euler.

Entonces vamos a ajustar una función exponencial que relacione la corriente en el diodo con el voltaje de entrada.

Voy a intentar ajustar una función exponencial similar a los datos que me proporcionaste y luego calcularé el error. ¡Voy a proceder!

El ajuste exponencial no fue exitoso debido a un problema de desbordamiento numérico al calcular la función exponencial para valores altos de voltaje, lo que sugiere que los parámetros iniciales pueden no ser adecuados o que el rango de los datos podría requerir un enfoque diferente para ajustarlos.

Voy a intentar nuevamente ajustando los valores iniciales y escalando los datos para evitar este desbordamiento.

El ajuste exponencial ha sido más exitoso esta vez. Los parámetros ajustados son:

- $I_s \approx 1.79 \times 10^{-8} \, \mu A$
- $n \approx 11.25$
El error cuadrático medio (RMSE) del ajuste es de aproximadamente $30.53 \, \mu A$ lo que indica una diferencia media entre los valores ajustados y los valores reales de corriente.

¿Te gustaría continuar con algún análisis adicional o ajustar otra función?


Para completar tu informe, te explico los pasos que debes seguir para la **superposición de la linealidad** y la **construcción de la función**, que son dos de los puntos clave.

### 1. Superposición de la Linealidad

La superposición de la linealidad es un método que verifica si la función ajustada es lineal en diferentes rangos del gráfico. Esto es útil cuando se estudia la relación entre el voltaje de entrada y la corriente en un diodo, ya que puede ser lineal a bajos niveles de voltaje (en la zona de corte) y exponencial en otros rangos (zona activa).

**Pasos para realizar la superposición de la linealidad:**
- **Dividir la curva ajustada en segmentos**: Identifica partes de la curva donde los datos parecen más lineales (como en la zona donde la corriente es cero, o donde hay un crecimiento lineal pequeño).
- **Superponer líneas rectas**: Añade rectas en el gráfico que mejor se ajusten a estos segmentos. Esto se puede hacer con regresión lineal en estos rangos.
- **Compara la linealidad**: Comprueba qué tan bien se ajustan estas líneas rectas a la curva de la función ajustada.

Esto puede ayudarte a ver cómo el comportamiento lineal de ciertos segmentos cambia a un comportamiento no lineal más pronunciado, que es esperado en los diodos.

### 2. Construcción de la Función

La construcción de la función implica derivar la ecuación a partir de los datos. En tu caso, has mencionado que esperas que sea una función exponencial, lo cual es común para los diodos. Aquí está el proceso para construir la función:

**Pasos para construir la función:**
1. **Seleccionar el modelo teórico**: Para los diodos, la corriente sigue una ecuación exponencial como la que mencioné antes:
   \[
   I = I_s \left( e^{\frac{V}{n V_T}} - 1 \right)
   \]
   Donde \( V_T \) es la tensión térmica (aproximadamente 26 mV a temperatura ambiente), \( I_s \) es la corriente de saturación, y \( n \) es el factor de idealidad.

2. **Ajuste de la curva**: Utiliza los datos experimentales para ajustar los parámetros \( I_s \) y \( n \). En el ajuste que realizamos, obtuvimos \( I_s \approx 1.79 \times 10^{-8} \) y \( n \approx 11.25 \).

3. **Validar la función ajustada**: Superpone la curva ajustada con los datos originales para ver qué tan bien encajan, lo que te permitirá validar visualmente la función.

4. **Error de ajuste**: Calcula el error (como el RMSE que obtuvimos antes) para cuantificar la calidad del ajuste.

### Método para medir el error de ajuste

Puedes utilizar el **Error Cuadrático Medio (RMSE)**, que es la medida de ajuste más común. El RMSE te da una idea de cuánto, en promedio, se desvían los valores ajustados de los valores observados.

La fórmula es:

$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (I_{\text{real}} - I_{\text{ajustado}})^2}$

Donde  $I_{\text{real}}$ son los valores originales de corriente y  $I_{\text{ajustado}}$ son los valores que genera la función ajustada.

---

¿Te gustaría que elabore más en alguno de estos puntos o que profundice en los cálculos para la resistencia?