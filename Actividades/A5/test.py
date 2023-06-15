import unittest
import funciones
from io import StringIO
from unittest.mock import patch
import inspect
from typing import Generator
from os.path import join
from utilidades import Categoria, Producto, generador_a_lista
from itertools import groupby


RUTA_PRODUCTOS = join('archivos', 'productos.csv')
RUTA_CATEGORIAS = join('archivos', 'categorias.csv')

class ComandoProhibidoError(BaseException):
    def __init__(self, *args: object) -> None:
        probibidos = args[0]
        mensaje = "Se utiliza alguno de estos elementos en la función: "
        mensaje += ", ".join(probibidos)
        super().__init__(mensaje, *args[1:])


def usa_comando_prohibido(func, prohibidos):
    codigo_fuente = inspect.getsource(func).replace("\\", " ")
    line = codigo_fuente.strip()
    for prohibido in prohibidos:
        if prohibido + " " in line:
            raise ComandoProhibidoError(prohibidos)
        if prohibido + "\t" in line:
            raise ComandoProhibidoError(prohibidos)
        if prohibido + "\r" in line:
            raise ComandoProhibidoError(prohibidos)

def usa_comando_esperado(func, comandos):
    codigo_fuente = inspect.getsource(func).replace("\\", " ")
    line = codigo_fuente.strip()
    for prohibido in comandos:
        if prohibido + " " in line:
            return True
        if prohibido + "\t" in line:
            return True
        if prohibido + "\r" in line:
            return True
    return False



class TestCargarDatos(unittest.TestCase):

    def test_cargar_productos(self):
        datos = funciones.cargar_productos(RUTA_PRODUCTOS)
    
        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        first = Producto(1, "Arroz", 1990, "Pasillo 1", 1000, "gr")
        last = Producto(17, "Mantequilla", 1490, "Pasillo 2", 200, "gr")
        self.assertSequenceEqual(lista_datos[0], first)
        self.assertSequenceEqual(lista_datos[-4], last)
    
    def test_cargar_categorias(self):
        datos = funciones.cargar_categorias(RUTA_CATEGORIAS)
    
        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        first = Categoria("Cereales", 1)
        last = Categoria("Endulzantes", 20)
        self.assertSequenceEqual(lista_datos[0], first)
        self.assertSequenceEqual(lista_datos[-2], last)


class TestConsultas(unittest.TestCase):
    
    def generador_producto(self):
        yield Producto(1, "Arroz", 1990, "Pasillo 1", 1000, "gr")
        yield Producto(17, "Mantequilla", 1490, "Pasillo 2", 200, "gr")
    
    def test_obtener_productos(self):
        datos = funciones.obtener_productos(self.generador_producto())
        self.assertIsInstance(datos, map)
        lista_datos = list(datos)
        # No usa for
        self.assertSequenceEqual(lista_datos, ["Arroz", "Mantequilla"])
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while"])
    
    def test_obtener_precio_promedio(self):
        promedio = funciones.obtener_precio_promedio(self.generador_producto())
        self.assertIsInstance(promedio, int)
        self.assertEqual(promedio, 1740)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])
    
    
