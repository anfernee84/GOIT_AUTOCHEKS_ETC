import pickle


# def write_contacts_to_file(filename, contacts):
#     with open(filename, "wb") as fh:
#         pickle.dump(contacts, fh)
    
        


# def read_contacts_from_file(filename):
#     with open(filename, "rb") as fh:
#         return pickle.load(fh)



def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as f:
        pickle.dump(contacts, f)
        
def read_contacts_from_file(filename):
    with open(filename, 'rb') as f:
        data_new = pickle.load(f)
        return data_new