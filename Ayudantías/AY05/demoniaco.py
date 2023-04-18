import threading
import time


def contador(clave, maximo):
    for j in range(1, maximo):
        print(f"{clave}: {int(j)}")
        time.sleep(1)


conteo_100 = threading.Thread(target=contador, args=("uno", 100,), daemon=True)
conteo_5 = threading.Thread(target=contador, args=("dos", 5,), daemon=True)

conteo_100.start()
conteo_5.start()
conteo_5.join()
