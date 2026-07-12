# Multidimensional Arrays


import numpy as np

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['A','Z','Y'],['X','W','V'],['U','T','S']]])
print(array.ndim)
print(array.shape)

print(array[0][0][0])      # this is called chain indexing which is usually used in python to access the elements.

# multidimensional indexing which is faster than chain indexing 

print(array[0,0,0])

word = array[0,0,0] + array[0,1,2]

print(word)