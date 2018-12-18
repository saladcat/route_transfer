from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
from source.Message import Message
import socket
import json

from source.JsonHelper import *


class ListenMessage(QThread):
    trigger = pyqtSignal(Message)

    def __init__(self, route_id):
        super(ListenMessage, self).__init__()
        self.route_id = route_id

    def run(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        localhost = socket.gethostbyname("")
        port = 10000 + self.route_id
        s.bind((localhost, port))

        s.listen(5)  # 等待客户端连接
        while True:
            c, addr = s.accept()  # 建立客户端连接。
            print(f'router_{self.route_id}_rec:连接地址：', addr)
            rec = c.recv(1024).decode()
            msg = json.loads(rec, object_hook=unserialize_object)
            c.close()  # 关闭连接
            for_msg = Message(msg.src, msg.dest, msg.content)
            self.trigger.emit(for_msg)


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
        self.listen_msg = ListenMessage(route_id)
        self.listen_msg.trigger.connect(self.forward_msg)
        self.listen_msg.start()

    # 转发信息
    def forward_msg(self, msg):
        json_str = json.dumps(msg, default=serialize_instance)
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
                    port = 10000 + int(forward_route_id)
                self.pc_trans.emit(msg, int(forward_route_id))
        s.connect((host, port))
        s.send(json_str.encode())
        s.close()
