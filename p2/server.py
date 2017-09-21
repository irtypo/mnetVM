# Anthony Iorio
# CS 4390.001 - Assignment 2: UDP pinger (server)

import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)		# Create a UDP socket
print("Server up")

serverSocket.bind(('', 31337))
while True:
	
	rand = random.randint(0, 10)				# random num 0-10
	msg, addr = serverSocket.recvfrom(1024)		# receives client packet with addr

	#if rand < 4:
	#	continue								# packet lost

	serverSocket.sendto(msg, addr)				# server responds 

