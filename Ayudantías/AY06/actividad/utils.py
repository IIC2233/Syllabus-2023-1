# NO MODIFICAR


def coordenadas_figuras():
    diccionario_figuras = {}

    diccionario_figuras["recta"] = []
    for i in range(4):
        diccionario_figuras["recta"].append((i, 0))

    diccionario_figuras["horizontal"] = []
    for i in range(4):
        diccionario_figuras["horizontal"].append((0, i))

    diccionario_figuras["l"] = []
    for i in range(3):
        diccionario_figuras["l"].append((i, 1))
    diccionario_figuras["l"].append((0, 0))

    diccionario_figuras["t"] = []
    for i in range(3):
        diccionario_figuras["t"].append((i, 1))
    diccionario_figuras["t"].append((1, 0))

    diccionario_figuras["s"] = []
    diccionario_figuras["s"].append((0, 0))
    diccionario_figuras["s"].append((0, 1))
    diccionario_figuras["s"].append((1, 1))
    diccionario_figuras["s"].append((1, 2))

    diccionario_figuras["c"] = []
    diccionario_figuras["c"].append((0, 0))
    diccionario_figuras["c"].append((0, 1))
    diccionario_figuras["c"].append((1, 1))
    diccionario_figuras["c"].append((1, 0))

    return diccionario_figuras
