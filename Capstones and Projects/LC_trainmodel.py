import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import datetime
import warnings

warnings.filterwarnings('ignore')


# load dataset
loan = pd.read_csv('accepted_2007_to_2018Q4.csv')

# convert date to datetime.date
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

def convert_date(d):
    try:
        return datetime.date(year=int(d[4:]), month=return_number[d[:3]], day=1)
    except:
        pass

# convert 'issue date' and 'earliest credit line' fields to datetime.date format
loan['issue_d'] = loan['issue_d'].apply(convert_date)
loan['earliest_cr_line'] = loan['earliest_cr_line'].apply(convert_date)

# we restrict our analysis to loans from January 2010 to July 2015
loan = loan[loan.issue_d < datetime.date(2015,7,1)]
loan = loan[loan.issue_d >= datetime.date(2010,1,1)]

# 36 month loans are paid back considerably more often, and we can use more recent data if 
# we restrict ourselves to studying 36 month loans (as opposed to 60 month loans)
loan = loan[loan.term == ' 36 months']

# convert earliest credit line field to a difference in days between that and the issue date
loan['earliest_cr_line'] = loan.apply(lambda x: (x['issue_d'] - x['earliest_cr_line']).days, axis=1)

# restrict to loans that met LC's credit policy and for which we know the outcome
loan = loan[(loan.loan_status == 'Fully Paid') | (loan.loan_status == 'Charged Off')]

# incomes above $1million are suspicious and are likely errors
loan = loan[loan.annual_inc < 1000000]

# convert income to log income
loan['ln_annual_inc'] = np.log(loan.annual_inc)

# revolving utilization is a percentage, so values over 150% should be removed
loan = loan[loan.revol_util < 150]
loan['ln_revol_bal'] = np.log(loan.revol_bal+1)

# convert time since credit origination to log value
loan['ln_earliest_cr_line'] = np.log(loan.earliest_cr_line)

# same for number of open accounts
loan['ln_open_acc'] = np.log(loan.open_acc)

# for the following variables, create dummy variables when data equals 0, and rename 
# variables for ease of interpretability
loan.rename(columns = {'delinq_2yrs': 'num_delinq_2yrs'}, inplace=True)
loan['delinq_2yrs'] = (loan['num_delinq_2yrs'] >= 1)

loan.rename(columns = {'pub_rec': 'num_pub_rec'}, inplace=True)
loan['pub_rec'] = (loan['num_pub_rec'] >= 1)

loan.rename(columns = {'inq_last_6mths': 'num_inq_last_6mths'}, inplace=True)
loan['inq_last_6mths'] = (loan['num_inq_last_6mths'] >= 1)

# dummy target variable
loan['target'] = (loan['loan_status'] == 'Fully Paid')

# list of variables of interest
col_list = ['loan_amnt', 'int_rate', 'ln_annual_inc', 'dti', 'fico_range_high', 'num_delinq_2yrs', 'ln_earliest_cr_line', 'num_inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record', 'ln_open_acc', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']

# save data from 2014-2015 for backtesting
train = loan[loan.issue_d < datetime.date(2014, 1, 1)]

#train logit model
y = train['target']
X1 = train[['loan_amnt', 'ln_annual_inc', 'dti', 'fico_range_high', 'delinq_2yrs', 'num_delinq_2yrs', 'ln_earliest_cr_line', 'inq_last_6mths', 'num_inq_last_6mths', 'ln_open_acc', 'pub_rec', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']]
logit =  sm.Probit(y, X1.astype(float)).fit()

# save model for more efficient use
logit.save('fitted_logit.pickle')

# save 5 observations for test use in GUI and display code
live = loan.iloc[:30, :]
live.to_csv('live.csv')