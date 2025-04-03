import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QPropertyAnimation, QRect
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

# Crear dos animaciones para el botón: una de entrada y otra de salida
ventana.animEnter = QPropertyAnimation(ventana.btnIniciar, b"geometry")
ventana.animEnter.setDuration(300)
ventana.animEnter.setStartValue(ventana.btnIniciar.geometry())
ventana.animEnter.setEndValue(QRect(ventana.btnIniciar.x()-5, ventana.btnIniciar.y()-5,
                                    ventana.btnIniciar.width()+10, ventana.btnIniciar.height()+10))

ventana.animLeave = QPropertyAnimation(ventana.btnIniciar, b"geometry")
ventana.animLeave.setDuration(300)
ventana.animLeave.setStartValue(QRect(ventana.btnIniciar.x()-5, ventana.btnIniciar.y()-5,
                                     ventana.btnIniciar.width()+10, ventana.btnIniciar.height()+10))
ventana.animLeave.setEndValue(ventana.btnIniciar.geometry())  # Restaurar tamaño original

# Vincular las animaciones a los eventos de entrada y salida del cursor
ventana.btnIniciar.enterEvent = lambda event: ventana.animEnter.start()
ventana.btnIniciar.leaveEvent = lambda event: ventana.animLeave.start()

# Mostrar la ventana
ventana.show()

sys.exit(app.exec())
