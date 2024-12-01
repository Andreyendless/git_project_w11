from utils.file_utils import load_json, save_json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @classmethod
    def load_contacts(cls):
        data = load_json('data/contacts.json')
        return [cls(contact['name'], contact['phone'], contact['email']) for contact in data]

    @classmethod
    def save_contacts(cls, contacts):
        save_json('data/contacts.json', [{'name': contact.name, 'phone': contact.phone, 'email': contact.email} for contact in contacts])

    def __str__(self):
        return f"Контакт: {self.name}\nТелефон: {self.phone}\nEmail: {self.email}"