import threading
from time import sleep


def comenzar_correr(nombre):
    print(f"{nombre} comenzó a correr!")


def contar():
    contador = 0
    while True:
        print(f"han pasado {contador} segs")
        sleep(1)
        contador += 1


tortuga = threading.Timer(0.5, comenzar_correr, args={"Tortuga"})
conejo = threading.Timer(5, comenzar_correr, args={"Conejo"})
reloj = threading.Thread(target=contar, daemon=True)

tortuga.start()
conejo.start()
reloj.start()
