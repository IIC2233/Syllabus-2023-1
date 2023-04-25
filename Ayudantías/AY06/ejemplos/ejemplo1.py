# Importacion de librerias para todas las celdas del ejemplo
import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class VentanaSinThread(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Creamos los botones y labels necesarios para el ejemplo.
        self.label_numero = QLabel("0", self)  # Muestra el numero que ira en aumento
        self.boton_numero = QPushButton("0", self)  # Muestra el numero que sube si lo apretamos
        self.boton_loop = QPushButton("Iniciar Loop", self)  # Inicia el loop
        self.layout_principal = QVBoxLayout(self)  # Layout de la ventana principal

        self.init_gui()


    def init_gui(self):
        # Ordenamos las Widgets
        self.layout_principal.addWidget(self.label_numero)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.boton_numero)
        self.layout_principal.addWidget(self.boton_loop)
        # Conectamos las senales
        self.boton_numero.clicked.connect(self.actualizar_boton)
        self.boton_loop.clicked.connect(self.iniciar_loop)
        self.actualizar_label_signal.connect(self.actualizar_label)
        self.show()


    def actualizar_label(self):
        # Obtenemos el numero actual del label y lo aumentamos en 1
        numero_actual = int(self.label_numero.text())
        self.label_numero.setText(str(numero_actual + 1))

    def actualizar_boton(self):
        # Obtenemos el numero actual del boton y lo aumentamos en 1
        numero_actual = int(self.boton_numero.text())
        self.boton_numero.setText(str(numero_actual + 1))

    def iniciar_loop(self):
        # Emitimos la senal 10 veces, con 0.5 segundos de espera entre emisiones.
        for _ in range(10):
            self.actualizar_label_signal.emit()
            sleep(0.5)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaSinThread()
    sys.exit(app.exec_())