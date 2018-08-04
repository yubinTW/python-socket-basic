#!/usr/bin/python3
from socket import *

host = '127.0.0.1'

s = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
s.bind((host, 0))

s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

print(s.recvfrom(65535))