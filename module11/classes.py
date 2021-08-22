class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print (f"Dog {self.name} created")

    def sit(self):
        return f"Dog {self.name} sat"

    def jump(self):
        return f"Dog {self.name}, {self.age} jumped"
    def __len__(self):
        return len(self.name)



dog = Dog("Vasya",3)
print(dog.jump())
print(dog.sit())
print(dog.__len__())
dogg = Dog("Chupakabra", 7)
print(dogg.jump())
print(getattr(dog, "name"))
setattr(dogg, "age", 25)
print(dogg.jump())
setattr(Dog, "weight", 15)
print(dogg.weight)
print (Dog.__dict__)
print (dog.__dict__)
print (dogg.__dict__)

class SomeClass:
    
    def __init__(self, val):

        self._val = val
    
    def __mul__(self, numb):
        return self._val * numb
    
    def _private(self):
        return f"{self._private} is an inside method"
    
    def __hidden(self):
        return f"{self.__hidden} is a hidden method"
    
    def getval(self):
        try:
            return self._val if True else None
        except:
            AttributeError
            return None
    
    def setval(self, val):
        self._val = val
  
    def delval(self):
        del self._val
    
    # def __getattribute__(self, name: str):
    #     return name.upper
    
    val = property(getval, setval, delval, "Value arrributes")

# digit = SomeClass(4)
# print(digit * 4)
# print(digit.__mul__(4))
# print(digit._private())
# print(digit._SomeClass__hidden())
# digit.val = 5
# print(digit * 4)
# print(digit.getval())
# digit.delval()
# print(digit.getval())
# digit.val = 3876
# print(digit.getval())



class GetAttr:
    def __init__(self, attr):
        self.attr = attr

    def __getattribute__(self, attr):
        return attr.upper() * 2

obj = GetAttr(5)
print(obj.attr5)

class Salary:
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)
    
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)
    def annualSalary(self):
        return f"Total: {self.salary.getTotal() + self.bonus}"

Onufriy = Employee(100,10)
print(Onufriy.annualSalary())

class Parent:
    def __init__(self):
        print(f"Parent init")
    def method(self):
        return f"Parent method"
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
    def method(self):
        return super(Child,self).method()

child = Child()
print(child.method())
        
class English:
    def greeting(self):
        print ("Helo")

class Russian:
    def greeting(self):
        print ("Cho nada?")

def intro(lamguage):
    lamguage.greeting()

john = English()
vasya = Russian()
intro(john)
intro(vasya)

# class Point3D:
#     """123"""
    
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

# print (Point3D.__doc__, "\n")
# a = Point3D(1,2,3)
# setattr(Point3D,"y",888)
# b = Point3D(4,5,6)
# print(a.x,a.y,a.z)
# print(b.x,b.y,b.z)
# print(getattr(a,"z",None))
# setattr(b,"x",159)
# print(b.__dict__)
# print(b.__dict__)

class Point3D:
    def __init__ (self,x,y,z):
        self.coordinates = (x,y,z)
    def setcoordinates(self, x,y,z):
        self.coordinates = (x,y,z)
    def getcoordinates(self):
        return self.coordinates
a = Point3D(1,2,3)
print(a.getcoordinates())
a.setcoordinates(4,5,6)
print(a.getcoordinates())
setattr(a, "y", 159)
print(a.__dict__)
        
    