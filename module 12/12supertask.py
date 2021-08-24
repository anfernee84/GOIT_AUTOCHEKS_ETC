from collections import UserDict
import re
from datetime import datetime
import pickle


class Phone:
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        flag = False
        res = re.search(
            r"(\+?(38)?0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7})", phone
        )
        if res:
            flag = True
            self.__phone = res.group()
        if not flag:
            print("Incorrect phone!")

    def __str__(self):
        return f"{self.__phone}"


class Name:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print("Incorrect name!")

    def __str__(self):
        return f"{self.__name}"


class Birthday:
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        flag = False
        date = birthday.split(".")
        if len(date) == 3:
            if int(date[0]) <= 31 and int(date[1]) <= 12:
                res = re.search(r"\d{1,2}\.\d{1,2}\.\d{4}", birthday)
                if res:
                    flag = True
                    self.__birthday = datetime.strptime(res.group(), "%d.%m.%Y")
        if not flag:
            print(
                "Incorrect date or format!\nTry to enter like the example: DD.MM.YYYY"
            )

    def __str__(self):
        if self.__birthday:
            return f"{self.__birthday.date()}"
        return "None"

    def __repr__(self):
        if self.__birthday:
            return f"{self.__birthday.date()}"
        return "None"


class Record:
    def __init__(self, name, phone, birthday):
        self.name = Name(name)
        self.phone = Phone(phone)
        if birthday:
            self.birthday = Birthday(birthday).__str__()
        else:
            self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday != "None" and self.birthday:
            date_now = datetime.now()
            birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
            birth_date = birth_date.replace(year=date_now.year)
            if (birth_date - date_now).days < 0:
                birth_date = birth_date.replace(year=birth_date.year + 1)
                return (birth_date - date_now).days
            return -(date_now - birth_date).days

    def __str__(self):
        if self.birthday:
            return f"{self.name},{self.phone},{self.birthday}"
        if self.phone.__str__() == "None":
            return None
        return f"{self.name},{self.phone}"


class AddressBook(UserDict):
    def add_record(self, rec):
        if rec.phone.__str__() != "None":
            self.data[rec.name.__str__()] = rec.__str__()
            if "None" in self.data.keys():
                self.data.pop("None")

    def change_phone(self, rec):
        if (
            rec.name.__str__() in self.data.keys()
            and len(self.data[rec.name.__str__()].split(",")) == 3
            and len(rec.__str__().split(",")) == 2
        ):
            sep_values = self.data[rec.name.__str__()].split(",")
            self.data[rec.name.__str__()] = rec.__str__() + "," + sep_values[2]
        else:
            self.data[rec.name.__str__()] = rec.__str__()

    def find_phone(self, name):
        if name in self.data.keys():
            value = self.data[name]
            res = re.search(r"\+?\d+", value)
            return res.group()
        return "Does not exist in database!"

    def find_anything(self, searching_param):
        print("Results of searching:")
        for key, value in self.data.items():
            if value.lower().find(searching_param.lower()) != -1:
                print(f"{key}:{value}")

    def __iter__(self):
        self.val_dict = [0] + [i for i in self.data.values()]
        self.count_iter = 0
        return self

    def __next__(self):
        if len(self.val_dict) - 1 != self.count_iter:
            self.count_iter += 1
            return self.val_dict[self.count_iter]
        raise StopIteration


def main():
    try:
        with open("data_test.bin", "rb") as f:
            main_address_book = pickle.load(f)
    except FileNotFoundError:
        main_address_book = AddressBook()
    while True:
        command = input("Command: ").lower()
        sep_val = command.split(" ")
        if sep_val[0] == "add" and len(sep_val) > 2:
            main_address_book.add_record(
                Record(
                    sep_val[1].title(),
                    sep_val[2],
                    sep_val[3] if len(sep_val) == 4 else None,
                )
            )

        elif sep_val[0] == "change" and len(sep_val) > 2:
            main_address_book.change_phone(
                Record(
                    sep_val[1].title(),
                    sep_val[2],
                    sep_val[3] if len(sep_val) == 4 else None,
                )
            )

        elif sep_val[0] == "phone":
            print(main_address_book.find_phone(sep_val[1].title()))

        elif sep_val[0] == "show" and sep_val[1] == "all":
            print(main_address_book)

        elif sep_val[0] == "iter" and len(sep_val) > 1:
            iter_for_book = iter(main_address_book)
            if len(main_address_book) < int(sep_val[1]):
                print(
                    f"Maximum possible iterations are {len(main_address_book)} instead of {int(sep_val[1])}!\n"
                    f"Please try again!"
                )
                continue
            for i in range(int(sep_val[1])):
                print(next(iter_for_book))
        elif sep_val[0] == "find" and len(sep_val) == 2:
            main_address_book.find_anything(searching_param=sep_val[1])
        elif sep_val[0] in ["good bye", "close", "exit", "."]:
            with open("data_test.bin", "wb") as file:
                pickle.dump(main_address_book, file)
            print("Good bye!")
            break
        elif sep_val[0] == "hello" or sep_val[0] == "help":
            print(
                "How can I help you?\nThe list of available commands:\n"
                '"add [name] [phone] [birthday](optional)" - adding the user to the Addressbook;\n'
                '"change [name] [phone] [birthday](optional)" - change the existing contact;\n'
                '"phone [name]" - find the phone of user;\n'
                '"show all" - show all of the contacts in the Addressbook;\n'
                '"iter [iterations]" - iterating the Addressbook;\n'
                '"good bye, close, exit, ." - exit the CLI-bot'
            )
        else:
            print("Incorrect! Try again")


if __name__ == "__main__":
    main()