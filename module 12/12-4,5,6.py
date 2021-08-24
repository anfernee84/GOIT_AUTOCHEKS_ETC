import pickle



class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite   
        
        
    


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False


    def save_to_file(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self, f)
        
            

    def read_from_file(self):
        with open(self.filename, 'rb') as f:
            data_new = pickle.load(f)
        return data_new

    def __getstate__(self):
        d = self.__dict__.copy()
        d["count_save"] += 1
        return d
    
    def __setstate__(self, value):
        self.__dict__ = value
        value["is_unpacking"] = True
    
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)

persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()
third.save_to_file()

print(persons.count)
print(first.count)
print(second.count)
print(third.count)
print(persons.__dict__)