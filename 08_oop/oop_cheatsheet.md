# OOP Cheat Sheet

## Class

A class is a blueprint for creating objects.

```python
class Student:
    pass
```

---

## Object

An object is an instance of a class.

```python
student1 = Student()
```

---

## Constructor

The `__init__()` method is automatically called when an object is created.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## self

`self` refers to the current object.

```python
self.name = name
```

---

## Instance Variable

Belongs to a specific object.

```python
self.name = "Rahul"
```

---

## Class Variable

Shared among all objects.

```python
class Student:
    school = "ABC School"
```

---

## Instance Method

A method that works with object data.

```python
def display(self):
    print(self.name)
```

---

## Encapsulation

Restricting direct access to data.

```python
self.__balance = 10000
```

---

## Access Modifiers

### Public

```python
self.name = "Rahul"
```

### Protected

```python
self._salary = 50000
```

### Private

```python
self.__balance = 10000
```

---

## Object Creation

```python
student1 = Student("Rahul")
```

---

## Common Syntax

```python
object.attribute
object.method()
```