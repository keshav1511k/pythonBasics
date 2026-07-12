# Histograms:- A visual representation of the distribution of quantitative data. They groups values into bins (intervals) and count how many fall in each range.

import matplotlib.pyplot as plt
import numpy as np

# loc :- location of centre or median of the data.
# scale :- standard deviation
# size :- how many numbers we want to generate

scores = np.random.normal(loc=80, scale=10, size=100) # normal function for a normal distribution.
scores = np.clip(scores, 0, 100)  # 100 se jada aur 0 se kam sab zero

plt.hist(scores, 
         bins=10,
         color="skyblue",
         edgecolor = "black")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("No. of Students")
plt.show()
