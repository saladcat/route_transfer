from source.Message import Message
from source.Host import Host
from source.Route import Route
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from source.Form1 import Ui_Form
import sys


class PC(QWidget, Ui_Form):

    def __init__(self, pc_id):
        super(PC, self).__init__()
        self.setupUi(self)
        self.pc_id = pc_id
        self.host = Host(pc_id)
        self.route = Route(pc_id)
        # 连接signal
        self.host.host_trans.connect(self.route.forward_msg)
        self.route.to_host_trans.connect(self.host.rec_msg)
        self.PB_send_data.clicked.connect(self.on_click_send)
        self.host.pc_trans.connect(self.show_host_info)
        self.route.pc_trans.connect(self.show_route_info)
        self.PC_name.setText(f"PC:{pc_id}")
        # show forward_table
        forward_table = self.route.forward_table
        for key in forward_table:
            value = forward_table[key]
            keyItem = QTableWidgetItem(str(key))
            valueItem = QTableWidgetItem(str(value))
            self.TV_route_table.insertRow(0)
            self.TV_route_table.setItem(0, 0, keyItem)
            self.TV_route_table.setItem(0, 1, valueItem)

    def show_host_info(self, msg):
        show_string = f"recive message:{msg.content} from id:{msg.src}"
        self.LV_send_rec_info.addItem(show_string)

    def show_route_info(self, msg, next_hop):
        show_string = f"forward message:{msg.content} to next hop:{next_hop if next_hop !=-1 else msg.dest}"
        self.LV_route_info.addItem(show_string)

    # 发送信息请求
    def on_click_send(self):
        if self.choose1.isChecked():
            rec_name = self.choose1.text()
        elif self.choose2.isChecked():
            rec_name = self.choose2.text()
        else:
            QMessageBox.information(self, "提示", "未选择接受者", QMessageBox.NoButton)
            return
        show_string = f"id:{self.pc_id} send {self.PTE_send_content.toPlainText()} to id:{rec_name}"
        self.LV_send_rec_info.addItem(show_string)
        msg = Message(self.pc_id, int(rec_name), self.PTE_send_content.toPlainText())
        self.PTE_send_content.clear()
        self.host.send_msg(msg)

    # 将3台路由器连在一起
    def link(self, pcs):
        for pc in pcs:
            self.route.route_table[pc.route.route_id] = pc.route
        if self.pc_id == 1:
            pass
        self.choose1.setText(str(pcs[0].pc_id))
        self.choose2.setText(str(pcs[1].pc_id))


def link(pcs):
    aaa = []
    for key in pcs:
        aaa.append(pcs[key])
    for pc in aaa:
        copy = aaa[:]
        copy.remove(pc)
        pc.link(copy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows_dict = {
        'PC1': PC(1),
        'PC2': PC(2),
        'PC3': PC(3),
    }

    link(windows_dict)

    windows_dict['PC1'].show()
    for index in windows_dict:
        windows_dict[index].show()
    sys.exit(app.exec_())
