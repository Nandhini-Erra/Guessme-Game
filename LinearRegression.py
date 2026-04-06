import pandas as pd
from sklearn.linear_model import LinearRegression
data={
    "Size":[1000,1500,2000],
    "Bedrooms":[2,3,4],  
    "Price":[50,75,100]
}
df=pd.DataFrame(data)
X=df[['Size']]
y=df['Price']
model=LinearRegression()
model.fit(X,y)
print("price of the 1800 sqft house is:",model.predict([[1800]]))