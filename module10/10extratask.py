# class Human:
#     counter = 0


#     def __init__(self, name):
#         self.name = name
#         Human.counter += 1

#     def how_many_persons(self):
#         return  f"the total amount of person is {Human.counter}"


# if __name__ == "__main__":
#     first = Human("Adam")
#     print (first.counter)
#     print (first.how_many_persons())

#     second = Human("Eve")
#     print (second.counter)    
#     print (second.how_many_persons())





# def flatten(items):
#     if len(items) == 0:
#         return []
#     item = items[0]

#     if not isinstance (item, list):
#         return [item] + flatten(items [1:])
#     return flatten (item) + flatten(items [1:])
        

# if __name__ == "__main__":
#     items = [1,2,3,[4,5],6,7,[8,9,10,11,12],[[[6,3,2,1],6,8,9,0,4,3]]]
#     print(flatten(items))

# def main ():
#     data = {
#         "first_name": "Sam",
#         "second_name": "Brown",
#         "age":45
#     }

#     with open("data.txt","w") as f:
#         f.write (
#             ",".join ([
#                 data["first_name"],
#                 data["second_name"],
#                 str(data["age"])
#                 ])
#             )

# if __name__ == "__main__":
#     main()


# from hero import *

# myhero1 = Hero("Vasya", 12, "urkagun")
# myhero2 = SuperHero("Onufriy", 14, "buhar", 5)

# myhero1.show_hero()
# myhero2.show_hero()
# myhero2.makemagic()
# myhero2.show_hero()



# class Meta(type):
#     classes = []
#     def __new__(cls, name, bases, attrs):
#         cls.classes.append({"cls":cls, "name" : name, "number": len(cls.classes) })
#         return type.__new__(cls, name, bases, attrs)

# class User(metaclass = Meta):
#     def __init__(self):
#         print("Constructor")
#         super().__init__()

# class User2(metaclass = Meta):
#     pass        


# user = User()
# print(Meta.classes)



# class DeveloperMeta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs["skill"] = "Python"
#         attrs["city"] = None
#         attrs["method1"] = DeveloperMeta.method1
#         return type.__new__(cls,name,bases,attrs)
#     def method1(cls):
#         print("asd")



# class Developer(metaclass = DeveloperMeta):
#     pass

# dev = Developer()
# print(dev.skill)

# dev.method1()

# import abc

# class DevOps(abc.ABC):

#     @property
#     @abc.abstractmethod
    
#     def skill(self):
#         return skill

# class PythonDeveloper(DevOps):
#     skill = "Python"



# dev = PythonDeveloper()
# print(dev.skill)
# print(dev.__dict__)


# class NotInplemented(Exception):
#     pass


# class AbstractClassMeta(type):
#     abstract_methods = []

#     def __new__(cls, name, bases, attrs):
#         #print (cls, name, bases, attrs )
#         if not bases:
#             for key,value in attrs.items():
#                 if callable (value):
#                     AbstractClassMeta.abstract_methods.append(key)

#                 else:
#                     for abstract_method in AbstractClassMeta.abstract_methods:
#                         if abstract_method not in attrs:
#                             raise NotImplemented (f"Method {abstract_method} is not implemented")


#         return type.__new__(cls, name, bases, attrs)

        
    

# class AbstractClass(metaclass = AbstractClassMeta):
    
#     def method(self):
#         pass

# class A(AbstractClass):
#     pass




user_info = {"name":"Alex", "last_name": "Pupkin", "nickname":"pupok"}
models = {}
class ModelMeta(type):
    def __new__(cls,name,bases,attrs):
        
        obj = type.__new__(cls,name,bases,attrs)

        models[name]  = obj
        return obj

    def __call__(cls,user_info):

        for k, v in user_info.items():
            if k in cls.__dict__:
                setattr(cls, k, v)
        return type.__call__(cls)
        
class Model(metaclass = ModelMeta):
    pass


class UsersPII(Model):
    name = None
    last_name = None
    # def __init__(self, user_info):
    #     pass

users_pii = UsersPII(user_info)

print(users_pii.last_name)


from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def parentmethod(self):
        print (f"I`m your father")
    @abstractmethod
    def abstractfunction(self):
        pass

    @abstractmethod
    def mathfunction(self):
        pass

class ChildMEthod(AbstractClass):
    def abstractfunction(self):
        print (f"I`m a child")
    def mathfunction(self,x,y):
        self.x = x
        self.y = y
        print(int(x)+int(y))
        return self.x + self.y

a = ChildMEthod()
a.parentmethod()
a.abstractfunction()

print(a.mathfunction(2,6))


ExampleClass = type("ExampleClass", (object,), {"class_var": "some_digit"})
e = ExampleClass()
print(e.__dir__)
print(e.class_var)
print(ExampleClass.__name__)
print(ExampleClass.__dict__)


def metafunc(name,bases,attrs):
    print ("metafunc called with", name,bases,attrs)
    attrs["somedata"] = 5
    return type(name,bases,attrs)

class Cls(metaclass = metafunc):
    some = 2

    def print_some(self):
        print(self.some)

print(Cls.some)
print(Cls.somedata)
print(Cls.__dict__)


class MyMeta(type):

    # def __new__(cls,name,bases,attrs):
    #     print(f"MyMeta new called with {cls},{name}, {bases}, {attrs}")
    #     return type.__new__(cls,name,bases,attrs)

    def __call__(cls, *args):
        print("call called")
        print("class:", cls)
        # print("name: ", name)
        # print("bases:", bases)
        print("attrs: ", *args)
        instance = object.__new__(cls)
        instance.__init__( *args)
        return instance





    
    # def __init__(cls,name,bases,attrs):
    #     print (f"MyMeta init attrs {cls},{name}, {bases}, {attrs}")

class A(metaclass = MyMeta):
    def __init__(self,data):
        self.data = data
        print(f"i`m a A method __init__")
    def printd(self):
        print(self.data)

a = A("arun")


from abc import abstractmethod, ABCMeta

class BaseMeta(metaclass = ABCMeta):
    
    @abstractmethod
    def func1(self):
        print ("i`m a func1")
    @abstractmethod
    def func2(self):
        print ("I`m a func2")


class Child(BaseMeta):
    
    # def func1(self):

    #     print("func1")

    # def func2(self):
    #     print("func2")
    def func1(self):
        return super().func1()

    def func2(self):
        return super().func2()
    


c = Child()

c.func1()
c.func2()


def class_decor(clas):
    class Inner(clas):
        def print_hello(self):
            print("hello")
    return Inner

@class_decor
class Z:
    pass

z = Z()
z.print_hello()
print(z)


class Decorator:
    def __init__(self, maxval, minval):
        self.maxval = maxval
        self.minval = minval
    
    def __call__(self,func):
        def inner (*args):
            for arg in args:
                if arg < self.minval or arg > self.maxval:
                    raise ValueError
            return (func, *args)
        return inner

@Decorator(0,5)
def foo(x,y):
    pass

@Decorator(-5,6)
def bar(g,y):
    pass

def dump_closure(f):
   if hasattr(f, "__closure__") and f.__closure__ is not None:
       print("- Dumping function closure for {}:".format(f.__name__))
       for i, c in enumerate(f.__closure__):
           print("-- cell {}  = {}".format(i, c.cell_contents))
   else:
       print(" - {} has no closure!".format(f.__name__))

dump_closure(classmethod)







