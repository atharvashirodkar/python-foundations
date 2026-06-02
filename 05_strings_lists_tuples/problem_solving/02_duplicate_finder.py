# Problem Statement:
# Write a Python program to find and display duplicate elements
# from a given list entered by the user.
#
# Example:
# Input: [1, 2, 3, 2, 4, 1]
# Output: 1, 2


print("Enter number with comma's, such as 1,2,3,4,5")
numbers = list(map(int, input("Enter list with comma: ").split(",")))

print(f"Your list items: {numbers}")

# Method 1:
bucket = []
for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1 and numbers[i] not in bucket:
        bucket.append(numbers[i])

print(f"Duplicate elements: {bucket}")


# Method 2:
sorted_list = sorted(numbers)

duplicates = []

for i in range(len(sorted_list) - 1):

    if sorted_list[i] == sorted_list[i + 1]:

        if sorted_list[i] not in duplicates:
            duplicates.append(sorted_list[i])

print("Duplicate elements:", duplicates)
