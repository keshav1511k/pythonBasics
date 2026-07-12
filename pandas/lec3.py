# DataFrames: A tabular data structure with rows and columns(2 Dimensional). Similar to an Excel spreadsheet.

import pandas as pd

data = {
    "Name": ["Keshav", "Aman", "Ankit", "Rahul"],
    "Age": [22, 23, 24, 25]
}

df = pd.DataFrame(data, index=["Employee1","Employee2","Employee3","Employee4"])

# print(df)
# print(df.loc["Employee1"])
# print(df.iloc[1])

# Add a new Column:
df["Job"] = ["Cook", "N/A", "Cashier", "Engineer"]
print(df)

# Add new Rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "SDE2"},
                         {"Name": "Shiv", "Age": 35, "Job": "Manager"}],
                       index=["Employee5","Employee6"])
df = pd.concat([df, new_rows])
print(df)
