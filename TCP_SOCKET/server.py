#!/usr/bin/python3
from socket import *

host = '127.0.0.1'
port = 9999

s = socket(AF_INET, SOCK_STREAM, 0)
s.bind((host, port))

s.listen(5)

while True:
    c,addr = s.accept()
    rmsg = c.recv(1024)
    print(rmsg.decode("ascii"))

    msg = 'hi this msg from the server'
    c.send(msg.encode('ascii'))

    break

s.close()