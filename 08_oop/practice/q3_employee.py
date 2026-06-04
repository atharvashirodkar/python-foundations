class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Details")
        print("----------------")
        print(f"ID     : {self.emp_id}")
        print(f"Name   : {self.name}")
        print(f"Salary : {self.salary}")

    def annual_salary(self):
        annual_salary = self.salary * 12
        print(f"Annual Salary: {annual_salary}")
        