import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 
import re 

df2 = pd.read_csv(r"C:\Users\charan\Desktop\Flipkart\scrapeflipkart\New_Flipkart.csv")
df2.drop(['product_name'],axis=1,inplace=True)
print(df2.head())
x = df2.iloc[:, :-1]
y = df2.iloc[:, -1] 
print(x)
print(y)

from sklearn.model_selection import train_test_split
X_train ,X_test ,Y_train,Y_test = train_test_split(x,y, test_size = 0.2,random_state = 2)
print(X_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 18 , random_state=2)
regressor.fit(X_train,Y_train)

y_pred = regressor.predict((X_test))
y_pred

from sklearn.metrics import r2_score
score=r2_score(Y_test,y_pred)

print(score)

