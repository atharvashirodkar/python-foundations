a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a > b:
    if a > c:
        print(f"{a} is greater")
    else:
        print(f"{c} is greater")
else:
    if b > c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")