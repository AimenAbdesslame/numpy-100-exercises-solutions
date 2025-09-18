#21. Create a checkerboard 8x8 matrix using the tile function 

import numpy as np 


arr = np.array([0,1,1,0]).reshape(2,2)

print("the init array : \n" , arr )

repetitions = ( 4 , 4 )
print("checkboard : \n " , np.tile(arr , repetitions))
