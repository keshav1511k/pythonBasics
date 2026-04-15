# Python writing files (.txt, .json, .csv)

# write

txt_data = "I like Apple"
file_path = "output.txt"

with open(file_path, "w") as file:   # we can take realtive file path also 
    file.write(txt_data)
    print(f"txt file '{file_path} was created")

# use x when file exists

txt_data = "I like Apple"
file_path = "output.txt"
try:
    with open(file_path, "x") as file:   
        file.write(txt_data)
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("This file already exist")

# use a for append

txt_data = "I like Apple"
file_path = "output.txt"
try:
    with open(file_path, "a") as file:   
        file.write("\n" + txt_data)
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("This file already exist")

# writing employee data

employees = ["Keshav", "Shiva", "Ankit", "Amit"]
file_path = "output.txt"
try:
    with open(file_path, "w") as file: 
        for employee in employees:  
            file.write(employee + " ")
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("This file already exist")


# writing json file

import json

employees = {
    "name": "Keshav",
    "age": 22,
    "job": "SDE"
}
file_path = "output.json"
try:
    with open(file_path, "w") as file: 
        json.dump(employees, file, indent=4)
        print(f"json file '{file_path} was created")
except FileExistsError:
    print("This file already exist")

# writing csv files

import csv

employees = [
    ["Name", "Age", "job"],
    ["Keshav", 22, "SDE"],
    ["Aman", 22, "DS"],
    ["Ankit", 22, "SDE"],
]
file_path = "output.csv"
try:
    with open(file_path, "w", newline="") as file: 
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path} was created")
except FileExistsError:
    print("This file already exist")