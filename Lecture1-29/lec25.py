# Dictionaries = a collection of {key:value} pairs, ordered and changeable. No duplicates

capitals = {"USA" : "WASHINGTON D.C ",
            "INDIA" : "DELHI",
            "CHINA" : "BEIJING",
            "RUSSIA" : "MOSCOW"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("RUSSIA"):
    print("The Capital exists.")
else:
    print("The Capital does not exist.")

capitals["PUNJAB"] = "CHANDIGARH"    # Adding to the dictionary
capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Detroit"})
capitals.pop("CHINA")
capitals.popitem()
capitals.clear()
print(capitals)

keys = capitals.keys()
for key in capitals.keys():
    print(key)

value = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")