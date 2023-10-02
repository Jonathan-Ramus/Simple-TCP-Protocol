from socket import *

serverName = input('Server IP: ')
serverPort = int(input('Server Port: '))
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
method = input('Method: ')
arg1 = input('1st Argument: ')
arg2 = input('2nd Argument: ')
sentence = ";".join([method, arg1, arg2])
clientSocket.send(sentence.encode())
response = clientSocket.recv(1024)
print('From server: ', response.decode())
clientSocket.close()