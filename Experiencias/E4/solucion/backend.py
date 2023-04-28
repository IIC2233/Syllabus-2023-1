from PyQt5.QtCore import QObject, QTimer, pyqtSignal
from random import randint
import parametros as p


class Meteorito(QObject):
    identificador = 0

    def __init__(self, x: int, y: int, senal_fin_meteorito: pyqtSignal,
                 senal_mover: pyqtSignal) -> None:
        super().__init__()

        self.id = Meteorito.identificador
        Meteorito.identificador += 1
        self.x = x
        self.y = y
        self.senal_mover = senal_mover
        self.senal_fin_meteorito = senal_fin_meteorito
        self._destruido = False
        self._distancia_a_recorrer = randint(
            p.DISTANCIA_MINIMA, p.DISTANCIA_MAXIMA)

        self.timer_movimiento = QTimer(self)
        self.timer_movimiento.setInterval(p.TIEMPO_CAIDA_METEORO)
        self.timer_movimiento.timeout.connect(self.mover)

    def mover(self) -> None:
        self.y += self._distancia_a_recorrer
        self.senal_mover.emit(self.id, self.x, self.y)
        if self.y >= p.POSICION_Y:
            # Desaparecer haciendo daño
            self.senal_fin_meteorito.emit(self.id, True)
            self.timer_movimiento.stop()

    @property
    def destruido(self) -> bool:
        return self._destruido

    @destruido.setter
    def destruido(self, new_value: bool) -> None:
        if new_value:  # Solo si se cambia a destruido == True
            self._destruido = new_value
            # Desaparecer sin hacer daño
            self.senal_fin_meteorito.emit(self.id, False)
            # Dejar de usar el timer para mover el meteorito
            self.timer_movimiento.stop()

    @property
    def centro_x(self) -> int:
        return self.x + 15

    @property
    def centro_y(self) -> int:
        return self.y + 192


class Ciudad:
    def __init__(self, nombre: str, senal_poblacion: pyqtSignal) -> None:
        self.nombre = nombre
        self._destruidos = 0
        self._poblacion = 0
        self.senal_poblacion = senal_poblacion

    @property
    def poblacion(self) -> int:
        return self._poblacion

    @poblacion.setter
    def poblacion(self, new_value: int) -> None:
        self._poblacion = new_value
        if self.poblacion <= 0:
            self.senal_poblacion.emit(
                f'{self.nombre} ha perdido todos sus ciudadanos')
        else:
            self.senal_poblacion.emit(
                f'{self.nombre} tiene {self.poblacion} ciudadanos')


class Juego(QObject):
    senal_validar_login = pyqtSignal(dict) # Agregamos una señal adicional
    senal_empezar_juego = pyqtSignal()
    senal_mover_meteorito = pyqtSignal(int, int, int)
    senal_aparecer_meteorito = pyqtSignal(int, int, int)
    senal_remover_meteorito = pyqtSignal(int)
    senal_fin_meteorito = pyqtSignal(int, bool)
    senal_actualizar_poblacion = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

        self.ciudad = Ciudad("DCCity", self.senal_actualizar_poblacion)
        self.meteoritos = []

        self.timer_meteoritos = QTimer(self)
        self.timer_meteoritos.timeout.connect(self.caer_meteorito)

        self.senal_fin_meteorito.connect(self.choque_meteorito)

    #######################################
    # Se agrega método para validar login
    #######################################
    def seleccionar_dificultad(self, dificultad: str) -> None:
        self.timer_meteoritos.setInterval(p.DIFICULTAD[dificultad])
        self.iniciar_juego()

    def iniciar_juego(self) -> None:
        self.ciudad._destruidos = 0
        self.ciudad.poblacion = p.POBLACION_MAXIMA
        self.senal_empezar_juego.emit()
        self.timer_meteoritos.start()

    def caer_meteorito(self) -> None:
        meteorito = Meteorito(
            x=randint(50, 750),
            y=-200,
            senal_fin_meteorito=self.senal_fin_meteorito,
            senal_mover=self.senal_mover_meteorito
        )
        self.senal_aparecer_meteorito.emit(meteorito.id,
                                           meteorito.x, meteorito.y)
        meteorito.timer_movimiento.start()
        self.meteoritos.append(meteorito)

    def choque_meteorito(self, id_meteorito: int, daño: bool) -> None:
        # Eliminar visualmente el meteorito
        self.senal_remover_meteorito.emit(id_meteorito)

        if daño:  # Si hay daño, disminuir población
            self.ciudad.poblacion -= p.AFECTADOS

        # Si no quedan personas. Parar los meteoritos
        if self.ciudad.poblacion <= 0:
            self.timer_meteoritos.stop()

    def click_pantalla(self, x: int, y: int) -> None:
        meteorito: Meteorito
        for meteorito in self.meteoritos:
            if not meteorito.destruido:  # Solo verificar meteoritos sin destruir
                if self.chequear_colision(x, y, meteorito):
                    # Si el click es válido, se destruye el meteorito
                    meteorito.destruido = True
                    self.ciudad._destruidos += 1
                    return

    def chequear_colision(self, x: int, y: int, meteorito: Meteorito) -> bool:
        distancia = ((x - meteorito.centro_x)**2 +
                     (y - meteorito.centro_y)**2)**(1/2)
        if distancia > 10:  # Lejos del centro del meteorio
            return False
        return True
