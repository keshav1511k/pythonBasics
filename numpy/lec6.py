# Aggregate Functions = summarize data and typically return a single value.

import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))        # Sum of all elements.
print(np.mean(array))       # Mean of the array.
print(np.std(array))        # Standard Deviation.
print(np.var(array))        # Variance.
print(np.min(array))        # Minimum in array.
print(np.max(array))        # Maximum in array.
print(np.argmin(array))     # Minimum element index in array.
print(np.argmax(array))     # Maximum element index in array.

print(np.sum(array, axis = 0))   # For Column sum.
print(np.sum(array, axis = 1))   # For row sum.