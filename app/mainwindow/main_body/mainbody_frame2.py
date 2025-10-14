
from PySide6.QtGui import QColor

# -------------------------------------------------------------
# Conectar el botón A2_pushbutton para encender/apagar la luz
# y actualizar el borde según el estado
# -------------------------------------------------------------
def manejar_A2_pushbutton(window, luz_controller):
    """
    Conecta el botón A2_pushbutton para encender/apagar la luz y actualiza el borde según el estado.
    """
    def actualizar_borde(estado):
        if estado == "on":
            color = "green"
        elif estado == "off":
            color = "gray"
        elif estado == "error":
            color = "red"
        else:
            color = "gray"
        window.A2_pushbutton.setStyleSheet(f"border: 2px solid {color};")

    def on_click():
        try:
            luz_controller.toggle_luz()
        except Exception:
            actualizar_borde("error")
            return

        # Solo actualiza el color si no hay excepción
        if luz_controller.luz_encendida:
            actualizar_borde("on")
        else:
            actualizar_borde("off")

    window.A2_pushbutton.clicked.connect(on_click)
    actualizar_borde("off")