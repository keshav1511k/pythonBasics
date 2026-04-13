# conditional statements = A one line shortcut for the if-else statement (ternary opeartor)
#.     print or assign one or two values on a condition
#.     X if condition else Y

num = 5
a = 6 
b = 7
age = 13
temperature = 20
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a >b else b
min_num = a if a <b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)
