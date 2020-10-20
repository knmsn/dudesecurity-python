import socket
import os
from urllib.request import urlopen
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup
import requests 
import base64

import string
from random import random, choice


def dudePortScanner(ip,x,y):
    portasAbertas = []
    x = int(x)
    y = int(y)

    
    while True:

        ## Definindo o alvo e enviando a verificacao

        socket_verification = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        alvo = (ip, x)
        resultado = socket_verification.connect_ex(alvo)

        socket_verification.close()

        ## Verificando o resultado

        

        if resultado == 0:
            portasAbertas.append(int(x))

        
        if x == y:
            return portasAbertas
            break
        else:
            x = x+1



def dudeVerifySite(link):
    # Pingando o endereço para validar o dominio
    r = ping(link)
    if r == False or r == None:
        return False
    else:
        # Fazendo webscrapping para validar a estrutura da página e verificar erros: 404,504,etc.
        html = urlopen("http://"+link)
        res = BeautifulSoup(html.read(),"html5lib")
        if res.title != "":
            return True
        else:
            return False



def dudeVerifyAPI(link):
# Pingando o endereço para validar o dominio
    r = ping(link)
    if r == False or r == None:
        return False

    else:
        resp = requests.get("http://"+link)
        if resp.status_code == 200:
            return True
        else:
            return False

def dudeEncodeb64(texto):
    textEncoded = base64.b64encode(texto.encode())
    return textEncoded

def dudeDecodeb64(texto):
    textDecoded = base64.b64decode(texto.encode())
    return textDecoded


#Gerador de senha aleatoria --------------

values = string.ascii_letters + string.digits + '@#&$'

password = ""

def generator_password(password, size =10):

    for i in range(size):
        password += choice(values)

    print(f'Senha gerada: \033[31m{password}')



generator_password(password)