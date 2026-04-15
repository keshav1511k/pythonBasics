import re

email = "test123@gmail.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
