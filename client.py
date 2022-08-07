import socket


def client(port):    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input('Input lowercase sentence: ')
    data = message.encode('ascii')
    s.sendto(data, ('127.0.0.1', port))
    print('The OS assigned the address {} to me'.format(s.getsockname()))

    MAX_SIZE_BYTES = 65535

    data, address = s.recvfrom(MAX_SIZE_BYTES) 
    text = data.decode('ascii')
    print('The server {} replied with {!r}'.format(address, text))