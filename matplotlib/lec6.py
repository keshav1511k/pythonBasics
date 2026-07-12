# PIE Charts:- Circular chart divided into slices to show percentages of the total. good for visualizing distribution among categories.

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([400,350,375,325])
colors = ["red","yellow","blue","green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.2],
                shadow=True,
                startangle=180)
plt.title("FCK College", fontweight="bold")
plt.show()