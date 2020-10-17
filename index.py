import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


wine_dict={'red wine':[3,6,5],'white wine':[5,0,10]}
sales=pd.DataFrame(wine_dict,index=["adam","bob","charles"])
print(sales['white wine'])
presidents_df=pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv',index_col='name')
print(presidents_df.shape)
print(presidents_df.head(n=5))
print(presidents_df.tail())
print(presidents_df.info())
print(presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant'])
print(presidents_df.iloc[15:18])
print(presidents_df['height'])
print(presidents_df['height'].shape)
print(presidents_df.loc[:,'order':'height'].head(n=3))
print(presidents_df.mean())
print(presidents_df['age'].quantile([0.25,0.5,0.75,1]))
print(presidents_df['age'].median())
dat=pd.Series([2,3,4])
print(dat.var())
print(dat.std())
print(presidents_df['age'].var())
print(presidents_df['age'].std())
print(presidents_df.describe())
print(presidents_df.groupby('party').mean())
print(presidents_df.groupby('party')['height'].agg(['min',np.median,max]))
x=np.linspace(0,10,1000)
fig=plt.figure()
ax=plt.axes()
ax.plot(x,np.sin(x))
ax.plot(x,np.cos(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title('function sin(x)')
plt.plot(x,np.sin(x),'k:',label='sin(x)')
plt.plot(x,np.cos(x),'r--',linestyle='--',label='cos(x)')
plt.legend()
plt.show()
plt.scatter(presidents_df['height'],presidents_df['age'],marker='>',color='b')
plt.xlabel('height')
plt.ylabel('age')
plt.title('U.S. presidents')
plt.show()
presidents_df.plot(kind='scatter',x='age',y='height',title='us presidents')
plt.show()
presidents_df['height'].plot(kind='hist',title='height',bins=5)
plt.show()
presidents_df.boxplot(column='height')
plt.show()
party_cnt=presidents_df['party'].value_counts()
plt.style.use('ggplot')
party_cnt.plot(kind='bar')
plt.show()
plt.style.use('ggplot')
fig=plt.figure()
ax=plt.axes()
plt.show()
#scikit learn
boston_dataset=load_boston()
boston=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston['MEDV']=boston_dataset.target
plt.show()
print(boston.columns)
print(boston.describe().round(2))
print(boston.hist(column='CHAS',bins=20))
plt.show()
corr_matrix=boston.corr().round(2)
print(corr_matrix)
boston.plot(kind='scatter',x='RM',y='MEDV',figsize=(8,6));
plt.show()
model=LinearRegression()
X=boston[['RM']]
Y=boston[['MEDV']]
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
print(X_train.shape)
try:
    model.fit(X_train,Y_train)
except:
    ValueError
finally:
    print(model.fit(X,Y))
print(model.intercept_.round(2))
print(model.coef_.round(2))

new_RM=np.array([6.5]).reshape(-1,1)
print(model.predict(new_RM))
print(model.intercept_+model.coef_*6.5)
plt.scatter(X_test,Y_test,label='testing data')
y_test_predicted=model.predict(X_test)
plt.plot(X_test,y_test_predicted,label='prediction', linewidth=3)
plt.xlabel('RM');plt.ylabel('MEDV')
plt.legend(loc='upper left')
plt.show()