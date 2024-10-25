class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.name}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        new_task = Task(name)
        self.tasks.append(new_task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task index.")


