# Linear search checks elements one by one

numbers = [45, 12, 78, 24, 56, 89]

target = 23

print("\n--- Number List ---")
print(numbers)

print("\nSearching for :", target)

# Method 1:

# def linear_search(list, target):
#     for i in list:
#         if i == target:
#             return True
#         else: return False


# method 2
def linear_search(list, target):
    for index, value in enumerate(list):
        print(f"Index: {index} -> {value}")

    if value == target:
        print(f"\nTarget found at index {index}")
        return True
    return False

found = linear_search(numbers, target)

print(f"Target value found: {found}")