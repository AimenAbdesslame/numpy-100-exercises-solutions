#Exercise 14. How to extract all numbers between a given range from a numpy array?
# Question: Get all items between 5 and 10 from a.

# Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output: (array([6, 9, 10]),)
import numpy as np  
a = np.array([2, 6, 1, 9, 10, 3, 27])
print("Original array:")
print(a)

a = a[(a>=5) & (a<=10)]
print("\nItems between 5 and 10:")
print(a)