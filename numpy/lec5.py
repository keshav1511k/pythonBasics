# Broadcasting : It allows Numpy to perform operations on array with different shapes by virtually expanding dimensions so they match the larger array's shape.

# The dimensions have the same size.
# OR 
# One of the dimensions has a size of 1.

import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)  # This can only happen beacuse their dimensions are not of same size but one of them is 1.

array3 = np.array([[1,2,3,4],
                   [5,6,7,8]])
array4 = np.array([[1],[2],[3],[4]])

print(array3 * array4)  # Their is an error because of the dimensions as they are not same and none of them are 1.

array5 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
array6 = np.array([[1,2,3,4,5,6,7,8,9,10]])

print(array5 * array6)  # The shape of this virtually created array is 10*10.

# Broadcasting allows Numpy to perform operations on array with different shapes by virtually expanding their dimensions.