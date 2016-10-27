#!/usr/bin/python
#compact tcp connect scanner that should work anywhere
import sys
from socket import socket
HOST = sys.argv[1]
for PORT in range(1, 1025):
    s = socket()
    if s.connect_ex((HOST, PORT)) == 0:
        print "\t%s is open!" % PORT
