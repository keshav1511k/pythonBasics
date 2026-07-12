# Selection from the file:

import pandas as pd

df = pd.read_csv("data.csv", index_col="Name") # By using index_col we can easily search by that value in the file.

# SELECTION BY COLUMNS

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Height","Weight"]].to_string())

# SELECTION BY ROWS

# print(df.loc["Pikachu"])

# print(df.loc["Charizard",["Height", "Weight"]])  # We pass a list inside as a second argument that contains the columns which we want to display.

# print(df.loc["Charizard" : "Blastoise", ["Height", "Weight"]])  # Here we use slicing technique to print values in a range.

# Use integer based indexing:

# print(df.iloc[0:11:2, 0:3])  # Here we print from 0 to 10 as last value (11) is exclusive and add a step of 2 and in second argument we pass the no of the columns which we want to print and from where.

# EXERCISE : Take input from user and search the details of that and print it.

import pandas as pd
df = pd.read_csv("data.csv", index_col="Name")

pokemon = input("Enter a name of a pokemon (first letter capital): ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")