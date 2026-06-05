class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_course(self):
        print(f"Course : {self.course}")


# Create Object

student1 = Student("Rahul", 20, "Python Programming")

print("Student Details")
print("----------------")

student1.display_info()
student1.show_course()
