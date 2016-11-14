#!/usr/bin/python

import socket
import time
import datetime
s = socket.socket()
host = ""
port = 12346	
s.bind((host, port))
s.listen (5)
while True:
	c, addr = s.accept()
	print 'dapat perintah', c.recv(1024)
	print 'dari', addr 
	localtime = time.localtime(time.time())
	dt = datetime.datetime(*localtime[:6])
	print "Local current time :", localtime
	c.send(dt.strftime('Tanggal : %d / %m / %Y'))

c.close()
