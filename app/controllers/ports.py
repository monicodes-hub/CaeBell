# ==============================================
# CONFIGURACIÓN DE PINES DIGITALES Y ANALÓGICOS
# ==============================================

# Diccionario de configuración de pines
PORTS = {
    "D8": {"digital": 8, "analog": "A0"},
    "D9": {"digital": 9, "analog": "A1"},
    "D10": {"digital": 10, "analog": "A2"},
    "D11": {"digital": 11, "analog": "A3"},
    
    # Agregar pines con función PWM calentadores
    "D5": {"digital": 5, "analog": "A4"},
    "D3": {"digital": 3, "analog": "A5"},
}

# Pines analógicos fijos (A0–A5)
AnalogPins = [0, 1, 2, 3, 4, 5]


def set_pin_state(board, pin_name, state):
    """
    Enciende o apaga un pin digital del Arduino.
    board: instancia de la placa (de arduino_board.py)
    pin_name: nombre lógico del pin (ej. "D8")
    state: True para encender, False para apagar
    """
    try:
        pin_digital = PORTS[pin_name]["digital"]
        value = 1 if state else 0
        board.digital_write(pin_digital, value)
        print(f"[DEBUG] set_pin_state({pin_name}) -> {'ON' if state else 'OFF'}")
    except Exception as e:
        print(f"[ERROR] set_pin_state({pin_name}): {e}")


