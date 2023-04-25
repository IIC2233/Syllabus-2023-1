# Importacion de librerias para todas las celdas del ejemplo
import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class ThreadDemoniaco(QThread):
    def __init__(self, padre, *args, **kwargs):
        # Entregar *args y **kwargs a la super clase es importante por si queremos dar algun parametro
        # inicial de los que ya ofrece la clase QThread
        super().__init__(*args, **kwargs)
        # Le entregamos una senal que queremos que el Thread emita
        self.ventana = padre
        self.actualizar_label_signal = self.ventana.actualizar_label_signal

    def run(self):
        while not self.ventana.terminar:
            self.actualizar_label_signal.emit()
            sleep(0.5)


class VentanaConThread(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.label_numero = QLabel("0", self)
        self.boton_empezar = QPushButton("Iniciar", self)
        self.boton_terminar = QPushButton("Terminar", self)

        self.layout_principal = QVBoxLayout(self)

        # Creamos nuestro thread y le entregamos la senal para actualizar el label
        self.terminar = False
        self.thread_demoniaco = ThreadDemoniaco(self)
        self.init_gui()

    def init_gui(self):
        self.layout_principal.addWidget(self.label_numero)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.boton_empezar)
        self.layout_principal.addWidget(self.boton_terminar)

        self.boton_empezar.clicked.connect(self.iniciar_qthread)
        self.boton_terminar.clicked.connect(self.terminar_qthread)

        # se conecta la señal
        self.actualizar_label_signal.connect(self.actualizar_label)
        self.show()
    
    def actualizar_label(self):
        numero_actual = int(self.label_numero.text())
        self.label_numero.setText(str(numero_actual + 1))

    def iniciar_qthread(self):
        self.thread_demoniaco.start()

    def terminar_qthread(self):
        self.terminar = True
        

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaConThread()
    sys.exit(app.exec_())