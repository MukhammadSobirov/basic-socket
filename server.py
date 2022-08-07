import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000

hostname = '127.0.0.1'

s.bind((hostname, port))

print('Listening at {}'.format(s.getsockname()))


MAX_SIZE_BYTES = 65535 

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    uppercase_msg = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = uppercase_msg.encode('ascii')
    s.sendto(data, clientAddress)