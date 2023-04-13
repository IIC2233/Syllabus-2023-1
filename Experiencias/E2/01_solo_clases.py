from random import choice


class Profesor:
    def __init__(self, nombre, curso, **kwargs) -> None:
        self.nombre = nombre
        self.curso = curso
        self.__energia = 100

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, e):
        return max(0, e)

    def resolver_duda(self, pregunta: str) -> str:
        self.energia -= 10
        return choice(['Sí', 'No'])


class Estudiante:
    def __init__(self, nombre, **kwargs) -> None:
        self.nombre = nombre
        self.__energia = 100

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, e):
        return max(0, e)

    def estudiar(self):
        self.energia -= 10


class Ayudante:
    def __init__(self, nombre, curso, **kwargs) -> None:
        self.nombre = nombre
        self.curso = curso
        self.__energia = 100

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, e):
        return max(0, e)

    def estudiar(self):
        self.energia -= 10

    def resolver_duda(self, pregunta: str) -> str:
        self.energia -= 10
        return choice(['Sí', 'No'])