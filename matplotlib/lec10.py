# PANDAS and MATPLOTLIB :-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="yellow",
                                             edgecolor="black")

plt.title("Number of Pokemon by Primary Type", fontweight="bold")
plt.xlabel("Count", fontweight="bold", color="red")
plt.ylabel("Type", fontweight="bold", color="blue")
plt.tight_layout()
plt.show()

# This is how we work with a given data and use pandas and matplot together for creating interactive visuals.