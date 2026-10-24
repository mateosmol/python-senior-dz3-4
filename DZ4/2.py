"""Завдання 2"""

class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.name} - {self.price} грн"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.available:
            self.products.append(product)
            print(f"{product.name} added to cart")
        else:
            print(f"{product.name} is not available")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from cart")
        else:
            print("Product not found in cart")

    def total_cost(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        if not self.products:
            print("Cart is empty")
        else:
            for product in self.products:
                print(product)

            print(f"Total cost: {self.total_cost()}")


"""Демонстрація"""

product1 = Product("Milk", 500, True)
product2 = Product("Bread", 500, False)
product3 = Product("Shoes", 1500, True)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.show_cart()
cart.add_product(product3)

cart.show_cart()