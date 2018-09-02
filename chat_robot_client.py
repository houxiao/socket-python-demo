# coding: utf-8

import socket

s=socket.socket()
host=socket.gethostbyname(socket.gethostname())
port=8888

s.connect((host,port))

while True:
	cmd=raw_input('input:')

	if cmd=='quit': break
	if cmd=='': continue
	s.sendall(cmd)
	data=s.recv(1024)
	print data
s.close()