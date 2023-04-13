from PyQt5.QtCore import QObject


class LogicaPrincipal(QObject):

    def __init__(self):
        super().__init__()

    def registrar(self, usuario):
        with open("registro_like.txt", "a") as archivo:
            archivo.write(usuario + "\n")
