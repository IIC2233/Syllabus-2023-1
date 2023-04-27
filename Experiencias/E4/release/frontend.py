from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QMouseEvent, QKeyEvent


class VentanaJuego(QMainWindow):
    # COMPLETAR
    # Definir señal para cuando hagamos click en la pantalla
    # ¿Qué información necesitamos del click?

    def __init__(self) -> None:
        super().__init__()
        # Importante que la ventana pueda seguir en todo momento el movimiento
        # del mouse y que este sea invisible
        self.setMouseTracking(True)
        self.setCursor(Qt.BlankCursor)

        # QLabel para el Background
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('./sprites/fondo.jpg'))
        self.background.setScaledContents(True)

        # Importante el QLabel sea transparente a los eventos del mouse.
        self.background.setAttribute(Qt.WA_TransparentForMouseEvents)

        # QLabel para la Vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        self.label_vida.setStyleSheet("color: white")

        # Importante el QLabel sea transparente a los eventos del mouse.
        self.label_vida.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.labels_meteorito = {}  # id: label
        self.pixmap_meteorito = QPixmap('./sprites/meteorite.png')

        # QLabel para la mira del disparo
        self.label_disparo = QLabel(self)
        self.label_disparo.setPixmap(QPixmap('./sprites/shooting-target.png'))
        self.label_disparo.setScaledContents(True)
        self.label_disparo.setGeometry(-100, -100, 100, 100)
        # Importante el QLabel sea transparente a los eventos del mouse.
        self.label_disparo.setAttribute(Qt.WA_TransparentForMouseEvents)

    def empezar_juego(self) -> None:
        # COMPLETAR
        # 1. Setear tamaño del juego en 800x500
        # 2. Setear tamaño de la imagen de fondo a 800x500
        # 3. Mostrar ventana
        pass

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        x = event.pos().x()
        y = event.pos().y()
        # Hacemos -50 para que esté en el centro.
        self.label_disparo.move(x - 50, y - 50)

    def actualizar_poblacion(self, texto: str) -> None:
        self.label_vida.setText(texto)
        self.label_vida.resize(self.label_vida.sizeHint())

    def aparecer_meteorito(self, id_meteorito: int, x: int, y: int) -> None:
        # Defini label de meteorito
        label = QLabel(self)
        label.setPixmap(self.pixmap_meteorito)
        label.setScaledContents(True)
        label.setGeometry(x, y, 30, 200)

        # Importante el QLabel sea transparente a los eventos del mouse.
        label.setAttribute(Qt.WA_TransparentForMouseEvents)
        # Guardar QLabel en nuestro diccionario
        self.labels_meteorito[id_meteorito] = label
        # La mira de disparo debe estar sobre todo lo demás
        self.label_disparo.raise_()
        # Mostrar imagen
        label.show()

    def remover_meteorito(self, id_meteorito: int) -> None:
        # Tarea para la casa
        # Investigar como eliminar elementos y no solo ocultarlos
        self.labels_meteorito[id_meteorito].hide()

    def mover_meteorito(self, id_meteorito: int, x: int, y: int) -> None:
        label: QPixmap = self.labels_meteorito[id_meteorito]
        label.move(x, y)


# PARTE 2 (lo veremos despues)
#######################################
# Se crea una nueva clase ↓↓↓↓↓↓↓↓↓
#######################################


class VentanaInicio(QWidget):
    senal_difficultad = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle("Selector Dificultad")

        # Creamos el selector que vamos a necesitar en nuestra ventana de Inicio
        self.selector_dificultad = QComboBox(self)
        self.selector_dificultad.addItems([
            "Facil", "Normal", "Díficil"
        ])
        self.boton_ingresar = QPushButton("Empezar juego", self)

        # Creamos el layout de nuestra ventana y agregamos los elementos
        layout = QHBoxLayout()
        layout.addWidget(self.selector_dificultad)
        layout.addWidget(self.boton_ingresar)

        self.setLayout(layout)

        # Conectamos las señales de los elementos
        self.boton_ingresar.clicked.connect(self.enviar_info)

        self.show()

    def enviar_info(self) -> None:
        # COMPLETAR
        # Le avisamos al backend la dificultad mediante la señal.
        pass

    # Detectar cuando se presiona enter para también enviar_info
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enviar_info()


#######################################
# Se crea una nueva clase ↑↑↑↑↑↑↑
#######################################
