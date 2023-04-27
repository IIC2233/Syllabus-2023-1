from PyQt5.QtWidgets import QApplication
from frontend import VentanaInicio, VentanaJuego  # Se agrega import
import sys
from backend import Juego


class ShootApplication:
    def __init__(self) -> None:
        self.frontend_juego = VentanaJuego()
        self.backend = Juego()

    def conectar(self) -> None:
        # Backend le avisa al frontend del juego que empieza el juego
        self.backend.senal_empezar_juego.connect(
            self.frontend_juego.empezar_juego)

        # COMPLETAR
        # Frontend_juego notifica al backend cuando se hace click en pantalla

        # Backend notifica al frontend_juego cuando aparece, se mueve
        # y desaparece el meteorito

        # Backend notifica al frontend_juego cuando se cambia la población

    def iniciar(self):
        # Comenzar el juego
        self.backend.iniciar_juego()


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
