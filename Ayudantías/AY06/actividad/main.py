import sys

from PyQt5.QtWidgets import QApplication

from backend.logica_juego import Juego, Bloque
from backend.ventana_inicio_backend import VentanaInicioBackend
from frontend.ventana_inicio import VentanaInicio, VentanaError
from frontend.ventana_juego import VentanaJuego, VentanaFin

import parametros as p


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    # No modificar ->
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    # Ventana inicio (front-end y back-end)
    ventana_inicio = VentanaInicio()
    logica_inicio = VentanaInicioBackend(p.RUTA_CANCION)

    # Ventana juego (front-end y back-end)
    ventana_juego = VentanaJuego()
    logica_juego = Juego()

    # Ventanas adicionales
    ventana_error = VentanaError()
    ventana_fin_juego = VentanaFin()

    # DESDE ACA PUEDES MODIFICAR

    # Aca conectamos las señales

    # SEÑALES DE VENTANA DE INICIO
    ventana_inicio.senal_verificar_usuario.connect(logica_inicio.verificar_usuario)
    logica_inicio.senal_mensaje_error.connect(ventana_error.mostrar)
    logica_inicio.senal_empezar_juego.connect(ventana_juego.mostrar_ventana)
    logica_inicio.senal_empezar_juego.connect(logica_juego.comenzar_partida)
    logica_inicio.senal_empezar_juego.connect(ventana_inicio.salir)

    # SEÑALES DE VENTANA DE JUEGO
    ventana_juego.senal_teclas.connect(logica_juego.mover_bloque)
    logica_juego.senal_enviar_grilla.connect(ventana_juego.colorear_grilla_entera)
    ventana_juego.empezar_senal_frontend.connect(logica_juego.comenzar_partida)
    logica_juego.senal_enviar_puntaje.connect(ventana_juego.mostrar_puntaje)

    # FIN DE JUEGO
    logica_juego.senal_game_over.connect(ventana_juego.fin_juego)
    logica_juego.senal_game_over.connect(ventana_fin_juego.mostrar_ventana)
    ventana_fin_juego.senal_inicio.connect(ventana_inicio.mostrar_ventana)

    sys.exit(app.exec_())
    app.exec()
