# Series : A Pandas 1-Dimensional labeled array that can hold any data type. Think of it like a single column in a spreadsheet (1-Dimensional)

# import pandas as pd

# data = [100,101,102,200,201]
# series = pd.Series(data, index=["a","b","c","d","e"])

# series.loc["c"] = 200
# # print(series)
# print(series.loc["c"])

# # iloc
# print(series.iloc[0])

# # applying conditions
# print(series[series < 200])

# EXERCISE:

import pandas as pd

calories = {"Day 1": 1750, "Day 2": 1500, "Day 3": 2040, "Day 4": 2121, "Day 5": 1640}

series = pd.Series(calories)

# print(series)
series.loc["Day 5"] += 500
# print(series.loc["Day 3"])
print(series[series < 2000])