# class Mammal:
#     phrase = ""
#     def voice(self):
#         return self.phrase

# class Dog(Mammal):
#     phrase = "Bark"

# class Cat(Mammal):
#     phrase = "Meow"

# class Chupakabra:
#     def voice(self):
#         return "Whooooooo"

# class Recorder:
#     def record_animal(self,animal):
#         voice = animal.voice()
#         print(f"Recorded '{voice}'")

# r = Recorder()
# cat = Cat()
# dog = Dog()
# unknown_animal = Chupakabra()

# r.record_animal(cat)
# r.record_animal(dog)
# r.record_animal(unknown_animal)


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
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Meow"

    def change_weight(self, weight):
        self.weight = weight
