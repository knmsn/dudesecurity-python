import socket
import os

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