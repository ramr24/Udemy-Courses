# sockets.py

import socket

# create a socket (positional arguments: family, type, protocol)
foo = socket.socket()

def get_constants(prefix):
    """filtered mapping of socket module constants to their names"""
    return {getattr(socket, name): name 
            for name in dir(socket) if name.startswith(prefix)}

def get_address_info(host, port):
    for response in socket.getaddrinfo(host, port):
        family, s_type, protocol, name, address = response
        print('family: {}'.format(families[family]))
        print('type: {}'.format(types[s_type]))
        print('protocol: {}'.format(protocols[protocol]))
        print('canonical name: {}'.format(name))
        print('socket address: {}'.format(address))
        print('')


if __name__ == "__main__":
    # What port a service uses
    print(socket.getservbyname('ssh')) # 22
    # What service a port uses
    print(socket.getservbyport(80)) # http
    # Hostname
    print(socket.gethostname()) # DESKTOP-JDL5VEN
    # IP Address
    print(socket.gethostbyname(socket.gethostname())) # 192.168.1.13
    print()
    print("IP address examples:")
    print(socket.gethostbyname('google.com')) # 216.58.193.78
    print(socket.gethostbyname('uw.edu')) # 128.95.155.135
    print(socket.gethostbyname('info.cern.ch')) # 188.184.100.82
    print()
    # More information
    print(socket.gethostbyname_ex('info.cern.ch'))
    print(socket.gethostbyname_ex('google.com'))
    print()
    # Created a socket called foo
    print(foo)
    print()
    print(foo.family) # family
    print(foo.type) # type
    print(foo.proto) # protocol
    print()
    families = get_constants('AF')
    print(families)
    print()
    types = get_constants('SOCK')
    print(types)
    print()
    protocols = get_constants('IPPROTO')
    print(protocols)
    print()
    #Piciking out specific family, type and protocol
    print(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
    print()
    # Information about available connections of a given host
    print(socket.getaddrinfo('google.com', 80))
    print()
    get_address_info(socket.gethostname(), 'http')