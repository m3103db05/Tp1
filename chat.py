#!/usr/bin/python

from socket import *
from threading import *
import time

# ------------------------------------------------ classe clientThread
class clientThread(Thread):

	def __init__(self, ip, port, clientsocket, liste):
	        Thread.__init__(self)
	        self.ip = ip
        	self.port = port
        	self.clientsocket = clientsocket
		self.listeClient = liste
        	print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))	

	def run(self): 
		print("Connexion de %s %s" % (self.ip, self.port, ))
		enFct = True
		sock=self.clientsocket
		while enFct == True:
			self.prompt()
			req = sock.recv(2048)
			mots = req.split(" ")
			cmde=mots[0].upper().rstrip()
			print(cmde)			
			if cmde == "QUIT" :
				self.fermer_connexion()
				enFct = False
			elif cmde == "LIST":
				self.lister_clients()
			elif cmde == "SEND":
				emetteur = str(self.ip)+":"+str(self.port)
				self.dispatch_msg(mots,emetteur)
			else:
				sock.send(" ?? \n")

	def prompt(self):
		self.clientsocket.send(" > ")

	def fermer_connexion(self):
		self.listeClient.remove(self)
		self.clientsocket.send("bye")
		self.clientsocket.close()
		print("Client deconnecte...")		

	def lister_clients(self):
		for c in self.listeClient:
			msg = str(c.ip)+":"+str(c.port)+"\n"
			self.clientsocket.send(msg)

	def dispatch_msg(self,mots,sender):
		l = len(mots)-1
		msg = ""
		for i in range(l):
			msg = msg+" "+mots[i+1]
		msg = "[ Msg from "+sender+" ] "+msg
		for c in self.listeClient:
			if c != self:
				c.clientsocket.send(msg)
				c.prompt()

	def __del__(self):
		print("destruction clientThread "+str(self.ip)+":"+str(self.port)+"\n")

# ------------------------------------------------ fin classe clientThread

# ------------------------------------------------ classe ChatServer
class ChatServer(Thread):

	def __init__(self,port):
	        Thread.__init__(self)
		self.listeClient = []
		self.s = socket(AF_INET,SOCK_STREAM)
		self.s.bind(('',port))

	def run(self): 
		while True:
			self.s.listen(5)
			print("en ecoute")
			(cSocket,(ip,port))=self.s.accept()
			newThread = clientThread(ip,port,cSocket,self.listeClient)
			self.listeClient.append(newThread)
			newThread.start()

	def __del__(self):
		print("destruction des clientThread en cours ...\n")
		for c in self.listeClient:
			c.fermer_connexion()
			self.listeClient.remove(c)
			del c 		
		print(" termine!\n")

# ------------------------------------------------ fin classe ChatServer

# -------------------------------------------------pgme ppal
fin = False
cs = ChatServer(12000)
cs.daemon = True
cs.start()
while fin == False:
	msg=raw_input("S pour stopper ChatServer : ")
	if msg.upper() == "S":
		fin = True
print ("fin")
cs=None
del cs
time.sleep(10)


