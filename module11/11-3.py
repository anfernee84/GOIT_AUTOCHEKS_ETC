# class Person:
#     def __init__(self, name):
#         self.__name = None
#         self.name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         if (type(name) == str) and (len(name) > 0):
#             self.__name = name


# person = Person(123)
# print(person.name)  # None


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int or type(x) == float):
            self.__x = x
        
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int or type(y) == float):
            self.__y = y



a = Point("hj", 4)
print(a.x)