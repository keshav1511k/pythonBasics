# Static methods = A method belong to a class rather than any object from that class (instance)
# Instance methods = Best for operations on the instances of the class (objects)
# Static methods = Best for the utility functions that do not need access to class data


class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Keshav", "Manager")
employee2 = Employee("Aman", "Cashier")
employee3 = Employee("Ankit", "Cook")

print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
