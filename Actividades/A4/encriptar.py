from typing import List
import json
from errors import JsonError, SequenceError


def serializar_diccionario(dictionary: dict) -> bytearray:
    # Completar
    pass


def verificar_secuencia(mensaje: bytearray, secuencia: List[int]) -> None:
    # Completar
    pass


def codificar_secuencia(secuencia: List[int]) -> bytearray:
    # Completar
    pass


def codificar_largo(largo: int) -> bytearray:
    # Completar
    pass


def separar_msg(mensaje: bytearray, secuencia: List[int]) -> List[bytearray]:
    m_bytes_secuencia = bytearray()
    m_reducido = bytearray()
    # Completar

    return [m_bytes_secuencia, m_reducido]


def encriptar(mensaje: dict, secuencia: List[int]) -> bytearray:
    verificar_secuencia(mensaje, secuencia)

    m_bytes_secuencia, m_reducido = separar_msg(mensaje, secuencia)
    secuencia_codificada = codificar_secuencia(secuencia)

    return (
        codificar_largo(len(secuencia))
        + m_bytes_secuencia
        + m_reducido
        + secuencia_codificada
    )


if __name__ == "__main__":
    original = serializar_diccionario({"tama": 1})
    encriptado = encriptar(original, [1, 5, 10, 3])
    print(original)
    print(encriptado)
