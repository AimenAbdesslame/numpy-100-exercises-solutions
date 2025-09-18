#"s 15 
#Create a 2d array with 1 on the border and 0 inside

import numpy as np


x = np.zeros((5,5))

for i in range(len(x)) : 
    for j in range(len(x)) :
        if ((i == 0) or (i == len(x)-1) or ( j==0 ) or ( j== len(x)-1 )): 
            x[i,j] = 1

print(x) 


#numpy optimized solution : 
z = np.ones((5,5))
z[1:-1,1:-1] = 0
print(z)
