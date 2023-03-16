import json
from collections import namedtuple
from os.path import join

Archivo = namedtuple('Archivo', ['nombre', 'peso', 'protegido'])


def transformar_key_a_nametupled(diccionario: dict | None):
    if diccionario is None:
        return

    nombre = diccionario["archivo"]["nombre"]
    protegido = diccionario["archivo"]["protegido"]
    peso = diccionario["archivo"]["peso"]
    diccionario["archivo"] = Archivo(nombre, peso, protegido)
    transformar_key_a_nametupled(diccionario["subcarpeta_1"])
    transformar_key_a_nametupled(diccionario["subcarpeta_2"])
    return diccionario


def cargar_carpeta() -> dict:
    with open(join("data", "tree.json"), "r", encoding="UTF-8") as archivo:
        carpetas = json.load(archivo)
        transformar_key_a_nametupled(carpetas)

    return carpetas


def obtener_archivos(carpeta: dict, lista_archivos: list) -> list:
    # Caso base
    if carpeta["archivo"]:
        lista_archivos.append(carpeta["archivo"])

    # Recursión
    if carpeta["subcarpeta_1"]:
        lista_archivos = obtener_archivos(
            carpeta["subcarpeta_1"], lista_archivos)

    if carpeta["subcarpeta_2"]:
        lista_archivos = obtener_archivos(
            carpeta["subcarpeta_2"], lista_archivos)

    return lista_archivos
