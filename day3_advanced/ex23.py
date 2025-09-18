# What Are Custom Dtypes in NumPy?
#A dtype (data type) in NumPy specifies the type and size of an array’s elements. Built-in dtypes include np.int32, np.float64, and np.str_. Custom dtypes extend this by allowing you to define complex, user-specified types
#Why Use Custom Dtypes : 
#Handling Complex Data ,Memory Efficiency , Improved Readability , Improved Readability

# for mor details read : https://www.sparkcodehub.com/numpy/advanced/custom-dtypes



import numpy as np

colors = np.dtype ([
    ('r' , np.ubyte,1) , 
    ('g' , np.ubyte,1) , 
    ('b' , np.ubyte,1) , 
    ('a' , np.ubyte,1) , 
])


#testing : 
arr = np.array ([(10,20,56,32),(230 , 10 , 50 , 0)] , dtype = colors )
print (arr['r'])
print (arr['g'])
print (arr['b'])
print (arr['a'])
