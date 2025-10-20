import threading
from app.controllers import ports as p

V_ENTRADA = 12.0    # Voltaje de entrada fijo (V)
R_SHUNT = 0.2205    # Resistencia media del shunt (Ω)

voltajes = {}

def analog_callback(data):
    """Callback para leer el valor de los pines analógicos."""
    global voltajes
    try:
        pin = data[1]       # Número del pin analógico
        valor = data[2]     # Valor leído (0–1023)
        voltaje = (valor / 1023.0) * V_ENTRADA
        voltajes[f"A{pin}"] = voltaje
    except Exception as e:
        print(f"[ERROR] analog_callback: {e}")

def update_voltage():
    """Devuelve el voltaje leído en cada pin analógico."""
    return voltajes

def update_current():
    """Devuelve la corriente estimada en cada pin analógico (I = Vshunt / Rshunt)."""
    corrientes = {}
    for pin, voltage in voltajes.items():
        corriente = voltage / R_SHUNT if voltage > 0.02 else 0.0
        corrientes[pin] = corriente
    return corrientes

def update_power():
    """Devuelve la potencia estimada en cada pin analógico (P = Ventrada * Ishunt)."""
    powers = {}
    corrientes = update_current()

    for pin, corriente in corrientes.items():
        potencia = V_ENTRADA * corriente
        powers[pin] = potencia if potencia >= 2.0 else 0.0  # Ignorar ruido o impedancia
    return powers

def initialize_analog_pins(board):
    """Configura los pines analógicos A0 a A5 con el callback para lectura."""
    for pin in p.AnalogPins:
        try:
            board.set_pin_mode_analog_input(pin, callback=analog_callback)
        except Exception as e:
            print(f"[ERROR] initialize_analog_pins({pin}): {e}")