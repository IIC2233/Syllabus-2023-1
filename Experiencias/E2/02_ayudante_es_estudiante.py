from random import choice


class Persona:
    def __init__(self, nombre, **kwargs) -> None:
        self.nombre = nombre
        self.__energia = 100
    
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, e):
        return max(0, e)


class Profesor(Persona):
    def __init__(self, curso, **kwargs) -> None:
        super().__init__(**kwargs)
        self.curso = curso

    def resolver_duda(self, pregunta: str) -> str:
        self.energia -= 10
        return choice(['Sí', 'No'])


class Estudiante(Persona):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def estudiar(self) -> None:
        self.energia -= 10


class Ayudante(Estudiante):
    def __init__(self, curso, **kwargs) -> None:
        super().__init__(**kwargs)
        self.curso = curso

    def resolver_duda(self, pregunta: str) -> str:
        self.energia -= 10
        return choice(['Sí', 'No'])