import socket
import os
from urllib.request import urlopen
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup

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
            print(portasAbertas)
            break
        else:
            x = x+1

def dudeVerifySite(link):
    r = ping(link)
    if r == False or r == None:
        return False
    else:
        html = urlopen("http://"+link)
        res = BeautifulSoup(html.read(),"html5lib")
        if res.title != "":
            return True
        else:
            return False