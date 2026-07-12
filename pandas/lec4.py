import pandas as pd

df = pd.read_csv("data.csv")
# df = pd.read_json("data.json").   To read json files.
print(df)
print(df.to_string())   # To print all the datas of the file.