# Data Cleaning = The process of fixing/removing:-
# 1. Incomplete, incorrect, irrelevant data.
# 2. 75% of work with Pandas is data cleaning.

import pandas as pd
df = pd.read_csv("data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])  # Here we drop two columns one is legendary and other is No column.

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2":"None"})  #  Fill all null values in type2 with none.

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                    "Fire":"FIRE",
#                                    "Water":"WATER"})

# 4. Standardze text 
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types 
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicates values
df = df.drop_duplicates()

print(df.to_string())