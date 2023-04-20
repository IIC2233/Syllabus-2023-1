from threading import Event, Thread
from io import StringIO
from unittest.mock import patch
import unittest

from carrera import Corredor


MESSAGE = "La función no finalizó a tiempo. Probablemente quedó en un loop infinito"


class FakeLock:

    def __init__(self) -> None:
        self._locked = False
        self.accessed = False
        self.blocking = True
        
    def acquire(self, blocking=True):
        self.blocking = blocking
        if not self._locked:
            self.accessed = True
            self._locked = True
            return True

        if self._locked:
            return False
        
    def release(self):
        if self._locked:
            self._locked = False
        return RuntimeError('release unlocked lock')

    def locked(self):
        return self._locked
    
    def __enter__(self, *args, **kwargs):
        self.acquire()
        return args, kwargs

    def __exit__(self, *args, **kwargs):
        self.release()
        return args, kwargs


class VerificarCorredor(unittest.TestCase):

    def setUp(self) -> None:
        tortuga = FakeLock()
        lock_verificar_tortuga = FakeLock()
        senal_inicio = Event()
        senal_fin = Event()

        # Instancia los corredores y la carrera
        self.j1 = Corredor('Juan', tortuga, senal_inicio, senal_fin, lock_verificar_tortuga)
        self.j2 = Corredor('Pepe', tortuga, senal_inicio, senal_fin, lock_verificar_tortuga)

        self.j1.asignar_rival(self.j1.ser_notificado_por_robo)

        self.j1._Corredor__velocidad = 10
        Corredor.TIEMPO_ESPERA = 0
        Corredor.PORCENTAJE_MIN = 100
        Corredor.PORCENTAJE_MAX = 100
        Corredor.PROBABILIDAD_ROBAR = 1

    def test_corredor_clases_thread(self):
        self.assertIn(Thread, Corredor.__mro__)

    def test_corredor_valor_daemon(self):
        self.assertTrue(self.j1.daemon)
        self.assertTrue(self.j2.daemon)

    def test_verificar_avanzar(self):
        self.assertEqual(self.j1.posicion, 0)
        self.j1.avanzar()
        self.assertEqual(self.j1.posicion, 10)

    def test_intentar_capturar_tortuga_verificar_blocking(self):
        self.assertTrue(self.j1.lock_tortuga.blocking)
        self.j1.intentar_capturar_tortuga()
        self.assertFalse(self.j1.lock_tortuga.blocking)

    def test_intentar_capturar_tortuga_verificar_lock(self):
        self.assertFalse(self.j1.tiene_tortuga)
        self.j1.intentar_capturar_tortuga()
        self.assertTrue(self.j1.lock_tortuga.locked())

    def test_intentar_capturar_tortuga_resultado_exitoso(self):
        self.assertFalse(self.j1.tiene_tortuga)
        self.j1.intentar_capturar_tortuga()
        self.assertTrue(self.j1.tiene_tortuga)

    def test_intentar_capturar_tortuga_resultado_fallido(self):
        self.j1.lock_tortuga.acquire()
        self.assertFalse(self.j1.tiene_tortuga)
        self.j1.intentar_capturar_tortuga()
        self.assertFalse(self.j1.tiene_tortuga)

    def test_perder_tortuga_verificar_tortuga(self):
        self.j1.tiene_tortuga = True
        self.j1.perder_tortuga()
        self.assertFalse(self.j1.tiene_tortuga)

    def test_perder_tortuga_verificar_lock(self):
        self.j1.lock_tortuga.acquire()
        self.assertTrue(self.j1.lock_tortuga.locked())
        self.j1.perder_tortuga()
        self.assertFalse(self.j1.lock_tortuga.locked())

    def test_robar_tortuga_notifica_robo(self):
        with patch('carrera.Corredor.perder_tortuga') as mock:
            self.j1.robar_tortuga()
            mock.assert_called()

    def test_robar_tortuga_obtiene_tortuga(self):
        with patch('carrera.Corredor.perder_tortuga'):
            self.assertFalse(self.j1.tiene_tortuga)
            self.j1.robar_tortuga()
            self.assertTrue(self.j1.tiene_tortuga)

    def test_robar_tortuga_obtiene_lock(self):
        with patch('carrera.Corredor.perder_tortuga'):
            self.j1.robar_tortuga()
            self.assertTrue(self.j1.lock_tortuga.locked())
    
    def test_robar_tortuga_robo_exitoso(self):
        with patch('carrera.Corredor.perder_tortuga'):
            self.assertTrue(self.j1.robar_tortuga())
    
    def test_robar_tortuga_robo_fallido(self):
        with patch('carrera.Corredor.perder_tortuga'):
            self.j1.PROBABILIDAD_ROBAR = 0
            self.assertFalse(self.j1.robar_tortuga())

    def test_correr_primera_mitad_verificar_resultado(self):
        self.assertEqual(self.j1.posicion, 0)
        test_thread = Thread(target=self.j1.correr_primera_mitad, daemon=True)
        test_thread.start()
        test_thread.join(timeout=2)
        self.assertFalse(test_thread.is_alive(), MESSAGE)
        self.assertGreaterEqual(self.j1.posicion, 50)

    def correr_segunda_mitad(self):
        self.resultado_carrera = "None"
        def correr():
            self.resultado_carrera = self.j1.correr_segunda_mitad()

        test_thread = Thread(target=correr, daemon=True)
        test_thread.start()
        test_thread.join(timeout=1)
        self.assertFalse(test_thread.is_alive(), MESSAGE)
        return self.resultado_carrera

    def test_correr_segunda_mitad_verificar_avance(self):
        self.j1.posicion = 50
        self.correr_segunda_mitad()
        self.assertGreaterEqual(self.j1.posicion, 51)

    def test_correr_segunda_mitad_verificar_uso_lock(self):
        self.assertFalse(self.j1.lock_verificar_tortuga.accessed)
        self.correr_segunda_mitad()
        self.assertTrue(self.j1.lock_verificar_tortuga.accessed)

    def test_correr_segunda_mitad_carrera_terminada_avanza_maximo_1_vez(self):
        self.j1.senal_fin.set()
        self.correr_segunda_mitad()
        DISTANCIA_MAXIMA = 20
        self.assertLessEqual(self.j1.posicion, DISTANCIA_MAXIMA)

    def test_correr_segunda_mitad_carrera_perdida_verficar_retorno(self):
        self.j1.senal_fin.set()
        resultado = self.correr_segunda_mitad()
        self.assertFalse(resultado)

    def test_correr_segunda_mitad_carrera_ganada_verficar_retorno(self):
        self.j1.posicion = 100
        self.j1.tiene_tortuga = True
        resultado = self.correr_segunda_mitad()
        self.assertTrue(resultado)

    def test_correr_segunda_mitad_carrera_ganada_verificar_senal(self):
        self.j1.posicion = 100
        self.j1.tiene_tortuga = True
        self.correr_segunda_mitad()
        self.assertTrue(self.j1.senal_fin.is_set())

    def test_correr_segunda_mitad_carrera_ganada_verificar_lock(self):
        self.j1.posicion = 100
        self.j1.tiene_tortuga = True
        self.j1.lock_tortuga.acquire()
        self.correr_segunda_mitad()
        self.assertFalse(self.j1.lock_tortuga.locked())

    def test_correr_segunda_mitad_carrera_verificar_robar_tortuga(self):
        self.called = False
        def stop():
            self.called = True
            self.j1._Corredor__correr = False

        with patch('carrera.Corredor.robar_tortuga', new_callable=stop) as mock:
            self.j1.tiene_tortuga = False
            self.correr_segunda_mitad()
            self.assertTrue(self.called)

    def test_run_verificar_senal_inicio(self):
        with patch('carrera.Corredor.correr_primera_mitad'):
            with patch('carrera.Corredor.correr_segunda_mitad'):
                with patch('threading.Event.wait') as mock:
                    self.j1.run()
                    mock.assert_called()

    def test_run_verificar_correr_primera_mitad(self):
        self.j1._Corredor__correr = False
        self.j1.senal_inicio.set()
        with patch('carrera.Corredor.correr_segunda_mitad'):
            with patch('carrera.Corredor.correr_primera_mitad') as mock:
                self.j1.run()
                mock.assert_called()

    def test_run_verificar_intento_captura(self):
        self.j1._Corredor__correr = False
        self.j1.senal_inicio.set()
        with patch('carrera.Corredor.correr_primera_mitad'):
            with patch('carrera.Corredor.correr_segunda_mitad'):
                with patch('carrera.Corredor.intentar_capturar_tortuga') as mock:
                    self.j1.run()
                    mock.assert_called()

    def test_run_verificar_correr_segunda_mitad(self):
        self.j1._Corredor__correr = False
        self.j1.senal_inicio.set()
        with patch('carrera.Corredor.correr_primera_mitad'):
            with patch('carrera.Corredor.correr_segunda_mitad') as mock:
                self.j1.run()
                mock.assert_called()


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
    # unittest.main()