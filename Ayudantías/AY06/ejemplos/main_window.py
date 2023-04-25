import os
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QAction)


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa el main widget y sus elementos.
        """
        self.label1 = QLabel('Texto', self)
        self.label2 = QLabel('Echo texto:', self)
        self.edit = QLineEdit('', self)
        self.edit.setGeometry(45, 15, 100, 20)

        self.boton = QPushButton('&Procesar', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.boton_callback)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label2)
        hbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def boton_callback(self):
        """
        Este método es el encargado ejecutar una acción cada vez que el botón
        es presionado. En esta caso, realiza el cambio en label2 y el status bar
        mediate la emisión de una señal en la cual se envía el texto correspondiente.
        """
        self.label2.setText(f'Echo texto: {self.edit.text()}')
        self.status_bar.emit(f'Qedit: {self.edit.text()}')

    def cargar_status_bar(self, signal):
        """
        Este método recibirá una señal creada desde el MainWindow.
        Esta señal permitirá al widget central emitir cambios al status bar.
        """
        self.status_bar = signal


class MainWindow(QMainWindow):

    # Esta señal permite comunicar la barra de estados con el resto de los widgets
    # en el formulario, incluidos el central widget.
    onchange_status_bar = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        """Configuramos la geometría de la ventana."""
        self.setWindowTitle('Ventana con Boton')
        self.setGeometry(200, 100, 300, 250)

        """Configuramos las acciones."""
        ver_status = QAction(QIcon(None), '&Cambiar Status', self)
        ver_status.setStatusTip('Este es un ítem de prueba')
        ver_status.triggered.connect(self.cambiar_status_bar)

        limpiar_status = QAction(QIcon(None), '&Limpiar Status', self)
        limpiar_status.setStatusTip('Esta acción limpia la barra de estado')
        limpiar_status.triggered.connect(self.limpiar_status_bar)

        buscar = QAction(QIcon(os.path.join('img', 'search_icon.png')), '&Search', self)
        buscar.setStatusTip('Un ícono de búsqueda')

        salir = QAction(QIcon(None), '&Exit', self)
        salir.setShortcut('Ctrl+Q')
        salir.setStatusTip('Salir de la aplicación')
        salir.triggered.connect(QApplication.quit)

        """Creamos la barra de menú."""
        menubar = self.menuBar()
        archivo_menu = menubar.addMenu('&Archivo')  # primer menú
        archivo_menu.addAction(ver_status)
        archivo_menu.addAction(salir)

        otro_menu = menubar.addMenu('&Otro Menú')  # segundo menú
        otro_menu.addAction(limpiar_status)

        """Creamos la barra de herramientas."""
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(buscar)
        toolbar.addAction(salir)

        """Incluimos la barra de estado."""
        self.statusBar().showMessage('Listo')
        self.onchange_status_bar.connect(self.actualizar_status_bar)

        """
        Configuramos el widget central con una instancia de la clase
        MiVentana(). Además cargamos la señal en el central widget para
        que este pueda interactuar con la barra de estados de la ventana
        principal.
        """
        self.form = MiVentana()
        self.setCentralWidget(self.form)
        self.form.cargar_status_bar(self.onchange_status_bar)

    def cambiar_status_bar(self):
        self.statusBar().showMessage('Cambié el Status')

    def limpiar_status_bar(self):
        self.statusBar().showMessage('Status limpio.')

    def actualizar_status_bar(self, msg):
        self.statusBar().showMessage(f'Actualizado. {msg}')


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
