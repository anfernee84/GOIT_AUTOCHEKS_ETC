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
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        self.data = {0:self.coordinates.x, 1:self.coordinates.y}

    def __setitem__(self, index, value):
        self.data[index] = value  
            
          

    def __getitem__(self, index):
        return self.data[index]
        
v = Vector(Point(1,10))
print(v[0] == 1)            
        
           