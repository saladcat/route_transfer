from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Host(QObject):
    host_trans = pyqtSignal(Message)
    pc_trans = pyqtSignal(Message)

    def __init__(self, host_id):
        super().__init__()
        self.host_id = host_id

    def send_msg(self, msg):
        self.host_trans.emit(msg)

    @pyqtSlot(Message)
    def rec_msg(self, msg):
        self.pc_trans.emit(msg)
