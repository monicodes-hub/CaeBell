### PROGRAMACIÓN PARA DAR FUNCIONALIDADES AL LOG, FILE EXPLORER, APPS & SETTINGS ###

import os
import subprocess
from pathlib import Path
from datetime import datetime

from PySide6.QtWidgets import (
    QMessageBox, QFileDialog, QDialog, QVBoxLayout, QTextEdit, QPushButton,
    QDialogButtonBox, QWidget, QInputDialog
)
from PySide6.QtCore import Qt

def attach_mb_frame3_handlers(window: QWidget):
    """
    Conectar handlers para los botones dentro de mb_frame3.
    Llamar a esta función después de `self.setupUi(self)` en MainWindow.
    """
    # Acceso directo a los widgets según ui generada por pyuic6
    try:
        a_btn = window.A1_pushButton
        b_btn = window.B1_pushButton
        c_btn = window.C1_pushButton
        d_btn = window.D1_pushButton
    except AttributeError:
        # Si los nombres no existen, avisar y salir
        QMessageBox.warning(window, "Handlers", "No se encontraron los botones A1/B1/C1/D1 en la UI.")
        return

    a_btn.clicked.connect(lambda: _handle_log(window))
    b_btn.clicked.connect(lambda: _open_pictures_folder(window))
    c_btn.clicked.connect(lambda: _open_apps_folder_and_run(window))
    d_btn.clicked.connect(lambda: _settings_placeholder(window))


# ---------- Helpers ----------
def _prompt_multiline(parent, title="Entrada", label="Texto"):
    """Dialogo simple para entrada multilínea (OK/Cancelar). Devuelve (text, accepted)."""
    dlg = QDialog(parent)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout(dlg)
    txt = QTextEdit(dlg)
    layout.addWidget(txt)
    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=dlg)
    layout.addWidget(buttons)
    accepted = {"val": False}
    def _ok():
        accepted["val"] = True
        dlg.accept()
    def _cancel():
        dlg.reject()
    buttons.accepted.connect(_ok)
    buttons.rejected.connect(_cancel)
    if dlg.exec_() == QDialog.DialogCode.Accepted and accepted["val"]:
        return txt.toPlainText(), True
    return "", False


def _show_text_file_dialog(parent, path: Path):
    """Muestra contenido del archivo en diálogo con opción de abrir en editor por defecto."""
    dlg = QDialog(parent)
    dlg.setWindowTitle(f"Ver log - {path.name}")
    dlg.setModal(True)
    layout = QVBoxLayout(dlg)
    txt = QTextEdit(dlg)
    txt.setReadOnly(True)
    try:
        txt.setPlainText(path.read_text(encoding="utf-8"))
    except Exception as e:
        txt.setPlainText(f"Error leyendo el archivo: {e}")
    layout.addWidget(txt)

    btn_open = QPushButton("Abrir en editor por defecto", dlg)
    def _open_ext():
        try:
            os.startfile(str(path))
        except Exception as e:
            QMessageBox.warning(parent, "Error", f"No se pudo abrir externamente:\n{e}")
    btn_open.clicked.connect(_open_ext)
    layout.addWidget(btn_open)
    dlg.resize(700, 500)
    dlg.exec_()


