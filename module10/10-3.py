class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
      
    def change_weight(self, weight):
        self.weight = weight

    
        


animal = Animal("Simon", 10)
animal.change_weight(12)


# class Human:
#     name = ""
#     def voice(self):
#         print (f"My name is {self.name}")
    
# class Developer (Human):
#     fiels_description = "My programming language"
#     language = ""
#     def make_some_code(self):
#         return f"{self.fiels_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"


# class JavaDeveloper(Developer):
#     value = "JS"


# pydev = PythonDeveloper()
# pydev.name = "Anufriy"
# pydev.voice()
# print(pydev.make_some_code())

# jsdev = JavaDeveloper()
# print(jsdev.make_some_code())