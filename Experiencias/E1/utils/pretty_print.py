def print_opciones_menu() -> None:
    opciones = '''
    Selecciona una de las siguientes opciones:
    a) Calcular el peso promedio de los archivos protegidos
    b) Obtener las extensiones de todos los archivos
    c) Mostrar top 3 archivos más pesados
    d) Obtener path absoluto del archivo d3.js
    '''
    print(opciones)


def print_peso_promedio(peso_total: float) -> None:
    print(f"> Peso promedio de los archivos protegidos: {peso_total} kb")


def print_extensiones(extensiones: set) -> None:
    if extensiones:
        print(f"> La extensiones son: {' '.join(extensiones)}")
    else:
        print("> No hay extensiones")


def print_top(top: list) -> None:
    print("> Top de archivos:")

    for i in range(len(top)):
        archivo = top[i]
        nombre, peso = archivo[0], archivo[1]
        print(f"   {i + 1}.- {nombre} [{peso} kb]")


def print_path(path: list) -> None:
    print(f"> Path del archivo: {'/'.join(path)}")


def print_opcion_invalida() -> None:
    print("> La opción ingresada es inválida")
