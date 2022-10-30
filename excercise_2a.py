from re import A
from unicodedata import name


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
        for i, item in enumerate(self._contacts):
            if item._name == contact._name:
                self._contacts[i] = contact
                break
        else:
            self._contacts.append(contact)
    
    def get_contact(self, name):
        for item in self._contacts:
            if item._name == name:
                return print("name:", item._name, ", number:", item.get_number, ", age:", item.get_age)
        else:
            print("name is not in the list")
    
    def __len__(self):
        if len(self._contacts) > 0:
            return len(self._contacts)
        else:
            print("list is empty")


name_list = ["oliver", "jens", "ola", "oliver"]
numb_list = [860612, 891210, 921009, 121212]
age_list = [36, 32, 28, 12]

pbook = PhoneBook()

for i in range(0, 4):
    pbook.add_contact(Contact(name_list[i], numb_list[i], age_list[i]))


for i in pbook._contacts:
    if i._name == "ola":
        print(i._name)


print(pbook.__len__())
pbook.get_contact("ola")