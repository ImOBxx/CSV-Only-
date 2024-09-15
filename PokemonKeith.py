import numpy as np
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.head())

#Prints Columns
#print(df.columns)

#print(df[['Name', 'Type 1', 'HP']])

#print(df.head(4))

#print(df.iloc[0:4])
#for index, row in df.iterrows():
#    print(index, row)
print(df.loc[df['Type 1'] == "Fire"])

#print(df.iloc[2, 1])

print(df.describe())

print(df.sort_values(['Type', 'HP'], ascending = [1.0]))

df.head(5)







