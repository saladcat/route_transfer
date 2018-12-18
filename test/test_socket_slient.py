import socket  # 导入 socket 模块

if __name__ == '__main__':
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostbyname("")  # 获取本地主机名
    port = 10001  # 设置端口号
    s.connect((host, port))
    print(s.recv(1024))
    s.close()
