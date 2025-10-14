
# --- CONSTANTES BASE ---
V_REF = 5.0         # Voltaje de referencia del ADC
V_SUPPLY = 12.0      # Voltaje de alimentación del circuito
R_SHUNT = 0.22       # Valor del resistor shunt (ohmios)

# --- PARÁMETROS DE CALIBRACIÓN ---
AMP_GAIN = 0.5       # Factor de ganancia del amplificador (ajustar para calibrar)
AMP_OFFSET = 0.0     # Offset en voltios, si el sensor tiene desplazamiento

# -------------------------------------------------------------
# Cálculo de potencia a partir del valor analógico leído
# -------------------------------------------------------------
def calcular_potencia(analog_value, r_shunt=R_SHUNT, v_ref=V_REF,
                      v_supply=V_SUPPLY, amp_gain=AMP_GAIN, amp_offset=AMP_OFFSET):
    """
    Calcula la potencia (W) a partir del valor analógico leído.

    Fórmulas:
        V_meas = (analog_value / 1023) * V_REF
        V_shunt = (V_meas - AMP_OFFSET) / AMP_GAIN
        I = V_shunt / R_SHUNT
        P = V_SUPPLY * I
    """
    try:
        # Conversión ADC a voltaje medido
        v_meas = (analog_value / 1023.0) * v_ref

        # Compensación de ganancia y offset
        v_shunt = (v_meas - amp_offset) / amp_gain

        # Corriente y potencia
        current = v_shunt / r_shunt
        potencia = v_supply * current

        # Filtrar valores anómalos
        if potencia < 0 or potencia != potencia:
            potencia = 0.0

        # Devuelve potencia y valores intermedios para depuración
        return {
            "analog": analog_value,
            "v_meas": v_meas,
            "v_shunt": v_shunt,
            "current": current,
            "power": potencia
        }

    except Exception as e:
        print(f"Error en calcular_potencia: {e}")
        return {
            "analog": 0,
            "v_meas": 0,
            "v_shunt": 0,
            "current": 0,
            "power": 0
        }