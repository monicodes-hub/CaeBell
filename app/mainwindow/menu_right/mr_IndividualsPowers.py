# LECTURA Y MOSTRAR POTENCIA EN FRAMES (mr_frame2 - mr_frame5)

from app.controllers.ports import set_pin_state, PORTS
from app.controllers.power import update_power
from PySide6.QtCore import QTimer, QObject, Signal
import threading

class PinsSignals(QObject):
    update_ui = Signal(float, int)

class LedController:
    """Controlar leds y actualiza potencia en UI."""
    
    def __init__(self, board, main_window, pin_name, label_widget, progress_widget):
        self.board = board
        self.main_window = main_window
        self.pin_name = pin_name
        self.label = label_widget
        self.progress = progress_widget
        self.pin_encendido = False

        # Estado inicial
        self.label.setText("0.00 W")
        self.progress.setValue(0)
        
        self.signals = PinsSignals()
        self.signals.update_ui.connect(self.update_widgets_slot)

        # Timer de actualización periódica
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_sampling)
    
    def update_widgets_slot(self, potencia, progreso):
        """Actualiza label y progress bar de forma segura."""
        self.label.setText(f"{potencia:.2f} W")
        self.progress.setValue(progreso)

    def start_sampling(self):
        """Lee la potencia actual y actualiza la UI."""
        if not self.pin_encendido:
            return

        def sampling_thread():
            try:
                powers = update_power()
                pin_key = PORTS[self.pin_name]["analog"]
                potencia = powers.get(pin_key, 0.0)

                print(f"[DEBUG] {self.pin_name} sampling -> PinKey: {pin_key}, Potencia: {potencia:.3f} W")

                valor_limitado = min(potencia, self.progress.maximum())
                progreso = int(round(valor_limitado))  # redondeo clásico
                
                self.signals.update_ui.emit(potencia, progreso)

            except Exception as e:
                print(f"[ERROR] {self.pin_name} sampling_thread: {e}")
                self.signals.update_ui.emit(0.00, 0)

        threading.Thread(target=sampling_thread).start()

    def toggle_led(self):
        """Enciende/apaga el pin y gestiona el timer."""
        try:
            self.pin_encendido = not self.pin_encendido
            set_pin_state(self.board, self.pin_name, self.pin_encendido)
            print(f"[DEBUG] set_pin_state({self.pin_name}) -> {'ON' if self.pin_encendido else 'OFF'}")

            if self.pin_encendido:
                # Lectura inmediata
                # self.start_sampling()-----
                # Segunda lectura rápida después de 200 ms (para estabilización)
                QTimer.singleShot(200, self.start_sampling)
                # Luego, lecturas periódicas cada 5 s
                self.timer.start(5000)
                return "on"
            else:
                self.timer.stop()
                self.label.setText("0.00 W")
                self.progress.setValue(0)
                return "off"

        except Exception as e:
            print(f"[ERROR] toggle_led({self.pin_name}): {e}")
            self.label.setText("Error")
            self.progress.setValue(0)
            return "error"