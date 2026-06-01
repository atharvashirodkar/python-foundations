"""
Temperature Conversion Formulas:

Celsius to Fahrenheit:
F = (9/5 * C) + 32

Fahrenheit to Celsius:
C = (5/9) * (F - 32)

Kelvin to Celsius:
C = K - 273.15

Celsius to Kelvin:
K = C + 273.15

"""


def celsius_to_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


print("Select a temperature conversion option:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Celsius")
print("4. Celsius to Kelvin")


num = input("Enter your choice (1-4): ")


match num:
    case "1":
        print("Celsius to Fahrenheit:")
        c = float(input("Enter the value: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c} Celsius = {f:.2f} Fahrenheit")
    case "2":
        print("Fahrenheit to Celsius :")
        f = float(input("Enter the value: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f} Fahrenheit = {c:.2f} Celsius")
    case "3":
        print("Kelvin to Celsius :")
        k = float(input("Enter the value: "))
        c = kelvin_to_celsius(k)
        print(f"{k} Kelvin = {c:.2f} Celsius")
    case "4":
        print("Celsius to Kelvin:")
        c = float(input("Enter the value: "))
        k = celsius_to_kelvin(c)
        print(f"{c} Celsius = {k:.2f} Kelvin")

    case _:
        print("Invalid Input")
