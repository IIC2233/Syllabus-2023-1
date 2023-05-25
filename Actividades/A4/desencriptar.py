from typing import List
import json
from errors import JsonError, SequenceError


def deserializar_diccionario(mensaje_codificado: bytearray) -> dict:
    # Completar
    pass


def decodificar_largo(mensaje: bytearray) -> int:
    # Completar
    pass


def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    secuencia_codificada = bytearray()
    # Completar

    return [m_bytes_secuencia, m_reducido, secuencia_codificada]


def decodificar_secuencia(secuencia_codificada: bytearray) -> List[int]:
    # Completar
    pass


def desencriptar(mensaje: bytearray) -> bytearray:
    # Completar
    pass


if __name__ == "__main__":
    mensaje = bytearray(b'\x00\x00\x00\x04"a}a{tm": 1\x00\x01\x00\x05\x00\n\x00\x03')
    desencriptado = desencriptar(mensaje)
    diccionario = deserializar_diccionario(desencriptado)
    print(diccionario)
