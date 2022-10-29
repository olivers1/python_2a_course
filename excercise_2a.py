class Contact:
    def __init__(self, name, number, age):
        self._name = name
        self._number = number
        self._age = age
    
    @property
    def get_age(self):
        return self._age

    @property
    def get_number(self):
        return self._number

    
class PhoneBook(Contact):
    def __init__(self):
        self._contacts = []

    def add_contact(self, contact: Contact):
        if contact in self._contacts:
            pass

