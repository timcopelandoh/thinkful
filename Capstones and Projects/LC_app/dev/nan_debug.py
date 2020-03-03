import requests
import numpy as np
import pandas as pd
import datetime
import warnings

warnings.filterwarnings('ignore')

apikey = '9K1Hh5G3ekNC4QiOrtxNLK/YG/U='

header = {'Authorization': apikey, 'Content-Type': 'application/json'}
params = {'showAll': 'True'}

resp = requests.get('https://api.lendingclub.com/api/investor/v1/loans/listing', headers=header, params=params)

loans = resp.json()['loans']

loans = pd.DataFrame.from_dict(loans)

modelinput = loans[['loanAmount', 'annualInc', 'dti', 'ficoRangeHigh', 'delinq2Yrs', 
'earliestCrLine', 'inqLast6Mths', 'openAcc', 'pubRec', 'revolBal', 'revolUtil', 'totalAcc']]

modelinput['lnAnnualInc'] = np.log(modelinput.annualInc+1)
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

import statsmodels.api as sm

logit = sm.load('fitted_logit.pickle')

loans['predict'] = logit.predict(modelinput.astype(float))
loans['predict_str'] = loans.apply(lambda x: str(round(x['predict']*100,1))+'%', axis=1)

def total_int_paid(n, i):
    ii = i/12
    return n*(ii * (1 + ii) ** n) / ((1+ii)**n - 1)-1

loans['total_int_paid'] = loans.apply(lambda x: total_int_paid(36, x['intRate']/100), axis=1)


loans['EV'] = (loans['predict'] * loans['total_int_paid'] - .37 * (1 - loans['predict'])) * 100
loans['EV_str'] = loans['EV'].apply(lambda x: str(round(x, 1)) + '%')

disp = loans[loans.term == 36][['id', 'loanAmount', 'term', 'intRate', 'grade', 'predict_str', 'EV_str']]

disp = disp.sort_values(by=['grade', 'predict_str'], ascending=[1,0])

#for l in range(modelinput.shape[0]//2):
	#print(modelinput.iloc[[l*2,l*2+1],:])

print(modelinput.isna().sum())









