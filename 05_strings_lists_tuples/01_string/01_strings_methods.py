"""
STRING METHODS IN PYTHON

Strings are immutable:
Once created, a string cannot be modified directly.
Any operation that changes a string creates a new string instead.
"""

# =========================================================
# BASIC STRINGS
# =========================================================

sentence1 = (
    "I forgot my charger at home, so my phone died "
    "halfway through the train ride."
)

sentence2 = "The coffee went cold."


# =========================================================
# CONCATENATION
# =========================================================

# Joining strings using +

combined = sentence2 + " " + sentence1
print(combined)


# =========================================================
# TYPE CONVERSION
# =========================================================

# Strings and numbers cannot be concatenated directly

age = 25
print("Age:", age)
print("Age: " + str(age))


# =========================================================
# STRING REPETITION
# =========================================================

print("Hello " * 3)


# =========================================================
# LENGTH OF A STRING
# =========================================================

print(len(sentence1))


# =========================================================
# CASE CONVERSION
# =========================================================

print(sentence2.upper())
print(sentence2.lower())


# =========================================================
# REMOVING WHITESPACE
# =========================================================

text = "   The lights flickered once   "

print(text)
print(text.strip())


# =========================================================
# REPLACING TEXT
# =========================================================

sentence3 = sentence2.replace("coffee", "tea")

print(sentence2)
print(sentence3)


# =========================================================
# CHECKING STRING CONTENT
# =========================================================

# startswith()

print(sentence1.startswith("Th"))
print(sentence1.startswith("I"))

# endswith()

print(sentence1.endswith("ride."))

# membership operator

print("the" in sentence1)


# =========================================================
# F-STRINGS
# =========================================================

name = "Alice"
age = 25

message = f"Hello, {name}! You are {age} years old."

print(message)


# =========================================================
# NUMBER FORMATTING
# =========================================================

# Decimal places

pi = 3.14159265
print(f"Pi: {pi:.2f}")

# Width and alignment

num = 42
print(f"{num:5}")

# Thousands separator

big_num = 1_000_000
print(f"{big_num:,}")