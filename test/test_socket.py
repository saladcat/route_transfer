import socket

if __name__ == '__main__':
    s = socket.socket()
    localhost = socket.gethostbyname("")
    port = 10001
    s.bind((localhost, port))

    s.listen(5)  # 等待客户端连接
    while True:
        c, addr = s.accept()  # 建立客户端连接。
        print('连接地址：', addr)
        c.send("hakka".encode())
        c.close()  # 关闭连接
