# import string

# class NameTooShortError(Exception):
#     pass


# class NameStartsFromLowError(Exception):
#     pass


# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError


# while True:
#     try :
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print("Name is too short")
#     except NameStartsFromLowError:
#         print ("Name sholud start from cap")

class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith ("01"):
        id_list.append(employee_id)
    else:
        raise IDException
    return id_list

