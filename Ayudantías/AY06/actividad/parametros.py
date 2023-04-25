import os


# Rutas a archivos *.ui
PATH_VENTANA_JUEGO = os.path.join("frontend", "assets", "templates", "ventana_de_juego.ui")
PATH_VENTANA_FIN = os.path.join("frontend", "assets", "templates", "ventana_game_over.ui")
VENTANA_ERROR = os.path.join("frontend", "assets", "templates", "Mensaje_error.ui")
VENTANA_INICIO = os.path.join("frontend", "assets", "templates", "Tetris_inicio.ui")

# Assets ventana de juego
BORDE_HORIZONTAL = os.path.join("frontend", "assets", "sprites", "bordes", "borde_horizontal.png")
BORDE_VERTICAL = os.path.join("frontend", "assets", "sprites", "bordes", "borde_vertical.png")
IMAGEN_FIN = os.path.join("frontend", "assets", "sprites", "game_over", "fin_juego.jpeg")
IMAGEN_ERROR = os.path.join("frontend", "assets", "sprites", "Ventana_inicio_y_error", "Logo_Error")
LOGO_INICIO = os.path.join("frontend", "assets", "sprites", "Ventana_inicio_y_error", "Logo")
FONDO = os.path.join("frontend", "assets", "sprites", "Ventana_inicio_y_error", "Fondo")
RUTA_CANCION = os.path.join("frontend", "assets", "Cancion", "Tetris.wav")

# Parámetros Backend
ALTO_GRILLA = 20
ANCHO_GRILLA = 10
TIEMPO_AVANCE = 0.1
PUNTAJE_LINEA = 10
