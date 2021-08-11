class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def info(self):
        return {"name": self.name,"age": self.age,"address": self.address}


class Cat(Animal):

    def __init__(self,nickname, weight, breed):
        self.breed = breed
        super().__init__(nickname, weight)


    def say(self):
        return f"Meow"

class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def who_is_owner(self):
        return Owner.info(self.owner)    

    def say(self):
        return f"Woof"




cat = Cat("Simon", 10, "british")
print(cat.nickname)
print(cat.breed)
print(cat.weight)




owner = Owner("Vasya", 33, "Vasilkovska str." )
dog = Dog("Barbos", 23, "labrador", owner)
print(dog.who_is_owner())
print(f"{dog.nickname} \n{dog.breed} \n{dog.weight}")