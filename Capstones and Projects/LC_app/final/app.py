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
import pickle
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

        modelinput['intrate'] = loans['intRate']

        modelinput['A'] = loans['grade'] == 'A'
        modelinput['B'] = loans['grade'] == 'B'
        modelinput['C'] = loans['grade'] == 'C'
        modelinput['D'] = loans['grade'] == 'D'
        modelinput['E'] = loans['grade'] == 'E'
        modelinput['F'] = loans['grade'] == 'F'
        modelinput['G'] = loans['grade'] == 'G'

        rf = pickle.load(open('rf.sav', 'rb'))

        loans['predict'] = [x[1] for x in rf.predict_proba(modelinput)]
        loans['predict_str'] = loans.apply(lambda x: str(round(x['predict']*100,1))+'%', axis=1)

        def total_int_paid(n, i):
            ii = i/12
            return n*(ii * (1 + ii) ** n) / ((1+ii)**n - 1)-1

        loans['total_int_paid'] = loans.apply(lambda x: total_int_paid(36, x['intRate']/100), axis=1)

        loans['EV'] = (loans['predict'] * loans['total_int_paid'] - .37 * (1 - loans['predict'])) * 100
        loans['EV_str'] = loans['EV'].apply(lambda x: str(round(x, 1)) + '%')

        loans['intRate_str'] = loans['intRate'].apply(lambda x: str(x) + '%')

        global display_raw
        display_raw = loans[loans.term == 36][['id', 'loanAmount', 'term', 'intRate', 'intRate_str', 'grade', 'predict_str', 'EV', 'EV_str']]




        display_raw['loanAmount'] = display_raw['loanAmount'].apply(lambda x: '$'+'{:,.2f}'.format(x))

        global display
        display_raw = display_raw.sort_values(by=['grade', 'EV'], ascending=[1,0])

        display = display_raw[['id', 'loanAmount', 'term', 'intRate_str', 'grade', 'predict_str', 'EV_str']]


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

        self.a_box.setCheckState(2)
        self.b_box.setCheckState(2)
        self.c_box.setCheckState(2)
        self.d_box.setCheckState(2)
        self.e_box.setCheckState(2)
        self.f_box.setCheckState(2)
        self.g_box.setCheckState(2)
        self.all_box.setCheckState(2)

        self.a_box.clicked.connect(self.redraw)
        self.b_box.clicked.connect(self.redraw)
        self.c_box.clicked.connect(self.redraw)
        self.d_box.clicked.connect(self.redraw)
        self.e_box.clicked.connect(self.redraw)
        self.f_box.clicked.connect(self.redraw)
        self.g_box.clicked.connect(self.redraw)
        self.all_box.clicked.connect(self.all_box_func)
        
        self.min_int = QtWidgets.QSlider(Form)
        self.min_int.setGeometry(QtCore.QRect(330, 20, 251, 22))
        self.min_int.setOrientation(QtCore.Qt.Horizontal)
        self.min_int.setObjectName("min_int")
        self.min_int.setMinimum(min(display_raw.intRate)-1)
        self.min_int.setMaximum(max(display_raw.intRate)+1)
        self.min_int.sliderMoved.connect(self.redraw)
        
        self.min_ev = QtWidgets.QSlider(Form)
        self.min_ev.setGeometry(QtCore.QRect(710, 20, 251, 22))  #
        self.min_ev.setOrientation(QtCore.Qt.Horizontal)
        self.min_ev.setObjectName("min_ev")
        self.min_ev.setMinimum(min(display_raw.EV)-1)
        self.min_ev.setMaximum(max(display_raw.EV)+1)
        self.min_ev.sliderMoved.connect(self.redraw)
        
        self.max_ev = QtWidgets.QSlider(Form)
        self.max_ev.setGeometry(QtCore.QRect(710, 50, 251, 22))
        self.max_ev.setOrientation(QtCore.Qt.Horizontal)
        self.max_ev.setObjectName("max_ev")
        self.max_ev.setMinimum(min(display_raw.EV)-1)
        self.max_ev.setMaximum(max(display_raw.EV)+1)
        self.max_ev.setValue(max(display_raw.EV)+1)
        self.max_ev.sliderMoved.connect(self.redraw)
        
        self.max_int = QtWidgets.QSlider(Form)
        self.max_int.setGeometry(QtCore.QRect(330, 50, 251, 22)) #(710, 20, 251, 22)
        self.max_int.setOrientation(QtCore.Qt.Horizontal)
        self.max_int.setObjectName("max_int")
        self.max_int.setMinimum(min(display_raw.intRate)-1)
        self.max_int.setMaximum(max(display_raw.intRate)+1)
        self.max_int.setValue(max(display_raw.intRate)+1)
        self.max_int.sliderMoved.connect(self.redraw)

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
        Form.setWindowTitle(_translate("Form", "Lending Club Live Dashboard"))
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

    def redraw(self):

        disp_rows = [(self.a_box.checkState() == 2) * 'A', 
                    (self.b_box.checkState() == 2) * 'B',
                    (self.c_box.checkState() == 2) * 'C',
                    (self.d_box.checkState() == 2) * 'D',
                    (self.e_box.checkState() == 2) * 'E',
                    (self.f_box.checkState() == 2) * 'F',
                    (self.g_box.checkState() == 2) * 'G',
                    ]


        newdf = display[[x in disp_rows for x in display.grade] & 
                    (display_raw['intRate'] >= self.min_int.value()) & 
                    (display_raw['intRate'] <= self.max_int.value()) &
                    (display_raw['EV'] >= self.min_ev.value()) &
                    (display_raw['EV'] <= self.max_ev.value())
                    ]

        self.tableWidget.setRowCount(newdf.shape[0])


        for r in range(newdf.shape[0]):
            for c in range(7):
                self.tableWidget.setItem(r,c,QtWidgets.QTableWidgetItem(str(newdf.iloc[r,c])))

    def all_box_func(self):
        self.a_box.setCheckState(self.all_box.checkState())
        self.b_box.setCheckState(self.all_box.checkState())
        self.c_box.setCheckState(self.all_box.checkState())
        self.d_box.setCheckState(self.all_box.checkState())
        self.e_box.setCheckState(self.all_box.checkState())
        self.f_box.setCheckState(self.all_box.checkState())
        self.g_box.setCheckState(self.all_box.checkState())
        self.redraw()

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
        self.keybox.setEchoMode(QtWidgets.QLineEdit.Password)

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

    
    
