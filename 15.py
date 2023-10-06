#Pandas Dataframes
import numpy as np
import pandas as pd
v1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a=pd.DataFrame(v1,columns=list("ABC"))
print(a)