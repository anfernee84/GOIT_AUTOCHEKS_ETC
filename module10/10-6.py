class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):

    def __init__(self,nickname, weight, breed):
        self.breed = breed
        super().__init__(nickname, weight)


    def say(self):
        return f"Meow"

class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        self.breed = breed
        super().__init__(nickname, weight)

    def say(self):
        return f"Woof"




cat = Cat("Simon", 10, "british")
print(cat.nickname)
print(cat.breed)
print(cat.weight)

dog = Dog("Barbos", 23, "labrador")
print(f"{dog.nickname} \n{dog.breed} \n{dog.weight}")