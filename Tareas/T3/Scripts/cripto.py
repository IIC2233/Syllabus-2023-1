import random
def encriptar(msg: bytearray, ID) -> bytearray:
    pass


def desencriptar(msg: bytearray, ID):
    pass
    


if __name__ == "__main__":
    # Testear encriptar
    ID = 1001
    random.seed(ID)
    msg_original = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05')
    msg_esperado = bytearray(b'\x01\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05\x03\x02')

    msg_encriptado = encriptar(msg_original, ID)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado, ID)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")