import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

np.set_printoptions(suppress=True)

lc = pd.read_csv('lendingclub.csv', header=1, low_memory=False)

#print(lc.shape)

#for i in range(lc.shape[1]):
	#print('Column {}: \t{}'.format(i, lc.columns[i]))


lc['own_home'] = pd.get_dummies((lc['home_ownership'] == 'OWN'), drop_first=True)

lc_reg = lc[['fico_range_low', 'dti', 'annual_inc', 'own_home', 'mths_since_last_delinq', 'open_acc', 'delinq_2yrs', 'revol_bal', 'total_acc']].dropna()
'''
Y = lc_reg['fico_range_low']
X = lc_reg[['dti', 'annual_inc', 'own_home', 'mths_since_last_delinq', 'open_acc', 'delinq_2yrs', 'revol_bal', 'total_acc']]

lrm = linear_model.LinearRegression()

lrm.fit(X, Y)

print('---------- Coefficients ----------')
print(lrm.coef_)
print('----------- Intercept ------------')
print(lrm.intercept_)'''

sns.distplot(lc_reg['mths_since_last_delinq'])
plt.show()ß
