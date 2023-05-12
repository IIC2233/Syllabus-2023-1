import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout,
)
from PyQt5.QtGui import QKeyEvent


class VentanaControlRemoto(QWidget):

    senal_volumen = pyqtSignal(str)
    senal_canal = pyqtSignal(str)
    senal_encendido = pyqtSignal()
    # NEW
    senal_zapping = pyqtSignal(bool)  # NUEVA SEÑAL

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.generar_botones()
        self.generar_layout()
        self.conectar_botones()
        self.agregar_estilo()
        self.setWindowTitle('Control remoto')
        self.move(800, 100)

    def generar_botones(self):
        # Botón encendido/apagado
        self.on_off = QPushButton('Off', self)

        # Botones de volumen
        self.volumen = [
            QPushButton('+', self),
            QPushButton('-', self)
        ]

        # Botones de canales  # Completar este
        self.canales = [
            QPushButton('+', self),
            QPushButton('-', self),
        ]

        # Botones de números  # Completar este
        self.numeros = []
        for numero in range(1, 10):
            boton = QPushButton(f'{numero}', self)
            self.numeros.append(boton)

    def generar_layout(self):
        # Generamos el layout principal
        vbox = QVBoxLayout()

        # Generamos un layout para los botones centrales
        hbox = QHBoxLayout()
        hbox.addLayout(self.generar_layout_subir_bajar(self.volumen, 'Vol'))
        hbox.addLayout(self.generar_layout_subir_bajar(self.canales, 'Canal'))

        # Agregamos los botones al layout principal
        vbox.addWidget(self.on_off)
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addLayout(self.generar_layout_numeros())
        vbox.addStretch()

        # Setteamos el layout
        self.setLayout(vbox)

    def generar_layout_subir_bajar(self, botones: list, texto: str):  # Dar
        texto = QLabel(texto, self)
        texto.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(botones[0])
        vbox.addWidget(texto)
        vbox.addWidget(botones[1])
        return vbox

    def generar_layout_numeros(self):
        # Creamos la grilla de los números
        grilla_numeros = QGridLayout()

        # Agregamos los botones a la grilla
        for pos, boton in enumerate(self.numeros):
            pos_x = pos // 3
            pos_y = pos % 3
            grilla_numeros.addWidget(boton, pos_x, pos_y)

        # Retornamos la grilla
        return grilla_numeros

    def agregar_estilo(self):  # Dar
        # Aplicamos estilo a los elementos
        self.setStyleSheet('''
            background: #2e2d2b;
            color:white;
        ''')
        self.on_off.setStyleSheet('''
            background: red;
        ''')

        # Ajustamos el tamaño de los botones
        for boton in (*self.volumen, *self.canales, *self.numeros):
            boton.setMinimumWidth(boton.sizeHint().height())
        self.on_off.setFixedSize(50, 50)

        # Ajustamos el tamaño del control
        self.resize(50, 360)

    def conectar_botones(self):
        # Botones de volumen
        for boton in self.volumen:
            boton.clicked.connect(self.actualizar_volumen)

        # Botones de canales
        for boton in [*self.canales, *self.numeros]:
            boton.clicked.connect(self.actualizar_canal)

        # Botón apagado
        self.on_off.clicked.connect(self.senal_encendido.emit)

    def actualizar_canal(self):
        sender = self.sender()
        identificador = sender.text()
        self.senal_canal.emit(identificador)

    def actualizar_volumen(self):
        sender = self.sender()
        identificador = sender.text()
        self.senal_volumen.emit(identificador)

    def prender_apagar(self, encendido: bool):
        self.on_off.setText('Off' if encendido else 'On')

    # NEW: NUEVO METODO
    def keyPressEvent(self, event: QKeyEvent) -> None:
        # Se debe verificar que el auto repeat es falto,
        # para así manejar el key press event una única vez
        if event.key() == Qt.Key_W and not event.isAutoRepeat():
            print("[Control Remoto] Se presionó W")
            self.senal_zapping.emit(True)

    # NEW: NUEVO METODO
    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        # Se debe verificar que el auto repeat es falto,
        # para así manejar el key release event una única vez
        if event.key() == Qt.Key_W and not event.isAutoRepeat():
            print("[Control Remoto] Se soltó W")
            self.senal_zapping.emit(False)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaControlRemoto()
    ventana.show()
    sys.exit(app.exec())
