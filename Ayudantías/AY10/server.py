import socket
import threading
import json
import time
import random


class Servidor:

    def __init__(self, port, host):
        self.max_recv = 2**16
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.bind_listen()
        self.accept_connections()

    def bind_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print(f'Servidor escuchando en {self.host} : {self.port}')

    def accept_connections(self):
        thread = threading.Thread(
            target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        while True:
            client_socket, address = self.socket_server.accept()
            self.sockets[client_socket] = address
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ),
                daemon=True)
            listening_client_thread.start()

    def listen_client_thread(self, client_socket):
        while True:
            largo_archivo = int.from_bytes(
                client_socket.recv(4), byteorder='big')
            if largo_archivo > self.max_recv:
                largo_archivo = self.max_recv
            bytes_leidos = bytearray()
            while len(bytes_leidos) < largo_archivo:
                # El último recv será probablemente más chico que 4096
                bytes_leer = min(4096, largo_archivo - len(bytes_leidos))
                respuesta = client_socket.recv(bytes_leer)
                bytes_leidos += respuesta
            try:
            # Si se elimina el usuario, el servidor recibe un mensaje vacío y no logra
            # deserializarlo.
                mensaje_entero = json.loads(bytes_leidos)
                self.chat_management(mensaje_entero)
            except json.decoder.JSONDecodeError as e:
                print('Usuario eliminado')
            # Eliminamos al cliente del diccionario de sockets
                del self.sockets[client_socket]
                break

    def chat_management(self, msg):
        msg_to_send = {"type": msg["type"],
                       "username": msg["username"],
                       "data": msg["data"]}
        for skt in self.sockets.keys():
            self.send(msg_to_send, skt)

    def send(self, value, sock):
        str_value = str(value)
        msg_bytes = str_value.encode()
        sock.send(msg_bytes)


if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    server = Servidor(port, host)
