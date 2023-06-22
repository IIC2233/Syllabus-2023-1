import unittest
import yolanda
import api
import time
from datetime import date


N_SLEEP = 0.5


class YolandaWebsServiceTestGet(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.host = "localhost"
        self.port = 4444
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }

    def setUp(self) -> None:
        # Levantar servidor siempre antes de un test
        self.servidor = api.Server(self.host, self.port, self.database)
        self.yolanda = yolanda.Yolanda(self.host, self.port)
        self.servidor.start()
        time.sleep(N_SLEEP)

    def tearDown(self) -> None:
        # Bajar servidor despues de un test
        self.servidor.stop()
        time.sleep(N_SLEEP)

    #####################
    #      Saludar      #
    #####################
    def test_saludar_mode_1_verificar_todo(self):
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y es un hermoso día para recibir un horoscopo"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    def test_saludar_mode_2_verificar_todo(self):
        self.servidor.mode = 2
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y me da gusto escribir horoscopos"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    #####################
    #  Verificar Signo  #
    #####################
    def test_verificar_signo_tipo_respuesta(self):
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertIsInstance(respuesta, bool)

    def test_verificar_signo_si_existe(self):
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertEqual(respuesta, True)

    def test_verificar_signo_no_existe(self):
        respuesta = self.yolanda.verificar_horoscopo("UWU")
        self.assertEqual(respuesta, False)

    #####################
    #   Dar horoscopo   #
    #####################
    def test_dar_horoscopo_verificar_keys(self):
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)

    def test_dar_horoscopo_existe_verificar_status_code(self):
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta['status-code'], 200)

    def test_dar_horoscopo_existe_verificar_mensaje(self):
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database["piscis"])

    def test_dar_horoscopo_no_existe_verificar_todo(self):
        respuesta = self.yolanda.dar_horoscopo("UWU")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta['status-code'], 400)
        self.assertEqual(respuesta["mensaje"], 'El signo no existe')

    ###########################
    # Dar horoscopo aleatorio #
    ###########################
    def test_dar_horoscopo_aleatorio_mode_1(self):
        self.servidor.mode = 1
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[0]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_2(self):
        self.servidor.mode = 2
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[-1]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_3(self):
        self.servidor.mode = 3
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta['status-code'], 500)
        self.assertEqual(respuesta["mensaje"], "ups, no pude")


if __name__ == '__main__':
    unittest.main(verbosity=2)
