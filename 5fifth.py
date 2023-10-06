#Converting Numpy array to numpy matrix
import numpy as np
a=np.array([1,2,3,4])
b=np.mat(a)
print(type(a))
print(type(b))
print(b)
print(b.shape)