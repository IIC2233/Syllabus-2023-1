import socket 
import threading
import json
import time
import random

#-----------------------------------------------------------------------------------
# '''
# SLIDE 1: 
# Primero creamos el Servidor, donde definimos el host y el port
# y creamos el socket con el protocolo de transporte de datos TCT 
# (socket.SOCK_STREAM) y el tipo de dirección IP (socket.AF_INET).
# Además creamos un diccionario donde guardaremos los sockets de
# los Clientes y llamamos a las funciones necesarias para que el Servidor
# funcione.
# ''' 
#-----------------------------------------------------------------------------------

class Servidor:


    def __init__(self, port, host):
        self.max_recv = 2**16
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.bind_listen()
        self.accept_connections()
        self.online()

#-----------------------------------------------------------------------------------
# '''
# SLIDE 2:
# Con este método, asociamos el sevidor al host y puerto que le pasamos
# en el __init__(), luego decidimos la cantidad de Clientes que va a 
# permitir que se conecten.
# '''
#-----------------------------------------------------------------------------------
    
    def bind_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print(f'Servidor escuchando en {self.host} : {self.port}')

#-----------------------------------------------------------------------------------
# '''
# SLIDE 3:
# En este método creamos el Thread encargado de aceptar las nuevas
# conexiones que lleguen al Servidor y finalmente hacemos que el Thread
# corra.
# '''
#-----------------------------------------------------------------------------------

    def accept_connections(self):
        thread = threading.Thread( \
            target=self.accept_connections_thread, \
            daemon=True)
        thread.start()

#-----------------------------------------------------------------------------------
# '''
# SLIDE 4:
# Este es el metodo que ejecuta el Thread encargado de aceptar conexiones,
# el cual se encarga de guardar el socket que se esta conectando (en la 
# variable client_socket) y su respectivo address (en la variable address).
# Vale destacar que el address no es del todo útil, puede como no ser 
# guardado. Luego se crea el Thread encargado de estar escuchando a dicho
# socket y finalmente hacemos que el Thread corra.
# '''
#-----------------------------------------------------------------------------------
    
    def accept_connections_thread(self):
        while True:
            client_socket, address = self.socket_server.accept()
            self.sockets[client_socket] = address
            listening_client_thread = threading.Thread( \
                target=self.listen_client_thread, \
                args=(client_socket, ), \
                daemon=True)
            listening_client_thread.start()

#-----------------------------------------------------------------------------------
# '''
# SLIDE 6:
# Este es el método que ejecuta el Thread encargado de escuchar a un
# Cliente. En éste, se genera un loop que recive el mensaje que manda el
# Cliente y luego prosigue a decodificarlo y a entregarselo a método 
# encargado de qué hacer con dicha información.
# '''
#-----------------------------------------------------------------------------------

    def listen_client_thread(self, client_socket):
        while True:
            largo_archivo = int.from_bytes(client_socket.recv(4), byteorder='big')
            if largo_archivo > self.max_recv:
                largo_archivo = self.max_recv
            bytes_leidos = bytearray()
            while len(bytes_leidos) < largo_archivo:
                # El último recv será probablemente más chico que 4096
                bytes_leer = min(4096, largo_archivo - len(bytes_leidos))
                respuesta = client_socket.recv(bytes_leer)
                bytes_leidos += respuesta
            mensaje_entero = bytes_leidos.decode()
            mensaje_entero = json.loads(mensaje_entero)
            self.chat_management(mensaje_entero)
#-----------------------------------------------------------------------------------
# '''
# SLIDE 7:
# Este método solo se encarga de mantener el Servidor abierto (que no se
# cierre el programa)
# '''
#-----------------------------------------------------------------------------------

    def online(self):
        while True:
            pass

#-----------------------------------------------------------------------------------
# '''
# SLIDE 8:
# Este método es el encargado de leer el mensaje que llego del Cliente
# y luego enviar la información (manejada por el Servidor) a cada Cliente
# que esta conectado al Servidor 
# '''
#-----------------------------------------------------------------------------------

    def chat_management(self, msg):
        msg_to_send = { "type" : msg["type"], \
                        "username" : msg["username"], \
                        "data" : msg["data"]}
        for skt in self.sockets.keys():
            self.send(msg_to_send, skt)

#-----------------------------------------------------------------------------------
# '''
# SLIDE 9:
# Este es el método encargado de enviar la información de manera
# encriptada (bytes) y es donde se llama a sock.send (el método que
# envia la información al socket (Cliente))
# '''
#-----------------------------------------------------------------------------------
    
    def send(self, value, sock):
        str_value = str(value)
        msg_bytes = str_value.encode()
        sock.send(msg_bytes)

#-----------------------------------------------------------------------------------

if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    server = Servidor(port, host)
