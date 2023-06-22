from functools import wraps
import signal
import platform
import unittest
import yolanda
import api
import time


class YolandaWebsServiceTestWithAutorization(unittest.TestCase):
    host = "localhost"
    port = 4444
    database = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
        "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
    }
    servidor = api.Server(host, port, database, mode=2)
    yolanda = yolanda.Yolanda(host, port)
    servidor.start()

    def setUp(self) -> None:
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }

    #####################
    # Agregar horoscopo #
    #####################
    
    def test_agregar_horoscopo_no_autorizado(self):
        respuesta = self.yolanda.agregar_horoscopo(
            "leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Agregar horoscopo no autorizado")

    
    def test_agregar_horoscopo_signo_ya_existe(self):
        respuesta = self.yolanda.agregar_horoscopo(
            "leo", "grande messi", "morenoiic2233")
        self.assertEqual(respuesta, "El signo ya existe, no puedes modificarlo")

    
    def test_agregar_horoscopo_signo_mensaje_muy_corto(self):
        respuesta = self.yolanda.agregar_horoscopo("leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    
    def test_agregar_horoscopo_ok_verificar_respuesta(self):
        mensaje = "grande messi"
        respuesta = self.yolanda.agregar_horoscopo(
            "Sagitario", mensaje, "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandaAPI ha sido actualizada")

    
    def test_agregar_horoscopo_ok_verificar_base_datos(self):
        mensaje = "grande messi"
        self.yolanda.agregar_horoscopo("Sagitario", mensaje, "morenoiic2233")
        self.assertIn("Sagitario", self.servidor.database)
        self.assertEqual(mensaje, self.servidor.database["Sagitario"])

    ########################
    # Actualizar horoscopo #
    ########################
    
    def test_actualizar_horoscopo_no_autorizado(self):
        respuesta = self.yolanda.actualizar_horoscopo(
            "leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Editar horoscopo no autorizado")

    
    def test_actualizar_horoscopo_signo_no_existe(self):
        respuesta = self.yolanda.actualizar_horoscopo(
            "messi", "grande messi", "morenoiic2233")
        self.assertEqual(respuesta, "El signo no existe")

    
    def test_actualizar_horoscopo_signo_mensaje_muy_corto(self):
        respuesta = self.yolanda.actualizar_horoscopo(
            "leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    
    def test_actualizar_horoscopo_ok_verificar_respuesta(self):
        mensaje = "grande messi"
        respuesta = self.yolanda.actualizar_horoscopo(
            "leo", mensaje, "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandaAPI ha sido actualizada")

    
    def test_actualizar_horoscopo_ok_verificar_base_datos(self):
        mensaje = "grande messi"
        self.yolanda.actualizar_horoscopo("leo", mensaje, "morenoiic2233")
        self.assertEqual(mensaje, self.servidor.database["leo"])

    ##################
    # Eliminar signo #
    ##################
    
    def test_eliminar_signo_no_autorizado(self):
        respuesta = self.yolanda.eliminar_signo("leo", "FAIL")
        self.assertEqual(respuesta, "Eliminar signo no autorizado")

    
    def test_eliminar_signo_signo_no_existe(self):
        respuesta = self.yolanda.eliminar_signo("messi", "morenoiic2233")
        self.assertEqual(respuesta, "El signo no existe")

    
    def testeliminar_signo_ok_verificar_respuesta(self):
        respuesta = self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandaAPI ha sido actualizada")

    
    def test_eliminar_signo_ok_verificar_base_datos(self):
        self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertNotIn("leo", self.servidor.database)


if __name__ == '__main__':
    unittest.main(verbosity=2)
