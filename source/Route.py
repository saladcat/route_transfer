from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
from source.Message import Message
import socket
import json


class ListenMessage(QThread):
    trigger = pyqtSignal(Message)

    def __init__(self, route_id):
        super(ListenMessage, self).__init__()
        self.route_id = route_id

    def run(self):
        s = socket.socket()
        localhost = socket.gethostbyname("")
        port = 10000 + self.route_id
        s.bind((localhost, port))

        s.listen(5)  # 等待客户端连接
        while True:
            c, addr = s.accept()  # 建立客户端连接。
            print('连接地址：', addr)
            rec = s.recv(1024).decode()
            msg = json.loads(rec, object_hook=Message.unserialize_object).decode()
            c.close()  # 关闭连接
            self.trigger.emit(msg)


class Route(QObject):
    # 所用到的signal
    pc_trans = pyqtSignal(Message, int)

    def __init__(self, route_id):
        super().__init__()
        self.route_id = route_id
        self.forward_table = {}
        df = pd.read_excel(f"../resource/R{self.route_id}.xlsx", sheet_name="Sheet1", header=0)
        for dest, next_hop in zip(df["dest"], df["next_hop"]):
            self.forward_table[dest] = next_hop
        listen_msg = ListenMessage(route_id)

    # 转发信息
    def forward_msg(self, msg):
        json_str = json.dumps(msg, default=Message.serialize_instance)
        dest = msg.dest

        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostbyname("")  # 获取本地主机名
        port = -1

        for route_id in self.forward_table:
            if route_id == dest:
                forward_route_id = self.forward_table[route_id]
                if forward_route_id == -1:
                    port = 20000 + int(self.route_id)  # 设置端口号
                else:
                    port = 10000 + int(self.route_id)
                self.pc_trans.emit(msg, forward_route_id)
        s.connect((host, port))
        s.send(json_str.encode())
        s.close()
