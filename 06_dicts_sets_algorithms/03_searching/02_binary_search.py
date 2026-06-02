# Binary search works only on sorted lists

numbers = [45, 12, 78, 23, 56, 89]

target = 23

print("\n--- Number List ---")
print(numbers)

print("\n--- Sorted Number List ---")
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("\nSearching for :", target)

def binary_search(list, target):
    left = 0
    right = len(list)

    while left <= right:
        mid = (left + right)//2

        print(f"\nLeft: {left}, Right: {right}")
        print(f"mid: {mid} -> {list[mid]}")

        if target > list[mid]:
            left = mid + 1
        elif target < list[mid]:
            right = mid - 1
        else:
            return "Target Found"
    return "Target Not Found"

result = binary_search(sorted_numbers, target)
print(result)