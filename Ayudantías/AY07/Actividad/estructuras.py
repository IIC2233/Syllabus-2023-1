from collections import deque


def explorador(arbol, buscado, algoritmo):

    if algoritmo == "BFS":
        resultado = arbol.recorridoBFS(buscado)
    elif algoritmo == "DFS":
        resultado = arbol.recorridoDFS(buscado)

    if resultado is None:
        print(f"ERROR: No se encontró el archivo: {buscado}")
    else:
        print(f"la ruta es: {str(resultado)}")



class NodoLista:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return self.valor


class ListaLigada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.largo = 0

    def append(self, nodo):
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = nodo
            self.ultimo = nodo
        self.largo += 1

    def insert(self, nodo, posicion):
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo

        elif posicion >= self.largo:
            self.ultimo.siguiente = nodo
            self.ultimo = nodo

        elif posicion == 0:
            nodo.siguiente = self.primero
            self.primero = nodo

        else:
            anterior = self.primero
            for _ in range(posicion-1):
                anterior = anterior.siguiente
            nodo.siguiente = anterior.siguiente
            anterior.siguiente = nodo

        self.largo += 1

    def pop(self):
        self.largo -= 1
        nodo_actual = self.primero
        if nodo_actual is not None:
            self.primero = nodo_actual.siguiente
            if self.primero is None:
                self.ultimo = None
        return nodo_actual

    def __str__(self):
        nodo = self.primero
        text = nodo.valor  # .strip("/")
        nodo = nodo.siguiente
        while nodo is not None:
            # con flechita
            # text += " -> " + nodo.valor.strip("/")

            # modo ruta
            text += nodo.valor
            nodo = nodo.siguiente
        return text


class Arbol:
    id_nodo = 0

    def __init__(self, valor=None, padre=None):
        self.id_nodo = Arbol.id_nodo
        Arbol.id_nodo += 1
        self.padre = padre
        self.valor = valor
        self.hijos = {}
        self.actualizar_profundidad()

    def actualizar_profundidad(self):
        if self.padre:
            self.profundidad = self.padre.profundidad + 1
        else:
            self.profundidad = 0

    def obtener_nodo_por_id(self, id_nodo):
        # Caso base: ¡Lo encontramos!
        if self.id_nodo == id_nodo:
            return self

        # Buscamos recursivamente entre los hijos
        for hijo in self.hijos.values():
            nodo = hijo.obtener_nodo_por_id(id_nodo)
            # Si lo encontró, lo retornamos
            if nodo is not None:
                return nodo

        # Si no lo encuentra, retorna None
        return None

    def obtener_nodo_por_valor(self, valor):
        # Caso base: ¡Lo encontramos!
        if self.valor == valor:
            return self

        # Buscamos recursivamente entre los hijos
        for hijo in self.hijos.values():
            nodo = hijo.obtener_nodo_por_valor(valor)
            # Si lo encontró, lo retornamos
            if nodo is not None:
                return nodo

        # Si no lo encuentra, retorna None
        return None

    def agregar_nodo(self, valor, valor_padre):
        # Primero, tenemos que encontrar al padre, si no existe no se hace nada
        padre = self.obtener_nodo_por_valor(valor_padre)

        if padre is None:
            return

        # Creamos el nodo

        nodo = type(self)(valor, padre) # Esto es para evitar problemas en herencia

        # Agregamos el nodo como hijo de su padre
        padre.hijos[nodo.id_nodo] = nodo


    def recorridoBFS(self, buscado):
        cola = deque()
        cola.append(self)
        encontrado = False
        # Mientras queden nodos por visitar en la cola
        while len(cola) > 0:
            # Extraemos el primero de la cola
            nodo_actual = cola.popleft()
            if nodo_actual.valor == buscado:
                encontrado = True

            # Agregamos todos los nodos hijos a la cola
            for hijo in nodo_actual.hijos.values():
                cola.append(hijo)

        if not encontrado:
            return None

        else:
            lugar = self.obtener_nodo_por_valor(buscado)
            return self.creador_camino(lugar)


    def recorridoDFS(self, buscado):
        stack = deque()
        stack.append(self)
        encontrado = False
        # Mientras queden nodos por visitar en la cola
        while len(stack) > 0:
            # Extraemos el ultimo de la cola
            nodo_actual = stack.pop()
            if nodo_actual.valor == buscado:
                encontrado = True

            # Agregamos todos los nodos hijos a la cola
            for hijo in nodo_actual.hijos.values():
                stack.append(hijo)

        if not encontrado:
            return None

        else:
            lugar = self.obtener_nodo_por_valor(buscado)
            return self.creador_camino(lugar)


    def creador_camino(self, lugar):
        camino = ListaLigada()
        while lugar is not None:
            
            nodo = NodoLista(lugar.valor)
            print(lugar.valor)
            camino.insert(nodo, 0)
            lugar = lugar.padre
        return camino


    def diagrama_descendencia(self, indent=0):
        diagrama = f"{self.profundidad}[{self.valor}]"
        for hijo in self.hijos.values():
            diagrama += f"\n{ indent *'    ' }└───{ hijo.diagrama_descendencia(indent + 1) }"
        return diagrama

    # Equivalente a __str__. Imprime la llave del nodo junto con su valor
    def __repr__(self):
        return self.diagrama_descendencia()



