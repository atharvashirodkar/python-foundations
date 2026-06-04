# Interview Questions - OOP Fundamentals

This document covers the most commonly asked interview questions from:

- Classes and Objects
- Constructors
- Instance Methods
- Class vs Instance Variables
- Encapsulation

---

# Classes and Objects

## Q1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using classes and objects.

It helps in:
- Code reusability
- Better organization
- Easier maintenance
- Real-world modeling

---

## Q2. What is a Class?

A class is a blueprint or template used to create objects.

Example:

```python
class Student:
    pass
```

The class defines the structure and behavior that objects will have.

---

## Q3. What is an Object?

An object is an instance of a class.

Example:

```python
student1 = Student()
```

Here:
- `Student` → Class
- `student1` → Object

---

## Q4. What is the difference between a Class and an Object?

| Class | Object |
|---------|---------|
| Blueprint | Instance |
| Logical entity | Physical entity |
| Created using `class` | Created from a class |
| Defines structure | Holds actual data |

Example:

```python
class Car:
    pass

car1 = Car()
```

---

## Q5. Can we create multiple objects from a single class?

Yes.

```python
student1 = Student()
student2 = Student()
student3 = Student()
```

All objects are created from the same class.

---

## Q6. What are Attributes?

Attributes are variables associated with a class or object.

Example:

```python
class Student:
    school = "ABC School"
```

```python
student.name = "Rahul"
```

Attributes store data related to an object.

---

# Constructors

## Q7. What is a Constructor?

A constructor is a special method that automatically executes when an object is created.

In Python:

```python
__init__()
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## Q8. Is `__init__()` a Constructor in Python?

In beginner and interview contexts, yes.

Technically:

1. Python creates the object using `__new__()`
2. Python initializes the object using `__init__()`

Therefore:

```python
__new__()
```

creates the object,

and

```python
__init__()
```

initializes it.

---

## Q9. Why Do We Use Constructors?

Constructors help initialize object data automatically.

Example:

```python
student1 = Student("Rahul")
```

Without constructors, attributes must be assigned manually.

---

## Q10. Can a Class Have Multiple Constructors in Python?

No.

Python does not support method overloading like Java.

Example:

```python
class Student:

    def __init__(self):
        pass

    def __init__(self, name):
        pass
```

The second constructor replaces the first one.

Alternative:

Use default arguments.

```python
def __init__(self, name="Unknown"):
```

---

# self Keyword

## Q11. What is `self`?

`self` refers to the current object.

Example:

```python
self.name = name
```

When:

```python
student1 = Student("Rahul")
```

internally Python does:

```python
Student.__init__(student1, "Rahul")
```

So:

```python
self.name
```

becomes:

```python
student1.name
```

---

## Q12. Is `self` a Keyword in Python?

No.

`self` is only a naming convention.

This also works:

```python
class Student:

    def __init__(current, name):
        current.name = name
```

However, using anything other than `self` is strongly discouraged.

---

## Q13. Why Must `self` Be the First Parameter?

Python automatically passes the current object when a method is called.

Example:

```python
student1.display()
```

Internally:

```python
Student.display(student1)
```

Therefore, the method must accept the object as its first parameter.

---

# Instance Methods

## Q14. What is an Instance Method?

An instance method is a method that operates on object data.

Example:

```python
class Student:

    def display(self):
        print(self.name)
```

---

## Q15. How Are Instance Methods Called?

Using an object.

Example:

```python
student1.display()
```

Internally:

```python
Student.display(student1)
```

---

## Q16. What Happens if We Remove `self` from an Instance Method?

Example:

```python
class Student:

    def display():
        print("Hello")
```

Calling:

```python
student1.display()
```

raises:

```text
TypeError:
display() takes 0 positional arguments but 1 was given
```

Because Python automatically passes the object.

---

# Class Variables vs Instance Variables

## Q17. What is an Instance Variable?

Instance variables belong to individual objects.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each object gets its own copy.

---

## Q18. What is a Class Variable?

Class variables belong to the class and are shared by all objects.

Example:

```python
class Student:

    school = "ABC School"
```

---

## Q19. Difference Between Class Variables and Instance Variables

| Class Variable | Instance Variable |
|---------------|------------------|
| Shared by all objects | Unique for each object |
| Defined inside class | Defined using `self` |
| One copy | Multiple copies |
| Stores common data | Stores object-specific data |

---

## Q20. When Should You Use a Class Variable?

Use a class variable when data should be shared across all objects.

Examples:

```python
school_name
company_name
tax_rate
employee_count
```

---

## Q21. What is a Common Mistake with Class Variables?

Example:

```python
class Student:
    school = "ABC School"

s1 = Student()
s1.school = "New School"
```

Many think this changes the class variable.

It does not.

Instead, Python creates a new instance variable for `s1`.

```python
print(Student.school)
```

Output:

```text
ABC School
```

```python
print(s1.school)
```

Output:

```text
New School
```

---

# Encapsulation

## Q22. What is Encapsulation?

Encapsulation is the process of combining data and methods into a single unit (class) and restricting direct access to internal data.

Example:

```python
class BankAccount:
    pass
```

---

## Q23. Why Is Encapsulation Important?

Benefits:

- Protects data
- Prevents invalid updates
- Improves maintainability
- Improves security
- Encourages controlled access

---

## Q24. What Are Public Members?

Public members can be accessed from anywhere.

Example:

```python
self.name = "Rahul"
```

Access:

```python
student.name
```

---

## Q25. What Are Protected Members?

Protected members use a single underscore.

Example:

```python
self._salary
```

They can still be accessed but are intended for internal use.

---

## Q26. What Are Private Members?

Private members use double underscores.

Example:

```python
self.__balance
```

Direct access is discouraged.

---

## Q27. Does Python Have Truly Private Variables?

No.

Python uses name mangling.

Example:

```python
self.__balance
```

internally becomes:

```python
self._BankAccount__balance
```

The variable still exists and can be accessed if necessary.

---

## Q28. What is Name Mangling?

Name mangling is Python's mechanism for reducing accidental access to private members.

Example:

```python
self.__balance
```

becomes:

```python
self._ClassName__balance
```

---

## Q29. Difference Between `_variable` and `__variable`?

| Type | Syntax | Meaning |
|--------|--------|----------|
| Public | `name` | Accessible everywhere |
| Protected | `_name` | Internal-use convention |
| Private | `__name` | Name-mangled |

---

## Q30. Why Does Python Use Conventions Instead of Strict Access Modifiers?

Python follows the philosophy:

> "We are all consenting adults here."

The language trusts developers and uses conventions rather than enforcing strict restrictions like Java or C++.