# Bar Charts :- Compare categories of the data by representing each category with a bar.

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4,3,2,5,3,2])

plt.bar(categories, values, color="orange")
# plt.barh(categories, values, color="skyblue")   # for horizontal bars.

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()