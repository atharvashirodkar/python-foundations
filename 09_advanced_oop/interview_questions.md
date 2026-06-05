# Interview Questions - Session 09: Advanced OOP

# 1. What is Inheritance in Python?

Inheritance allows one class to acquire properties and methods from another class.

The class being inherited is called the:
- parent class
- base class

The class that inherits is called the:
- child class
- derived class

Inheritance helps:
- reduce code duplication
- improve code reusability
- create logical class hierarchies

---

## Example

```python
class Person:
    def display_info(self):
        print("Person Information")

class Student(Person):
    pass

student1 = Student()

student1.display_info()
```

---

## Real-World Example

```text
Animal → Dog
Vehicle → Car
Employee → Manager
```

A Dog IS-A Animal.

That is why inheritance is appropriate.

---

# 2. Why Should Inheritance Be Used Carefully?

Many beginners misuse inheritance.

Inheritance should only be used when a true:

```text
IS-A
```

relationship exists.

Correct:

```text
Car IS-A Vehicle
Dog IS-A Animal
```

Incorrect:

```text
ShoppingCart IS-A Product
Engine IS-A Car
```

Wrong inheritance creates tightly coupled and confusing designs.

In many situations, composition is a better choice.

---

# 3. What is Method Overriding?

Method overriding occurs when a child class provides its own implementation of a parent class method.

This allows child classes to define specialized behavior.

---

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

---

## Output

```text
Dog barks
```

---

## Why is Method Overriding Important?

Without overriding, every child class would behave exactly like the parent class.

Overriding allows:
- flexibility
- customization
- runtime polymorphism

---

# 4. What is super() in Python?

`super()` is used to access parent class methods and constructors from a child class.

It prevents code duplication and allows reuse of parent functionality.

---

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

---

## Output

```text
Employee works
Developer writes code
```

---

## Why is super() Useful?

Without `super()`, child classes may completely replace parent behavior.

Using `super()` allows:
- extending parent functionality
- cleaner code reuse
- better maintainability

---

# 5. What is Polymorphism?

Polymorphism means:

```text
Same method name
Different behavior
```

Different objects can respond differently to the same method call.

---

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

---

## Output

```text
Dog barks
Cat meows
```

---

## Why is Polymorphism Powerful?

Without polymorphism, programs often rely on large:

```python
if-else
```

chains.

Polymorphism makes code:
- cleaner
- scalable
- easier to extend

New classes can be added without changing existing logic.

---

# 6. What is Runtime Polymorphism?

Runtime polymorphism occurs when method execution is decided during program execution.

Python determines which method to call based on the object type at runtime.

Method overriding is the most common example of runtime polymorphism.

---

# 7. What is Abstraction?

Abstraction hides internal implementation details and exposes only essential functionality.

Users interact with features without knowing internal complexity.

---

## Real-World Example

```text
ATM Machine
```

Users:
- insert card
- enter PIN
- withdraw money

They do not know how the banking system internally works.

---

# 8. What is an Abstract Class?

An abstract class is a class that contains abstract methods and acts as a blueprint for child classes.

Abstract classes cannot be instantiated directly.

Python uses:
- `ABC`
- `abstractmethod`

from the `abc` module.

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

## Why Use Abstract Classes?

Abstract classes enforce rules.

They ensure every child class implements required methods.

This creates consistency across child classes.

---

# 9. What is an Abstract Method?

An abstract method is a method declared without implementation in the parent class.

Child classes are required to implement it.

---

## Example

```python
@abstractmethod
def start(self):
    pass
```

---

## Why Use Abstract Methods?

They define a common interface for all child classes.

For example:

```text
Every vehicle must start()
Every vehicle must stop()
```

but implementation may differ.

---

# 10. Why Do We Inherit from ABC?

`ABC` converts a normal class into an abstract class.

Without inheriting from `ABC`, Python will not properly enforce abstract method implementation.

---

# 11. Difference Between Inheritance and Composition

## Inheritance

Represents:

```text
IS-A
```

relationship.

Example:

```text
Dog IS-A Animal
```

---

## Composition

Represents:

```text
HAS-A
```

relationship.

Example:

```text
ShoppingCart HAS-A Products
Car HAS-A Engine
```

---

## Why Composition is Important

Many beginners overuse inheritance.

Composition often creates:
- more flexible designs
- lower coupling
- easier maintenance

---

# 12. Difference Between Overriding and Overloading

## Method Overriding

- occurs in parent-child classes
- same method name
- different implementation

---

## Method Overloading

- same method name
- different parameters

Python has limited support for traditional method overloading.

---

# 13. What is Encapsulation?

Encapsulation means combining:
- data
- methods

inside a class.

It helps protect object data and organize behavior logically.

---

## Example

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance
```

The balance belongs to the object itself.

---

# 14. What is self in Python?

`self` refers to the current object of the class.

It is used to:
- access instance variables
- access instance methods

---

## Example

```python
self.name
self.display()
```

Without `self`, object-specific data cannot be accessed properly.

---

# 15. Why Are Classes Important?

Classes help organize code into reusable objects.

Without classes:
- programs become repetitive
- data and behavior become disconnected
- large projects become difficult to maintain

Classes improve:
- structure
- scalability
- readability

---

# 16. Common Beginner Mistakes in OOP

## 1. Using inheritance everywhere

Not every relationship requires inheritance.

---

## 2. Confusing class variables and instance variables

```python
products = []
```

inside class body creates shared state.

---

## 3. Writing procedural code inside classes

Some beginners create classes but still write everything inside one large method.

---

## 4. Ignoring object relationships

Example mistake:

```text
ShoppingCart inherits Product
```

This is logically incorrect.

---

# 17. When Should Inheritance Be Avoided?

Inheritance should be avoided when:
- relationships are weak
- classes are unrelated
- code reuse is forced artificially

In such cases, composition is usually better.

---

# 18. Why is Polymorphism Better Than Large if-else Blocks?

Without polymorphism:

```python
if vehicle == "car":
    ...
elif vehicle == "bike":
    ...
```

Programs become harder to maintain.

Polymorphism removes unnecessary condition chains and makes systems easier to extend.

---

# 19. What Happens If a Child Class Does Not Implement Abstract Methods?

Python raises an error during object creation.

Example:

```text
TypeError:
Can't instantiate abstract class
```

because required methods are missing.

---

# 20. Explain Advanced OOP in One Line

Advanced OOP combines:
- inheritance
- overriding
- polymorphism
- abstraction

to create reusable, scalable, and organized software systems.