# TCP编程

## socket编程思路
### TCP服务端：

1 创建套接字，绑定套接字到本地IP与端口
```python
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind()
```

2 开始监听连接
```python
s.listen()
```

3 进入循环，不断接受客户端的连接请求
```python
s.accept()
```

4 然后接收传来的数据，并发送给对方数据
```python
s.recv()
s.sendall()
```

5 传输完毕后，关闭套接字
```python
s.close()
```

### TCP客户端:

1 创建套接字，连接远端地址
```python
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect()
```

2 连接后发送数据和接收数据
```python
s.sendall()
s.recv()
```

3 传输完毕后，关闭套接字
```python
s.close()
```
