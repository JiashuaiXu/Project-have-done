# server.py
import socket

# 创建一个TCP/IP socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到本地地址和端口
server_socket.bind(('localhost', 8000))

# 开始监听，最大连接队列长度为5
server_socket.listen(5)
print("Server listening on port 8000...")

while True:
    # 接受客户端连接（此处会自动进行三次握手）
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # 接收数据
    request = client_socket.recv(1024).decode()
    print(f"Request: {request}")

    # 生成HTTP响应
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
    client_socket.send(response.encode())

    # 关闭连接
    client_socket.close()
