# Dictionary stores data as key-value pairs

# Real-world example: product details
product = {
    "id": 101,
    "name": "Wireless Mouse",
    "price": 799.50,
    "in_stock": True,
    "brand": "Logitech"
}

print("\n--- Product Details ---")
print(product)

# Access values using keys
print("\n--- Accessing Values ---")
print("Product Name :", product["name"])
print("Product Price:", product["price"])

# get() avoids KeyError if key is missing
print("\n--- Using get() ---")
print("Brand :", product.get("brand"))
print("Color :", product.get("color"))

# Add new key-value pair
product["color"] = "Black"

# Update existing value
product["price"] = 749.00

print("\n--- After Add & Update ---")
print(product)

# Remove a key-value pair
product.pop("in_stock")

print("\n--- After Removing in_stock ---")
print(product)

# keys() returns all keys
print("\n--- Dictionary Keys ---")
print(product.keys())

# values() returns all values
print("\n--- Dictionary Values ---")
print(product.values())

# items() returns key-value pairs
print("\n--- Dictionary Items ---")
print(product.items())

# Loop through dictionary
print("\n--- Looping Through Dictionary ---")

for key, value in product.items():
    print(f"{key} : {value}")

# Check if key exists
print("\n--- Checking Key ---")

if "price" in product:
    print("Price key exists")

# len() returns number of items
print("\n--- Total Items ---")
print(len(product))