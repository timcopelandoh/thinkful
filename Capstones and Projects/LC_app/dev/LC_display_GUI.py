import pandas as pd
import statsmodels.api as sm

gui=False
# import data: 'live.csv' is a csv with 5 lines of data for testing
live = pd.read_csv('live.csv')

# create DF for data that needs to be fed into the model
live_input = live[['loan_amnt', 'ln_annual_inc', 'dti', 'fico_range_high', 'delinq_2yrs', 
'num_delinq_2yrs', 'ln_earliest_cr_line', 'inq_last_6mths', 'num_inq_last_6mths', 
'ln_open_acc', 'pub_rec', 'num_pub_rec', 'ln_revol_bal', 'revol_util', 'total_acc']]

# load trained model
logit = sm.load('fitted_logit.pickle')

# create column for predicted values and the same value 
# in a readable string format
live['predict'] = logit.predict(live_input.astype(float))
live['predict_str'] = live.apply(lambda x: str(round(x['predict']*100,1))+'%', axis=1)

# create DF of data we want to display
disp = live[['id', 'issue_d', 'loan_amnt', 'term', 'int_rate', 'grade', 'predict_str']]

# sort display dataframe and print to console
disp = disp.sort_values(by = ['grade', 'predict_str'], ascending = [1,0])
#

from pandasgui import show


if gui:
	if __name__ == '__main__':
		show(disp)
else:
	print(disp)

