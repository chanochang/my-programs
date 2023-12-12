# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:28:55 2023

@author: chano
"""

import pandas as pd
import matplotlib.pyplot as plt

readFile = 'carmpg.csv'
df = pd.read_csv(readFile)

print(df.dtypes)
df = df.dropna(how="any")

print(df[['mpg']].describe())

q_1 = df['mpg'].quantile(0.25)
q_3 = df['mpg'].quantile(0.75)
q_low = q_1 - 1.5*(q_3-q_1)
q_hi = q_3 + 1.5*(q_3-q_1)
df = df[(df['mpg'] < q_hi) & (df['mpg'] > q_low)]
print(df[['mpg']].describe())

x = df['modelyear']
y = df['mpg']
print(pd.crosstab(x, y))

x = df['origin']
y = df['mpg']
print(pd.crosstab(x, y))

x = df['horsepower']
y = df['mpg']
plt.figure()
plt.scatter(x, y, c = "green")  

  
x = df['weight']
y = df['mpg']
plt.figure()
plt.scatter(x, y,  c = "red")  


x = df['displacement']
y = df['mpg']
plt.figure()
plt.scatter(x, y)  

mpg = df[(df['origin']== 'USA')]

# 'mpg','cylinders','modelyear','name'
mpg = mpg.iloc[:,[0,1,4,5,6]]

mpg = mpg.dropna()

import statsmodels.api as sm

X = mpg[['cylinders','weight','acceleration','modelyear']]
Y = mpg[['mpg']]
X = sm.add_constant(X)

lsfit = sm.OLS(Y,X).fit()

print(lsfit.summary())
print(lsfit.mse_resid)

x = pd.DataFrame([[1, 4, 2720, 15.6, 78]])
prediction = lsfit.get_prediction(x)
print(prediction.summary_frame())
print('predicted mpg =' ,prediction.predicted_mean[0])
