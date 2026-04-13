# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces no. of arguments
#                     1. positional 2. DEFAULT 3. keyword 4. arbitrary


def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1-discount) * (1+tax)

print(f"The net price is : {net_price(500,0.1)}")
print(f"The net price is : {net_price(500, 0.1, 0)}")


# exercise - Count up timer

import time

def count(start, end):   # another way using default :-  def count(end, start = 0):    # we proceed from end beacuse default parameter followed by a positional argument
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE")

count(0,3)    # count(30,15). start from 15 and end at 30
