# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(770, 522)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 351, 231))
        self.groupBox.setObjectName("groupBox")
        self.PB_send_data = QtWidgets.QPushButton(self.groupBox)
        self.PB_send_data.setGeometry(QtCore.QRect(210, 50, 113, 31))
        self.PB_send_data.setObjectName("PB_send_data")
        self.choose1 = QtWidgets.QRadioButton(self.groupBox)
        self.choose1.setGeometry(QtCore.QRect(220, 130, 100, 20))
        self.choose1.setObjectName("choose1")
        self.choose2 = QtWidgets.QRadioButton(self.groupBox)
        self.choose2.setGeometry(QtCore.QRect(220, 170, 100, 20))
        self.choose2.setObjectName("choose2")
        self.PTE_send_content = QtWidgets.QPlainTextEdit(self.groupBox)
        self.PTE_send_content.setGeometry(QtCore.QRect(20, 50, 161, 141))
        self.PTE_send_content.setPlainText("")
        self.PTE_send_content.setObjectName("PTE_send_content")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 300, 361, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.LV_send_rec_info = QtWidgets.QListWidget(self.groupBox_2)
        self.LV_send_rec_info.setGeometry(QtCore.QRect(10, 30, 341, 171))
        self.LV_send_rec_info.setObjectName("LV_send_rec_info")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 300, 371, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.TV_route_table = QtWidgets.QTableWidget(self.groupBox_4)
        self.TV_route_table.setGeometry(QtCore.QRect(10, 30, 351, 171))
        self.TV_route_table.setObjectName("TV_route_table")
        self.TV_route_table.setColumnCount(2)
        self.TV_route_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TV_route_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TV_route_table.setHorizontalHeaderItem(1, item)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 50, 371, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.LV_route_info = QtWidgets.QListWidget(self.groupBox_3)
        self.LV_route_info.setGeometry(QtCore.QRect(10, 30, 351, 201))
        self.LV_route_info.setObjectName("LV_route_info")
        self.PC_name = QtWidgets.QLabel(Form)
        self.PC_name.setGeometry(QtCore.QRect(340, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.PC_name.setFont(font)
        self.PC_name.setObjectName("PC_name")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("back.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.PC_name.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "发送数据"))
        self.PB_send_data.setText(_translate("Form", "发送数据"))
        self.choose1.setText(_translate("Form", "host2"))
        self.choose2.setText(_translate("Form", "host3"))
        self.groupBox_2.setTitle(_translate("Form", "主机信息"))
        self.groupBox_4.setTitle(_translate("Form", "Routing table"))
        item = self.TV_route_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "dest"))
        item = self.TV_route_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "next_hop"))
        self.groupBox_3.setTitle(_translate("Form", "路由器信息"))
        self.PC_name.setText(_translate("Form", "ID："))

