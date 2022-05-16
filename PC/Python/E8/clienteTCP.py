import argparse
import socket
from cryptography.fernet import Fernet

# Uso:
# En una terminal ejecutar:
# py .\servidorTCP.py
# En otra terminal ejecutar:
# py .\clienteTCP.py -msj [Mensaje a enviar entre comillas]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-msj', type=str, help='Mensaje a enviar', required=True)
    args = parser.parse_args()

    key = Fernet.generate_key()
    fk = Fernet(key)
    with open('clave.key','wb') as f:
        f.write(key)

    mensaje = args.msj
    mensaje = mensaje.encode(encoding='utf-8')
    token = fk.encrypt(mensaje)
    print(token)

    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 2048

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(token)
    recieve = s.recv(BUFFER_SIZE).decode()
    s.close()
    print(recieve)