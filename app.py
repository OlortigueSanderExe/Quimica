
import streamlit as st
import numpy as np
from scipy.stats import weibull_min

# Título de la app
st.title("Calculadora de Energía Eólica")

# Ingreso de datos
forma_weibull = st.number_input("Parámetro de forma (Weibull)", min_value=1.0, max_value=3.0, value=2.0)
escala_weibull = st.number_input("Parámetro de escala (Weibull)", min_value=1.0, value=8.0)
velocidad_viento_promedio = st.number_input("Velocidad promedio del viento (m/s)", min_value=1.0, value=6.0)

# Función de cálculo de energía eólica
def calcular_energia(forma_weibull, escala_weibull, velocidad_viento_promedio):
    velocidades_viento = np.linspace(0, 25, 100)  # 100 puntos de velocidad de 0 a 25 m/s
    distribucion_viento = weibull_min.pdf(velocidades_viento, forma_weibull, scale=escala_weibull)

    def curva_potencia(velocidad_viento):
        if velocidad_viento < 3:
            return 0
        elif velocidad_viento < 15:
            return 0.5 * velocidad_viento**3
        elif velocidad_viento < 25:
            return 1.0 * velocidad_viento**3
        else:
            return 0

    potencia_generada = np.array([curva_potencia(v) for v in velocidades_viento])
    energia_anual = np.trapz(potencia_generada * distribucion_viento, velocidades_viento) * 24 * 365
    return energia_anual

# Botón para calcular la energía
if st.button("Calcular Energía"):
    energia = calcular_energia(forma_weibull, escala_weibull, velocidad_viento_promedio)
    st.write(f"Energía estimada generada por año: {energia:.2f} kWh")

