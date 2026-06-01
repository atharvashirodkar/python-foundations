# Parameter: A variable defined in a function declaration.
# Argument: The actual value passed to a function when calling it.

# Function with one parameter
# Here 'name' is a parameter
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")


# Function with multiple parameters
# Here 'a' and 'b' are the parameters
def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 5)
add_numbers(7, 3)



# Function with default parameter
def sign_up(name="Guest"):
    print(f"Welcome {name}")


sign_up()
sign_up("Rahul")


