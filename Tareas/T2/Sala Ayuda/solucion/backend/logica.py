from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class ControladorLogico(QObject):
    senal_volumen = pyqtSignal(int)
    senal_canal = pyqtSignal(int)
    senal_encendido = pyqtSignal(bool)
    senal_empezar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._volumen = 20
        self._canal = 1
        self.prendido = True

        # NEW: NUEVO ATRIBUTO
        self.zapping_timer = QTimer(self)
        self.zapping_timer.timeout.connect(self.empezar_zapping)
        self.zapping_timer.setInterval(100)

    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, valor):
        if valor < 0:
            valor = 0
        elif valor > 100:
            valor = 100

        self._volumen = valor

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, valor):
        if (valor < 1) or (valor > 9):
            valor = 1 + (valor - 1) % 9

        self._canal = valor

    def cambiar_volumen(self, cambio):
        if cambio == "+":
            self.volumen += 10
        elif cambio == "-":
            self.volumen -= 10
        self.actualizar_volumen()

    def cambiar_canal(self, cambio):
        if cambio == "+":
            self.canal += 1
        elif cambio == "-":
            self.canal -= 1
        else:
            self.canal = int(cambio)

        self.actualizar_canal()

    def actualizar_volumen(self):
        self.senal_volumen.emit(self.volumen)

    def actualizar_canal(self):
        self.senal_canal.emit(self.canal)

    def prender_apagar(self):
        self.prendido = not self.prendido
        self.senal_encendido.emit(self.prendido)

    def empezar(self):
        self.actualizar_canal()
        self.actualizar_volumen()
        self.senal_empezar.emit()

    # NEW: NUEVO METODO
    def zapping(self, empezar):
        if empezar:
            self.zapping_timer.start()
        else:
            self.zapping_timer.stop()

    # NEW: NUEVO METODO
    def empezar_zapping(self):
        self.cambiar_canal("+")

