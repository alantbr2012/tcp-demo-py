#!/usr/bin/env python3
# arquivo: servidor.py

from socket import *

HOSPEDEIRO = '0.0.0.0'
PORTA = 2000

socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind((HOSPEDEIRO, PORTA))
socketServidor.listen(1)
print('Esperando por uma conexão...')
conexao, endereco = socketServidor.accept()
print ('Conexao vinda de {end_ip} pela porta {num_porta}'.format(
    end_ip=endereco[0], num_porta=endereco[1]))

dados = conexao.recv(1024)
dados = dados.decode('utf-8')
print(f'Recebi "{dados}"')
    
conexao.close()












