import pandas as pd

# help(round)

df = pd.read_csv('adult.data.csv')

# print(df.head())
print()
print(df.columns)
print()
print(df.describe())
print()
print(df.dtypes)
print()
print(df.shape)
print()
print(df.info)