import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.interface.mainwindow4_ui import Ui_MainWindow
from app.controllers.arduino_board import board
from app.mainwindow.main_body.mainbody_frame2 import manejar_boton_push
from app.mainwindow.menu_right.mr_IndividualsPowers import LedController
from app.controllers.power import initialize_analog_pins

# ---------------------------------------------
# Clase principal de la aplicación
# ---------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        super().__init__()

        # el método setupUi heredado del diseño, generará la interfaz gráfica
        self.setupUi(self)

        # Inicializar pines analógicos con callback
        initialize_analog_pins(board)

        # --- Crear controladores por botón/pin/UI ---
        self.luz_A2 = LedController(board, self, "D8", self.mr_frame2_c_label2, self.mr_frame2_b_progress_bar)
        self.luz_B2 = LedController(board, self, "D9", self.mr_frame3_c_label2, self.mr_frame3_b_progress_bar)
        self.luz_C2 = LedController(board, self, "D10", self.mr_frame4_c_label2, self.mr_frame4_b_progress_bar)
        self.luz_D2 = LedController(board, self, "D11", self.mr_frame5_c_label2, self.mr_frame5_b_progress_bar)

        # --- Vincular botones ---
        manejar_boton_push(self, self.luz_A2, "A2_pushbutton")
        manejar_boton_push(self, self.luz_B2, "B2_pushbutton")
        manejar_boton_push(self, self.luz_C2, "C2_pushbutton")
        manejar_boton_push(self, self.luz_D2, "D2_pushbutton")

        # Conectar funcionalidades de mb_frame3 (botones A1/B1/C1/D1)
        from app.mainwindow.main_body.mainbody_frame3 import attach_mb_frame3_handlers
        attach_mb_frame3_handlers(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())