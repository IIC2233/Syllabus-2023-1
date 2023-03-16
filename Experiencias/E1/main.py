from functions import (
    peso_promedio_archivos_protegidos,
    buscar_extensiones_unicas, cargar_top_archivos,
    buscar_archivo
)

from utils.loader import cargar_carpeta, obtener_archivos
from utils.pretty_print import (
    print_opciones_menu, print_peso_promedio, print_extensiones,
    print_top, print_path, print_opcion_invalida
)


def menu():
    # Cargamos los datos
    carpeta = cargar_carpeta()
    archivos = obtener_archivos(carpeta, [])

    # Poner el print bonito de las opciones del menu
    print_opciones_menu()
    opcion = int(input())

    if opcion == "a": 
        peso_promedio = peso_promedio_archivos_protegidos(archivos)
        print_peso_promedio(peso_promedio)

    elif opcion == "b":
        extensiones = buscar_extensiones_unicas(archivos)
        print_extensiones(extensiones)

    elif opcion == "c":
        top = cargar_top_archivos()
        print_top(top)

    elif opcion == "d":
        path = buscar_archivo(carpeta, "d3.js")
        print_path(path)

    else:
        print_opcion_invalida()


if __name__ == "__main__":
    menu()
