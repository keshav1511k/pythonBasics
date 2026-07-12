# Slicing 
import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start : end : step]

# this is row selection

print(array[::-1])       #reverse
print(array[0:])         #print all
print(array[1:4])        #from 1 to 3
print(array[0:4:2])      #use step of 2

# column selection

print(array[:, 1])       #print column no-1 elements
print(array[:, 0:3])     #print from 0 to 2nd index column
print(array[:, ::-1])    #print reverse columns
print(array[:, ::2])     #print columns with a step of 2 i.e every 2nd column
print(array[0:2, 0:2])   #print first two rows and two columns elements i.e total 4 elements
