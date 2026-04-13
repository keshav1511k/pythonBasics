# LIST comprehensions = A concise way to create lists in python
#                       compact and easier to read then traditional loops
#                       [expression for value in iterable if condition]


# Traditional way 

doubles = []
for x in range (0,10):
    doubles.append(x*2)
print(doubles)

# Exercise - 1 : new way

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

# Exercise - 2

fruits = ["apple", "banana", "orange","peach"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)


# Exercise - 3

numbers = [1, -2, -3, 4, 5, -6, 7, -9]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num %2 == 0]
odd_nums = [num for num in numbers if num %2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

# Exercise - 4

grades = [85, 42, 54, 67, 69, 82, 97, 32]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)