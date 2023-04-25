from collections import defaultdict, OrderedDict

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

import parametros as p


window_name, base_class = uic.loadUiType(p.PATH_VENTANA_JUEGO)
window_name_fin, base_class_fin = uic.loadUiType(p.PATH_VENTANA_FIN)


class VentanaJuego(window_name, base_class):
    # DEBES MODIFICAR ESTA CLASE

    senal_teclas = pyqtSignal(dict)
    empezar_senal_frontend = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.diccionario_grilla = defaultdict(lambda: [])
        self.piezas_encajadas = []
        self.posicion_x_antes = 0
        self.init_gui()

    # ACA SE ENCUENTRAN LOS MÉTODOS A MODIFICAR

    def mostrar_puntaje(self, puntaje):
        # DEBES MODIFICAR ESTE MÉTODO
        self.puntaje_usuario.setText(str(puntaje))

    def mostrar_ventana(self, usuario):
        # DEBES MODIFICAR ESTE MÉTODO
        self.nombre_usuario.setText(usuario)
        self.puntaje_usuario.setText('0')
        self.show()

    def init_gui(self):
        # NO DEBES MODIFICAR ESTE MÉTODO
        borde_horizontal = QPixmap(p.BORDE_HORIZONTAL)
        borde_vertical = QPixmap(p.BORDE_VERTICAL)
        self.borde_1.setPixmap(borde_vertical)
        self.borde_1.setScaledContents(True)
        self.borde_2.setPixmap(borde_vertical)
        self.borde_2.setScaledContents(True)
        self.borde_3.setPixmap(borde_horizontal)
        self.borde_3.setScaledContents(True)
        self.borde_4.setPixmap(borde_horizontal)
        self.borde_4.setScaledContents(True)
        self.logo_DCCTetis.setPixmap(QPixmap(p.LOGO_INICIO))
        self.logo_DCCTetis.setScaledContents(True)
        self.armar_diccionario_grilla()

    def armar_diccionario_grilla(self):
        # NO DEBES MODIFICAR ESTE MÉTODO
        """
        Este método crea un diccionario de la grilla 
        que se accede como dict[fila][columna]
        """
        self.atributos_clase = self.__dict__
        self.atributos_clase = OrderedDict(sorted(self.atributos_clase.items()))
        for label in self.atributos_clase:
            if "grilla" in label:
                for fila in range(20):
                    if "_{}_".format(str(fila)) in label:
                        for columna in range(10):
                            if "{}_{}".format(str(fila), str(columna)) in label and label[-1] in str(columna):
                                dict_columna = {}
                                self.atributos_clase[label].setText("")
                                self.atributos_clase[label].setStyleSheet("background:transparent;")
                                dict_columna[columna] = self.atributos_clase[label]
                                self.diccionario_grilla[fila].append(dict_columna[columna])

        self.diccionario_grilla = OrderedDict(sorted(self.diccionario_grilla.items()))

    def keyPressEvent(self, event):
        # DEBES MODIFICAR ESTE MÉTODO
        if event.key() == Qt.Key_A:
            self.senal_teclas.emit({'direccion': 'left'})
        if event.key() == Qt.Key_D:
            self.senal_teclas.emit({'direccion': 'right'})

    def colorear_grilla_entera(self, diccionario):
        # NO DEBES MODIFICAR ESTE MÉTODO
        for key, value in diccionario.items():
            self.diccionario_grilla[19 - key[1]][key[0]].setStyleSheet(f"background:{value};")

    def fin_juego(self):
        # NO DEBES MODIFICAR ESTE MÉTODO
        self.armar_diccionario_grilla()
        self.hide()




class VentanaFin(window_name_fin, base_class_fin):
    # DEBES MODIFICAR ESTA CLASE

    senal_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fondo_end.setPixmap(QPixmap(p.IMAGEN_FIN))
        self.fondo_end.setScaledContents(True)
        self.boton_inicio.clicked.connect(self.emitir_senal_inicio)

    def emitir_senal_inicio(self):
        # DEBES MODIFICAR ESTE MÉTODO
        self.hide()
        self.senal_inicio.emit()

    def mostrar_ventana(self, puntaje):
        # NO DEBES MODIFICAR ESTE MÉTODO
        self.puntaje_final.setText(str(puntaje))
        self.show()
