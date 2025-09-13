##11. Create a 3x3 identity matrix 


import numpy as np 


ID = np.zeros((3,3))
for i in range(0,3):
    ID[i , i] = 1

print (ID)


# the fastest solutio is using numpy built in function identity : 
ID3 = np.identity(3)
print (ID3)