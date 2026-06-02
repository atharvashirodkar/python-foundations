"""
STRING SLICING IN PYTHON

Slicing allows you to extract parts of a string
using index positions.

Syntax:
string[start : stop : step]

- start -> index to begin from
- stop  -> index to stop before
- step  -> jump interval
"""

# =========================================================
# BASIC STRING
# =========================================================

text = "Python Programming"

print("Original String:", text)


# =========================================================
# ACCESSING CHARACTERS USING INDEXES
# =========================================================

# Positive indexing starts from the left

print("First character:", text[0])
print("Second character:", text[1])

# Negative indexing starts from the right

print("Last character:", text[-1])
print("Second last character:", text[-2])


# =========================================================
# BASIC SLICING
# =========================================================

# Extract characters from index 0 to 5
# (stop index is excluded)

print("text[0:6]  ->", text[0:6])

# From beginning to a position

print("text[:6]   ->", text[:6])

# From a position to the end

print("text[7:]   ->", text[7:])


# =========================================================
# SLICING WITH STEP
# =========================================================

# Every second character

print("text[::2]  ->", text[::2])

# Every third character

print("text[::3]  ->", text[::3])


# =========================================================
# REVERSE STRING
# =========================================================

# Negative step reverses the string

print("Reversed:", text[::-1])


# =========================================================
# NEGATIVE INDEX SLICING
# =========================================================

# Extract using negative indexes

print("text[-11:-1] ->", text[-11:-1])


# =========================================================
# IMMUTABILITY EXAMPLE
# =========================================================

# Strings cannot be modified directly

word = "Hello"

# This would cause an error:
# word[0] = "Y"

# Create a new string instead

new_word = "Y" + word[1:]

print("Original word:", word)
print("Modified word:", new_word)


# =========================================================
# COMMON MISTAKES
# =========================================================

# stop index is excluded

print("text[0:4] ->", text[0:4])

# IndexError happens with invalid indexes

# print(text[100])   # Error


# =========================================================
# USEFUL TRICKS
# =========================================================

# Copy entire string

print("Copy:", text[:])

# Last 3 characters

print("Last 3 characters:", text[-3:])

# Remove first character

print("Without first character:", text[1:])

# Remove last character

print("Without last character:", text[:-1])