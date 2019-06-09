import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# df_test = pd.read_csv("test.csv")
# print (list(df_test.columns))

df_train = pd.read_csv("train.csv")
# print (list(df_train.columns))

# print (df_train.head())
# print (df_train.shape)
# print (df_train.describe())

# Wrangling:
df_train.drop(["PassengerId","Name","Cabin","Ticket"], axis=1, inplace=True)

# print (df_train[df_train["Age"].isnull()])
# (df_train[df_train["Age"].isnull()]).hist(bins=3)

# There are 177 rows with Nal value in Age. So just fill it with Nal value
df_train.fillna(df_train.mean(),inplace=True)
(df_train[df_train["Embarked"].isnull()]) # There are 2 rows with Nal value in Embarked. We drop them
df_train.dropna(inplace=True) # dropna = drop all row with Nal value in anywhere


