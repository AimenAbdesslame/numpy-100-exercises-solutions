import numpy as np 

arr = np.random.randint(0,10,size=(5,5))

print(arr)
array = (arr - np.mean(arr)) / (np.std(arr))

print(array)

