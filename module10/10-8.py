# class A:
#     x= "i`m A class"

# class B:
#     x = "i`m B class"
#     y = "I exist only in B"

# class C(B,A):
#     z = "Thisd exists only in C"

# per = C()

# print(per.z)
# print(per.y)
# print(per.x)

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat,Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"



class DogCat(Dog,Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


catdog = CatDog("Simon", 10)
print (catdog.say())    
dogcat = DogCat("Barsik", 4)
print (dogcat.say())

print (dogcat.info())
print (catdog.info())