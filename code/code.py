# Constante de la resistencia en ohmios
resistencia = 1000  # 1 kΩ

# Voltaje inicial
voltaje_inicial = 0.1

# Número de valores a calcular
num_valores = 50

# Voltaje mínimo para que haya corriente
voltaje_minimo = 0.6

# Lista para almacenar los valores de corriente
corrientes = []

# Cálculo de la corriente usando la ley de Ohm (I = V / R)
for i in range(num_valores):
    voltaje = voltaje_inicial + i * 0.1
    if voltaje < voltaje_minimo:
        corriente = 0
    else:
        corriente = voltaje / resistencia
    corrientes.append(corriente)

# Mostrar los resultados
for idx, corriente in enumerate(corrientes):
    voltaje_actual = voltaje_inicial + idx * 0.1
    print(f"{corriente:.5f}")
