# 2D collections = it behaves like a matrix and we can access elements by using the indeces

fruits = ["apple", "orange", "banana", "peach"]
vegetables = ["pea", "potato", "carrots"]
meats = ["chicken", "fish", "mutton"]

groceries = [fruits, vegetables, meats]
# print(groceries[0][2])

for collections in groceries:
    for food in collections:
        print(food, end =" ")
    print()

# example - 1 :- make a keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for rows in num_pad:
    for num in rows:
        print(num, end=" ")
    print()