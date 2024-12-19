## Modelo matemático simple

### 1. Ecuación eléctrica de la armadura

La ecuación para el circuito de la armadura es:

$V = I_a R_a + L_a \frac{dI_a}{dt} + E_b$

donde:
- $V$ es el voltaje de alimentación ($5V$ en este caso).
- $I_a$ es la corriente en la armadura.
- $R_a$ es la resistencia de la armadura.
- $L_a$ es la inductancia de la armadura.
- $E_b$ es la fuerza contra-electromotriz (CEM) inducida.

La fuerza contra-electromotriz $E_b$ está dada por:

$E_b = K_e \omega$

donde:
- $K_e$ es la constante de fuerza electromotriz.
- $\omega$ es la velocidad angular del rotor en rad/s.

### 2. Ecuación de la dinámica del rotor (mecánica)

La dinámica rotacional del motor se describe mediante la segunda ley de Newton para el movimiento rotacional:

$J \frac{d\omega}{dt} = \tau_a - \tau_f - B \omega$

donde:
- $J$ es la inercia del rotor.
- $\frac{d\omega}{dt}$ es la aceleración angular del rotor.
- $\tau_a$ es el par generado por la armadura.
- $\tau_f$ es el par de fricción estática.
- $B$ es la fricción dinámica (par viscoso) que depende de la velocidad.

El par generado por la armadura $\tau_a$ se relaciona con la corriente de la armadura $I_a$ mediante:

$\tau_a = K_t I_a$

donde $K_t$ es la constante de par, que es generalmente igual a $K_e$ para motores DC ideales.

### Modelo completo del motor

Uniendo las ecuaciones, el modelo del motor se describe por el siguiente sistema de ecuaciones diferenciales:

1. **Ecuación eléctrica:**

$V = I_a R_a + L_a \frac{dI_a}{dt} + K_e \omega
$

2. **Ecuación mecánica:**

$J \frac{d\omega}{dt} = K_t I_a - \tau_f - B \omega
$

donde cada parámetro representa lo siguiente:
- **$V = 5 \, \text{V}$**: voltaje de alimentación.
- **$R_a = 1.5 \, \Omega$**: resistencia de la armadura.
- **$L_a = 0.2 \, \text{mH}$**: inductancia de la armadura.
- **$K_e = 0.015 \, \text{V} \cdot \text{s}/\text{rad}$**: constante de fuerza electromotriz.
- **$J = 0.002 \, \text{kg} \cdot \text{m}^2$**: inercia del rotor.
- **$B = 0.005 \, \text{N} \cdot \text{m} \cdot \text{s}/\text{rad}$**: fricción dinámica.
- **$\tau_f = 0.002 \, \text{N} \cdot \text{m}$**: par de fricción estática.

Este modelo puede usarse para simular el comportamiento del motor al aplicar diferentes voltajes y analizar cómo responde el rotor en términos de velocidad angular y corriente en la armadura.






























# Modelo matemático en el tiempo

Para obtener la función de transferencia de un motor de corriente continua (DC) y poder expresar su velocidad y posición angular en términos del modelo eléctrico, se sigue un procedimiento basado en la modelación matemática de sus componentes eléctricos y mecánicos.

### 1. Modelo matemático de un motor DC
Un motor DC tiene dos subsistemas que se modelan por separado: el circuito eléctrico (rotor y sus bobinas) y el sistema mecánico (rotación del eje).

#### 1.1 Ecuación del circuito eléctrico
El circuito eléctrico del motor DC sigue la Ley de Kirchhoff de voltaje:

$V_a(t) = R_a I_a(t)+ L_a \frac{dI_a(t)}{dt} + E_b(t)$

$V_a(t) = R_a I_a(t)+ L_a \frac{dI_a(t)}{dt} + K_e \omega(t)$

