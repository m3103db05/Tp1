from socket import *

serverPortIN = 12000

serverPortOUT = 13000

serverSocket1 = socket(AF_INET,SOCK_STREAM)

serverSocket1.bind(('',serverPortIN))

serverSocket1.listen(1)

serverSocket2 = socket(AF_INET,SOCK_STREAM)

serverSocket2.bind(('',serverPortOUT))

serverSocket2.listen(1)

print 'The server is ready to receive'


while 1:
	connectionSocket1, addr = serverSocket1.accept()

	sentence = connectionSocket1.recv(1024)

	capitalizedSentence = sentence.upper()
	connectionSocket1.send(capitalizedSentence)
	connectionSocket1.close()
    	while 1:
                connectionSocket2, addr = serverSocket2.accept()

		connectionSocket2.send(capitalizedSentence)
		print capitalizedSentence
		
		connectionSocket2.close()
