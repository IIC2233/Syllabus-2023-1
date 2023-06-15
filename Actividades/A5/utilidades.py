from collections import namedtuple
from itertools import tee


Producto = namedtuple('Producto', 'id_producto, nombre, precio, pasillo, medida, unidad_medida')
Categoria = namedtuple('Categoria', 'nombre_categoria, id_producto')

generador_a_lista = lambda generador: list(generador)
duplicador_generadores = tee
