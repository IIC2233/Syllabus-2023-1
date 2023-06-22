from copy import copy
from functools import reduce
from itertools import groupby
from typing import Generator
from os.path import join

from utilidades import (
    Categoria, Producto, duplicador_generadores, generador_a_lista
)


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_productos(ruta: str) -> Generator:
    # TODO: Completar
    archivo = open(ruta, 'r')
    result = map(lambda char: char, archivo)
    return Producto(result)


def cargar_categorias(ruta: str) -> Generator:
    # TODO: Completar
    pass


# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------

def obtener_productos(generador_productos: Generator) -> map:
    # TODO: Completar
    pass


def obtener_precio_promedio(generador_productos: Generator) -> int:
    # TODO: Completar
    pass


def filtrar_por_medida(generador_productos: Generator,
                       medida_min: float, medida_max: float, unidad: str
                       ) -> filter:
    # TODO: Completar
    pass


def filtrar_por_categoria(generador_productos: Generator,
                          generador_categorias: Generator,
                          nombre_categoria: str) -> Generator:
    # TODO: Completar
    pass


def agrupar_por_pasillo(generador_productos: Generator) -> Generator:
    # TODO: Completar
    pass


# ----------------------------------------------------------------------------
# Parte 3: Iterables
# ----------------------------------------------------------------------------

class Carrito:
    def __init__(self, productos: list) -> None:
        self.productos = productos

    def __iter__(self):
        # TODO: Completar
        pass


class IteradorCarrito:
    def __init__(self, iterable_productos: list) -> None:
        self.productos_iterable = copy(iterable_productos)

    def __iter__(self):
        # TODO: Completar
        pass

    def __next__(self):
        # TODO: Completar
        pass


if __name__ == '__main__':
    RUTA_PRODUCTOS = join('archivos', 'productos.csv')
    [print(char) for char in cargar_productos(RUTA_PRODUCTOS)]
