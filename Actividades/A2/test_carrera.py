from threading import Event, Thread
from io import StringIO
from unittest.mock import patch
import unittest

from carrera import Carrera, Corredor


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


class VerificarCarrera(unittest.TestCase):

    def setUp(self) -> None:
        tortuga = FakeLock()
        lock_verificar_tortuga = FakeLock()
        senal_inicio = Event()
        senal_fin = Event()

        self.j1 = Corredor('Juan', tortuga, senal_inicio, senal_fin, lock_verificar_tortuga)
        self.j2 = Corredor('Pepe', tortuga, senal_inicio, senal_fin, lock_verificar_tortuga)

        self.j1.asignar_rival(self.j1.ser_notificado_por_robo)

        self.j1._Corredor__velocidad = 10
        Corredor.TIEMPO_ESPERA = 0
        Corredor.PORCENTAJE_MIN = 100
        Corredor.PORCENTAJE_MAX = 100
        Corredor.PROBABILIDAD_ROBAR = 1

        self.carrera = Carrera(self.j1, self.j2, senal_inicio, senal_fin)

    def test_carrera_clases_thread(self):
        self.assertIn(Thread, Carrera.__mro__)

    def test_carrera_valor_daemon(self):
        self.assertFalse(self.carrera.daemon)

    @patch('threading.Thread.join')
    def test_empezar_verificar_start(self, new_join):
        with patch('threading.Thread.start') as mock:
            self.carrera.empezar()
            mock.assert_called()
    
    @patch('threading.Thread.start')
    def test_empezar_verificar_join(self, new_start):
        with patch('threading.Thread.join') as mock:
            self.carrera.empezar()
            mock.assert_called()

    @patch('threading.Thread.start')
    @patch('threading.Thread.join')
    def test_empezar_verificar_ganadores(self, new_join, new_start):
        self.j1.tiene_tortuga = True
        self.j2.tiene_tortuga = False
        winner = self.carrera.empezar()
        self.assertEqual(winner, self.j1.name)

        self.j1.tiene_tortuga = False
        self.j2.tiene_tortuga = True
        winner = self.carrera.empezar()
        self.assertEqual(winner, self.j2.name)

    def test_run_verificar_start_corredores(self):
        with patch('threading.Thread.start') as mock:
            self.carrera.senal_fin.set()
            self.carrera.run()
            self.assertEqual(mock.call_count, 2)

    @patch('threading.Thread.start')
    def test_run_verificar_senal_inicio(self, new_start):
            self.assertFalse(self.carrera.senal_inicio.is_set())
            self.carrera.senal_fin.set()
            self.carrera.run()
            self.assertTrue(self.carrera.senal_inicio.is_set())

    @patch('threading.Thread.start')
    def test_run_verificar_senal_fin(self, new_start):
        with patch('threading.Event.wait') as mock:
            self.carrera.run()
            mock.assert_called()


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
    # unittest.main()