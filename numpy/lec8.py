# # Random numbers

import numpy as np

rng = np.random.default_rng(seed = 1) # seed is used to reproduce the same result.

print(rng.integers(low=1, high=101, size=(3,2)))

# # Floating Numbers 

import numpy as np 
np.random.seed(seed = 1)
print(np.random.uniform(low=1, high=5, size=(3,2)))

# # Shuffle Array

import numpy as np
rng = np.random.default_rng()

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# For random chice we use rng object 

import numpy as np 
rng = np.random.default_rng()

fruits = np.array(["🍎","🍌","🥥","🍍","🍊"])
fruits = rng.choice(fruits, size = (3,3))
print(fruits)