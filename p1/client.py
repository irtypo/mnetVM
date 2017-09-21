# Anthony Iorio
# CS 4390.001 - Project 1: Sockets

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostbyaddr('10.0.0.1')

s.connect(('10.0.0.1', 31337))
#s.connect((host, 31337))
msg = input('Enter a string: ')
s.send(msg.encode('ascii'))


msg = s.recv(1024)
s.close()

print(msg.decode('ascii'))
