
def imprimir_tablero_con_utf8(tablero: list) -> None:
    n = len(tablero)

    tablero = [[str(x) if isinstance(x, int) else x for x in y] for y in tablero]

    columnas = ' ' * 5
    for indice in range(n):
        columnas += f' {indice}'

    print(columnas)
    print(' ' * 4 + '┌' + '─' * (2 * n + 1) + '┐')

    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} │'
        else:
            fila += f' {indice} │'

        fila += ' ' + ' '.join(tablero[indice]) + ' │'
        print(fila)

    print(' ' * 4 + '└' + '─' * (2 * n + 1) + '┘')

def imprimir_tablero_sin_utf8(tablero):
    n = len(tablero)

    tablero = [[str(x) if isinstance(x, int) else x for x in y] for y in tablero]

    columnas = ' ' * 4
    for indice in range(n):
        columnas += f' {indice}'

    print(columnas)
    print()

    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} '
        else:
            fila += f' {indice} '

        fila += ' ' + ' '.join(tablero[indice])
        print(fila)

'''
Por defecto imprimir_tablero tiene el parametro utf8 en True, por lo que
en caso de que no se pueda visualizar bien en consola, se debera cambiar
el valor de utf8 a False.
'''

# Cambiar utf8=False si no se puede visualizar bien en consola
def imprimir_tablero(tablero, utf8=True):
    if utf8:
        imprimir_tablero_con_utf8(tablero)
    else:
        imprimir_tablero_sin_utf8(tablero)