# LABELS:-

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,22,25,12])
y2 = np.array([17,25,5,22])
y3 = np.array([13,20,15,32])

plt.title("Class size", fontsize=25,
                        fontfamily="Arial",
                        fontweight="bold",
                        color="#2d4cfc")

plt.xlabel("Year",      fontsize=20,
                        fontfamily="Arial",
                        fontweight="bold",
                        color="#2dbefc")

plt.ylabel("Students",  fontsize=20,
                        fontfamily="Arial",
                        fontweight="bold",
                        color="#2dbefc")

plt.tick_params(axis="both",
                colors="red")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x)

plt.show()