# client.py
import socket

# 创建一个TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(('localhost', 8000))

# 发送HTTP请求
http_request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.send(http_request.encode())

# 接收HTTP响应
response = client_socket.recv(1024).decode()
print(f"Response: {response}")

# 关闭连接
client_socket.close()
