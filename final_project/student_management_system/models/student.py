class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }

    def display_info(self):
        print(f"""
            Student Id : {self.student_id}
            Name       : {self.name}
            Age        : {self.age}
            Course     : {self.course}
            """)
