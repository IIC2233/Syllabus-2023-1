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
        # Completar
        pass

    def verificar_palabra(self, palabra):
        ''' Verifica si una palabra está en el árbol de prefijos '''
        # Completar
        pass
    
    def listar_palabras(self):
        ''' Lista todas las palabras en el árbol '''
        # Completar
        pass
    
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
    



    