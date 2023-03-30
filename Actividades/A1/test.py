from abc import ABC, abstractmethod
import unittest
from unittest.mock import patch
import types

from clases import Animal, Terrestre, Acuatico, Perro, Pez, Ornitorrinco

class VerificarClaseAnimal(unittest.TestCase):

    def test_no_puede_instanciarse(self):
        self.assertRaises(TypeError, Animal, 10)

    def test_metodo_abstracto_definido(self):
        self.assertIn('desplazarse', Animal.__abstractmethods__)

    def test_herencia_abc(self):
        self.assertIn(ABC, Animal.__mro__)

    def test_property_energia_definida(self):
        self.assertIsInstance(Animal.energia, property)

class VerificarClaseTerrestre(unittest.TestCase):

    def test_energia_gastada_definida(self):
        self.assertIsInstance(Terrestre.energia_gastada_por_desplazamiento, types.FunctionType)
    
    def test_metodo_desplazarse_definido(self):
        self.assertIsInstance(Terrestre.desplazarse, types.FunctionType)

    def test_herencia_abc(self):
        self.assertIn(ABC, Terrestre.__mro__)


class VerificarClaseAcuatico(unittest.TestCase):

    def test_energia_gastada_definida(self):
        self.assertIsInstance(Acuatico.energia_gastada_por_desplazamiento, types.FunctionType)
    
    def test_metodo_desplazarse_definido(self):
        self.assertIsInstance(Acuatico.desplazarse, types.FunctionType)

    def test_herencia_abc(self):
        self.assertIn(ABC, Acuatico.__mro__)


class VerificarClasePerro(unittest.TestCase):

    def setUp(self) -> None:
        self.perro = Perro(nombre='p', raza='a', peso=8)

    def test_llama_init_terrestre(self):
        with patch('clases.Terrestre.__init__') as mock:
            mock.return_value = None
            Perro(nombre='o', peso=10, raza='rojo')
            mock.assert_called_once()

    def test_llama_init_animal(self):
        with patch('clases.Animal.__init__') as mock:
            mock.return_value = None
            Perro(nombre='o', peso=10, raza='rojo')
            mock.assert_called_once()

    def test_setter_permite_poner_valor_valido(self):
        self.perro.energia = 55
        self.assertEqual(self.perro.energia, 55)

    def test_energia_no_puede_ser_menor_0(self):
        self.perro.energia = -10
        self.assertEqual(self.perro.energia, 0)

    def test_energia_gastada_correcto(self):
        self.assertEqual(self.perro.energia_gastada_por_desplazamiento(), 40)

    def test_patas(self):
        self.assertEqual(self.perro.cantidad_patas, 4)

    def test_raza(self):
        self.assertEqual(self.perro.raza, 'a')

    def test_peso(self):
        self.assertEqual(self.perro.peso, 8)

    def test_desplazarse(self):
        self.assertEqual(self.perro.energia, 100)
        self.perro.desplazarse()
        self.assertEqual(self.perro.energia, 60)

    def test_metodo_ladrar(self):
        self.assertIsInstance(self.perro.ladrar, types.MethodType)

    def test_herencia_terrestre(self):
        self.assertIn(Terrestre, Perro.__mro__)

    def test_herencia_acuatico(self):
        self.assertNotIn(Acuatico, Perro.__mro__)

    def test_herencia_animal(self):
        self.assertIn(Animal, Perro.__mro__)

    def test_herencia_pez(self):
        self.assertNotIn(Pez, Perro.__mro__)


