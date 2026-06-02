# Nested List Example

# 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Complete Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nElement 5:")
print(matrix[1][1])

print("\nUsing Loops:")

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()