#!/usr/bin/python

import socket
s = socket.socket()
host = socket.gethostname()
port = 12346

s.connect((host, port))
s.send('helllo kelompok 2')
print s.recv(1024)
s.close
