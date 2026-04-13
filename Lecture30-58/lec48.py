# Inheritance = allows a class to inherit attributes and methods from another class which helps with code reusability and extensibility 
# class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name 
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQEEK!")

dog = Dog("Scooby")
cat = Cat("Snowbell")
mouse = Mouse("Jerry")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()