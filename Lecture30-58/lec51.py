# Polymorphism = greek word that means to "have many forms or faces"
# Poly = many
# Morphe = form

# Two ways to achieve Polymorphism
# 1. Inheritance = an object could be treated of the same type as a parent class
# 2. Duck Typing = object must have necessary attributes/methods


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(slef):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(2,3), Pizza("paneer", 12)]

for shape in shapes:
    print(f"area is {shape.area()}cm^2")


# In this example pizza have many forms like it is circle, pizza and also a shape.
