from collections import UserDict
import re


class Field:
    @staticmethod
    def check_number(number: list):
        for item in number:
            result = re.search(r'\+?380\d+|0\d+', item)
            if result:
                if len(item) != len(result.group()):
                    print('Incorrect number')
                    return []
            else:
                res = re.search(r'\w+@\w+\.\w+', item)
                if not res:
                    print('It`s not number or email. Please try again!')
                    number.remove(item)
        return number

    @staticmethod
    def check_name(name: str):
        if not name.isalpha():
            print('Enter correct name')
            return None
        return name


class Phone(Field):
    def __init__(self, phone: list):
        self.phone = Field.check_number(phone)

    def __str__(self):
        return f'{self.phone}'


class Name(Field):
    def __init__(self, name):
        self.name = Field.check_name(name)

    def __str__(self):
        return f'{self.name}'


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)

    def __str__(self):
        return f'{self.name},{self.phone}'


class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.__str__()] = rec.__str__()
        if 'None' in self.data.keys():
            self.data.pop('None')

    def change_phone(self, rec):
        self.data[rec.name.__str__()] = rec.__str__()

    def find_phone(self, name):
        if name in self.data.keys():
            value = self.data[name]
            res = re.search(r'\+?\d+', value)
            return res.group()
        return 'Does not exist in database!'


def main():
    main_address_book = AddressBook()
    while True:
        command = input('Command: ').lower()
        sep_val = command.split(' ')
        if sep_val[0] == 'add' and len(sep_val) > 2:
            main_address_book.add_record(Record(sep_val[1].title(), sep_val[2:]))
        elif sep_val[0] == 'change' and len(sep_val) > 2:
            main_address_book.change_phone(Record(sep_val[1].title(), sep_val[2:]))
        elif sep_val[0] == 'phone':
            print(main_address_book.find_phone(sep_val[1].title()))
        elif sep_val[0] == 'show' and sep_val[1] == 'all':
            print(main_address_book)
        elif sep_val[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_val[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')
            


if __name__ == '__main__':
    main()