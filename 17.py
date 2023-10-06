import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plotting lne chart

x = np.linspace(0,10,100) #(start,stop,number)
print(x)
plt.plot(x,x,label='linear',color='b')
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("First Plot")
plt.show()