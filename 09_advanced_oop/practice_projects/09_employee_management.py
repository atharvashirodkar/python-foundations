class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"ID       : {self.emp_id}")
        print(f"Name     : {self.name}")
        print(f"Salary   : {self.salary}")


class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_details(self):
        print("Developer Details")
        print("-----------------")
        super().display_details()
        print("Role     : Developer")
        print(f"Language : {self.programming_language}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def display_details(self):
        print("Manager Details")
        print("---------------")
        super().display_details()
        print("Role      : Manager")
        print(f"Team Size : {self.team_size}")


# Developer Object

developer1 = Developer(101, "Rahul", 50000, "Python")

developer1.display_details()


print()


# Manager Object

manager1 = Manager(201, "Priya", 80000, 10)

manager1.display_details()
