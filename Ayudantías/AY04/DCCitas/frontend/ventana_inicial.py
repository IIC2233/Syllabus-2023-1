import sys
from os.path import join
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal


class VentanaInicial(QWidget):
    senal_login = pyqtSignal(str)
    senal_abrir = pyqtSignal()


    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(300, 300, 500, 500)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('DCCitas')
        self.init_gui()


    def init_gui(self):
        layout = QVBoxLayout()

        self.logo = QLabel(self)
        self.logo.resize(100, 100)
        path_logo = join('frontend', 'imgs', 'logo1.png')
        print(path_logo)
        pixmap_logo = QPixmap(path_logo)
        self.logo.setPixmap(pixmap_logo)
        layout.addWidget(self.logo)
        layout.addStretch(1)

        self.texto = QLabel("Ingresa tu nombre de usuario", self)
        
        layout.addWidget(self.texto)
        layout.addStretch(1)

        self.input = QLineEdit(self)

        layout.addWidget(self.input)
        layout.addStretch(1)

        self.boton = QPushButton("Ingresar", self)
        self.boton.clicked.connect(self.login)

        layout.addWidget(self.boton)
        layout.addStretch(1)

        self.setLayout(layout)

    def mostrar(self):
        self.show()


    def login(self):
        usuario = self.input.text()
        self.senal_login.emit(usuario)


    def validacion(self, result):
        if result:
            print(result)
            self.hide()
            self.senal_abrir.emit()
        else:
            self.input.setText("")
            self.input.setPlaceholderText("Usuario Invalido")
