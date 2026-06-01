# Lambda functions are short anonymous functions written in one line.


# Normal function
def square(number):
    return number * number


print(square(4))


# Lambda function
square_lambda = lambda number: number * number

print(square_lambda(4))


# Lambda function with multiple parameters
add = lambda a, b: a + b

print(add(10, 5))

# Lambda Function with default parameter
sign_up = lambda name="Guest": f"Welcome {name}"


print(sign_up())
print(sign_up("Rahul"))