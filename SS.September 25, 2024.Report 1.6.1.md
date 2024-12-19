$3.3V \to 4095$

$\textrm{Voltaje de la fotoresistencia} \leftarrow \textrm{Valor entero leido}$

$\textrm{Voltaje de la fotoresistencia} = \frac{3.3V \times (\textrm{Valor entero leido})}{4095}$

Consideraremos el tiempo $17:46$ y su valor como el punto de origen, es decir que a todas las funciones consecuentes, se les debe restar este origen para obtener su valor respecto a este tiempo

$f(17:46) = f(0) = 0.1797142857 - 0.1797142857 = 0V$

$f(17:56) = f(10) = 0.1943516484V - 0.1797142857V = 0.0146373627V$

$f(18:00) = f(14) = 0.2472087912V - 0.1797142857V = 0.06749445055V$

> $f(18:10) = f(24)= 0.2935604396V - 0.1797142857V = 0.1138461539V$
>
> $f(10+14) =  0.0146373627V + 0.06749445055V = 0.0791318132V$

---

$\textrm{Valor medido por el ADC } = M$

$\textrm{Indice Resistencia fija } = 1$

$\textrm{Indice Fotoresistencia } = f$

Para $R_1 = 1M\varOmega$

$Max(M_f) = 3995$

$V_f = \frac{3.3V \times 3995}{4095} = 3.21V$

$V_1 = 3.3V - 3.21V = 0.08V$

$R_f = \frac{R_1 \times V_f}{V_1} = \frac{1M\varOmega \times 3.21V}{0.08V} = 40.125M\varOmega$

$40.125M\varOmega \approx 40,125k\varOmega \approx 40,125,000\varOmega$

Para $R_1 = 1k\varOmega$

$Min(M_f) = 100$

$V_f = \frac{3.3V \times 100}{4095} = 0.08V$

$V_1 = 3.3V - 0.08V = 3.21V$

$R_f = \frac{R_1 \times V_f}{V_1} = \frac{1k\varOmega \times 0.08V}{ 3.21V} = 0.02k\varOmega$

$0.02k\varOmega \approx 20\varOmega$
