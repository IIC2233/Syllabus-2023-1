from frontend.ventana_inicial import VentanaInicial
from frontend.ventana_principal import VentanaPrincipal
from backend.logica_inicial import LogicaInicio
from backend.logica_principal import LogicaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

class DCCitas(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.ventana_inicial = VentanaInicial()
        self.ventana_principal = VentanaPrincipal()

        self.logica_inicio = LogicaInicio()
        self.logica_principal = LogicaPrincipal()
        self.conectar_senales()

        self.ventana_inicial.mostrar()

    
    def conectar_senales(self):
        self.ventana_inicial.senal_login.connect(self.logica_inicio.comprobar_usuario)
        self.logica_inicio.senal_respuesta.connect(self.ventana_inicial.validacion)
        self.ventana_inicial.senal_abrir.connect(self.ventana_principal.mostrar)

        self.ventana_principal.senal_like.connect(self.logica_principal.registrar)


if __name__ == '__main__':
    app = DCCitas([])
    sys.exit(app.exec())
