"""Завдання 5"""
class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return f"Загальна ціна: {self.price * self.quantity}"

    def display_info(self):
        return f"Інформація про товар {self.name}: Ціна {self.price}, Кількість: {self.quantity}"

"""Демонстрація"""
prod = Product("Milk", 50, 20)
print(prod.display_info())
print(prod.calculate_total_price())
