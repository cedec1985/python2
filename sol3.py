import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score #model evaluation
df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
model.fit(X,y)
y_pred=model.predict(X)
print("accuracy",accuracy_score(y,y_pred))
print("precision",precision_score(y,y_pred))
print("recall",recall_score(y,y_pred))
print("score",f1_score(y,y_pred))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,y_pred))
from sklearn.model_selection import train_test_split
df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
X_train,X_test,y_train,y_test= train_test_split(X,y)
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
y_pred=model.predict(X_test)
print("accuracy",accuracy_score(y_test,y_pred))
print("precision",precision_score(y_test,y_pred))
print("recall",recall_score(y_test,y_pred))
print("score",f1_score(y_test,y_pred))
X=[1,1],[2,2],[3,3],[4,4] #random test
y=[0,0,1,1]
print("X_train",X_train)
print('y_train', y_train)
#logistic regression treshold, sensitivyn specificity, ROC curve


from sklearn.metrics import precision_recall_fscore_support
sensitivity_score=recall_score
def specificity_score(y_true,y_pred):
    p,r,f,s= precision_recall_fscore_support(y_true,y_pred)
    return r[0]
df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y=df['Survived'].values
model= LogisticRegression()
X_train,X_test,y_train,y_test= train_test_split(X,y)
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
y_pred=model.predict(X_test)
print("sensitivity:",sensitivity_score(y_test,y_pred))
print("specificity:",specificity_score(y_test,y_pred))

#adjusting with proba
model.predict_proba(X_test)[:,1]>0.75
print("model proba:")
print(model.predict_proba(X_test))
print("precision",precision_score(y_test,y_pred))
print("recall",recall_score(y_test,y_pred))