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

def dudePortScanner(ip,x,y):
    portasAbertas = []
    x = int(x)
    y = int(y)

    while True:

        socket_verification = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        alvo = (ip, x)
        resultado = socket_verification.connect_ex(alvo)

        socket_verification.close()
        

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

def dudeWordList(word_size, profile, path):

    if isinstance(profile, dict):
        birthdate_yy = profile["birthdate"][-2:]
        birthdate_yyy = profile["birthdate"][-3:]
        birthdate_yyyy = profile["birthdate"][-4:]
        birthdate_xd = profile["birthdate"][1:2]
        birthdate_xm = profile["birthdate"][3:4]
        birthdate_dd = profile["birthdate"][:2]
        birthdate_mm = profile["birthdate"][2:4]

        bd_list = [
            birthdate_yy,
            birthdate_yyy,
            birthdate_yyyy,
            birthdate_xd,
            birthdate_xm,
            birthdate_dd,
            birthdate_mm,
        ]

        name_lastname_list = [profile["name"], profile["lastname"], profile["nickname"]]

        for name  in name_lastname_list:
            if name.capitalize() not in name_lastname_list: name_lastname_list.append(name.capitalize())
            if name.upper() not in name_lastname_list: name_lastname_list.append(name.upper())
            if name.lower() not in name_lastname_list: name_lastname_list.append(name.lower())

        output_list = bd_list + name_lastname_list
        combination_list = []

        for i in range(word_size):
            combination_list += permutations(output_list, i+1)

        if not os.path.exists(path):
            output_file = open(path, 'w')
            for word in combination_list:
                output_file.write('{}\n'.format(''.join(word)))

def generateCpf():
    

    list_cpf = [random.randint(0,9) for i in range(9)]
    sum_digit_one = 0
    sum_digit_two = 0
    count_one = len(list_cpf) + 1
    count_two = len(list_cpf) + 2
    
    for i in range(count_two):
        if count_one >= 2:
            sum_digit_one += list_cpf[i] * count_one
        if count_one == 2:
            if sum_digit_one % 11 > 2:
                list_cpf.append(abs((sum_digit_one * 10) % 11))
            else:
                list_cpf.append(0)

        if count_two >= 2:
            sum_digit_two += list_cpf[i] * count_two
        if count_two == 2:
            if sum_digit_two % 11 > 2:
                list_cpf.append(abs((sum_digit_two * 10) % 11))
            else:
                list_cpf.append(0)

        count_one -= 1
        count_two -= 1
    
    string_cpf = ''.join(str(elem) for elem in list_cpf)
    
    return f"{string_cpf[:3]}.{string_cpf[3:6]}.{string_cpf[6:9]}-{string_cpf[9:]}"


def generator_password(size):
    password = ""

    values = string.ascii_letters + string.digits + '@#&$'

    for i in range(size):
        password += choice(values)

    print(password)
    return password
