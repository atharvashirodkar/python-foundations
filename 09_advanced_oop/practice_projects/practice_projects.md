# Practice Projects - Session 09: Advanced OOP

## Project 1: Employee Management System

Create a base class `Employee`.

### Constructor Attributes
- `emp_id`
- `name`
- `salary`

### Methods
- `display_details()`

The `display_details()` method should print employee information.

---

Create two child classes:

- `Developer`
- `Manager`

Both classes must inherit from `Employee`.

---

### Developer Class Requirements

#### Additional Attribute
- `programming_language`

#### Requirements
- Override the `display_details()` method.
- Use `super()` to display common employee details.
- Add developer-specific information.

---

### Manager Class Requirements

#### Additional Attribute
- `team_size`

#### Requirements
- Override the `display_details()` method.
- Use `super()` to display common employee details.
- Add manager-specific information.

---

### Object Creation

Create:
- one `Developer` object
- one `Manager` object

Call the `display_details()` method for both objects.

---

### Expected Output

```text
Developer Details
-----------------
ID       : 101
Name     : Rahul
Salary   : 50000
Role     : Developer
Language : Python

Manager Details
---------------
ID        : 201
Name      : Priya
Salary    : 80000
Role      : Manager
Team Size : 10
```

---

# Project 2: Shopping Cart System

Create a class `Product`.

### Constructor Attributes
- `product_name`
- `price`

---

Create a class `ShoppingCart`.

### Requirements
- Store multiple `Product` objects inside a list.
- The cart should initially be empty.

---

### Methods

#### add_product(product)
- Accept a `Product` object as parameter.
- Add the product to the cart.

---

#### remove_product(product_name)
- Remove a product using its name.
- If the product is not found, display:

```text
Product not found
```

---

#### display_cart()
Display all products in the cart using the format:

```text
Products in Cart
----------------
Laptop  : ₹50000
Mouse   : ₹1000
```

---

#### calculate_total()
- Calculate the total price of all products.
- Display the total amount.

---

### Object Creation

Create at least:
- 2 product objects
- 1 shopping cart object

Add products to the cart and display the final bill.

---

### Expected Output

```text
Products in Cart
----------------
Laptop  : ₹50000
Mouse   : ₹1000

Total Amount: ₹51000
```

---

# Project 3: Vehicle Management System

Import:
- `ABC`
- `abstractmethod`

from the `abc` module.

---

Create an abstract class `Vehicle`.

### Abstract Methods
- `start()`
- `stop()`

Both methods should contain only:

```python
pass
```

---

Create child classes:

- `Car`
- `Bike`
- `Truck`

Each class must:
- inherit from `Vehicle`
- implement both abstract methods

---

### Method Output

#### Car

```text
Car started
Car stopped
```

#### Bike

```text
Bike started
Bike stopped
```

#### Truck

```text
Truck started
Truck stopped
```

---

### Polymorphism Requirement

Store all vehicle objects inside a list.

Use a loop to call:
- `start()`
- `stop()`

for every object.

---

### Object Creation

Create:
- one `Car` object
- one `Bike` object
- one `Truck` object

Store them in a list and demonstrate polymorphism.

---

### Expected Output

```text
Car started
Car stopped

Bike started
Bike stopped

Truck started
Truck stopped
```