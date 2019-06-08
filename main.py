import pandas as pd 


df_test = pd.read_csv("test.csv")


df_train = pd.read_csv("train.csv")


print (list(df_test.columns))
print (list(df_train.columns))