from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket
import json
from source.JsonHelper import *


class ListenMessage(QThread):
    trigger = pyqtSignal(Message)

    def __init__(self, host_id):
        super(ListenMessage, self).__init__()
        self.host_id = host_id

    def run(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        localhost = socket.gethostbyname("")
        port = 20000 + self.host_id
        s.bind((localhost, port))

        s.listen(5)  # 等待客户端连接
        while True:
            c, addr = s.accept()  # 建立客户端连接。
            print(f'host_{self.host_id}_rec:连接地址：', addr)
            rec = c.recv(1024).decode()  # 接受消息
            msg = json.loads(rec, object_hook=unserialize_object)
            c.close()  # 关闭连接
            for_msg = Message(msg.src, msg.dest, msg.content)
            self.trigger.emit(for_msg)  # 循环完毕后发出信号


class Host(QObject):
    pc_trans = pyqtSignal(Message)
    rec_trigger = pyqtSignal(Message)

    def __init__(self, host_id):
        super(Host, self).__init__()
        self.host_id = host_id
        self.listen_msg = ListenMessage(host_id)
        self.listen_msg.start()
        self.listen_msg.trigger.connect(self.rec_msg)

    # 发送消息
    def send_msg(self, msg):
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostbyname("")  # 获取本地主机名
        port = 10000 + int(msg.src)  # 设置端口号
        s.connect((host, port))
        json_str = json.dumps(msg, default=serialize_instance)
        s.send(json_str.encode())
        s.close()

    # 接受消息
    @pyqtSlot(Message)
    def rec_msg(self, msg):
        self.pc_trans.emit(msg)
