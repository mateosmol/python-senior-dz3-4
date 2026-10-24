"""Завдання 4"""
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2*(self.width + self.height)

"""Демонстрація"""
rect = Rectangle(50, 100)
print(rect.calculate_area())
print(rect.calculate_perimeter())