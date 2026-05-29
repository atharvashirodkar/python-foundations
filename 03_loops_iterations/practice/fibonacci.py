# Fibonacci Series: 
# 0 1 1 2 3 5 8 13 ...

a = 0
b = 1

iteration = 15

print(a,b, end=" ")

for i in range(iteration):
    result = a + b
    print(result, end=" ")
    a = b
    b = result