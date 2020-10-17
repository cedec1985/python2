import pandas as pd

df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
print(X)
print(y)
from sklearn.linear_model import LogisticRegression  # using sklearn

df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
X=df[['Age','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
model.fit(X,y)
print(model.coef_, model.intercept_)
model.predict(X)
print(model.predict(X[:5]))

df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
model.fit(X,y)
print(model.predict([[3,True,22.0,1,0,7.25]]))
print(model.predict(X[:5]))
print(y[:5])

y_pred=model.predict(X)
y==y_pred
print((y==y_pred).sum())
print((y==y_pred).sum()/y.shape[0])#accuracy of the model
print(model.score(X,y))
from sklearn.datasets import load_breast_cancer

cancer_data=load_breast_cancer()
print(cancer_data.keys())
print(cancer_data['DESCR'])
print(cancer_data['data'].shape)
print(cancer_data['feature_names'])
df=pd.DataFrame(cancer_data['data'],#dataframe
columns=cancer_data['feature_names'])
print(df.head())
print(cancer_data['target'])
print(cancer_data['target'].shape)
print(cancer_data['target_names'])
df['target']=cancer_data['target']#pandas dataframe
print(df.head())
X=df[cancer_data.feature_names].values
y=df['target'].values
model=LogisticRegression(solver='liblinear',max_iter=100)
model.fit(X,y)
model.fit(X,y)
print(model.predict([X[0]]))
print(model.score(X,y))

df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
model.fit(X,y)
y_pred=model.predict(X)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
