#!/usr/bin/python3
from socket import *

host = '127.0.0.1'
port = 9999

s = socket(AF_INET, SOCK_STREAM, 0)
s.connect((host,port))

msg = 'hi there from the client'
s.send(msg.encode('ascii'))

rmsg = s.recv(1024)

print(rmsg.decode('ascii'))
s.close()