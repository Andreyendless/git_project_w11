from models.note import Note
from models.task import Task
from models.contact import Contact
from models.finance import Finance
from utils.file_utils import export_to_csv, import_from_csv
from utils.validation import validate_date, validate_email
from utils.calculator import calculate
from datetime import datetime

def main_menu():
    print('')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Управление финансовыми записями")
    print("5. Калькулятор")
    print("6. Выход")

def notes_menu():
    print('')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Управление заметками:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Экспорт заметок в CSV")
    print("6. Импорт заметок из CSV")
    print("7. Назад")

def tasks_menu():
    print('')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Управление задачами:")
    print("1. Добавить новую задачу")
    print("2. Просмотреть задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Редактировать задачу")
    print("5. Удалить задачу")
    print("6. Экспорт задач в CSV")
    print("7. Импорт задач из CSV")
    print("8. Назад")

def contacts_menu():
    print('')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Управление контактами:")
    print("1. Добавить новый контакт")
    print("2. Поиск контакта")
    print("3. Редактировать контакт")
    print("4. Удалить контакт")
    print("5. Экспорт контактов в CSV")
    print("6. Импорт контактов из CSV")
    print("7. Назад")

def finance_menu():
    print('')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Управление финансовыми записями:")
    print("1. Добавить новую запись")
    print("2. Просмотреть все записи")
    print("3. Генерация отчёта")
    print("4. Удалить запись")
    print("5. Экспорт финансовых записей в CSV")
    print("6. Импорт финансовых записей из CSV")
    print("7. Назад")

