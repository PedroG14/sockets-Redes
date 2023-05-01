#!/usr/bin/python3

import socket, time
from random import randrange

HOST = 'localhost'
PORT = 5000

def main():
    exceptHappened = False

    print("--CLIENTE--\n")
    
    while True:
        #Criando objeto Socket s de endereço IPv4 e tipo TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Except para caso o programa servidor ainda não tenha sido aberto
        try:
            #Conectando-se ao servidor
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            if not exceptHappened:
                print("Esperando servidor... \n")
                exceptHappened = True
            continue
        exceptHappened = False

        #Número aleatório gerado para ser enviado ao servidor
        randomInt = randrange(1000000000000000000000000000000)

        #Enviando dado ao servidor (no caso o número gerado)
        s.sendall(str.encode(str(randomInt)))

        #Esperando resposta do servidor e imprimindo ao recebê-lo
        data = s.recv(1024)
        print(data.decode(), "FIM\n")

        #Fechando conexão ao servidor e esperando 10 segundos para reenviar outro valor
        s.close()
        time.sleep(10)

if __name__ == "__main__":
    main()
