# python compound interest calculator


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter the principle amount : "))
    if principle <= 0:
        print("principle cannot be less than or equal to zero.")

while rate <= 0:
    rate = float(input("enter the rate of interest : "))
    if rate <= 0:
        print("rate cannot be less than or equal to zero.")

while time <= 0:
    time = int(input("enter the time in years : "))
    if time <= 0:
        print("time cannot be less than or equal to zero.")

total = principle * pow((1 + rate / 100), time)
print(f"balance after {time} years : ${total:.2f}")



# other method in which we take time, principle and rate is zero and not specifying while loop condition
#.  only write true or false to run and use break to break the loop


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principle amount : "))
    if principle < 0:
        print("principle cannot be less than zero.")
    else :
        break

while True:
    rate = float(input("enter the rate of interest : "))
    if rate < 0:
        print("rate cannot be less than zero.")
    else :
        break

while True:
    time = int(input("enter the time in years : "))
    if time < 0:
        print("time cannot be less than zero.")
    else :
        break

total = principle * pow((1 + rate / 100), time)
print(f"balance after {time} years : ${total:.2f}")