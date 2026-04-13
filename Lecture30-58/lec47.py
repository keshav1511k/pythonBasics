# class variable = shared among all instances of a class
# defined outside the constructor
# allow you to share data among all objects created from that class

class Student:
    
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.num_students += 1  # if we modify a class variable use class name instead of instance name i.e object name

student1 = Student("Keshav", 22)
student2 = Student("Aman", 23)
student3 = Student("Ankit", 24)
student4 = Student("Amit", 23)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student3.name)
print(student3.age)

# print(student1.class_year) # donot call like that always use from class not from instance

# print(Student.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
