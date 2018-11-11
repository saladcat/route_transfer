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
        Form.resize(570, 373)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 291, 151))
        self.groupBox.setObjectName("groupBox")
        self.PB_send_data = QtWidgets.QPushButton(self.groupBox)
        self.PB_send_data.setGeometry(QtCore.QRect(160, 50, 113, 31))
        self.PB_send_data.setObjectName("PB_send_data")
        self.choose1 = QtWidgets.QRadioButton(self.groupBox)
        self.choose1.setGeometry(QtCore.QRect(170, 80, 100, 20))
        self.choose1.setObjectName("choose1")
        self.choose2 = QtWidgets.QRadioButton(self.groupBox)
        self.choose2.setGeometry(QtCore.QRect(170, 110, 100, 20))
        self.choose2.setObjectName("choose2")
        self.PTE_send_content = QtWidgets.QPlainTextEdit(self.groupBox)
        self.PTE_send_content.setGeometry(QtCore.QRect(20, 50, 141, 71))
        self.PTE_send_content.setPlainText("")
        self.PTE_send_content.setObjectName("PTE_send_content")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 291, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.LV_send_rec_info = QtWidgets.QListWidget(self.groupBox_2)
        self.LV_send_rec_info.setGeometry(QtCore.QRect(10, 30, 271, 101))
        self.LV_send_rec_info.setObjectName("LV_send_rec_info")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(330, 210, 231, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.TV_route_table = QtWidgets.QTableWidget(self.groupBox_4)
        self.TV_route_table.setGeometry(QtCore.QRect(10, 20, 211, 111))
        self.TV_route_table.setObjectName("TV_route_table")
        self.TV_route_table.setColumnCount(2)
        self.TV_route_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TV_route_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TV_route_table.setHorizontalHeaderItem(1, item)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 50, 251, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.LV_route_info = QtWidgets.QListWidget(self.groupBox_3)
        self.LV_route_info.setGeometry(QtCore.QRect(10, 20, 221, 121))
        self.LV_route_info.setObjectName("LV_route_info")
        self.PC_name = QtWidgets.QLabel(Form)
        self.PC_name.setGeometry(QtCore.QRect(280, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.PC_name.setFont(font)
        self.PC_name.setObjectName("PC_name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "发送数据"))
        self.PB_send_data.setText(_translate("Form", "发送数据"))
        self.choose1.setText(_translate("Form", "host2"))
        self.choose2.setText(_translate("Form", "host3"))
        self.groupBox_2.setTitle(_translate("Form", "信息显示"))
        self.groupBox_4.setTitle(_translate("Form", "Routing table"))
        item = self.TV_route_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "dest"))
        item = self.TV_route_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "next_hop"))
        self.groupBox_3.setTitle(_translate("Form", "信息"))
        self.PC_name.setText(_translate("Form", "ID："))

