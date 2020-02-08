# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

def clicked():
    apikey = ui.keybox.text()
    print(apikey)


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(410, 132)
        self.ok_button = QtWidgets.QDialogButtonBox(login)
        self.ok_button.setGeometry(QtCore.QRect(0, 70, 411, 32))
        self.ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button.setCenterButtons(True)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(clicked)
        self.keybox = QtWidgets.QLineEdit(login)
        self.keybox.setGeometry(QtCore.QRect(110, 30, 261, 21))
        self.keybox.setObjectName("keybox")
        self.keybox_label = QtWidgets.QLabel(login)
        self.keybox_label.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.keybox_label.setObjectName("keybox_label")

        self.retranslateUi(login)
        self.ok_button.accepted.connect(login.accept)
        self.ok_button.rejected.connect(login.reject)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.keybox_label.setText(_translate("login", "API Key:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

