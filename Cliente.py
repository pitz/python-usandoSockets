# Pacotes 
from __future__ import print_function
import random
import socket

regP = 0  # P
regG = 0  # g
regA = 6  # a
regB = 15 # b

ip = 'localhost' #raw_input('Digite o IP de conexao: ')
port = 7002
mensagem = ""
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

# Buscar valor randomico para regP
while regP == 0:
    auxP = random.randrange(32, 2048)
    if (((2**(auxP-1)) % auxP) == 1): regP = auxP 
    if (((3**(auxP-1)) % auxP) == 1): regP = auxP
    if (((4**(auxP-1)) % auxP) == 1): regP = auxP
    if (((5**(auxP-1)) % auxP) == 1): regP = auxP
    if (((6**(auxP-1)) % auxP) == 1): regP = auxP

# Enviar o regP
regEnvio = str(regP)
client_socket.send(regEnvio)

# Receber o regG
regRecebe = client_socket.recv(1024)
regG = int(regRecebe)

# Buscar valor randomico para regA
regA = random.randrange(1, 255)
A = (regG ** regA) % regP

# Enviar o A
client_socket.send(str(A))

# Recebe o B
regRecebe = client_socket.recv(1024)
B = int(regRecebe)

# Calculando as Chaves
regChave  = (B ** regA) % regP
print("Chave Calculada: ", regChave)

while (mensagem != "SAIR"):
    mensagem = raw_input("Digite a mensagem para enviar ao servidor")
    client_socket.send(mensagem)
    print("Mensagem enviada")
    data = client_socket.recv(1024)
    print('Mensagem recebida: ' + data)
    
client_socket.close()
