import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

data=[15,16,18,19,25,28,17,23]
print("mean",np.mean(data))
print("median",np.median(data))
print("percentile 50(median)",np.percentile(data,50))
print("standard deviation", np.std(data))
print("variance", np.var(data))

#using pandas
df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
pd.options.display.max_columns=6
print(df.head())
print(df.describe())
col=df['Fare']
print(col)
df['male']=df['Sex']=='male'
print(df.head())
#using numpy
df['Fare'].values
print(df['Fare'].values)
arr=df[['Fare','Sex','Pclass']].values
print(arr.shape)
print(arr[0])
print(arr[:,1])
mask=arr[:,2]<18
print(arr[mask])
print(arr[arr[:,2]<18])#without mask variable
print(mask.sum())
print((arr[:,2]<18).sum())
#using matplotlib
plt.scatter(df['Age'],df['Fare'],c=df['Pclass'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.plot([0,80],[85,5])
plt.show()