donde:
- $V(t)$ es el voltaje aplicado al motor.
- $L$ es la inductancia del devanado.
- $R$ es la resistencia del devanado.
- $I_a(t)$ es la corriente en el devanado.
- $E_b(t)$ es el voltaje de contraelectromotriz (CEM), dado por $E_b(t) = K_e \cdot \omega(t)$, donde $K_e$ es la constante de CEM y $\omega(t)$ es la velocidad angular.

#### 1.2 Ecuación del sistema mecánico
La ecuación del sistema mecánico está dada por la segunda ley de Newton aplicada al momento angular:

$J \frac{d\omega(t)}{dt} + b \omega(t) = T(t)$

$J \frac{d\omega(t)}{dt} = \tau_a(t) - \tau_f - B \omega(t)$

$\tau_a(t) = K_t I_a(t)$

$J \frac{d\omega(t)}{dt} = K_t I_a(t) - \tau_f - B \omega(t)$






# Modelo matematico en el tiempo corregido

### 1. Modelo matemático

#### 1.1 Ecuación del circuito eléctrico
La ecuación del circuito eléctrico en el motor DC sigue la Ley de Kirchhoff de voltaje y está dada por:

$V_a(t) = R_a I_a(t) + L_a \frac{dI_a(t)}{dt} + K_e \omega(t)$

donde:
- $V_a(t)$ es el voltaje aplicado al motor.
- $R_a$ es la resistencia del devanado del rotor.
- $L_a$ es la inductancia del devanado.
- $I_a(t)$ es la corriente que pasa por el devanado.
- $K_e$ es la constante de contraelectromotriz (CEM).
- $\omega(t)$ es la velocidad angular del rotor.

#### 1.2 Ecuación del sistema mecánico
La dinámica del rotor está dada por la ecuación de movimiento rotacional considerando la fricción y el amortiguamiento:

$J \frac{d\omega(t)}{dt} = K_t I_a(t) - \tau_f - B \omega(t)$

donde:
- $J$ es el momento de inercia del rotor.
- $K_t$ es la constante de torque del motor.
- $\tau_f$ es el torque de fricción constante (carga estática).
- $B$ es el coeficiente de fricción viscosa.
- $\omega(t)$ es la velocidad angular.

### 2. Obtención de la función de transferencia

Para obtener la función de transferencia, pasamos ambas ecuaciones al dominio de Laplace (asumiendo condiciones iniciales en cero).

#### 2.1 Transformación de la ecuación eléctrica
Aplicando la transformada de Laplace a la ecuación eléctrica:

$V_a(s) = R_a I_a(s) + L_a s I_a(s) + K_e \Omega(s)$

donde:
- $V_a(s)$ es la transformada de Laplace del voltaje aplicado.
- $I_a(s)$ es la transformada de Laplace de la corriente.
- $\Omega(s)$ es la transformada de Laplace de la velocidad angular.

#### 2.2 Transformación de la ecuación mecánica
Aplicando la transformada de Laplace a la ecuación mecánica:

$J s \Omega(s) = K_t I_a(s) - \tau_f - B \Omega(s)$

Para simplificar el análisis, suponemos que $\tau_f$ es despreciable o se compensa, por lo que podemos escribir la ecuación como:

$(J s + B) \Omega(s) = K_t I_a(s)$

#### 3. Función de transferencia de velocidad angular

Para encontrar la función de transferencia $\frac{\Omega(s)}{V_a(s)}$, despejamos $I_a(s)$ de la ecuación eléctrica y lo sustituimos en la ecuación mecánica.

1. **Despejamos $I_a(s)$ en términos de $V_a(s)$ y $\Omega(s)$ en la ecuación eléctrica:**

   $   I_a(s) = \frac{V_a(s) - K_e \Omega(s)}{R_a + L_a s}
$

2. **Sustitución de $I_a(s)$ en la ecuación mecánica:**

   $   (J s + B) \Omega(s) = K_t \frac{V_a(s) - K_e \Omega(s)}{R_a + L_a s}
$

