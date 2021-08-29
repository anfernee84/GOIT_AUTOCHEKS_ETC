import re
import difflib

class Validator:
    def __init__(self, **k):
        self.meth = k['meth']
        self.phone = k['phone']
        self.email = k['email']

    def check_method(self):
        com_dict = { 1: "Add", 2: "Show", 3: "Change", 4: "Delete"}
        for value in com_dict.values():
            ratio = int(difflib.SequenceMatcher(None, self.meth, value).ratio()*100)
            if ratio > 50:
                fixed_string = value[0].upper()+value[1:]
                return f"{fixed_string}"
            elif ratio < 50:
                continue
        return f"Command {self.meth} was not identified"

    def check_phone(self):
        regex = re.compile("(\+?(38)?0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7})")
        if not re.search(regex, self.phone):
            print(re.search(regex, self.phone))
            return 'phone invalid'
        else:
            return self.phone

    def check_email(self):
        regex = "[a-zA-Z\.-]+@[\w\.-]+"
        if not re.search(regex, self.email):
            return 'email_invalid'
        else:
            return self.email
v = Validator(meth='dda',phone='+3805055555444325',email='roottt@dfddd')
v.check_method()
v = Validator(meth='chge',phone='+3805055555522325',email='roottt@dfddd.net')
print(v.check_method()) 
print(v.check_phone())
print(v.check_email())



