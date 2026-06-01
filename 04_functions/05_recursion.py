# Recursion is when a function calls itself to solve a problem.


# Recursive function example
def reverse_num(number):

    # Base case
    if number == 0:
        print("Done!")
        return

    print(number)

    # Function calling itself
    reverse_num(number - 1)


reverse_num(5)