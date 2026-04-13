# if = do some code if the condition is true  else = do something else


age = int(input("enter your age : "))
if age>= 18:
    print("you are eligible to vote.")
elif age < 18:
    print("you are not eligible to vote.")
else:
    print("wrong input")


# example - 2

name = input("enter your name : ")
if name == "":
    print("you have not typed your name")
else:
    print(f"Hello {name}")

# example - 3

online = True
if online :
    print("you are online")
else:
    print("you are offline")