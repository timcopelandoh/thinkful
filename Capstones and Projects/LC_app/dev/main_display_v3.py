# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_display_v3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 579)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 971, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.a_box = QtWidgets.QCheckBox(Form)
        self.a_box.setGeometry(QtCore.QRect(40, 20, 41, 20))
        self.a_box.setObjectName("a_box")
        self.e_box = QtWidgets.QCheckBox(Form)
        self.e_box.setGeometry(QtCore.QRect(140, 20, 31, 20))
        self.e_box.setObjectName("e_box")
        self.b_box = QtWidgets.QCheckBox(Form)
        self.b_box.setGeometry(QtCore.QRect(40, 50, 31, 20))
        self.b_box.setObjectName("b_box")
        self.d_box = QtWidgets.QCheckBox(Form)
        self.d_box.setGeometry(QtCore.QRect(90, 50, 31, 20))
        self.d_box.setObjectName("d_box")
        self.g_box = QtWidgets.QCheckBox(Form)
        self.g_box.setGeometry(QtCore.QRect(180, 20, 41, 20))
        self.g_box.setObjectName("g_box")
        self.c_box = QtWidgets.QCheckBox(Form)
        self.c_box.setGeometry(QtCore.QRect(90, 20, 31, 20))
        self.c_box.setObjectName("c_box")
        self.f_box = QtWidgets.QCheckBox(Form)
        self.f_box.setGeometry(QtCore.QRect(140, 50, 31, 20))
        self.f_box.setObjectName("f_box")
        self.all_box = QtWidgets.QCheckBox(Form)
        self.all_box.setGeometry(QtCore.QRect(180, 50, 41, 20))
        self.all_box.setObjectName("all_box")
        
        self.min_prob = QtWidgets.QSlider(Form)
        self.min_prob.setGeometry(QtCore.QRect(330, 20, 251, 22))
        self.min_prob.setOrientation(QtCore.Qt.Horizontal)
        self.min_prob.setObjectName("min_prob")
        self.min_ev = QtWidgets.QSlider(Form)
        self.min_ev.setGeometry(QtCore.QRect(330, 50, 251, 22))
        self.min_ev.setOrientation(QtCore.Qt.Horizontal)
        self.min_ev.setObjectName("min_ev")
        self.max_ev = QtWidgets.QSlider(Form)
        self.max_ev.setGeometry(QtCore.QRect(710, 50, 251, 22))
        self.max_ev.setOrientation(QtCore.Qt.Horizontal)
        self.max_ev.setObjectName("max_ev")
        self.max_prob = QtWidgets.QSlider(Form)
        self.max_prob.setGeometry(QtCore.QRect(710, 20, 251, 22))
        self.max_prob.setOrientation(QtCore.Qt.Horizontal)
        self.max_prob.setObjectName("max_prob")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(660, 20, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(660, 50, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(790, 10, 101, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Loan id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Term"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Interest Rate"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Grade"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Payback Likelihood"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Expected Value"))
        self.a_box.setText(_translate("Form", "A"))
        self.e_box.setText(_translate("Form", "E"))
        self.b_box.setText(_translate("Form", "B"))
        self.d_box.setText(_translate("Form", "D"))
        self.g_box.setText(_translate("Form", "G"))
        self.c_box.setText(_translate("Form", "C"))
        self.f_box.setText(_translate("Form", "F"))
        self.all_box.setText(_translate("Form", "All"))
        self.label.setText(_translate("Form", "Interest Rate"))
        self.label_2.setText(_translate("Form", "Min:"))
        self.label_3.setText(_translate("Form", "Min:"))
        self.label_4.setText(_translate("Form", "Max:"))
        self.label_5.setText(_translate("Form", "Max:"))
        self.label_6.setText(_translate("Form", "Expected Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

