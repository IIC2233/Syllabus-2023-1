import socket
import threading
import json
import random
import string
from PyQt5.QtCore import pyqtSignal, QObject

#-----------------------------------------------------------------------------------
# '''
# SLIDE 1:
# Primero creamos el Cliente, el cual es más complejo que el Servidor, 
# ya que posee caracteristicas de Networking (sockets) y de Interfaz de
# Usuario (QThread). Ésto se hace debido a que el Cliente es el encargado
# del Backend del DCChat (donde el archivo lobby.py es su Frontend).
# Networking: 
# Definimos el host y el port y creamos el socket con el 
# protocolo de transporte de datos TCT (socket.SOCK_STREAM) y el tipo 
# de dirección IP (socket.AF_INET). Luego debemos tratar de conectarnos
# al servidor (tratamos porque no siempre se garantiza una conección
# éxitosa), por lo que aplicamos un try/except en donde en el try se
# llaman a los métodos encargados de conectarse y en el except se cierra
# el socket y se detiene el programa.
# Backend:
# Definimos las señales necesarias para que exista comunicación con el 
# Frontend y las distintas variables y métodos que implementarían la
# lógica.
# '''
#-----------------------------------------------------------------------------------




class Cliente(QObject):


    update_lobby_chat = pyqtSignal(str)
    send_username = pyqtSignal(str)


    def __init__(self, port, host):
        super().__init__()
        print('Creando cliente')
        self.port = port
        self.host = host
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = 'User' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        try:
            self.connect_to_server()
            self.initBackend()
            self.listen()
        except ConnectionError:
            print('Conexion terminada')
            self.socket_cliente.close()
            self.isConnected = False

#-----------------------------------------------------------------------------------
# '''
# SLIDE 2:
# En este método se realiza la conección cone el Servidor
# '''
#-----------------------------------------------------------------------------------

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        print('Cliente conectado a servidor')

#-----------------------------------------------------------------------------------
# '''
# SLIDE 3:
# En este método se crea el Thread encargado de escuchar al Servidor y 
# luego hacemos que corra.
# '''
#-----------------------------------------------------------------------------------

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

#-----------------------------------------------------------------------------------
# '''
# SLIDE 4:
# En es el método que ejecuta el Thread encargado de escuchar al Servidor.
# En éste, se genera un loop que recive el mensaje que manda el
# Servidor y luego prosigue a decodificarlo y a entregarselo a método 
# encargado de qué hacer con dicha información.
# '''
#-----------------------------------------------------------------------------------

    def listen_thread(self):
        while self.isConnected:
            data = self.socket_cliente.recv(2**16)
            decoded_data = data.decode()
            decoded_data = decoded_data.replace('\'', '\"') #Esto lo hacemos porque json solo hacepta el "", no el ''
            data = json.loads(decoded_data)
            self.decode_msg_from_server(data)
            pass
#-----------------------------------------------------------------------------------
# '''
# SLIDE 5:
# En este método, encriptamos la información a enviar y procedemos 
# a enviarla al Servidor.
# '''
#-----------------------------------------------------------------------------------

    def send(self, msg):
        json_msg = json.dumps(msg)
        msg_to_send = json_msg.encode()
        largo = len(msg_to_send)
        self.socket_cliente.send(largo.to_bytes(4, byteorder='big') + msg_to_send)



#-----------------------------------------------------------------------------------
# '''
# SLIDE 7:
# Aquí están los métodos encargados del Backend de DCChat.
# run(self): sobrescribimos el run para así definir que se ejecuta 
# cuando se llama el start() del QThread.
# initBackend(self): creamos las variables self.isConnected, la cual es
# la condicion del while en el método online(self) y la variable 
# self.chat, donde guardaremos el chat del DCChat (todos los mensajes 
# que han sido enviados) para luego poder mostrarlos en el Frontend.
# send_init_info_to_chat(self): este método se encarga de enviar el nombre
# de usuario al frontend del DCChat
# recive_msg_from_lobby(self, event): este método se encarga de recivir 
# la información del Frontend del DCChat (el mensaje que quiere enviar
# el usuario) y, como no hay que "manejarlo" lo enviamos al Servidor
# decode_msg_from_server(self, msg): este método es el encargado de 
# decodificar la información recivida por el Servidor, agregarlo a 
# self.chat y finalmente mandar la información al Backend.
# '''
#-----------------------------------------------------------------------------------


    def initBackend(self):
        self.isConnected = True
        self.chat = ''


    def send_init_info_to_chat(self):
        self.send_username.emit(self.username)


    def recive_msg_from_lobby(self, event):
        self.send(event)


    def decode_msg_from_server(self, msg):
        string_to_add = f'{msg["username"]}: {msg["data"]}\n'
        self.chat += string_to_add
        self.update_lobby_chat.emit(self.chat)
        


# if __name__ == '__main__':
#     port = 3245
#     host = 'localhost'
#     client = Cliente(port, host)

