from app.controllers.fixed_ports import set_pin_state, PORTS
from app.controllers.power import calcular_potencia, R_SHUNT
from PySide6.QtCore import QTimer
import threading

# -------------------------------------------------------------
# Controlador de la luz y gestión de lecturas periódicas
# -------------------------------------------------------------
class LuzController:
    def __init__(self, board, main_window):
        self.board = board
        self.main_window = main_window
        self.pin_name = "D8"
        self.luz_encendida = False

        # Inicializa la UI
        try:
            self.main_window.mr_frame2_c_label2.setText("0.00 W")
            self.main_window.mr_frame2_b_progress_bar.setValue(0)
        except Exception:
            pass

        # Timer cada 5 minutos (300000 ms)
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_sampling)

        # Control de muestras
        self.sample_values = []
        self.sampling_active = False
        self.num_samples = 10


    def start_sampling(self):
        """Inicia la toma de muestras del pin analógico."""
        if not self.luz_encendida or self.sampling_active:
            return

        self.sampling_active = True
        self.sample_values = []
        analog_pin = PORTS[self.pin_name]["analog"]

        def analog_callback(data):
            """Recibe datos analógicos desde Telemetrix."""
            try:
                if isinstance(data, (list, tuple)):
                    if len(data) == 2:
                        analog_value = data[1]
                    elif len(data) >= 3:
                        analog_value = data[2]
                    else:
                        analog_value = 0
                else:
                    analog_value = 0

                self.sample_values.append(float(analog_value))

                # Si ya hay suficientes muestras, procesamos
                if len(self.sample_values) >= self.num_samples:
                    self.finish_sampling(analog_pin)

            except Exception as e:
                print("Error en callback analógico:", e)

        try:
            self.board.set_pin_mode_analog_input(analog_pin, callback=analog_callback)
        except Exception as e:
            print("Error al configurar lectura analógica:", e)
            self.main_window.mr_frame2_c_label2.setText("Error")
            self.main_window.mr_frame2_b_progress_bar.setValue(0)
            self.sampling_active = False


    def finish_sampling(self, analog_pin):
        """Procesa las muestras, calcula potencia y actualiza UI."""
        try:
            # Desactivar reportes continuos
            try:
                if hasattr(self.board, "disable_analog_reporting"):
                    self.board.disable_analog_reporting(analog_pin)
                else:
                    self.board.set_pin_mode_analog_input(analog_pin)
            except Exception as e:
                print("Warning: no se pudo desactivar reporting:", e)

            # Calcular promedio
            if not self.sample_values:
                analog_avg = 0
            else:
                analog_avg = sum(self.sample_values) / len(self.sample_values)

            # --- Calcular potencia (usa power.py) ---
            datos = calcular_potencia(analog_avg, R_SHUNT)
            potencia_w = datos["power"]

            # --- Actualiza UI ---
            try:
                self.main_window.mr_frame2_c_label2.setText(f"{potencia_w:.2f} W")
                self.main_window.mr_frame2_b_progress_bar.setValue(
                    int(min(potencia_w, self.main_window.mr_frame2_b_progress_bar.maximum()))
                )
            except Exception as e:
                print("Error actualizando UI:", e)

            # --- Consola ---
            print(
                f"[LECTURA] Luz {'ON' if self.luz_encendida else 'OFF'} | "
                f"Analog Avg: {datos['analog']:.2f} | "
                f"V_meas: {datos['v_meas']:.4f} V | "
                f"V_shunt: {datos['v_shunt']:.4f} V | "
                f"I: {datos['current']:.4f} A | "
                f"Potencia: {datos['power']:.3f} W"
            )

        finally:
            self.sampling_active = False
            self.sample_values = []


    def toggle_luz(self):
        """Cambia el estado de la luz y gestiona lecturas periódicas."""
        try:
            self.luz_encendida = not self.luz_encendida
            set_pin_state(self.board, self.pin_name, self.luz_encendida)

            if not self.luz_encendida:
                # Apagado
                try:
                    self.timer.stop()
                except Exception:
                    pass
                self.main_window.mr_frame2_c_label2.setText("0.00 W")
                self.main_window.mr_frame2_b_progress_bar.setValue(0)
                print("[LECTURA] Luz OFF | Potencia: 0.00 W")
                return "off"

            else:
                # Encendido
                threading.Thread(target=self.start_sampling).start()
                self.timer.start(5 * 60 * 1000)  # cada 5 min
                return "on"

        except Exception as e:
            print(f"Error en toggle_luz: {e}")
            self.main_window.mr_frame2_c_label2.setText("Error")
            self.main_window.mr_frame2_b_progress_bar.setValue(0)
            return "error"