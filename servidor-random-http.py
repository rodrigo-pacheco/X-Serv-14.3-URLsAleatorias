#!/usr/bin/python3
"""
Simple HTTP Server: serves random URLs usign a hyperlink

Rodrigo Pacheco Martinez-Atienza
r.pachecom @ gsyc.es
SAT subject (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        aleat = str(random.randrange(999999999))
        recvSocket.send(bytes(
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello\r World!</h1>" +
                        b"<p>And in particular hello to you, " +
                        bytes(address[0], 'utf-8') +
                        b"</p>" +
                        b"</body></html>" +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
