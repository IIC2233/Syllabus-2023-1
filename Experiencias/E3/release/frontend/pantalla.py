import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QProgressBar


class VentanaPantalla(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.posicion = (100, 100)
        self.porte = (640, 360)
        self.setGeometry(*self.posicion, *self.porte)
        self.setWindowTitle("Pantalla")

        self.generar_widgets()
        self.agregar_estilo()

    def generar_widgets(self):
        # Generamos y posicionamos los distintos widgets
        self.imagen = QLabel("", self)
        self.imagen.setGeometry(0, 0, *self.porte)

        self.canal = QLabel("Canal: #0", self)
        self.canal.move(20, 20)

        self.volumen = QLabel("Volumen: 0", self)
        self.volumen.move(20, self.porte[1] - 30)

        self.volumen_barra = QProgressBar(self, textVisible=False)
        self.volumen_barra.resize(100, 15)
        self.volumen_barra.move(120, self.porte[1] - 30)

    def agregar_estilo(self):
        # Agregamos un poco de estilo a los labels
        self.canal.setStyleSheet(
            """
            color: white;
            background: black;
        """
        )
        self.volumen.setStyleSheet(
            """
            color: white;
            background: black;
        """
        )

    def actualizar_volumen(self, nuevo_volumen):
        # Cambiamos el texto
        # COMPLETAR

        # Actualizamos la barra
        self.volumen_barra.setValue(nuevo_volumen)

    def actualizar_canal(self, nuevo_canal):
        # Actualizamos el texto
        # COMPLETAR

        # Cargamos, rescalamos y cambiamos la imagen
        # COMPLETAR
        pass

    def prender_apagar(self, encendido):
        if encendido:
            self.show()
        else:
            self.hide()


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPantalla()
    ventana.show()
    sys.exit(app.exec())
