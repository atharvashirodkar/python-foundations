class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product=None):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"{product.product_name} added to cart")
        else:
            print("Please provide a valid product")

    def remove_product(self, product_name):
        if not self.products:
            print("Cart is empty")
            return

        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart")
                return

        print("Product not found")

    def display_cart(self):
        if not self.products:
            print("Cart is empty")
            return

        print("Products in Cart")
        print("----------------")
        for product in self.products:
            print(f"{product.product_name}  : ₹{product.price}")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        print(f"Total Amount: {total}")


# Create Product Objects

product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)
product3 = Product("Keyboard", 2000)


# Create Shopping Cart Object

cart = ShoppingCart()


# Add Products

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print()


# Display Cart

cart.display_cart()

print()


# Remove Product

cart.remove_product("Mouse")

print()


# Display Updated Cart

cart.display_cart()


# Calculate Total

cart.calculate_total()
