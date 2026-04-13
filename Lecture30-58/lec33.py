# keyword arguments = An argument preceded by an identifier 
#                     helps with readability 
#                     order of the arguments does not matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello!", title="Mr.", last="Kumar", first="Keshav")       # keyword arguments followed by positional arguments

# seperate by -
print("1", "2", "3", "4", "5", sep="-")

# print phone number

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+1", area="123", first="456", last="2345")
print(phone_num)
