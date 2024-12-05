class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student1(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id

    def display_student_info(self):
        self.display_info() 
        print(f"Student ID: {self.student_id}")

# Create an instance of the class
student1 = Student1("saranya", 21, "S12345")
student2 = Student1("lakshmi", 11, "S12346")


# Display student information
student1.display_student_info()
student2.display_student_info()
