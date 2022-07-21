
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
df = df.drop_duplicates()
best_selling = df.loc[:, "Global_Sales"] > 1.0
df.loc[best_selling, "Successful"] = 1
df.loc[~best_selling, "Successful"] = 0
obj_features = ['Name', 'Platform', 'Genre' , 'Publisher', 'Developer', 'Rating', 'User_Score']
num_features = list(set(df.columns) - set(obj_features))

for f in num_features:
  df[f] = np.where(df[f] < 0, np.NaN , df[f])

for f in num_features:
  nulls = df[f].isnull().sum()
  if (nulls < 5000):
    median=df[f].median()
    df[f].fillna(value=median, inplace=True)

for f in obj_features:
  nulls = df[f].isnull().sum()
  if (nulls < 5000):
    mode=df[f].mode()[0]
    df[f].fillna(value=mode, inplace=True)

df = df.dropna(axis=0)
df = df.astype({'User_Score':float})

y = df[['Successful']].values
X = df.drop(columns=['Successful', 'Name', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release'])

def label_encode_columns(df, columns):
    for col in columns:
        le = LabelEncoder().fit(df[col])
        df[col] = le.transform(df[col])
    return df

X = label_encode_columns(X,  ['Platform', 'Genre', 'Publisher', 'Developer', 'Rating'])
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model_rf = RandomForestClassifier(n_estimators=100)
model_rf.fit(X_train, y_train)
train_predict_rf1 = model_rf.predict(X_test)