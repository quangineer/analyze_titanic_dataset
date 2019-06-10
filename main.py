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


# Whether the fare is associated with Survival???
survived = df_train.Survived == True
died = df_train.Survived == False
# Divived the Survived column into 2 groups
(df_train["Survived"][survived].count())   # print 340
(df_train["Survived"][died].count())       # print 549
(df_train.Fare[survived].mean())    # print 48.2094
(df_train.Fare[died].mean())        # print 22.1178

# df_train.Fare[survived].hist(alpha=0.5, bins=20, label='survived')
df_train.Fare[died].hist(alpha=0.5, bins=20, label='died')
plt.show()

# Whether the fare is associated with class?
print(df_train.groupby("Pclass").Survived.mean())

# Distribution of Age between Survival and Died?
df_train.Age[survived].hist(alpha=0.5, bins=20, label='survived')
df_train.Age[died].hist(alpha=0.5, bins=20, label='died')
# plt.show()

# Gender associated with Survival/Died?
print(df_train.groupby("Sex").Survived.mean())
# Further investigate in Gender:
df_train["Sex"].value_counts()    # How many in each gender?
df_train.groupby("Sex")["Pclass"].value_counts()
df_train.query('Sex=="female"')["Fare"].median()   # 23
df_train.query('Sex=="male"')["Fare"].median()     # 10.5
df_train.groupby(["Pclass","Sex"]).Survived.mean().plot(kind='bar')
# plt.show() # Women in each fare class survived more than men

print (df_train["SibSp"][survived].value_counts())
print (df_train["SibSp"][died].value_counts())

df_train["SibSp"][survived].value_counts().plot(kind="bar", alpha=0.5, color="blue", label="survived")
df_train["SibSp"][died].value_counts().plot(kind="bar", alpha=0.5, color="orange", label="died")
plt.show()

df_train["Embarked"][survived].value_counts().plot(kind="bar", alpha=0.5, color="blue", label="survived")
df_train["Embarked"][died].value_counts().plot(kind="bar", alpha=0.5, color="orange", label="died")
plt.show()