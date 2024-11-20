import json
import csv

def load_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON-файла.")
        return []

def save_json(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Ошибка при записи в JSON-файл: {e}")

def export_to_csv(filename, data, headers):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Ошибка при экспорте в CSV-файл: {e}")

def import_from_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при импорте из CSV-файла: {e}")
        return []