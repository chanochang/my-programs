# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:07:24 2023

@author: chano
"""

import pandas as pd
import matplotlib.pyplot as plt

file = 'C:/Users/chano/Documents/CS5007/Wk10/Activity/Miles_Per_Gallon.csv'
df = pd.read_csv(file)

df.info()

dis_df = df['displ']

# ax = dis_df.plot(kind = 'hist', title = 'Displacement Distribution', ylabel = 'Frequency', color = 'orange' ,  bins = 20)
# ax = df['displ'].plot.hist(title = 'Displacement Distribution', ylabel = 'Frequency', color = 'orange' ,  bins = 20 , legend = 'true')

df2 = df[df['year'] == 1993]

cyl = df2.value_counts("cylinders")

cyl.plot.pie(ylabel = 'cylinders', title = '1993 models');
