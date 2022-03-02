#!/usr/bin/env python3

from socket import *

HOSPEDEIRO = '127.0.0.1'
PORTA = 2000

clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((HOSPEDEIRO, PORTA))

mensagem = 'Olah mundo!'
dados_a_enviar = bytearray(mensagem, 'utf-8')
clienteSocket.send(dados_a_enviar)
clienteSocket.close()    