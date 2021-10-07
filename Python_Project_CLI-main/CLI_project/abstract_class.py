from abc import ABC, abstractmethod
from collections import UserDict
from datetime import timedelta, date, datetime
import re
import time
from address_book import Name, Phone, Email, Birthday, Address, Record
from notes import NoteRecord


class AbstractClass(ABC):

    @abstractmethod
    def show_info():
        pass

    # @abstractmethod    
    # def add():
    #     pass
    
    # @abstractmethod
    # def edit():
    #     pass


class aAddressBook(AbstractClass,UserDict):

    def show_info(usrDict,name):
        for key, value in usrDict.items():
            if str(name) == str(key):
                print (f"{key}: {value}")

class aBirthday(AbstractClass):

    def show_info(self, number_days):
        EndDate = date.today() + timedelta(days=number_days)
        list = []
        try:
            for key, val in self.data.items():
                result = re.search(r"\d{1,2}\/\d{1,2}\/\d{4}", str(val)).group()
                if datetime.strptime(result, "%d/%m/%Y").month == EndDate.month \
                        and datetime.strptime(result, "%d/%m/%Y").day == EndDate.day:
                    list.append({str(key): str(val)})
        except AttributeError:
            pass
        return list


class aShowAll(AbstractClass):
    def show_info(self):
        print(f'Total contacts: {len(self.data)}')
        for key, val in self.data.items():
            print(f'{str(key)}:{str(val)}'.removesuffix(','))


class aNotes(AbstractClass):
    def show_info(note_list):
        print(f"Total notes: {NoteRecord.counter}")
        if not note_list:
            print("List with notes is empty!")
        for note in note_list:
            print(f"Title: {note['title']}\nNote: {note['note']}\nTags: {note['tag']}\n")
        



class aHelp(AbstractClass):
    def show_info():
        """
        =====================================================
                    CLI - Command Line Interface
                        Personal Assistant
        =====================================================
        Personal Assistant works with Address book, write,
        save Notes and sort files in folders.
        Personal Assistant has a commands:
        1. "add contact" - for add name, address, contact
        information (phone, e-mail) and birthday to Address
        book write "add contact" then details and enter it;
        2. "add note" - for add note write "add note" then
        your note after write "-title" and title for your note
        and enter it; additionally in this option you can add
        a tag to your note for this after title write "-tag"
        and tag and enter it;
        3. "add tag" - for add tag to notes write "add tag"
        then write tag after write "-title" and title of note
        which you wont to add tag and enter it;
        4. "show contact" - for get all contact information
        write "show contact" then name and enter it;
        5. "show birthday" - for show a list of contacts who
        have a birthday after a specified number of days from
        the current date write "show birthday" then number of
        days and enter it;
        6. "show all" - for show all contacts in Address book
        write "show all" and enter command;
        7. "show notes" - for show all notes write "show notes"
        and enter it;
        8. "edit contact" - for edit contact information write
        "edit contact" then name and enter it;
        9. "edit note" - for edit note write "edit note" then
        title after write "-edit" and new text and enter it;
        10. "search tags" - for search and sort notes by tags
        write "search tags" then tag and enter it;
        11. "search note" - for search note in notes write
        "search note" then few words from note and enter it;
        12. "sort folders" - for sort files in folders write
        "sort folders" then path to folder and enter it;
        13. "delete contact" - for delete name and contact
        information in Address book write "delete contact" then
        name and enter it;
        14. "delete note" - for delete note write "delete note"
        then title and enter it;
        15. "help", "reference" - for ask reference how to
        use Personal Assistant write "help" or "reference"
        and enter the command;
        16. "close", "exit", "good bye" - for finish work with
        Personal Assistant, write one of "close", "exit" or
        "good bye" and enter command then you will exit from
        Command Line Interface.
        Pleasant use!
        """
        print(aHelp.show_info.__doc__)