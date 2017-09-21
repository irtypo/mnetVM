import time
from socket import *

count = 1
while count < 11:
	s = socket(AF_INET, SOCK_DGRAM)			# create UDP socket
	s.settimeout(1)							# set timeout to 1 sec

	msg = "ping"
	addr = ('10.0.0.1', 31337)				# set server address
	sTime = time.time()						# get start time
	s.sendto(msg.encode('ascii'), addr)		# ping server

	try:
		data, server = s.recvfrom(1024)		# listen for server
		eTime = time.time()					# set end time
		rtt = eTime - sTime 				# calculate RTT
		print(count," RTT: ",rtt)					
	except timeout:	
		print("REQUEST TIMED OUT")

	count += 1

