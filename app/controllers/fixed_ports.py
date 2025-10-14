# =============================
# CONFIGURACIÓN DE PINES FIJOS
# ==============================

# Diccionario de configuración de pines
PORTS = {
    "D8": {
        "digital": 8,   # Pin digital D8
        "analog": 0     # Pin analógico A0
    }
}

# Función para encender/apagar un pin digital
def set_pin_state(board, pin_name, state):
    """
    Enciende (True) o apaga (False) el pin digital asociado.
    """
    pin = PORTS[pin_name]["digital"]
    board.digital_write(pin, int(state))