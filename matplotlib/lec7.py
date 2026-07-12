# Scatter Grpah:- Shows the realtionship between two variables which helps to identify a correlation (+, -, None).
# Example: Study Hours vs Test Scores

import matplotlib.pyplot as plt 
import numpy as np

x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])
y1 = np.array([55,60,65,62,68,72,75,76,82,85,87])

x2 = np.array([0,1,2,3,3,4,5,6,7,8,8])
y2 = np.array([50,58,65,72,78,70,71,78,81,85,92])

plt.scatter(x1, y1, color="blue",
                    alpha = 0.5,  #transparency
                    s = 200, #size
                    label = "Class B")      

plt.scatter(x2, y2, color="red",
                    alpha = 0.5,  #transparency
                    s = 200, #size
                    label = "Class B")      

plt.title("Test Scores", fontweight= "bold")
plt.xlabel("Hours Studies")
plt.ylabel("Scores Got")

plt.legend()
plt.show()