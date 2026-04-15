# Python reading file (.txt, .json, .csv)

# text file

# file_path = "output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have the permission to read that file ")

# json file

# import json

# file_path = "output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])   # access name only "print(content["name"])"
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have the permission to read that file ")

# csv file

import csv

file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)  # acces each column "print(line[0])"
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read that file ")