class VerificarClasePez(unittest.TestCase):

    def setUp(self) -> None:
        self.pez = Pez(nombre='z', color='rojo', peso=1)

    def test_llama_init_animal(self):
        with patch('clases.Animal.__init__') as mock:
            mock.return_value = None
            Pez(nombre='o', peso=10, color='rojo')
            mock.assert_called_once()

    def test_llama_init_pez(self):
        with patch('clases.Pez.__init__') as mock:
            mock.return_value = None
            Pez(nombre='o', peso=10, color='rojo')
            mock.assert_called_once()

    def test_energia_no_puede_ser_menor_0(self):
        self.pez.energia = -10
        self.assertEqual(self.pez.energia, 0)

    def test_setter_permite_poner_valor_valido(self):
        self.pez.energia = 55
        self.assertEqual(self.pez.energia, 55)

    def test_energia_gastada_correcto(self):
        self.assertEqual(self.pez.energia_gastada_por_desplazamiento(), 2)

    def test_color(self):
        self.assertEqual(self.pez.color, 'rojo')

    def test_peso(self):
        self.assertEqual(self.pez.peso, 1)

    def test_nombre(self):
        self.assertEqual(self.pez.nombre, 'z')

    def test_desplazarse(self):
        self.assertEqual(self.pez.energia, 100)
        self.pez.desplazarse()
        self.assertEqual(self.pez.energia, 98)

    def test_metodo_nadar(self):
        self.assertIsInstance(self.pez.nadar, types.MethodType)


class VerificarClaseOrnitorrinco(unittest.TestCase):

    def setUp(self) -> None:
        Animal.identificador = 1
        self.ornitorrinco = Ornitorrinco(nombre='o', peso=10, cantidad_patas=4)

    def test_llama_init_animal(self):
        with patch('clases.Animal.__init__') as mock:
            mock.return_value = None
            Ornitorrinco(nombre='o', peso=10, cantidad_patas=4)
            mock.assert_called_once()

    def test_llama_init_terrestre(self):
        with patch('clases.Terrestre.__init__') as mock:
            mock.return_value = None
            Ornitorrinco(nombre='o', peso=10, cantidad_patas=4)
            mock.assert_called_once()

    def test_problema_diamante(self):
        with patch('clases.Animal.__init__') as mock:
            mock.return_value = None
            Ornitorrinco(nombre='o', peso=10, cantidad_patas=4)
            mock.assert_called_once()

    def test_problema_diamante_2(self):
        self.assertEqual(self.ornitorrinco.identificador, 1)
        self.assertEqual(Animal.identificador, 2)

    def test_peso(self):
        self.assertEqual(self.ornitorrinco.peso, 10)

    def test_desplazarse_cambio_energia(self):
        self.ornitorrinco.desplazarse()
        self.assertEqual(self.ornitorrinco.energia, 65)
    
    def test_desplazarse_mensaje_retorno(self):
        mensaje = self.ornitorrinco.desplazarse()
        self.assertIn(mensaje, ['caminando...nadando...', 'nadando...caminando...'])

    def test_desplazarse_mensaje_retorno_mock(self):
        with patch('clases.Terrestre.desplazarse') as mock:
            with patch('clases.Acuatico.desplazarse') as mock2:
                mock.return_value = 'a'
                mock2.return_value = 'b'
                mensaje = self.ornitorrinco.desplazarse()
                self.assertIn(mensaje, ['ab', 'ba'])

        mensaje = self.ornitorrinco.desplazarse()
        self.assertIn(mensaje, ['caminando...nadando...', 'nadando...caminando...'])

    def test_herencia_terrestre(self):
        self.assertIn(Terrestre, Ornitorrinco.__mro__)

    def test_herencia_acuatico(self):
        self.assertIn(Acuatico, Ornitorrinco.__mro__)

    def test_herencia_animal(self):
        self.assertIn(Animal, Ornitorrinco.__mro__)

    def test_herencia_pez(self):
        self.assertNotIn(Pez, Ornitorrinco.__mro__)

    def test_herencia_perro(self):
        self.assertNotIn(Perro, Ornitorrinco.__mro__)

    def test_llama_desplazarse_clase_padre_terrestre(self):
        with patch('clases.Terrestre.desplazarse') as mock:
            self.ornitorrinco.desplazarse()
            mock.assert_called_once()

    def test_llama_desplazarse_clase_padre_acuatico(self):
        with patch('clases.Acuatico.desplazarse') as mock:
            self.ornitorrinco.desplazarse()
            mock.assert_called_once()

if __name__ == '__main__':
    unittest.main(verbosity=2)
