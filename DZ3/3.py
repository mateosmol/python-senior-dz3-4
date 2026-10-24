"""Завдання 3"""
class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self.salary = salary
        self.position = position

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

"""Демонстрація"""
bob = Employee("Bob", 123456789, 1000)
print(bob.get_salary_info())
