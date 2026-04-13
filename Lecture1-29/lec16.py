# while loop = executes some of the codes while some condition remains true

# example 1

name = input("enter your name : ")

while name == "":
    print("you did not enter your name ")
    name = input("enter your name : ")

print(f"hello {name}")


# example 2 

age = int(input("enter your age : "))

while age < 0 :
    print("age cannot be negative ")
    age = int(input("enter your age : "))

print(f"you are {age} years old ")


# example 3

food = input("enter a food you like (q to quit) : ")

while not food == "q":
    print(f"you like {food}")
    food = input("enter a food you like (q to quit) : ")

print("bye")


# example 4

num = int(input("enter a number between 1 - 10 : "))

while num < 1 or num > 10 :
    print(f"{num} is not valid ")
    num = int(input("enter a number between 1 - 10 : "))

print(f"your number is {num}")