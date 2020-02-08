# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
import datetime
import statsmodels.api as sm
import requests
import warnings

warnings.filterwarnings('ignore')


'''
live = pd.read_csv('live.csv')

# create DF for data that needs to be fed into the model
live_input = live[['loan_amnt', 'ln_annual_inc', 'dti', 'fico_range_high', 'delinq_2yrs', 'num_delinq_2yrs', 'ln_earliest_cr_line', 'inq_last_6mths', 'num_inq_last_6mths', 'ln_open_acc', 'pub_rec', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']]

# load trained model
logit = sm.load('fitted_logit.pickle')

# create column for predicted values and the same value 
# in a readable string format
live['predict'] = logit.predict(live_input.astype(float))
live['predict_str'] = live.apply(lambda x: str(round(x['predict']*100,1))+'%', axis=1)

def total_int_paid(n, i):
    ii = i/12
    return n*(ii * (1 + ii) ** n) / ((1+ii)**n - 1)-1

live['total_int_paid'] = live.apply(lambda x: total_int_paid(36, x['int_rate']/100), axis=1)

live['EV'] = (live['predict'] * live['total_int_paid'] - .37 * (1 - live['predict'])) * 100
live['EV_str'] = live['EV'].apply(lambda x: str(round(x, 1)) + '%')

# create DF of data we want to display
disp = live[['id', 'loan_amnt', 'term', 'int_rate', 'grade', 'predict_str', 'EV_str']]

# sort display dataframe and print to console
disp = disp.sort_values(by = ['grade', 'EV_str'], ascending = [1,0])
'''

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 579)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 971, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

        header = {'Authorization': apikey, 'Content-Type': 'application/json'}
        params = {'showAll': 'True'}

        resp = requests.get('https://api.lendingclub.com/api/investor/v1/loans/listing', headers=header, params=params)

        loans = resp.json()['loans']

        loans = pd.DataFrame.from_dict(loans)

        modelinput = loans[['loanAmount', 'annualInc', 'dti', 'ficoRangeHigh', 'delinq2Yrs', 
        'earliestCrLine', 'inqLast6Mths', 'openAcc', 'pubRec', 'revolBal', 'revolUtil', 'totalAcc']]

        modelinput['lnAnnualInc'] = np.log(modelinput.annualInc)
        modelinput['boolDelinq2Yrs'] = modelinput['delinq2Yrs'] >= 1

        def convert_date(x):
            return datetime.date(int(x[:4]), int(x[5:7]), int(x[8:10]))

        modelinput['lnEarliestCrLine'] = modelinput['earliestCrLine'].apply(lambda x: np.log((datetime.date.today()-convert_date(x)).days))

        modelinput['boolInqLast6Mths'] = modelinput['inqLast6Mths'] >= 1
        modelinput['lnOpenAcc'] = np.log(modelinput['openAcc'])
        modelinput['boolPubRec'] = modelinput['pubRec'] >= 1
        modelinput['lnRevolBal'] = np.log(modelinput['revolBal'])

        modelinput = modelinput[['loanAmount', 'lnAnnualInc', 'dti', 'ficoRangeHigh', 'boolDelinq2Yrs', 'delinq2Yrs', 
        'lnEarliestCrLine', 'boolInqLast6Mths', 'inqLast6Mths', 'lnOpenAcc', 'boolPubRec', 'pubRec', 'lnRevolBal', 'revolUtil', 'totalAcc']]

        logit = sm.load('fitted_logit.pickle')

        loans['predict'] = logit.predict(modelinput.astype(float))
        loans['predict_str'] = loans.apply(lambda x: str(round(x['predict']*100,1))+'%', axis=1)

        def total_int_paid(n, i):
            ii = i/12
            return n*(ii * (1 + ii) ** n) / ((1+ii)**n - 1)-1

        loans['total_int_paid'] = loans.apply(lambda x: total_int_paid(36, x['intRate']/100), axis=1)


        loans['EV'] = (loans['predict'] * loans['total_int_paid'] - .37 * (1 - loans['predict'])) * 100
        loans['EV_str'] = loans['EV'].apply(lambda x: str(round(x, 1)) + '%')

        display = loans[loans.term == 36][['id', 'loanAmount', 'term', 'intRate', 'grade', 'predict_str', 'EV_str']]

        display = display.sort_values(by=['grade', 'EV_str'], ascending=[1,0])

        self.tableWidget.setRowCount(display.shape[0])
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

        for r in range(display.shape[0]):
            for c in range(7):
                self.tableWidget.setItem(r,c,QtWidgets.QTableWidgetItem(str(display.iloc[r,c])))


        self.a_box = QtWidgets.QCheckBox(Form)
        self.a_box.setGeometry(QtCore.QRect(30, 20, 87, 20))
        self.a_box.setObjectName("a_box")
        self.e_box = QtWidgets.QCheckBox(Form)
        self.e_box.setGeometry(QtCore.QRect(230, 20, 87, 20))
        self.e_box.setObjectName("e_box")
        self.b_box = QtWidgets.QCheckBox(Form)
        self.b_box.setGeometry(QtCore.QRect(30, 50, 87, 20))
        self.b_box.setObjectName("b_box")
        self.d_box = QtWidgets.QCheckBox(Form)
        self.d_box.setGeometry(QtCore.QRect(130, 50, 87, 20))
        self.d_box.setObjectName("d_box")
        self.g_box = QtWidgets.QCheckBox(Form)
        self.g_box.setGeometry(QtCore.QRect(330, 20, 87, 20))
        self.g_box.setObjectName("g_box")
        self.c_box = QtWidgets.QCheckBox(Form)
        self.c_box.setGeometry(QtCore.QRect(130, 20, 87, 20))
        self.c_box.setObjectName("c_box")
        self.f_box = QtWidgets.QCheckBox(Form)
        self.f_box.setGeometry(QtCore.QRect(230, 50, 87, 20))
        self.f_box.setObjectName("f_box")
        self.all_box = QtWidgets.QCheckBox(Form)
        self.all_box.setGeometry(QtCore.QRect(330, 50, 87, 20))
        self.all_box.setObjectName("all_box")
        self.min_prob = QtWidgets.QSlider(Form)
        self.min_prob.setGeometry(QtCore.QRect(450, 20, 251, 22))
        self.min_prob.setOrientation(QtCore.Qt.Horizontal)
        self.min_prob.setObjectName("min_prob")
        self.min_ev = QtWidgets.QSlider(Form)
        self.min_ev.setGeometry(QtCore.QRect(450, 50, 251, 22))
        self.min_ev.setOrientation(QtCore.Qt.Horizontal)
        self.min_ev.setObjectName("min_ev")
        self.max_ev = QtWidgets.QSlider(Form)
        self.max_ev.setGeometry(QtCore.QRect(729, 50, 251, 22))
        self.max_ev.setOrientation(QtCore.Qt.Horizontal)
        self.max_ev.setObjectName("max_ev")
        self.max_prob = QtWidgets.QSlider(Form)
        self.max_prob.setGeometry(QtCore.QRect(729, 20, 251, 22))
        self.max_prob.setOrientation(QtCore.Qt.Horizontal)
        self.max_prob.setObjectName("max_prob")

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
        self.ok_button.clicked.connect(self.logging_in)
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

    def logging_in(self):
        global apikey 
        apikey = ui.keybox.text()
        Form = QtWidgets.QDialog()
        uimain = Ui_Form()
        uimain.setupUi(Form)
        Form.show()
        Form.exec_()


    
#Form = QtWidgets.QWidget()
#uimain = Ui_Form()
#uimain.setupUi(Form)
#Form.show()

def clicked():
    apikey = ui.keybox.text()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()

    sys.exit(app.exec_())
    #app.exec_()

    
    
