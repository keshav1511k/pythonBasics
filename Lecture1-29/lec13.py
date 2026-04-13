# strings methods 

name = input("enter your full name :")
phone_number = input("enter your phone number : ")

result = len(name)
result = name.find("e")  # first occurance 
result = name.rfind("e") # last occurance
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count("-")
phone_number = phone_number.replace("-", "")

print(phone_number)



# validate user input exercise 
# 1. username doesnot contain more than 12 characters
# 2. username doesnot contain any spaces
# 3. username doesnot contain any digits

username =input("enter a username : ")
if len(username) > 12 :
    print("your username doesnot contain more than 12 characters")
elif  username.find(" ") != -1:
    print("your username doesnot contain any spaces")
elif not username.isalpha():
    print("your username doesnot contain any digits")
else :
    print(f"Welcome {username}")