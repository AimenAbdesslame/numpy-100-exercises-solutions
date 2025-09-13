

import numpy as np 
# Find indices of non-zero elements from [1,2,0,0,4,0]

array = np.array([1,2,0,0,4,0])
arr = np.where(array != 0)
print(arr[0])