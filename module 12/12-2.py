import json


def write_contacts_to_file(filename, contacts):
  with open(filename, "w") as fh:
    json.dump({'contacts': contacts}, fh)
    
        
def read_contacts_from_file(filename):
  with open(filename, "rb") as fh:
    unpacked = json.load(fh)
    return unpacked["contacts"]


contacts = [
  {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
  {"name": "Vasya Pupkin", "email": "vasya.pupkine@pisem.net", "phone": "(050) 111-1111", "favorite": True}]


write_contacts_to_file("data.json", contacts)
print(read_contacts_from_file("data.json"))