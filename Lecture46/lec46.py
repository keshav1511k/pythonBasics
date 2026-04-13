# object = A bundle of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# you need a 'class' to create objects

# class = (blueprint) used to design the structure and layout of an object


from car import Car

car1 = Car("mustang", 2020, "red", False)
car2 = Car("ford", 2024, "blue", False)
car3 = Car("bmw", 2025, "black", True)

print(car1.model)
print(car2.model)
print(car3.model)

car1.drive()
car1.stop()
car1.describe()

car2.drive()
car2.stop()
car2.describe()

car3.drive()
car3.stop()
car3.describe()