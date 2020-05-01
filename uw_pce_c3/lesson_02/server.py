# server.py

import socket

# server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# bind server_socket to local host and port
server_socket.bind(('127.0.0.1', 50000))

# listen for incoming connections
server_socket.listen(1)

# wait for incoming connection
connection, client_address = server_socket.accept()

connection.recv(64) #b'Hello??'

connection.sendall(b'Yes? Can you hear me?!')

connection.recv(64) # b'Excellent!'