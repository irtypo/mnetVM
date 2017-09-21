#Anthony Iorio
# CS 4390.001 - Project 1: Sockets

import socket
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

serversocket.bind(('10.0.0.1', 31337))
#serversocket.bind((host, 31337))
print("Server up:",datetime.datetime.now())
exitString = 'SHUTDOWN'
serversocket.listen(5);

while True:
	clientsocket,addr = serversocket.accept()
	print("Got a connection from %s" %str(addr))

	msg = clientsocket.recv(1024)
	if msg.decode('ascii') == 'SHUTDOWN':
		print('Server down:',datetime.datetime.now())
		exit()

	msg = msg.upper()
	clientsocket.send(msg)
	clientsocket.close()


