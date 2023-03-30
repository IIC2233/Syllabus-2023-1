class Animal:
    pass

class Terrestre:
    pass

class Acuatico:
    pass

class Perro:
    pass

class Pez:
    pass

class Ornitorrinco:
    pass


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    perro.desplazarse()
    pez.desplazarse()
    ornitorrinco.desplazarse()