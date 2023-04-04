# Básicamente, es un ejemplo en el que somos un usuario usando una versión
# simplificada de la app de Red, en el que buscamos si cierto recorrido de bus
# existe para un paradero dado.
#
# Por simplicidad, basta con que existan buses en el recorrido para que la app
# de un resultado "positivo".
#
# Para vincular con excepciones, puede suceder que no hayan buses para un
# recorrido D:, o que ese recorrido no pase por el paradero, en cuyo caso
# la app va a intentar buscar en otros "cercanos".


class Recorrido:

    def __init__(self, numero, paraderos):
        self.numero = numero
        self.activo = False

    def activar_recorrido(self):
        self.activo = True

    def detener_recorrido(self):
        self.activo = False


class Paradero:

    def __init__(self, codigo, recorridos):
        self.codigo = codigo
        self.recorridos = recorridos
        
    def buscar_bus(self, recorrido):
        if not recorrido.activo:
            ### Completar aquí
            pass
            raise BusNotFoundError(recorrido)
         
        elif recorrido not in self.recorridos:
            ###
            pass
            raise StopNotFoundError(recorrido, self)
        
        else:
            return True


class BusNotFoundError(Exception):
    ### Completar aquí
    pass
    
    def __init__(self, recorrido):
        super().__init__(f"No hay buses para este recorrido ({recorrido.numero}) :(")


class StopNotFoundError(Exception):
    ### Completar aquí
    pass

    def __init__(self, recorrido, parada):
        self.recorrido = recorrido
        super().__init__(
            f"Este recorrido ({recorrido.numero}) no corresponde a esta parada ({parada.codigo})"
        )

    def dar_detalles(self):
        msg = (f"En esta parada se detienen:\n")
        for recorrido in self.parada.recorridos:
            msg += recorrido.numero + "\n"
        return msg


# Recorridos
recorrido_506 = Recorrido(506)
recorrido_425 = Recorrido(425)
recorrido_555 = Recorrido(555)

recorridos = {
    "506": recorrido_506,
    "425": recorrido_425,
    "555": recorrido_555
}

recorrido_506.activar_recorrido()
recorrido_425.activar_recorrido()

# Paraderos
paradero_A1 = Paradero("A1", recorrido_506)
paradero_A2 = Paradero("A2", recorrido_506)
paradero_B1 = Paradero("B1", recorrido_425)
paradero_B2 = Paradero("B2", recorrido_425)
paradero_B3 = Paradero("B3", recorrido_555)
paradero_AB = Paradero(
    "AB", recorrido_506, recorrido_555, recorrido_425
)

paraderos = {
    "A1": paradero_A1,
    "A2": paradero_A2,
    "B1": paradero_B1,
    "B2": paradero_B2,
    "B3": paradero_B3,
    "AB": paradero_AB
}


continuar = True
while continuar:
    try:
        paradero_str = input("Introduzca el código de su paradero: ")
        recorrido_str = input("Introduzca el recorrido que busca: ")
        paradero = paraderos[paradero_str.upper()]
        recorrido = recorridos[recorrido_str]
        continuar = False

    except KeyError:
        print("Datos inválidos, intente nuevamente")

        
### Completar aquí
# Ejecución
try:
    if paradero.buscar_bus(recorrido):
        print("Hay buses de este recorrido para este paradero :D")
except BusNotFoundError as error:
    print(error)
except StopNotFoundError as error:
    print(error)
    print(error.dar_detalles())
