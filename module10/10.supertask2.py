from collections import UserDict
import re

class Field:
    @staticmethod
    def checkingnum (num:list):
        for item in num:
            phonenum = re.search(r'\+?380\d+|0\d+', item)
            if phonenum:
                if len(item) != len(phonenum.group()):
                    print("Number isn`t correct")
                    return []
            else:
                email = re.search(r'[a-zA-Z\.-]+@[\w\.-]+', item)
                if not email:
                    print("email isn`t correct")
                    num.remove(item)
        return num
    @staticmethod
    def checkingname (name:str):
        if name.isalpha():
            return name
        print('Enter correct name')
        return None


class Phone(Field):
    

    def __init__(self, phone:list):
        self.phone = Field.checkingnum(phone)

    def __str__(self):
        return f"{self.phone}"


class Name(Field):
    
    def __init__(self, name):
        self.name = Field.checkingname(name)

    def __str__(self):
        return f"{self.name}"



class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)


    def __str__(self):
        return f"{self.name}, {self.phone}"


class AddemailsBook(UserDict):

    def add_change_record (self, rec):
        self.data[rec.name.__str__()] = rec.__str__()
        if "None" in self.data.keys():
            self.data.pop("None")
    
    # def change_phone(self, rec):
    #     self.data[rec.name.__str__()] = rec.__str__()

    def find_phone(self, name):
        if name in self.data.keys():
            value = self.data[name]
            email = re.search(r'\+?\d+', value)
            return email.group()
        return 'No record in DB'

def main():
    main_addemails_book = AddemailsBook()
    while True:
        ask = input("What the hell do you want?: ")
        ask = ask.lower()
        cmd = ask.split(" ")
        if cmd[0] in ["good","close", ".", "exit"]:
            print ("Good bye")
            break
        elif cmd[0] in ["hello"]:
            print ("How can i help you?")
        elif cmd[0] in ["show"]:
            print(main_addemails_book)
        elif cmd[0] in ["phone"]:
            print(main_addemails_book.find_phone(cmd[1].title()))
        # elif cmd[0] in ["change"] and len(cmd) > 2:
        #     main_addemails_book.change_phone(Record(cmd[1].title(), cmd[2:]))
        elif cmd[0] in ["add"] or["change"] and len(cmd) > 2:
            main_addemails_book.add_change_record(Record(cmd[1].title(), cmd[2:]))
        else:
            print('Incorrect! Try again')
            

if __name__ == '__main__':
    main()
            

    



    

