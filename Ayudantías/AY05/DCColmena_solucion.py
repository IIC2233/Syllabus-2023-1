
from threading import Event, Thread, Lock, Timer
from collections import deque
from time import sleep


class Colonia(Thread):

    def __init__(self, jardin):
        super().__init__()
        self.polen = deque()
        self.polen.append('unidad_polen')
        self.miel = deque()
        self.miel.append('unidad_miel')
        self.jardin = jardin

        self.senal_inicio_trabajo = Event()

        self.obreras = [Abeja(self, jardin) for _ in range(4)]

    def run(self):
        print('\nBienvenido a la DCColonia!')
        print('Iniciando día...\n')
        sleep(5)

        self.iniciar_dia()
        self.criar_abeja()
        self.senal_inicio_trabajo.set()

        while True:
            if input() == 'end':
                break
        self.imprimir_estado()
        print('✖ Fin thread colonia')

    def iniciar_dia(self):
        for abeja in self.obreras:
            abeja.start()

    def criar_abeja(self):
        abeja = Abeja(self, self.jardin)
        self.obreras.append(abeja)
        abeja.start()
        criar_timer = Timer(10, self.criar_abeja)
        criar_timer.daemon = True
        criar_timer.start()

    def imprimir_estado(self):
        print('\n' + '----'*5)
        print('Estado DCColonia')
        print(f'Número de abejas: {len(self.obreras)}')
        print(f'Unidades de miel: {len(self.miel)}')
        print('---'*6)


class Abeja(Thread):

    counter = 0
    lock_abertura = Lock()

    def __init__(self, colonia, jardin):
        super().__init__()
        self.id = Abeja.counter
        Abeja.counter += 1
        self.daemon = True
        self.polen = deque()
        self.colonia = colonia
        self.jardin = jardin

    def __str__(self):
        return f'Abeja {self.id}'

    def run(self):
        print(f'✚ {self} ha nacido')
        self.colonia.senal_inicio_trabajo.wait()
        while True:
            self.salir_colonia()
            self.volar_al_jardin()
            self.recolectar_polen()
            self.volar_a_la_colonia()
            self.entrar_colonia()
            self.producir_miel()

    def salir_colonia(self):
        with self.lock_abertura:
            sleep(2)
            print(f'→ {self} salió del panal')

    def volar_al_jardin(self):
        sleep(5)
        print(f'❀ {self} llegó al jardín')

    def recolectar_polen(self):
        sleep(5)
        self.polen.append(self.jardin.polen.pop())
        print(f'▧ {self} recolectó {len(self.polen)} polen, y se devuelve')

    def volar_a_la_colonia(self):
        sleep(5 * len(self.polen))
        print(f'▣ {self} regresó a la colonia')

    def entrar_colonia(self):
        with self.lock_abertura:
            sleep(2)
            print(f'← {self} entró al panal')

        for _ in range(len(self.polen)):
            unidad_polen = self.polen.pop()
            self.colonia.polen.append(unidad_polen)

    def producir_miel(self):
        self.colonia.polen.pop()
        sleep(10)
        self.colonia.miel.append('unidad_miel')
        print(f'♨ {self} ha producido una unidad de miel')


class Jardin(Thread):

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.polen = deque()

    def run(self):
        while True:
            sleep(1)
            self.polen.append('unidad_polen')


if __name__ == '__main__':
    jardin = Jardin()
    colonia = Colonia(jardin)
    jardin.start()
    colonia.start()