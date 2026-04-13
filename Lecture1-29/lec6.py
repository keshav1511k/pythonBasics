# Arithemetics and Maths
#operators

friends = 10
# friends += 1
# friends -= 1
# friends *= 2
# friends /= 2
# friends **= 2
remainder = friends % 2
print(remainder)


#other operations

x = 3.14
y = 4
z = 5
result = round(x)
result = abs(y)
result = pow(y, 2)
result = max(y, x, z)
result = min(y, x, z)
print(result)


# other useful math functions

import math
x = 9.9
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)
print(result)


# circumference of circle

import math
radius = float(input("enter the radius of the circle:"))
circumference = 2 * math.pi * radius
print(f"the circumference is : {circumference}")

# area of circle

import math
radius = float(input("enter the radius of the circle:"))
area = math.pi * pow(radius, 2)
print(round(area,2))


# Hypotaneous of the triangle

import math
a =float(input("enter side A:"))
b =float(input("enter side B:"))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"this is the value of C : {c}")