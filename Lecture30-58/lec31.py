# function = a block of resuable code place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happpy Birthday to {name}!")
    print(f"You are {age} years old.")
    print("Happy Birthday to you!")
    print()

happy_birthday("Aman", 20)
happy_birthday("Keshav", 20)
happy_birthday("David",21)


# Example - 1

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due : {due_date}")

display_invoice("Keshav", 200, "01/02")


# return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(substract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


# captialize first and last name 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("keshav", "kumar")
print(full_name)