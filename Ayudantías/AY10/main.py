from  PyQt5.QtWidgets import QApplication
import sys
from client import Cliente
from lobby import MainWindow

app = QApplication([])

PORT = 3245
HOST = 'localhost'


cliente = Cliente(PORT, HOST)
window = MainWindow()


cliente.send_username.connect(window.get_username)
cliente.update_lobby_chat.connect(window.update_chat)
cliente.send_init_info_to_chat()

window.send_msg_signal.connect(cliente.recive_msg_from_lobby)


window.show()
sys.exit(app.exec_())