class TestFiltros(unittest.TestCase):
    
    def generador_producto(self):
        yield Producto(1, "Arroz", 1990, "Pasillo 1", 1000, "gr")
        yield Producto(17, "Mantequilla", 1490, "Pasillo 2", 200, "gr")
    
    def generador_categoria(self):
        yield Categoria("Cereales", 1)
        yield Categoria("Cereales", 17)

    def test_filtrar_por_medida_max(self):
        datos = funciones.filtrar_por_medida(self.generador_producto(), 0, 300, "gr")
        self.assertIsInstance(datos, filter)
        lista_datos = list(datos)
        producto = Producto(17, "Mantequilla", 1490, "Pasillo 2", 200, "gr")
        self.assertSequenceEqual(lista_datos, [producto])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])
    
    def test_filtrar_por_medida_min(self):
        datos = funciones.filtrar_por_medida(self.generador_producto(), 500, 1400, "gr")
        self.assertIsInstance(datos, filter)
        lista_datos = list(datos)
        producto = Producto(1, "Arroz", 1990, "Pasillo 1", 1000, "gr")
        self.assertSequenceEqual(lista_datos, [producto])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])

    def test_filtrar_por_medida_vacio(self):
        datos = funciones.filtrar_por_medida(self.generador_producto(), 0, 2000, "ml")
        self.assertIsInstance(datos, filter)
        lista_datos = list(datos)
        self.assertSequenceEqual(lista_datos, [])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])

    def test_filtrar_por_categoria(self):
        productos = self.generador_producto()
        categorias = self.generador_categoria()
        datos = funciones.filtrar_por_categoria(productos, categorias, "Cereales")

        lista_datos = list(datos)
        resultado_productos = list(self.generador_producto())
        self.assertSequenceEqual(lista_datos, resultado_productos)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])
    
    def test_filtrar_por_categoria_vacio(self):
        productos = self.generador_producto()
        categorias = self.generador_categoria()
        datos = funciones.filtrar_por_categoria(productos, categorias, "No existe")
        self.assertIsInstance(datos, filter)
        
        lista_datos = list(datos)
        self.assertSequenceEqual(lista_datos, [])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])


class TestBonus(unittest.TestCase):
    
    def generador_producto(self):
        yield Producto(1, "Arroz", 1990, "Pasillo 1", 1000, "gr")
        yield Producto(17, "Mantequilla", 1490, "Pasillo 2", 200, "gr")

    def test_agrupar_por_pasillo(self):
        productos = self.generador_producto()
        datos = funciones.agrupar_por_pasillo(productos)
        self.assertIsInstance(datos, groupby)

        lista_datos = [(x[0], list(x[1])) for x in datos]
        productos = list(self.generador_producto())

        self.assertEqual(lista_datos[0][0], "Pasillo 1")
        self.assertSequenceEqual(lista_datos[0][1], [productos[0]])

        self.assertEqual(lista_datos[1][0], "Pasillo 2")
        self.assertSequenceEqual(lista_datos[1][1], [productos[1]])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while", "list", "dict", "set"])

class TestIterables(unittest.TestCase):
    
    def generador_producto(self):
        yield Producto(1, "Arroz", 200, "Pasillo 1", 1000, "gr")
        yield Producto(5, "Takoyaki", 100, "Pasillo 1", 1000, "ml")
        yield Producto(17, "Mantequilla", 999, "Pasillo 2", 200, "gr")
    

    def test_Carrito_iter(self):
        productos = list(self.generador_producto())
        iterador = iter(funciones.Carrito(productos))
        self.assertIsInstance(iterador, funciones.IteradorCarrito)

        self.assertSequenceEqual(iterador.productos_iterable, productos)
        # No usa for
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while"])
    
    
    def test_IteradorCarrito_iter(self):
        productos = list(self.generador_producto())
        iterador = iter(funciones.IteradorCarrito(productos))
        self.assertIsInstance(iterador, funciones.IteradorCarrito)

        self.assertSequenceEqual(iterador.productos_iterable, productos)
        # No usa for
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while"])
    
    def test_IteradorCarrito_next(self):
        productos = list(self.generador_producto())
        carrito = funciones.IteradorCarrito(productos)

        producto_1 = next(carrito)
        self.assertSequenceEqual(producto_1, productos[1])

        producto_2 = next(carrito)
        self.assertSequenceEqual(producto_2, productos[0])
        
        producto_3 = next(carrito)
        self.assertSequenceEqual(producto_3, productos[2])
        
        self.assertRaises(StopIteration, next, carrito)

        # No usa for
        usa_comando_prohibido(funciones.obtener_productos, ["for", "while"])
    
if __name__ == '__main__':
    # with patch('sys.stdout', new=StringIO()):
    unittest.main(verbosity=2)
