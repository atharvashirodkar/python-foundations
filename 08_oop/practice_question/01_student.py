class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display_details(self):
        print("\nStudent Details")
        print("----------------")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Result  : {self.check_result()}")

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
        
student1 = Student(101, "Rahul", 75)
student2 = Student(102, "Priya", 35)

student1.display_details()
student2.display_details()