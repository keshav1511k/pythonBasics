# plot Customization

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,22,25,12])
y2 = np.array([17,25,5,22])
y3 = np.array([13,20,15,32])

line_style = dict(marker=".",
                  markersize=20,
                  markerfacecolor="#1cd3fc",
                  markeredgecolor="#1cd3fc",
                  linestyle="solid",
                  linewidth=2)

plt.plot(x,y1, color="blue", **line_style)
plt.plot(x,y2, color="red", **line_style)
plt.plot(x,y3, color="green", **line_style)
plt.show()