# coding: utf-8

import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(1024).decode()
        time.sleep(1)
        if not data or data == 'exit':
            break
        print("received data:", data)
        response_data = foo(data)
        sock.send(('the square is, %s!' % response_data).encode())
    sock.close()
    print('Connection from %s:%s closed.' % addr)

foo = lambda n: str(int(n)**2)

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000

sk.bind((host, port))
sk.listen(5)

print('Waiting for connection...')

while True:
    sock, addr = sk.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


