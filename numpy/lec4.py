# Arithmetic
import numpy as np

# Scalar Arithmetic

array = np.array([1,2,3,4])

print(array + 1)     #Add
print(array - 2)     #Substract
print(array * 3)     #Multiply
print(array / 4)     #Divide
print(array ** 5)    #Power

# Vectorized Math Functions

array = np.array([1.01,2.02,3.03,4.04])

print(np.sqrt(array))
print(np.round(array))
print(np.pi)

# Exercise 

import numpy as np

radii = np.array([1,2,3,4])
print(np.pi * radii ** 2)

# Element wise Array

import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparision Operator

import numpy as np

scores = np.array([91,55,100,73,82,64])
 
print(scores == 100)  # It will return a boolean array
print(scores < 60)
scores[scores < 60 ] = 0   # Assigning 0 to all the values that are less than 60 in the array
print(scores)