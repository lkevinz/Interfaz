import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

# Inicializar la app
app = QApplication(sys.argv)

# Cargar archivo .ui
ventana = loadUi("Login.ui")

# Restringir la redimensión de la ventana
ventana.setFixedSize(ventana.size())

# Cargar el archivo de estilos
with open("estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

# Mostrar la ventana
ventana.show()

sys.exit(app.exec())
