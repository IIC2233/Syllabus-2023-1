import sys
import random
import PyQt5.QtWidgets as widgets
import PyQt5.QtCore as core
from PyQt5 import uic


#Usamos la función loadUiType para generar una tupla del nombre de la ventana y su clase base
window_name, base_class = uic.loadUiType("DCChat.ui")


class MainWindow(window_name, base_class):

    send_msg_signal = core.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self) #Construimos la ventana creada en QtDesigner
        self.sendButton.clicked.connect(self.send_msg_to_client)
        self.displayWidget.setReadOnly(True)
        self.show()

    def salir(self, event):
        sys.exit()
 
    def send_msg_to_client(self):
        print(self.userInputWidget.toPlainText())
        data = {    
            "type"  :   "chat", \
            "username"  :   self.username, \
            "data"  :   self.userInputWidget.toPlainText() \
                }
        self.send_msg_signal.emit(data)
        self.userInputWidget.setPlainText('')

    def get_username(self, event):
        self.username = event
        print('Username seted')

    def update_chat(self, event):
        self.displayWidget.setPlainText(event)

if __name__ == '__main__':
    app = widgets.QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
