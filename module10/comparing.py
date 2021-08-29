import difflib

def compare(command_string):    
    command_split = command_string.split()
    com_dict = { 1: "Add", 2: "Show", 3: "Change", 4: "Delete"}
    for value in com_dict.values():
        ratio = int(difflib.SequenceMatcher(None, command_split[0], value).ratio()*100)
        if ratio > 50:
            fixed_string = value[0].upper()+value[1:] + " " + " ".join(str(item) for item in command_split[1:])
            return f"{fixed_string}" 
        elif ratio < 50:
            continue
    return f"Command {command_split[0]} was not identified"
            

print(compare("letD Vasya 0961111111 vasya@mail.net"))

 

