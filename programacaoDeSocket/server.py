#!/usr/bin/python3

import socket, random, string

HOST = 'localhost'
PORT = 5000

def main():
    print("--SERVIDOR--\n")

    #Criando objeto Socket s de endereço IPv4 e tipo TCP e vinculando ao endereço "localhost" (127.0.0.1) e a porta 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    while True:
        #Habilitando servidor
        s.listen()

        #Esperando conexão para então retornar um socket (conn) e o endereço vinculado ao socket (cliente, no nosso caso o endereço "localhost") (ender)
        conn, ender = s.accept()

        #Recebendo dados enviados pelo cliente
        data = conn.recv(1024)

        #Imprimindo dado recebido do cliente
        print("Valor recebido:", data.decode(), "\n")

        #Caso o tamanho da string de dados seja maior que 10, é criada uma palavra aleatória do mesmo tamanho do dado enviado
        if len(data.decode()) > 10:
            conn.sendall(str.encode(randomWord(len(data.decode()))))
        #Caso não, é checado se o valor recebido é par ou ímpar
        else:
            if int(data.decode())%2 == 0:
                conn.sendall(str.encode('Par'))
            else:
                conn.sendall(str.encode('Ímpar'))

#Função para gerar uma palavra aleatória de tamanho "length"
def randomWord(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    main()
