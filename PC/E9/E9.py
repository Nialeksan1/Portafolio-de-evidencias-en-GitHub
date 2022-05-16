import urllib3
import Metadata
import re
import os
import argparse
from bs4 import BeautifulSoup
from time import sleep


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', type=str, help='Escribe una url con el formato http[s]://[LaUrl].[terminacion]/')
    args = parser.parse_args()
    if args.url:
        x = ''
        comp1 = re.compile('(http:\/\/|https:\/\/)?(www\.)?')
        comp2 = re.compile('((\.(com))?\.(\w+))\/')
        comp3 = re.compile('.+\....')
        comp4 = re.compile('.+="(http:\/|https:\/)?\/.+"')
        comp5 = re.compile('"(http:\/|https:\/)?\/.+"')

        input_url = args.url
        if input_url[-1] != '/':
            input_url = input_url + '/'
        folder_name = re.sub(comp1, '', input_url)
        folder_name = re.sub(comp2, '', folder_name)
        if not os.path.isdir(f'./img/'):
                os.mkdir(f'./img/')
        if not os.path.isdir(f'./img/{folder_name}') and not os.path.isdir(f'./img/{folder_name}_Metadata'):
            os.mkdir(f'./img/{folder_name}')
            os.mkdir(f'./img/{folder_name}_Metadata')
        else:
            x = input('Ya existe una carpeta con información de esta página, desea continuar de todos modos:\n[0] No\tENTER Sí\n')
        http = urllib3.PoolManager()
        try:
            resp = http.request('GET', input_url).data.decode()
            soup = BeautifulSoup(resp, 'html.parser')
            lstsoup = soup.find_all('img')

            if x == '':
                print('\nEl proceso puede tardar un tiempo. . .\n')
                lstURLs = []
                for tag in lstsoup:
                    tag = str(tag).split()
                    lstATT = [att for att in tag if re.match(comp4, att)]
                    lstURL = [re.search(comp5, url).group().strip('"') for url in lstATT if re.search(comp5, url)]
                    lstURLs += lstURL
                for link in lstURLs:
                    name = re.match(comp3, link.split("/")[-1]).group()
                    try:
                        print(f'[+] Extrayendo url = {link}')
                        req = http.request('GET', link)
                        print(f'[+] Extraído {link} exitosamente')
                        print(f'[+] Escribiendo bytes en ./img/{folder_name}/')
                        try:
                            with open(f'./img/{folder_name}/{name}', 'wb') as f:
                                f.write(bytes(req.data))
                                print(f'[+] Imagen guardada como /{name} exitosamente')
                            with open(f'./img/{folder_name}_Metadata/{name[0:-4:]}.txt', 'w') as txt:
                                txt.write(Metadata.Metadata(f'./img/{folder_name}/{name}'))
                        except:
                            print(f'[-] No se ha podido guardar la imágen')
                    except:
                        try:
                            print(f'[+] Extrayendo url = {input_url}{link[1::]}')
                            req = http.request('GET', f'{input_url}{link[1::]}')
                            print(f'[+] Extraído {input_url}{link[1::]} exitosamente')
                            print(f'[+] Escribiendo bytes en ./img/{folder_name}/')
                            try:
                                with open(f'./img/{folder_name}/{name}', 'wb') as f:
                                    f.write(bytes(req.data))
                                    print(f'[+] Imagen guardada como /{name} exitosamente')
                                with open(f'./img/{folder_name}_Metadata/{name[0:-4:]}.txt', 'w') as txt:
                                    txt.write(Metadata.Metadata(f'./img/{folder_name}/{name}'))
                            except:
                                print(f'[-] No se ha podido guardar la imágen')
                        except:
                            print('[-] No se ha podido extraer el link')
                            pass
                print('\nHecho!')
                sleep(1)
            else:
                print('\nSaliendo del programa. . .\n')
                sleep(1)
                quit()
        except Exception as e:
            print('Error:', e)
            # print('\nIngrese una url válida.\n')
