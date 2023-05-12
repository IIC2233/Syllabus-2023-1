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
        # NEW:
        self.cargar_pixmaps()

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
        self.volumen.setText("Volumen: " + str(nuevo_volumen))
        self.volumen.resize(self.volumen.sizeHint())

        # Actualizamos la barra
        self.volumen_barra.setValue(nuevo_volumen)

    # NEW: NUEVO METODO
    def cargar_pixmaps(self):
        self.pixmaps = {}
        path = os.path.join("frontend", "assets")
        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            number = image.strip(".png")
            self.pixmaps[str(number)] = QPixmap(img_path)

    def actualizar_canal(self, nuevo_canal):
        print("[Pantalla] Nuevo canal es...", nuevo_canal)
        # Actualizamos el texto
        self.canal.setText("Canal: " + str(nuevo_canal))
        self.canal.resize(self.canal.sizeHint())

        # Cargamos, rescalamos y cambiamos la imagen
        # NEW:
        # 1. Cargar la imagen de nuestro diccionario
        imagen = self.pixmaps[str(nuevo_canal)]
        # 2. Ajustar imagen al tamaño de la ventana (rescalamos)
        imagen = imagen.scaled(*self.porte, Qt.KeepAspectRatioByExpanding)

        # 3. Actualizar label con la imagen
        self.imagen.setPixmap(imagen)

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
