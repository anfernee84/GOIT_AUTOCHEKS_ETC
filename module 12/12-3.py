import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline="") as csvfile:
        fieldnames = ['name', 'email', "phone", "favorite"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)

      
def read_contacts_from_file(filename):
    with open(filename, "r", newline='') as fh:
        reader = csv.DictReader(fh)
        contacts = []
        for row in reader:
            contacts.append({"name":row["name"],
                             "email": row["email"],
                             "phone": row["phone"],
                             "favorite": False if row["favorite"] == "False" else True})
        return contacts



contacts = [
  {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
  {"name": "Vasya Pupkin", "email": "vasya.pupkine@pisem.net", "phone": "(050) 111-1111", "favorite": True}]


write_contacts_to_file('data.csv', contacts)
print(read_contacts_from_file('data.csv'))

