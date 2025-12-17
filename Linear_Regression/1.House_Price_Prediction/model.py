import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df=pd.read_csv('house.csv')
X=df[['area']]
y=df['price']

model=LinearRegression()
model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))