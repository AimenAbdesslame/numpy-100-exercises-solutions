
#25. Given a 1D array, negate all elements which are between 3 and 8, in place

import numpy as np 


arr = np.arange(13)
print('befor \n' , arr )
arr = np.where(((arr > 3) & (arr <= 8)) , arr * -1 , arr)

print ("After : \n",arr)



#other solution 
arr[(3 < arr) & (arr <= 8)] * -1
print (arr) 
