# has_client.py

import socket

# example of socket
example = socket.getaddrinfo('hasthelargehadroncolliderdestroyedtheworldyet.com', 'http')

# create a socket (positional arguments: family, type, protocol)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

# connect to server using IP address and port
client.connect(('216.92.96.71', 80)) # No error means succesful connection to server

# send a message
msg = "GET / HTTP/1.1\r\n"
msg += "Host: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n"
msg = msg.encode('utf8')

client_send = client.sendall(msg) # No error means message has been sent
response = client.recv(2314)

if __name__ == "__main__":
    print(example)
    print()
    print(client)
    print()
    print(msg)
    print()
    print(response)
    client.close()