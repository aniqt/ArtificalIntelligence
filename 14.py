#Numpy Array to Pandas Series
import numpy as np
import pandas as pd
a=np.array([1,2,3,4])
print(a)
print(type(a))
b=pd.Series(a)
print(b)
print(type(b))