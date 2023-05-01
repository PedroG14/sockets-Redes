# Sockets Cliente-Servidor
Trabalho Prático - Programação de Sockets (Redes de Computadores - Universidade Federal do Ceará (Campus Russas))

O trabalho consiste em duas aplicações, uma "Cliente" (client.py) e uma "Servidor" (server.py), que realizam a troca de informações por meio de sockets.

Inicialmente, o programa servidor espera pela conexão de um programa cliente, o qual ao realizar a conexão, gera um valor inteiro aleatório de tamanho de até 30 casas, e envia ao servidor, onde é verificado se o valor tem ou não mais de 10 casas. 

Caso o valor TENHA mais de 10 casas, é gerada uma string, composta de letras minúsculas de tamanho igual ao número de casas do número verificado, que então é enviada ao cliente.

Caso não, o servidor checa se o valor é par ou ímpar, e envia ao cliente uma string com a informação obtida.

Ao receber os dados retornados pelo servidor, o programa cliente então os imprime, fecha a conexão com o servidor, e então reestabelece para enviar um outro valor inteiro aleatório.

É recomendado abrir inicialmente o programa servidor, e logo depois o cliente, embora não haja problemas em abrir o cliente primeiro.
