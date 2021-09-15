import time

def TestTime(fn):
    def wrapper (*args, **kwargs):
        st = time.time()
        print(fn(*args,**kwargs))
        dt = time.time() - st
        return(f"work time {dt} seconds")
    return wrapper




@TestTime
def getNOD(a,b):
    while a != b:
        if a>b:
            a -= b
        else: b -= a
    return(a)


@TestTime
def hello():
    return f"Hello world"


print(getNOD(20000,1563))
print(hello())

