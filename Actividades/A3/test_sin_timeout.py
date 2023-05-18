from collections import defaultdict
from functools import wraps
from io import StringIO
import unittest
from unittest.mock import patch

from equipo import Jugador, Equipo




N_SECOND = 0.2


class VerificarEquipo(unittest.TestCase):
    
    def setUp(self) -> None:
        self.equipo = Equipo()
        self.equipo.jugadores = {
            0: Jugador('Alan', 2),
            1: Jugador('Alberto', 3),
            2: Jugador('Alejandra', 5),
            3: Jugador('Alex', 8),
            4: Jugador('Alonso', 13),
            5: Jugador('Alba', 21),
            6: Jugador('Alicia', 34),
            7: Jugador('Alfredo', 55),
            8: Jugador('Alma', 16),
            9: Jugador('Aldo', 89)
        }
        adyacencia = {
            0: {1},
            1: {0, 2, 3},
            2: {1, 3},
            3: {1},
            4: {5},
            5: {4, 6},
            6: {4, 5},
            7: {8},
            8: {9},
            9: set()
        }
        self.equipo.dict_adyacencia = defaultdict(set)
        for key, value in adyacencia.items():
            self.equipo.dict_adyacencia[key] = value

    
    def test_agregar_jugador_correcto(self):
        new = Jugador('Alejo', 10)
        ret = self.equipo.agregar_jugador(10, new)
        self.assertEqual(len(self.equipo.jugadores), 11)
        self.assertTrue(ret)

    
    def test_agregar_jugador_fallido(self):
        new = Jugador('Alejo', 10)
        ret = self.equipo.agregar_jugador(9, new)
        self.assertEqual(len(self.equipo.jugadores), 10)
        self.assertFalse(ret)

    
    def test_agregar_vecinos_correcto(self):
        ret = self.equipo.agregar_vecinos(8, [7, 9])
        self.assertSetEqual(self.equipo.dict_adyacencia[8], {7, 9})
        self.assertEqual(len(self.equipo.dict_adyacencia[9]), 0)
        self.assertEqual(ret, 1)

    
    def test_agregar_vecinos_fallido(self):
        ret = self.equipo.agregar_vecinos(10, [])
        self.assertEqual(ret, -1)

    
    def test_mejor_amigo_correcto(self):
        ret = self.equipo.mejor_amigo(5)
        self.assertEqual(ret, self.equipo.jugadores[4])

    
    def test_mejor_amigo_fallido(self):
        ret = self.equipo.mejor_amigo(9)
        self.assertIsNone(ret)

    
    def test_peor_companero_correcto(self):
        ret = self.equipo.peor_compañero(0)
        self.assertEqual(ret, self.equipo.jugadores[9])

    
    def test_peor_companero_fallido(self):
        self.equipo.jugadores = {9: Jugador('Aldo', 89)}
        self.equipo.dict_adyacencia = {9: {}}
        ret = self.equipo.peor_compañero(9)
        self.assertIsNone(ret)

    
    def test_peor_conocido_unico(self):
        ret = self.equipo.peor_conocido(7)
        self.assertEqual(ret, self.equipo.jugadores[8])

    
    def test_peor_conocido_simple(self):
        ret = self.equipo.peor_conocido(4)
        self.assertEqual(ret, self.equipo.jugadores[6])

    
    def test_peor_conocido_complejo(self):
        ret = self.equipo.peor_conocido(0)
        self.assertEqual(ret, self.equipo.jugadores[3])

    
    def test_peor_conocido_none(self):
        ret = self.equipo.peor_conocido(9)
        self.assertIsNone(ret)

    
    def test_distancia_self(self):
        ret = self.equipo.distancia(7, 7)
        self.assertEqual(ret, 0)

    
    def test_distancia_simple(self):
        ret = self.equipo.distancia(7, 8)
        self.assertEqual(ret, 1)

    
    def test_distancia_complejo(self):
        ret = self.equipo.distancia(0, 3)
        self.assertEqual(ret, 2)
        ret = self.equipo.distancia(0, 2)
        self.assertEqual(ret, 2)

    
    def test_distancia_none(self):
        ret = self.equipo.distancia(0, 9)
        self.assertEqual(ret, -1)


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
