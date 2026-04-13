# Class methods = Allow operations related to the class itself
# take (cls) as the first parameter, which represents the class itself.
# cls means class

# Instance methods = Best for the operations on instances of the class (object)
# Static methods = Best for the utility functions that do not need access to class data
# Class methods = Best for the class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students : {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa : {cls.total_gpa / cls.count:.2f}"
        
student1 = Student("Keshav", 7.5)
student2 = Student("Ankit", 7.6)
student3 = Student("Shiv", 7.7)

print(Student.get_count())
print(Student.get_average_gpa())