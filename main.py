import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.interface.mainwindow4_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        super().__init__()

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)

        # Conectar funcionalidades de mb_frame3 (botones A1/B1/C1/D1)
        from app.mainwindow.main_body.mainbody_frame3 import attach_mb_frame3_handlers
        attach_mb_frame3_handlers(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())