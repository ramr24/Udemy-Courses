# client.py

import socket

if __name__ == "__main__":
    print("Hello")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    
    client_socket.connect(('127.0.0.1', 50000))
    
    client_socket.sendall(b'Hello??')
    
    client_socket.recv(64) # b'Yes? Can you hear me?!'

    client_socket.sendall(b'Excellent!')