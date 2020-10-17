import numpy as np 
import matplotlib as plt
import pandas as pd

data=[15,16,18,19,25,28,17,23]
print("mean",np.mean(data))
print("median",np.median(data))
print("percentile 50(median)",np.percentile(data,50))
print("standard deviation", np.std(data))
print("variance", np.var(data))


df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
pd.options.display.max_columns=6
print(df.head())
print(df.describe())
col=df['Fare']
print(col)
df['male']=df['Sex']=='male'
print(df.head())



