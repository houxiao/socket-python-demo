# coding: utf-8
import socket

s = socket.socket()

s.connect(('127.0.0.1', 5000))

while 1:
    cmd = input("input cmd: ")
    if cmd == 'quit':  # 不要再client里处理退出，在server中处理
        break 
    elif cmd == '':
        continue
    s.sendall(cmd.encode())
    data = s.recv(1024).decode()
    print(data)

s.close()
