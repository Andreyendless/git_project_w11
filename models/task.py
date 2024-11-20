from utils.file_utils import load_json, save_json
from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = datetime.strptime(due_date, '%d-%m-%Y')
        self.completed = False

    @classmethod
    def load_tasks(cls):
        data = load_json('data/tasks.json')
        return [cls(task['title'], task['description'], task['priority'], task['due_date']) for task in data]

    @classmethod
    def save_tasks(cls, tasks):
        save_json('data/tasks.json', [{'title': task.title, 'description': task.description, 'priority': task.priority, 'due_date': task.due_date.strftime('%d-%m-%Y'), 'completed': task.completed} for task in tasks])

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнена" if self.completed else "Не выполнена"
        return f"Задача: {self.title}\nОписание: {self.description}\nПриоритет: {self.priority}\nСрок выполнения: {self.due_date.strftime('%d-%m-%Y')}\nСтатус: {status}"