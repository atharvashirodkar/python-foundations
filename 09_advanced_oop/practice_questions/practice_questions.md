# Practice Questions - Session 09: Advanced OOP

## Question 1: Student Inheritance

Create a parent class `Person` with the following:

### Attributes
- `name`
- `age`

### Methods
- `display_info()`

Create a child class `Student` that inherits from `Person`.

### Additional Attribute
- `course`

### Additional Method
- `show_course()`

### Expected Output

```text
Student Details
----------------
Name   : Rahul
Age    : 20
Course : Python Programming
```

---

## Question 2: Multilevel Inheritance

Create the following class hierarchy:

```text
Animal
   ↓
Dog
   ↓
Puppy
```

### Methods

#### Animal
- `eat()`

#### Dog
- `bark()`

#### Puppy
- `weep()`

### Expected Output

```text
Animal can eat
Dog can bark
Puppy can weep
```

---

## Question 3: Method Overriding

Create a parent class `Animal`.

### Method
- `sound()`

Create child classes:
- `Dog`
- `Cat`

Override the `sound()` method in both child classes.

### Expected Output

```text
Dog barks
Cat meows
```

---

## Question 4: Method Overriding with super()

Create a parent class `Employee`.

### Method
- `work()`

Display:

```text
Employee works
```

Create a child class `Developer`.

Override the `work()` method and use `super()` to call the parent method first.

### Expected Output

```text
Employee works
Developer writes code
```

---

## Question 5: Polymorphism

Create the following classes:

- `Dog`
- `Cat`
- `Cow`

Each class should contain a method:

- `sound()`

Store all objects inside a list and use a loop to call the method.

### Expected Output

```text
Dog barks
Cat meows
Cow moos
```

---

## Question 6: Vehicle Polymorphism

Create the following classes:

- `Car`
- `Plane`
- `Boat`

Each class should contain:

- `move()`

### Expected Output

```text
Car is moving
Plane is flying
Boat is sailing
```

Use a list and loop to demonstrate polymorphism.

---

## Question 7: Vehicle Abstraction

Create an abstract class `Vehicle`.

### Abstract Methods
- `start()`
- `stop()`

Create child classes:

- `Car`
- `Bike`

Implement all abstract methods.

### Expected Output

```text
Car engine started
Car engine stopped

Bike started
Bike stopped
```

---

## Question 8: Shape Abstraction

Create an abstract class `Shape`.

### Abstract Method
- `calculate_area()`

Create the following child classes:

- `Rectangle`
- `Circle`

Implement area calculation for both shapes.

### Expected Output

```text
Rectangle Area: 50
Circle Area: 78.5
```