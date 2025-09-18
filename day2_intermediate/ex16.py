#ex 16 
#16. How to add a border (filled with 0's) around an existing array?

import numpy as np 

# arr is a given array 

arr = np.random.randint(0,5,size=(3,3))# generating a random 3x3 array
print("original array")
print(arr)  

arr = np.pad(arr , pad_width=1)#adding a border of width one (1) of 0's around the array
print("array after adding border of 0's")
print(arr)
