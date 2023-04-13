import sys
from PyQt5.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == "__main__":
    app = QApplication([])

    # Instanciamos las clases
    backend = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    # Conectamos las señales
    # COMPLETAR

    # Empezamos la ejecución del programa
    backend.empezar()

    sys.exit(app.exec())
