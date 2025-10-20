from PySide6.QtGui import QColor

# -------------------------------------------------------------
# Conectar el botón [X]_pushbutton para encender/apagar el pin
# y actualizar el borde según el estado
# -------------------------------------------------------------
def manejar_boton_push(window, led_controller, boton_nombre):
    """
    Conecta un botón push (A2/B2/C2/D2) a la lógica de LedController,
    actualizando el borde de color según el estado.
    """

    boton = getattr(window, boton_nombre)  # Obtiene el botón por su nombre (A2_pushbutton, etc.)

    def actualizar_borde(estado):
        if estado == "on":
            color = "green"
        elif estado == "off":
            color = "gray"
        elif estado == "error":
            color = "red"
        else:
            color = "gray"
        boton.setStyleSheet(f"border: 2px solid {color};")

    def on_click():
        try:
            estado = led_controller.toggle_led()  # Ejecuta el encendido/apagado
        except Exception:
            actualizar_borde("error")
            return

        actualizar_borde(estado)

    # Conecta el botón y establece el estado inicial
    boton.clicked.connect(on_click)
    actualizar_borde("off")