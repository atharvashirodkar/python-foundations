# Practice Questions - Session 08: OOP Fundamentals

## Question 1: Student Class

Create a `Student` class with the following:

### Attributes
- `roll_no`
- `name`
- `marks`

### Methods
- `display_details()`
- `check_result()`

### Condition
- If marks >= 40 → Pass
- Otherwise → Fail

### Expected Output

```text
Student Details
----------------
Roll No : 101
Name    : Rahul
Marks   : 75
Result  : Pass

Student Details
----------------
Roll No : 102
Name    : Priya
Marks   : 35
Result  : Fail
```

---

## Question 2: Bank Account

Create a `BankAccount` class with the following:

### Attributes
- `account_holder`
- `balance`

### Methods
- `deposit(amount)`
- `withdraw(amount)`
- `show_balance()`

### Conditions
- Allow withdrawal only if sufficient balance is available.
- Display `"Insufficient Balance"` otherwise.

### Expected Output

```text
Deposited ₹2000
Withdrawn ₹1000
Current Balance: 11000
```

---

## Question 3: Employee Class

Create an `Employee` class with the following:

### Attributes
- `emp_id`
- `name`
- `salary`

### Methods
- `display_details()`
- `annual_salary()`

### Formula

```text
Annual Salary = salary × 12
```

### Expected Output

```text
Employee Details
----------------
ID     : 101
Name   : Rahul
Salary : 50000

Annual Salary: 600000
```