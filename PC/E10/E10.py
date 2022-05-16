import subprocess

user = input('Ingrese un nombre de usuario: ')
try:
    list_files = subprocess.run(['/root/buscaUsuario.sh', user])
    print(list_files.returncode)
except FileNotFoundError as e:
    print('Error:',e)
    print('Es muy probable que "buscaUsuario.sh" no se encuentre en root')
