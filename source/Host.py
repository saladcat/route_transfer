from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Host(QObject):
    host_trans = pyqtSignal(Message)
    pc_trans = pyqtSignal(Message)

    def __init__(self, host_id):
        super().__init__()
        self.host_id = host_id

    # 发送消息
    def send_msg(self, msg):
        self.host_trans.emit(msg)

    # 接受消息
    @pyqtSlot(Message)
    def rec_msg(self, msg):
        self.pc_trans.emit(msg)
