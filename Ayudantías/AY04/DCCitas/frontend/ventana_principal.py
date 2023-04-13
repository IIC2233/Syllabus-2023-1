import sys
from os.path import join
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal


class VentanaPrincipal(QWidget):
    senal_like = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(300, 300, 500, 500)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('DCCitas')
        self.init_pixmaps()
        self.actual = "Julio"
        self.frases = {"Julio": "Hola! soy Julio, en que te ayudo?", "Manuel": "Una te lleva al pais de las maravillas, la otra te da caña"}
        self.init_gui()
        self.actualizar_descripcion()
        

    def init_pixmaps(self):
        self.pixmap_perfiles = dict()
        pixmap_julio = QPixmap(join('frontend', 'imgs', 'perfiles', 'julio.jpg'))
        pixmap_manuel = QPixmap(join('frontend', 'imgs', 'perfiles', 'manuel.jpeg'))
        self.pixmap_perfiles["Julio"] = pixmap_julio
        self.pixmap_perfiles["Manuel"] = pixmap_manuel


    def init_gui(self):
        layout = QVBoxLayout()

        self.foto = QLabel(self)

        pixmap_foto = self.pixmap_perfiles[self.actual]
        self.foto.setPixmap(pixmap_foto)
        self.foto.resize(100, 100)
        layout.addWidget(self.foto)
        layout.addStretch(1)

        self.texto = QLabel("Descripcion", self)
        
        layout.addWidget(self.texto)
        layout.addStretch(1)

        # Botones
        self.like = QPushButton("Like", self)
        self.like.clicked.connect(self.like_perfil)

        self.next = QPushButton("Next", self)
        self.next.clicked.connect(self.siguiente_perfil)
        
        horizontal = QHBoxLayout()
        horizontal.addWidget(self.next)
        horizontal.addWidget(self.like)

        layout.addLayout(horizontal)
        layout.addStretch(1)

        self.setLayout(layout)


    def mostrar(self):
        self.show()

    def actualizar_descripcion(self):
        frase = self.frases[self.actual]
        self.texto.setText(frase)


    def actualizar_foto(self):
        pixmap_foto = self.pixmap_perfiles[self.actual]
        self.foto.setPixmap(pixmap_foto)
        self.foto.resize(100, 100)
        self.foto.repaint()


    def like_perfil(self):
        self.senal_like.emit(self.actual)

    def siguiente_perfil(self):
        if self.actual == "Julio":
            self.actual = "Manuel"
        elif self.actual == "Manuel":
            self.actual = "Julio"
        self.actualizar_foto()
        self.actualizar_descripcion()
        