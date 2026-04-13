# Iterables = An object / collection that can return its elements one at a time
#             allowing it to be iterated over in a loop

numbers = (1,2,3,4,5)   #. we can use list as well 

for num in reversed(numbers):
    print(num, end = " ")


# sets : these are not reversible 

fruits = {"apple", "banana", "orange", "peach"}

for fruit in fruits:
    print(fruit, end = " ")


# string

name = "Keshav Kumar"

for character in name:
    print(character, end=" ")


# Dictionaries 

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
