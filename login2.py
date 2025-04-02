from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 412)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(147, 255, 215);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(140, 170, 141, 22))
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.UpArrowCursor))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.Iniciar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Iniciar.setGeometry(QtCore.QRect(160, 230, 111, 41))
        self.Iniciar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WhatsThisCursor))
        self.Iniciar.setStyleSheet("background-color: rgb(233, 215, 255);")
        self.Iniciar.setCheckable(False)
        self.Iniciar.setAutoDefault(False)
        self.Iniciar.setDefault(True)
        self.Iniciar.setFlat(False)
        self.Iniciar.setObjectName("Iniciar")
        self.Usuario = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(140, 110, 141, 22))
        self.Usuario.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.UpArrowCursor))
        self.Usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Usuario.setObjectName("Usuario")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio de sesión"))
        self.label.setText(_translate("MainWindow", "Login ERP"))
        self.Iniciar.setText(_translate("MainWindow", "Iniciar sesión"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())