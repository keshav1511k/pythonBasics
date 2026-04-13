# nested loop = a loop within another loop (outer , inner)
#              outer loop:
#                  inner loop:


for y in range(3):
    for x in range(1,10):
        print(x, end="\n")
    print()


# exercise 1 = to print a rectangle

rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("enter a symbol to use: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()