3. **Reorganización para despejar $\Omega(s)$:**

   Multiplicamos ambos lados por $R_a + L_a s$ para eliminar el denominador:

   $   (J s + B)(R_a + L_a s) \Omega(s) = K_t V_a(s) - K_t K_e \Omega(s)
$

4. **Factorizamos $\Omega(s)$:**

   $   \left[ (J s + B)(R_a + L_a s) + K_t K_e \right] \Omega(s) = K_t V_a(s)
$

5. **Expresión final de la función de transferencia de velocidad angular:**

   $\frac{\Omega(s)}{V_a(s)} = \frac{K_t}{(J s + B)(R_a + L_a s) + K_t K_e}$

#### 4. Función de transferencia de posición angular

La posición angular $\theta(t)$ es la integral de la velocidad angular $\omega(t)$. En el dominio de Laplace, esto significa que:

$\Theta(s) = \frac{\Omega(s)}{s}$

Por lo tanto, la función de transferencia de posición angular respecto al voltaje aplicado es:

$\frac{\Theta(s)}{V_a(s)} = \frac{\Omega(s)}{s V_a(s)} = \frac{K_t}{s \left( (J s + B)(R_a + L_a s) + K_t K_e \right)}$

### 5. Interpretación

- **Función de transferencia de velocidad angular** $\frac{\Omega(s)}{V_a(s)}$: esta función te permite obtener la respuesta de la velocidad angular del motor en función del voltaje aplicado.
- **Función de transferencia de posición angular** $\frac{\Theta(s)}{V_a(s)}$: esta función describe la respuesta de la posición angular en función del voltaje aplicado.

Estas funciones de transferencia pueden utilizarse para diseñar un controlador o para simular la respuesta del motor en software como MATLAB o Simulink.






$\frac{\Omega(s)}{V_a(s)} = \frac{K_t}{(J s + B)(R_a + L_a s) + K_t K_e}$

$\frac{\Theta(s)}{V_a(s)} = \frac{K_t}{s \left( (J s + B)(R_a + L_a s) + K_t K_e \right)}$

| Parámetro                   | Símbolo        | Valor ajustado                                         |
| --------------------------- | -------------- | ------------------------------------------------------ |
| Resistencia de armadura     | \( R_a \)      | \( 1 \, \Omega \)                                      |
| Inductancia de armadura     | \( L_a \)      | \( 0.5 \, \text{mH} \)                                 |
| Masa del rotor              | \( M \)        | \( 18 \, \text{g} \)                                   |
| Inercia del rotor           | \( J \)        | \( 2 \times 10^{-6} \, \text{kg} \cdot \text{m}^2 \)   |
| Constante de torque/FEM     | \( K_t, K_e \) | \( 0.025 \, \text{Nm/A} \)                             |
| Fricción viscosa            | \( B \)        | \( 2 \times 10^{-6} \, \text{Nm} \cdot \text{s/rad} \) |
| Torque de fricción estática | \( \tau_f \)   | \( 0.0001 \, \text{Nm} \)                              |

$\frac{\Omega(s)}{V_a(s)} = \frac{0.025 \, \text{Nm/A}}{((2 \times 10^{-6} \, \text{kg} \cdot \text{m}^2) s + 2 \times 10^{-6} \, \text{Nm} \cdot \text{s/rad})(1 \, \Omega + (0.5 \, \text{mH}) s) + (0.025 \, \text{Nm/A})(0.025 \, \text{Nm/A})}$

$\frac{\Theta(s)}{V_a(s)} = \frac{0.025 \, \text{Nm/A}}{s \left( ((2 \times 10^{-6} \text{kg} \cdot \text{m}^2) s + 2 \times 10^{-6} \, \text{Nm} \cdot \text{s/rad})(1 \, \Omega + (0.5 \, \text{mH}) s) + (0.025 \, \text{Nm/A})(0.025 \, \text{Nm/A}) \right)}$




