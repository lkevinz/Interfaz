# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(417, 423)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnIniciar = QPushButton(self.centralwidget)
        self.btnIniciar.setObjectName(u"btnIniciar")
        self.btnIniciar.setEnabled(True)
        self.btnIniciar.setGeometry(QRect(120, 260, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic"])
        font1.setPointSize(10)
        self.btnIniciar.setFont(font1)
        self.lineEditPasswd = QLineEdit(self.centralwidget)
        self.lineEditPasswd.setObjectName(u"lineEditPasswd")
        self.lineEditPasswd.setGeometry(QRect(100, 200, 201, 41))
        self.lineEditPasswd.setMaximumSize(QSize(300, 100))
        self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditUsuario = QLineEdit(self.centralwidget)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")
        self.lineEditUsuario.setGeometry(QRect(100, 140, 201, 41))
        self.lineEditUsuario.setMaximumSize(QSize(300, 100))
        self.lineEditUsuario.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(100, 90, 201, 31))
        self.titulo.setFont(font)
        self.titulo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.titulo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titulo.setTextFormat(Qt.TextFormat.AutoText)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.btnIniciar.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"LOGIN ERP", None))
    # retranslateUi

