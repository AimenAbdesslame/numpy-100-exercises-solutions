#Exercise 12. How to remove from one array those items that exist in another?

# Qst : Fom array A remove all items present in array B 

#ex : 

#INPUT : A = np.array([1,2,5,7,8,6])
#        B = np.array([1,6,8,,10,11,15])
#OUTPUT : array([2,5,7])

import numpy as np 

a = np.random.randint(10 , size= 5)
b = np.random.randint(10 , size= 5)

## printing the original a array : 
print("this is the original a : " , a)

## printing the original b array : 
print("this is the original b : " , b)


#Removing all items in a showing in b : 
result = np.array([], dtype=int) # make sure that type of this array is int because we are going to store index of a array in it and by default numpy makees it is float

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            result = np.append(result , i)

a = np.delete(a , result)# np.delete function removes the index given in the second argument from the array given the first argument and retruns the new array (we store it in old a array) 
print("Result : " , a)



## In clean way using numpy built in function : 
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4])

result = a[~np.isin(a, b)]
print("Result:", result)
# [1 3 5]
