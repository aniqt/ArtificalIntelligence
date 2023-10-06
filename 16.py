#Create Dataset using numpy array

import numpy as np
import pandas as pd
df = pd.read_csv("annual.csv")
print(df)
print(df.head())
print(df.tail())
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.describe)
print(df.sort_values(by='Year',ascending=False))
print(df.T)