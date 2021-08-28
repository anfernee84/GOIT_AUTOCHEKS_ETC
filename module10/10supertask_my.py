from collections import UserDict
import re

class Field:
    @staticmethod
    def checknum(data:list):
        for item in data:
            phonenum = re.search(r'\+?380\d+|0\d+', item)
            if phonenum:
                if len(item) != len(phonenum.group()):
                    print (f"Number {phonenum} is not correct. Try again...")
                    return []
            else:
                email = re.search(r'[a-zA-Z\.-]+@[\w\.-]+', item)
                if not email:
                    print(f"Email {email} is not correct. Try again...")
                    data.remove(item)
        return data

    @staticmethod
    def checkname(name:str):
        if name.isalpha():
            return name
        print('Enter correct name')
        return None




class Phone(Field):

    def __init__(self, phonenum:list):
        self.phonenum = Field.checknum(phonenum)

    def __str__(self):    
        return f"{self.phonenum}"

class Name(Field):
    def __init__(self,name):
        self.name = Field.checkname(name)

    def __str__(self):   
        return f"{self.name}"



class Record:
    def __init__(self, name, phonenum):
        self.name = Name(name)
        self.phonenum = Phone(phonenum)
    
    def __str__(self):
        return f"{self.name}, {self.phonenum}"

class AddMailBook(UserDict):
    def add_change_record(self,record):
        self.data[record.name.__str__()] = record.__str__()
        if "None" in self.data.keys():
            self.data.pop("None")

    def find_phone(self,name):
        if name in self.data.keys():
            value = self.data[name]
            email = re.search(r'\+?\d+', value)
            return email.group()
        return ("No email in DB")


def main():
    main_book = AddMailBook()
    while True:
        ask = input("What the hell do you want?: ")
        ask = ask.lower()
        splits = ask.split(" ")
        if splits[0] in ["good","close", ".", "exit"]:
            print ("Good bye")
            break
        elif splits[0] in ["hello"]:
            print ("How can i help you?")
        elif splits[0] in ["show"]:
            print(main_book)
        elif splits[0] in ["phone"]:
            print(main_book.find_phone(splits[1].title()))
        elif splits[0] in ["add"] or ["change"] and len(splits)>2:
            main_book.add_change_record(Record(splits[1].title(), splits[2:]))
        else:
            print ("Input incorrect. Try again...")

if __name__ == "__main__":
    main()

