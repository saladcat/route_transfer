from source.Message import Message
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
from source.Message import Message


class Route(QObject):
    route_trans = pyqtSignal(Message)
    to_host_trans = pyqtSignal(Message)
    pc_trans = pyqtSignal(Message, int)

    def __init__(self, route_id):
        super().__init__()
        self.route_id = route_id
        self.forward_table = {}
        self.route_table = {}
        df = pd.read_excel(f"../resource/R{self.route_id}.xlsx", sheet_name="Sheet1", header=0)
        for dest, next_hop in zip(df["dest"], df["next_hop"]):
            self.forward_table[dest] = next_hop

    def forward_msg(self, msg):
        src = msg.src
        dest = msg.dest
        content = msg.content

        flag = False
        for route_id in self.forward_table:
            if route_id == dest:
                forward_route_id = self.forward_table[route_id]
                if forward_route_id == -1:
                    self.to_host_trans.emit(msg)
                else:
                    self.route_trans.connect(self.route_table[forward_route_id].forward_msg)
                    self.route_trans.emit(msg)
                    self.route_trans.disconnect()
                self.pc_trans.emit(msg, forward_route_id)

    def regis_route(self, routes):
        for route in routes:
            self.route_table[route.route_id] = route
