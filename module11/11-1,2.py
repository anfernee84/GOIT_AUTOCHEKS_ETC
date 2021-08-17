class Human:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    
    # def say_hello(self):
    #     return f"Hello, {self.name}"

    def __str__(self):
        return f"Hello, {self.name}"


bill = Human("Bill", 45)
bill_str = str(bill)
print(bill_str)


# -----------/ Task 11-1 /--------------------
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __repr__ (self):
        return f"Point ({self.x}, {self.y})"

a = Point(2, 4)

class ListedValuesDict:
    def __init__ (self):
        self.data = {}

    def __setitem__ (self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]
        print(self.data)
    
    def __getitem__ (self, key):
        result = str(self.data[key][0])
        print(result)
        
        for val in self.data[key][1:]:
            result += ", " + str(val)
            print(result)
        return result

ldict = ListedValuesDict()
ldict[1] = "a"
ldict[1] = "b"
print(ldict[1])


class Adder():
    def __init__ (self, add_value):
        self.add_value = add_value

    def __call__ (self, value):
        return self.add_value + value

two_adder = Adder(2)
print(two_adder(5))
print(two_adder(4))

class Session():
    def __init__(self, addr, port = 8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f"Connected to {self.addr}, {self.port}")
        return self

    def __exit__ (self, exception_type, exception_value, traceback):
        self.connected = False
        if exception_type is not None:
            print ("Some error!")
        else:
            print ("No problem")


localhost_session = Session("localhost")
with localhost_session as session:
    print(session is localhost_session)
    print(localhost_session.connected)

with Session("localhost") as session:
    print(session.connected)

class Iterable:
    MAX_VALUE = 10
    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration

class CustomIterator():
    def __iter__ (self):
        return Iterable()

c = CustomIterator()
for i in c:
    print (i)

    
class Secret:
    public_field = "This is visible"
    _private_field = "Do not touch me!"
    __real_secret = "You cannot see me!"

s = Secret()

print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)


class PositiveNumber:
    def __init__ (self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print ("Only numbers greater zero accepted")

p = PositiveNumber()
p.value = 1
print(p.value)
p.value = -1
print (p.value)
p._PositiveNumber__value = -1
print(p.value)

# ---------------/ Task 11-2 /---------------
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):        
        return self.__x

    @property
    def y(self):
        return self.__y
       
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self.__y = new_y
a = Point(2, 4)
print(a.x)


