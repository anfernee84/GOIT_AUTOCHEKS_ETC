
def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a + b

if __name__ == "__main__":
    value = fib(10)
    print(
        list (value)
    )


class Fibiterator:

    def __init__(self.count):
        self.count = Counter
        self.generated_numbers = 0


    def __iter__(self):
        self.a = 0
        self.b = 1
        self.generated_numbers = 0
        return self

    def __next__(self):
        if self.generated_numbers <= self.count:
            yield self.a
            self.a,self.b = self.b, self.a + self.b
            self.generated_numbers += 1
        else:
            raise StopIteration

if __name__ == "__main__":
    fib_iter = Fibiterator(10)
    print (fib_iter.a)

