# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:09:17 2023

@author: Asus
"""

import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open(r'D:\My office\Udemy\Python and Tableau-The complete Data Analytics Bootcamp!\Project 2\loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open(r'D:\My office\Udemy\Python and Tableau-The complete Data Analytics Bootcamp!\Project 2\loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#fineing unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#Working with arrays

#1D array
arr = np.array([1, 2, 3, 4])

#0D array
arr = np.array(43)

#2D array 
arr = np.array([[1,2,3],[4,5,6]])

# using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >=600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

# for interest rates, a new column is wanted. rate >0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)
