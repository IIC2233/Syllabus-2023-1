import socket
import sys
import os
import string
import pickle


class Mensaje:
    
    def __init__(self, operacion = None, data = None, estado = None):
        self.operacion = operacion
        self.data = data
        self.estado = estado


class Cliente:

    def __init__(self, port: int, host: str):
        super().__init__()
        self.conectado = False
        self.port = port
        self.host = host
        self.chunk_size = 2**16
        # TODO: Completar
            
    def menu(self):
        opciones = {
            '1': self.pedir_lista_archivos,
            '2': self.descargar_archivo,
            '3': self.salir
        }
        while self.conectado:
            opcion = input('''
¿Qué deseas hacer?
[1]Pedir lista de archivos
[2]Descargar Archivo
[3]Salir
''')
            if opcion in opciones:
                opciones[opcion]()
            else:
                print(f"{opcion} no es una opcion válida")

    def recibir_bytes(self, cantidad: int):
        # TODO: Recibir <cantidad> bytes desde el socket
        pass

    def recibir_mensaje(self):
        # TODO: Se encarga de recibir los bytes necesarios y retorna el mensaje
        pass

    def pedir_lista_archivos(self):
        # TODO: Debe enviar un mensaje con la operacion "listar", e imprimir en consola
        # los archivos que llegan dentro de la respuesta del servidor
        pass

    def descargar_archivo(self):
        # TODO: Pide el nombre del archivo que quiere descargar, le pide al servidor que le envíe
        # el archivo y luego llama al método self.guardar_archivo con lo que recibió del servidor
        pass
    
    def guardar_archivo(self, nombre_archivo: string, archivo: bytearray):
        # Crear carpeta si es que no existe
        os.makedirs("descargas", exist_ok=True)
        
        # Guardar archivo 
        with open(os.path.join('descargas', nombre_archivo), 'wb') as file:
            file.write(archivo)

    def salir(self):
        self.socket_cliente.close()
        self.conectado = False

    def enviar_mensaje(self, mensaje: Mensaje):
        # TODO: Debe enviar el mensaje cumpliendo con las reglas antes mencionadas:
        # Primero enviar 4 bytes con el largo del mensaje, y luego el mensaje
        pass


if __name__ == '__main__':
    # TODO: El puerto y el host deben poder pasarse por consola,
    # y en caso de que no se reciban, tener por defecto un valor.
    PORT = None
    HOST = None
    client = Cliente(PORT, HOST)

