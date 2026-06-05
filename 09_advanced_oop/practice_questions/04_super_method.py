class Employee:
    def work(self):
        print("Employee works")


class Developer(Employee):
    def work(self):
        super().work()
        print("Developer writes code")


# Create Object

developer1 = Developer()

developer1.work()
