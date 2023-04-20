from threading import Event, Lock
from time import sleep

from carrera import Carrera, Corredor


class Simulación:
    def __init__(self):
        self.tortugas = {
            'c1' : Lock(),
            'c2' : Lock(),
            'c3' : Lock()
        }
        self.lock_verificar_tortuga = {
            'c1' : Lock(),
            'c2' : Lock(),
            'c3' : Lock()
        }
        self.s_inicio = {
            'c1' : Event(),
            'c2' : Event(),
            'c3' : Event()
        }
        self.s_fin = {
            'c1' : Event(),
            'c2' : Event(),
            'c3' : Event()
        }
        self.equipo_a = {
            'c1' : Corredor('Alexis', self.tortugas['c1'], self.s_inicio['c1'], self.s_fin['c1'], self.lock_verificar_tortuga['c1']),
            'c2' : Corredor('Alicia', self.tortugas['c2'], self.s_inicio['c2'], self.s_fin['c2'], self.lock_verificar_tortuga['c2']),
            'c3' : Corredor('Alonso', self.tortugas['c3'], self.s_inicio['c3'], self.s_fin['c3'], self.lock_verificar_tortuga['c3']),
        }
        self.equipo_c = {
            'c1' : Corredor('Carmen', self.tortugas['c1'], self.s_inicio['c1'], self.s_fin['c1'], self.lock_verificar_tortuga['c1']),
            'c2' : Corredor('Camila', self.tortugas['c2'], self.s_inicio['c2'], self.s_fin['c2'], self.lock_verificar_tortuga['c2']),
            'c3' : Corredor('Carlos', self.tortugas['c3'], self.s_inicio['c3'], self.s_fin['c3'], self.lock_verificar_tortuga['c3']),
        }
        self.carreras = self.crear_carreras()

    def crear_carreras(self):
        carrera_1 = Carrera(
            corredor_1 = self.equipo_a['c1'],
            corredor_2 = self.equipo_c['c1'],
            senal_inicio = self.s_inicio['c1'],
            senal_fin = self.s_fin['c1']
        )
        carrera_2 = Carrera(
            corredor_1 = self.equipo_a['c2'],
            corredor_2 = self.equipo_c['c2'],
            senal_inicio = self.s_inicio['c2'],
            senal_fin = self.s_fin['c2']
        )
        carrera_3 = Carrera(
            corredor_1 = self.equipo_a['c3'],
            corredor_2 = self.equipo_c['c3'],
            senal_inicio = self.s_inicio['c3'],
            senal_fin = self.s_fin['c3']
        )
        return {'c1': carrera_1, 'c2': carrera_2, 'c3': carrera_3}


if __name__ == '__main__':
    sim = Simulación()
    wins = list()
    for carrera in sim.carreras.values():
        carrera.empezar()

        ganador = carrera.corredor_1 if carrera.corredor_1.tiene_tortuga else carrera.corredor_2
        
        print(f'\n\n{ganador.name} ha ganado la carrera')
        print(f'Un punto para el equipo {ganador.name[0]}\n\n')
        wins.append(ganador.name[0])

    puntos_a = sum([w == 'A' for w in wins])
    equipo_ganador = 'A' if puntos_a >= 2 else 'C'
    print(f'¡El equipo {equipo_ganador} gana la competencia!')
