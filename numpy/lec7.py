# Filtering = Refers to the process of selecting elements from an array that match a given condition.

import numpy as np 

ages = np.array([[21,17,19,20,16,30,18,65],
                 [22,23,24,25,34,54,41,99]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(odds)

# Filtering by Replacing 

# syntax:- new_array_name = np.where(condition, old_array_name, replace_with).  It will preserve the shape also.

adults = np.where(ages >= 18, ages, 0)
print(adults)