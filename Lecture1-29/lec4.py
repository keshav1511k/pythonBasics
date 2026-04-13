# input() :- a function that prompts the user to enter data 
# Returns the entered data as a string

name = input("what is your name:")
age = int(input("how old are you:"))

age += 1

print(f"hello {name}")
print("happy birthday")
print(f"your are {age} years old")


# exercise 1 :- area of a rectangle 

length = float(input("enter the length:"))
width = float(input("enter width:"))
area = length * width

print(f"the area is {area} cm^2")


# erercise 2 :- shopping cart program 

item = input("what item would you like to buy:")
price = float(input("what is the price of item:"))
quantity = int(input("how many items you buy:"))
total = price * quantity

print (f"you have bought {quantity} items")
print(f"total price is ${total}")