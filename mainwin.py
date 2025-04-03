import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
import Style.animation as animation  # Importamos el módulo de animaciones

# Inicializar la app
app = QApplication(sys.argv)

# Cargar archivo .ui
ventana = loadUi("Login.ui")

# Restringir la redimensión de la ventana
ventana.setFixedSize(ventana.size())

# Cargar el archivo de estilos
with open("Style/estilos.qss", "r") as file:
    app.setStyleSheet(file.read())

# Vincular las animaciones correctamente
ventana.btnIniciar.enterEvent = lambda event: ventana.animEnter.start()
ventana.btnIniciar.leaveEvent = lambda event: ventana.animLeave.start()

# Definir y almacenar las animaciones para evitar que se destruyan
ventana.animEnter = animation.animate_button(ventana.btnIniciar)
ventana.animLeave = animation.reset_button(ventana.btnIniciar)

# Mostrar la ventana
ventana.show()

sys.exit(app.exec())
