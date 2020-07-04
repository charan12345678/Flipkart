import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 
import re 

df = pd.read_csv(r"C:\Users\charan\Desktop\Flipkart\Flipkart.csv")
df['New_back_camera'] = df['New_back_camera'].astype(float)
df['Ram'] = df['Ram'].astype(float)
df['battery'] = df['battery'].astype(float)
df['Internal_storage'] = df['Internal_storage'].astype(float)
df['display'] = df['display'].astype(float)
df['rating'] = df['rating'].astype(float)
df['no_of_ratings'] = df['no_of_ratings'].astype(float)
df['price'] = df['price'].astype(float)
df.drop('Unnamed: 0',axis=1,inplace = True)
df.dropna(how='any',axis=0,inplace = True)
df.drop(['no_of_ratings','no_of_reviews'],axis=1,inplace=True)
print(df)
df.to_csv("New_Flipkart.csv")



