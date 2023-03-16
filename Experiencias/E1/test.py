import unittest
from functions import peso_promedio_archivos_protegidos, \
    buscar_extensiones_unicas, cargar_top_archivos, buscar_archivo
from utils.loader import cargar_carpeta, obtener_archivos


class TestMain(unittest.TestCase):

    def setUp(self):
        self.carpeta = cargar_carpeta()
        self.archivos = obtener_archivos(self.carpeta, [])

    def test_peso_promedio_archivos_protegidos(self):
        peso_promedio = peso_promedio_archivos_protegidos(self.archivos)
        self.assertIsInstance(peso_promedio, float)
        self.assertEqual(peso_promedio, 37.5)

    @unittest.skip("Función todavía no corregida")
    def test_buscar_extensiones_unicas(self):
        extensiones = buscar_extensiones_unicas(self.archivos)
        self.assertIsInstance(extensiones, set)
        self.assertSetEqual(extensiones, set(["pdf", "py", "txt", "js"]))

    @unittest.skip("Función todavía no corregida")
    def test_cargar_top_archivos(self):
        top = cargar_top_archivos()
        self.assertIsInstance(top, list)
        self.assertIsInstance(top[0], list)
        self.assertListEqual(top, [
            ["apuntes.pdf", "100.36"],
            ["notas.txt", "40.16"],
            ["notas.secretas.no.mostrar.txt", "20.41"],
        ])

    @unittest.skip("Función no implementada completamente")
    def test_buscar_archivo_1(self):
        path = buscar_archivo(self.carpeta, "d3.js")
        self.assertIsInstance(path, list)
        self.assertListEqual(path, ['UC', 'semestre 1', 'IIC2026', 'd3.js'])

    @unittest.skip("Función no implementada completamente")
    def test_buscar_archivo_2(self):
        path = buscar_archivo(self.carpeta, "notas.secretas.no.mostrar.txt")
        self.assertIsInstance(path, list)
        self.assertListEqual(
            path, ['UC', 'semestre 2', 'notas.secretas.no.mostrar.txt'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
