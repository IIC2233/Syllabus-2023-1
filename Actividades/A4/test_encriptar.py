import unittest
from encriptar import serializar_diccionario, verificar_secuencia, \
    codificar_secuencia, codificar_largo, separar_msg, encriptar
from errors import JsonError, SequenceError
from io import StringIO
from unittest.mock import patch


class TestEncriptar(unittest.TestCase):

    def test_serializar_diccionario_result(self):
        test_1 = serializar_diccionario({"user": "name"})
        test_2 = serializar_diccionario({"1": [1, 2], "2": "aei"})
        res_1 = bytearray(b'{"user": "name"}')
        res_2 = bytearray(b'{"1": [1, 2], "2": "aei"}')

        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, bytearray)
        # Verificar excepciones
        self.assertRaises(JsonError, serializar_diccionario, {"anya": set()})
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_verificar_secuencia(self):
        mensaje = bytearray(b'\x00\x01\x02\x03')
        # Verificar excepciones
        self.assertRaises(SequenceError, verificar_secuencia, mensaje, [100])
        self.assertRaises(SequenceError, verificar_secuencia, mensaje, [2, 2])
        # Verificar que retorne None cuando todo es válido
        self.assertIsNone(verificar_secuencia(mensaje, [1, 2]))

    def test_codificar_secuencia(self):
        test_1 = codificar_secuencia([1, 2, 3])
        test_2 = codificar_secuencia([11, 4242, 12])

        res_1 = bytearray(b'\x00\x01\x00\x02\x00\x03')
        res_2 = bytearray(b'\x00\x0b\x10\x92\x00\x0c')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_codificar_largo(self):
        test_1 = codificar_largo(8)
        test_2 = codificar_largo(4242)

        res_1 = bytearray(b'\x00\x00\x00\x08')
        res_2 = bytearray(b'\x00\x00\x10\x92')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_separar_msg(self):
        test_1 = separar_msg(bytearray(b'\x00\x01\x02\x03'), [1, 3])
        test_2 = separar_msg(bytearray(b'\x00\x01\x02\x03'), [3])

        res_1 = [bytearray(b'\x01\x03'), bytearray(b'\x00\x02')]
        res_2 = [bytearray(b'\x03'), bytearray(b'\x00\x01\x02')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, list)
        # Verificar resultados
        self.assertListEqual(test_1, res_1)
        self.assertListEqual(test_2, res_2)

    def test_encriptar(self):
        test_1 = encriptar(bytearray(b'\x00\x01\x02\x03\x05'), [1, 3])
        test_2 = encriptar(bytearray(b'\x00\x01\x02\x03\xAA'), [3])

        res_1 = bytearray(
            b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03')
        res_2 = bytearray(b'\x00\x00\x00\x01\x03\x00\x01\x02\xaa\x00\x03')
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_encriptar_2(self):
        test_1 = encriptar(bytearray(b'\x02\x01\x02\x03\x05'), [2, 3])
        test_2 = encriptar(bytearray(b'\x10\x01\x02\x03\xAA'), [2, 1, 0])

        res_1 = bytearray(
            b'\x00\x00\x00\x02\x02\x03\x02\x01\x05\x00\x02\x00\x03')
        res_2 = bytearray(
            b'\x00\x00\x00\x03\x02\x01\x10\x03\xaa\x00\x02\x00\x01\x00\x00')
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
