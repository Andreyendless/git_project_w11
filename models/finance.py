from utils.file_utils import load_json, save_json
from datetime import datetime

class Finance:
    def __init__(self, date, income, expense):
        self.date = datetime.strptime(date, '%d-%m-%Y')
        self.income = income
        self.expense = expense

    @classmethod
    def load_finances(cls):
        data = load_json('data/finance.json')
        return [cls(finance['date'], finance['income'], finance['expense']) for finance in data]

    @classmethod
    def save_finances(cls, finances):
        save_json('data/finance.json', [{'date': finance.date.strftime('%d-%m-%Y'), 'income': finance.income, 'expense': finance.expense} for finance in finances])

    def __str__(self):
        return f"Дата: {self.date.strftime('%d-%m-%Y')}\nДоход: {self.income} руб.\nРасход: {self.expense} руб."