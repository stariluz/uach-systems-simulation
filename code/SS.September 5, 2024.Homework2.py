import numpy as np
import pandas as pd

# Crear los datos originales
data = {
    'V de salida (V)': [8.95, 8.91, 8.86, 8.81, 8.76, 8.71, 8.66, 8.61, 8.56, 8.51, 
                        8.46, 8.41, 8.35, 8.31, 8.27, 8.2, 8.14, 8.11, 8.07, 8.01, 7.94],
    'I en el diodo (mA)': [27.1, 27, 26.8, 26.7, 26.5, 26.4, 26.2, 26.1, 26, 25.8, 
                           25.6, 25.5, 25.3, 25.2, 25.1, 24.9, 24.7, 24.6, 24.5, 24.3, 24.1]
}

df = pd.DataFrame(data)

# Añadir ruido a los datos (ruido aleatorio pequeño con distribución normal)
ruido_voltaje = np.random.normal(0, 0.005, size=len(df))  # Ruido pequeño para voltaje
ruido_corriente = np.random.normal(0, 0.005, size=len(df))  # Ruido pequeño para corriente

# Aplicar el ruido a los datos
df['V de salida (V)'] = (df['V de salida (V)'] + ruido_voltaje).round(2)
df['I en el diodo (mA)'] = (df['I en el diodo (mA)'] + ruido_corriente).round(2)

# Mostrar los datos con ruido redondeados a 2 decimales
print(df)

# Si deseas guardarlo en un archivo CSV:
df.to_csv('mediciones_con_ruido_redondeado.csv', index=False)
