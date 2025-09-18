import numpy as np 

Z = np.zeros((5,5))

Z = np.diag(1+np.arange(4),k=-1)
print(Z)
