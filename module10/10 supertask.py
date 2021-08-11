# Класс AddressBook, который наследуется от UserDict и мы потом добавим логику поиска по записям в этот класс.
# Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
# Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
# Класс Name, обязательное поле с именем.
# Класс Phone, не обязательное поле с телефоном и таких одна запись (Record) может содержать несколько.


from collections import UserDict, UserList, UserString
import re


class Field:
    pass

class Phone(Field):
    def __init__(self, *phone):
        self.phone = list(x for x in phone)

    def phonecheck(self):



    


class AddressBook(UserDict):
    pass






class Record(Field):
    pass


class Name(Field):
    pass

