from socket import *
import random
import threading

def handleClient(connectionSocket, addr):
        data = connectionSocket.recv(1024).decode()
        result = 0
        print(str(addr) + data)
        try:
            args = data.split(";")
            arg1 = int(args[1])
            arg2 = int(args[2])
            match args[0]:
                case "Random":
                    result = random.randint(arg1, arg2)
                case "Add":
                    result = arg1 + arg2
                case "Subtract":
                    result = arg1 - arg2
            connectionSocket.send(str(result).encode())
        except Exception as error:
            print(error)
            connectionSocket.send("Bad Request".encode())
        finally:
            connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client Conneted ", str(addr))
    threading.Thread(target = handleClient, args = (connectionSocket, addr, )).start()
    