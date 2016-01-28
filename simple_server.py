import socket
import sys


loopback = '127.0.0.1'
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
conn, addr = sock.accept()
while True:
    data = conn.recv(1000)
    if not data:
        break
    print data
    conn.sendall(data)

conn.close()
sock.close()