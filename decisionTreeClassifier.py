import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data={
    "hrs_studied":[1,2,3,4,5],
    "passed":[0,0,1,1,1]
}
df=pd.DataFrame(data)
X=df[['hrs_studied']]
y=df['passed']
model=DecisionTreeClassifier()
model.fit(X,y)
print(model.predict([[2]]))
print(model.predict([[10]]))