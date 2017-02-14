# Tp1

## P1
*UDPclient.py*

from socket import *

serverName = 'hostname'

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)

message = input("Input lowercase sentence:")

clientSocket.sendto(message,(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print modifiedMessage

clientSocket.close()

*UDPserver.py*
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print "the server is ready to receive"

while 1:

	message, clientAddress = serverSocket.recvfrom(2048)

	modifiedMessage = message.upper()

	serverSocket.sendto(modifiedMessage, clientAddress)
