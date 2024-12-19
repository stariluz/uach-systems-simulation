import math

def calc_system_params(K_w2, double_zeta_w, w2):
    # Frecuencia natural
    omega_n = math.sqrt(w2)
    
    # Factor de amortiguamiento
    zeta = double_zeta_w / (2 * omega_n)
    
    # Ganancia estática
    ganancia_estatica = K_w2 / w2
    
    # Determinación oscilatorio
    if zeta < 1:
        comportamiento = "Oscilatorio"
    elif zeta == 1:
        comportamiento = "Amortiguamiento crítico"
    else:
        comportamiento = "Sobreamortiguado (no oscilatorio)"
    
    # Resultados
    return omega_n, zeta, ganancia_estatica, comportamiento


K_w2 = 58737.82
double_zeta_w = 8069.07
w2 = 4633.67
omega_n, zeta, ganancia_estatica, comportamiento = calc_system_params(K_w2, double_zeta_w, w2)

# Resultados
print(f"Frecuencia natural (ωn): {omega_n:.2f} rad/s")
print(f"Factor de amortiguamiento (ζ): {zeta:.4f}")
print(f"Ganancia estática (K): {ganancia_estatica:.2f}")
print(f"Comportamiento: {comportamiento}")
