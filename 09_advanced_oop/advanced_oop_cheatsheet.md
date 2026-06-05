# Advanced OOP Cheatsheet

# 1. Inheritance

Inheritance allows one class to acquire properties and methods from another class.

## Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

## Example

```python
class Person:
    def display(self):
        print("Person Class")

class Student(Person):
    pass

student1 = Student()

student1.display()
```

## Types of Inheritance

### Single Inheritance

```text
Parent → Child
```

### Multilevel Inheritance

```text
Grandparent → Parent → Child
```

### Multiple Inheritance

```text
Parent1 + Parent2 → Child
```

---

# 2. Method Overriding

Method overriding occurs when a child class provides its own implementation of a parent class method.

## Example

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog1 = Dog()

dog1.sound()
```

## Output

```text
Dog barks
```

---

# 3. super()

`super()` is used to access parent class methods and constructors.

## Example

```python
class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        super().work()
        print("Developer writes code")

developer1 = Developer()

developer1.work()
```

## Output

```text
Employee works
Developer writes code
```

---

# 4. Polymorphism

Polymorphism allows the same method name to behave differently for different objects.

## Example

```python
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

## Output

```text
Dog barks
Cat meows
```

---

# 5. Abstraction

Abstraction hides implementation details and shows only essential features.

Python uses:
- `ABC`
- `abstractmethod`

from the `abc` module.

---

## Abstract Class Syntax

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car started")

car1 = Car()

car1.start()
```

## Output

```text
Car started
```

---

# 6. Difference Between Abstraction and Inheritance

| Inheritance | Abstraction |
|---|---|
| Reuses code | Hides implementation |
| Creates parent-child relationship | Defines mandatory methods |
| Uses normal classes | Uses abstract classes |

---

# 7. Difference Between Overloading and Overriding

| Method Overloading | Method Overriding |
|---|---|
| Same method, different parameters | Same method, different implementation |
| Occurs in same class | Occurs in parent-child classes |
| Python has limited support | Fully supported |

---

# 8. Important Keywords

| Keyword | Purpose |
|---|---|
| `class` | Create class |
| `self` | Current object reference |
| `super()` | Access parent class |
| `ABC` | Create abstract class |
| `@abstractmethod` | Create abstract method |
| `pass` | Empty block placeholder |

---

# 9. Common OOP Interview Questions

## What is inheritance?

Inheritance allows one class to acquire properties and methods from another class.

---

## What is method overriding?

Method overriding means redefining a parent class method inside a child class.

---

## What is polymorphism?

Polymorphism allows one interface to behave differently for different objects.

---

## What is abstraction?

Abstraction hides implementation details and exposes only required functionality.

---

## Why use abstract classes?

Abstract classes enforce method implementation in child classes.

---

## Difference Between Class and Object

| Class | Object |
|---|---|
| Blueprint | Real instance |
| Logical entity | Physical entity |

---

# 10. Best Practices

- Use inheritance only for true IS-A relationships.
- Avoid unnecessary inheritance.
- Prefer simple class structures for beginners.
- Use meaningful class and method names.
- Keep methods focused on one responsibility.
- Use polymorphism instead of large if-else chains.
- Use abstraction for common interfaces.

---

# 11. Quick Revision Summary

| Concept | Purpose |
|---|---|
| Inheritance | Reuse code |
| Method Overriding | Change parent behavior |
| super() | Access parent methods |
| Polymorphism | Same method, different behavior |
| Abstraction | Hide implementation details |