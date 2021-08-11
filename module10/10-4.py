# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

#     def how_many_people(self):
#         print (f" it`s {Person.count} people now")


# first = Person("Boris")
# first.how_many_people()
# second = Person("Onufriy")
# first.how_many_people()
# second.how_many_people()

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color
        print (f"Color is {Animal.color}")

first_animal = Animal("Barsik",4)
second_animal = Animal("Tobik", 6)
first_animal.change_color("red")
