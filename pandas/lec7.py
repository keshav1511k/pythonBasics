# Aggregate Functions = Reduces a set of values into a single summary value.
# Used to summarize and analyze data.
# Often used with the groupby() function.

import pandas as pd
df = pd.read_csv("data.csv")

# Some of them are used only for numeric values 
# These are applied for WHOLE DATAFRAMES.

# print(df.mean(numeric_only = True))  # For numeric we use this.
# print(df.sum(numeric_only = True))
# print(df.min(numeric_only = True))
# print(df.max(numeric_only = True))
# print(df.count())    # It doesnot count the null values.

# SINGLE COLUMNS

# print(df["Height"].mean())  # Since height is a numeric value so we donot need to pass anything.
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# GROUP SAME DATA

group = df.groupby("Type1")  # We choose on which thing we want to group elemnts.

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())