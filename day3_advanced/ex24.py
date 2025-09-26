#23. Create a custom dtype that describes a color as four unsigned bytes

import numpy as np 


arr1 = np.random.randint(0,10,size=(5,3))
arr2 = np.random.randint(0,10,size=(3,2))

print("array1 :\n",arr1)
print("array2 :\n",arr2)
result_arr = arr1.dot(arr2)
print(result_arr)



# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
