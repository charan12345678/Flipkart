import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy 
import sklearn
import seaborn as sns 
import re 

dataset = pd.read_csv(r"C:\Users\charan\Desktop\Flipkart\scrapeflipkart\item.csv")
print(dataset.head())
dataset['New_battery'] = dataset['battery']
dataset['New_battery'] = dataset['New_battery'].astype(str)
for i in range(0,513):
    dataset['battery'][i] = re.findall("[0-9]{4}",dataset['New_battery'][i])
    i= i+1
print(dataset['battery'].head()) 
dataset['New_display'] = dataset['display'] 
dataset['New_display'] = dataset['New_display'].astype(str)
for i in range(0,513):
    dataset['display'][i] = re.findall(r"\(([^)]+)", dataset['New_display'][i])
    i=i+1
print(dataset['display'].head())
dataset['display'] = dataset['display'].astype(str)
for i in range(0,513):
    dataset['display'][i]= re.findall(r"\d*\.\d+|\d+",dataset['display'][i])
    i=i+1
print(dataset['display'].head())
dataset['no_of_ratings'] = dataset['no_of_ratings'].astype(str)
dataset['no_of_ratings'] = dataset['no_of_ratings'].str.replace(',','')
dataset['no_of_ratings'] = dataset['no_of_ratings'].str.replace(' ','')
for i in range(0,513):
    dataset['no_of_ratings'][i] = re.findall(r"\d+",dataset['no_of_ratings'][i])
    i=i+1
print(dataset['no_of_ratings'].head())
dataset['no_of_reviews'] = dataset['no_of_reviews'].astype(str)
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.replace(',','')
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.replace(' ','')
for i in range(0,513):
    dataset['no_of_reviews'][i] = re.findall(r"\d+",dataset['no_of_reviews'][i])
    i=i+1
print(dataset['no_of_reviews'].head())
dataset['price']= dataset['price'].str.strip('₹')
dataset['price']= dataset['price'].str.replace(',','')
dataset['price']= dataset['price'].str.replace(' ','')
print(dataset['price'].head()) 

new_list =dataset['ram'].str.split("|",n=1,expand=True)
dataset['Ram']=new_list[0]
dataset['Rom']=new_list[1]
dataset.drop(columns=["ram"],inplace=True)

my_list = dataset['Rom'].str.split("|",n=1,expand=True)
dataset['Internal_storage'] = my_list[0]
dataset.drop(columns=["Rom"],inplace=True)

my_list2 = dataset['camera'].str.split("|",n=1,expand=True)
dataset['back_camera'] = my_list2[0]
dataset['front_camera'] = my_list2[1]
print(dataset.head())

dataset['front_camera'] = dataset['front_camera'].astype(str)
for i in range(0,513):
    dataset['front_camera'][i] = re.findall(r"\d+",dataset['front_camera'][i])
    i=i+1

dataset['back_camera'] = dataset['back_camera'].astype(str)
for i in range(0,513):
    dataset['back_camera'][i] = re.findall(r"\d+",dataset['back_camera'][i])
    i= i+1
new_list2 = dataset['back_camera']
dataset['New_back_camera'] = new_list2
for i in range(0,513):
    dataset['New_back_camera'][i] = new_list2[i][0]
    i=i+1
 
print(dataset['New_back_camera'].head())
dataset.drop(['camera','back_camera','New_display','front_camera','New_battery'],axis=1,inplace=True)
dataset['battery'] = dataset['battery'].astype(str)
dataset['battery'] = dataset['battery'].str.replace('[','')
dataset['battery'] = dataset['battery'].str.replace(']','')
dataset['battery'] = dataset['battery'].str.strip('\'')

dataset['display'] = dataset['display'].astype(str)
dataset['display'] = dataset['display'].str.replace('[','')
dataset['display'] = dataset['display'].str.replace(']','')
dataset['display'] = dataset['display'].str.strip('\'')


dataset['no_of_ratings'] = dataset['no_of_ratings'].astype(str)
dataset['no_of_ratings'] = dataset['no_of_ratings'].str.replace('[','')
dataset['no_of_ratings'] = dataset['no_of_ratings'].str.replace(']','')
dataset['no_of_ratings'] = dataset['no_of_ratings'].str.strip('\'')


dataset['no_of_reviews'] = dataset['no_of_reviews'].astype(str)
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.replace('[','')
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.replace(']','')
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.replace(' ','')
dataset['no_of_reviews'] = dataset['no_of_reviews'].str.strip('\'')


for i in range(0,513):
    dataset['Ram'][i]= re.findall(r"\d*\.\d+|\d+",dataset['Ram'][i])
    i=i+1
dataset['Internal_storage'] = dataset['Internal_storage'].astype(str)
for i in range(0,513):
    dataset['Internal_storage'][i]= re.findall(r"\d*\.\d+|\d+",dataset['Internal_storage'][i])
    i=i+1

dataset['Ram'] = dataset['Ram'].astype(str)
dataset['Ram'] = dataset['Ram'].str.replace('[','')
dataset['Ram'] = dataset['Ram'].str.replace(']','')
dataset['Ram'] = dataset['Ram'].str.strip('\'')

dataset['Internal_storage'] = dataset['Internal_storage'].astype(str)
dataset['Internal_storage'] = dataset['Internal_storage'].str.replace('[','')
dataset['Internal_storage'] = dataset['Internal_storage'].str.replace(']','')
dataset['Internal_storage'] = dataset['Internal_storage'].str.strip('\'')


dataset['product_name'] = dataset['product_name'].astype(str)
for i in range(0,271):
    dataset['product_name'][i] = dataset['product_name'][i][0:10]
    i=i+1

dataset = dataset[['product_name','Ram','New_back_camera','battery','Internal_storage','display','rating','no_of_ratings','no_of_reviews','price']]

print(dataset)
dataset.to_csv("Flipkart2.csv")
