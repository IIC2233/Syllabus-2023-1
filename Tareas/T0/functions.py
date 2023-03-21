# Agregar los imports que estimen necesarios


def cargar_tablero(nombre_archivo: str) -> list:
    pass


def guardar_tablero(nombre_archivo: str, tablero: list) -> None:
    pass


def verificar_valor_bombas(tablero: list) -> int:
    pass


def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    pass


def verificar_tortugas(tablero: list) -> int:
    pass


def solucionar_tablero(tablero: list) -> list:
    pass


if __name__ == "__main__":
    tablero_2x2 = [
        ['-', 2],
        ['-', '-']
    ]
    resultado = verificar_valor_bombas(tablero_2x2)
    print(resultado)  # Debería ser 0

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 3

    tablero_resuelto = solucionar_tablero(tablero_2x2)
    print(tablero_resuelto)

    tablero_2x2_sol = [
        ['T', 2],
        ['-', '-']
    ]

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 2

    resultado = verificar_tortugas(tablero_2x2_sol)
    print(resultado)  # Debería ser 0
