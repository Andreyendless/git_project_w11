import json
from utils.file_utils import load_json, save_json

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def load_notes(cls):
        data = load_json('data/notes.json')
        return [cls(note['title'], note['content']) for note in data]

    @classmethod
    def save_notes(cls, notes):
        save_json('data/notes.json', [{'title': note.title, 'content': note.content} for note in notes])

    def __str__(self):
        return f"Заметка: {self.title}\nСодержание: {self.content}"
    