# Importacion de librerias para todas las celdas del ejemplo
import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class ThreadBacan(QThread):
    def __init__(self, actualizar_label_signal, *args, **kwargs):
        # Entregar *args y **kwargs a la super clase es importante por si queremos dar algun parametro
        # inicial de los que ya ofrece la clase QThread
        super().__init__(*args, **kwargs)
        # Le entregamos una senal que queremos que el Thread emita
        self.actualizar_label_signal = actualizar_label_signal

    def run(self):
        for _ in range(10):
            self.actualizar_label_signal.emit()
            sleep(0.5)


class VentanaConThread(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.label_numero = QLabel("0", self)
        self.boton_numero = QPushButton("0", self)
        self.boton_loop = QPushButton("Iniciar Loop", self)

        self.layout_principal = QVBoxLayout(self)

        # Creamos nuestro thread y le entregamos la senal para actualizar el label
        self.thread_bacan = ThreadBacan(self.actualizar_label_signal)
        self.init_gui()

    def init_gui(self):
        self.layout_principal.addWidget(self.label_numero)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.boton_numero)
        self.layout_principal.addWidget(self.boton_loop)

        self.boton_numero.clicked.connect(self.actualizar_boton)
        self.boton_loop.clicked.connect(self.iniciar_loop)
        self.actualizar_label_signal.connect(self.actualizar_label)
        self.show()
    
    def actualizar_label(self):
        numero_actual = int(self.label_numero.text())
        self.label_numero.setText(str(numero_actual + 1))

    def actualizar_boton(self):
        numero_actual = int(self.boton_numero.text())
        self.boton_numero.setText(str(numero_actual + 1))

    def iniciar_loop(self):
        self.thread_bacan.start()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaConThread()
    sys.exit(app.exec_())