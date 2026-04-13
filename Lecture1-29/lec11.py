# Logical opeartors = ecvaluate multiple conditions (or, and , not)
#                or = atleast one condition is true 
#                and = both conditions must be true
#                not = inverts the condition (not false , not true)

                # or

temp = 25 
is_raining = True

if temp > 35 or temp < 0 or is_raining :
    print("outdoor event is cancelled")
else :
    print("outdoor event is still scheduled")


                # and & not 

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("it is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("it is cloudy")
