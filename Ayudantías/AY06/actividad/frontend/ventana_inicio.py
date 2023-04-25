from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

import parametros as p


window_name_main, base_class_main = uic.loadUiType(p.VENTANA_INICIO)

window_name_error, base_class_error = uic.loadUiType(p.VENTANA_ERROR)


class VentanaInicio(window_name_main, base_class_main):
    # DEBES MODIFICAR ESTA CLASE

    senal_verificar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logo.setPixmap(QPixmap(p.LOGO_INICIO))
        self.logo.setScaledContents(True)
        self.logo.setAttribute(Qt.WA_TranslucentBackground)
        self.fondo.setPixmap(QPixmap(p.FONDO))
        self.fondo.setScaledContents(True)

        # PUEDES MODIFICAR DESDE ESTA LÍNEA
        self.boton_comenzar.clicked.connect(self.verificar_usuario)
        self.boton_salir.clicked.connect(self.salir)
        self.show()

    def verificar_usuario(self):
        # DEBES MODIFICAR ESTE MÉTODO
        print(self.campo_nombre.text())
        self.senal_verificar_usuario.emit(self.campo_nombre.text())

    def salir(self):
        # NO DEBES MODIFICAR ESTE MÉTODO
        self.close()

    def mostrar_ventana(self):
        # NO DEBES MODIFICAR ESTE MÉTODO
        self.campo_nombre.setText("")
        self.show()


class VentanaError(window_name_error, base_class_error):
    # NO DEBES MODIFICAR ESTA CLASE

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.esconder)
        self.logo.setPixmap(QPixmap(p.IMAGEN_ERROR))
        self.logo.setScaledContents(True)

    def mostrar(self):
        self.show()

    def esconder(self):
        self.hide()
