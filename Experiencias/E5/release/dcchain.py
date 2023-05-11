from collections import namedtuple
from hashlib import sha1
import pickle


Transaccion = namedtuple('Transaccion', 'emisor monto receptor')


class Bloque:
    def __init__(self, padre, hash_padre, transacciones):
        self.nonce = 0
        self.transacciones = transacciones
        self.padre = padre
        self.hash_padre = hash_padre
        self.hash_bloque = None

    def calcular_hash(self, funcion_hash):
        ''' Calcula la el hash asegurándose de que parta con 0 '''
        # Calcula la el hash con la funcion entregada
        h = funcion_hash(self.nonce, self.transacciones, self.hash_padre)
        # Recalcula el hash si su primer valor no es 0
        while h[0] != '0':
            # Cambia el nonce para cambiar el valor del hash
            self.nonce += 1
            h = funcion_hash(self.nonce, self.transacciones, self.hash_padre)
        # Guarda el hash cuando obtengas un valor válido
        self.hash_bloque = h


class DCChain:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    @staticmethod
    def funcion_hash(*args):
        ''' Funcion para calcular el hash de los nodos '''
        # Convierte el objeto a bytes para calcular su hash
        bytes = pickle.dumps(args)
        # calcula y retornas el hash del objeto
        return sha1(bytes).hexdigest()

    def agregar_bloque(self, transacciones):
        ''' Agrega una lista de transacciones a la blockchain '''
        # Completar
        pass

    def llenar_cadena(self, path_transacciones, largo_bloque=5):
        ''' Llena la blockchain con transacciones de un archivo '''
        # Lee el archivo de transacciones
        with open(path_transacciones, 'r') as archivo:
            transacciones = list()
            for linea in archivo:
                # Crea una transaccion por cada linea del archivo
                tr = Transaccion(*linea.strip().split())
                # Guarda la transaccion en la lista
                if len(transacciones) < largo_bloque:
                    transacciones.append(tr)
                # Si tiene suficientes transacciones, crea el bloque
                if len(transacciones) == largo_bloque:
                    self.agregar_bloque(transacciones)
                    transacciones = list()
            # Si quedan transacciones en el aire, crea un bloque para ellas
            if len(transacciones):
                self.agregar_bloque(transacciones)

    def verificar_cadena(self):
        ''' Verifica que todas las transacciones de la cadena sean válidas '''
        # Completar
        pass


if __name__ == '__main__':
    cadena = DCChain()
    cadena.llenar_cadena('transacciones.txt')
    print(cadena.verificar_cadena())

    fraude = Transaccion('21120606', '1000000', '15669833')
    cadena.head.transacciones.append(fraude)
    print(cadena.verificar_cadena())
