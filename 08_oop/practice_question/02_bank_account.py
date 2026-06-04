class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance: {self.__balance}")

account1 = BankAccount("Rahul", 10000)

account1.deposit(2000)
account1.withdraw(1000)
account1.show_balance()

account1.withdraw(15000)