def main():
    while True:
        main_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            notes_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                title = input("Введите название заметки: ")
                content = input("Введите содержание заметки: ")
                notes = Note.load_notes()
                notes.append(Note(title, content))
                Note.save_notes(notes)
                print("Заметка успешно добавлена!")
            elif choice == "2":
                notes = Note.load_notes()
                for note in notes:
                    print(note)
            elif choice == "3":
                notes = Note.load_notes()
                for i, note in enumerate(notes):
                    print(f"{i+1}. {note.title}")
                index = int(input("Введите номер заметки для редактирования: ")) - 1
                title = input("Введите новое название заметки: ")
                content = input("Введите новое содержание заметки: ")
                notes[index].title = title
                notes[index].content = content
                Note.save_notes(notes)
                print("Заметка успешно отредактирована!")
            elif choice == "4":
                notes = Note.load_notes()
                for i, note in enumerate(notes):
                    print(f"{i+1}. {note.title}")
                index = int(input("Введите номер заметки для удаления: ")) - 1
                del notes[index]
                Note.save_notes(notes)
                print("Заметка успешно удалена!")
            elif choice == "5":
                notes = Note.load_notes()
                export_to_csv('data/notes_export.csv', [{'title': note.title, 'content': note.content} for note in notes], ['title', 'content'])
                print("Заметки успешно экспортированы в CSV-файл.")
            elif choice == "6":
                filename = input("Введите имя CSV-файла для импорта: ")
                imported_notes = import_from_csv(filename)
                notes = Note.load_notes()
                notes.extend([Note(note['title'], note['content']) for note in imported_notes])
                Note.save_notes(notes)
                print("Заметки успешно импортированы из CSV-файла.")
            elif choice == "7":
                continue

        elif choice == "2":
            tasks_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                priority = input("Выберите приоритет (Высокий/Средний/Низкий): ")
                due_date = input("Введите срок выполнения (в формате ДД-ММ-ГГГГ): ")
                if not validate_date(due_date):
                    print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
                    continue
                tasks = Task.load_tasks()
                tasks.append(Task(title, description, priority, due_date))
                Task.save_tasks(tasks)
                print("Задача успешно добавлена!")
            elif choice == "2":
                tasks = Task.load_tasks()
                for task in tasks:
                    print(task)
            elif choice == "3":
                tasks = Task.load_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.title}")
                index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                tasks[index].mark_as_completed()
                Task.save_tasks(tasks)
                print("Задача успешно отмечена как выполненная!")
            elif choice == "4":
                tasks = Task.load_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.title}")
                index = int(input("Введите номер задачи для редактирования: ")) - 1
                title = input("Введите новое название задачи: ")
                description = input("Введите новое описание задачи: ")
                priority = input("Выберите новый приоритет (Высокий/Средний/Низкий): ")
                due_date = input("Введите новый срок выполнения (в формате ДД-ММ-ГГГГ): ")
                if not validate_date(due_date):
                    print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
                    continue
                tasks[index].title = title
                tasks[index].description = description
                tasks[index].priority = priority
                tasks[index].due_date = datetime.strptime(due_date, '%d-%m-%Y')
                Task.save_tasks(tasks)
                print("Задача успешно отредактирована!")
            elif choice == "5":
                tasks = Task.load_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.title}")
                index = int(input("Введите номер задачи для удаления: ")) - 1
                del tasks[index]
                Task.save_tasks(tasks)
                print("Задача успешно удалена!")
            elif choice == "6":
                tasks = Task.load_tasks()
                export_to_csv('data/tasks_export.csv', [{'title': task.title, 'description': task.description, 'priority': task.priority, 'due_date': task.due_date.strftime('%d-%m-%Y'), 'completed': task.completed} for task in tasks], ['title', 'description', 'priority', 'due_date', 'completed'])
                print("Задачи успешно экспортированы в CSV-файл.")
            elif choice == "7":
                filename = input("Введите имя CSV-файла для импорта: ")
                imported_tasks = import_from_csv(filename)
                tasks = Task.load_tasks()
                tasks.extend([Task(task['title'], task['description'], task['priority'], task['due_date']) for task in imported_tasks])
                Task.save_tasks(tasks)
                print("Задачи успешно импортированы из CSV-файла.")
            elif choice == "8":
                continue

        elif choice == "3":
            contacts_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                name = input("Введите имя контакта: ")
                phone = input("Введите телефон контакта: ")
                email = input("Введите email контакта: ")
                if not validate_email(email):
                    print("Некорректный email. Пожалуйста, введите корректный email.")
                    continue
                contacts = Contact.load_contacts()
                contacts.append(Contact(name, phone, email))
                Contact.save_contacts(contacts)
                print("Контакт успешно добавлен!")
            elif choice == "2":
                contacts = Contact.load_contacts()
                for contact in contacts:
                    print(contact)
            elif choice == "3":
                contacts = Contact.load_contacts()
                for i, contact in enumerate(contacts):
                    print(f"{i+1}. {contact.name}")
                index = int(input("Введите номер контакта для редактирования: ")) - 1
                name = input("Введите новое имя контакта: ")
                phone = input("Введите новый телефон контакта: ")
                email = input("Введите новый email контакта: ")
                if not validate_email(email):
                    print("Некорректный email. Пожалуйста, введите корректный email.")
                    continue
                contacts[index].name = name
                contacts[index].phone = phone
                contacts[index].email = email
                Contact.save_contacts(contacts)
                print("Контакт успешно отредактирован!")
            elif choice == "4":
                contacts = Contact.load_contacts()
                for i, contact in enumerate(contacts):
                    print(f"{i+1}. {contact.name}")
                index = int(input("Введите номер контакта для удаления: ")) - 1
                del contacts[index]
                Contact.save_contacts(contacts)
                print("Контакт успешно удален!")
            elif choice == "5":
                contacts = Contact.load_contacts()
                export_to_csv('data/contacts_export.csv', [{'name': contact.name, 'phone': contact.phone, 'email': contact.email} for contact in contacts], ['name', 'phone', 'email'])
                print("Контакты успешно экспортированы в CSV-файл.")
            elif choice == "6":
                filename = input("Введите имя CSV-файла для импорта: ")
                imported_contacts = import_from_csv(filename)
                contacts = Contact.load_contacts()
                contacts.extend([Contact(contact['name'], contact['phone'], contact['email']) for contact in imported_contacts])
                Contact.save_contacts(contacts)
                print("Контакты успешно импортированы из CSV-файла.")
            elif choice == "7":
                continue
        
        elif choice == "4":
            finance_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                date = input("Введите дату (в формате ДД-ММ-ГГГГ): ")
                if not validate_date(date):
                    print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
                    continue
                income = float(input("Введите доход: "))
                expense = float(input("Введите расход: "))
                finances = Finance.load_finances()
                finances.append(Finance(date, income, expense))
                Finance.save_finances(finances)
                print("Финансовая запись успешно добавлена!")
            elif choice == "2":
                finances = Finance.load_finances()
                for finance in finances:
                    print(finance)
            elif choice == "3":
                start_date = input("Введите начальную дату (в формате ДД-ММ-ГГГГ): ")
                if not validate_date(start_date):
                    print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
                    continue
                end_date = input("Введите конечную дату (в формате ДД-ММ-ГГГГ): ")
                if not validate_date(end_date):
                    print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
                    continue
                start_date = datetime.strptime(start_date, '%d-%m-%Y')
                end_date = datetime.strptime(end_date, '%d-%m-%Y')
                finances = Finance.load_finances()
                filtered_finances = [finance for finance in finances if start_date <= finance.date <= end_date]
                total_income = sum(finance.income for finance in filtered_finances)
                total_expense = sum(finance.expense for finance in filtered_finances)
                balance = total_income - total_expense
                print(f"Финансовый отчёт за период с {start_date.strftime('%d-%m-%Y')} по {end_date.strftime('%d-%m-%Y')}:")
                print(f"Общий доход: {total_income} руб.")
                print(f"Общие расходы: {total_expense} руб.")
                print(f"Баланс: {balance} руб.")
                export_to_csv(f'data/report_{start_date.strftime("%d-%m-%Y")}_{end_date.strftime("%d-%m-%Y")}.csv', [{'date': finance.date.strftime('%d-%m-%Y'), 'income': finance.income, 'expense': finance.expense} for finance in filtered_finances], ['date', 'income', 'expense'])
                print(f"Подробная информация сохранена в файле report_{start_date.strftime('%d-%m-%Y')}_{end_date.strftime('%d-%m-%Y')}.csv")
            elif choice == "4":
                finances = Finance.load_finances()
                for i, finance in enumerate(finances):
                    print(f"{i+1}. {finance.date.strftime('%d-%m-%Y')}")
                index = int(input("Введите номер финансовой записи для удаления: ")) - 1
                del finances[index]
                Finance.save_finances(finances)
                print("Финансовая запись успешно удалена!")
            elif choice == "5":
                finances = Finance.load_finances()
                export_to_csv('data/finance_export.csv', [{'date': finance.date.strftime('%d-%m-%Y'), 'income': finance.income, 'expense': finance.expense} for finance in finances], ['date', 'income', 'expense'])
                print("Финансовые записи успешно экспортированы в CSV-файл.")
            elif choice == "6":
                filename = input("Введите имя CSV-файла для импорта: ")
                imported_finances = import_from_csv(filename)
                finances = Finance.load_finances()
                finances.extend([Finance(finance['date'], finance['income'], finance['expense']) for finance in imported_finances])
                Finance.save_finances(finances)
                print("Финансовые записи успешно импортированы из CSV-файла.")
            elif choice == "7":
                continue
        
        elif choice == "5":
            expression = input("Введите математическое выражение: ")
            result = calculate(expression)
            if result is not None:
                print(f"Результат: {result}")
        
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")

print("Добро пожаловать в Персональный помощник!")
main()