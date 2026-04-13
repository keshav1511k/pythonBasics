# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

# in 

word = "Apple"
letter = input("enter a letter to guess in word: ")
if letter in word:
    print(f"There is a {letter}")
else:
     print(f"{letter} was not found")

# not in  :- just reverse the statements

word = "Apple"
letter = input("enter a letter to guess in word: ")
if letter not in word:
    print(f"{letter} was not found")
else:
     print(f"There is a {letter}")


# sets (we can as take lists and tuples)

students = {"keshav", "kumar", "ankit"}
student = input("enter a name of a student : ")
if student in students:   # here we can also use "not in" just by reversing the print statements
     print(f"{student} is a student")
else:
     print(f"{student} is not a student")


# Dictionaries


grades = {"keshav": 1,
          "shiva": 2,
          "ankit": 3}

student = input("enter the name of a student: ")
if student in grades :
     print(f"{student}'s grade is {grades[student]}")
else:
     print(f"{student} was not found")


# check email is valid or not

email = "keshav@test.com"
if "@" in email and "." in email:
     print("email is valid")
else :
     print("email is invalid ")