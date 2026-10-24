"""Завдання 2"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

"""Демонстрація"""
car1 = Car("Ford", "Mustang", 1999)
print(car1.get_info())
