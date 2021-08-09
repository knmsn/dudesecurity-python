## Importando librarys

import socket
import os
import random
from urllib.request import urlopen
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup
from itertools import permutations
import requests 
import base64
from random import choice
import string

def functionPS(x,y,debug):
    portasAbertas = []
    x = int(x)
    y = int(y)
    while True:
        socket_verification = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        alvo = ('localhost', x)
        resultado = socket_verification.connect_ex(alvo)
        socket_verification.close()
        if debug == True:
            print(x)
        if resultado == 0:
            portasAbertas.append(int(x))
        if x == y:
            return portasAbertas
            break
        else:
            x = x+1