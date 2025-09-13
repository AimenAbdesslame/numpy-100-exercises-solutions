#9. Create a 3x3 matrix with values ranging from 0 to 8 

import numpy as np 

#usntin random and randint function to create the matrix (but values with this solution will be randomly generated not aranged from 0 to 8)
array = np.random.randint(0 , 9 , size = (3 ,3))
print(array)

#using arange and reshape funcitons : 
array2 = np.arange(0,9).reshape(3,3)
print(array2)