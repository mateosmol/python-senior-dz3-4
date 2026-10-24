"""Завдання 1"""

class Task():
    def __init__(self, name, description, deadline, state="Not done"):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.state = state

    def __str__(self):
        return f"{self.name} {self.description} {self.deadline} {self.state}"


class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
        else:
            print("Invalid task number")

    def get_tasks(self):
        return self.tasks

    def change_status(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].state = "Done"
            print(
                f"Status of {self.tasks[task_number].name} "
                f"changed to Done"
            )
        else:
            print("Invalid task number")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")


"""Демонстрація"""

manager = TaskManager()

task = Task("Task 1","Task description","Task deadline")

manager.add_task(task)
manager.show_tasks()

manager.change_status(0)
manager.show_tasks()
