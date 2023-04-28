from PyQt5.QtWidgets import QApplication
from frontend import VentanaInicio, VentanaJuego  # Se agrega import
import sys
from backend import Juego


class ShootApplication:
    def __init__(self) -> None:
        self.frontend_dificultad = VentanaInicio() # Se agrega una ventana
        self.frontend_juego = VentanaJuego() 
        self.backend = Juego()

    def conectar(self) -> None:
        #######################################
        # Se agregan 2 señales más ↓↓↓↓↓↓↓↓↓
        #######################################
        # frontend_dificultad avisa al backend sobre la dificultad
        self.frontend_dificultad.senal_difficultad.connect(
            self.backend.seleccionar_dificultad)

        # Backend avisa al frontend_dificultad que se esconda
        self.backend.senal_empezar_juego.connect(
            self.frontend_dificultad.hide)

        #######################################
        # Se agregan 2 señales más ↑↑↑↑↑↑↑
        #######################################

        # Backend le avisa al frontend del juego que empieza el juego
        self.backend.senal_empezar_juego.connect(
            self.frontend_juego.empezar_juego)

        # Frontend_juego notifica al backend cuando se hace click en pantalla
        self.frontend_juego.senal_click_pantalla.connect(
            self.backend.click_pantalla)

        # Backend notifica al frontend_juego cuando aparece, se mueve
        # y desaparece el meteorito
        self.backend.senal_aparecer_meteorito.connect(
            self.frontend_juego.aparecer_meteorito)
        self.backend.senal_mover_meteorito.connect(
            self.frontend_juego.mover_meteorito)
        self.backend.senal_remover_meteorito.connect(
            self.frontend_juego.remover_meteorito)

        # Backend notifica al frontend_juego cuando se cambia la población
        self.backend.senal_actualizar_poblacion.connect(
            self.frontend_juego.actualizar_poblacion)

    def iniciar(self) -> None:
        # En vez de comenzar juego, mostramos la ventana de login
        self.frontend_dificultad.show()


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    game = ShootApplication()
    game.conectar()
    game.iniciar()

    # Si queremos solo ver la VentanaInicio
    # game=VentanaInicio()
    # game.show()

    sys.exit(app.exec())
