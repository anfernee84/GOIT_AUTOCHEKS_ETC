# class Human:
#     name = ""
#     def voice(self):
#         print (f"Hello! My name is {self.name}")

# class Developer(Human):
#     field_description = "My programming language"
#     language = ""

#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"

# class PythonDeveloper(Developer):
#     value = "Python"


# class JSDeveloper(Developer):
#     value = "JS"

# first_dev = PythonDeveloper()
# first_dev.name = "Vasya"
# first_dev.voice()
# print(first_dev.make_some_code())
# second_dev = JSDeveloper()
# print(second_dev.make_some_code())


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return f"Meow"

cat = Cat("Simon", 10)
print(cat)



