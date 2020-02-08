import numpy as np
import pandas as pd
from sklearn import ensemble
import datetime
import warnings
import pickle

warnings.filterwarnings('ignore')

loan = pd.read_csv('../../accepted_2007_to_2018Q4.csv')

# Dictionary that returns corresponding month number when given a 3-letter string
return_number = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

# Function that converts string date format to datetime format
def convert_date(d):
    try:
        return datetime.date(year=int(d[4:]), month=return_number[d[:3]], day=1)
    except:
        pass

# Apply function to issue_d and earliest_cr_line fields
loan['issue_d'] = loan['issue_d'].apply(convert_date)
loan['earliest_cr_line'] = loan['earliest_cr_line'].apply(convert_date)

# Restrict analysis to loans originating from January 2010 to July 2015
loan = loan[loan.issue_d < datetime.date(2015,7,1)]
loan = loan[loan.issue_d >= datetime.date(2010,1,1)]
loan = loan[loan.term == ' 36 months']

# Modify earliest_cr_line field to reflect days since opening, relative to loan application
loan['earliest_cr_line'] = loan.apply(lambda x: (x['issue_d'] - x['earliest_cr_line']).days, axis=1)

# Restrict analysis to loans that met the credit policy
loan = loan[(loan.loan_status == 'Fully Paid') | (loan.loan_status == 'Charged Off')]


# restrict loan to income under $1,000,000
loan = loan[loan.annual_inc < 1000000]

loan['ln_annual_inc'] = np.log(loan.annual_inc)

loan = loan[loan.revol_util < 150]
loan['ln_revol_bal'] = np.log(loan.revol_bal+1)

loan['ln_earliest_cr_line'] = np.log(loan.earliest_cr_line)

loan['ln_open_acc'] = np.log(loan.open_acc)

loan.rename(columns = {'delinq_2yrs': 'num_delinq_2yrs'}, inplace=True)
loan['delinq_2yrs'] = (loan['num_delinq_2yrs'] >= 1)

loan.rename(columns = {'pub_rec': 'num_pub_rec'}, inplace=True)
loan['pub_rec'] = (loan['num_pub_rec'] >= 1)

loan.rename(columns = {'inq_last_6mths': 'num_inq_last_6mths'}, inplace=True)
loan['inq_last_6mths'] = (loan['num_inq_last_6mths'] >= 1)

col_list = ['loan_amnt', 'int_rate', 'ln_annual_inc', 'dti', 'fico_range_high', 'num_delinq_2yrs', 'ln_earliest_cr_line', 'num_inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record', 'ln_open_acc', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']

loan['target'] = loan['loan_status'] == 'Fully Paid'

loan = loan[(loan.issue_d < datetime.date(2015, 7, 1))]

y = loan['target']
X1 = loan[['loan_amnt', 'ln_annual_inc', 'dti', 'fico_range_high', 'delinq_2yrs', 'num_delinq_2yrs', 'ln_earliest_cr_line', 'inq_last_6mths', 'num_inq_last_6mths', 'ln_open_acc', 'pub_rec', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']]
X = pd.concat([X1, loan.int_rate, pd.get_dummies(loan.grade)], axis=1)

rf = ensemble.RandomForestClassifier(n_estimators=500, max_features=4, max_depth=10)
rf.fit(X, y)


pickle.dump(rf, open('rf.sav', 'wb'))





