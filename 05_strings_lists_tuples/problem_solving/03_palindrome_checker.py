# Problem Statement:
# Write a Python program to check whether a given string
# is a palindrome or not.
#
# A palindrome reads the same forward and backward.
#
# Example:
# Input: madam
# Output: Palindrome

name = input("Enter a string: ")
print(f"Input: {name}")

# Method 1:
# if name == name[::-1]:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")


# Method 2:
is_Palindrome = True

for i in range(len(name) // 2):
    if name[i] != name[-(i+1)]:
        is_Palindrome = False
        break

print(f"Palindrome: {is_Palindrome}")


"""
0 -1
1 -2
2 -3
3 -4
4 -5

equation:

4 - 4*2 - 1
4-8-1 = -5

hence : i - (i*2) - 1
i(1-2)-1
i(-1)-1
-i-1
-(i+1)

"""
