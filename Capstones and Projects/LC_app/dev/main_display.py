# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_display.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import statsmodels.api as sm

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


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 579)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 971, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(disp.shape[0])
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

        for r in range(disp.shape[0]):
            for c in range(7):
                self.tableWidget.setItem(r,c,QtWidgets.QTableWidgetItem(str(disp.iloc[r,c])))


        self.a_box = QtWidgets.QCheckBox(Form)
        self.a_box.setGeometry(QtCore.QRect(30, 20, 87, 20))
        self.a_box.setObjectName("a_box")
        self.a_box.setCheckState(2)
        #self.a_box.stateChanged(1).connect(redraw)
        #self.a_box.stateChanged(2).connect(redraw)
        self.e_box = QtWidgets.QCheckBox(Form)
        self.e_box.setGeometry(QtCore.QRect(230, 20, 87, 20))
        self.e_box.setObjectName("e_box")
        self.e_box.setCheckState(2)
        self.b_box = QtWidgets.QCheckBox(Form)
        self.b_box.setGeometry(QtCore.QRect(30, 50, 87, 20))
        self.b_box.setObjectName("b_box")
        self.b_box.setCheckState(2)
        self.d_box = QtWidgets.QCheckBox(Form)
        self.d_box.setGeometry(QtCore.QRect(130, 50, 87, 20))
        self.d_box.setObjectName("d_box")
        self.d_box.setCheckState(2)
        self.g_box = QtWidgets.QCheckBox(Form)
        self.g_box.setGeometry(QtCore.QRect(330, 20, 87, 20))
        self.g_box.setObjectName("g_box")
        self.g_box.setCheckState(2)
        self.c_box = QtWidgets.QCheckBox(Form)
        self.c_box.setGeometry(QtCore.QRect(130, 20, 87, 20))
        self.c_box.setObjectName("c_box")
        self.c_box.setCheckState(2)
        self.f_box = QtWidgets.QCheckBox(Form)
        self.f_box.setGeometry(QtCore.QRect(230, 50, 87, 20))
        self.f_box.setObjectName("f_box")
        self.f_box.setCheckState(2)
        self.all_box = QtWidgets.QCheckBox(Form)
        self.all_box.setGeometry(QtCore.QRect(330, 50, 87, 20))
        self.all_box.setObjectName("all_box")
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
        self.min_int.setGeometry(QtCore.QRect(450, 20, 251, 22))
        self.min_int.setOrientation(QtCore.Qt.Horizontal)
        self.min_int.setObjectName("min_int")
        self.min_int.setMinimum(min(disp.int_rate)-1)
        self.min_int.setMaximum(max(disp.int_rate)+1)
        self.min_int.sliderMoved.connect(self.redraw)
        self.min_ev = QtWidgets.QSlider(Form)
        self.min_ev.setGeometry(QtCore.QRect(450, 50, 251, 22))
        self.min_ev.setOrientation(QtCore.Qt.Horizontal)
        self.min_ev.setObjectName("min_ev")
        self.max_ev = QtWidgets.QSlider(Form)
        self.max_ev.setGeometry(QtCore.QRect(729, 50, 251, 22))
        self.max_ev.setOrientation(QtCore.Qt.Horizontal)
        self.max_ev.setObjectName("max_ev")
        self.max_int = QtWidgets.QSlider(Form)
        self.max_int.setGeometry(QtCore.QRect(729, 20, 251, 22))
        self.max_int.setOrientation(QtCore.Qt.Horizontal)
        self.max_int.setObjectName("max_int")
        self.max_int.setMinimum(min(disp.int_rate)-1)
        self.max_int.setMaximum(max(disp.int_rate)+1)
        self.max_int.setValue(max(disp.int_rate)+1)
        self.max_int.sliderMoved.connect(self.redraw)

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

    def redraw(self):

        disp_rows = [(self.a_box.checkState() == 2) * 'A', 
                    (self.b_box.checkState() == 2) * 'B',
                    (self.c_box.checkState() == 2) * 'C',
                    (self.d_box.checkState() == 2) * 'D',
                    (self.e_box.checkState() == 2) * 'E',
                    (self.f_box.checkState() == 2) * 'F',
                    (self.g_box.checkState() == 2) * 'G',
                    ]


        newdf = disp[[x in disp_rows for x in disp.grade] & 
                    (disp['int_rate'] >= self.min_int.value()) & 
                    (disp['int_rate'] <= self.max_int.value())]

        self.tableWidget.setRowCount(newdf.shape[0])

        print(self.min_int.value())
        print(self.max_int.value())

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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

