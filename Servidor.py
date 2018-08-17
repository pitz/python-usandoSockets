from __future__ import print_function
import random
import socket

regP = 0  # P
regG = 0  # g
regA = 6  # a
regB = 15 # b

host = ''
port = 7002
recebe = "" #var. que recebe a mensagem

addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10) #limite de conexoes

print('Servidor Online.')
con, cliente = serv_socket.accept()

print('Estabelecendo Conexecao...')

# Receber o regP
regRecebe = con.recv(1024)
regP = int(regRecebe)

# Buscar valor randomico para regG
while regG == 0:
    auxG = random.randrange(1, regP)
    if (((2**(auxG-1)) % auxG) == 1): regG = auxG 
    if (((3**(auxG-1)) % auxG) == 1): regG = auxG
    if (((4**(auxG-1)) % auxG) == 1): regG = auxG
    if (((5**(auxG-1)) % auxG) == 1): regG = auxG
    if (((6**(auxG-1)) % auxG) == 1): regG = auxG

# Envia o valor calculado para regG 
con.send(str(regG))

# Buscar valor randomico para regB
regB = random.randrange(1, 255)
B = (regG ** regB) % regP

# Enviar o B
con.send(str(B))

regRecebe = con.recv(1024)
A = int(regRecebe)
# Recebe o A

regChaveB = (A ** regB) % regP	
print("Chave Calculada: ", regChaveB)
