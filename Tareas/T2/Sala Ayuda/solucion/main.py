import sys
from PyQt5.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == "__main__":
    # NEW: METODO PARA AYUDAR EN ERROR
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciamos las clases
    backend = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    # Conectamos las señales
    control_remoto.senal_volumen.connect(backend.cambiar_volumen)
    control_remoto.senal_canal.connect(backend.cambiar_canal)
    control_remoto.senal_encendido.connect(backend.prender_apagar)

    backend.senal_volumen.connect(pantalla.actualizar_volumen)
    backend.senal_canal.connect(pantalla.actualizar_canal)

    backend.senal_encendido.connect(pantalla.prender_apagar)
    backend.senal_encendido.connect(control_remoto.prender_apagar)

    backend.senal_empezar.connect(pantalla.show)
    backend.senal_empezar.connect(control_remoto.show)

    # NEW: NUEVA CONEXIÓN
    control_remoto.senal_zapping.connect(backend.zapping)

    # Empezamos la ejecución del programa
    backend.empezar()

    sys.exit(app.exec())
