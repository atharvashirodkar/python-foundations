"""

Topic:
- for loop
- while loop
- break
- continue
- nested loops
- range function

"""


# =========================================
# for loop
# =========================================

print("===== for loop =====")

for i in range(1, 6):
    print("Iteration:", i)


# =========================================
# while loop
# =========================================

print("\n===== while loop =====")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# =========================================
# break statement
# =========================================

print("\n===== break statement =====")

for i in range(1, 11):

    if i == 6:
        print("Loop stopped at:", i)
        break

    print(i)

while True:  # Infinite loop
    password = input("Enter password: ")
    if password == "secret":
        print("User logged in succesfully!")
        break  # Exit loop
    print("Wrong password!")



# =========================================
# continue statement
# =========================================

print("\n===== continue statement =====")

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print("Odd Number:", i)


# =========================================
# nested loops
# =========================================

print("\n===== nested loops =====")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


# =========================================
# range function
# =========================================

print("\n===== range function =====")

# range(stop)              # 0 to stop-1
# range(start, stop)       # start to stop-1
# range(start, stop, step) # start to stop-1, by step


for i in range(5):
    print(i)


for i in range(1, 6):
    print(i)


for i in range(1, 10, 2):
    print(i)


# =========================================
# Multiplication Table
# =========================================

print("\n===== Multiplication Table =====")

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# For loop - when you know iterations
for i in range(5):
    print(i)

# While loop - when condition-based
count = 0
while count < 5:
    print(count)
    count += 1
