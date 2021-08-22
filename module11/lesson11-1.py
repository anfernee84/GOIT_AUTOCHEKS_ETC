# class OpenFile:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.filehandler = None

    
#     def __enter__(self):
#         self.filehandler = open(self.filename, self.mode)
#         return self.filehandler

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.filehandler.close()



    
# if __name__ == "__main__":
#     with OpenFile("data.txt", "r") as f:
#         print(f.read())


def fib (n):
    a,b = 0,1
    for _ in range (n):
        yield b
        a,b = b, a+b


class Fibiterator:
    
    def __init__(self,count):
        self.count = count
        self.generated_numbers = 0

    
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.generated_numbers = 0
        return self

    def __next__(self):
        if self.generated_numbers > self.count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.generated_numbers += 1
        return self.a
            

    
if __name__ == "__main__":
    for item in Fibiterator(10):
        print (item)

    print (list(Fibiterator(10)))
    print ([x for x in Fibiterator(10) if x < 13])



class Circle:
    def __init__(self, x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def __repr__(self) -> str:
        return f"Circle({self.x}, {self.y})"

if __name__ == "__main__":
    c = Circle(2,4,5,"red")
    print(c)
    

class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)   

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    a = Vector(0,0)
    b = Vector(1,1)
    
    c = a + b
    print(c)
    