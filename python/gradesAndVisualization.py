
import numpy as np
import matplotlib.pyplot as plt

def parabola(a,b):
    x = np.linspace(-5, 5, 100)
    y = (a * x**2) + b
    plt.plot(x,y)
    plt.show()
    
parabola(2,3)
    
def parabolabis(a,b):
    x = np.linspace(-5, 5, 100)
    y = (a * x**2) + b
    plt.plot(x,y)
    
plt.subplot(2,2,1)
# Write here the code for the first chart
parabolabis(2,3)

plt.subplot(2,2,2)
# Write here the code for the second chart
parabolabis(1, 4)

plt.subplot(2,2,3)
# Write here the code for the third chart
parabolabis(-2, 7)

plt.subplot(2,2,4)
# Write here the code for the fourth chart
parabolabis(0, 0) 
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('grades.csv', encoding = "ISO-8859-1")

# df = pd.read_csv('grades.csv')
# print(df)

print(df.head())
print(df.tail())
print(df.describe())
print(df.dtypes)

df2 = df.iloc[:,[2,3]]
print(df2)

df2.T

print((df2.head()).T)

df2 = df2.sort_values(by= "TP3")
print(df2.tail())

plt.subplot(2, 1, 1)
df.boxplot(column = "TD1")
plt.subplot(2, 1, 2)
df.boxplot(column = "DS1")

plt.show()