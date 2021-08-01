import re

CONTACTS = {}

def main():
    while True:
        ask = input("What the hell are you want?: ")
        ask = ask.lower()
        cmd = ask.split(" ")
        if cmd[0] in ["good","close", ".", "exit"]:
            print ("Good bye")
            break
        elif cmd[0] in ["hello"]:
            print ("How can i help you?")
        elif cmd[0] in ["show"]:
            print(hdl_showall())
        elif cmd[0] in ["phone"]:
            hdl_phone(cmd[1].title())
        elif cmd[0] in ["change"] and len(cmd) > 2:
            hdl_change(cmd[1].title(), cmd[2])
        elif cmd[0] in ["add"] and len(cmd) > 2:
            hdl_add(cmd[1].title(), cmd[2])


def input_errors(func):
    def wrapper(*args):
        if len(args) <= 2 and len(args) > 1:
            result = re.search(r'\+?380\d+|0\d+', args[1])
            if not args[0].isalpha():
                print ("Enter correct name")
            if result:    
                if len(args[1]) < 10:
                    if len(args[1]) != len(result.group()):
                        print("Enter right number")
                else:
                    func (args[0], args[1])
            else:
                print ("Enter correct number")
        else:    
            if not args[0] in CONTACTS.keys():
                print("There`s no such contact")
            else:
                print (func(args[0]))
    return wrapper


def hdl_showall():
    return CONTACTS


@input_errors
def hdl_phone(name):
    return CONTACTS[name]


@input_errors
def hdl_change(name, phonenumber):
    CONTACTS[name] = phonenumber

@input_errors
def hdl_add(name, phonenumber):
    CONTACTS[name] = phonenumber



            
main()