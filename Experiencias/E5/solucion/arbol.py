class Nodo:
    def __init__(self, letra):
        self.letra = letra
        self.hijos = dict()


class ArbolPrefijos:
    def __init__(self):
        self.raiz = Nodo('')
        self.nodos = 1

    def agregar_palabra(self, palabra):
        ''' Agrega una nueva palabra al árbol de prefijos, si la palabra ya está la ignora '''
        # Comienza buscando desde la raíz
        nodo_actual = self.raiz
        # Revisa letra por letra
        for letra in palabra:
            # Si la letra está en el árbol, pasa al hijo del nodo y a la siguiente letra
            if letra in nodo_actual.hijos.keys():
                nodo_actual = nodo_actual.hijos[letra]
            # Si la letra no está en el árbol, crea un nuevo nodo con la letra y sigue avanzando
            else:
                nuevo_nodo = Nodo(letra)
                nodo_actual.hijos[letra] = nuevo_nodo
                nodo_actual = nuevo_nodo
                self.nodos += 1

    def verificar_palabra(self, palabra):
        ''' Verifica si una palabra está en el árbol de prefijos '''
        # Comienza buscando desde la raíz
        nodo_actual = self.raiz
        # Revisa letra por letra
        for letra in palabra:
            # Si la letra NO está en el árbol, la palabra tampoco lo está
            if letra not in nodo_actual.hijos.keys():
                return False
            # Si la letra está en el árbol, pasa al nodo que la tiene y a la siguiente letra
            else:
                nodo_actual = nodo_actual.hijos[letra]
        # Si todas las letras están en el árbol, la palabra lo está
        return True
    
    def listar_palabras(self):
        ''' Lista todas las palabras en el árbol '''
        # Comienza a visitar nodos partiendo por la raíz
        por_visitar = [('', self.raiz)]
        palabras = list()
        # Continúa mientras queden nodos por visitar
        while por_visitar:
            # Visita un nodo y la palabra que representa
            palabra_actual, nodo_actual = por_visitar.pop()
            # Si el nodo es una hoja, es porque aquí termina una palabra
            if not nodo_actual.hijos:
                # Guarda la palabra actual y continua visitando
                palabras.append(palabra_actual)
                continue
            # Si el nodo NO es una hoja, visita a sus hijos
            for letra, nodo in nodo_actual.hijos.items():
                por_visitar.append((palabra_actual + letra, nodo))
        return palabras
    
    def llenar_arbol(self, path_usuarios):
        ''' Agrega todas las palabras de un archivo al árbol'''
        with open(path_usuarios, 'r') as archivo:
            for linea in archivo:
                self.agregar_palabra(linea.strip())
    
    def __len__(self):
        return self.nodos


            
if __name__ == '__main__':
    arbol_prueba = ArbolPrefijos()
    print('Creamos un árbol de prueba:')
    print(f'   Cantidad de nodos: {len(arbol_prueba)}')
    print(f'   Palabras: {arbol_prueba.listar_palabras()}')
    print(f'   Verifica la palabra "prueba": {arbol_prueba.verificar_palabra("prueba")}')
    print(f'   Verifica la palabra "progra": {arbol_prueba.verificar_palabra("progra")}')

    print('Agregamos la palabra prueba:')
    arbol_prueba.agregar_palabra('prueba')
    print(f'   Cantidad de nodos: {len(arbol_prueba)}')
    print(f'   Palabras: {arbol_prueba.listar_palabras()}')
    print(f'   Verifica la palabra "prueba": {arbol_prueba.verificar_palabra("prueba")}')
    print(f'   Verifica la palabra "progra": {arbol_prueba.verificar_palabra("progra")}')


    print('Agregamos la palabra progra:')
    arbol_prueba.agregar_palabra('progra')
    print(f'   Cantidad de nodos: {len(arbol_prueba)}')
    print(f'   Palabras: {arbol_prueba.listar_palabras()}')
    print(f'   Verifica la palabra "prueba": {arbol_prueba.verificar_palabra("prueba")}')
    print(f'   Verifica la palabra "progra": {arbol_prueba.verificar_palabra("progra")}')


    print('\n\nCreamos y llenamos un arbol para 100 usuarios:')
    arbol_usuarios = ArbolPrefijos()
    arbol_usuarios.llenar_arbol('usuarios.txt')
    usuarios = arbol_usuarios.listar_palabras()
    cuenta = 0
    for usuario in usuarios:
        cuenta += len(usuario)
    print(f'   Cantidad de carateres de los usuarios: {cuenta}')
    print(f'   Cantidad de nodos en el arbol: {len(arbol_usuarios)}')


    print('\n\nCreamos y llenamos un arbol para 10,000 usuarios:')
    arbol_usuarios = ArbolPrefijos()
    arbol_usuarios.llenar_arbol('usuarios_long.txt')
    usuarios = arbol_usuarios.listar_palabras()
    cuenta = 0
    for usuario in usuarios:
        cuenta += len(usuario)
    print(f'   Cantidad de carateres de los usuarios: {cuenta:,}')
    print(f'   Cantidad de nodos en el arbol: {len(arbol_usuarios):,}')
    



    