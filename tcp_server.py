# coding: utf-8

# 流程：	服务器	创建套接字->绑定到端口->监听 处理 返回

import socket
import sys

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字 类型 流式

host = "127.0.0.1"
port = 5000
sk.bind((host, port))

sk.listen(5)

while 1:
    clnt, addr = sk.accept()
    print("client address:", addr)
    while True:
        data = clnt.recv(10).decode()
        print(data)
        if not data: break
        clnt.sendall(data.encode())
clnt.close()
