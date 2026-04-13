# Dice roller Program

import random

dice_art = {
    1 : ("┌---------┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└---------┘"),
    2 : ("┌---------┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└---------┘"),
    3 : ("┌---------┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└---------┘"),
    4 : ("┌---------┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└---------┘"),
    5 : ("┌---------┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└---------┘"),
    6 : ("┌---------┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└---------┘"),
}

dice = []
total = 0
num_of_dice = int(input("How many dice? : "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):    # want to print it on one line so chhose other approach
#         print(line)

for line in range(5):   # pattern contain 5 lines 
    for die in dice:
        print(dice_art.get(die)[line], end=" ")   # want to print one line 
    print()

for die in dice:
    total += die
print(f"total: {total}")