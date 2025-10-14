import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.interface.mainwindow4_ui import Ui_MainWindow
from app.controllers.arduino_board import board
from app.mainwindow.main_body.mainbody_frame2 import manejar_A2_pushbutton
from app.mainwindow.menu_right.mr_frame1 import LuzController

# ---------------------------------------------
# Clase principal de la aplicación
# ---------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        super().__init__()

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)

        # Inicializamos el controlador de luz con la instancia de board
        self.luz_controller = LuzController(board, self)

        # Conecta el botón "A2_pushbutton" al método toggle_luz
        manejar_A2_pushbutton(self, self.luz_controller)

        # Conectar funcionalidades de mb_frame3 (botones A1/B1/C1/D1)
        from app.mainwindow.main_body.mainbody_frame3 import attach_mb_frame3_handlers
        attach_mb_frame3_handlers(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

