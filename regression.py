import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import cross_val_score, KFold

df = pd.read_csv('results.csv')

y = df['Interactivity']
# x = df[['Rotation average']]
# x = df[['Distance average']]
# x = df[['Rotation average', 'Distance average']]
# x = df[['S1Rot Avg', 'S2Rot Avg', 'S3Rot Avg']]
# x = df[['S1Rot Tot', 'S2Rot Tot', 'S3Rot Tot']]
# x = df[['S2Rot Tot', 'S4Rot Tot']]
x = df[['S2Rot Tot']]

#select variables to observe
# df = df.loc[:, ['S1Rot Avg', 'S2Rot Avg', 'S3Rot Avg', 'Interactivity']]
# df = df.loc[:, ['S2Rot Avg', 'S4Rot Avg', 'Interactivity']]
# df = df.loc[:, ['S1Rot Tot', 'S2Rot Tot', 'S3Rot Tot', 'Interactivity']]
df = df.loc[:, ['S2Rot Tot', 'Interactivity']]
# df = df.loc[:, ['Rotation average', 'Interactivity']]
# df = df.loc[:, ['Distance average', 'Interactivity']]

# sns.regplot(x="Rotation average", y="Interactivity", data=df, fit_reg=False)
# sns.regplot(x="Distance average", y="Interactivity", data=df, fit_reg=False)

# rescale variables
df_columns = df.columns
scaler = MinMaxScaler()
# scaler = StandardScaler()
df = scaler.fit_transform(df)

# rename columns
df = pd.DataFrame(df)
df.columns = df_columns

sns.regplot(x="S2Rot Tot", y="Interactivity", data=df, fit_reg=True)
# sns.regplot(x="Distance average", y="Interactivity", data=df, fit_reg=True)

# x = x.values.reshape(-1, 2)
x = x.values.reshape(-1, 1)
y = y.values.reshape(-1,1)

# print(df)

# print(y.shape)
# print(x.shape)

lr = LinearRegression()
model = lr.fit(x,y)
# print(model.coef_)
# print(model.intercept_)
print("r2 =", model.score(x,y))

folds = KFold(n_splits = 5, shuffle = True, random_state = 100)
scores = cross_val_score(lr, x, y, scoring = 'r2', cv = folds)
print(scores)