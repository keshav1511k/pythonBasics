# for loops = execute a block of code a fixed number of times.
#.  you can iterate over a range, string, sequence, etc.

# example 1

for x in range (1, 11):
    print(x)
print("hello")

# example 2 

for x in reversed(range(1, 11)):
    print(x)
print("hello")

# example 3 

for x in range (1, 11, 2):
    print(x)
print("hello")

# example 4

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# example 5

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# example 6

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)