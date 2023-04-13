from PyQt5.QtCore import QObject, pyqtSignal


class LogicaInicio(QObject):
    senal_respuesta = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.usuarios = ["Julio"]

    def comprobar_usuario(self, usuario):
        result = True
        if not usuario.isalnum():
            result = False
        if not len(usuario) > 3:
            result = False
        if usuario in self.usuarios:
            result = False

        self.senal_respuesta.emit(result)
            