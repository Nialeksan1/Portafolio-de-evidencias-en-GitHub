import socket
from cryptography import fernet


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen()
while(True):
    client, address = s.accept()
    print('Se estableció la conexión')
    recive = client.recv(BUFFER_SIZE)
    client.send('Enterado. Bye!'.encode())
    client.close()
    break

file = open('clave.key','rb')
key = file.read()
file.close()

f = fernet.Fernet(key)
mensaje = f.decrypt(recive).decode()
print(mensaje)
