# module = a file containig the code you want to include in your program 
#          use import to include a module (built-in or your own) useful
#          to break up a large program reusable seperate files

# #. example-1
import math
print(math.pi)

# # example-2
import math as m
print(m.pi)

# example - 3 (import external module) build own module

import example

result = example.pi
result = example.square(3)
result = example.cube(2)
result = example.circumference(4)
result = example.area(3)

print(result)