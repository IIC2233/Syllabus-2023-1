import unittest
from desencriptar import deserializar_diccionario, decodificar_largo, \
    separar_msg_encriptado, decodificar_secuencia, desencriptar
from encriptar import serializar_diccionario, encriptar
from errors import JsonError
from io import StringIO
from unittest.mock import patch


class TestDesencriptar(unittest.TestCase):
    def test_deserializar_diccionario(self):
        test_1 = deserializar_diccionario(bytearray(b'{"user": "name"}'))
        test_2 = deserializar_diccionario(
            bytearray(b'{"1": [1, 2], "2": "aei"}'))

        res_1 = {"user": "name"}
        res_2 = {"1": [1, 2], "2": "aei"}

        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, dict)
        # Verificar excepciones
        self.assertRaises(JsonError, deserializar_diccionario, b'{123:}')
        # Verificar resultados
        self.assertDictEqual(test_1, res_1)
        self.assertDictEqual(test_2, res_2)

    def test_decodificar_largo(self):
        test_1 = decodificar_largo(bytearray(b'\x00\x00\x00\x01'))
        test_2 = decodificar_largo(bytearray(b'\xA0\xA0\x11\xA1'))

        res_1 = 1
        res_2 = 2694844833
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, int)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_separar_msg_encriptado(self):
        test_1 = separar_msg_encriptado(
            bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03'))
        test_2 = separar_msg_encriptado(
            bytearray(b'\x00\x00\x00\x01\x03\x00\x01\x02\xAA\x00\x03'))

        res_1 = [bytearray(b'\x01\x03'), bytearray(
            b'\x00\x02\x05'), bytearray(b'\x00\x01\x00\x03')]
        res_2 = [bytearray(b'\x03'), bytearray(
            b'\x00\x01\x02\xAA'), bytearray(b'\x00\x03')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, list)
        # Verificar resultados
        self.assertListEqual(test_1, res_1)
        self.assertListEqual(test_2, res_2)

    def test_decodificar_secuencia(self):
        test_1 = decodificar_secuencia(bytearray(b'\x00\x01\x00\x02\x00\x03'))
        test_2 = decodificar_secuencia(bytearray(b'\x00\x0b\x10\x92\x00\x0c'))

        res_1 = [1, 2, 3]
        res_2 = [11, 4242, 12]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, list)
        # Verificar resultados
        self.assertListEqual(test_1, res_1)
        self.assertListEqual(test_2, res_2)

    def test_desencriptar(self):
        test_1 = desencriptar(
            bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03'))
        test_2 = desencriptar(
            bytearray(b'\x00\x00\x00\x01\x03\x00\x01\x02\xAA\x00\x03'))
        res_1 = bytearray(b'\x00\x01\x02\x03\x05')
        res_2 = bytearray(b'\x00\x01\x02\x03\xAA')

        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)

    def test_desencriptar_2(self):
        test_1 = desencriptar(
            bytearray(b'\x00\x00\x00\x02\x02\x03\x02\x01\x05\x00\x02\x00\x03'))
        test_2 = desencriptar(
            bytearray(b'\x00\x00\x00\x03\x02\x01\x10\x03\xAA\x00\x02\x00\x01\x00\x00'))
        res_1 = bytearray(b'\x02\x01\x02\x03\x05')
        res_2 = bytearray(b'\x10\x01\x02\x03\xAA')

        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
        self.assertEqual(test_2, res_2)


if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
