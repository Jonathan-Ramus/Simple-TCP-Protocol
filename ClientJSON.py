from socket import *
import json

serverName = input('Server IP: ')
serverPort = int(input('Server Port: '))
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
method = input('Method: ')
arg1 = input('1st Argument: ')
arg2 = input('2nd Argument: ')
jsonObj = {
    "method" : method,
    "arg1" : arg1,
    "arg2" : arg2
}
jsonString = json.dumps(jsonObj)
clientSocket.send(jsonString.encode())
response = clientSocket.recv(1024)
print('From server: ', response.decode())
clientSocket.close()