# ---------- Feature A: Logs ----------
def _handle_log(parent):
    """
    Opciones:
    - Crear nuevo log (no sobrescribe)
    - Añadir a existente
    - Ver logs existentes
    Logs en carpeta 'logs' dentro del proyecto (same folder que este archivo).
    """
    base_dir = Path(__file__).resolve().parent  # carpeta del proyecto (bn_project)
    logs_dir = base_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Construir lista de opciones
    existing = sorted(logs_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)
    options = ["Crear nuevo", "Añadir a existente", "Ver existente"]
    choice, ok = QInputDialog.getItem(parent, "Log - opción", "Selecciona acción:", options, 0, False)
    if not ok or not choice:
        return

    if choice == "Crear nuevo":
        text, accepted = _prompt_multiline(parent, "Nuevo log", "Escribe el contenido del nuevo log:")
        if not accepted:
            return
        name = datetime.now().strftime("log_%Y%m%d_%H%M%S.txt")
        path = logs_dir / name
        path.write_text(text, encoding="utf-8")
        QMessageBox.information(parent, "Log creado", f"Log creado en:\n{path}")
        _show_text_file_dialog(parent, path)
        return

    if choice == "Añadir a existente":
        if not existing:
            QMessageBox.information(parent, "Sin logs", "No hay logs existentes para añadir. Crea uno nuevo primero.")
            return
        # Usar diálogo de selección de archivo
        start = str(logs_dir)
        file_path, _ = QFileDialog.getOpenFileName(parent, "Selecciona log para añadir", start, "Text files (*.txt);;All files (*)")
        if not file_path:
            return
        add_text, accepted = _prompt_multiline(parent, "Añadir a log", "Texto a añadir:")
        if not accepted:
            return
        p = Path(file_path)
        with p.open("a", encoding="utf-8") as f:
            f.write("\n\n---\n")
            f.write(f"{datetime.now().isoformat()}\n")
            f.write(add_text)
        QMessageBox.information(parent, "Añadido", f"Texto añadido a:\n{p}")
        _show_text_file_dialog(parent, p)
        return

    if choice == "Ver existente":
        if not existing:
            QMessageBox.information(parent, "Sin logs", "No hay logs para ver.")
            return
        start = str(logs_dir)
        file_path, _ = QFileDialog.getOpenFileName(parent, "Selecciona log para ver", start, "Text files (*.txt);;All files (*)")
        if not file_path:
            return
        p = Path(file_path)
        if p.exists():
            _show_text_file_dialog(parent, p)
        else:
            QMessageBox.warning(parent, "No encontrado", "El archivo seleccionado no existe.")


# ---------- Feature B: Abrir carpeta de Imágenes ----------
def _open_pictures_folder(parent):
    """
    Abre el Explorador en la carpeta Pictures del usuario.
    Intenta rutas comunes (Pictures, Imágenes, Mis imágenes). Si no encuentra, usa home.
    """
    candidates = [
        Path.home() / "Pictures",
        Path.home() / "Imágenes",
        Path.home() / "Mis imágenes",
    ]
    found = None
    for p in candidates:
        if p.exists():
            found = p
            break
    if not found:
        found = Path.home()
    try:
        subprocess.run(["explorer", str(found)])
    except Exception as e:
        QMessageBox.warning(parent, "Error", f"No se pudo abrir el Explorador:\n{e}")


# ---------- Feature C: Abrir apps desde Program Files ----------
def _open_apps_folder_and_run(parent):
    """
    Abre selector para que el usuario escoja un .exe o .lnk (ruta inicial: Desktop del usuario).
    Al aceptar, lanza ese ejecutable/atajo con os.startfile.
    """
    # Intentar Desktop en inglés/español; si no existe, fallback a Program Files o home
    desktop_candidates = [
        Path.home() / "Desktop",
        Path.home() / "Escritorio"
    ]
    start_dir = None
    for d in desktop_candidates:
        if d.exists():
            start_dir = d
            break

    if start_dir is None:
        # fallback a Program Files si existe, sino al home
        pf = os.environ.get("ProgramFiles", r"C:\Program Files")
        pf_path = Path(pf)
        start_dir = pf_path if pf_path.exists() else Path.home()

    start = str(start_dir)
    file_filter = "Programs (*.exe *.lnk);;All files (*)"
    file_path, _ = QFileDialog.getOpenFileName(parent, "Selecciona programa para abrir", start, file_filter)
    if not file_path:
        return
    try:
        os.startfile(file_path)
    except Exception as e:
        QMessageBox.warning(parent, "Error al abrir", f"No se pudo abrir el programa:\n{e}")


# ---------- Feature D: Settings (placeholder) ----------
def _settings_placeholder(parent):
    """
    Placeholder para Settings. Actualmente no realiza cambios.
    En el futuro se deberá crear un Widget/ventana para configurar opciones (persistencia).
    """
    QMessageBox.information(parent, "Settings", "La sección de settings está pendiente de implementar.")

# NOTA IMPORTANTE/TODO:
# - La sección "Settings" (D1_pushButton) es un placeholder. Pendiente:
#   * Crear un QWidget o QDialog específico para opciones/ajustes.
#   * Definir mecanismo de persistencia (archivo JSON/INI en carpeta del proyecto o uso del registro).
#   * Conectar ese widget desde _settings_placeholder para mostrar y guardar cambios.

