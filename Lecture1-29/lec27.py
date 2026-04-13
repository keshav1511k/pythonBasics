# Random Numbers

import random

low = 1
high = 100

number = random.randint(low, high)  # here we can also pass it as start, end like (0, 6)
number = random.random()   # for floating numbers
print(number)


# example 1

import random
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# example - 2

import random
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)