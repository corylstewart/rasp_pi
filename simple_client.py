import socket
import sys


loopback = '127.0.0.1'
port = 1234

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

sock.connect((loopback, port))

while True:
    data = raw_input()
    if data == 'done':
        break
    try:
        sock.sendall(data)
    except socket.error:
        print 'Failed to send'
    response = sock.recv(1000)
    print response

sock.close()