from copy import copy,deepcopy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_class = Person(copy(self.name), copy(self.email), copy(self.phone), copy(self.favorite))
        return copy_class

            
            
            
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_class = Contacts(copy(self.filename), copy(self.contacts))
        # copy_class.filename = copy(self.filename)
        # copy_class.contacts = copy(self.contacts)
        copy_class.is_unpacking = copy(self.is_unpacking)
        copy_class.count_save = copy(self.count_save)
        return copy_class
        
        

    def __deepcopy__(self, memo):
        deepcopy_class = Contacts(deepcopy(self.filename), deepcopy(self.contacts))
        memo[id(deepcopy_class)] = deepcopy_class
        # deepcopy_class.filename = copy.deepcopy(self.filename)
        # deepcopy_class.contacts = copy.deepcopy(self.contacts)
        deepcopy_class.is_unpacking = deepcopy(self.is_unpacking)
        deepcopy_class.count_save = deepcopy(self.count_save)
        
        
        return deepcopy_class
        
        
        