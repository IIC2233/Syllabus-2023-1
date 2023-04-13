from random import choice, random


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
    
    def preparar_clase(self, contenidos: str) -> str:
        return contenidos


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


class AyudanteCorrector(Ayudante):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def corregir(self):
        self.energia -= 10
        return random(0, 7)


class AyudanteJefe(Ayudante):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.ayudantes = []
    
    def organizar_curso(self):
        self.energia -= 50


class AyudanteCatedra(Ayudante):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def realizar_ayudantia(self):
        self.energia -= 20