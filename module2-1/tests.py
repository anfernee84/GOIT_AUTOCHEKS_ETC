# ExampleClass = type("ExampleClass", (object,), {"somevar": "vasya"})
# print(ExampleClass.__name__)
# print(ExampleClass.somevar)


# a = ExampleClass()
# print(a.somevar)
# print(a.__str__)
# print(type(a))

# def meta_func(name, args, kwargs):
#     print("metafunction with", name, args, kwargs)
#     kwargs["somedata"] = 42
#     return type(name,args,kwargs)

# class Kls(metaclass = meta_func):
#     some = 2
#     def printsome(self):
#         print(self.some)

# print(Kls.somedata)


# class MyMeta(type):
#     def __new__(*args):
#         print(f"MyMeta __new__ called with {args}")
#         return type.__new__(*args)

#     def __init__(*args):
#         print(f"MyMeta __init__ called with {args}")

# class A(metaclass = MyMeta):
#     def __init__(self, data) -> None:
#         self.data = data        

from abc import abstractmethod, ABCMeta
class MyBaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def baz(self):
        pass


class Child(MyBaseClass):
    print(f"im a childo")


c = Child() 