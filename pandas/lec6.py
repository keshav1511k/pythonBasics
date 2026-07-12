# Filtering : Keeping the rows that matches the condition.

import pandas as pd
df = pd.read_csv("data.csv")

# tall_pokemon = df[df["Height"] >= 2]
# heavy_pokemon = df[df["Weight"] >= 100]
# legendary_pokemon = df[df["Legendary"] == 1]

# OR operator (we do not use "or" like in python. here we use "|")

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

# AND operator (we do not use "and" like in python. here we use "&")

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)